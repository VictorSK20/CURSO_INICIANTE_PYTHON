# Crie um programa que leia a velocidade de um carro
# Se o carro ultrapassa 80Km/h, mostre uma mensagem dizendo que o motorista foi multado
# A multa custa 7.00R$ por cada Km acima de 80Km/h

velocidade = int(input('Qual a velocidade do carro: '))

if velocidade > 80:
    multa = float(velocidade - 80) * 7
    print(f'Você foi multado por correr a {velocidade}Km/h em uma pista de 80Km/h')
    print(f'Valor da multa R${multa:.2f}')

else:
    print('Motorista esta seguindo uma direção segura\n Tenha um bom dia !')
