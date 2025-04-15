from fastapi import FastAPI
from veiculos_dao import VeiculosDAO

app = FastAPI()




veiculos_dao = VeiculosDAO()

@app.get('/veiculos')
def veiculos_list():
  veiculos = veiculos_dao.todos()
  return veiculos
