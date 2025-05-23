from fastapi import APIRouter, Form, HTTPException
from tinydb import TinyDB, Query
from tinydb import TinyDB
from pathlib import Path

# Nastav TinyDB
DB_PATH = "db/graph_config.json"
Path("db").mkdir(parents=True, exist_ok=True)
db = TinyDB(DB_PATH)
# from tinydb_setup import db

router = APIRouter()

GraphConfig = Query()

@router.post("/configure")
async def configure_graph(
    filename: str = Form(...),
    color: str = Form("#3366cc"),  # Default color
    line_width: int = Form(2)
):
    try:
        # zkus najít
        existing = db.search(GraphConfig.filename == filename)
        
        if existing:
            # uprav
            db.update(
                {
                    "color": color,
                    "line_width": line_width
                },
                GraphConfig.filename == filename & GraphConfig.collection == "configuration"
            )
        else:
            # vlož
            db.insert({
                "collection": "configuration",
                "filename": filename,
                "color": color,
                "line_width": line_width,
            })
        
        return {
            "status": "success",
            "filename": filename,
            "color": color,
            "line_width": line_width
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/config/{filename}")
async def get_graph_config(filename: str):
    try:
        result = db.search(GraphConfig.filename == filename)
        if not result:
            raise HTTPException(
                status_code=404,
                detail=f"No configuration found for filename: {filename}"
            )
        return result[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/configs")
async def get_all_configs():
    try:
        return db.all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
