# Crie um programa que leia a Idade eo Sexo de várias Pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# Se o Usuário quer ou não continuar. No final, Mostre:
# A) Quantas pessoas tem mais de 18 Anos
# B) Quantos Homens foram cadastrados.
# C) Quantas Mulheres tem menos de 20 Anos

idade = maior_idade = homens = mulheres_menor_20 = 0
sexo = continuar = ''

while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    # Loop para idade
    while True:
        try:
            idade = int(input('Idade: '))
            if idade >= 18:
                maior_idade += 1  # Se variavel idade receber maior ou igual a 18 a variavel maior_idade recebe +1
            break
        except ValueError:
            print(end='')

    # Loop para sexo
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[:1]
        if sexo == 'M':
            homens += 1  # Se sexo for homem a variavel homens recebe +1
        if sexo in ['M', 'F']:
            break

    # se a variavel idade for menor que 20 e o sexo for mulher a variavel mulheres_menor_20 vai receber +1
    if idade < 20:
        if sexo == 'F':
            mulheres_menor_20 += 1

    # Loop para interroper o código ou continuar
    while True:
        print('-' * 30)
        continuar = str(input(f'{"Quer continuar? [S/N]":^25}')).upper().strip()[:1]
        if continuar in ['S', 'N']:
            break

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'E ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menor_20} mulheres com menos de 20 anos')
