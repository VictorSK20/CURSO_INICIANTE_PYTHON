# Crie um programa que faça o computador jogar JOKENPÔ com você

import random
import emoji


def cor(escolha, texto):
    if escolha == 'ganhar':
        return f'\033[1;33m{texto}'



try:
    print(f"{' j O K E N P Ô ':=^60}")

    print(emoji.emojize('ESCOLHAR: :raised_fist: ----- :hand_with_fingers_splayed: ----- :victory_hand:\n'))

    print(emoji.emojize('[1] = PEDRA: [:raised_fist:]\n'))  # raised_fist = Pedra

    print(emoji.emojize('[2] = PAPEL: [:hand_with_fingers_splayed:]\n'))  # hand_with_fingers_splayed = Papel

    print(emoji.emojize('[3] = TESOURA: [:victory_hand:]\n'))  # victory_hand = Tesoura

    # Escolha do jogador
    jokenpo = int(input('Faça sua escolhar:\n 1 para: Pedra\n 2 para: Papel\n 3 para: Tesoura\n'))

    # randomizando a escolha de pedra, papel, tesoura para o computador
    escolhas_computador = (':raised_fist:', ':hand_with_fingers_splayed:', ':victory_hand:')
    computador = random.choice(escolhas_computador)

    if jokenpo == 1:
        print(emoji.emojize(':raised_fist:'))
        if computador == ':raised_fist:':
            print(f'{emoji.emojize(computador)}\nEMPATE')
        elif computador == ':hand_with_fingers_splayed:':
            print(cor(f"{emoji.emojize(computador)}\nVOCÊ PERDEU, "))
        elif computador == ':victory_hand:':
            print(f'{emoji.emojize(computador)}\nVOCÊ GANHOU')

    elif jokenpo == 2:
        print(emoji.emojize(':hand_with_fingers_splayed:'))
        if computador == ':raised_fist:':
            print(f'{emoji.emojize(computador)}\nVOCÊ GANHOU')
        elif computador == ':hand_with_fingers_splayed:':
            print(f'{emoji.emojize(computador)}\nEMPATE')
        elif computador == ':victory_hand:':
            print(f'{emoji.emojize(computador)}\nVOCÊ PERDEU')

    elif jokenpo == 3:
        print(emoji.emojize(':victory_hand:'))
        if computador == ':raised_fist:':
            print(f'{emoji.emojize(computador)}\nVOCÊ PERDEU !')
        elif computador == ':hand_with_fingers_splayed:':
            print(f'{emoji.emojize(computador)}\nVOCÊ GANHOU !')
        elif computador == ':victory_hand:':
            print(f'{emoji.emojize(computador)}\nEMPATE !')

    else:
        print('É permitido somente os números 1, 2 e 3.')

except ValueError:
    print('Erro !')
