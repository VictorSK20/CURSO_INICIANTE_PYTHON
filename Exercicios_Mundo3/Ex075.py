# Desenvolva um programa que leia Quatro Valores pelo Teclado e guarde-os em uma TUPLA. No final mostre:
"""
A) Quantos vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

valores = (n1, n2, n3, n4)

print(f'Você digitou os valores {valores}')

# Questão A
print(f'O valor 9 apareceu {valores.count(9)} vezes')

# Questão B
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3) + 1}')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')

# Questão C
pares_encontrados = False

print('Os valores pares digitado foram: ', end='')
for pares in valores:
    if pares % 2 == 0:
        print(pares, end=' ')
        pares_encontrados = True

if not pares_encontrados:
    print('Nenhum valor par foi encontrado')
