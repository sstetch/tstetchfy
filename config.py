from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "1404114574"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/3e49b4d917574daf2a432.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3e49b4d917574daf2a432.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TXNX5")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/its_stetch")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1404114574").split()))


FAILED = "https://telegra.ph/file/ba5e50feaff3c2bbde984.jpg"
