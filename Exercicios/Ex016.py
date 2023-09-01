#Informe um numero Float e mostre seu resultado em inteiro
'''
import math
numf = (float(input('Informe um numero: ')))
resultado = math.floor(numf)
print(f'O numero {numf} \ntem a parte inteira = {resultado}')
'''

# cor amarela
cor1 = '\033[1;93m'

# cor azul ciano
cor2 = '\033[1;94m'

# remover cor
nocor = '\033[m'

num = float(input('informe um numero em casa decimal e receber o retorno em inteiro: '))
print(f'O numero {cor1}{num}{nocor} tem sua propoção inteira = {cor2}{int(num)}{nocor}')
