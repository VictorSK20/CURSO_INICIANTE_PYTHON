# Crie um programa que leia o nome de uma cidade e informe se ela começa ou não com o nome Santos

from colorama import init

init(autoreset=True)

def valor(value):
    if value:
        return f'\033[1;32m{value}'
    else:
        return f'\033[1;31m{value}'

city = input('Digite o nome da cidade:\n').strip()

city = city.lower()

# cor verde padrão RGB
cor1 = '\033[38;2;128;255;0m'

# cor vermelha padrão RGB
cor2 = '\033[38;2;255;0;0m'

if city == 'santos':
    print(f'{cor1}Analisando o codigo:\nO usuário nasceu em Santos')
    print(valor(city[:6] == 'santos'))

else:
    print(f'{cor2}Analisando o codigo:\nO usuário não nasceu em Santos')
    print(valor(city[:6] == 'santos'))
