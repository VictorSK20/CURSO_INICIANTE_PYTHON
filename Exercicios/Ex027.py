# Leia o nome de uma pessoa e mostre na tela o seu primeiro nome e o seu último nome

n = input('Informe seu nome completo:\n')

n = n.split()

print(f'Primeiro nome: {n[0]}')

print(f'Ultimo nome: {(n[-1])}')
