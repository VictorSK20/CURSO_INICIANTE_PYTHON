# Crie um programa que leia um numero inteiro e mostre se ele é PAR ou IMPAR

# cores

# verde
cor1 = '\033[92m'

# amarelo
cor2 = '\033[93m'

# vermelho
cor3 = '\033[092m'

n = int(input('Informe um numero: '))

print('Escolha qual método de IF deseja utilizar\n 1 para metodo Simplificado\n 2 para metodo Padrão')

metodo = int(input('Qual metodo deseja utilizar ?\n'))

metodo_nome = ''
resultado = ''
cor = ''

if metodo == 1:
    '''             Utilizando o metodo simplificado            '''
    cor = cor1
    metodo_nome = 'Metodo Simplificado'
    resultado = 'par' if n % 2 == 0 else f'Impar'

elif metodo == 2:
    '''             Utilizando o metodo padrão            '''
    cor = cor2
    metodo_nome = 'Metodo Padrão'
    if n % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
else:
    print(f'O número escolhido {metodo} não é um número valido\nFavor digite apenas 1 para metodo simplificado ou 2 para metodo padrão')

if metodo in [1, 2]:
    print(f'{cor}O Metodo Utilizado Foi O {metodo_nome}\nO Numero {n} É {resultado}')
