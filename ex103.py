def voto(number):
    check = 2024 - number
    return check

anoNascimento = int(input('DIGITE O ANO DE NASCIMENTO ->'))
if voto(anoNascimento) >= 65:
    print(f'POR SER IDOSO, O VOTO É OPCIONAL !')
elif voto(anoNascimento) >= 18:
    print(f'COM {voto(anoNascimento)} ANOS, VOTO É OBRIGATÓRIO !')
elif voto(anoNascimento) < 16:
    print(f'COM {voto(anoNascimento)} ANOS, VOTO NÃO É PERMITIDO !')
elif voto(anoNascimento) >= 16 and voto(anoNascimento) < 18:
    print(f'COM {voto(anoNascimento)} ANOS, VOTO OPCIONAL !')