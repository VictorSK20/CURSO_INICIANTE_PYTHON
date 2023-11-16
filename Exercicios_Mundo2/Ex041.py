# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
"""
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER
"""

# função init irá utilizar o autoreset True, para reseta a cor para o padrão a cada linha
from colorama import init
init(autoreset=True)

' CORES'
# cor 1 Azul com tom verde
cor1 = '\033[38;5;50m'

# cor 2 Verde
cor2 = '\033[38;5;48m'

# cor 3 Azul
cor3 = '\033[38;5;45m'

# cor 4 Laranja
cor4 = '\033[38;5;214m'

# cor 5 Amarelo
cor5 = '\033[38;5;226m'

# cor 6 para mensagem de erro - Vermelho
cor6 = '\033[38;5;196m'

try:
    idade = int(input('Informe a idade do atleta: '))

    if idade > 0 and idade < 10:
        print(f'O atleta de {idade} esta na categoria: {cor1}Mirim')

    elif idade > 9 and idade < 15:
        print(f'O atleta de {idade} esta na categoria: {cor2}Infantil')

    elif idade > 15 and idade < 20:
        print(f'O atleta de {idade} esta na categoria: {cor3}Junior')

    elif idade == 20:
        print(f'O atleta de {idade} esta na categoria: {cor4}Sênior')

    else:
        print(f'O atleta de {idade} esta na categoria: {cor5}Master')

except ValueError:
    print(f'{cor6}Digite um valor valido !')
