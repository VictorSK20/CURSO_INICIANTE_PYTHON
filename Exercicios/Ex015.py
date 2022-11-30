km = float(input('Km percorrido: '))
dia = int(input('Dias alugado: '))
total = (km * 0.15) + (dia * 60)
print('O total a pagar pelo aluguel: R${:.2f}'.format(total))
