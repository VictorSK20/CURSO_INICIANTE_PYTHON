# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo
"""
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida
"""

print('Descubra seu IMC')

try:
    peso = float(input('Informe seu peso: '))

    altura = float(input('Informe sua altura: '))

    imc = peso / (altura ** 2)

    if imc >0 and imc < 18.5:
        print(f'Seu IMC é de {imc:.2f}: Você esta abaixo do peso')

    elif imc >= 18.5 and imc <25:
        print(f'Seu IMC é de {imc:.2f}: Você esta no peso ideal')

    elif imc >=25 and imc <=40:
        print(f'Seu IMC é de {imc:.2f}: Você esta com sobrepeso')

    elif imc > 40:
        print(f'Seu IMC é de {imc:.2f}: Você esta com obesidade mórbida')

    else:
        print('\033[1;31mValor informado inválido\033[m')

except ValueError:
    print('\033[1;31mValor informado inválido\033[m')
