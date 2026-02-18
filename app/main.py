from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI works!"}

@app.get("/db")
def check_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"error": str(e)}
