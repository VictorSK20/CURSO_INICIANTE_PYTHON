# Faça um programa que mostre a Tabuada de Vários Números, um de cada vez.
# Para cada valor digitado pelo usúario. O programa será interrompido quando o número solicitado for Negativo

while True:
    n2 = 1
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    if n1 < 0:
        print('-'*30)
        print('Programa encerrado. Volte Sempre !!!')
        print('-'*30)
        break

    print('-'*30)
    while n2 < 11:
        print(f'{n1} x {n2:2} = {n1*n2}')
        n2 += 1
    print('-'*30)
