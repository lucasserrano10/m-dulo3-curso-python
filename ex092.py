alunos = {}
alunos['Nome'] = str(input('NOME DO ALUNO: '))
alunos['Média'] = float(input('MÉDIA DO ALUNO: '))
if alunos['Média'] <= 6.9:
    alunos['Situação'] = 'REPROVADO'
else:
    alunos['Situação'] = 'APROVADO'
for v,k in alunos.items():
    print(f'{v} é igual a {k}')
