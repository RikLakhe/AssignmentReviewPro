from fastapi import APIRouter

from models.message_dto import MessageDTO

router = APIRouter()


@router.get("/permission", response_model=MessageDTO)
async def root():
    """Returns a simple message."""
    return MessageDTO(message="Hello, world! permission v2")
