def fatorial(a,show = False):
    if show:
        if a < 0:
            print("Não é possível calcular o fatorial de um número negativo.")
            return
        s = 1
        while a > 1:
            s *= a
            a -= 1
            print(f'{s}*{a} = {a * s}')
    else:
        if a < 0:
            print("Não é possível calcular o fatorial de um número negativo.")
            return
        s = 1
        while a > 1:
            s *= a
            a -= 1
        print(s)

fatorial(5,True)
