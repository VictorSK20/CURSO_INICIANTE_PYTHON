# Faça um programa que leia um Número qualquer e mostre o seu Fatorial

n = int(input('Informe um número e descubra seu fatorial: '))

fatorial = n
resultado = 1

escolhar = int(input('Ecolhar 1 para executar o código em while\nEscolhar 2 para executar o código em for: \n\t\t'))

if escolhar == 1:
    print(f'{n}! = ', end='')

    while fatorial > 0:
        resultado *= fatorial
        if fatorial > 1:
            print(f'{fatorial} x ', end='')
        else:
            print(f'{fatorial} = ', end='')
        fatorial -= 1

elif escolhar == 2:
    print(f'{n}! = ', end='')
    for i in range(fatorial, 1 - 1, -1):
        if fatorial > 1:
            print(fatorial, end=' X ')
        else:
            print(fatorial, end=' = ')
        resultado *= fatorial
        fatorial -= 1

print(f'{resultado:,}'.replace(',', '.'))
