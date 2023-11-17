# Refaça p DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
"""
EQUILÁTERO: Todos os lados iguais
ISÓSCELES: Dois lados iguais
ESCALENO: Todos os lados diferentes
"""


# Função para adiciona cores ao codigo
def color(cor):
    if r1:
        return '\033[93m'
    elif r2:
        return '\033[94m'
    elif r3:
        return '\033[95m'
    else:
        return '\033[0m'


try:
    # Inserido os valores das 3 retas
    r1 = int(input(f'Informe o tamanho da reta A: '))
    r2 = int(input(f'Informe o tamanho da reta B: '))
    r3 = int(input(f'Informe o tamanho da reta C: '))

    if r1 == r2 and r1 == r3 and r2 == r3:
        print('\nO Triângulo é do tipo Equilátero\nTodos os lados são iguais')
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 != r1):
        print('\nO triângulo é do tipo Isóceles\nPossui dois lados iguais')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('\nO triângulo é do tipo Escaleno\nNão possui nenhum lado igual')

    # Calculo para ser verdadeiro as condições de 3 retas formarem um triângulo
    if r1 > 0 and r2 > 0 and r3 > 0:
        if r1 < (r2 + r3) or r2 < (r1 + r3) or r3 < (r1 + r2):
            print(f'\n{color(r1)}As três retas formam um triângulo. '
                  f'Pois a soma de qualquer lado é maior que o terceiro lado')

        # Condições se caso as 3 retas não formarem um triângulo
        else:
            if r1 == r2 + r3 or r2 == r1 + r3 or r3 == r1 + r2:
                print(f'\nAs retas não forma um triângulo. '
                      f'\nPois a maior reta é igual a soma das outras duas retas')
            else:
                print(f'\nAs retas não forma um triângulo. '
                      f'\nPois entre as três retas a soma de duas é maior')
    else:
        print('Favor digite um valor positivo')

except ValueError:
    print(f'\033[91mDigite um valor válido\033[m')
