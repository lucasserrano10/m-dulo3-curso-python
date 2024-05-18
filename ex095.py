jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome Do Jogador ->'))
total = int(input(f'Quantidade de Partidas de {jogador['Nome']} ->'))
for c in range(0,total):
    partidas.append(int(input(f'QUANTOS GOLS NA PARTIDA {c+1} ->')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')