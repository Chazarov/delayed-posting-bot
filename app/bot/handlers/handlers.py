from aiogram import types
from aiogram.types import InlineKeyboardButton as IB
from aiogram import F, types, Router, Dispatcher, Bot

from app.bot.helper import keyboard

router = Router()


@router.message(F.text == "/start")
async def h(message: types.Message):
    await message.answer(text = \
"""
СОЗДАНИЕ ПОСТА
Выберите канал, в котором хотите создать публикацию.
""",
        reply_markup=keyboard(
            [
                [IB(text="Добавленый канал", callback_data="")]
                [IB(text="+ Добавить канал", callback_data="")]
            ]
        )
    )

@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Отправьте боту то, что хотите опубликовать в канале:
{}
""",
        reply_markup=keyboard(
            [
                [IB(text="Выбрать другой канал", callback_data="")]
            ]
        )
    )

@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Картинка или видео Текст
""",
        reply_markup=keyboard(
            [
                [IB(text="Медиа", callback_data=""), IB(text="Изменить описание", callback_data="")],
                [IB(text="URL Кнопки", callback_data="")],
                [IB(text="Скрытое предложение", callback_data="")],
                [IB(text="Больше настроек", callback_data="")],
                [IB(text="Отменить", callback_data=""), IB(text="Далее", callback_data="")]
            ]
        )
    )


@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
отправте новое описание для поста
""",
        reply_markup=keyboard(
            [
                [IB(text="Удалить описание", callback_data="")],
                [IB(text="Назад", callback_data="")],
            ]
        )
    )

@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Создание поста отменено
""")
    
@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(reply_markup=keyboard(
            [
                [IB(text="X Комментарии", callback_data=""), IB(text="X Закрепить", callback_data="")],
                [IB(text="V Комментарии", callback_data=""), IB(text="V Закрепить", callback_data="")],
            ]
        )
    )



@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Комментарии отключены.
Для корректной работы дайте боту @createbotchannel право на удаление сообщений в прикрепленном к каналу чате.
""")
    

@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
7 Комментарии включены. 
Напоминаем, что для появления комментариев под постами, вы должны прикрепить к каналу чат в разделе «Обсуждение».
""")
    
@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Картинка или видео текст
""",
        reply_markup=keyboard(
            [
                [IB(text="Изменить медиа", callback_data="")],
                [IB(text="Спойлер", callback_data="")],
                [IB(text="Платный пост", callback_data="")],
                [IB(text="Спойлер", callback_data="")],
                [IB(text="Расположение: сверху/снизу", callback_data="")],
                [IB(text="Удалить медиа", callback_data="")],
                [IB(text="Назад", callback_data="")],
            ]
        )
    )


@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
Скрытая картинка под спойлером с надписью Раскрыть за *1
""",
        reply_markup=keyboard(
            [
                [IB(text="Изменить медиа", callback_data="")],
                [IB(text="Платный пост", callback_data="")],
                [IB(text="Цена за платный пост: 1", callback_data="")],
                [IB(text="Расположение: сверху/снизу", callback_data="")],
                [IB(text="Удалить медиа", callback_data="")],
                [IB(text="Назад", callback_data="")],
            ]
        )
    )

@router.callback_query(F.data == "")
async def h(message: types.Message, callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
* ЦЕНА ЗА ПЛАТНЫЙ ПОСТ
Отправьте цену в звёздах за платный пост.
Цена должна находиться в диапазоне от 1 до 2.500 звёзд.
""",
        reply_markup=keyboard(
            [
                [IB(text="Назад", callback_data="")],
            ]
        )
    )


@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
URL-КНОПКИ
Отправьте боту список URL-кнопок в следующем формате:
Кнопка 1-link.com
Кнопка 2-ink.com
Используйте разделитель "1", чтобы добавить до 8 кнопок в один ряд (допустимо 15 рядов):
Кнопка 1 - link.com" target="_blank">link.com | Кнопка 2 - http://link.com
""")


@router.callback_query(F.data == "")
async def h(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text = \
"""
СКРЫТОЕ ПРОДОЛЖЕНИЕ
В этом разделе вы можете добавить кнопки, под которые вы можете скрыть текст от тех, кто не подписан на ваш канал.
""",
        reply_markup=keyboard([
                [IB(text="Удалить описание", callback_data="")],
                [IB(text="Назад", callback_data="")],
            ]
        )
    )