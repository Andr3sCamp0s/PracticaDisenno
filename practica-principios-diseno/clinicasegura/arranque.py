import os
from clinicasegura.dominio.servicio import EmisionDeRecetas

def construir_servicio() -> EmisionDeRecetas:
    timeout = os.getenv("FARMACIA_TIMEOUT_MS", "1500")
    
    return EmisionDeRecetas(
        pasarelas={},
        reloj=None,
        folios=None,
        bitacora=None
    )

#Desde aca empieza a correr el codigo y llama a los otrso servicios 