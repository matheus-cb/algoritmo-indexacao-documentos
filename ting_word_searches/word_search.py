def exists_word(word, instance):
    occurrences = []

    for i in range(len(instance)):
        file_data = instance.search(i)
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]
        file_occurrences = {
            "palavra": word, "arquivo": file_name, "ocorrencias": []
        }

        for line_number, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                file_occurrences["ocorrencias"].append({"linha": line_number})

        if file_occurrences["ocorrencias"]:
            occurrences.append(file_occurrences)

    return occurrences


def search_by_word(word, instance):
    occurrences = []

    for i in range(len(instance)):
        file_data = instance.search(i)
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]
        file_occurrences = {
            "palavra": word, "arquivo": file_name, "ocorrencias": []
        }

        for line_number, line_content in enumerate(lines, start=1):
            if word.lower() in line_content.lower():
                occurrence = {"linha": line_number, "conteudo": line_content}
                file_occurrences["ocorrencias"].append(occurrence)

        if file_occurrences["ocorrencias"]:
            occurrences.append(file_occurrences)

    return occurrences
