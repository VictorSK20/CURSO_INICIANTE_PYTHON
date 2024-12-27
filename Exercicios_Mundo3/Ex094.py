# Crie um programa que leia Nome, Sexo e Idade de Várias Pessoas, guardando os dados de cada pessoa em um Dicionário
# Todos os dicionários devem ser guardado em uma Lista. No final, mostre:
"""
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""

total_cadastro = []
total_mulheres = []
acima_media = []
pessoas = {}
total_idade = 0

while True:
    # Cadastro de cada pessoa
    pessoas['nome'] = str(input('Nome: ').title())
    pessoas['sexo'] = str(input('Sexo: ').strip().upper()[0])

    if pessoas['sexo'] == "F":
        total_mulheres.append(pessoas['nome'])

    pessoas['idade'] = int(input('Idade: '))
    total_cadastro.append(pessoas.copy())

    total_idade += pessoas['idade']

    continua = str(input('Deseja continuar ? ').strip().upper()[0])
    while continua not in 'SN':
        continua = str(input('Deseja continuar ? ').strip().upper()[0])
    if continua == 'N':
        break

media = total_idade / len(total_cadastro)

if pessoas['idade'] > media:
    acima_media.append(pessoas)

print(f'Total de pessoas cadastradas {len(total_cadastro)}')  # total de pessoas cadastrada

print(f'Media de idade {media:.1f}')  # Calculando a média de idade do grupo

print(f'As mulheres cadastradas foram: {total_mulheres}')  # Informando os nome somente das mulheres

print(f'pessoas que estão acima da média {acima_media}')

print(total_cadastro)
