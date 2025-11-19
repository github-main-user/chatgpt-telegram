#!/usr/bin/env python
import asyncio

from aiogram import Bot, Dispatcher

from src.config import settings
from src.handlers import router

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
