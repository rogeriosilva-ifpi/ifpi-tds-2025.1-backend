from fastapi import FastAPI
from veiculos_routes import roteador_veiculos
from auth_routes import router as roteador_auth
from montadoras_routes import app as roteador_montadoras

app = FastAPI()

# Rotas de Veículos
app.include_router(roteador_veiculos)

# Rotas de Autenticaco
app.include_router(roteador_auth)

# Rotas de Montadas
app.include_router(roteador_montadoras)



