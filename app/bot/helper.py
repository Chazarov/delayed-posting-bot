from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

def keyboard(buttons:List[List[InlineKeyboardButton]]):
    kbd = InlineKeyboardMarkup(inline_keyboard=buttons)

    return kbd

def button(text:str, callback_data:str):
    return InlineKeyboardButton(text=text, callback_data=callback_data)
