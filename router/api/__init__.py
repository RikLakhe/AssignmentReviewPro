# from fastapi import APIRouter
# from .v1 import user as v1_router_user, permission as v1_router_permission
# from .v2.permission import router as v2_permission_router
#
# api_router = APIRouter()
#
#
# # api_router.include_router(v1_router_user.router, prefix="/v1", tags=["v1"])
# # api_router.include_router(v1_router_permission.router, prefix="/v1", tags=["v1"])
# #
# # api_router.include_router(v2_permission_router, prefix="/v2", tags=["v2"])
from fastapi import APIRouter
from .v1 import user as v1_user_router, permission as v1_permission_router
from .v2.user import router as v2_user_router

api_router = APIRouter()

# Mount version 1 routes under /api/v1
api_router.include_router(v1_user_router.router, prefix="/v1", tags=["v1"])
api_router.include_router(v1_permission_router.router, prefix="/v1", tags=["v1"])

# Mount version 2 routes under /api/v2
api_router.include_router(v2_user_router, prefix="/v2", tags=["v2"])
