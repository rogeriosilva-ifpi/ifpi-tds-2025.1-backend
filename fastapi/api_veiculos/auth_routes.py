from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException

from auth_dao import AuthDAO
from auth_utils import create_jwt_token, get_current_user, hash_password, is_valid_password, verify_hash_password
from modelos import  SignInUser, SignUpUser, Usuario

router = APIRouter()

auth_dao = AuthDAO()

@router.post('/auth/signin')
def login(data: SignInUser):
  usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

  if not usuario_existente:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'Email e/ou senha incorreto(s)!')
  
  if not verify_hash_password(data.senha, usuario_existente.senha):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'Email e/ou senha incorreto(s)!')
  
  access_token = create_jwt_token(usuario_existente.email)
  
  return {
    'username': usuario_existente.nome,
    'access_token': access_token}


@router.post('/auth/signup', status_code=status.HTTP_201_CREATED)
def signup(data: SignUpUser):
  usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

  if not is_valid_password(data.senha):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'A senha não atende aos critérios.')

  if usuario_existente:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'Já existe um usuário com email {data.email}.')

  data.senha = hash_password(data.senha)
  usuario = auth_dao.salvar(data)

  return usuario

@router.post('/auth/forget-password')
def forget_password():
  ...


@router.get('/auth/me')
def me(user: Annotated[Usuario, Depends(get_current_user)]):
  return {
    'name': user.nome,
    'email': user.email
  }