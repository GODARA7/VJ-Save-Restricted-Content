import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7505160165:AAFwhs1lGStRDlcHJsRBTfuNtFtxQOZQw4Y")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26512964"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://weloxa8533:WKmtuOzgMtTFGCrC@cluster0.jrz7hfn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
