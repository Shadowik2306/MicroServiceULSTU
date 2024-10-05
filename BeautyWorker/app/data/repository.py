from typing import List

from sqlalchemy import select, update, delete

from app.data.database import async_session_maker
from app.data.model import BeautyWorkerModel
from app.data.schemas import SWorkerAdd, SWorkerUpdate


class WorkerRepository:
    @classmethod
    async def add_one(cls, worker: SWorkerAdd):
        async with async_session_maker() as session:
            user_dict = worker.model_dump()
            worker = BeautyWorkerModel(**user_dict)
            session.add(worker)
            await session.flush()
            await session.commit()
            return worker

    @classmethod
    async def get_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(BeautyWorkerModel).where(BeautyWorkerModel.id == id)
            res = await session.execute(query)
            worker_model: BeautyWorkerModel = res.scalars().first()
            return worker_model

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(BeautyWorkerModel)
            res = await session.execute(query)
            workers_models: List[BeautyWorkerModel] = res.scalars().all()
            return workers_models

    @classmethod
    async def update_by_id(cls, worker: SWorkerUpdate):
        async with async_session_maker() as session:
            worker_dict = worker.model_dump(exclude_none=True)
            query = update(BeautyWorkerModel).where(BeautyWorkerModel.id == worker_dict["id"]).values(worker_dict)
            await session.execute(query)
            await session.commit()
            return

    @classmethod
    async def delete_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = delete(BeautyWorkerModel).where(BeautyWorkerModel.id == id)
            await session.execute(query)
            await session.commit()
            return


