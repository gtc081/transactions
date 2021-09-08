# transactions

Projeto feito em Ubuntu LTS 18.04, Python 3.8.3

## Requisitos

- Instância Unix
- Python 3

## Bibliotecas

Todas as bibliotecas utilizadas são nativas do Python 3. São elas:

- sys
- json
- datetime
- unittest

## Como usar

Ao descompactar a pasta, entre nela pelo terminal. Há duas maneiras de rodar o programa:

- Passando um arquivo com os comandos, por argumento
- Sem passar arquivo

### Com arquivo

Rode o comando:
```
python transactions.py <caminho do arquivo>
```
Onde o arquivo segue uma lógica de várias strings em formato JSON, cada string JSON em uma linha diferente. Temos um exemplo abaixo, que também é o conteúdo do arquivo *operations*:

```
{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T10:00:00.000Z"}}
{"transaction": {"merchant": "Habbib's", "amount": 90, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "McDonald's", "amount": 30, "time": "2019-02-13T12:00:00.000Z"}}
```

### Sem arquivo

Também é possível rodar o programa apenas assim:
```
python transactions.py
```
Assim, é possível digitar linha por linha, no mesmo formato JSON das linhas do arquivo.

Para mostrar o status das transações já adicionadas na tela, digite *print*.

Para sair da execução e mostrar o status de todas as transações processadas, digite *exit*. 

**OBS**: o *keyboard interrupt*(Ctrl+C) **NÃO** mostrará o resultado. É necessário digitar *exit*.

## Testes

Há um arquivo de teste para a classe Main, chamado *teste_main.py*, que testa os formatos dos métodos que retornam valores inteiros. Para rodar, apenas digite no terminal:
```
python teste_main.py
```