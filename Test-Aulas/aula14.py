# Estrutura de repetição lógica em while

# Indo de 1 até 10
'''n = 1
while n <= 10:
    print(n)
    n += 1

print('fim')
'''

# Criando uma flag com while
'''n = 1
while n != 0:
    n = int(input('Digite um número: '))'''

# Criando uma while com condições de parada
'''n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar ? [N/S] ')).upper()  # Enquanto r for igual a S o Loop não ira finalizar
'''

# Utilizando o while para encontrar a quantidade de números pares e impares digitado abaixo
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Quantidade de números pares = {par}\nQuantidade de números impares = {impar}')
