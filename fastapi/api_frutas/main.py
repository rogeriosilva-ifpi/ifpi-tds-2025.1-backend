from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel

app = FastAPI()

class Fruta(BaseModel):
  id: int
  nome: str
  citrica: bool


class FrutaUpdate(BaseModel):
  nome: str
  citrica: bool


frutas = [
  {'id': 1, 'nome': 'Banana', 'citrica': False}, 
  {'id': 2, 'nome': 'Maça', 'citrica': True}, 
  {'id': 3, 'nome': 'Melancia', 'citrica': False},
  {'id': 4, 'nome': 'Acerola', 'citrica': True},
  {'id': 5, 'nome': 'Pêra', 'citrica': True}
]

@app.get('/frutas')
def frutas_list(order: str = None, 
                citrica: Annotated[str | None, Query(max_length=1, 
                                                     description='Filtra por cítrico')] = None):

  frutas_friltradas = []
  if citrica:
    # filtra a lista de frutas e mandar somente as citricas
    if citrica == '1':
      for fruta in frutas:
        if fruta['citrica'] == True:
          frutas_friltradas.append(fruta)
    elif citrica == '0':
      for fruta in frutas:
        if fruta['citrica'] == False:
          frutas_friltradas.append(fruta)
    
  else:
    frutas_friltradas = frutas

  
  if not order:
    return frutas_friltradas

  # ordenar
  if order == 'ASC':
    # ordem crescente por nome
    frutas_ordenadas = sorted(frutas_friltradas, key=lambda f:f['nome'])
    return frutas_ordenadas
  elif order == 'DESC':
    # ordem descresc. por nome
    frutas_ordenadas = sorted(frutas_friltradas, key=lambda f:f['nome'], reverse=True)
    return frutas_ordenadas
  else:
    raise HTTPException(status_code=400, detail='Order tem que ser ASC ou DESC')


@app.get('/frutas/{id}')
def frutas_detail(id: int):
  fruta_localizada = obter_fruta_por_id(id)

  if fruta_localizada:
    return fruta_localizada
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail='Fruta não localizada!')
    


@app.post('/frutas', status_code=status.HTTP_201_CREATED)
def frutas_create(fruta: Fruta):
  frutas.append({ "id": fruta.id, 
                 "nome": fruta.nome, 
                 "citrica": fruta.citrica})
  return frutas[-1]


@app.put('/frutas/{id}')
def frutas_update(id: int, fruta: FrutaUpdate):
  index = obter_index_fruta_por_id(id)

  if not index:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'Fruta não localizada (id={id})!')
  
  frutas[index]['nome'] = fruta.nome
  frutas[index]['citrica'] = fruta.citrica
  return frutas[index]
    

@app.delete('/frutas/{id}', status_code=status.HTTP_204_NO_CONTENT)
def frutas_remove(id: int):
  index = obter_index_fruta_por_id(id)
  
  if not index:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'Fruta não localizada (id={id})!')
  
  frutas.pop(index)




# Utilidades
def obter_fruta_por_id(id: int):
  for fruta in frutas:
    if fruta['id'] == id:
      return fruta
    

def obter_index_fruta_por_id(id: int):
  for index, fruta in enumerate(frutas):
    if fruta['id'] == id:
      return index
  
  return None