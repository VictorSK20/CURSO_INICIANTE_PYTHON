from colorama import init

init(autoreset=True)

def valor(value):
    if value:
        # True - cor verde
        print(f"\033[32m {value}\033[0m")
    else:
        # False - cor vermelha
        print(f"\033[31m {value}\033[0m")


print('Tipos Primitivos')

valor_informado = input('Informe algo e receber os valores primitivos:\n')

print('Valor informado é Alpha Numérico:', end=' ')
valor(valor_informado.isalnum())

print('Valor informado é Alpha:', end=' ')
valor(valor_informado.isalpha())

print('Valor informado é minúsculo:', end=' ')
valor(valor_informado.islower())

print('Valor informado é decimal:', end=' ')
valor(valor_informado.isdecimal())

print('Valor informado é espaço:', end=' ')
valor(valor_informado.isspace())

print('Valor informado é numérico:', end=' ')
valor(valor_informado.isnumeric())

print('Valor informado é maiúsculo:', end=' ')
valor(valor_informado.isupper())

print('Valor informado é dígito:', end=' ')
valor(valor_informado.isdigit())
