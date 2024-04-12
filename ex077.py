palavras = ('pizza', 'python','jogo','apple','iphone')
for p in palavras:
    print(f'NA PALAVRA {p} temos')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)
