# https://www.freecodecamp.org/news/work-with-sqlite-in-python-handbook/
import sqlite3

from modelos import Veiculo


class VeiculoDAO():
  
  def __init__(self):
    pass

  def todos(self):
    with sqlite3.connect('veiculos.db') as connection:
      cursor = connection.cursor()

      select_query = 'SELECT * from Veiculos;'
      cursor.execute(select_query)

      veiculos_list = cursor.fetchall()

      veiculos: list[Veiculo] = []

      for v in veiculos_list:
        veiculo = Veiculo(
          id=v[0], 
          nome=v[1], 
          ano_fabricacao=v[2],
          ano_modelo=v[3], 
          valor=v[4]
        )

        veiculos.append(veiculo)

      return veiculos


  def obter_por_id(self, id: int):
    with sqlite3.connect('veiculos.db') as conn:
      cursor = conn.cursor()

      # sql injection
      sql = 'SELECT * FROM Veiculos where id = ?'
      cursor.execute(sql, (id,))
      result = cursor.fetchone()

      if not result:
        return None

      veiculo = Veiculo(
        id=result[0],
        nome=result[1], 
        ano_fabricacao=result[2],
        ano_modelo=result[3], 
        valor=result[4]
      )

      return veiculo
  
  
  
  
  
  def remover_por_id(self, id: int):
    pass

  def atualizar(self, id: int, veiculo: Veiculo):
    pass

  def inserir(self, veiculo: Veiculo):
    pass