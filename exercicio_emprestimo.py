# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


nome = "Maria"
emprestimo = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcela = data_emprestimo
parcelas = []

while data_parcela < data_final:
    parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

valor_parcela = emprestimo / len(parcelas)

for data in parcelas:
    print(data.strftime("%d/%m/%Y"), f"R$ {valor_parcela:,.2f}")

print(
    f"{nome} pegou um empréstimo de R$ {emprestimo:,.2f} para pagar em"
    f"{len(parcelas)} meses em parcelas de {valor_parcela:,.2f}"
)
