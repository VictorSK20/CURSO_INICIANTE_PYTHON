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

pi = 3.1415
pi_r = 180
angulo = float(input('Informe um angulo: '))
angulo = angulo*((2*pi)/360)

seno = math.sin((angulo))
cosseno = math.cos((angulo))
tangente = math.tan((angulo))

print('victor',)
print(f'O angulo de {angulo:.2f} é igual a {seno:.2f}')
print(f'O angulo de {angulo:.2f} é igual a {cosseno:.2f}')
print(f'O angulo de {angulo:.2f} é igual a {tangente:.2f}')
