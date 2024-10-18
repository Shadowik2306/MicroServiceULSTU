from fastapi import APIRouter, Depends, Form, HTTPException, status
from data.repository import WorkerRepository

router = APIRouter(
    prefix="",
    tags=["BeautyWorker"],
)

@router.get('/workers')
async def get_workers():
    workers = await WorkerRepository.get_all()
    return workers

