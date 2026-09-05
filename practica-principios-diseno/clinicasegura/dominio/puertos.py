from typing import Protocol
from datetime import datetime
from clinicasegura.dominio.modelos import Receta

class Reloj(Protocol):
    def ahora(self): ... 
#Hoy aprendi que son estos 3 puntitos, sirven para decirle a python esta funcion va a quedar vacia

class GeneradorFolio(Protocol):
    def siguiente(self): ...

class Bitacora(Protocol):
    def registrar(self, folio: str, evento: str, cuando: datetime): ...

class Pasarela(Protocol):
    def enviar(self, receta: Receta, vence: datetime, folio: str, cadena: str): ...

#Creamos los contratos para no tener que estar dependiedo de randoms ni de la fecha dle sistema