import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            if not path_file.endswith('.txt'):
                raise ValueError("Formato inválido")
            lines = [line.strip() for line in file.readlines()]
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError as e:
        print(e, file=sys.stderr)
