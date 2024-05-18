'''locadora = [{'modelo':'onix', 'ano':2020},{'modelo':'hb20','ano':2023}]
print(locadora[1])
for k, v in filme.items():
    print(f'O {k} é {v}')

pessoa = {'nome':'lucas','sexo':'M','idade':18}
print(f'O {pessoa['nome']} que é do sexo {pessoa['sexo']} tem {pessoa['idade']} anos')
print('-=-')
print(pessoa.keys())
print('-=-')
print(pessoa.values())
print('-=-')
print(pessoa.items())
del pessoa['sexo']
pessoa['nome'] = 'LUQUEBA'
pessoa['peso'] = 98.6
for k, v in pessoa.items():
    print(f'{k} == {v}')'''

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('UNIDADE FEDERATIVA -> '))
    estado['sigla'] = str(input('SIGLA -> '))
    brasil.append(estado.copy())
for e in brasil:
    for v, k in e.items():
        print(f'{v}--{k}')
        print()