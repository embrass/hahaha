#uvicorn app.main:app --reload

from fastapi import FastAPI

app = FastAPI()



@app.get("/{name}")
def get_info(name: str):
    return {"Hello. H ow are you": name}

