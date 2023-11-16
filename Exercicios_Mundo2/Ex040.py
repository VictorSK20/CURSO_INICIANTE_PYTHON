# Crie um programa que leia duas notas de um aluno e calcule sua média
# Mostrando uma mensagem final, de acordo com a média atingida
# abaixo de 5.0 = REPROVADO - entre 5.0 e 6.9 = RECUPERAÇÃO - igual ou superior a 7.0 = APROVADO
print('Nota dos alunos:')

# Primeira nota
n1 = float(input('Informe a primeira nota do aluno: '))

# Segunda nota
n2 = float(input('Informe a segunda nota do aluno: '))

media = (n1 + n2) / 2


if media > 0 and media <= 5.0:
    print(f'O aluno foi reprovado com: {media}')
elif media > 0 and media >= 7.0:
    print(f'O aluno foi aprovado com: {media}')
elif media > 5.0 and media < 7.0:
    print(f'O aluno esta em recuperação com: {media}')
else:
    print('Digite um valor válido')
