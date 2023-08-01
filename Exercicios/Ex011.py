print('Calculo da quantidade de tinta para uma parede: ')
print(' ')

altura_prd = float(input('Informe a altura da parede em metros: '))
largura_prd = float(input('Informe a largura da parede em metros: '))

area = altura_prd * largura_prd
tinta = area/2

print('')
print(f'Sua parede é \033[1;4;32m{largura_prd}\033[m x \033[1;4;32m{altura_prd}\033[0m e sua area é de \033[1;4;32m{area}m²\033[0m'
      f'\nA quantidade de tinta necessaria para pinta a parede é de: \033[1;4;32m{tinta:.1f}L\033[m')
