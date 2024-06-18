# Desenvolva um programa que leia o Nome, Idade e Sexo de 4 Pessoas. No final do programa mostre:
""" A idade média do grupo - Qual é o nome do Homem mais Velho - Quantas Mulheres tem menos de 21 Anos"""

nome_lista = []
idade_lista = []
sexo_lista = []

idade_mulher = 0
homem_mais_velho_idade = 0
homem_mais_velho_nome = ''
nome_mulher = ''

print("="*50, ' LISTA DE CADASTRO ', "="*50)

for lista_cadastro in range(1, 4+1):
    nome = input(f'\nInforme o nome da {lista_cadastro}º pessoa\n')
    idade = int(input(f'\nInforme a idade da {lista_cadastro}º pessoa\n'))
    sexo = int(input(f'\nInforme o sexo da {lista_cadastro}º pessoa\n\tDigite 1 Para - Masculino\n\tDigite 2 Para - Feminino\n\t>>> '))

    if sexo == 1:
        sexo = 'masculino'
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome
    elif sexo == 2:
        if idade < 21:
            idade_mulher += 1
            nome_mulher = nome
        sexo = 'Feminino'
    else:
        print('comando inválido')
        break

    nome_lista.append(nome)
    idade_lista.append(idade)
    sexo_lista.append(sexo)

# Somando a idade média do grupo
idade_media = (sum(idade_lista) / len(idade_lista))


print(f"\nNomes dos usuários cadastrado: {nome_lista}")
print(f"\nIdades dos usuários cadastrado: {idade_lista}")
print(f"\nGeneros dos usuários cadastrado: {sexo_lista}")

print(f'\nA idade media do grupo = {idade_media}')

if nome_mulher:
    print(f'\nVerificando cadastro de mulheres com menos de 21 de idade:\n\tNomes: {nome_mulher} Totais: {idade_media}')
else:
    print(f'\nVerificando cadastro de mulheres com menos de 21 de idade:\n\tNão existe  mulher cadastrada com menos de 21 anos de idade')

if homem_mais_velho_nome:
    print(f'\nVerificando o homem mais velho do cadastro:\n\t{homem_mais_velho_nome} é o homem mais velho do cadastro com {homem_mais_velho_idade} anos de idade')
else:
    print(f'\nVerificando o homem mais velho do cadastro:\n\tNão foi possível verifica o homem mais velho poís não existe homem cadastrado')
