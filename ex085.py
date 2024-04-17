valores = [[], []]
for c in range(1,8):
    num = int(input(f'DIGITE O {c} NÚMERO :'))
    c += 1
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f'-=-'*20)
print(f'OS VALORES PARES SÃO {valores[0]}')
print(f'-=-'*20)
print(f'OS VALORES IMPARES SÃO {valores[1]}')