import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass(frozen=True)
class Cedula:
    valor: str

    def __post_init__(self):
        p = self.valor.split("-") #Use la misma funcion que tenia en reglas
        return len(p) == 3 and len(p[0]) == 1 and len(p[1]) == 4 and len(p[2]) == 4 and all(x.isdigit() for x in p)

@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    medicamento: str  #Agregamos este campo que pide el test de la etapa 4
    dias: int
    dosis_mg: Decimal
    riesgo_alto: bool = False  #Por defecto

@dataclass(frozen=True)
class Despacho:
    folio: str
    cadena: str
    vence: datetime
