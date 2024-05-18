cidadao = {}
cidadao['Nome'] = str(input('NOME ->'))
anoNascimento = int(input('ANO DE NASCIMENTO ->'))
cidadao['Idade'] = 2024 - anoNascimento
cidadao['ctps'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM) ->'))
if cidadao['ctps'] !=0:
    cidadao['contratacao'] = int(input('Ano de contratação ->'))
    cidadao['salario'] = int(input('SALÁRIO -> R$ '))
    cidadao['ano da aposentadoria'] = 35 + cidadao['contratacao']
print(f'='*25)
for v, k in cidadao.items():
    print(f'{v} <--> {k}')