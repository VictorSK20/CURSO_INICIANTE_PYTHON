'''print('Valor do real para o dolar')
print('')

real = float(input('informe seu valor em real: '))
dolar = real/5.18
euro = real/5.18
print('R${:.2f} em Dolar = US${:.2f}'.format(real, dolar))
print(f'R${real:.2f} em Euro = €{euro:.2f}')
'''

import requests


def get_exchange_rate():
    try:
        response = requests.get("https://economia.awesomeapi.com.br/USD-BRL")
        data = response.json()
        exchange_rate = float(data[0]["bid"])
        return exchange_rate
    except Exception as e:
        print("\033[1;31mErro ao obter o valor do dólar:\033[7;31;40m", e, '\033[0m')
        return None


def main():
    exchange_rate = get_exchange_rate()
    if exchange_rate is not None:
        exchange_rate_str = "{:.2f}".format(exchange_rate).replace('.', ',')
        print(f"O valor atual do dólar em reais é: \033[1;33m{exchange_rate_str}\033[1;32mR$\033[0m")


if __name__ == "__main__":
    main()
