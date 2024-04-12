print(f'--'*30)
print('SUPERMERCADO GOOGLE')
print(f'--'*30)
listagem = ('CREATINA',130,
            'GLUTAMINA',95.9,
            'BOTOX',1000,
            'ALBUMINA',25.99)

for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>4.2f}')

