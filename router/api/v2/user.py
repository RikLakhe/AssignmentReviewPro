from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def get_users():
    return {"message": "Version 2 - Get Users"}
