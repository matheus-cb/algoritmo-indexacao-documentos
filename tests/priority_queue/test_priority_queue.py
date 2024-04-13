import pytest
from ting_file_management.priority_queue import PriorityQueue

# AAA (Arrange, Act, Assert)


# Cria instâncias de arquivos e os adiciona na fila
def create_file_instances_and_enqueue(list, queue):
    for i in range(len(list)):
        item = {
            "nome_do_arquivo": f"arquivo_{i}.txt",
            "qtd_linhas": list[i],
            "linhas_do_arquivo": ["linhas do arquivo"],
        }
        queue.enqueue(item)


# Verifica a ordem dos elementos na fila
def check_queue_order(queue):
    size_list_order = []
    for index in range(len(queue)):
        size_list_order.append(queue.search(index)["qtd_linhas"])
    return size_list_order


def test_basic_priority_queueing():
    # Testa a inserção de elementos na fila de prioridade

    # Arrange

    priority_queue = PriorityQueue()
    # Lista de elementos a serem adicionados
    entrys = [9, 4, 2, 5, 7, 11, 3]

    # Act

    create_file_instances_and_enqueue(entrys, priority_queue)

    # Asserts

    new_list_order = check_queue_order(priority_queue)
    # Verifica se a ordem está correta
    assert new_list_order == [4, 2, 3, 9, 5, 7, 11]
    # Verifica se a ordem está correta
    assert new_list_order != entrys

    priority_queue.dequeue()
    # Verifica a ordem dos elementos na fila
    assert check_queue_order(priority_queue) == [2, 3, 9, 5, 7, 11]
    # Verifica o tamanho da fila
    assert len(priority_queue) == 6

    priority_queue.dequeue()
    # Verifica a ordem dos elementos na fila
    assert check_queue_order(priority_queue) == [3, 9, 5, 7, 11]
    # Verifica o tamanho da fila
    assert len(priority_queue) == 5

    # Testa a busca de elementos inválidos
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(10)
