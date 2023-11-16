# os.path trabalha com caminhos em widnows, Linux e Mac
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas
#
# Exemplo do os.path:
#
# os.path.join: junta strings em  um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta\2\arquivo.txt' no Windows.
#
# os.path.split: divide um caminho em uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt') retornaria
# ('/home/user', 'arquivo.txt').
#
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída com arquivos

import os

caminho = os.path.join("documentos", "curso", "arquivo.txt")
print(caminho)

diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)

print(diretorio, arquivo)
print(caminho_arquivo, extensao_arquivo)

print(os.path.exists(caminho))

print(os.path.abspath("."))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
