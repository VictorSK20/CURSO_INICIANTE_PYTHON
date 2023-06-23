
'''print('Valor do real para o dolar')
print('')

real = float(input('informe seu valor em real: '))
dolar = real/5.18
euro = real/5.18
print('R${:.2f} em Dolar = US${:.2f}'.format(real, dolar))
print(f'R${real:.2f} em Euro = €{euro:.2f}')
'''

import requests

# Faz a requisição HTTP à API para obter os dados do dólar
response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obtém o valor do dólar em relação ao real
    data = response.json()
    exchange_rate = data["rates"]["BRL"]

    # Exibe o valor atual do dólar
    print(f"O valor atual do dólar em reais é: {exchange_rate}")
else:
    # Exibe uma mensagem de erro caso a requisição falhe
    print("Falha ao obter o valor do dólar")
