import os
from fastapi import FastAPI
from backend.src.api.transcribe import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.include_router(router)

if os.getenv('prod'):
    app.mount("/", StaticFiles(directory="./static", html=True), name="static")
else:
    @app.get("/")
    async def root():
        return {"message": "Hello World"}