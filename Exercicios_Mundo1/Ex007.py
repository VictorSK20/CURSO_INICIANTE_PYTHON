print('Mostra a nota do Aluno')
print('')


def media(nota1, nota2):
    media_aluno = (nota1 + nota2) / 2
    if media_aluno < 8:
        print(f'\033[31m{nota1}\033[0m')
    else:
        print(f'\033[32m{nota2}\033[0m')


nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

print(f'O aluno tem media ={media(nota1, nota2)}')


