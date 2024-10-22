from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 


class BaseModel(DeclarativeBase):
    __abstract__ = True


    created: Mapped[DateTime] = mapped_column(DateTime, default = func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default = func.now())



    async def delete(self, session:AsyncSession):
        await session.delete(self)
        await session.commit()
