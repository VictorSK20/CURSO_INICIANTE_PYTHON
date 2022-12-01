print('Programa para ler Distancia em metro, centimetro e minimetros')
print(' ')

metro = int(input('Informe uma medida em Metro e veja sua conversão para outras medidas: '))
quilometro = metro/1000
hectometro = metro/100
decametro = metro/10
decimetro = metro*10
centimetro = metro*100
minimetro = metro*1000

print('{}M em Km = {:.3f}.\n{}M em Hm = {:.2f}.\n{}M em Dam = {}.\n{}M em Dm = {}.\n{}M em Cm = {}.\n{}M em Mm {}'.format(metro, quilometro, metro, hectometro, metro, decametro, metro, decimetro, metro, centimetro, metro, minimetro))
