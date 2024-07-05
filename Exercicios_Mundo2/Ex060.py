# Faça um programa que leia um Número qualquer e mostre o seu Fatorial

n = int(input('Informe um número e descubra seu fatorial: '))

fatorial = n
resultado = 1

print(f'{n}! = ', end='')

while fatorial > 0:
    resultado *= fatorial
    if fatorial > 1:
        print(f'{fatorial} x ', end='')
    else:
        print(f'{fatorial} = ', end='')
    fatorial -= 1

print(resultado)
