from uteis import strings
from uteis import numeros

n = strings.leiaDinheiro('DIGITE O PREÇO -> R$')
p = strings.leiaDinheiro('DIGITE A TAXA ->')
print(numeros.resumo(n,p))