"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento
O programa também deverá mostrar o tempo que falta ou que passou do prazo
"""

import datetime

print('Informe sua data de nascimento: ')

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

# salvando dia, mês e ano da data de nascimento
data_nascimento = datetime.datetime(year=ano, month=mes, day=dia)

# salvando a idade do usúario utilizando o calculo da data atual menos a data de nascimento do usúario resultando no valor da idade
idade = datetime.datetime.now().year - data_nascimento.year

if idade > 18:
    print(f'Data de nascimento do jovem: {data_nascimento.strftime("%d/%m/%Y")}')
    print(f'O jovem esta atrasado a {idade - 18} anos para o alistamento !')

elif idade < 18:
    print(f'Data de nascimento do jovem {data_nascimento.strftime("%d/%m/%Y")}')
    print(f'Falta {18 - idade} anos para o jovem se alistar !')

else:
    print(f'Data de nascimento do jovem: {data_nascimento.strftime("%d/$m/%Y")}')
    print(f'O jovem deve se alista neste ano')
