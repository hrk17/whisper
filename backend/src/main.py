from fastapi import FastAPI
from backend.src.api.transcribe import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/test/")
# async def test():
#     return "Success"