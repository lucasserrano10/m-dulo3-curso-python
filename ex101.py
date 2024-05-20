'''from time import sleep
def maiorValor(*valores):
    lista = []
    print('ANALISANDO VALORES...')
    sleep(3)
    lista.append(valores)
    maior = valores[0]
    for v in valores:
        if v > maior:
            maior = v
    print(f'FORAM PASSADOS {len(valores)} VALORES, E O VALOR MAIS ALTO FOI {maior}')

maiorValor(2,2,2,2,2,2,2,2,2,2)'''

def maiorValor(*valores):
    lista = []
    print('ANALISANDO VALORES...')
    lista.append(valores)
    sorted(lista)
    i = len(valores) - 1
    print(f'FORAM PASSADOS {len(valores)} VALORES, E O VALOR MAIS ALTO FOI {valores[i]}')


maiorValor(2,143,43224,4342432)