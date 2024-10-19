from fastapi import FastAPI
from routers.router_crud import router as crud_router
from routers.router_report import router as report_router

app = FastAPI()
app.include_router(crud_router)
app.include_router(report_router)



@app.get("/")
async def main():
    return {"Hello": "World"}

