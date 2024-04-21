from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from constants.app_config import HOST,PORT
from router.api import api_router

app = FastAPI(
    title="Assignment Review Pro",  # Replace with your application name
    description="A brief description of your application",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT)