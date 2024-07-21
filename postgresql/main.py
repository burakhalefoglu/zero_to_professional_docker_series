import os
import psycopg2

POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]


# Veritabanı bağlantısı kurma fonksiyonu
def get_connection():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return conn

# Veritabanı tablo oluşturma fonksiyonu
def create_user_table_if_not_exists():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS
        users (id SERIAL PRIMARY KEY, name VARCHAR(100), surname VARCHAR(100))""")
    conn.commit()
    cur.close()
    conn.close()

# CREATE: Yeni bir kullanıcı ekleme fonksiyonu
def create_user(name, surname):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, surname) VALUES (%s, %s) RETURNING id", (name, surname))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

# READ: Tüm kullanıcıları listeleme fonksiyonu
def read_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# READ: Belirli bir kullanıcıyı id ile bulma fonksiyonu
def read_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

# UPDATE: Kullanıcı bilgilerini güncelleme fonksiyonu
def update_user(user_id, name, surname):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s, surname = %s WHERE id = %s", (name, surname, user_id))
    conn.commit()
    cur.close()
    conn.close()

# DELETE: Kullanıcı silme fonksiyonu
def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_user_table_if_not_exists()
    user_1 = create_user("Burak", "Halefoplu")
    new_user_id = create_user("Ahmet", "Mehmet")
    print(f"Created user with ID: {new_user_id}")

    users = read_users()
    print("All users:", users)

    user = read_user_by_id(new_user_id)
    print(f"User with ID {new_user_id}:", user)

    update_user(new_user_id, "Burak", "Halefoplu")
    updated_user = read_user_by_id(new_user_id)
    print(f"Updated user with ID {new_user_id}:", updated_user)

    delete_user(new_user_id)
    users_after_deletion = read_users()
    print("All users after deletion:", users_after_deletion)