<<<<<<< Updated upstream:Exercicios_Mundo1/Ex007.py
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


=======
print('Mostra a nota do Aluno')
print('')

# Criando a função "media" e passando como parametro ("nota1" e "nota2")
def media(nota1, nota2):
    media_aluno = (nota1 + nota2) / 2
    if media_aluno < 8:
        print(f'Aluno tirou media {media_aluno}\n\033[1;31mAluno reprovado\033[0m')
    else:
        print(f'Aluno tirou media {media_aluno}\n\033[1;32mAluno aprovado\033[0m')


nota1 = float(input('Informe a primeira nota do aluno: '))
if nota1 < 0 or nota1 > 10:
    print('Nota inválida. As notas devem estar entre 0 e 10.')
else:
    nota2 = float(input('Informe a segunda nota do aluno: '))

    if nota2 < 0 or nota2 > 10:
        print('Nota inválida. As notas devem estar entre 0 e 10.')
    else:
        media(nota1, nota2)
>>>>>>> Stashed changes:Exercicios/Ex007.py
