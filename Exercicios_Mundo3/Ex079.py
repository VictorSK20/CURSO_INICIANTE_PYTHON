# Crie um programa onde o úsuario possa digitar vários Valores Númericos e cadastre-os em uma Lista.
# Caso o número já existe lá dentro, ele não será adicionado.
# No final, serão exibidos todos os Valores Únicos digitados, em ordem crescente.

valores = []
while True:
    res = ''

    valor = int(input('Informe um Valor Númerico: '))

    while valor in valores:
        print('Valor existende, Favor digite outro valor !')
        valor = int(input('Informe um Valor Númerico: '))
    else:
        print('valor adicionado com sucesso !')
        valores.append(valor)

    while res != 'N' and res != 'S':
        res = input('Você deseja continuar ? [S/N]').upper().strip()[0]

    if res == 'N':
        break

valores.sort()

print(valores)
