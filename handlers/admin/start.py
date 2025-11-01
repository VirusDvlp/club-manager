from aiogram.filters import CommandStart, StateFilter
from aiogram import Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatType

from filters.user_filters import AdminFilter
from markups.admin.main import main_admin_markup


async def start_cmd(m: types.Message, state: FSMContext):
    await state.clear()

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

