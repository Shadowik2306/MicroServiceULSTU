from fastapi import FastAPI
from routers.auth_router import router as auth_router

app = FastAPI()

@app.get("/")
def initial():
    return "Hello i am beauty worker crud"


app.include_router(auth_router)
