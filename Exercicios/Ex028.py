# Escreva um programa que faça o PC pensa em um numero entre 0 e 5 e ´peça para o usuario tenta descobri o numero
# escolhido pela maquina, o programa deve informa se o usuário acertou ou não

from random import randrange
from time import sleep

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
        print(f'O número escolhido pelo usuario foi {n_user}\nO número escolhido pelo computador foi: {n_pc}\nVocê venceu !')
    else:
        print(f'O número escolhido pelo usuario foi {n_user}\nO número escolhido pelo computador foi: {n_pc}\nVocê perdeu !')

else:
    print('Digite um número valido entre 0 a 5')
