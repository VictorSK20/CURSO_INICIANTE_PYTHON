import time
import tkinter
import calendar
from datetime import date, datetime

data_completa = time.localtime()
calendario = calendar.calendar(data_completa[0])

print(calendario)

print('=' * 100)

data_atual = date.today()
hora_atual = datetime.now()
print(f'Data atual: {data_atual}')

print(f'hora atual: {hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}')
