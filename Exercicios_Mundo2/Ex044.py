# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÕES DE PAGAMENTO:
"""
À vista Dinheiro Cheque: 10% de desconto
À vista no Cartão: 5% de desconto
Em até 2x no cartão: preço normal
3% ou mais no cartão: 20% de juros
"""

# importando biblioteca de cores
from colorama import init

init(autoreset=True)


# função para adiciona cores
def cor(texto, tipo):
    if tipo == 'produto':
        return f'\033[1;32mR${texto:.2f}\033[m'  # Verde
    elif tipo == 'parcelas':
        return f'\033[1;33m{texto}x\033[m'  # Amarelo
    elif tipo == 'juros':
        return f'\033[1;34mR${texto:.2f}\033[m'  # Azul
    elif tipo == 'desconto':
        return f'\033[1;35mR${texto:.2f}\033[m'  # Roxo
    elif tipo == 'erro':
        return f'\033[1;31m{texto}\033[m'  # Vermelho


# tratativa de erro
try:
    produto = float(input('Informe o valor do produto: '))

    # Seleção de formas de pagamentos
    print('''Formas de pagamentos disponiveis: 
    \t1 = À vista no dinheiro Cheque: 10% de desconto
    \t2 = À vista no cartão: 5% de desconto
    \t3 = Até 2x no cartão: valor normal
    \t4 = 3x ou mais no cartão: 20% juros
          ''')

    # escolhendo forma de pagamento (Dinheiro ou Cartão) - se for em Dinheiro, compras à vista com 10% de desconto, se for no cartão compras à vista, ou com juros para parcelas de 3x ou mais
    forma_pagamento = int(input('escolhar a forma de pagamento\n1: para Dinheiro Cheque\n2: para Cartão\n\t'))

    if forma_pagamento == 1:
        desconto = produto * 10 / 100
        print(f'''Forma de pagamento escolhida: À vista no dinheiro cheque
        Valor do produto: {cor(produto, 'produto')} 
        Número de parcelas: À Vista
        Juros: Sem Juros
        10% de Desconto: {cor(desconto, 'desconto')}
        Total: {cor(produto - ((produto * 10) / 100), 'produto')}''')

    elif forma_pagamento == 2:
        parcelas = int(input('Informa a quantidade de parcelas\n\t'))

        if parcelas == 1:
            print(f'''Forma de pagamento escolhida foi: À vista no cartão
Valor do produto: {cor(produto, 'produto')}
Numero de parcelas: A VISTA
SEM JUROS ''')

        elif parcelas == 2:
            juros = (produto * 5) / 100
            valor_parcelas = (produto + juros) / parcelas
            print(f'''Forma de pagamento escolhida foi: de {cor(parcelas, 'parcelas')} no cartão
Valor do produto: {cor(produto, 'produto')}
Numeros de parcelas: {cor(parcelas, 'parcelas')}
5% de Juros: {cor(juros, 'juros')}
valor das parcelas com juros: {cor(valor_parcelas, 'juros')}
total: {cor(produto + juros, 'produto')}''')

        elif parcelas >= 3:
            juros = (produto * 20) / 100
            valor_parcelas = (produto + juros) / parcelas
            print(f'''Forma de pagamento escolhida foi: de {cor(parcelas, 'parcelas')} no cartão
Valor do produto: {cor(produto, 'produto')}
Numeros de parcelas: {cor(parcelas, 'parcelas')}
20% de Juros:  {cor(juros, 'juros')}
Valor das parcelas com juros: {cor(valor_parcelas, 'juros')}
total: {cor(produto + juros, 'produto')}.''')

    else:
        print(cor('Favor escolher apenas 1 ou 2 para as formas de pagamento dísponivel ', 'erro'))

except ValueError:
    print(cor('Valor invalido !', 'erro'))
