# Faça um programa que Leia 3 números e mostre qual é o maior e menor.

print('Informe 3 numeros inteiros, e descubra o maior e o menor entre eles: ')

# criando condições para tentativas de erro
# os erros serão se digitar numeros iguais e letras
try:
    num1 = int(input('Informe o primeiro número:\n'))
    num2 = int(input('Informe o segundo número:\n'))
    num3 = int(input('Informe o terceiro número:\n'))
except ValueError:
    print('Digite apenas numeros')


if num2 == num1 and num2 == num3:
    print('Não use numeros repetidos')

elif num3 == num1 and num3 == num2:
    print('Não use numeros repetidos')

elif num1 == num3 and num1 == num2:
    print('Não use numeros repetidos')

# Verificando qual o maior número digitado
else:
    if num2 > num1 and num2 > num3:
        print(f'O maior número digitado é {num2}: ')

    elif num3 > num2 and num3 > num1:
        print(f'O maior número digitado é {num3}:')

    else:
        print(f'O maior número digitado é {num1}:')

# Verificando qual o menor número digitado
if num1 < num2 or num1 < num3:
    print(f'E o menor número digitado é {num1}:')

elif num2 < num1 or num2 < num3:
    print(f'E o menor número digitado é {num2}:')

else:
    print(f'E o menor número digitado é {num3}:')
