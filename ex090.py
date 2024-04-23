boletim = [[],[],[]]
cont = 0
while True:
    nome = str(input('NOME :'))
    boletim[0].append(nome)
    n1 = int(input('NOTA 1 :'))
    boletim[1].append(n1)
    n2 = int(input('NOTA 2 :'))
    boletim[2].append(n2)
    cont += 1
    continuar = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'No|||Nome|||Nota1||||Nota2')
print(f'======================')
print(f'{boletim[0][0]}\n {boletim[0][1]}')
