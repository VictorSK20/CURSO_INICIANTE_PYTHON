print('Valor de um produto com desconto e parcelado')
print(' ')

produto = float(input('Informe o preço do produto: '))
desconto = int(input('Informe qual o desconto do produto: '))

avista = produto - (desconto/100 * produto)
parcelado = produto + (3/100 * produto)
print('O produto com o valor de R${:.2f} com {}% de desconto fica = R${:.2f} \nValor do descontado = {:.2f}R$'.format(produto, desconto, avista, desconto/100 * produto))
print(f'O produto no valor de R${produto:.2f} se for parcelado, terá um juros de 3% e tera o valor de {parcelado:.2f}R$')
print(f'Valor do juros: {3/100 * produto:.2f}')
