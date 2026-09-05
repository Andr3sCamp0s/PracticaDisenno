def construir_registro(pasarelas: list):
    registro = {}
    for p in pasarelas:
        registro[p.cadena] = p
    return registro

#Esta amiga agarra la lista que se pasa por la pasarela y la convierte en diccionario con indices
