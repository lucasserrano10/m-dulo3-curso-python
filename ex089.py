import random
print(f'-=-'*30)
print('MEGA SENA')
print(f'-=-'*30)
numerosPossiveis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
qtdade = int(input('QUANTOS JOGOS VOCÊ QUER QUE EU SORTEIE: '))
aux = 0
jogo = []
print('=-=SORTEANDO JOGOS=-=')
for c in range(0,qtdade):
    while aux <= 9:
        escolha = random.choice(numerosPossiveis)
        jogo.append(escolha)
        aux += 1
    print(f'JOGO {c + 1}:{jogo}')
    jogo.clear()
print('=-=-=-=-=-BOA SORTE=-==-=-=-=-')
