# Crie um programa que leia a velocidade de um carro
# Se o carro ultrapassa 80Km/h, mostre uma mensagem dizendo que o motorista foi multado
# A multa custa 7.00R$ por cada Km acima de 80Km/h

from colorama import init
init(autoreset=True)

# cores

# Azul
cor1 = '\033[94m'

# Vermelha
cor2 = '\033[91m'

# Verde
cor3 = '\033[92m'

velocidade = int(input(f'{cor1}Qual a velocidade do carro: '))

if velocidade > 80:
    multa = float(velocidade - 80) * 7
    print(f'{cor2}Você foi multado por correr a {velocidade}Km/h em uma pista de 80Km/h')
    print(f'{cor2}Valor da multa R${multa:.2f}')

else:
    print(f'{cor3}Motorista esta seguindo uma direção segura\nTenha um bom dia !')
