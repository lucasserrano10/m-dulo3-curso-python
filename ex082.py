gerais = []
pares = []
impares = []
while True:
    num = int(input('DIGITE UM NÚMERO: '))
    if num % 2 == 0:
        gerais.append(num)
        pares.append(num)
    else:
        gerais.append(num)
        impares.append(num)
    continuar = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'-=-'*30)
print(f'TODOS OS VALORES DIGITADOS - {gerais}')
print(f'-=-'*30)
print(f'VALORES PARES DIGITADOS - {pares}')
print(f'-=-'*30)
print(f'VALORES ÍMPARES DIGITADOS - {impares}')