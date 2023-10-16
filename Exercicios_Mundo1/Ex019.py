#Faça um programa que ajude a um professor sortear um dos 4 alunos para
# apaga o quadro

import random

# Cor Amarela
cor1 ='\033[1;93m'

# Cor Verde
cor2 ='\033[1;92m'

# Cor Vermelha
cor3 ='\033[1;91m'

# Reseta cor
cor0 ='\033[m'

print('Informe os nomes dos alunos')
alunos = input(f'{cor1}Informe o nome primeiro aluno: \n'), \
         input(f'{cor2}Informe o nome do segundo aluno: \n'), \
         input(f'{cor1}Informe o nome do terceiro aluno: \n'), \
         input(f'{cor2}Informe o nome do quarto aluno: \n')

print(f'{cor1}O aluno sorteado para apaga o quadro é {cor3}{random.choice(alunos)}')
