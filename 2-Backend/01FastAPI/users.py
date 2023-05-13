from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# peticion usuarios ->
@app.get("/users")
async def users():
    return [
        {"name": "martin", "surnmae": "gvn", "url": "https://martin.dev"},
        {"name": "lucas", "surname": "lan", "url": "https://lucas.dev"},
        {"name": "ramiro", "surname": "pwa", "url": "https://ramiro.dev"}
    ]

#
