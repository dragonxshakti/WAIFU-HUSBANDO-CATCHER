class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6890857225"
    sudo_users = "6890857225", "6765826972"
    GROUP_ID = -1002133191051
    TOKEN = "6818727286:AAFriRWq7EkzCiSmgWuE8oS-9-sV8VLOz4g"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
