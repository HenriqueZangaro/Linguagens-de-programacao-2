from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"Mensagem": "Minha primeira api com FastAPI"}

