# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta.

from random import randint
jogos = []
total_jogos = []
cont = 1

palpite = int(input('Informe a quantidade de Palpites que desejar visualizar: '))

# criando jogos em quantidade ao número de palpites
while cont <= palpite:
    # criando uma lista com 6 números
    while len(jogos) < 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)

    jogos.sort()
    total_jogos.append(jogos[:])
    jogos.clear()
    cont += 1

# organizando a impressão dos jogos
for i, j in enumerate(total_jogos):
    print(f'{i + 1}º Jogo = {j}')
