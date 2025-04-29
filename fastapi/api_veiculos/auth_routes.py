from fastapi import APIRouter

router = APIRouter()

@router.post('/auth/signin')
def login():
  ...

@router.post('/auth/signup')
def signup():
  ...

@router.post('/auth/forget-password')
def forget_password():
  ...