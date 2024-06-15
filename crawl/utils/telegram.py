from jinja2 import Environment, FileSystemLoader
from scrapy.utils.project import get_project_settings
from telegram import Bot, ParseMode

settings = get_project_settings()

env = Environment(
    loader=FileSystemLoader(settings["TELEGRAM_TEMPLATES_PATH"]),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template(settings["TELEGRAM_MESSAGE_TEMPLATE_FILE"])


def send_message(product: dict) -> None:
    """
    Send formatted message to specific chat id.
    """
    bot = Bot(token=settings["TELEGRAM_BOT_TOKEN"])

    bot.send_message(
        chat_id=settings["TELEGRAM_CHAT_ID"],
        text=template.render(product=product),
        parse_mode=ParseMode.HTML,
    )
