# Crie um programa que leia o comprimento de 3 retas e informe se essas retas podem forma um triângulo ou não

r1 = int(input('Informe o tamanho da reta A: '))
r2 = int(input('Informe o tamanho da reta B: '))
r3 = int(input('Informe o tamanho da reta C: '))

if (r2 - r3) < r1 < (r2 + r3) != 0:
    print(f'A três retas forma um triângulo. \n Pois a reta A({r1}) é maior que a Reta B({r2}) - Reta C({r3}) e menor que a Reta B({r2}) + Reta C({r3})')

elif (r1 - r3) < r2 < (r1 + r3) != 0:
    print(f'A três retas forma um triângulo. \n Pois a reta B({r2}) é maior que a Reta A({r1}) - Reta C({r3}) e menor que a Reta A{r1} + Reta C({r3})')

elif (r1 - r2) < r3 < (r1 + r2) != 0:
    print(f'A três retas forma um triângulo. \n Pois a reta C({r3}) é maior que a Reta A({r1}) - Reta B({r2}) e menor que a Reta A({r1}) + Reta B({r2})')

else:
    if r1 == r2 + r3 or r2 == r1 + r3 or r3 == r1 + r2:
        print(f'As retas não forma um triângulo. \n Pois a maior reta é igual a soma das outras duas retas')
    else:
        print(f'As retas não forma um triângulo. \n Pois entre as três retas a soma de duas é maior')
