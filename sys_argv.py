# sys.arv - Executando arquivos com argumentos no sistema

# import sys

# argumentos = sys.argv
# qts_argumentos = len(argumentos)

# if qts_argumentos <= 1:
#     print('Não passou argumentos')
# else:
#     try:
#         for i in range(qts_argumentos):
#             print(f'Faça alguma coisa com {argumentos[i]}')
#     except IndexError:
#         print('Faltam Argumentos')

# ========================================================================

# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)