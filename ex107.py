def notas(*n, sit = False):
    r = dict()
    r['Total'] = len(n)
    r['Máximo'] = max(n)
    r['Menor'] = min(n)
    r['média'] = sum(n)/len(n)
    r['Situação'] = False
    if r['média'] >= 7:
        r['Situação'] = 'APROVADO'
    elif r['média'] >= 5 and r['média'] <= 7:
        r['Situação'] = 'RECUPERAÇÃO'
    else:
        r['Situação'] = 'REPROVADO'

    print(r)

notas(3,4,10,sit = False)
