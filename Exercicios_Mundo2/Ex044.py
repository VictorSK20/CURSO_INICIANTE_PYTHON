# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÕES DE PAGAMENTO:
"""
À vista Dinheiro Cheque: 10% de desconto
À vista no Cartão: 5% de desconto
Em até 2x no cartão: preço normal
3% ou mais no cartão: 20% de juros
"""

# cores

from colorama import init

init(autoreset=True)

def cor():
    produto = '\033[1;32m'  # Verde
    erro = '\033[1;31m'  # Vermelho

try:
    produto = float(input('Informe o valor do produto: '))

    print('''Formas de pagamentos disponiveis: 
    \t1 = À vista no dinheiro Cheque: 10% de desconto
    \t2 = À vista no cartão: 5% de desconto
    \t3 = Até 2x no cartão: valor normal
    \t4 = 3x ou mais no cartão: 20% juros
          ''')

    forma_pagamento = int(input('escolhar a forma de pagamento\n1: para Dinheiro Cheque\n2: para Cartão\n\t'))

    if forma_pagamento == 1:
        print(f'''Forma de pagamento escolhida: À vista no dinheiro cheque
        O produto no valor de {produto} com 10% de desconto ficará no valor de: {produto - ((produto * 10) / 100):.2f}''')

    elif forma_pagamento == 2:
        parcelas = int(input('Informa a quantidade de parcelas\nInforme 0 para compra à vista\n\t'))
        if parcelas == 0:
            print(f'''Forma de pagamento escolhida foi: À vista no cartão
O produto no valor de R${produto} com 5% de desconto ficará no valor de R${produto - ((produto * 5) / 100)}:.2f''')

        elif parcelas > 0 and parcelas < 3:
            print(f'''Forma de pagamento escolhida foi: de {parcelas}x no cartão
O produto no valor de R${produto:.2f} com {parcelas}x ficará no valor de R${(produto / parcelas):.2f}''')

        elif parcelas >= 3:
            print(f'''Forma de pagamento escolhida foi: de {parcelas}x no cartão
O produto no valor de R${produto} com {parcelas} parcelas ficarás no valor de {produto + ((produto * 20) / 100):.2f}''')

    else:
        print('Favor escolher apenas 1 ou 2 para as formas de pagamento dísponivel ')

except ValueError:
    print('valor invalido !')
