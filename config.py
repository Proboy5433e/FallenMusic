from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "11783043"))
API_HASH = getenv("API_HASH", "05defcdc9b57c133630c277c0a732a63")

BOT_TOKEN = getenv("BOT_TOKEN", "5991637461:AAHHe_Ga0dyxGZFNuj9VtlSlB9ddXkvuk20")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9079876"))

OWNER_ID = int(getenv("OWNER_ID", "5909779566"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AQBGTllxYAXp7GO39xLm45Lg8YDENe_1i2oZoUP_kvClGnPCkkY_CQ6eFOshrQkFi8OCd6LIzOdmF5zjgvIFJ2U1zg_HqDhWbg9lkW8cxPfsV9ijky4JS_KanaKaI6jT9Si2Hhdf89Ol5sggQJ7fdXBiB6dLhgfclRhyhENzBZli3ZBWmcNVjUVl9KMX3E9gSRtN0vUv-uMs443bpoMUI-Y6w6q0i2w2xPRjanbJPmaN68JWGEmWAkEgPoz8r12M18_dz6mwIpH4vjTxnwvvtu_vKUNTEKXToHHEYgiwxQCeR6HMd80OpoVDO089O_K4tOO64Zx7R6gKIP-i5Rov42v0AAAAAWBAFG4A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5909779566").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
