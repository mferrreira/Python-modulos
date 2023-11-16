# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretório de
# maneira resursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs) e
# uma lista dos arquivos do diretório atual (files)

import os
from itertools import count

caminho = os.path.join("/home", "marcio", "Documentos")
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, "pasta atual", root)

    for dir_ in dirs:
        print("  ", the_counter, "dir", dir_)

    # EXCLUI ARQUIVOS DA PASTA:
    # os.unlink()
