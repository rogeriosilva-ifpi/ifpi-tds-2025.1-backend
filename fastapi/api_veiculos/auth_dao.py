import sqlite3
from modelos import SignUpUser, Usuario


class AuthDAO():

  def __init__(self):
    pass


  def buscar_usuario_por_email(self, email: str):
    with sqlite3.connect('veiculos.db') as conn:
      cursor = conn.cursor()
      sql = 'SELECT * FROM Usuarios where email = ?'
      cursor.execute(sql, (email,))
      result = cursor.fetchone()

      if not result:
        return None

      usuario = Usuario(
        id=result[0], nome=result[1], 
        email=result[2], senha=result[3], 
      )

      return usuario
  
  def salvar(self, usuario: SignUpUser):
    with sqlite3.connect('veiculos.db') as conn:
      cursor = conn.cursor()

      sql = '''INSERT INTO usuarios(nome, email, senha)
              VALUES (?, ?, ? )'''
      
      cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha))

      id = cursor.lastrowid

      return Usuario(id=id, **usuario.dict())