# Crie um programa que leia uma Frase qualquer e diga se ela é um Palíndromo, desconsiderando os espaços

#  1 - forma: resolvendo exércicio com fatiamento
'''frase = input('Digite uma frase: ').upper()

reverse = frase[::-1].replace(' ', '')

print(f'O reverse de {frase} é {reverse}')

if frase.replace(' ', '') == reverse:
    print(f'A frase - {frase} - é um Palíndromo ')
else:
    print(f'A frase - {frase} - não é um Palíndromo')'''

# 2 - forma: resolvendo com FOR
frase = input('Digite uma frase: ').upper().strip()  # transformando toda a String em maíusculo e removendo os espaços no início e fim

frase = frase.split()

junto = ''.join(frase)

inverso = ''

for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]

print(f'O inverso da frase {junto} é {inverso}', end=' - ')

if junto == inverso:
    print('Esta frase é um Palíndromo')
else:
    print('Esta frase não é um Palíndromo')
