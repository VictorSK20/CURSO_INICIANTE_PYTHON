# Melhore o Desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 Termos

termo = 1

while termo != 0:
    termo = int(input('Informe quantos termos quer mostrar\nUse o dígito 0 para finalizar\n'))
    if termo == 0:
        print('Finalizando Operação')
        break

    a1 = int(input('Informe o primero termo: '))
    r = int(input('Informe a razão: '))
    n = termo

    for i in range(1, n + 1):
        print(f'{i:2}º Termo - {(a1 + (i - 1) * r):2}')
