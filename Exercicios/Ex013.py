# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe seu salario: '))

# Calculo do aumento
valor_aumentado = 15 / 100 * salario
aumento = salario + valor_aumentado

# esquerma de cores com Sequence ANSI
# variavel "v" se refere a verde
v = "\033[1;32m"
# variavel "r" se refere a "reset" da cor
r = "\033[m"

# Imprimindo novo valor
print(f'O salario atual do funcionário com aumento de 15% fica = {v}R${aumento:.2f}{r}')
print(f'valor aumentado = {v}R${valor_aumentado:.2f}{r}')
