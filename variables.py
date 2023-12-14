# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 29538539  # Get this value from my.telegram.org/apps
    API_HASH = "e3141eb87727600cee656cf0cf8007d6"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://pduhrcnhaeqyrm:d7f4e0e6574d42442306af06f51898d3577142efa4bc94aa799e215fee889dce@ec2-3-228-158-221.compute-1.amazonaws.com:5432/d4aa0m215o548q"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1001943753978
    MESSAGE_DUMP = -1001943753978

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://y2965860:xGSHMdXYftGkEoxQ@teamgodz.gaulnoy.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "LostCorps"
    SUPPORT_ID = -1002110091339

    # Database name
    DB_NAME = "TEAMGoDz"

    # Bot token
    TOKEN = "6834502380:AAF-PyzgaN-ERy5Fzi9H5fIetDE_SkCendk"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6230236721
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = ""

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
