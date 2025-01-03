import os
from dotenv import load_dotenv

# ..env faylini yuklash
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.getenv("DB_PATH", "to_do.db")
LANGUAGES = ['uz', 'en']

