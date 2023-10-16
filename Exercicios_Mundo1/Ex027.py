# Leia o nome de uma pessoa e mostre na tela o seu primeiro nome e o seu último nome
from colorama import init

init(autoreset=True)

n = input('Informe seu nome completo:\n')

n = n.split()

cor1 ='\033[38;5;118m'

cor2 = '\033[38;5;119m'

print(f'{cor1}Primeiro nome: {n[0]}')

print(f'{cor2}Ultimo nome: {(n[-1])}')
