def ficha(nome=0,gols=0):
    if nome != '' and gols != 0:
        print(f'O JOGADOR {nome} FEZ {gols} GOLS NO CAMPEONATO')
    if nome != '' or gols != 0:
        if nome == '':
            nome = '<desconhecido>'
        else:
            gols = 'NÃO POSSUI GOLS REGISTRADOS'
        print(f'O JOGADOR {nome} - POSSUI - > {gols} GOLS NO CAMPEONATO !')



nome = str(input('NOME JOGADOR ->'))
gols = str(input('GOLS DO JOGADOR ->'))
if gols == '':
    gols = None
else:
    int(gols)

ficha(nome,gols)