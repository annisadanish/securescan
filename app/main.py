from fastapi import FastAPI

app = FastAPI(title="SecureScan")

@app.get("/")
def read_root():
    return {"message": "SecureScan API is running"}
