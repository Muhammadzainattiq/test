from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"ABCD {os.environ.get('NAME')}"}