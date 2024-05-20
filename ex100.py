from time import sleep
def linha():
    print(f'='*30)

print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1')
def contador1(inicio,fim,passo):
    while inicio <= fim:
        print(inicio, end= ' ')
        sleep(0)
        inicio += passo
contador1(1,10,1)
linha()
print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2')
def contador2(inicio,fim,passo):
    while inicio >= fim:
        print(inicio, end= ' ')
        sleep(0)
        inicio -= passo

contador2(10,0,2)
linha()
print('CONTAGEM PERSONALIZADA')
def contador3(inicio,fim,passo):
        if inicio >= fim:
            while inicio >= fim:
                print(inicio, end=' ')
                inicio -= passo
        else:
            while inicio <= fim:
                print(inicio, end=' ')
                inicio += passo

inicio = int(input('inicio ->'))
fim = int(input('fim ->'))
passo = int(input('passo ->'))
contador3(inicio,fim,passo)