# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro dos fogos de artifícios
# Indo de 10 até 0, com uma pausa de 1 SEGUNDO entre elas

from time import sleep
from emoji import emojize

for contagem in range(10, 0-1, -1):  # Criando range de 10 até 0
    sleep(1)  # A cada numero do range contagem for exibido, o programa ira aguarda 1 segundo para exibir o próximo número
    print(contagem)
print(emojize(':collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol::collision::anger_symbol:'))
