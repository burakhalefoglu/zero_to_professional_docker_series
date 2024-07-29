import os
import pymongo

MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")

def get_connection():
    # mongodb://<username>:<password>@<host>:<port>
    connection_string = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
    client = pymongo.MongoClient(connection_string)
    db = client[MONGO_DB]
    col = db["users"]
    return col

# CRUD

## create
def create_user(name:str, surname:str) -> str:
    col = get_connection()
    user_dic = {"name": name, "surname": surname}
    result = col.insert_one(user_dic)
    return result.inserted_id

## read
def get_user(user_id:str) -> dict:
    col = get_connection()
    result = col.find_one({"_id": user_id})
    return result

## update
def update_or_crate(user_id: str, name: str, surname: str):
    col = get_connection()
    result = col.update_one({"_id": user_id}, {"$set": {"name": name, "surname": surname}})
    return result.upserted_id

## delete
def delete_user(user_id: str):
    col = get_connection()
    result = col.delete_one({"_id": user_id})
    return result

if __name__ == "__main__":
    inserted_id = create_user("Burak", "Halefoğlu")
    inserted_id_2 = create_user("Ahmet", "Halefoğlu")
    print("eklenen veriler id'si", inserted_id, inserted_id_2)

    user1 = get_user(inserted_id)
    print(user1)

    user2 = get_user(inserted_id_2)
    print(user2)

    update_or_crate(inserted_id_2, "Hasan", "KARACA")
    user2 = get_user(inserted_id_2)
    print(user2)

    delete_user(inserted_id_2)
    user2 = get_user(inserted_id_2)
    print(user2)
