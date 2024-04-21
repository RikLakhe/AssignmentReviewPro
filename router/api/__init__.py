from fastapi import APIRouter
from .v1 import api_router as v1_router
from .v2 import api_router as v2_router

api_router = APIRouter()

# Mount version 1 routes under /api/v1
api_router.include_router(v1_router, prefix="/v1", tags=["v1"])

# Mount version 2 routes under /api/v2
api_router.include_router(v2_router, prefix="/v2", tags=["v2"])
