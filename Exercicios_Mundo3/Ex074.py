# Crie um programa que vai gerar Cinco Números Aleatórios e colocar em uma TUPLA.
# Depois disso, mostre a Listagem de Números gerados e também indique o Menor e o Maior valor que estão na tupla

from random import randint

rep = maior = menor = 0

for n in range(5):
    nr = randint(0, 5)
    print(f'{nr}', end=' ')

    rep += 1
    if rep == 1:
        maior = menor = nr
    else:
        if nr < menor:
            menor = nr
        elif nr > maior:
            maior = nr

print(f'\nO maior valor sorteado foi {maior}')
print(f'\nO menor valor sorteado foi {menor}')
