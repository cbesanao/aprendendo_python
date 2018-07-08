def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

print (maior((1,5,4,64,8,15,65,11,0)))


def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print (menor((65,54,84,68,18,83,91,55,6,4,63)))
