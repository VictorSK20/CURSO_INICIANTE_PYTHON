# Crie um programa onde 4 Jogadores joguem um Dado e tenham resultados Aleatórios. Guarde esses resultados em um Dicionário.
# No final, coloque esse dicionário em Ordem, sabendo que o Vencedor tirou o Maior Número no dado

from time import sleep
from random import randint
from operator import itemgetter
jogadores = {}
rank = {}

# criando range de tamanho 4 para adiciona um valor de 1 a 6 em cada range
for index in range(1, 5):
    jogador = f'jogador{index}'
    jogadores[jogador] = randint(1, 6)

# Exibindo os resultados dos números aleatorios
print(("-=" * 7), 'Valores Sorteados', ("-=" * 7))
for j, d in jogadores.items():
    print(f'               O {j} tirou {d}')
    sleep(1)

# exibindo os resultados em ordem do maior para o menor
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # organizando os valores pelo values do dist

pos = 0
print(("-=" * 6), 'RANKING DOS JOGADORES', ("-=" * 6))
for j, d in rank:
    pos += 1
    print(f'         {pos}º lugar esta o {j} com {d}')
    sleep(1)
