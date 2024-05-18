from time import sleep
import random
from operator import itemgetter
print()
print('<--VALORES SORTEADOS-->')
print()
jogadores = {}
for c in range(1,6):
    jogadores[f'JOGADOR {c}'] = random.randint(1,6)
    sleep(1)
    print(f'JOGADOR {c} -> {jogadores[f'JOGADOR {c}']}')
print()
print('<--RANKING DOS GANHADORES-->')
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
for i, v in enumerate(ranking):
    print(f'{i+1}* Lugar -- > {v[0]} --- {v[1]} score')
    sleep(1)