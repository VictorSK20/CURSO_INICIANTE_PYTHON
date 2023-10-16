# Faça um programa que Leia 3 números e mostre qual é o maior e menor.

from colorama import init

init(autoreset=True)

# Verde
cor1 = '\033[1;92m'

# Amarelo
cor2 = '\033[1;93m'

# Ciano
cor3 = '\033[1;94m'

# Vermelho
cor4 = '\033[1;91m'

print('Informe 3 numeros inteiros, e descubra o maior e o menor entre eles: ')

# Iniciando as variavéis com valores padrão - para evita o erro "can be undefined"
num1 = None
num2 = None
num3 = None

# criando condições para tratamento de erro
# os erros serão se digitar numeros iguais e letras
try:
    num1 = int(input('Informe o primeiro número: \n'))
    num2 = int(input('Informe o segundo número: \n'))
    num3 = int(input('Informe o terceiro número: \n'))
except ValueError:
    print(f'{num3}Digite apenas numeros')


if num2 == num1 or num2 == num3:
    print(f'{cor3}Não use numeros repetidos')

elif num3 == num1 or num3 == num2:
    print(f'{cor3}Não use numeros repetidos')

elif num1 == num3 or num1 == num2:
    print(f'{cor3}Não use numeros repetidos')

# Verificando qual o maior número digitado
else:
    if num2 > num1 or num2 > num3:
        print(f'{cor1}O maior número digitado é: {num2}')

    elif num3 > num2 or num3 > num1:
        print(f'{cor1}O maior número digitado é: {num3}')

    else:
        print(f'{cor1}O maior número digitado é: {num1}')

# Verificando qual o menor número digitado
    if num1 < num2 or num1 < num3:
        print(f'{cor2}E o menor número digitado é: {num1}')

    elif num2 < num1 or num2 < num3:
        print(f'{cor2}E o menor número digitado é: {num2}')

    else:
        print(f'{cor2}E o menor número digitado é: {num3}')
