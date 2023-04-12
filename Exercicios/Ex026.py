""" Crie um programa que conte quantas vezes aparece a letra "A" e informe em qual posição ela apareceu
pela primeira vez e pela última vez """

n = input('Informe uma Palavra: \n')

# transformando meus caracteres para minusculo
n = n.lower()

# Informando quantas vezes o caracter " A " aparece
print(f'A quantidade de vezes que o caracter A aparece é {n.count("a")}\n')

# Informando a posição que o caracter "A" aparece pela primeira vez
print(f'O caracter A aparece pela primeira vez na posição {n.find("a")} da lista de caracteres\n')

# Informando a posição que o caracter "A" aparece pela última vez
print(f'O caracter A aparece pela ultima vez na posição {n.rfind("a")} da lista de caracteres\n')
