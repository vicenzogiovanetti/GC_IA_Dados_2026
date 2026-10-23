from fastapi import FastApi

app = FastApi()

@app.get("/")
def home():
    return {"olá":"Mundo!"}

