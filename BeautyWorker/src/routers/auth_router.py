from typing import Annotated

import httpx
from fastapi import APIRouter, Request

from data.repository import WorkerRepository
from data.schemas import SWorkerAdd, SWorkerUpdate

router = APIRouter(
    prefix="",
    tags=["BeautyWorker"],
)


@router.post("/worker", description="# Регистрация нового работника")
async def sign_up(
        user: SWorkerAdd
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
        user: SWorkerUpdate
):
    await WorkerRepository.update_by_id(user)
    return {"Status": "Updated"}


@router.delete("/worker", description="# Удаление данных рабочего")
async def delete_worker(
        id: int
):
    await WorkerRepository.fire_by_id(id)
    return {"Status": "Fired"}


@router.get("/get_report")
async def get_report(
        request: Request,
):
    async with httpx.AsyncClient() as client:
        url = f"http://web-report:8002/workers"
        response = await client.get(url)

        return response.json()


