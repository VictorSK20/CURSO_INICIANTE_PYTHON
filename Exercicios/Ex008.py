print('Programa para ler Distancia em metro, centimetro e minimetros')
print('')

metro = float(input('Informe uma medida em Metro e veja sua conversão para outras medidas: '))

quilometro = metro / 1000
hectometro = metro / 100
decametro = metro / 10
decimetro = metro * 10
centimetro = metro * 100
minimetro = metro * 1000

if metro.is_integer():
    print(f'\033[1;32m{metro}\033[0mM em Km = \033[1;32m{quilometro:,}\033[0m (Quilômetro)'
          f'\n\033[1;32m{metro}\033[0mM em Hm = \033[1;32m{hectometro:,}\033[0m (Hectômetro)'
          f'\n\033[1;32m{metro}\033[0mM em Dam = \033[1;32m{decametro:,}\033[0m (Decâmetro)'
          f'\n\033[1;32m{metro}\033[0mM em Dm = \033[1;32m{decimetro:,}\033[0m (Decímetro)'
          f'\n\033[1;32m{metro}\033[0mM em Cm = \033[1;32m{centimetro:,}\033[0m (Centímetro)'
          f'\n\033[1;32m{metro}\033[0mM em Mm = \033[1;32m{minimetro:,}\033[0m (Minímetro)')

else:
    print(f'\033[1;32m{metro}\033[0mM em Km = \033[1;32m{quilometro:}\033[0m'
          f'\n\033[1;32m{metro}\033[0mM em Hm = \033[1;32m{hectometro:}'
          f'\n\033[1;32m{metro}\033[0mM em Dam = {decametro:}'
          f'\n\033[1;32m{metro}\033[0mM em Dm = {decimetro:}'
          f'\n\033[1;32m{metro}\033[0mM em Cm = {centimetro:}'
          f'\n\033[1;32m{metro}\033[0mM em Mm = {minimetro:}')
'''
def metro(fgfd.f,fgfg,fg,)


'''