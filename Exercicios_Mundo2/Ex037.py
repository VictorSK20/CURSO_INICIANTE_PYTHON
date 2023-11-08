<<<<<<< HEAD
"""
 Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a BASE DE CONVERSÃO
 1 para Binário
 2 para octal
 3 para hexadecimal
 """

print('Programa para conversão de numero decimal para Binario, Octal e Hexadecimal')

num = int(input('Digite um numero a ser convertido: '))

print('para qual Base gostaria de converter o número ?')

base_conversao = int(input('\n'
                           'Escolha qual Base de Conversão deseja utilizar de acordo com os números abaixo\n'
                           '1 - Binário\n'
                           '2 - Octal\n'
                           '3 - Hexadecimal\n'
                           'Base de Conversão escolhida →: '))

if base_conversao == 1:
    bi = bin(num)[2::]
    print(f' Binario = {bi:}')

elif base_conversao == 2:
    octal = oct(num)[2::]
    print(f' Octal = {octal}')

elif base_conversao == 3:
    hexa = hex(num)[2::]
    print(f' Hexadecimal = {hexa}')
else:
    print('Escolha somente os numeros informado acima, 1, 2 ou 3')
=======
"""
 Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a BASE DE CONVERSÃO
 1 para Binário
 2 para octal
 3 para hexadecimal
 """

print('Programa para conversão de numero decimal para Binario, Octal e Hexadecimal')

num = int(input('Digite um numero a ser convertido: '))

print('para qual Base gostaria de converter o número ?')

base_conversao = int(input('\n'
                           'Escolha qual Base de Conversão deseja utilizar de acordo com os números abaixo\n'
                           '1 - Binário\n'
                           '2 - Octal\n'
                           '3 - Hexadecimal\n'
                           'Base de Conversão escolhida →: '))

if base_conversao == 1:
    bi = bin(num)[2::]
    print(f' Binario = {bi:}')

elif base_conversao == 2:
    octal = oct(num)[2::]
    print(f' Octal = {octal}')

elif base_conversao == 3:
    hexa = hex(num)[2::]
    print(f' Hexadecimal = {hexa}')
else:
    print('Escolha somente os numeros informado acima, 1, 2 ou 3')
>>>>>>> 2a13c86a50f88adb3afe2d544d692c2976fd869f
