# Crie um programa que leia o nome de uma cidade e informe se ela começa ou não com o nome Santos

city = input('Digite o nome da cidade:\n').strip()

city = city.lower()


if city == 'santos':
    print('Analisando o codigo:\nO usuário nasceu em Santos')
    print(city[:6] == 'santos')

else:
    print('Analisando o codigo:\nO usuário não nasceu em Santos')
    print(city[:6] == 'santos')
