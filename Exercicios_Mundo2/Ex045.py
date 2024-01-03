# Crie um programa que faça o computador jogar JOKENPÔ com você

from random import choice
from emoji import emojize

# função de cores
def cor(color, texto):
    if color == 'ganhar':
        return f'\033[1;38;5;46m{texto}\033[m'  # Verde
    elif color == 'perder':
        return f'\033[1;38;5;124m{texto}\033[m'  # Vermelho
    elif color == 'empate':
        return f'\033[1;38;5;208m{texto}\033[m'  # Laranja
    elif color == 'erro':
        return f'\033[1;38;2;255;0;0m{texto}\033[m'  # Vermelho diferente para mensagens de erro
    elif color == 'pedra':
        return f'\033[1;38;5;58m{texto}\033[m'  # Marrom
    elif color == 'papel':
        return f'\033[1;38;5;14m{texto}\033[m'  # Ciano
    elif color == 'tesoura':
        return f'\033[1;38;5;1m{texto}\033[m'  # Laranja
    elif color == 'principal':
        return f'\033[1;38;5;226m{texto}\033[m'  # Amarelo
    elif color == 'titulo':
        return f'\033[1;38;5;5m{texto}\033[m'  # Vermelho rosa
    elif color == 'escolhar':
        return f'\033[1;38;5;198m{texto}\033[m'  # Lilas
    elif color == 'escolhar1':
        return f'\033[1;38;5;199m{texto}\033[m'  # Rosa
    elif color == 'escolhar2':
        return f'\033[1;38;5;200m{texto}\033[m'  # Rosa
    elif color == 'escolhar3':
        return f'\033[1;38;5;201m{texto}\033[m'  # Rosa


try:
    print(cor('principal', f"{' j O K E N P Ô ':=^60}\n"))

    print(emojize(cor('titulo', 'ESCOLHAR: :raised_fist: ----- :hand_with_fingers_splayed: ----- :victory_hand:\n')))

    print(emojize(cor('pedra', '[1] = PEDRA: [:raised_fist:]\n')))  # raised_fist = Pedra

    print(emojize(cor('papel', '[2] = PAPEL: [:hand_with_fingers_splayed:]\n')))  # hand_with_fingers_splayed = Papel

    print(emojize(cor('tesoura', '[3] = TESOURA: [:victory_hand:]\n')))  # victory_hand = Tesoura

    # Escolha do jogador
    jokenpo = int(input(cor('escolhar', 'Faça sua escolha:\n' + cor('escolhar1', '* 1 para: Pedra\n') + cor('escolhar2', '* 2 para: Papel\n') + cor('escolhar3', '* 3 para: Tesoura\n'))))

    # randomizando a escolha de pedra, papel, tesoura para o computador
    escolhas_computador = (':raised_fist:', ':hand_with_fingers_splayed:', ':victory_hand:')
    computador = choice(escolhas_computador)

    if jokenpo == 1:
        print(emojize(':raised_fist:'))
        if computador == ':raised_fist:':
            print(cor('empate', f'{emojize(computador)}\nEMPATE !'))
        elif computador == ':hand_with_fingers_splayed:':
            print(cor('perder', f'{emojize(computador)}\nVOCÊ PERDEU !'))
        elif computador == ':victory_hand:':
            print(cor('ganhar', f'{emojize(computador)}\nVOCÊ GANHOU !'))

    elif jokenpo == 2:
        print(emojize(':hand_with_fingers_splayed:'))
        if computador == ':raised_fist:':
            print(cor('ganhar', f'{emojize(computador)}\nVOCÊ GANHOU !'))
        elif computador == ':hand_with_fingers_splayed:':
            print(cor('empate', f'{emojize(computador)}\nEMPATE !'))
        elif computador == ':victory_hand:':
            print(cor('perder', f'{emojize(computador)}\nVOCÊ PERDEU !'))

    elif jokenpo == 3:
        print(emojize(':victory_hand:'))
        if computador == ':raised_fist:':
            print(cor('perder', f'{emojize(computador)}\nVOCÊ PERDEU !'))
        elif computador == ':hand_with_fingers_splayed:':
            print(cor('ganhar', f'{emojize(computador)}\nVOCÊ GANHOU !'))
        elif computador == ':victory_hand:':
            print(cor('empate', f'{emojize(computador)}\nEMPATE !'))

    else:
        print('É permitido somente os números 1, 2 e 3.')

except ValueError:
    print(cor('erro', 'Erro !'))

