import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            print(
               f"Arquivo {path_file} já processado. Ignorando...",
               file=sys.stdout
            )
            return
    lines = txt_importer(path_file)
    file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
    }
    instance.enqueue(file_data)
    print(file_data, file=sys.stdout)


def remove(instance):
    try:
        removed_file = instance.dequeue()
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout
        )
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
