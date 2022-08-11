import os
from DB import Database

MONGO_URL = os.environ.get('MONGO_URL')

db = Database(MONGO_URL)
