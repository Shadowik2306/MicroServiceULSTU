from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, status

from data.repository import WorkerRepository
from data.schemas import SWorkerAdd, SWorkerUpdate

router = APIRouter(
    prefix="/api/BeautyWorker",
    tags=["BeautyWorker"],
)


@router.post("/worker", description="# Регистрация нового работника")
async def sign_up(
        user: Annotated[SWorkerAdd, Depends()]
):
    res = await WorkerRepository.add_one(user)
    return res


@router.get('/workers')
async def get_workers():
    workers = await WorkerRepository.get_all()
    return workers


@router.get("/worker", description="# Получение нового работника")
async def get_worker(
        id: int
):
    res = await WorkerRepository.get_by_id(id)
    return res


@router.put("/worker", description="# Обновление данных рабочего")
async def update_worker(
        user: Annotated[SWorkerUpdate, Depends()]
):
    await WorkerRepository.update_by_id(user)
    return {"Status": "Updated"}


@router.delete("/worker", description="# Удаление данных рабочего")
async def delete_worker(
        id: int
):
    await WorkerRepository.delete_by_id(id)
    return {"Status": "Deleted"}

