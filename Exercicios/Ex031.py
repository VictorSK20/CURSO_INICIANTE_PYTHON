# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da viagem
# cobrando R$0,50 por Km para viagem de até 200Km e R$0,45 para viagens mais longas

import math

passagem = float(input('Qual será a distância da viagem\n'))
preco1 = 0.50
preco2 = 0.45

if passagem <= 200.00:
    total = preco1 * passagem
    print(f'O valor da viagem esta a {total:.2f}R$')
else:
    total = preco2 * passagem
    print(f'O valor da viagem esta a {total:.2f}R$')
