# Crie um programa onde o usuário possa digitar sete valores numéricos
# Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente

valores = [[], []]

for index in range(1, 8):
    n = int(input(f'{index}º Número: '))
    if n % 2 == 0:
        valores[0].append(n)
    elif n % 2 == 1:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print(f'Valores pares {valores[0]}')
print(f'Valores ímpares {valores[1]}')
