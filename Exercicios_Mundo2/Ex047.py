# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo  entre 1 e 50

for n in range(1, 50+1): # Criando um range de 1 até 50
    if n % 2 == 0: # Calculando o range de n dividindo por 2, se a sobra da divisão for zero, então o número é par
        print(n, end=' - ') # imprimindo o range de n, e só será exibidos valores par
