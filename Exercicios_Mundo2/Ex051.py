# Desenvolva um programa que leia o Primeiro Termo e a Razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

a1 = int(input('Informe o primeiro termo: '))

r = int(input('Informe a razão da PA: '))

n = 10

formula_geral_PA = a1 + (n - 1) * r

print('\nOs 10 primeiros termos da PA informada são → ', end='')
for termos in range(a1, formula_geral_PA + 1, r):
    print(f'{a1}', end=' ')
    a1 += r

