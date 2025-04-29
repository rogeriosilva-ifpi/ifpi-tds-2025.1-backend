from fastapi import APIRouter

app = APIRouter()

@app.get('/montadoras')
def montadoras_list():
  ...