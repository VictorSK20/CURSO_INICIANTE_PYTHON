print('Conversor de temperatura')
print(' ')

# armazenando a cor na variavel c e resetando essa cor na variavel r
c = "\033[1;94m"
r = "\033[m"

celsius = int(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura de {c}°C{celsius}{r} em = {c}°F{fahrenheit:.0f}{r}')
