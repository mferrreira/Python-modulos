# os.listdir para navegar em caminhos

import os

caminho = "/home/marcio/Área de Trabalho/Projects"

for pasta in os.listdir(caminho):
    print(pasta)
    if os.path.isdir(os.path.join(caminho, pasta)):
        new_path = os.path.join(caminho, pasta)
        for item in os.listdir(new_path):
            print("     ", item)
