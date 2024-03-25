# Estrutura de Repetição FOR

# Exibindo uma string x vezes
'''
for c in range(1, 5):
    print('Oi')
'''

# Exibindo o range de c x vezes
"""
for c in range(1, 5):
    print(c)
"""

# Criando um range de numero para o input N
'''
n = int(input('Informe o range de números'))
for c in range(0, n+1):
    print(c, end=' - ')
'''

# teste para criação de tabuadas
'''
n1 = int(input('Informe de qual numero deseja ver a tabuada: '))
for n2 in range(1, 10+1):
    print(f'|{n1:2} + {n2:2} = {n1 + n2:3}|'
          f'\t'
          f'|{n1:2} - {n2:2} = {n1 - n2:3}|'
          f'\t'
          f'|{n1:2} * {n2:2} = {n1 * n2:3}|'
          f'\t'
          f'|{n1:2} / {n2:2} = {n1 / n2:.2f}|')
'''

# criando uma ordem de inicio - fim e passo a passo dos numeros
"""i = int(input('Informe o inicio: '))
f = int(input('Informe o final: '))
p = int(input('Informe o passo: '))
for n in range(i, f + 1, p):
    print(n)
"""

# rependindo um input x vezes e somando os valores
soma = 0
for n in range(0, 5):
     valor = int(input('Informe um número: '))
     soma += valor
print(f'A soma dos valores é = {soma}')
