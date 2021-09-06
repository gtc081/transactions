# transactions

Projeto feito em Ubuntu LTS 18.04, Python 3.8.3

## Requisitos

- Instância Unix
- Python 3

## Como usar

Ao descompactar a pasta, entre nela pelo terminal. Há duas maneiras de rodar o programa:

- Passando um arquivo com os comandos, por argumento
- Sem passar arquivo

### Com arquivo

Rode o comando:
```
python transactions.py <caminho do arquivo>
```
Onde o arquivo segue uma lógica de várias strings em formato JSON, cada string JSON em uma linha diferente. Temos um exemplo abaixo, que é o conteúdo do arquivo *operations*:

```
{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T10:00:00.000Z"}}
{"transaction": {"merchant": "Habbib's", "amount": 90, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "McDonald's", "amount": 30, "time": "2019-02-13T12:00:00.000Z"}}
```

### Sem arquivo

Também é possível rodar o progrma apenas assim:
```
python transactions.py
```
Assim, é possível digitar linha por linha, no mesmo formato JSON das linhas do arquivo
