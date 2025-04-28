from pydantic import BaseModel

class VeiculoBase(BaseModel):
  nome: str
  ano_fabricacao: int
  ano_modelo: int
  valor: float


class Veiculo(VeiculoBase):
  id: int | None = None

class VeiculoCreate(VeiculoBase):
  pass
