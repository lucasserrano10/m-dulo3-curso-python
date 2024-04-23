matriz1 = [[], [], []]
contM1 = 0
matriz2 = [[], [], []]
contM2 = 0
matriz3 = [[], [], []]
contM3 = 0
somaPares = 0
somaLinhaTres = 0
for c in range(1,10):
    num = int(input(f'DIGITE O {c} NÚMERO: '))
    if num % 2 == 0:
        somaPares += num
    if c >= 0 and c <= 3:
        matriz1[contM1].append(num)
        contM1 += 1
    elif c >= 4 and c <= 6:
        matriz2[contM2].append(num)
        contM2 += 1
    else:
        somaLinhaTres += num
        matriz3[contM3].append(num)
        contM3 += 1
print(f'-=-'*25)
print(matriz1)
print(matriz2)
print(matriz3)
print(f'A SOMA DOS VALORES PARES DIGITADOS SÃO {somaPares}')
print(f'A SOMA DOS VALORES DA LINHA 3 SÃO {somaLinhaTres}')
sorted(matriz2)
print(f'O MAIOR VALOR DA LINHA 2 É O {matriz2[2]}')
print(f'-=-'*25)

