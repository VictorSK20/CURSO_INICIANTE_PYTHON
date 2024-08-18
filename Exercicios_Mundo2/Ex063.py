# Escreva um programa que leia um Número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência Fibonacci

fibonacci = int(input("Informe quantos elementos em sequência Fibonacci deseja vizualizar: "))
atual = 0

elementos = 0
n1 = 0
n2 = 1

print(f'Os {fibonacci}º elementos da sequência Fibonacci são: ', end='')
print(f'{n1} - {n2}', end=' - ')

while elementos < fibonacci:
    atual = n1 + n2
    print(f'{atual}', end=' - ')
    n1 = n2
    n2 = atual
    elementos += 1
