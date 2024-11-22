# Crie um programa que vai ler Vários Números e colocar em uma Lista. Depois disso mostre:
"""
A) Quantos números foram digitados
B) A lista de valores em ordem decrescente
C) Se o valor 5 foi digitado ou não na lista
"""
numeros = []
continuar = 'S'
rept = 1
valores_em_ordem = numeros

while continuar == 'S':
    for n in range(rept):
        numeros.append(int(input(f'Informe o {rept}º número: ')))
        rept += 1

        continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
        if continuar == 'N':
            break

        # esta linha será utilizada caso o úsuario informe um comando ínvalido
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Favor digite somente [S] para sim ou [N] para não')).upper().strip()[0]
            if continuar == 'N':
                break

print('-='*40)
print(f'Valores digitados {numeros}')
print(f'O total de números digitados foram {len(numeros)}')

valores_em_ordem.sort(reverse=True)
print(f'Lista dos valores digitados em ordem decrescente {valores_em_ordem}')

if 5 in numeros:
    print(f'O número {5} esta na lista, e esta localizado na posição {numeros.index(5)}')
else:
    print(f'O valor {5} não esta na lista')
print('-='*40)
