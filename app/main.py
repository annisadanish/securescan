from fastapi import FastAPI
from scanner import scan

app = FastAPI(title="SecureScan API")


@app.get("/")
def read_root():
    return {"message": "SecureScan API is running"}


@app.get("/scan/{target}")
def run_scan(target: str):
    return scan(target)
