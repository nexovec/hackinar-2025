from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import os
from datetime import datetime
from pathlib import Path
from tinydb_setup import db

router = APIRouter()

# Zaruč, že složka pro soubory existuje, aby je bylo kam uložit
UPLOAD_DIR = "soubory"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    filename: str = Form(...)
):
    try:
        # unikátní jméno souboru s pomocí času a data.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        assert file.filename is not None
        file_ext = file.filename.split(".")[-1]
        saved_filename = f"{filename}_{timestamp}.{file_ext}"
        
        # ulož to
        file_path = os.path.join(UPLOAD_DIR, saved_filename)
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # ulož informaci o souboru do tinydb
        file_info = {
            "collection": "uploads",
            "filename": filename,
            "saved_filename": saved_filename,
            "original_name": file.filename,
            "file_size": len(content),
            "file_path": file_path,
            "upload_time": timestamp,
            "file_extension": file_ext
        }
        db.insert(file_info)

        return {
            "status": "success",
            "filename": saved_filename,
            "original_name": file.filename,
            "size": len(content),
            "saved_path": file_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{filename}")
async def download_file(
    filename: str
):
    ...

@router.get("/list_filenames")
async def list_filenames():
    ...
