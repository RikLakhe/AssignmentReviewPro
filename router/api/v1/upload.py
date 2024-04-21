from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pathlib import Path

from models.message_dto import MessageDTO

router = APIRouter()


@router.post("")
async def upload_file(file: UploadFile = File(...), user_id: str = Form(...), user_email: str = Form(...)):
    try:
        # Save the uploaded file to a local folder
        filename = file.filename
        file_path = Path("uploads") / filename
        with file_path.open("wb") as buffer:
            buffer.write(file.file.read())

        # You can use user_id and user_email here for additional processing
        # For now, just return a success message
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully", "filename": filename})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Failed to upload file", "error": str(e)})
