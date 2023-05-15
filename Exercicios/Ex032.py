# Crie um programa que leia um ano e informe se é Bissexto ou não

# Adicionando uma informação na variavel ano
ano = (input('Informe um ano e descubra se ele é Bissexto ou não: '))

# nessa parte o programa verificara se a variavel ano tem o tamanho diferente de 4 caracteres, se caso sim, o programa vai retorna uma mensagem de aviso
if len(ano) != 4:
    print('Favor digitar um ano válido com 4 digitos númericos')

# Verificando se a variavel ano começa com 0, se caso sim, o programa vai retorna outro aviso
elif ano[0] == '0':
    print('Favor evite usa o digito zero na frente do ano')

# O programa vai executar o calculo para verifica se a variavel ano é bissexto ou não e imprimir a mensagem na tela
else:
    ano = int(ano)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano de {ano} é BISSEXTO')
    else:
        print(f'O ano de {ano} não é BISSEXTO')
