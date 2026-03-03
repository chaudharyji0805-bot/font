import os

# Bot Token (Heroku Config Vars se aayega)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB (Heroku Config Vars se)
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "fontbot")

# Force join channels
FORCE_CHANNELS = [
    "@BotzEmpire",
    "@AboutDeva",
    "@BotsDeal"
]

# Admin IDs (apna Telegram ID)
ADMINS = [7538572906]

# Watermark / Credits (empty = no watermark)
WATERMARK = ""
