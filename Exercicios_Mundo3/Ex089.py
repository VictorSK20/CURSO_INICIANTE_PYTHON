# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    # Nome e notas do/s aluno/s
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    alunos.append([nome, nota1, nota2])

    # Condição de parada
    continua = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if continua == 'N':
        break

# Imprimindo o nome e media de todos alunos
print("-=" * 30)
print(f'{"ID.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 60)
for index, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{index:>2}'.ljust(3), f'{aluno[0]:<10}{media:>8.2f}')
print('-=' * 30)


while True:
    ID_nota = int(input('Informe o ID de qual aluno deseja ver as notas? (OBS: Informe 999 para finalizar) '))
    if ID_nota == 999:
        break
    elif ID_nota < len(alunos):
        print(f'\033[1mAs notas do aluno(a) {alunos[ID_nota][0]} são {alunos[ID_nota][1]} - {alunos[ID_nota][2]}\033[m')
    else:
        print('Aluno não encontrado')
