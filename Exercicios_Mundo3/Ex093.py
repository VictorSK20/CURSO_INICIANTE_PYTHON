# crie um programa que gerencie o aproveitamento de um Jogador de Futebol.
# O programa vai ler o Nome do Jogador e Quantas Partidas ele jogou.
# Depois vai ler a Quantidades de Gols feitos em Cada Partida.
# No final, tudo isso será guardado em um Dicionário, incluindo o Total de Gols feitos durante o compeonato

jogador_dados = {'nome': str(input('Nome do Jogador: ').strip().capitalize())}
jogador_dados['partidas'] = int(input(f'Quantas Partidas {jogador_dados["nome"]} jogou? '))
gols = []

# informando quantos gols fez em cada partida
for partida in range(jogador_dados['partidas']):
    gol = int(input(f'Quantos gols na partida {partida + 1}º '))
    gols.append(gol)

# guardando as informações de gols dentro do dicionário jogador_dados e somando o total de gols
jogador_dados['gols'] = gols
jogador_dados['totais_gols'] = sum(jogador_dados['gols'])

# Exibindo os valores do dicionário jogador_dados - 1º forma
print('-='*40)
print(jogador_dados)
print('-='*40)

# Exibindo os valores do dicionário jogador_dados - 2º forma
for chave, valor in (jogador_dados.items()):
    print(f'O campo {chave} tem o valor {valor}')
print('-='*40)

# Exibindo os valores do dicionário jogador_dados - 3º forma
print(f'O jogador {jogador_dados["nome"]} jogou {jogador_dados["partidas"]} partidas')

gol = 0
for partidas in range(jogador_dados['partidas']):
    if jogador_dados['gols'][gol] == 1:
        print(f'Na partida {partidas + 1}º fez {jogador_dados["gols"][gol]} gol')
    elif jogador_dados['gols'][gol] > 1:
        print(f'Na partida {partidas + 1}º fez {jogador_dados["gols"][gol]} gols')
    elif jogador_dados['gols'][gol] == 0:
        print(f'Na partida {partidas + 1}º fez nenhum gol')
    gol += 1
print(f'Total de gols {jogador_dados["totais_gols"]}')
print('-='*40)
