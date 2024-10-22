from aiogram import F, types, Router, Dispatcher, Bot


from app.bot.handlers.handlers import *

router = Router()


@router.message(F.text == "/start")
async def h(message:types.Message):
    await h1(message)


@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await h2(callback_query.message)