# comando break e while True

# While True = comando sem condições de parada
# break= interroper o código e finalizar o comando While mesmo sem condições de parada

soma = count = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    count += 1

print(f'Quantidade de números digitados = {count}\nSoma entre os números é = {soma}')


# testando o format do Python 3.6+ - Python 3 - Python 2

Nome = 'Victor'
Idade = 28
Salario = 2000

print(f'O funcionario {Nome} tem {Idade} e recebe {Salario}')  # Python 3.6+
print('O funcionario {} tem {} e recebe {}'.format(Nome, Idade, Salario))  # Python 3
print('O funcionario %s tem %d e recebe %d' % (Nome, Idade, Salario))  # Python 2
