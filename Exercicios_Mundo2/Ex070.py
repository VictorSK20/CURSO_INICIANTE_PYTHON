# Crie um programa que leia o Nome e o Preço de Vários Produtos. O programa deverá perguntar se o Usuário vai continuar.
# No final. Mostre:
# A) Qual é o Total Gasto na compra.
# B) Quantos produtos custam Mais de R$1000,00
# C) Qual é o Nome do produto mais Barato

total_compra = preco_maior = preco_produtos = menor_preco = 0
produto = continua = produto_barato = ''
preco_barato = float('inf')

print('-' * 30)
print(F'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)

while True:

    # Loop para inserir os nomes dos produtos
    while True:
        produto = str(input('Nome do Produto: ')).capitalize()
        if not produto.isalpha():
            print('Valor insira um nome válido')
        else:
            break

    # Loop para inserir os valores dos produtos
    while True:
        preco = float(input('Preço: R$'))
        preco_produtos += 1
        total_compra += preco

        # Se a variavel preco for menor que a variavel preço_barato, barato recebe valor de preço
        if preco < preco_barato:
            preco_barato = preco
            produto_barato = produto

        # cada vez que a variavel preço receber um valor acima de 1000, a variavel preço_maior recebe +1
        if preco > 1000:
            preco_maior += 1
        break

    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[:1]
        if continua in ['S', 'N']:
            break

    if continua == 'N':
        break

print(F'\n{"-" * 10} FIM DO PROGRAMA {"-" * 10}')

print(f'O valor do total da compra foi R${total_compra:,.2f}')
print(f'Temos {preco_maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {produto_barato} que custa R${preco_barato:.2f}')
