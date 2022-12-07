#Faça um programa que ajude a um professor sortear um dos 4 alunos para
# apaga o quadro

import random
print('Informe os nomes dos alunos')
alunos = input('Informe o nome primeiro aluno: \n'), \
         input('Informe o nome do segundo aluno: \n'), \
         input('Informe o nome do terceiro aluno: \n'), \
         input('Informe o nome do quarto aluno: \n')

print(f'O aluno sorteado para apaga o quadro é {random.choice(alunos)}')
