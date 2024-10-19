from fastapi import APIRouter, Request

from utils.forward import gateway

router = APIRouter(
    prefix="/reports",
    tags=["BeautyWorkerReport"],
)

@router.get("/")
async def get_reports(
        request: Request,
):
    return await gateway("get_report", request)

