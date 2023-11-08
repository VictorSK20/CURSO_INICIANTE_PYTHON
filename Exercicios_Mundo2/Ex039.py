
"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento
O programa também deverá mostrar o tempo que falta ou que passou do prazo"""

import datetime

print('Informe sua data de nascimento: ')

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

data_nascimento = datetime.date(year=ano, month=mes, day=dia)


# ano_nascimento = int(input('Infome sua data de nascimento'))
