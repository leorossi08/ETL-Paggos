# ETL Project

## Visão Geral

Este projeto implementa um pipeline ETL simples que integra dois bancos de dados PostgreSQL, uma API construída com FastAPI e um script de ETL.
A aplicação consiste em:

- Banco Fonte: Armazena dados brutos, que inicialmente estarão vazios. Após o Docker estar em execução, você deve popular esse banco ativando o script populate_data.py.
- API: Expondo um endpoint /data para consultar os dados brutos do banco fonte e outro endpoint /signal para consultar os dados transformados (agregados) que o ETL processa.
- Processo ETL: Extrai os dados do endpoint /data via httpx, transforma-os utilizando pandas (reagrupar os dados em janelas de 10 minutos e calcular estatísticas como média, mínimo, máximo e desvio padrão) e carrega os resultados na tabela “signal” do banco destino.

Após popular o banco fonte e reiniciar o Docker (para que os dados estejam disponíveis no banco source), os endpoints funcionam conforme abaixo:
- Acessando o link:
  http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power,ambient_temperature
  Você visualizará o JSON com os dados brutos do banco de dados source.
- Já para o banco de destino, acesse:
  http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
  Neste endpoint, serão apresentados os dados transformados (agregados) pelo ETL.



## Como Usar

### Execução com Docker

1. Inicialmente, o banco de dados fonte estará vazio. Com o Docker rodando, você deve popular esse banco ativando o script populate_data.py (este script deve ser executado separadamente para inserir os dados brutos no source_db).
2. Após a população, reinicie o Docker para que os dados fiquem disponíveis no banco fonte.



### Consultando os Endpoints

- **Dados Brutos (Banco Fonte):**  
  Acesse o endpoint /data para visualizar os registros brutos:
  
  http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power,ambient_temperature
  
- **Dados Agregados (Banco Destino):**  
  Após a execução do ETL, acesse o endpoint /signal para visualizar os dados transformados:
  
  http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
  


## Resumo

- Visão Geral: Projeto ETL com dois bancos de dados, uma API para exposição de dados e um processo ETL que extrai, transforma e carrega os dados.
- Estrutura do Projeto: Organizado em módulos para a API, bancos de dados, ETL e scripts de utilidade.
- Pré-requisitos: Docker, Docker Compose e, opcionalmente, Python 3.9+ com as dependências.
- Como Usar: 
   1. Inicialmente, use `docker-compose build` para criar o docker e, após isso, faça um `docker-compose up` e ative o script populate_data.py para popular o banco fonte.
   2. Reinicie o Docker, dando Control-C e rodando novamente `docker-compose up`
   3. Acesse os endpoints:
      - Dados do banco fonte: http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power,ambient_temperature
      - Dados do banco destino (transformados): http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
