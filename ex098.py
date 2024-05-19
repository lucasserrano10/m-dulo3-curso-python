def area(a,b):
    atotal = a * b
    print(f'A ÁREA DO SEU TERRENO DE {a}m LARGURA E {b}m DE COMPRIMENTO É {atotal}m2')

print('-----TERRENOS PARTICULARES, QUANTO VOCÊ PRECISA ? ------')
largura = int(input('LARGURA DO SEU TERRENO (m) ->'))
comprimento = int(input('COMPRIMENTO DO TERRENO (m) ->'))
area(largura,comprimento)