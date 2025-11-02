from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from database.dao import UserDAO
from database.utils import connection

from fsm.user.private import SuggestActivityFSM

from text import get_activity_suggestion_text
from config import chat_settings


async def ask_name(c: types.CallbackQuery, state: FSMContext):

    await state.set_state(SuggestActivityFSM.name_state)
    await c.message.answer(
        "Введите название активности"
    )

    await c.answer()


async def ask_description(m: types.Message, state: FSMContext):
    await state.set_state(SuggestActivityFSM.descr_state)
    await state.update_data(name=m.text.strip())

    await m.answer("Введите краткое описание активности")


async def ask_date(m: types.Message, state: FSMContext):
    await state.set_state(SuggestActivityFSM.date_state)
    await state.update_data(descr=m.text.strip())

    await m.answer("Введите дату и время встречи")


async def ask_place(m: types.Message, state: FSMContext):
    await state.set_state(SuggestActivityFSM.place_state)
    await state.update_data(date=m.text.strip())

    await m.answer("Введите место встречи")


async def create_suggestion(m: types.Message, state: FSMContext):
    place = m.text.strip()
    s_data = await state.get_data()

    await m.bot.send_message(
        chat_settings.ADMIN_CHAT_ID,
        get_activity_suggestion_text(
            name=s_data['name'],
            description=s_data['descr'],
            date=s_data['date'],
            place=place,
            username=m.from_user.username
        )
    )

    await m.answer("✅Ваше предлоэение успещно отправлено администрации")

def register_create_suggestion_handlers(dp: Dispatcher):
    dp.callback_query.register(ask_name, F.data == "suggest_activity")
    dp.message.register(ask_description, StateFilter(SuggestActivityFSM.name_state))
    dp.message.register(ask_date, StateFilter(SuggestActivityFSM.descr_state))
    dp.message.register(ask_place, StateFilter(SuggestActivityFSM.date_state))
    dp.message.register(create_suggestion, StateFilter(SuggestActivityFSM.place_state))
