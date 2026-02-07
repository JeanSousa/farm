# union types permite que uma variavel seja uma string ou nenhum tipo
from typing import Union 

from fastapi import FastAPI

from pydantic import BaseModel

# instancia do fast api para criar os endpoints
app = FastAPI()

# links de acesso as docs swagger e redock
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


# classe que herda BaseModel do pydantic 
# além de validar os tipos ela lê os TYPE HINTS e consegue criar o constructor sozinha
class Item(BaseModel):
    name: str 
    price: float 
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

# rota de item com route param {item_id}
@app.get("/items/{item_id}")
# segundo argumento é um query param 'q' opcional do tipo union de str ou None com valor default None
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}