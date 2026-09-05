from clinicasegura.dominio.errores import RecetaInvalida
from clinicasegura.dominio.modelos import Receta
from decimal import Decimal

def validar_formato_cedula(c: str):
    p = c.split("-") #Se ve el formato x-xxxx-xxxx valida el tamaño entre guiones 1-4-4 y que todo sea digito
    return len(p) == 3 and len(p[0]) == 1 and len(p[1]) == 4 and len(p[2]) == 4 and all(x.isdigit() for x in p)

def calcular_recargo(dias_restantes: int, tarifa_diaria: Decimal, recargo_por_riesgo: bool):
    if dias_restantes <= 0: #Ya aca quedo mejor sin varas globales
        return Decimal("0")
    if recargo_por_riesgo:
        return tarifa_diaria * dias_restantes * 2
    return tarifa_diaria * dias_restantes
