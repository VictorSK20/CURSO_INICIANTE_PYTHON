# Desenvolva um programa que leia Seis Números Inteiros e mostre a soma apenas daqueles que forem Pares.
# Se o valor digitado for Impar, desconsidere-o
soma = 0
numeros_pares = []

for n in range(1, 6 + 1):
    num = int(input(f'Informe o {n}º número: '))
    if num % 2 == 0:
        soma += num
        numeros_pares.append(num)


print(f'Números pares: {numeros_pares}')

print(f'a soma total dos números pares: {soma}')
