# Crie um programa que leia o nome de uma pessoa e diga se ela tem o "Silva" no nome

nome = input('Informe seu nome:\n')
nome = nome.title()
print(f'Essa pessoa tem o Silva no nome = {"Silva" in nome}')
