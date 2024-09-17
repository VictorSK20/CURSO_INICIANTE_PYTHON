# Crie um programa que leia Vários Números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a Condição de Parada.
# No final, mostre Quantos Números foram digitados e qual foi a Soma entre eles
# Desconsiderando o flag

count = soma = 0

while True:
    n = int(input('Digite um número [Digite 999 para finalizar]\n'))
    if n == 999:
        break
    count += 1
    soma += n

print(f'A quantidade de números digitados foram = {count}\nA soma entre eles = {soma}')
