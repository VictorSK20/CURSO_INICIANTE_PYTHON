# Faça um programa que leia um Número Inteiro e diga se ele é ou não Número Primo

from colorama import init

init(autoreset=True)

red = '\033[1;31m'
green = '\033[1;32m'

contagem = 0

n = int(input('Informe um número e descubra se ele é número primo: '))

for a in range(1, n+1):
    if n % a == 0:
        numeros = f'{green}{a}'
        contagem += 1
    else:
        numeros = f'{red}{a}'

    if contagem == 2:
        e_primo = f'{green}O número {n} é primo, ele foi divisível {contagem}'
    else:
        e_primo = f'{red}O número {n} não é primo, ele foi divisível {contagem}'

    print(numeros, end=' ')

print(f'\n{e_primo}')
