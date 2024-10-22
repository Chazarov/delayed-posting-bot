from aiogram import Bot
from aiogram import Bot, Dispatcher, types

from app.core.config import configs

from app.bot.strings import USER_COMANDS, GROUP_COMMANS, DESCRIPTION

bot = Bot(token=configs.BOT_TOKEN)
dp = Dispatcher()


async def on_startup(bot):
    print("Bot was started.")

async def on_shutdown(bot):
    print("Bot was down.")




async def main()->None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)


    await bot.delete_webhook(drop_pending_updates = True)
    await bot.set_my_description(DESCRIPTION)
    await bot.set_my_commands(commands = USER_COMANDS,scope = types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands = GROUP_COMMANS,scope = types.BotCommandScopeAllGroupChats())
    await dp.start_polling(bot)