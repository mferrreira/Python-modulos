"""
Usando calendar para calendários e datas
https://docs.python.org/3/library/calendar.html

Calendar é usado para coisas genéricas de calendários e datas.
Com calendar, você pode saber coisas como:

    - Qual o último dia do mês (monthrange)
    - Qual o nome e número do dia de determinada data (weekday)
    - Criar um calendário em si (monthcalendar)
    - trabalhar com coisas específicas de calendários (calendar, month)

Por padrão, dia da semana começa em 0 (seg) até 6 (dom)
"""

import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[numero_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
