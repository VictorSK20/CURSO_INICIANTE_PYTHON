#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
#cosseno e tangente desses ângulo
'''
co = float(input('Informe o valor do Cateto Oposto: '))
ca = float(input('Informe o valor do Cateto Adjagente: '))
hi = (co**2 + ca**2) ** 0.5
num = float(input('Informe o Ângulo: '))
seno = co/hi
cosseno = ca/hi
tangente = ca/co
print('\nSegue os valores dos ângulo abaixo:')
print(f'valor do seno: {seno} \nvalor do cosseno: {cosseno} \nvalor da tangente: {tangente}')
'''

import math

# Laranja
cor1 = '\033[38;2;255;128;0m'

# Azul escuro
cor2 = '\033[38;2;0;128;255m'

# Remover Cor
cor0 = '\033[m'

angulo = float(input(f'{cor1}Informe um angulo:\n'))

# Calculo dos angulos
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# Imprimindo os resultados
print(f'{cor2}O angulo de {angulo:.2f} é igual a {seno:.2f}')
print(f'{cor1}O angulo de {angulo:.2f} é igual a {cosseno:.2f}')
print(f'{cor2}O angulo de {angulo:.2f} é igual a {tangente:.2f}')
