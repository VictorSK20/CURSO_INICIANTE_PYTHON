# Crie um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para salários inferiores ou igual, o aumento é de 15%

salario = float(input('Informe seu salário: \n'))

if salario > 1250.00:
    aumento = salario * 10 / 100
    print(f'O funcionário tem o salário de {salario:.2f} e tera um aumento de {aumento} e tera o salário total de {salario + aumento}')

elif salario <= 1250.00:
    aumento = salario * 15 / 100
    print(f'O funcionário tem o salário de {salario:.2f} e tera um aumento de {aumento} e tera o salário total de {salario + aumento}')
    
else:
    print('Digite um valor válido')
