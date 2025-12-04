# database.py
# MongoDB database operations

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from config import MONGO_URI, MONGO_TIMEOUT, DB_NAME, COLLECTION_NAME


class Database:
    """Handles all MongoDB operations"""
    
    def __init__(self):
        self.client = None
        self.db = None
        self.lexicon = None
        self.is_connected = False
        self._connect()
    
    def _connect(self):
        """Establish connection to MongoDB"""
        try:
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
            self.client.admin.command("ping")
            self.db = self.client[DB_NAME]
            self.lexicon = self.db[COLLECTION_NAME]
            self.is_connected = True
            print("✓ Connected to MongoDB successfully")
        except Exception as e:
            self.is_connected = False
            print(f"✗ MongoDB connection failed: {e}")
    
    def get_user_correction(self, word):
        """Retrieve user correction for a word"""
        if not self.is_connected or self.lexicon is None:
            return None
        
        try:
            doc = self.lexicon.find_one({"mot": word})
            return doc.get("user") if doc else None
        except Exception as e:
            print(f"Error retrieving correction: {e}")
            return None
    
    def save_correction(self, word, pos, i3rab, gender):
        """Save user correction to database"""
        if not self.is_connected or self.lexicon is None:
            return False
        
        try:
            self.lexicon.update_one(
                {"mot": word},
                {"$set": {
                    "mot": word,
                    "user": {
                        "pos": pos,
                        "i3rab": i3rab,
                        "gender": gender
                    }
                }},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error saving correction: {e}")
            return False
    
    def is_online(self):
        """Check if database connection is active"""
        return self.is_connected