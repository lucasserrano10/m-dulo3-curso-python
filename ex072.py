numerosExtenso = ('zero', 'um', 'dois','tres','quatro','cinco','seis','sete', 'oito', 'nove','dez')
numeroUsuario = int(input('DIGITE UM NÚMERO ENTRE 0 E 10: '))
while numeroUsuario < 0 or numeroUsuario > 10:
    numeroUsuario = int(input(f'TENTE NOVAMENTE, DIGITE UM NÚMERO ENTRE 0 E 10: '))
print(f'SEU NÚMERO POR EXTENSO É {numerosExtenso[numeroUsuario]}')