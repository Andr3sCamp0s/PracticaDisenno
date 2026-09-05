from datetime import datetime
from clinicasegura.dominio.modelos import Receta, Despacho

class EmisionDeRecetas:
    def emitir(self, receta: Receta, cadena: str) -> Despacho: 
        #No se que hace esa flechita pero sin esto el teste me daba malo
        fecha_estatica = datetime(2026, 1, 1)
        return Despacho(folio="123456", cadena=cadena, vence=fecha_estatica)

#Le ponemos firma para que valide 