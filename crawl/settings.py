import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_PATH = Path(__file__).parent.parent

TEMPLATES_PATH = BASE_PATH / "crawl" / "templates"

# Telegram settings
TELEGRAM_MESSAGE_TEMPLATE_FILE = "telegram_message.jinja2"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# MongoDB settings
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_PRODUCT_COLLECTION = os.getenv("MONGO_PRODUCT_COLLECTION")

BOT_NAME = "reverb-crawl"

SPIDER_MODULES = ["crawl.spiders"]
NEWSPIDER_MODULE = "crawl.spiders"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"'
)

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
