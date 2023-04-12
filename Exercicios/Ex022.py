"""Crie um programa que Leia o nome completo de uma pessoa e execute os seguintes comandos:
    Transforme todos os caracter para MAIUSCULO, MENUSCULO, QUANTAS LETRAS TEM(SEM CONTA OS ESPAÇOS)
E QUANTAS LETRAS TEM O PRIMEIRO NOME """

nome = str(input("Digite seu nome:\n").strip())

PrimeiroNome = nome.split()

# Para maiusculo
print(f'seu nome em maiusculo é :{nome.upper()}')

# Para minusculo
print(f'Seu nome em minusculo é :{nome.lower()}')

# Conta letras ignorando os espaços
caracteres = (len(nome.replace(' ', '')))
print(f'Quantidade de caracteres igual a: {caracteres}')

# Conta quantas letra tem o primeiro nome
print(f'O seu primeiro nome é {(PrimeiroNome[0])} e ele tem {len(PrimeiroNome[0])} letras')
