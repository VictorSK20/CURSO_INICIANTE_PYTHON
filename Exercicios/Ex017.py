# O programa vai ler o comprimento do cateto oposto e do cateto adjacente
# de um triangulo , retângulo, é calcula, mostrado o resultado da hipotenusa

print('Calculo do Triângulo Retãngulo')

'''
# EM TESTE

cateto_oposto = (float(input('Informe o tamanho do Cateto Oposto: ')))
cateto_adjacente = (float(input('Informe o tamanho do Cateto Adjacente: ')))
hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2))**0.5

print(f'O resultado da Hipotenusa é = {hipotenusa}')
'''

import math

# cor amarela
cor1 = '\033[1;95m'

# cor vermelha para mensagem de erro
cor2 = '\033[1:91m'

# remover cor
cor0 = '\033[m'

n = int(input('Para utiliza somente calculos matematicos digite 1\n'
              'Para utiliza somente formula da hipotenusa digite 2\n'))

if n == 1:

    c1 = (float(input('Informe o valor do Cateto Oposto: ')))
    c2 = (float(input('Informe o valor do Cateto adjacente: ')))

    potencia = (math.pow(c1, 2) + math.pow(c2, 2))
    raiz = math.sqrt(potencia)
    print(f'O valor da Hipotenusa é = {cor1}{raiz:.4f}{cor0}')

elif n == 2:
    co = float(input('Informe o valor do Cateto Oposto: '))
    ca = float(input('Informe o valor do Cateto Adjacente: '))
    hi = math.hypot(co, ca)
    print(f'O valor da Hipotenusa é = {cor1}{hi:.4f}{cor0}')

else:
    print(f'{cor2}Erro, por favor digite apenas o numero 1 ou 2{cor0}')
