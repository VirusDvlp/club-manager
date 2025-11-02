from aiogram.filters import CommandStart, StateFilter
from aiogram import Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatType

from database.dao import UserDAO
from database.utils import connection

from filters.user_filters import AdminFilter
from markups.admin.main import main_admin_markup


@connection
async def start_cmd(m: types.Message, state: FSMContext, db_session):
    await state.clear()

    user = await UserDAO.get_obj(
        db_session,
        telegram_id=m.from_user.id,
    )
    if not user:
        await UserDAO.register_user(
            db_session,
            telegram_id=m.from_user.id,
            username=m.from_user.username,
            has_bot_chat=True,
            is_admin=True
        )

    await m.answer(
        text="Добро пожаловать!",
        reply_markup=main_admin_markup
    )


def register_start_handlers(dp: Dispatcher) -> None:
    dp.message.register(
        start_cmd,
        CommandStart(),
        AdminFilter(),
        F.chat.type == ChatType.PRIVATE,
        StateFilter('*')
    )

