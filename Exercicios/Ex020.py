#Um professor vai sortear a ordem de apresentação de 4 alunos para ser apresentado
#Faça um programa que leia o nomes dos alunos e mostra a ordem sorteada

import random
alunos = input('Informe o nome do primeiro aluno: \n'), \
         input('Informe o nome do segundo aluno: \n'), \
         input('Informe o nome do terceiro aluno: \n'),\
         input('Informe o nome do quarto aluno: \n')

print(f'A ordem das apresentações: \n{random.sample(alunos, 4)}\n')
