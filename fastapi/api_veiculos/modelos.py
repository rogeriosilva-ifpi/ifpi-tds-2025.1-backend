from pydantic import BaseModel


class Veiculo(BaseModel):
  id: int | None = None
  nome: str
  ano_fabricacao: int
  ano_modelo: int
  valor: float