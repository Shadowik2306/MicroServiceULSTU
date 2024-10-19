from fastapi import APIRouter, Request

from data.schemas import SWorkerAdd, SWorkerUpdate
from utils.forward import gateway

router = APIRouter(
    prefix="/crud",
    tags=["BeautyWorker"],
)


@router.post("/worker", description="# Регистрация нового работника")
async def sign_up(
        user: SWorkerAdd,
        request: Request
):
    return await gateway("worker", request)


@router.get('/workers')
async def get_workers(request: Request):
    return await gateway("workers", request)


@router.get("/worker", description="# Получение нового работника")
async def get_worker(
    id: int,
    request: Request
):
    return await gateway("worker", request)


@router.put("/worker", description="# Обновление данных рабочего")
async def update_worker(
        user: SWorkerUpdate,
        request: Request,
):
    return await gateway("worker", request)


@router.delete("/worker", description="# Удаление данных рабочего")
async def delete_worker(
        id: int,
        request: Request
):
    return await gateway("worker", request)

