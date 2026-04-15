from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Mensaje":"CRM Biomédico funcionando"}