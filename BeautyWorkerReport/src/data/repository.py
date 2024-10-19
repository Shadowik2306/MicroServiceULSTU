from typing import List

from sqlalchemy import select, update, delete

from data.database import async_session_maker
from data.model import BeautyWorkerModel
from data.schemas import SWorkerAdd, SWorkerUpdate


class WorkerRepository:
    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(BeautyWorkerModel)
            res = await session.execute(query)
            workers_models: List[BeautyWorkerModel] = res.scalars().all()
            return workers_models

    @classmethod
    async def get_report_fired(cls):
        async with async_session_maker() as session:
            result = {
                "Applied": [],
                "Fired": []
            }

            query = select(BeautyWorkerModel).where(BeautyWorkerModel.status == "Applied")
            res_app = await session.execute(query)
            result["Applied"] = res_app.scalars().all()

            query = select(BeautyWorkerModel).where(BeautyWorkerModel.status == "Fired")
            res_fired = await session.execute(query)
            result["Fired"] = res_fired.scalars().all()

            return result

