# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[], []]
c = 0

for l in range(3):
    linha = int(input(f'Informe a posição [{l}][{c}] '))
    matriz[0].append(linha)
    for c in range(3):
        coluna = int(input(f'Informe a posição [{l}][{c}] '))
        matriz[1].append(coluna)

print(matriz)
'''

matriz = []


print(f'{matriz}')

