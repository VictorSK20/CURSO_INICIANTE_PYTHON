print('Calculo da quantidade de tinta para uma parede')
print(' ')

altura_prd = float(input('Informe a altura da parede em metros: '))
largura_prd = float(input('Informe a largura da parede em metros: '))
area = altura_prd * largura_prd
tinta = area/2
print('')
print('Sua parede é {}x{} e sua area é de {}m²\nA quantidade de tinta necessaria para pinta a parede é de: {:.1f}L'.format(largura_prd, altura_prd, area, tinta))

