from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def get_users():
    return {"message": "Version 2 - Get Users"}
