# Desenvolva um programa que leia o Primeiro Termo e a Razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão


primeiro_termo = int(input('Informe o primeiro termo: '))

razao = int(input('Informe a razão da PA: '))

print('\nOs 10 primeiros termos da PA informada')
for termos in range(1, 10+1):
    print(f'termo {termos} - {primeiro_termo}')
    primeiro_termo += razao

