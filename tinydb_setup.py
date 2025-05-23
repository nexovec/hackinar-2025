from tinydb import TinyDB
from pathlib import Path

# Nastav TinyDB
DB_PATH = "db/graph_config.json"
Path("db").mkdir(parents=True, exist_ok=True)
db = TinyDB(DB_PATH)
