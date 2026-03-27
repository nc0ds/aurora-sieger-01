# Aurora Sieger - Atividade 1

## Pré-requisitos

- Python 3.x

## Como executar

Execute os seguintes comandos:

1. `python3 data_generator.py` para gerar os dados de telemetria
   - O script gerador de dados recebe uma flag opcional `-l` ou `--lines` que determina a quantidade de linhas que devem ser geradas. O valor padrão é `100`.
2. Em seguida, execute `python3 main.py` para executar o algoritmo de verificação de decolagem

## Resultado esperado

Ao executar o algoritmo de verificação, há duas possibilidades previstas:

- Resultado positivo: "PRONTO PARA DECOLAR"
- Resultado negativo: "DECOLAGEM ABORTADA"

Para o resultado positivo acontecer, é necessário que a média dos valores de telemetria gerados anteriormente estejam de acordo com os valores mínimos e máximos determinados no algoritmo, possibilitando então a decolagem.

Por outro lado, para o resultado negativo acontecer, basta qualquer valor médio estar fora do esperado que automaticamente a validação termina, previnindo a decolagem.
