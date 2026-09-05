from dataclasses import dataclass

@dataclass(frozen=True)
class Cedula: 
    valor: str

@dataclass(frozen=True)
class Receta:
    cedula: str
    dias: int
    dosis_mg: float
    riesgo_alto: bool

@dataclass(frozen=True)
class Despacho:
    folio: str
    vence_iso: str
    recargo: float
    cadena: str
