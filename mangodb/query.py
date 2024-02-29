import pymongo
import datetime
import os
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

for item in collection.find().limit(3).sort("released", pymongo.DESCENDING):
    print(item, "\n")

print("\n")

result = collection.find().limit(10).skip(0)
for document in result:
    print(document)

print("\n")

result = collection.find().limit(10).skip(10)
for document in result:
    print(document)

print("\n")

result = collection.find_one({"title": "Robbery"})

print("Document found:\n", result)

print("\n")

current_time = datetime.datetime.now()

# filter
query = {
    "released": {"$gte": datetime.datetime(1968, 12, 9, 0, 1), "$lte": current_time}
}

result = collection.find(query).limit(1)

for document in result:
    print(document)

print("\n")

# Regular expression query, ignoring case
result = collection.find({"title": {"$regex": r"(?i)Sand"}}).limit(1)
for document in result:
    print(document)

print("\n")

# Fuzzy query, semantic search
result = collection.aggregate(
    [
        {
            "$search": {
                "index": "title",
                "autocomplete": {"path": "title", "query": "Sand"},
            },
        },
        {
            "$limit": 2,
        },
    ]
)
for document in result:
    print(document)
