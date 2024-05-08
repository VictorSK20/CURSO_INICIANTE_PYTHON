# Crie um programa que leia o Ano de Nascimento de Sete Pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
# Considerando a maior idade em 21 anos

from datetime import datetime

print('A data deve seguir o padrão DD/MM/YYYY\n')
print('Informe a data de nascimento dos setes(7) usuários')

datas_de_nascimento = {}

for a in range(1, 7+1):
    data_nascimento = input(f'Informe a data de nascimento da {a}° pessoa\n')
    data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y')
    datas_de_nascimento[a] = data_formatada

for usuario, data in datas_de_nascimento.items():
    print(f'O usuário {usuario} nasceu em: {data.strftime("%d/%m/%Y")}')