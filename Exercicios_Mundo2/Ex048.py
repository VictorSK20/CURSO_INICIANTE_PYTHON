# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES
# Que sejam MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500

soma = 0  # Esta varíavel será responsavél para soma o range abaixo
contador = 0  # Esta varíavel sera responsavél para conta quantos valores que será imprimido no range abaixo

for contagem in range(1, 500+1):
    if contagem % 3 == 0:  # Calculando os multipros de 3
        if contagem % 2 == 1:  # Calculo para imprimir somentes os impares
            soma += contagem
            contador += 1
            print(contagem, end=', ')


print(f'\n\nA soma entre os números impares de 1 até 500 sendo multipros de 3 é = {soma}')
print(f'A quantidade de valores encontrados foram {contador}')
