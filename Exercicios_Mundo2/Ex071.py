# Crie um programa que simule o funcionamento de um Caixa Eletrônico. No início, pergunte ao usuário qual será o Valor
# A Ser Sacado (número inteiro) e o programa vai informar quantas Cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, e R$1

cedula50 = cedula20 = cedula10 = cedula1 = 0

print('=' * 35)
print(f'{"BANCO CEV":^30}')
print('=' * 35)

valor = int(input('Qual será o valor a ser sacado: R$'))

while True:

    # Enquanto valor for maior ou igual a 50, o valor vai receber -50 e adiciona +1 na variavel cedula 50
    while valor >= 50:
        valor -= 50
        cedula50 += 1

    # Enquanto valor for maior ou igual a 20, o valor vai receber -20 e adiciona +1 na variavel cedula 20
    while valor >= 20:
        valor -= 20
        cedula20 += 1

    # Enquanto valor for maior ou igual a 10, o valor vai receber -10 e adiciona +1 na variavel cedula 10
    while valor >= 10:
        valor -= 10
        cedula10 += 1

    # Enquanto valor for maior ou igual a 1, o valor vai receber -1 e adiciona +1 na variavel cedula 1
    while valor >= 1:
        valor -= 1
        cedula1 += 1

    break

if cedula50 > 0:
    print(f'Total de {cedula50:2} cédulas de R$50')
if cedula20 > 0:
    print(f'Total de {cedula20:2} cédulas de R$20')
if cedula10 > 0:
    print(f'Total de {cedula10:2} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1:2} cédulas de R$1')

print('=' * 35)
print('Volte sempre ao BANCO CEV! Tenha um bom dia')