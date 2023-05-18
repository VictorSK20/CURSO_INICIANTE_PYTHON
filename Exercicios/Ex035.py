# Crie um programa que leia o comprimento de 3 retas e informe se essas retas podem forma um triângulo ou não

# Inserido os valores das 3 retas
r1 = int(input('Informe o tamanho da reta A: '))
r2 = int(input('Informe o tamanho da reta B: '))
r3 = int(input('Informe o tamanho da reta C: '))

# Calculo para ser verdadeiro as condições de 3 retas formarem um triângulo
# Condições para r1
if (r2 - r3) < r1 < (r2 + r3):
    print(f'\nA três retas forma um triângulo. \nPois a reta A({r1}) é maior que a Reta B({r2}) - Reta C({r3}) = ({r2 - r3}) e menor que a Reta B({r2}) + Reta C({r3}) = ({r2 + r3})')

# Condições para r2
elif (r1 - r3) < r2 < (r1 + r3):
    print(f'\nA três retas forma um triângulo. \nPois a reta B({r2}) é maior que a Reta A({r1}) - Reta C({r3}) = ({r1 - r3}) e menor que a Reta A{r1} + Reta C({r3}) = ({r1 + r3})')

# Condições para r3
elif (r1 - r2) < r3 < (r1 + r2):
    print(f'\nA três retas forma um triângulo. \nPois a reta C({r3}) é maior que a Reta A({r1}) - Reta B({r2}) = ({r1 - r2}) e menor que a Reta A({r1}) + Reta B({r2}) = ({r1 + r2})')

# Condições se caso as 3 retas não formarem um triângulo
else:
    if r1 == r2 + r3 or r2 == r1 + r3 or r3 == r1 + r2:
        print(f'\nAs retas não forma um triângulo. \nPois a maior reta é igual a soma das outras duas retas')
    else:
        print(f'\nAs retas não forma um triângulo. \nPois entre as três retas a soma de duas é maior')
