# Crie um programa que leia a velocidade de um carro
# Se o carro ultrapassa 80Km/h, mostre uma mensagem dizendo que o motorista foi multado
# A multa custa 7.00R$ por cada Km acima de 80Km/h

carro = int(input('Qual a velocidade do carro: '))

if carro >80:
    multa = float(carro - 80) * 7
    print(f'Você foi multado por correr a {carro}Km/h em uma pista de 80Km/h')
    print(f'Valor da multa {multa:.2f}R$')

else:
    print('Direção segura')
