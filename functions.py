import random

def gerarLista():
    user_input = input("Qual o tamanho da Lista a ser gerada? ")
    n = int(user_input)
    S = []
    for i in range(n):
        S.append(random.randint(0, n))

    print("Lista gerada: ", S)
    return S

def search(lista):

    user_input = input("Qual elemento deseja buscar? ")
    x = int(user_input)
    i = 0

    while(len(lista) > i):

        if x == lista[i]:
            print(i)
            return i
            break

        i = i + 1

def moda(lista):
    #moda = mode(lista)
    lista_dic = {}

    for l in lista:
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            lista_dic[l] += 1

    maior_repeticao = max(lista_dic.values())

    for i in lista_dic:
        if lista_dic[i] == maior_repeticao:
            moda = i

    print ("A moda da lista é: ", moda)
    return moda