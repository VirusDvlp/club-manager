from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession



from database.dao import UserDAO
from database.utils import connection

from fsm.user.private import CreateInitiativeFSM

from markups.user.events import get_take_part_in_event_markup

from text import get_initiative_text

from config import chat_settings

from utils.date import validate_date_time
from utils.enums import EventType


async def ask_date(c: types.CallbackQuery, state: FSMContext):

    await c.answer()

    await state.set_state(CreateInitiativeFSM.date_state)

    await c.message.answer(
        "Введите дату и время мероприятия в формате ММ-ММ-ГГГГ чч:мм"
    )


async def ask_place(m: types.Message, state: FSMContext):
    date = validate_date_time(m.text.strip())

    if not date:
        await m.answer("❗Неверный формат! Попробуйте еще раз")
        return 1

    await state.update_data(datetime=date)
    await state.set_state(CreateInitiativeFSM.place_state)

    await m.answer(
        "Укажите место встречи"
    )


async def ask_comment(m: types.Message, state: FSMContext):
    await state.set_state(CreateInitiativeFSM.comment_state)
    await state.update_data(place=m.text.strip()[:200])

    await m.answer("Введите небольшой комментарий-описание о вашей инициативе")


async def create_initiative(m: types.Message, state: FSMContext):
    s_data = await state.get_data()
    await state.clear()

    await m.bot.send_message(
        chat_id=chat_settings.GROUP_ID,
        message_thread_id=chat_settings.INITIATIVES_THREAD_ID,
        text=get_initiative_text(
            s_data['datetime'],
            s_data['place'],
            m.text.strip()
        )
    )

    await m.answer("Ваша инициатива успешно опубликована в группе")


def register_create_initiative(dp: Dispatcher):
    dp.callback_query.register(ask_date, F.data == "create_initiative")
    dp.message.register(ask_place, StateFilter(CreateInitiativeFSM.date_state))
    dp.message.register(ask_comment, StateFilter(CreateInitiativeFSM.place_state))
    dp.message.register(create_initiative, StateFilter(CreateInitiativeFSM.comment_state))
