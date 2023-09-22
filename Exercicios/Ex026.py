""" Crie um programa que conte quantas vezes aparece a letra "A" e informe em qual posição ela apareceu
pela primeira vez e pela última vez """
from colorama import init

init(autoreset=True)

n = input('Informe uma Palavra: \n')

# cores
cor1 = '\033[1;36m'

cor2 = '\033[1;35m'

cor3 = '\033[1;34m'

# transformando meus caracteres para minusculo com o comando "lower"
n = n.lower()

# Informando quantas vezes o caracter " A " aparece
# comando count informa a primeira posição da variavel "n" a esquerda

print(f'{cor1}A quantidade de vezes que o caracter A aparece é {n.count("a")}\n')

# Informando a posição que o caracter "A" aparece pela primeira vez
# comando find informa a primeira posição da variavel "n" a esquerda
print(f'{cor2}O caracter A aparece pela primeira vez na posição {n.find("a")+1} da lista de caracteres\n')

# Informando a posição que o caracter "A" aparece pela última vez
# comando rfind informa a primeira posição da variavel "n" a direita
print(f'{cor3}O caracter A aparece pela ultima vez na posição {n.rfind("a")+1} da lista de caracteres\n')
