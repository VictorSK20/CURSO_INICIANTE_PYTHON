# Faça um programa que leia Nome e Média de um aluno, guardando também a Situação em um Dicionário.
# No final, mostre o conteúdo da estrutura na tela.

alunos = {'nome': str(input('Nome: '))}
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))

if alunos['media'] < 7:
    alunos['situacao'] = 'Reprovado'
elif alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'

print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
print(f'Situação é igual a {alunos["situacao"]}')
