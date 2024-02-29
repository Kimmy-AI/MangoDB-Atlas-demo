import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

mongodb_password = os.getenv("mongodb_password")

# connect to your Atlas cluster
client = pymongo.MongoClient(
    f"mongodb+srv://rpmckg:{mongodb_password}@cluster0.nixga4w.mongodb.net/?retryWrites=true&w=majority"
)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

collection = client["sample_mflix"]["movies"]

for item in collection.find():
    print(item)

collection.delete_many({})

print("\n")

for item in collection.find():
    print(item)
