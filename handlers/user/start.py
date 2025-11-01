from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatType

from sqlalchemy.ext.asyncio import AsyncSession

from markups.user.main import main_user_markup

from database.dao import UserDAO
from database.utils import connection


@connection
async def start_cmd(m: types.Message, state: FSMContext, db_session: Async):
    await state.clear()

    if not UserDAO.get_user(db_session, m.from_user.id):
        UserDAO.register_user(
            db_session, m.from_user.id, m.from_user.username, True
        )



    await m.answer(
        "Приветстсвую! Я твой помощник в комьюнити RendezVous.\nЧто хотите сделать?",
        reply_markup=main_user_markup
    )


def register_user_start_handlers(dp: Dispatcher):
    dp.message.register(
        start_cmd,
        F.chat.type == ChatType.PRIVATE,
        CommandStart()
    )
