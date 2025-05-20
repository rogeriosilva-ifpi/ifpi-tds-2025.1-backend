from datetime import datetime, timezone, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext

from auth_dao import AuthDAO

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


SECRET_KEY = "rogerio2025ifpi-tds"
ALGORITHM = "HS256"

def create_jwt_token(email: str):
  expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  data = {
    'sub': email,
    'exp': expire
  }

  token = jwt.encode(data, SECRET_KEY, ALGORITHM)

  return token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_dao = AuthDAO()

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  try:
    data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = data['sub']
    user = auth_dao.buscar_usuario_por_email(email)
    return user
  except:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail='Token inválido ou Expirado!'
    )
