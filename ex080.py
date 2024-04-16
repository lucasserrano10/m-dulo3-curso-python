numeros = []
for c in range(0,5):
    num = int(input('digite um número: '))
    if c == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                break
            pos += 1

print(f'-=-'*30)
print(f'VALORES DIGITADOS EM ORDEM: {numeros}')
print(f'-=-'*30)