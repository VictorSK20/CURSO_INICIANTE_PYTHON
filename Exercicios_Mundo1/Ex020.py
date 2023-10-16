#Um professor vai sortear a ordem de apresentação de 4 alunos para ser apresentado
#Faça um programa que leia o nomes dos alunos e mostra a ordem sorteada

import random
# cor vermelho
cor1 = '\033[1;38;5;197m'

# cor verde
cor2 = '\033[1;38;5;84m'

# cor amarelo
cor3 = '\033[1;38;5;227m'

# cor laranja
cor4 = '\033[1;38;5;210m'

#cor verde amarelado
cor5 = '\033[1;38;5;192m'

alunos = input(f'{cor1}Informe o nome do primeiro aluno: \n'), \
         input(f'{cor2}Informe o nome do segundo aluno: \n'), \
         input(f'{cor3}Informe o nome do terceiro aluno: \n'),\
         input(f'{cor4}Informe o nome do quarto aluno: \n')

print(f'{cor5}A ordem das apresentações: \n{random.sample(alunos, 4)}\n')
