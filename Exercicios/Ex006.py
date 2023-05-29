print('\033[1;7;37mMostra o Doblo, Triplo e Raiz Quadrada do valor\033[0m\n')
print('')
n = int(input('Informe o Valor: \n'))
print('\033[1mDoblo = \033[1;33m{}\033[0m \n\033[1mTriplo = \033[1;34m{}\033[0m \n\033[1mRaiz Quadrada = \033[1;35m{}\033[0m '.format(n*2, n*3, round(pow(n, 0.5))))
