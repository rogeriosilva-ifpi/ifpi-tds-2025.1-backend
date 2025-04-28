from fastapi import FastAPI, HTTPException, status
from veiculos_dao import VeiculoDAO

app = FastAPI()


veiculos_dao = VeiculoDAO()

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
