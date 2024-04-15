# Document Indexing Algorithm

## Descrição 
Este projeto simula um algoritmo de indexação de documentos similar ao utilizado pelo Google, focando na identificação de ocorrências de termos em arquivos de texto (.TXT). O sistema é dividido em dois módulos principais: gerenciamento de arquivos e busca.

## Módulos
### Gerenciamento de Arquivos
Permite ao usuário anexar arquivos de texto ao sistema, preparando-os para a indexação e a busca subsequente.
### Busca
Permite realizar buscas eficientes pelos termos desejados nos documentos indexados, utilizando estruturas de dados avançados para otimizar as operações.

## Habilidades Desenvolvidas
 - Manipulação de Pilhas
 - Manipulação de Deques
 - Manipulação de Nós e Listas Ligadas
 - Manipulação de Listas Duplamente Ligadas

## Estrutura do Projeto
<details>
<summary>O projetos está organizado conforme mostrado abaixo:</summary>
  
```
.
├──🔹dev-requirements.txt
├──🔹pyproject.toml
├──🔹README.md
├──🔹requirements.txt
├──🔹setup.cfg
├──🔹setup.py
├──statics
│   ├──🔹arquivo_teste.csv
│   ├──🔹arquivo_teste.txt
│   ├──🔹nome_pedro.txt
│   ├──🔹novo_paradigma_globalizado-min.txt
│   └──🔹novo_paradigma_globalizado.txt
├──tests
│   ├──🔹__init__.py
│   ├──🔹test_file_management.py
│   ├──🔹test_file_process.py
│   ├──🔹test_queue.py
│   └──🔹test_word_search.py
├──ting_file_management
│   ├──🔹file_management.py
│   ├──🔹file_process.py
│   ├──🔹__init__.py
│   └──🔹queue.py
├──ting_word_searches
│   ├──🔹__init__.py
│   └──🔹word_search.py
└──🔹trybe.yml
``` 
</details>

## Como usar
### Configuração Inicial
<details>
  <summary><strong>Ambiente Virtual</strong>strong></summary>
  
O Python oferece um recurso chamado ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas. Para utilizar este recurso siga os passos a passos:
  1. criar o ambiente virtual
```
$ python3 -m venv .venv
```
 2. ativar o ambiente virtual
```
$ source .venv/bin/activate
```
  3. instalar as dependências no ambiente virtual
```
$ python3 -m pip install -r dev-requirements.txt
```
Com o seu ambiente virtual ativo as dependências serão instaladas neste ambiente.
</details>

### Testes
<details>
  <summary><strong>🛠 Testes</strong></summary><br />

 👀 **Para executar os testes certifique-se de que você está com o ambiente virtual ativado.**

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```
</details>



`Desenvolvido durante o curso de desenvolvimento web da Trybe`
