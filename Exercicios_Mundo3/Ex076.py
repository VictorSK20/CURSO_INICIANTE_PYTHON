# Crie um programa que tenha uma TUPLA única com Nome de Produtos e seus respectivos Preços na sequência .
# No final, mostre uma listagem de preço organizando os dados em forma Tabular

produtos = (str(input('Nome do 1º Produto: ').capitalize()), float(input('Valor do 1º Produto R$')),
            str(input('Nome do 2º Produto: ').capitalize()), float(input('Valor do 2º Produto R$')),
            str(input('Nome do 3º Produto: ').capitalize()), float(input('Valor do 3º Produto R$')),
            str(input('Nome do 4º Produto: ').capitalize()), float(input('Valor do 4º Produto R$')),
            str(input('Nome do 5º Produto: ').capitalize()), float(input('Valor do 5º Produto R$')),
            str(input('Nome do 6º Produto: ').capitalize()), float(input('Valor do 6º Produto R$')),
            str(input('Nome do 7º Produto: ').capitalize()), float(input('Valor do 7º Produto R$')),
            str(input('Nome do 8º Produto: ').capitalize()), float(input('Valor do 8º Produto R$')),
            )

print('-'*50)
print(f"{'LISTAGEM DE PREÇOS':^48}")
print('-'*50)

for i in range(0, len(produtos), 2):
    nome_produto = produtos[i]
    valor_produto = produtos[i + 1]
    print(f'{nome_produto:.<42}R${valor_produto:6.2f}')
print('-'*50)
