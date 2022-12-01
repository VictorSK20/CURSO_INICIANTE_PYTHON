print('Mostra o salario do funcionario')
print('')

salario = float(input('Informe seu salario: '))
s_base = 15/100 * salario
aumento = salario + s_base
print('O salario atual com aumento de 15% fica = R${:.2f}'.format(aumento))
print('valor aumentado = R${:.2f}'.format(s_base))
