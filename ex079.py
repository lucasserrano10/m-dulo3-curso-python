valores = []
while True:
    num = int(input('DIGITE UM NÚMERO: '))
    if valores.count(num):
        print('VALOR JÁ TINHA SIDO CADASTRADO !')
    else:
        valores.append(num)
        print('CADASTRADO COM SUCESSO !')
    continuar = input('DESEJA CONTINUAR [S/N]: ').strip().upper()
    if continuar == 'N':
        break
print(f'-=-'*45)
print(f'VALORES CADASTRADOS {valores}')
