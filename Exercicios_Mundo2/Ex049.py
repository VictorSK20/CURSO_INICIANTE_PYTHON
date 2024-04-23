# Refaça o desafio 09, mostrando a tabuada de um número que o usúario escolher, só que agora utilizando o FOR

# Função para variaveles
def color(cor, variavel):
    if cor == "blue":
        return f'\033[34m{variavel:2}\033[0m'  # Cor azul
    elif cor == "yellow":
        return f'\033[33m{variavel:2}\033[0m'  # Cor amarelo
    elif cor == "green":
        return f'\033[32m{variavel:2}\033[0m'  # Cor verde


num1 = float(input('Informe a tabuada de qual número deseja esta vizualizando: '))

for num2 in range(0, 10 + 1):
    resultado = num1 * num2
    print(f'{color("blue", num1)} * {color("yellow", num2)} = {color("green", resultado)}'.replace('.0', ''))
