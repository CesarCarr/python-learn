def remove_repetidos(lista):
    lista2 = sorted(lista[:])
    lista3 = []
    for x in lista2:
        if x not in lista3:
            lista3.append(x)
    return lista3
