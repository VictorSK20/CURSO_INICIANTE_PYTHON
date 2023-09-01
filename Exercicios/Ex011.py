print('Calculo da quantidade de tinta para uma parede: ')
print(' ')

altura_prd = float(input('Informe a altura da parede em metros: '))
largura_prd = float(input('Informe a largura da parede em metros: '))

area = altura_prd * largura_prd
tinta = area/2

cor_verde = "\033[1;4;32m"
reset_verde = "\033[m"


print('')
print(f'Sua parede é {cor_verde}{largura_prd}{reset_verde} x {cor_verde}{altura_prd}{reset_verde} e sua area é de {cor_verde}{area}m²{reset_verde}'
      f'\nA quantidade de tinta necessaria para pinta a parede é de: {cor_verde}{tinta:.1f}L{reset_verde}')
