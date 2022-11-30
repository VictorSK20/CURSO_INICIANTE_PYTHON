# + = Adição                ** = Potência ou pow( )
# - = Subtração             // = Divisão Inteira
# * = Multiplicação          % = Resto da Divisão
# / = Divisão

# Ordem de Precedência
"""
1 = ()
2 = **
3 = * / // %
4 = + -
"""
#nome = input('Qual é seu nome ? ')
#print('!{:!^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
d = n1 / n2
m = n1 * n2
r = n1 % n2
di = n1 // n2
rq = (n1 + n2)**0.5
q = (n1 + n2)**2

print('Soma: {} \nMultiplicação: {} \nDivisão: {:.2f} \nResto da divisão: {} \nDivisão inteira: {}\nRaiz Quadrada: {} \nAo Quadrado: {}'.format(s, m, d, r, di, round(rq), q))
