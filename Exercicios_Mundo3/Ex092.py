# Crie um programa que leia Nome, Ano de Nascimento e Carteira de Trabalho e cadastre-os (com Idade)
# Em um Dicionário se por acaso a CTPS for diferente de Zero, o dicionário receberá também o Ano de Contratação e o Salário.
# Calcule e acrescente, além da Idade, com quantos anos a pessoa vai se Aposentar.

from datetime import datetime

# adicionando dados da pessoa
cadastro = {'nome': str(input('Nome: ')).strip(),
            'ano_nascimento': int(input('Ano de Nascimento: ')),
            'ctps': int(input('Carteira de Trabalho (0 não tem)'))
            }

# Calcular idade
ano_atual = datetime.now().year
cadastro['idade'] = ano_atual - cadastro['ano_nascimento']

# Adicionando as informações da Carteira de Trabalho caso valor de cadastro['ctps'] for maior que 0
if cadastro['ctps'] > 0:
    contrato = int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$'))

    # reservando um valor para ano de contribuição
    ano_contribuicao = 35

    cadastro['contratacao'] = contrato
    cadastro['salario'] = salario

    aposentar = cadastro['idade'] + ((cadastro['contratacao'] + ano_contribuicao) - ano_atual)
    cadastro['aposentadoria'] = aposentar

# exibindo os resultados
for k, v in cadastro.items():
    print(f'{k} tem o valor: {v}')
