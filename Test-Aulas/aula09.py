frase = 'Curso em Vídeo Python'

# Transformando toda a String em minusculo com lower
print(frase.lower())

# Transformando toda a String em maiúsculo com upper
print(frase.upper())

# Deixando apenas a primeira letra de toda a String em maiúsculo com capitalize
print(frase.capitalize())

# Deixando a primeira letra de cada String em maiúsculo com title
print(frase.title())

# conta o tamanho da String com len
print(len(frase))

# fazendo a separação de uma String em substrings com split
print(frase.split())

# fazendo as junções de cada substrings com join
'frase = frase.split()'
print('*'.join(frase))

# Removendo o espaço inicial e final de uma String com strip
frase_espaco = '   Aulas de Python   '
print(frase_espaco.split())

# Alterando uma String com replace
print(frase.replace('Python', 'Android'))

# Fatiamento de Strings
print(frase[15:])  # Fatiamento da posição 15 das Strings até o final
print(frase[:6])  # Fatiamento da posição inicial da String até a posição 6
print(frase[::2])  # Fatiamento da posição inicial até a posição final, pulando de 2 em 2
print(frase[0:21:1])  # Fatiamento da posição 0 até a posição 21, pulando de 1 em 1

