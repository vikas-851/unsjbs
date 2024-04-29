class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5932230962"
    sudo_users = "5932230962", "6996612518", "6454320047", "6257270528", "6574393060"
    GROUP_ID = -1001875834087
    TOKEN = "6789724300:AAHBw-GuS8fkDlLbl-YqnSei3YcdqBTcpEE"
    mongo_url = "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/c756fddc0bb096255e9d4.jpg", "https://telegra.ph/file/68cc8c9e6ac0d91035aa0.jpg", "https://telegra.ph/file/a2f0095d70121c2680911.jpg"]
    SUPPORT_CHAT = "-1002038805604"
    UPDATE_CHAT = "Nᴀʀᴜᴛᴏ Uᴘᴅᴀᴛᴇs"
    BOT_USERNAME = "nudeXcatchrbot"
    CHARA_CHANNEL_ID = "-1001875834087"
    api_id = 22792918
    api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"
    
    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
