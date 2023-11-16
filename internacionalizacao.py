# locale para internacionalização

# https://docs.python.org/2/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/internationalization.html

import calendar
import locale

# traduz configurações de local de acordo com o sistema operacional
locale.setlocale(locale.LC_ALL, "")

a = calendar.calendar(2023)
print(a)
