def leiaint(msg,msgerro):
  entrada = input(msg)
  while True:
      if not entrada.isnumeric():
          print(msgerro)
          entrada = input(msg)
      else:
          int(entrada)
          break
  print(f'O NÚMERO ESCRITO FOI {entrada}')

leiaint('DIGITE UM NÚMERO PARA VERIFICAÇÃO ->','erro!, DIGITE UM NÚMERO !')
