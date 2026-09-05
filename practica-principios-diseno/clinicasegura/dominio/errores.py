class ErrorDominio(Exception): pass #Este es el tata de los otros 3, el error principal por default

#Estos 3 son los hijos que busca el test_1
class RecetaInvalida(ErrorDominio): pass #Para datos basura o no validos
class CadenaNoSoportada(ErrorDominio): pass #Si la farmacia no existe
class FarmaciaNoDisponible(ErrorDominio): pass #La farmacia no responde 
