print('Programa para ler Distancia em metro, centimetro e minimetros')
print('')

metro = int(input('Informe uma medida em Metro e veja sua conversão para outras medidas: '))

quilometro = metro/1000
hectometro = metro/100
decametro = metro/10
decimetro = metro*10
centimetro = metro*100
minimetro = metro*1000

print(f'\033[1;32m{metro}M\033[0;1m em \033[1;33mKm = {quilometro:,}\033[0m.\n'
      f'\033[1;32m{metro}M\033[0;1m em \033[1;33mHm = {hectometro:,}\033[0m.\n'
      f'\033[1;32m{metro}M\033[0;1m em \033[1;33mDam = {decametro:,}\033[0m.\n'
      f'\033[1;32m{metro}M\033[0;1m em \033[1;33mDm = {decimetro:,}\033[0m.\n'
      f'\033[1;32m{metro}M\033[0;1m em \033[1;33mCm = {centimetro:,}\033[0m.\n'
      f'\033[1;32m{metro}M\033[0;1m em \033[1;33mMm {minimetro:,}\033[0m')
