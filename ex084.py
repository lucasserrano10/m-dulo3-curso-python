cadastrados = []
dados = []
peso = []
c = 0
quantidadeCadastrados = 0
while True:
    dados.append(str(input('NOME :')))
    dados.append(int(input('PESO :')))
    print(f'-=-'*35)
    print('CADASTRADO COM SUCESSO !')
    print(f'-=-' * 35)
    cadastrados.append(dados[:])
    quantidadeCadastrados += 1
    peso.append(cadastrados[c][1])
    c +=1
    dados.clear()
    continuar = str(input('QUER CONTINUAR [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
sorted(peso)
print(f' QUANTIDADE DE PESSOAS CADASTRADAS :{quantidadeCadastrados}')
print(f'-=-' * 35)
print(f' MAIOR PESO É : {peso[quantidadeCadastrados-1]}')
print(f'-=-' * 35)
print(f' MENOR PESO É : {peso[0]}')