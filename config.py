import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_NOBITA_DEFAULTERS_ll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME", "NOBITA_MUSIC_ROBOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002344707828))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5536473064))

# Make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv(
    "PRIVACY_LINK",
    "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18",
)

## Fill these variables if you're deploying on heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/harshnu12035/NOBITA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shona_bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+AJuUNJPIuIQwM2M9")

# auto leaving on/off
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Pyrogram String Sessions
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/fcawaj.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/tcz7s6.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
STATS_IMG_URL = "https://files.catbox.moe/i7uj2i.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/fcawaj.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/fcawaj.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/fcawaj.jpg"


# Convert duration to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Check URLs
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. It must start with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. It must start with https://"
        )
