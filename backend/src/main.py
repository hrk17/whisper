import os
from fastapi import FastAPI
from backend.src.api.transcribe import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()
app.include_router(router)

if os.getenv("prod"):
    app.mount("/", StaticFiles(directory="./static", html=True), name="static")


@app.get(
    "/",
    response_class=FileResponse if os.getenv("prod") else JSONResponse,
    include_in_schema=False,
)
def root():
    if os.getenv("prod"):
        return FileResponse("/index.html")
    else:
        return "Hello World"