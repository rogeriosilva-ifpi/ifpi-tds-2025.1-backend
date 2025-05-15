from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
  hash = pwd_context.hash(password)
  return hash


def verify_hash_password(password: str, hash_password: str):
  return pwd_context.verify(password, hash_password)



def is_valid_password(password: str):
  '''
    Tamanho: no mínimo 8 caracteres
    Conter números, letras minusculas, 
    maiúsculas, caracter especiais
  '''
  if len(password) < 6:
    return False

  if not contem_numero(password):
    return False

  return True


def contem_numero(text: str):
  numeros = '1234567890'

  for caractere in text:
    if caractere in numeros:
      return True
  
  return False