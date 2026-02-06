# union types permite que uma variavel seja uma string ou nenhum tipo
from typing import Union 

from fastapi import FastAPI

# instancia do fast api para criar os endpoints
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# rota de item com route param {item_id}
@app.get("/items/{item_id}")
# segundo argumento é um query param 'q' opcional do tipo union de str ou None com valor default None
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}