# Aprimore o desafio anterior, mostrando no final:
' A) A soma de todos os valores pares digitados. '
' B) A soma dos valores da terceira coluna. '
' C) O maior valor da segunda linha. '

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
segunda_linha = []
somar_par = terceira_coluna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        matriz[linha][coluna] = int(input(f'Posição [{linha}][{coluna}] '))

print('*'*30)

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()

print('*'*30)

# A) comando FOR para retorna os valores pares
for elementos in matriz:
    for num_pares in elementos:
        if num_pares % 2 == 0:
            somar_par += num_pares
print(f'A soma dos valores pares = {somar_par}')

# B) comando FOR para soma os valores da terceira coluna
for linha in range(len(matriz)):
    terceira_coluna += matriz[linha][2]  # armazenando o valor da terceira coluna na variavel terceira_coluna

print(f'A soma dos valores da terceira coluna = {terceira_coluna}')

# C) O maior valor da segunda linha
for linha in range(len(matriz)):
    segunda_linha.append(matriz[1][linha])  # armazenando o valor da segunda linha em segunda_linha

print(f'O valor mais alto da segunda linha = {max(segunda_linha)}')
