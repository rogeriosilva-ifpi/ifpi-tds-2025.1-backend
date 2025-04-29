from fastapi import APIRouter, HTTPException, status
from modelos import VeiculoCreate
from veiculos_dao import VeiculoDAO

roteador_veiculos = APIRouter()

veiculos_dao = VeiculoDAO()

@roteador_veiculos.post('/veiculos', status_code=status.HTTP_201_CREATED)
def veiculos_create(novo: VeiculoCreate):
  veiculo  = veiculos_dao.inserir(novo)

  return veiculo


@roteador_veiculos.get('/veiculos')
def veiculos_list():
  veiculos = veiculos_dao.todos()
  return veiculos


@roteador_veiculos.get('/veiculos/{id}')
def veiculos_detail(id: int):
  veiculo = veiculos_dao.obter_por_id(id)

  if veiculo:
    return veiculo
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Não existe um veículo com id = {id}'
    )
  
@roteador_veiculos.delete('/veiculos/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_veiculo(id:int):
  if veiculos_detail(id):
    veiculos_dao.remover_por_id(id)
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Não existe um veículo com id = {id}'
    )
