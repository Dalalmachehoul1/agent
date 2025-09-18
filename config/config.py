import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_URI = os.getenv("DB_URI")
    GPT_KEY = os.getenv("GPT_KEY")
