from fastapi import FastAPI

app = FastAPI()


# Primera peticion con FastAPI ->
@app.get("/")
async def root():
    return ("Hola Mundo")


# Segunda peticion con otra direccion "/url" ->
@app.get("/url")
async def root():
    return {"curso": "https://martin.com"}
