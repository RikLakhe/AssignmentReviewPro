from fastapi import FastAPI

from constants.app_config import HOST,PORT
from routers import api, user

app = FastAPI(
    title="Assignment Review Pro",  # Replace with your application name
    description="A brief description of your application",
    version="1.0.0",
)

app.include_router(api.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT)