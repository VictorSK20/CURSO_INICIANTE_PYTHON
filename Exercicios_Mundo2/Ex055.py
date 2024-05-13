# Faça um programa que leia o Peso de Cinco Pessoas. No final, mostre qual foi o Maior e o Menor pesos lidos

lista_peso = []  # Criando uma lista para armazenar a variavel peso

for a in range(1, 5+1):
    peso = float(input('Informe seu peso: '))
    lista_peso.append(peso)  # salvando as informações da var peso dentro de lista_peso[]

peso_maximo = max(lista_peso)  # retornando o valor maximo
peso_minimo = min(lista_peso)  # retornando o valor mínimo

print(f'peso menor = {peso_minimo}')
print(f'peso maior = {peso_maximo}')
