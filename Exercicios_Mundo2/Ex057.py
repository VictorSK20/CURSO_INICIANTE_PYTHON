# Faça um programa que leia o Sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
# Digitação novamente até ter um valor corrreto

F = ""
M = ""
pessoa = ""
erro = int(0)

while pessoa != 'F' and pessoa != 'M':
    pessoa = str(input("Informe seu sexo [M/F] ")).strip().upper()

    if 'F' != pessoa != "M":
        print('\ninformação inválida, favor digite somente as opções abaixo')
        print('\t[M] para Masculino\n\t[F] para Feminino\n')
        erro += 1


if erro > 0:
    print(f'total de erro de digitação {erro}')
