# -*- coding: utf-8 -*-
from aiogram import types
from aiogram import Bot, Dispatcher, executor


from settings import Settings


cfg = Settings()
bot = Bot(token=cfg.token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def start_cmd(msg: types.Message):
    await msg.send_copy(msg.chat.id)


async def on_startup(dp: Dispatcher):
    await dp.bot.set_webhook(str(cfg.webhook_url))


async def on_shutdown(dp: Dispatcher):
    await dp.bot.delete_webhook()


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=cfg.webhook_url.path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host='127.0.0.1',
        port=cfg.webapp_port
    )
