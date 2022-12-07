#O programa vai ler o comprimento do cateto oposto e do cateto adjacente
# de um triangulo , retângulo, é calculado e mostrado o o resultado da hipotenusa

print ('Calculo do Triângulo Retãngulo')

'''
cateto_oposto = (float(input('Informe o tamanho do Cateto Oposto: ')))
cateto_adjacente = (float(input('Informe o tamanho do Cateto Adjacente: ')))
hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2))**0.5

print(f'O resultado da Hipotenusa é = {hipotenusa}')
'''

import math

c1 = (float(input('Informe o valor do Cateto Oposto: ')))
c2 = (float(input('Informe o valor do Cateto adjacente: ')))

potencia = (math.pow(c1, 2) + math.pow(c2, 2))
raiz = math.sqrt(potencia)
print(f'O valor da Hipotenusa é = {raiz:.4f}')


#co = float(input('Informe o valor do Cateto Oposto: '))
#ca = float(input('Informe o valor do Cateto Adjacente: '))
#hi = math.hypot(co, ca)

#print(f'O valor da Hipotenusa é = {hi}')
