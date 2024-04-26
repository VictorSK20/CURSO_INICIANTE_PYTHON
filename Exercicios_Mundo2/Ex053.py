# Crie um programa que leia uma Frase qualquer e diga se ela é um Palíndromo, desconsiderando os espaços

frase = input('Digite uma frase: ').upper()

reverse = frase[::-1].replace(' ', '')

if frase.replace(' ', '') == reverse:
    print(f'A frase - {frase} - é um Palíndromo ')
else:
    print(f'A frase - {frase} - não é um Palíndromo')
