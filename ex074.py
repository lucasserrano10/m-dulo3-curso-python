import random
numeros = [0,1,2,3,4,5,6,7,8,9,10]

num1 = random.choice(numeros)
num2 = random.choice(numeros)
num3 = random.choice(numeros)
num4 = random.choice(numeros)
num5 = random.choice(numeros)

numerosAletorios = (num1, num2, num3,num4,num5)
print(f'OS NÚMEROS SORTEADOS FORAM {numerosAletorios}')
print(f'MENOR NÚMERO: {sorted(numerosAletorios)[0]}')
print(f'MAIOR NÚMERO: {sorted(numerosAletorios)[4]}')