cadastradas = []
pessoa = {}
soma = 0
media = 0
while True:
    pessoa['Nome'] = str(input('DIGITE SEU NOME :'))
    pessoa['Idade'] = int(input('DIGITE SUA IDADE :'))
    pessoa['Sexo'] = str(input('DIGITE SEU SEXO [M/F]:')).strip().upper()
    while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        pessoa['Sexo'] = str(input('DIGITE SEU SEXO [M/F]:')).strip().upper()
    cadastradas.append(pessoa.copy())
    continuar = str(input('QUER CONTINUAR ? [S/N] ->')).upper()
    if continuar == 'N':
        break
print('-'*35)
print(f'A) Ao todo temos {len(cadastradas)} pessoas cadastradas !')
media = soma / len(cadastradas)
print(f'B) A Média de idade é de {media}')