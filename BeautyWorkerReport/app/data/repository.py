from typing import List

from sqlalchemy import select, update, delete

from app.data.database import async_session_maker
from app.data.model import BeautyWorkerModel
from app.data.schemas import SWorkerAdd, SWorkerUpdate


class WorkerRepository:
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(BeautyWorkerModel)
            res = await session.execute(query)
            workers_models: List[BeautyWorkerModel] = res.scalars().all()
            return workers_models



