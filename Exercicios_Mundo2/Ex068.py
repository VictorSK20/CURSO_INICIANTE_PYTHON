# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será imterrompido quando
# o jogador Perder. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
from colorama import init

init(autoreset=True)  # Reseta a cor para o padrão em cada linha

# Cores
red = '\033[31m'
gleen = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
reset = '\033[m'

jogador = vencer = 0  # Iniciando a variavel jogador e vencer

print(f'JOGUE PAR OU ÍMPAR COM O COMPUTADOR\nQUE VENÇA O MELHOR !!!\n')

while True:

    #  Loop para a escolha de PAR ou IMPAR
    while True:
        escolha = str(input('Qual sua escolha (PAR / IMPAR) = ')).upper().strip()
        if escolha in ['PAR', 'IMPAR']:
            break
        print(f'Escolha somente PAR OU IMPAR, você digitou {escolha}')

        # Se o usuário escolher PAR a maquina será IMPAR e vice-versa
        if escolha == 'PAR':
            computador_escolha = 'IMPAR'
        elif escolha == 'IMPAR':
            computador_escolha = 'PAR'

    # Loop para escolha de 0 á 5
    while True:
        jogador = int(input('Favor para o jogo escolha somente entre o digito 0 até 5 = '))
        if jogador < 6:
            break
        print(f'Favor escolha somente entre 0 á 5\nVocê digitou {jogador}')

    computador = randint(0, 5)
    soma = jogador + computador
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

    # Adicionando um time de 3 segundos para exibir os resultados
    for i in range(0, 4):
        print(i, end='...')
        sleep(1)

    print(f'\n{yellow}Jogador{reset} = {jogador}\n{blue}Computador{reset} = {computador}\n{soma} Deu = {resultado}')

    if resultado == escolha:
        print(f'{gleen}\nVocê Venceu !!!')
        vencer += 1
    else:
        print(f'{red}\nVocê Perdeu !!!')
        break

print(f'\nO jogador venceu {vencer}x')  # É informando quantas vezes o usúario venceu
