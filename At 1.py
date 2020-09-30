lista = []
while True:
    recebe_lista = int(input(
        "digite os numeros de rebeldes ou digite 0 para sair: "))
    if recebe_lista > 0:
        lista.append(recebe_lista)
    else:
        print(lista)
        break


def maiornumero(l):
    meunumero_maior = l[0]
    for num in l:
        if meunumero_maior < num:
            meunumero_maior = num
    return meunumero_maior


def menornumero(l):
    meunumero_menor = l[0]
    for num in l:
        if meunumero_menor > num:
            meunumero_menor = num
    return meunumero_menor


def media(l):
    soma = 0
    for a in l:
        soma = soma + a

    media = soma / len(lista)
    return media


def comparacao(list):

    avg = sum(list) / len(list)
    diffs = {value: abs(value - avg) for value in list}

    return min(diffs, key=diffs.get)


print("menor numero", menornumero(lista))
print("maior numero", maiornumero(lista))
print("media", media(lista))
print("numero aproximado da média", comparacao(lista))
