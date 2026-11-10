from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "GIGA backend is running"}
