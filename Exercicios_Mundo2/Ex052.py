# Faça um programa que leia um Número Inteiro e diga se ele é ou não Número Primo

n = int(input('Informe um número e descubra se ele é número primo: '))
primo = []  # criando uma lista para exibir os números primos

# criando um laço de repetição do 1 até o número informado pelo usúario
for a in range(1, n+1):
    if n % a == 0:  # se o resto da divisão entre o número 'n' e 'a' for igual a zero, onde a é igual a 1 e n, então o número é primo
        primo.append(a)

if len(primo) == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
