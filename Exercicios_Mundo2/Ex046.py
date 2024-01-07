# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro dos fogos de artifícios
# Indo de 10 até 0, com uma pausa de 1 SEGUNDO entre elas

from time import sleep
from emoji import emojize

for contagem in range(10 , 0-1, -1):
    sleep(1)
    print(contagem)
print(emojize(':collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol:'))
