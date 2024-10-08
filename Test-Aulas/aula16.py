# Aula sobre TUPLAS "Varíaveis Compostas"

lanche = ('Pizza', 'Suco', 'Pudim', 'Guarana', 'Bolo', 'Churrasco', 'Café', 'Sopa')

#print(lanche[0:])
#print(lanche[0:8:2])

'''for posicao, comida in enumerate(lanche):
    print(f'Vou comer: {comida}, este é o item: {posicao}')

for contagem in range(0, len(lanche)):
    print(lanche[contagem])

for i in lanche:
    print(i)

print(sorted(lanche))
'''

a = (1, 3, 7)
b = (2, 1, 5, 7)
c = a+b

c_info = c
c_tamanho = len(c)
c_contar = c.count(2)

print(c_contar)
