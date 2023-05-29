print('Mostra N antecessor e Sucessor ao N atual')
print(' ')

n = int(input('Informe um valor: \n'))
print('Seu antecessor é \033[1;31m{}\033[0m e seu sucessor é \033[1;32m{}\033[0m'.format(n-1, n+1))
