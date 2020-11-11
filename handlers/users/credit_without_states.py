# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import zapros_telefona
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import CommandStart


@dp.message_handler(CommandStart())
async def ask_phone(message: types.Message):
    await message.answer(
        'Здравствуйте!\n'
        'Мы хотим узнать ваш номер телефона'
        'Нажмите на кнопку "поделиться номером"',
        reply_markup=zapros_telefona.keyboard
    )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    answer = message.contact
    await message.answer(
        f'Ваш телефонный номер: {answer.phone_number}',
        reply_markup=ReplyKeyboardRemove()  # убирает инлайн
    )
    await message.answer("А сейчас введите сумму которую вы хотите получить.")


@dp.message_handler()
async def answer_q2(message: types.Message):
    answer2 = message.text
    await message.answer('Поздравляю,Вы отправили запрос!')
    # await message.answer(f"{answer1} - your phone number")
    await message.answer(f'{answer2} - ваша желаемая сумма')
    await message.answer(f'В ближайщее время,с вами свяжется наш менеджер')



