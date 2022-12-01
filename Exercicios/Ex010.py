print('Valor do real para o dolar')
print(' ')

real = float(input('informe seu valor em real: '))
dolar = real/5.18
euro = real/5.18
print('R${:.2f} em Dolar = US${:.2f}'.format(real, dolar))
print(f'R${real:.2f} em Euro = €{euro:.2f}')
