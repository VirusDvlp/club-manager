from typing import List, Any, Dict
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from .models import User


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instance

    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[Dict[str, Any]]):
        new_instances = [cls.model(**values) for values in instances]
        session.add_all(new_instances)
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        return new_instances


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def get_user(cls, session: AsyncSession, telegram_id: int):
        query = select(cls.model).filter_by(telegram_id=telegram_id)

        result = await session.execute(query)
        user = result.scalar_one_or_none()
        return user

    @classmethod
    async def register_user(
        cls,
        session: AsyncSession,
        telegram_id: int,
        username: str,
        has_bot_chat: bool
    ):
        self.add(
            session,
            telegram_id=telegram_id,
            telegram_username=username,
            is_private=has_bot_chat
        )
        
    
