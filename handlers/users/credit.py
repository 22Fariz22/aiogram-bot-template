# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import zapros_telefona
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from states.state_credit import Test
from datetime import datetime
from utils.json_write_function import write_json

phone_num = {'89167345200': 'Екатерина Юрьевна', '89288167447': 'Денис Олегович', '89262682738': 'Фариз Фазилевич'}




@dp.message_handler(CommandStart())
async def ask_phone(message: types.Message):
    await message.answer(
        'Здравствуйте!\n'
        'Мы хотим узнать ваш номер телефона.\n'
        'Ниже будет кнопка "Поделится номером".\n'
        'Нажмите на неё,чтобы мы смогли взять ваш телефонный номер.',
        reply_markup=zapros_telefona.keyboard
    )
    # await Test.Q1.set()
    await Test.first()


@dp.message_handler(state=Test.Q1, content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message, state: FSMContext):
    answer = message.contact
    # await state.update_data(answer1=answer)
    # await state.update_data({'answer': answer})
    async with state.proxy() as data: data['answer1'] = answer
    await message.answer(
        f'Ваш телефонный номер: +{answer.phone_number}',
        reply_markup=ReplyKeyboardRemove()  # убирает инлайн
    )

    await message.answer("А сейчас введите сумму которую вы хотите получить.")

    # await Test.Q2.set()
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):

    data = await state.get_data()  # достаем все ответы
    client_number = data.get('answer1')["phone_number"]
    credit = message.text
    name = data.get('answer1')["first_name"]
    user_id = data.get('answer1')["user_id"]
    time = datetime.now()

    # name = answer3  # надо определить клиента из списка
    # client_number = answer1
    # credit = answer2
    # user_id = answer4
    person = {
        'name': name,
        'phone_number': client_number,
        'credit': credit,
        'user_id': user_id,
        #'sms': False,
        'time': str(time)
    }

    write_json(person)

    await message.answer('Поздравляю,Вы отправили запрос!')
    await message.answer(f"+{client_number} - Ваш телефонный номер")
    await message.answer(f'{credit} - Ваша желаемая сумма')
    await message.answer(f'В ближайщее время,с Вами свяжется наш менеджер')

    await state.finish()


