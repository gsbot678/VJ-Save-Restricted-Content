import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", ":")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28225971"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d5de247a7d8b865b48d1bb5944058315

1 17:16")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5943224894"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mdalimurtaza78689:<2MIzJuEaFpMvsJCK>@cluster0.1ysrw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
