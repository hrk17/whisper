import os
from fastapi import FastAPI
from backend.src.api.transcribe import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    if os.getenv('prod'):
        app.mount("/static", StaticFiles(directory="static"), name="static")
    else:
        return {"message": "Hello World"}