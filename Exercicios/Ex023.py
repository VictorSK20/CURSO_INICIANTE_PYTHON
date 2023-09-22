"""Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada numero separado por
    unidade, dezena, centena e milhar"""

'''
# Utilizando o modulo random

import random

num = str(random.randint(0, 9999))

print(f'O numero informado pelo sistema é {num} \n')

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print(f'Milhar = {milhar}')
print(f'Centena = {centena}')
print(f'Dezena = {dezena}')
print(f'Unidade = {unidade}')

'''

'''
num = int(input('Digite um numero de 0 a 9999\n'))

if num >= 0 and num < 10000:
    num = ' '
    num = str(num)
    u = num[0]
    d = num[1]
    c = num[2]
    m = num[3]

    print(f'Milhar = {m}')
    print(f'Centena = {c}')
    print(f'Dezena = {d}')
    print(f'Unidade = {u}')

elif int(num) is None:
    print('Digite um valor valido')

else:
    print('Numero invalido')
'''

numero = int(input('Informe um numero: \n '))

# cor
cor1 = '\033[1;38;5;40m'

# cor
cor2 = '\033[1;38;5;226m'

# cor
cor3 = '\033[1;38;5;26m'

# cor
cor4 = '\033[1;38;5;1m'

# cor
cor0 = '\033[m;'

# negrito
N = '\033[1m'

u = numero // 1 % 10
d = numero // 10 % 10  # resolução na calculadora: Ex 1234 // 10 = 123 - referente ao valor inteiro da div, agora 123 % 10 = 3 referente ao resto da div
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'{N}A unidade = {cor1}{u}{cor0}')
print(f'{N}A dezena  = {cor2}{d}{cor0}')
print(f'{N}A centena = {cor3}{c}{cor0}')
print(f'{N}O milhar  = {cor4}{m}{cor0}')
