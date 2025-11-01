from aiogram import BaseMiddleware, types
from aiogram.enums import ChatType

from typing import Callable, Any, Dict, Awaitable

from database.dao import UserDAO
from database.utils import connection



class RegisterUserMiddleware(BaseMiddleware):
    
    @connection
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
        session
    ) -> Any:

        if chat.type == ChatType.SUPERGROUP:
            if isinstance(event, types.Message):
                chat = event.chat
            elif isinstance(event, types.CallbackQuery):
                chat = event.message.chat
            user_id = event.from_user.id
            user = UserDAO.get_user(session=session, telegram_id=user_id)

            if not user:
                await UserDAO.register_user(
                    session,
                    event.from_user.id,
                    event.from_user.username,
                    False
                )
