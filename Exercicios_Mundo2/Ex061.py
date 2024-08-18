# Refaça o Desafio 051, lendo o Primeiro Termo e a Razão de uma PA, mostrando os 10 Primeiros Termos da progressão
# Usando a estrutura Whilef

a1 = int(input('Informe o primeiro termo: '))

r = int(input('Informe a razão da PA: '))

n = 1
termo = 0

print('\nOs 10 primeiros termos da PA informada são:')

while n < 11:
    termo += 1
    print(f'{termo:2}º Termo = {a1 + (n - 1) * r}')
    n += 1

print('fim')

