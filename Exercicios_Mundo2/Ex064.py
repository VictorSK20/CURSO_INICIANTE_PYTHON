# Crie um programa que leia Vários Números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor
# 999, que é a Condição de Parada. No final, mostre Quantos Números foram digitados e qual foi a Soma entre eles
# Desconsiderando o (Flag)

from colorama import init

init(autoreset=True)

red = '\033[31m'
negrito = '\033[1m'
defalt = '\033[0m'

num_digitados = 0
soma = 0
n = 0

while n != 999:
    n = int(input(f'{negrito}Informe os números desejado para as somas entre eles de 0 à 998\n{red}Obs: Digite 999 para condição de parada\n'))
    if n != 999:
        soma += n
        num_digitados += 1

print(f'Você digitou {num_digitados} números\nA soma entre eles são: {soma}')
