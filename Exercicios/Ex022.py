"""Crie um programa que Leia o nome completo de uma pessoa e execute os seguintes comandos:
    Transforme todos os caracter para MAIUSCULO, MENUSCULO, QUANTAS LETRAS TEM(SEM CONTA OS ESPAÇOS)
E QUANTAS LETRAS TEM O PRIMEIRO NOME """

# cor azul escuro
cor1 = '\033[38;5;27m'

#cor roxo azul
cor2 = '\033[38;5;63m'

#cor roxo claro
cor3 = '\033[38;5;105m'

#cor rosa claro
cor4 = '\033[38;5;147m'

#cor azul verde
cor5 = '\033[38;5;30m'

nome = str(input(f"{cor1}Digite seu nome:\n").strip())

PrimeiroNome = nome.split()

# Para maiusculo
print(f'{cor2}seu nome em maiusculo é :{nome.upper()}')

# Para minusculo
print(f'{cor3}Seu nome em minusculo é :{nome.lower()}')

# Conta letras ignorando os espaços
caracteres = (len(nome.replace(' ', '')))
print(f'{cor4}Quantidade de caracteres igual a: {caracteres}')

# Conta quantas letra tem o primeiro nome
print(f'{cor5}O seu primeiro nome é {(PrimeiroNome[0])} e ele tem {len(PrimeiroNome[0])} letras')
