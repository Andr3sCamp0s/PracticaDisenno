from decimal import Decimal
from pydantic import BaseModel, Field
from clinicasegura.dominio.modelos import Receta, Cedula

class SolicitudReceta(BaseModel):
    # Se verifica el patrón 0-0000-0000
    cedula: str = Field(pattern=r"^\d{1}-\d{4}-\d{4}$")
    medicamento: str
    dias: int = Field(gt=0, le=90)  # Mayor a 0 y menor o igual a 90 días
    dosis_mg: Decimal = Field(gt=0) # Mayor a 0 

    model_config = {
        "extra": "forbid",
        "frozen": True
    }

def a_receta(solicitud: SolicitudReceta):
    return Receta(
        cedula=Cedula(solicitud.cedula),
        medicamento=solicitud.medicamento,
        dias=solicitud.dias,
        dosis_mg=solicitud.dosis_mg
    )

#Aqui se tranforma la soli en objetos del dominio