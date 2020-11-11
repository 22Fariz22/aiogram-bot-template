# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(row_width=1,
    keyboard=[
        [
            KeyboardButton(
                text='Поделится номером',
                request_contact=True
            )
        ]
    ],
    resize_keyboard=True
)