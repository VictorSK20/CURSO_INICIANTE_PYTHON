# Crie um programa que tenha uma Tupla com Várias Palavras (Não usar acértos)
# Depois disso você deve mostrar, para cada palavra, quais são suas Vorgais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO',)

vogal = "AEIOU"

for p in palavras:
    print(f'\nNa palavra {p} Temos as vogais', end=' ')
    for v in p:
        if v in vogal:
            print(f'{v}', end='')
