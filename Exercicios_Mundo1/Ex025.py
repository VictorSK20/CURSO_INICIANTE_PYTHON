# Crie um programa que leia o nome de uma pessoa e diga se ela tem o "Silva" no nome

nome = input('Informe seu nome:\n')

# o Title define a primeira letra de cada palavra para maiuscula e o resto para minuscula
nome = nome.title()

if 'Silva' in nome:
    print(f'\033[1;32m{nome}')
else:
    print(f'\033[1;31m{nome}')

print(f'Essa pessoa tem o Silva no nome ? \nResultado = {"Silva" in nome}')
