# Crie um programa para ler Vários Números e colocar em uma Lista.
# Depois disso, crie Duas Listas Extras que vão conter apenas os valores Pares e os valores Ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das Três Listas gerados.

lista_completa = []
lista_pares = []
lista_impares = []

while True:
    continuar = ''
    lista_completa.append(int(input('Digite um número: ')))

    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Deseja digitar outro valor ? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

for i in lista_completa:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Todos os valores digitados foram {lista_completa}')
print(f'Valores Pares {lista_pares}')
print(f'Valores Ímpares {lista_impares}')
