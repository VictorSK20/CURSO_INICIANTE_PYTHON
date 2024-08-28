# Melhore o Desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 Termos

termo = int(input('Informe quantos termos deseja vizualizar: '))
a1 = int(input('Informe o primeiro termo: '))

r = int(input('Informe a razão: '))

for i in range(1, termo + 1):
    print(f'{i:2}º Termo = {(a1 + (i - 1) * r):2}')

continuar_termos = termo

while continuar_termos != 0:
    continuar_termos = int(input('Quantos termos à mais desejar ver?\nDigite 0 para encerar o processo: '))

    for j in range(i, continuar_termos + i):
        print(f'{1 + j:2}º termo =  {(a1 + j * r):2}')

    # atualizando o valor de i para o próximo laço
    i += continuar_termos

print('Fim da operação')
