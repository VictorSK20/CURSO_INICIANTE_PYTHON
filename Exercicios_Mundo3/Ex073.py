# Crie uma TUPLA preenchida com os 20 Primeiros colocados da tabela do Campeonato Brasileiro de Futebol
# Na ordem de colocação. Depois mostre:
"""
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados na tabela
C) Uma lista com os times em ordem alfabética
D) Em que Posição na tabela está o time da Chapecoense
"""
from colorama import init

init(autoreset=True)

green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
lemon = '\033[38;5;46m'
negrito = '\033[1m'
reset = '\033[m'

times = ('Santos', 'Novorizontino', 'Sport', 'Mirassol', 'Vila Nova', 'Ceará',
         'América-MG', 'Coritiba', 'Avaí', 'Operário PR', 'Amazonas', 'Goiás',
         'Chapecoense', 'Paysandu', 'Ponte Preta', 'Botafogo-SP', 'Brusque', 'Ituano', 'CRB', 'Guarani')

cinco_primeiros = times[0:5]
rebaixados = times[16:]
ordem_alfabetica = sorted(times)
chapecoense = times.index('Chapecoense') + 1

print('-='*125)
print(f'{negrito}Lista dos times do brasileirão{reset}\n{times}')
print('-='*125)

print(f'{negrito}Os primeiros 5 colocados na tabela{reset}\n{green}{cinco_primeiros}')
print('-='*125)

print(f'{negrito}Os times na zona vermelha{reset}\n{red}{rebaixados}')
print('-='*125)

print(f'{negrito}Os times em ordem alfabética{reset}\n{blue}{ordem_alfabetica}')
print('-='*125)

print(f'{lemon}O time da Chapecoense esta na {chapecoense}ª posição')
print('-='*125)
