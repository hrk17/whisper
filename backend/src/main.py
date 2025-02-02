import os
from fastapi import FastAPI
from backend.src.api.transcribe import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.include_router(router)

if os.getenv('prod'):
    app.mount("/static", StaticFiles(directory="/app/static"), name="static")

@app.get("/")
async def root():
    if os.getenv('prod'):
        return FileResponse('/app/static/index.html')
    else:
        return {"message": "Hello World"}