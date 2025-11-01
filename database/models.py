from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import BigInteger, func, String, Boolean

import datetime


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'


class User(Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    telegram_username: Mapped[str] = mapped_column(String(32))
    register_date: Mapped[datetime] = mapped_column(server_default=func.now())
    has_private: Mapped[bool] = mapped_column()


class BaseEvent(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    max_members: Mapped[int] = mapped_column(default=0)
    date: Mapped[datetime] = mapped_column(Boolean, default=True)
