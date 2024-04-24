from random import randint
print(f'-=-'*10)
print('     MEGA SENA     ')
print(f'-=-'*10)
lista = []
jogos = []
quant = int(input('QUANTOS JOGOS VOCÊ QUER QUE EU SORTEIE: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'-=-'*3,f'SORTEANDO {quant} JOGOS',f'-=-'*3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')