from fastapi import APIRouter, Depends, Form, HTTPException, status, Response
from fastapi.responses import JSONResponse
from data.repository import WorkerRepository


router = APIRouter(
    prefix="",
    tags=["BeautyWorker"],
)

@router.get('/workers')
async def get_workers(
        response: Response,
):
    workers = await WorkerRepository().get_report_fired()
    return workers

