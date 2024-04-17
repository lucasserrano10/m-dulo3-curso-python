matriz1 = [[], [], []]
contM1 = 0
matriz2 = [[], [], []]
contM2 = 0
matriz3 = [[], [], []]
contM3 = 0
for c in range(1,10):
    num = int(input(f'DIGITE O {c} NÚMERO: '))
    if c >= 0 and c <= 3:
        matriz1[contM1].append(num)
        contM1 += 1
    elif c >= 4 and c <= 6:
        matriz2[contM2].append(num)
        contM2 += 1
    else:
        matriz3[contM3].append(num)
        contM3 += 1
print(f'-=-'*25)
print(matriz1)
print(matriz2)
print(matriz3)
print(f'-=-'*25)

