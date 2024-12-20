import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26512964"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")

#Database 
DB_URI = os.environ.get("DB_URI", "")
