from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from auth_utils import get_current_user
from modelos import Usuario, VeiculoCreate
from veiculos_dao import VeiculoDAO

roteador_veiculos = APIRouter()

veiculos_dao = VeiculoDAO()

# Abreviação / Alias para Tipo
LoggedUser = Annotated[Usuario, Depends(get_current_user)]

@roteador_veiculos.post('/veiculos', status_code=status.HTTP_201_CREATED)
def veiculos_create(novo: VeiculoCreate, user: LoggedUser):

  veiculo  = veiculos_dao.inserir(novo, user)

  return veiculo


@roteador_veiculos.get('/veiculos')
def veiculos_list(user: LoggedUser):
  veiculos = veiculos_dao.todos_por_usuario(user)
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
