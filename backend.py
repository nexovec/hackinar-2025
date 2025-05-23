from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import os
from tinydb import TinyDB, Query
from file_upload import router as upload_router
from graph_config import router as config_router

app = FastAPI()


# CORS konfigurace
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routery, skupiny endpointů
app.include_router(upload_router, prefix="/api/files", tags=["file_upload"])
app.include_router(config_router, prefix="/api/graph", tags=["graph_config"])

@app.get("/")
def read_root():
    return {"message": "FastAPI File Upload and Graph Configuration Service"}
