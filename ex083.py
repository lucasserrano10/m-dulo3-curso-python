expr = str(input('DIGITE SUA EXPRESSÃO: '))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('SUA EXPRESSÃO ESTÁ VÁLIDA')
else:
    print('SUA EXPRESSÃO ESTÁ INVÁLIDA')
