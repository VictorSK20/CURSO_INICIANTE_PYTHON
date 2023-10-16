"""
Crie um programa que aprove o emprétismo bancário para a compra de uma casa.
O programa vai pergunta o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""

ValorCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
AnoPagar = int(input('Informe em quantos anos será pago o empréstimo: '))

# Calculo da restação mensal
ParcelaAno = ValorCasa / (AnoPagar*12)

if ParcelaAno > (30 / 100 * salario):
    print(f'Empréstimo negado, pois o emprestimo no valor de R${ValorCasa:,.2f} '
          f'excede 30% do salário de R${salario:,.2f} a ser pago a cada mês')
    print(f'30% do salario = {(30 / 100 * salario):,.2f}')
else:
    print(f'Empréstimo de R${ValorCasa:,.2f} foi aceito pelo banco')
    print(f'Valor a ser pago a cada mês durante {AnoPagar} anos será de R${ParcelaAno:,.2f}')
