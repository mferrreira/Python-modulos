# csv.reader e csv.DictReader

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula180.csv"

lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereço": "Av 1, 22"},
    {"Nome": "João Silva", "Endereço": 'R. 2, "1"'},
    {"Nome": "Maria Sol", "Endereço": "Av B, 3A"},
]

with open(CAMINHO_CSV, "w") as arquivo:
    colunas = lista_clientes[0].keys()  # pega as chaves do dicionário
    escritor = csv.DictWriter(arquivo, colunas)

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
