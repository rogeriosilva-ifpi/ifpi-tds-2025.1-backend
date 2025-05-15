from pydantic import BaseModel

class UsuarioBase(BaseModel):
  nome: str
  email: str
  senha: str

class Usuario(UsuarioBase):
  id: int | None = None


class SignUpUser(UsuarioBase):
  pass


class SignInUser(BaseModel):
  email: str
  senha: str


class VeiculoBase(BaseModel):
  nome: str
  ano_fabricacao: int
  ano_modelo: int
  valor: float


class Veiculo(VeiculoBase):
  id: int | None = None

class VeiculoCreate(VeiculoBase):
  pass
