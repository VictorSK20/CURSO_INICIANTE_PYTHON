# Faça um programa que leia o preço de um produto e mostre seu valor final com desconto de 5%
# o produto deve ter 3% de juros se for parcelado

# Informando o valor de um produto
produto = float(input('Informe o preço do produto \nR$'))
# esconto = int(input('Informe qual o desconto do produto: '))

# armazenando nas variaveis "desconto" e "avista" o valor do produto com a porcetagem
avista = produto - (5 / 100 * produto)
parcelado = produto + (3 / 100 * produto)

green_code = '\033[92m'
reset_code = '\033[0m'

print(f'\nO produto no valor de R${produto:.2f} com 5% de desconto vai custar {green_code}R${avista:.2f}{reset_code} '
      f'\nValor do desconto {green_code}R${5 / 100 * produto:.2f}{reset_code}')

print(f'\nO produto no valor de R${produto:.2f} se for parcelado, terá um juros de 3% e vai custar {green_code}R${parcelado:.2f}{reset_code}')
print(f'Valor do juros: {green_code}R${3 / 100 * produto:.2f}{reset_code}')
