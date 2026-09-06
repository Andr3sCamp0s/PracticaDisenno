from datetime import timedelta
from clinicasegura.dominio.modelos import Receta, Despacho
from clinicasegura.dominio.errores import CadenaNoSoportada, FarmaciaNoDisponible

class EmisionDeRecetas:
    def __init__(self, pasarelas: dict, reloj, folios, bitacora):
        self.pasarelas = pasarelas
        self.reloj = reloj
        self.folios = folios
        self.bitacora = bitacora

    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        # Buscamos en el mapa de registro dinámico
        if cadena not in self.pasarelas:
            raise CadenaNoSoportada(f"La farmacia {cadena} no está registrada")
            
        pasarela = self.pasarelas[cadena]
        
        # Obtenemos los valores usando los puertos que creamos en puertos.py
        folio = self.folios.siguiente()
        ahora = self.reloj.ahora()
        vence = ahora + timedelta(days=30)
        
        try:
                resultado = pasarela.enviar(receta, folio, vence)
                self.bitacora.registrar("emitida", folio)
                return resultado
        except TimeoutError:
            # Si falla, dejamos rastro en la bitácora y mandamos el error
            self.bitacora.registrar("fallida", folio)
            raise FarmaciaNoDisponible(f"La farmacia {cadena} no respondió para el folio {folio}")
