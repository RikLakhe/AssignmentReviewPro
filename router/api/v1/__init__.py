from fastapi import APIRouter
from .user import router as user_router
from .permission import router as permission_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(permission_router, prefix="/permission", tags=["permission"])
