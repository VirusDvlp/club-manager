from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatType

from sqlalchemy.ext.asyncio import AsyncSession

from fsm.user.private import RegistrationFSM

from markups.user.main import main_user_markup

from database.dao import UserDAO
from database.utils import connection


@connection
async def start_cmd(m: types.Message, state: FSMContext, db_session: AsyncSession):
    await state.clear()

    user = await UserDAO.get_obj(db_session, telegram_id=m.from_user.id)
    reg = True
    if not user:
        reg = False
        await UserDAO.register_user(
            db_session, m.from_user.id, m.from_user.username, True
        )
    else:
        if not user.has_private:
            reg = False
            user.has_private = True
            await db_session.commit()

    if reg:
        await m.answer(
            "Открыто главное меню",
            reply_markup=main_user_markup
        )
    else:
        await state.set_state(RegistrationFSM.name_state)
        await m.answer_photo(
            photo=types.FSInputFile("image/start_image.jpg"),
            caption="""
Приветстсвую! Я твой помощник в комьюнити RendezVous.\n Давай познакомимся. Как тебя зовут?
"""
        )




async def ask_alias(m: types.Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer(
        "Отлично! Теперь придумайте себе псеводним"
    )


@connection
async def finish_registration(
    m: types.Message, state: FSMContext, db_session: AsyncSession, *args
):
    s_data = await state.get_data()

    user = await UserDAO.get_obj(db_session, telegram_id=m.from_user.id)

    user.name = s_data['name']
    user.alias = s_data['alias']

    await db_session.commit()

    await m.answer(
        "Регистрация прошла успешно. Какие ваши дальнейшие действия?",
        reply_markup=main_user_markup
    )


def register_user_start_handlers(dp: Dispatcher):
    dp.message.register(
        start_cmd,
        F.chat.type == ChatType.PRIVATE,
        CommandStart(),
        StateFilter('*')
    )
