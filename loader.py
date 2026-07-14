from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
from data import config
import os
load_dotenv()

proxy_url = os.getenv("PROXY_URL")

session = AiohttpSession(proxy=proxy_url)

bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    session=session
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)