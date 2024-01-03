# Elabore um programa que calcule o valor a ser pago por um produto
# Considerando o seu PREÇO NORMAL e CONDIÇÕES DE PAGAMENTO:


from colorama import init  # Utilizando a biblioteca colorama para cores

init(autoreset=True)  # Comando para resetar a cor para o padrão a cada linha

# Função para as cores
def color(cor, texto):
    if cor == 'titulo':
        return f'\033[1;38;5;15m{texto}'
    if cor == 'tabela':
        return f'\033[1;38;5;46m{texto}'
    if cor == 'f_pag':
        return f'\033[1;38;5;11m{texto}'
    if cor == 'dinheiro':
        return f'\033[1;32m{texto}'

print(color('titulo', f'{" BEM VINDO AO SISTEMA DE PAGAMENTO DA LOJA ":*^100}\n'))

print(color('tabela', f'''{"":=^50}
\t TABELA DE VALORES COM DESCONTOS E JUROS
\t---------------------------------------
\t À VISTA NO DINHEIRO CHEQUE: 10% DE DESCONTO
\t---------------------------------------
\t À VISTA NO CARTÃO: 5% DE DESCONTO
\t---------------------------------------
\t EM ATÉ 2x NO CARTÃO: PREÇO NORMAL
\t---------------------------------------
\t 3x OU MAIS NO CARTÃO: 20% DE JUROS
\t---------------------------------------
{"":=^50}
'''))

print(color('f_pag', 'Escolhar a forma de pagamento'))

forma_pagamento = int(input(color('f_pag', '''
[1] Dinheiro
[2] Cartão 
Informe o número >>> ''')))

if forma_pagamento == 1:
    (print(f'\nForma de pagamento escolhida: {color("dinheiro","Dinheiro")}'))
    produto = float(input('Informe o valor do produto R$'))
    desconto = (produto - (10 * produto / 100))
    print(f'O produto no valor de R${produto:.2f} com 10% de desconto sairá no valor de R${desconto:.2f}')

elif forma_pagamento == 2:
    print(f'\nForma de pagamento escolhida: {color("dinheiro", "Cartão")}')
    produto = float(input('Informe o valor do produto R$'))
    parcelas = int(input('De quantas vezes deseja parcela o produto x'))

    if parcelas == 0 or parcelas == 1:
        desconto = (produto - (5 * produto / 100))
        print(f'O produto no valor de R${produto:.2f} com 5% de desconto sairá no valor de R${desconto:.2f}')

    elif parcelas == 2:
        print(f'Valor do produto R${produto:.2f} será pago com duas parcelas de R${produto / parcelas:.2f}')

    elif parcelas >= 3:
        juros = (produto + (20 * produto / 100))
        print(f'O produto no valor de R${produto:.2f} parcelado em x{parcelas} ficará com 20% de juros')
        print(f'Valor de cada parcela R${juros / parcelas:.2f}')
