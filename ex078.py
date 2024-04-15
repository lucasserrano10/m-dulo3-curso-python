valores = []
for v in range(0,5):
    num = int(input('DIGITE UM VALOR: '))
    valores.append(num)
valores.sort()
print(f'VALORES DIGITADOS {valores}')
print(f'MAIOR VALOR DIGITADO {valores[4]}')
print(f'MENOR VALOR DIGITADO {valores[0]}')