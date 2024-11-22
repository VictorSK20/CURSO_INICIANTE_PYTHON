# Crie um programa onde o usúario digite uma expressão qualquer que use Parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem Correta.

lista = []

frase = str(input('Digite uma expresão: '))

for caracteres in frase:
    if '(' in caracteres:
        lista.append('(')
    elif ')' in caracteres:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão esta correta')

else:
    print('Sua expressão esta errada')
