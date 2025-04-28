from fastapi import FastAPI, HTTPException, status
from modelos import VeiculoCreate
from veiculos_dao import VeiculoDAO

app = FastAPI()


veiculos_dao = VeiculoDAO()


@app.post('/veiculos', status_code=status.HTTP_201_CREATED)
def veiculos_create(novo: VeiculoCreate):
  veiculo  = veiculos_dao.inserir(novo)

  return veiculo


@app.get('/veiculos')
def veiculos_list():
  veiculos = veiculos_dao.todos()
  return veiculos


@app.get('/veiculos/{id}')
def veiculos_detail(id: int):
  veiculo = veiculos_dao.obter_por_id(id)

  if veiculo:
    return veiculo
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Não existe um veículo com id = {id}'
    )
  
@app.delete('/veiculos/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_veiculo(id:int):
  if veiculos_detail(id):
    veiculos_dao.remover_por_id(id)
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Não existe um veículo com id = {id}'
    )

