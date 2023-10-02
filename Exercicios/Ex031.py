# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da viagem
# cobrando R$0,50 por Km para viagem de até 200Km e R$0,45 para viagens mais longas

from colorama import init

init(autoreset=True)

# Amarelo
cor1 = '\033[38;2;255;192;0m'

# Laranja
cor2 = '\033[38;2;255;128;0m'

passagem = float(input('Qual será a distância da viagem\n'))
preco1 = 0.50
preco2 = 0.45

if passagem <= 200.00:
    total = preco1 * passagem
    print(f'{cor1}O valor da viagem esta a {total:.2f}R$\n\n')
else:
    total = preco2 * passagem
    print(f'{cor2}O valor da viagem esta a {total:.2f}R$\n\n')

print(f'{cor1}Viagens de até 200Km é cobrado R$0,50 por cada Kilometro \n'
      f'{cor2}Viagens acima de 20Km é cobrado R$0,45 por cada Kilometro')
