# Faça um programa que leia 5 Valores Númericos e guarde-os em uma Lista.
# No final, mostre qual foi o Maior e o Menor valor digitado e as suas respectivas Posições na lista

valores = []
pos_maior = []
pos_menor = []

for i in range(0, 5):
    valor = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

for i, valor in enumerate(valores):
    if valor == maior:
        pos_maior.append(i)
    if valor == menor:
        pos_menor.append(i)

print(f'\nO maior valor digitado foi {maior} que esta na posição {pos_maior}')

print(f'\nO menor valor digitado foi {menor} que esta na posição {pos_menor}')
