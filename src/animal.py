from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware


app =FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str 


banco: List[Animal] = []

@app.get('/animais')
def listar_animais():
    return banco

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None

@app.get('/animais/{id_animal}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'error': 'animal não localizado'}

@app.delete('/animais/{id_animal}')
def remover_animal(animal_id: str):
    posicao = -1
    for index, animal in enumerate (banco): #buscar a posição do animal
        if animal.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem' : 'animal removido com sucesso'}
    
    else:
        return {'error' : 'animal não localizado'}


uvicorn.run(app, host="127.0.0.1", port = 8086)