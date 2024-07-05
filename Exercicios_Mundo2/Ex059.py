# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
"""
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
"""
# Seu programa deverá realizar a operação solicitada em cada caso

from colorama import init

init(autoreset=True)

escolhar = 0
maior = ''

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

cor1 = '\033[1;34m'  # cor azul para o resultado das operações
cor2 = '\033[1;31m'  # cor vermelha para o resultado inválido nas operações

if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
elif n1 == n2:
    maior = 'Valores digitado são iguais'

while escolhar != 5:
    print('\nEscolha um dos números abaixo para executa o comando escolhido.'
          '\n\t[1] Somar\n\t[2] Multiplicar\n\t[3] Maior\n\t[4] Novos Números\n\t[5] Sair do Programa')

    escolhar = int(input('\t\033[1m→  '))
    if escolhar == 1:
        print(f'{cor1}{n1} + {n2} = {n1+n2}')

    elif escolhar == 2:
        print(f'{cor1}{n1} x {n2} = {n1*n2}')

    elif escolhar == 3:
        print(f'O maior número digitado → {cor1}{maior}')

    elif escolhar == 4:
        print('Informe novos valores para as operações.\n')

        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))

    elif escolhar == 5:
        print(f'{cor1}Finalizando operações')

    else:
        print(f'{cor2}Escolhar Inválida')
