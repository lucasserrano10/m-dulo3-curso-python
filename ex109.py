from uteis import numeros

n = int(input('DIGITE UM NÚMERO PARA SER MANIPULADO->'))
p = int(input('DIGITE UM NÚMERO INTEIRO QUE VAI SER USADO COMO PORCENTAGEM ->'))
print(f'='*60)
print(f'O DOBRO DO NÚMERO {n} É {numeros.dobro(n)}')
print(f'A METADE DO NÚMERO {n} É {numeros.metade(n)}')
print(f'VAMOS AUMENTAR O SEU NÚMERO DE ACORDO COM A PORCENTAGEM COLOCADA\n VAI SER AUMENTADO O NÚMERO {n} E O TOTAL PÓS PORCENTAGEM É {numeros.aumentar(n,p)}')
print(f'='*60)
print(f'VAMOS DIMINUIR O SEU NÚMERO DE ACORDO COM A PORCENTAGEM COLOCADA\n VAI SER DIMINUIDO O NÚMERO {n} E O TOTAL PÓS PORCENTAGEM É {numeros.diminuir(n,p)}')