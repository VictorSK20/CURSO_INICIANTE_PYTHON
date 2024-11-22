# Crie um programa onde o usúario possa digitar cinco Valores Númericos e cadastre-os em uma Lista.
# Já na posição correta de inserção (sem usar o sort()). No final, mostre a Lista Ordenada na tela

valores = []
for cont in range(5):
    valor = int(input(f'Informe o {cont +1}ª valor: '))
    if len(valores) == 0 or valor > valores[-1]:
        print(f'O valor {valor} foi adicionado na última posição da lista')
        valores.append(valor)
    else:
        for i in range(len(valores)):
            if valor < valores[i]:
                valores.insert(i, valor)
                print(f'O valor {valor} foi adicionado na {i}º posição da lista')
                break
print('-'*60)
print(f"{f'Os valores digitados da lista em ordem: {valores}':^55}")
