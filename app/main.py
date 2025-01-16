from fastapi import FastAPI,APIRouter,HTTPException
import sqlite3

app = FastAPI()
router = APIRouter()

DB_FILE = "merito.db"

# Utility function to execute database queries
def execute_query(query, params=(), fetch_all=True):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch_all:
            return cursor.fetchall()
        conn.commit()

@app.get("/")
def root():
    return {'message':'home Page'}

@app.get("/allbudget/")
def getAllBudget():
    query = 'SELECT * FROM budget'
    records = execute_query(query)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"data": records}