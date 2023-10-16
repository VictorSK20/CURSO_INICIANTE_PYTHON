# Crie um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para salários inferiores ou igual, o aumento é de 15%
from colorama import init

init(autoreset=True)

salario = float(input('Informe seu salário: \n'))

# cor verde
green = '\033[1;92m'

# cor vermelha
red = '\033[1;91m'

if salario > 0:
    if salario > 1250.00:
        aumento = salario * 10 / 100
        print(f'{green}O funcionário tem o salário de {salario:.2f} e tera um aumento de {aumento} e tera o salário total de {salario + aumento}')

    elif salario <= 1250.00:
        aumento = salario * 15 / 100
        print(f'{green}O funcionário tem o salário de {salario:.2f} e tera um aumento de {aumento} e tera o salário total de {salario + aumento}')
    
else:
    print(f'{red}Digite um valor válido')
