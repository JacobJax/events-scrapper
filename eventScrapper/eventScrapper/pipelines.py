# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

CONN = os.getenv("DB_CONN_STRING")
DB = os.getenv("DB_NAME")
COLL = os.getenv("DB_COLLECTION")

class EventscrapperPipeline:

    def __init__(self):
        self.cluster = MongoClient(f"{CONN}")
        db = self.cluster[f"{DB}"]
        self.collection = db[f"{COLL}"]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
