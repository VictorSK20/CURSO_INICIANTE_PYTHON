# Escreva um programa que faça o PC pensa em um numero entre 0 e 5 e ´peça para o usuario tenta descobri o numero
# escolhido pela maquina, o programa deve informa se o usuário acertou ou não

from random import randrange
from time import sleep
from colorama import init

init(autoreset=True)

win = '\033[1;92m'
lose = '\033[1;91m'
default = '\033[m'

n_pc = randrange(5)

print('O computador está escolhendo um número aleatório de 0 até 5\nAguarde um momento...')
sleep(7)
print('Pronto o computador já escolheu um número agora é sua vez\n')
sleep(4)

n_user = int(input('Tente acerta o numero escolhido pelo computador de 0 até 5:\n'))

print('Processando...')
sleep(5)

if n_user <= 5:
    if n_user == n_pc:
        print(f'O número escolhido pelo usuario foi {win}{n_user}{default}\nO número escolhido pelo computador foi: {lose}{n_pc}\n{win}Você venceu !')
    else:
        print(f'O número escolhido pelo usuario foi {win}{n_user}{default}\nO número escolhido pelo computador foi: {lose}{n_pc}\n{lose}Você perdeu !')

else:
    print('Digite um número valido entre 0 a 5')
