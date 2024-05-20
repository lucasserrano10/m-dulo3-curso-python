import random
from random import choice,randint
numeros = []
def sortear(lista):
    for cont in range(0,5):
        cont = randint(1,10)
        lista.append(cont)
    print(f'NÚMEROS SORTEADOS ! {lista}')
def somaPares(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A SOMA DOS VALORES PARES SÃO {soma}')

sortear(numeros)
print(f'='*30)
somaPares(numeros)