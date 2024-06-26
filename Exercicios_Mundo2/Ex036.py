"""
Crie um programa que aprove o emprétismo bancário para a compra de uma casa.
O programa vai pergunta o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""

print(f'\t\033[1;93mSeja bem Vindo(a) !\033[0m\n'
      f'\033[91mOBS: para o emprestimo ser aceito em nosso sistema, o valor da prestação mensal não pode exceder 30% do seu salário\033[0m')
ValorCasa = float(input('\tImpréstimo\nInforme o valor da casa: '))
salario = float(input('Informe seu salário: '))
AnoPagar = int(input('Informe em quantos anos será pago o empréstimo: '))

# Calculo da prestação mensal
ParcelaAno = ValorCasa / (AnoPagar*12)

if ParcelaAno > (30 / 100 * salario):
    print(f'\nEmpréstimo negado, pois o emprestimo no valor de R${ValorCasa:,.2f} '
          f'excede 30% do salário de R${salario:,.2f} a ser pago a cada mês')
    print(f'30% do salario = {(salario * 30 / 100 ):,.2f}')
    print(f'Prestação Mensal = {ParcelaAno:.2f}')

else:
    print(f'\nEmpréstimo de R${ValorCasa:,.2f} foi aceito pelo banco')
    print(f'Valor a ser pago a cada mês durante {AnoPagar} anos será de R${ParcelaAno:,.2f}')
    print(f'30% do salario = {(30 / 100 * salario):,.2f}')
