from fastapi import FastAPI, HTTPException

app = FastAPI()

frutas = [
  {'id': 1, 'nome': 'Banana', 'citrica': False}, 
  {'id': 2, 'nome': 'Maça', 'citrica': True}, 
  {'id': 3, 'nome': 'Melancia', 'citrica': False},
  {'id': 4, 'nome': 'Acerola', 'citrica': True}
]

@app.get('/frutas')
def frutas_list(order: str = None, citrico: str = None):

  frutas_friltradas = []
  if citrico:
    # filtra a lista de frutas e mandar somente as citricas
    if citrico == '1':
      for fruta in frutas:
        if fruta['citrica'] == True:
          frutas_friltradas.append(fruta)
    elif citrico == '0':
      for fruta in frutas:
        if fruta['citrica'] == False:
          frutas_friltradas.append(fruta)
    else:
      raise HTTPException(status_code=400, detail='Cítrico deve ser 1 ou 0')
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
    raise HTTPException(status_code=404, detail='Fruta não localizada!')
    


@app.post('/frutas', status_code=201)
def frutas_create():
  frutas.append('Manga')
  return {'nome': 'Manga'} 


# Utilizados
def obter_fruta_por_id(id: int):
  for fruta in frutas:
    if fruta['id'] == id:
      return fruta
  
  return None