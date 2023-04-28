# Escreva um programa que faça o PC pensa em um numero entre 0 e 5 e ´peça para o usuario tenta descobri o numero
# escolhido pela maquina, o programa deve informa se o usuário acertou ou não

from random import randrange

n_pc = randrange(5)

n_user = int(input('Tente acerta o numero escolhido pelo computador de 0 até 5:\n'))

if n_user <= 5:
    if n_user == n_pc:
        print(f'o numero escolhido pelo usuario foi {n_user} e o do computador foi computador {n_pc}, Você venceu !')
    else:
        print(f'O numero escolhido pelo usuario foi {n_user} e o escolhido pelo computador {n_pc}, o computador venceu !')

else:
    print('Digite um numero valido entre 0 a 5')
