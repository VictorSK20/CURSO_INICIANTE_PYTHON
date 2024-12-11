# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Matriz inicial 3x3 preenchida com zeros

# adicionado os valores a matriz 3x3
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'valor[{linha}][{coluna}] '))

# organizando a impressão da matriz 3x3
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print('')
