# Aulas sobre Lista "Variavel Composta"

lanche = ['hamburguer', 'suco', 'pudim', 'pizza']
valores = [8, 0, 2, 1, 7, 5, 3, 9]
# valores.sort()  # Mostra os valores de forma organizada, do menor para o maior
valores.sort(reverse=True)  # Mostra os valores de forma organizada, do maior para o menor
print(len(valores))  # Tamanho de index da lista


# lanche[3] = 'picole'  # Adiciona um objeto no index informado
#lanche.append('salada')  # adiciona um objeto na última posição
#lanche.insert(2, 'bolacha')  # adiciona um objeto na posição de outro index

'Comandos de delete'
# lanche.remove('hamgurguer')
# lanche.pop(0)
# del lanche[0]

'fazendo uma ligação entre listas'
a = [7, 4, 1, 9]
# b = a  # Lista B esta fazendo uma ligação com a lista A
b = a[:]  # Lista B esta copiando os valores da lista A
b[2] = 0

print(f'Valor de A{a}')
print(f'Valor de B{b}')

print(valores)
