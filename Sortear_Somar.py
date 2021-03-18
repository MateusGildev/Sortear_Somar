import random
from time import sleep

def sorteia(lista):
    print("~="*30)
    print("Sorteando os 5 valores da lista --> ", end='')
    for cont in range(0,5):
        n = random.randint(0,30)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print("PRONTO !!!")
        

def SomaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print("Somando os valores pares de {}, temos {}".format(lista, soma))
    print("~="*30)

valores = list()
sorteia(valores)
SomaPar(valores)

