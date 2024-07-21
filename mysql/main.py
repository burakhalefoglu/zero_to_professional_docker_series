import os
import mysql.connector as ct


MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_PORT = os.environ["MYSQL_PORT"]
MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_DB = os.environ["MYSQL_DB"]


# Veritabanı bağlantısı kurma fonksiyonu
def get_connection():
    conn = ct.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return conn


# Veritabanı tablo oluşturma fonksiyonu
def create_user_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT, name VARCHAR(100), surname VARCHAR(100), PRIMARY KEY (id))"
    )
    conn.commit()
    cursor.close()
    conn.close()


# Veri ekleme fonksiyonu
def create_user(name, surname):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", (name, surname))
    user_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return user_id

# Veri okuma fonksiyonu
def read_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


# veri güncelleme fonksiyonu
def update_user(user_id, name, surname):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, surname = %s WHERE id = %s", (name, surname, user_id))
    conn.commit()
    cursor.close()
    conn.close()

# Veri silme fonksiyonu
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_user_table_if_not_exists()
    user_id = create_user("Burak", "Halefoglu")
    user_2_id = create_user("Ahmet", "Mehmet")
    print(read_user_by_id(user_id))
    print(read_user_by_id(user_2_id))
    update_user(user_2_id, "Ahmet", "Halefoglu")
    delete_user(user_2_id)
    print(read_user_by_id(user_2_id))