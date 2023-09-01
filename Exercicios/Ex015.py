km = float(input('Km percorrido: '))
dia = int(input('Dias alugado: '))

total = (km * 0.15) + (dia * 60)

# criando a variavel para troca a cor das letras
cor = '\033[1;92m'
reset_cor = '\033[m'

print(f'O total a pagar pelo aluguel: {cor}R${total:.2f}{reset_cor}')
