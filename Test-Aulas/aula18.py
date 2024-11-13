#  Manipulação de Listas


"""
*___________________________________________________*
| ['Victor', 28] | ['Débora', 26] | ['Caio', 24] |  |
|     0       1  |     0      1   |    0     1   |  |
*---------------------------------------------------*
         0                1             2
Exemplos de prints com a lista acima
print(lista[0])    - resultado = ['Victor', 28]
print(lista[1][0]) - resultado = ['Débora']
print(lista[2][1]) - resultado = [24]
"""

# testes 1
'''
galera = list(['Victor', 28]), (['Debora', 26]), (['Caio', 24])  # Criando várias listas dentro de outra lista

print(galera[0][0])  # imprimido uma posição expecifica da lista

# Criando pulando uma linha a cada lista
for index in galera:
    print(f"{f'Nome: {index[0]:<7} - Idade: {index[1]}'}")
'''

# testes 2
galera = []
dado = []
maior = menor = 0
for c in range(3):
    dado.append(str(input('Informe seu nome: ')))
    dado.append(int(input('Informe sua idade: ')))
    galera.append(dado[:])  # atenção neste append, append(dado[:]) = copia - append(dado) = todas as listas iria fica iguais
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    elif p[1] < 18:
        print(f'{p[0]} é menor de idade')
        menor += 1

print(f'Temos {maior} pessoas maior de idade e {menor} menor de idade')
