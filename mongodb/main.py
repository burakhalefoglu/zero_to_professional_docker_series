import os
import pymongo


MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_DB = os.environ["MONGO_DB"]
MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]

def get_connection():
    client = pymongo.MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")
    db = client[MONGO_DB]
    mycol = db["users"]
    return mycol

def create_user(name, surname):
    mycol = get_connection()
    mydict = {"name": name, "surname": surname}
    x = mycol.insert_one(mydict)
    return x.inserted_id

def update_user(user_id, name, surname):
    mycol = get_connection()
    myquery = {"_id": user_id}
    newvalues = {"$set": {"name": name, "surname": surname}}
    mycol.update_one(myquery, newvalues)

def delete_user(user_id):
    mycol = get_connection()
    myquery = {"_id": user_id}
    mycol.delete_one(myquery)

def read_user_by_id(user_id):
    mycol = get_connection()
    myquery = {"_id": user_id}
    mydoc = mycol.find_one(myquery)
    return mydoc

if __name__ == "__main__":
    create_user("Burak", "Halefoglu")
    user_2_id = create_user("Ahmet", "Mehmet")
    print(read_user_by_id(user_2_id))
    update_user(user_2_id, "Ahmet", "Halefoglu")
    delete_user(user_2_id)
    print(read_user_by_id(user_2_id))