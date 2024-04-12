num = (int(input('DIGITE UM NÚMERO: ')),int(input('DIGITE OUTRO NÚMERO: '))
       ,int(input('DIGITE OUTRO NÚMERO: ')), int(input('DIGITE OUTRO NÚMERO: ')))
print(f'=*'*30)
print(f'VOCÊ DIGITOU OS VALORES {num}')
print(f'=*'*30)
print(f'O VALOR 9 APARECEU {num.count(9)} VEZ')
print(f'=*'*30)
if 3 in num:
    print(f'O PRIMEIRO VALOR 3 ESTÁ NA POSIÇÃO {num.index(3)}')
else:
    print('VALOR 3 NÃO FOI DIGITADO !')
print(f'=*'*30)
print('OS VALORES PARES FORAM:')
for n in num:
    if n % 2 == 0:
        print(n)
