print('Soma entre dois numeros')

n1 = int(input('\033[1;31mDigite o Primeiro Valor{reset_verde} \n'))
n2 = int(input('\033[1;32mDigite o Segundo Valor{reset_verde} \n'))

total = n1 + n2

print(f'A soma entre \033[1;31m{n1}\033[1;m + \033[1;32m{n2}\033[1;m = ', total)
