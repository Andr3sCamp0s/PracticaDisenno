import pytest
from datetime import datetime
from clinicasegura.dominio.modelos import Receta, Cedula, Despacho
from clinicasegura.dominio.servicio import EmisionDeRecetas

# Objetos de mentira súper sencillos para simular las herramientas
class RelojFijo:
    def ahora(self):
        return datetime(2026, 5, 1, 12, 0, 0)

class FolioFijo:
    def siguiente(self):
        return "F-001"

class BitacoraVacia:
    def registrar(self, evento, folio):
        pass  # No hace nada, solo cumple con el requisito

class PasarelaNormal:
    def enviar(self, receta, folio, vence):
        return Despacho(folio=folio, cadena="test", vence=vence)

class PasarelaCaida:
    def enviar(self, receta, folio, vence):
        raise TimeoutError("Error de red")


# 1) Prueba de vigencia con reloj fijo
def test_vigencia_reloj_fijo():
    servicio = EmisionDeRecetas({"test": PasarelaNormal()}, RelojFijo(), FolioFijo(), BitacoraVacia())
    receta = Receta(Cedula("1-1234-5678"), "N02B", 10, 500.0)
    
    despacho = servicio.emitir(receta, "test")
    assert despacho.vence == datetime(2026, 5, 31, 12, 0, 0)

# 2) Prueba de la farmacia caída
def test_farmacia_caida():
    servicio = EmisionDeRecetas({"caida": PasarelaCaida()}, RelojFijo(), FolioFijo(), BitacoraVacia())
    receta = Receta(Cedula("1-1234-5678"), "N02B", 10, 500.0)
    
    with pytest.raises(TimeoutError):
        servicio.emitir(receta, "caida")

# 3) Prueba de la receta con cédula inválida
def test_cedula_invalida():
    with pytest.raises(ValueError):
        Receta(Cedula("1234-5678"), "N02B", 10, 500.0)


#La vdd aqui le pedi ayuda a chat para saber que cosas podia testear y como hacerlas secillas.