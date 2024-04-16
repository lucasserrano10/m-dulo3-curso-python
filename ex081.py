valores = []
while True:
    num = int(input('DIGITE UM NÚMERO :'))
    valores.append(num)
    continuar = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'-=-'*30)
print(len(valores))
print(f'-=-'*30)
valores.sort(reverse=True)
print(f'VALORES DE FORMA DECRESCENTE - {valores}')
print(f'-=-'*30)
if valores.count(5) == True:
    print('O VALOR 5 ESTÁ NA LISTA')
else:
    print('O VALOR 5 NÃO ESTÁ NA LISTA')