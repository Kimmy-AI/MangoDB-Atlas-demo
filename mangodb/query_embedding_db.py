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

collection = client["sample_mflix"]["embedded_movies"]

result = collection.find_one({"title": "test1"})

print(result)
