from time import sleep
ficha = []
while True:
    nome = str(input('NOME :'))
    n1 = float(input('NOTA 1 :'))
    n2 = float(input('NOTA 2 :'))
    media = ((n1+n2)/2)
    ficha.append([nome,[n1,n2],media])
    continuar = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'-=-'*25)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print(f'-'*25)
    opc = int(input('MOSTRAR NOTAS DE QUAL ALUNO [999-INTERROMPE]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'NOTAS DE {ficha[opc][0]} SÃO {ficha[opc][1]}')
sleep(2)
print('<<<VOLTE SEMPRE>>>')