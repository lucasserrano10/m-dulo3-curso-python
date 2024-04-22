merlot = 90
sauvignon = 85
charlot = 200
print(f'----------BEM VINDO A VINHERIA AGNELLO----------')
print(f'-=-' * 30)
print(f'PRECISAMOS DE ALGUMAS INFORMAÇÕES !')
print(f'-=-'*30)
nome = input('DIGITE SEU NOME: ')
endereco = input('ENDEREÇO: ')
idade = int(input('idade :'))

if idade < 18:
    print('VOCÊ É MENOR DE IDADE')
else:
    print(f'-=-' * 30)
    print('-----NOSSAS OPÇÕES DE VINHO----')
    print(f'-=-' * 30)
    print(f'MERLOT - {merlot}R$')
    print(f'SAUVIGNON - {sauvignon}R$')
    print(f'CHARLOT - {charlot}R$')
    while True:
        escolha = int(input('QUAL DOS VINHOS GOSTARIA [1-MERLOT] [2-SAUVIGNON] [3-CHARLOT]?'))
        if escolha == 1:
            print(f'-=-' * 30)
            print(f'MERLOT CUSTA {merlot}R$, SENDO UMA ÓTIMA OPÇÃO.')
        elif escolha == 2:
            print(f'-=-' * 30)
            print(f'SAUVIGNON CUSTA {sauvignon}R$, SENDO UMA ÓTIMA OPÇÃO.')
        elif escolha == 3:
            print(f'-=-' * 30)
            print(f'CHARLOT CUSTA {charlot}R$, SENDO UMA ÓTIMA OPÇÃO.')
        else:
            print(f'-=-' * 30)
            print('ESCOLHA UMA OPÇÃO !')
        escolha = int(input('QUAL DOS VINHOS GOSTARIA [1-MERLOT] [2-SAUVIGNON] [3-CHARLOT]?'))
        qtdade = int(input('QUANTOS VINHOS O SENHOR(a) GOSTARIA'))
        if qtdade <= 0:
            print('QUANTIDADE NÃO VÁLIDA')
            qtdade = int(input('QUANTOS VINHOS O SENHOR(a) GOSTARIA :'))
        if qtdade >= 2:
            print(f'-=-' * 30)
            print('VOCÊ GANHOU FRETE GRÁTIS')
            if escolha == 1:
                print(f'SEU CARRINHO ESTÁ AVALIADO EM : {qtdade*merlot}')
            elif escolha == 2:
                print(f'SEU CARRINHO ESTÁ AVALIADO EM : {qtdade * sauvignon}')
            else:
                print(f'SEU CARRINHO ESTÁ AVALIADO EM : {qtdade * charlot}')
    print(f'-=-' * 30)
    print(f'SENHOR(a) {nome} SUA ENCOMENDA SERÁ ENTREGUE NO ENDEREÇO : {endereco}')
    while True:
        confirmacao = str(input('ESTÁ CORRETO O ENDEREÇO [S/N]: ')).upper().strip()
        if confirmacao == 'S':
            print(f'-=-' * 30)
            print('MUITO OBRIGADO POR COMPRAR NA VINHERIA AGNELLO !')
            break
        else:
            print(f'-=-' * 30)
            print('SINTO MUITO, TENTE REINICIAR A COMPRA')
            break







