# Crie um programa que leia Vários Números inteiros pelo teclado.
# No final da execução, mostre a Média entre todos os valores e qual foi o Maior e o Menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não Continuar a digitar valores

flag = 'S'

media = 0
num_digitados = 0
total_num = 0
maior = 0
menor = 0

while flag == 'S':
    if flag == 'S':
        n = int(input('Digite um número: '))
        total_num += n
        num_digitados += 1

        if num_digitados == 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        flag = str(input('Deseja continuar S/N?\n')).upper()

        while flag != 'S' and flag != 'N':
            flag = str(input('Favor informe somente S para sim ou N para não\n')).upper()
            total_num += n
            num_digitados += 1

if flag == 'N':
    media = total_num / num_digitados
    print(f'A media entres os números digitados são = {media}')
    print(f'O maior número digitado = {maior}')
    print(f'O menor número digitado = {menor}')
    print('Programa finalizado')
