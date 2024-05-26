from time import sleep

def Bemvindo():
    print(f'='*30)
    print('SISTEMA DE AJUDA !')
    print(f'=' * 30)


def sistemaAjuda():
    while True:
        entrada = str(input('DIGITE UMA FUNÇÃO OU BIBLIOTECA PARA ACESSARMOS [FIM-ENCERRA] ->')).strip().lower()
        if entrada != 'fim':
            print(f'˜'*30)
            print(f'ACESSANDO O DOC DO {entrada}')
            print(f'˜'*30)
            sleep(1)
            print(f'='*30)
            sleep(2)
            help(entrada)
            print(help(entrada))
        else:
            print(f'ATÉ LOGO !')
            break




Bemvindo()
sistemaAjuda()