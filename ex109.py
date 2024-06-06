from uteis import numeros

n = int(input('DIGITE O PREÇ0 -> R$'))
p = int(input('DIGITE UM NÚMERO INTEIRO PARA PORCENTAGEM->'))
print(f'='*60)
print(f'O DOBRO DO NÚMERO {numeros.moeda(n)} É {numeros.moeda(numeros.dobro(n))}')
print(f'A METADE DO NÚMERO {numeros.moeda(n)} É {numeros.moeda(numeros.metade(n))}')
print(f'AUMENTANDO {p}% temos {numeros.moeda(numeros.aumentar(n,p))}')
print(f'DIMINUINDO {p}% temos {numeros.moeda(numeros.diminuir(n,p))}')
print(f'='*60)