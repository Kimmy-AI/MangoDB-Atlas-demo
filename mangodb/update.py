import os
import pymongo
import datetime
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

title = "Test"

collection.update_many(
    {"title": title},
    {
        "$push": {
            "languages": "Franch",
        },
        "$setOnInsert": {
            "plot": "Illiterate peasant Juan Gallardo rises meteorically to fame and fortune in the bullfight arena only to sow the seeds of his own fall.",
            "genres": ["Drama", "Sport"],
            "runtime": 125,
            "rated": "APPROVED",
            "cast": ["Tyrone Power", "Linda Darnell", "Rita Hayworth", "Alla Nazimova"],
            "num_mflix_comments": 1,
            "poster": "https://m.media-amazon.com/images/M/MV5BZDU4YmIyMDUtYjA5NC00ODYyLWJmNTItOTZlYTZlNmFjNGVkL2ltYWdlXkEyXkFqcGdeQXVyNjQzNDI3NzY@._V1_SY1000_SX677_AL_.jpg",
            "title": title,
            "fullplot": "Bullfighter Juan Gallardo falls for socialite Dona Sol, turning from the faithful Carmen who nevertheless stands by her man as he continues to face real danger in the bullring.",
            "released": datetime.datetime(1941, 5, 30, 0, 0),
            "directors": ["Rouben Mamoulian"],
            "writers": [
                "Vicente Blasco Ibèèez (based on the novel by)",
                "Jo Swerling (screenplay)",
            ],
            "awards": {
                "wins": 0,
                "nominations": 2,
                "text": "Won 1 Oscar. Another 1 nomination.",
            },
            "lastupdated": "2015-09-05 00:27:47.423000000",
            "year": 1941,
            "imdb": {"rating": 7.0, "votes": 1417, "id": 33405},
            "countries": ["USA"],
            "type": "movie",
            "tomatoes": {
                "viewer": {"rating": 3.7, "numReviews": 611, "meter": 67},
                "dvd": datetime.datetime(2007, 5, 1, 0, 0),
                "critic": {"rating": 7.2, "numReviews": 6, "meter": 100},
                "lastUpdated": datetime.datetime(2015, 9, 10, 19, 7, 49),
                "rotten": 0,
                "production": "20th Century Fox",
                "fresh": 6,
            },
        },
    },
    True,
)


print("\n")

result = collection.find_one({"title": title})
print(result)
