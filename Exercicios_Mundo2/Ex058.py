# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randrange
from time import sleep
from colorama import init

init(autoreset=True)

win = '\033[1;92m'
lose = '\033[1;91m'
default = '\033[m'

n_pc = randrange(10)

n_tentativa = 0

print('O computador está escolhendo um número aleatório de 0 até 10\nAguarde um momento...')
sleep(7)
print('Pronto o computador já escolheu um número agora é sua vez\nTenta acerta o número escolhido pelo computador')
sleep(4)

while True:
    try:
        n_user = int(input('Escolhar um número entre 0 e 10: '))

        while n_pc != n_user:
            print('Verificando', end=' ')
            for n in range(3):
                sleep(1)
                print('.', end='')
                sleep(1)

            if n_user < n_pc:
                print(f'\n\t{lose}Mais...Tente Novamente !!!')
            elif n_user > n_pc:
                print(f'\n\t{lose}Menos...Tente Novamente !!!')

            n_user = int(input('Escolhar um número entre 0 e 10: '))
            n_tentativa += 1

        if n_pc == n_user:
            print(f'Verificando', end=' ')
            for n in range(3):
                sleep(1)
                print('.', end='')
                sleep(1)
            print(f'{win}\nPARABÉNS VOCÊ ACERTOU COM {n_tentativa} TENTATIVAS')

        break
    except ValueError:
        print('digite um valor válido')
