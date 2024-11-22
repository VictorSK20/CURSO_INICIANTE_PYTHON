# Faça um programa que leia Nome e Peso de Várias Pessoas, guardando tudo em uma Lista.
# No final, mostre:

"""
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais Pesadas
C) Uma listagem com as pessoas mais Leves
"""
pessoas = list()
dados = list()
pessoas_leve = list()
pessoas_pesada = list()
peso_maior = peso_menor = 0

while True:
    dados.append(str(input('Informe o nome: ').capitalize()))
    dados.append(float(input('Informe o peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continua = str(input('Deseja continua [S/N] ?')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Entrada ínvalida, favor informe S para SIM ou N para NÃo')).upper().strip()[0]
    if continua == 'N':
        break

for n, p in enumerate(pessoas):
    if n == 0:
        peso_maior = peso_menor = p[1]
        pessoas_pesada = [p[0]]
        pessoas_leve = [p[0]]
    else:
        if p[1] > peso_maior:
            peso_maior = p[1]
            pessoas_pesada = [p[0]]
        elif p[1] == peso_maior:
            pessoas_pesada.append(p[0])

        if p[1] < peso_menor:
            peso_menor = p[1]
            pessoas_leve = [p[0]]
        elif p[1] == peso_menor:
            pessoas_leve.append(p[0])

print(f'Foram cadastrada {len(pessoas)} pessoas')
print(f'Os mais pesados foram {", ".join(pessoas_pesada)} com {peso_maior}kg')
print(f'Os mais leves foram {", ".join(pessoas_leve)} com {peso_menor}kg')
