# ETL Project

## Visão Geral

Este projeto implementa um pipeline ETL simples que integra dois bancos de dados PostgreSQL, uma API construída com FastAPI e um script de ETL.
A aplicação consiste em:

- Banco Fonte: Armazena dados brutos, que inicialmente estarão vazios. Após o Docker estar em execução, você deve popular esse banco ativando o script populate_data.py.
- API: Expondo um endpoint /data para consultar os dados brutos do banco fonte e outro endpoint /signal para consultar os dados transformados (agregados) que o ETL processa.
- Processo ETL: Extrai os dados do endpoint /data via httpx, transforma-os utilizando pandas (reagrupar os dados em janelas de 10 minutos e calcular estatísticas como média, mínimo, máximo e desvio padrão) e carrega os resultados na tabela “signal” do banco destino.

Após popular o banco fonte e reiniciar o Docker (para que os dados estejam disponíveis no banco source), os endpoints funcionam conforme abaixo:
- Acessando o link:
  http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power
  Você visualizará o JSON com os dados brutos do banco de dados source.
- Já para o banco de destino, acesse:
  http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
  Neste endpoint, serão apresentados os dados transformados (agregados) pelo ETL.

## Estrutura do Projeto

ETL_Project/
├── README.md
├── docker-compose.yml
├── Dockerfile-api
├── Dockerfile-etl
├── requirements.txt
├── config.py
├── api/
│   ├── main.py                # Ponto de entrada da API (FastAPI)
│   ├── routes.py              # Endpoint /data para o banco fonte
│   ├── routes_target.py       # Endpoint /signal para o banco destino
│   └── database.py            # Conexão com o banco fonte
├── db/
│   ├── source/                # Scripts e SQL para criação/população do banco fonte (source_db)
│   │   └── create_tables.sql
│   └── target/                # Models e script de criação do esquema do banco destino (target_db)
│       └── models.py
├── etl/
│   ├── __init__.py
│   ├── etl_runner.py          # Ponto de entrada do ETL (extrai, transforma e carrega os dados)
│   ├── extract.py             # Extração dos dados (usa httpx para acessar o endpoint /data)
│   ├── transform.py           # Transformação dos dados (pandas, resample e agregações)
│   └── load.py                # Carregamento dos dados (usa SQLAlchemy para inserir os dados na tabela signal)
└── scripts/
    └── visualize_signal.py   # Script para visualizar os dados da tabela signal (Banco destino)

## Pré-requisitos

- Docker (https://www.docker.com/)
- Docker Compose (https://docs.docker.com/compose/)
- Se preferir executar alguns scripts localmente: Python 3.9+ e as dependências listadas em requirements.txt

## Como Usar

### Execução com Docker

1. Inicialmente, o banco de dados fonte estará vazio. Com o Docker rodando, você deve popular esse banco ativando o script populate_data.py (este script deve ser executado separadamente para inserir os dados brutos no source_db).
2. Após a população, reinicie o Docker para que os dados fiquem disponíveis no banco fonte.
3. Com os dados disponíveis, execute:
   
   docker-compose up --build

Os serviços serão iniciados da seguinte forma:
- db_source: Banco fonte (source_db)
- db_target: Banco destino (target_db) – mapeado para a porta 5433 do host
- api: A API (FastAPI) na porta 8000
- etl: O processo ETL que extrai, transforma e carrega os dados no banco destino

### Configuração das Variáveis de Ambiente

O arquivo config.py utiliza os valores das variáveis de ambiente ou usa padrões:
  
Exemplo de config.py:

---------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()

import os

# Conexão com o banco de dados Fonte (usado na API)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db_source/source_db")

# Conexão com o banco de dados Alvo (usado no ETL)
TARGET_DATABASE_URL = os.getenv("TARGET_DATABASE_URL", "postgresql://user:password@db_target/target_db")

# URL da API para o processo de ETL
API_URL = os.getenv("API_URL", "http://localhost:8000")
---------------------------------------------------------

Você pode definir essas variáveis:
- Diretamente no arquivo config.py,
- Através de um arquivo .env na raiz do projeto,
- No próprio docker-compose.yml (como configurado abaixo).

Exemplo de trecho no docker-compose.yml:

services:
  api:
    environment:
      - DATABASE_URL=postgresql://user:password@db_source/source_db
      - TARGET_DATABASE_URL=postgresql://user:password@db_target/target_db
      - API_URL=http://api:8000
  etl:
    environment:
      - API_URL=http://api:8000
      - TARGET_DATABASE_URL=postgresql://user:password@db_target/target_db

### Consultando os Endpoints

- **Dados Brutos (Banco Fonte):**  
  Acesse o endpoint /data para visualizar os registros brutos:
  
  http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power
  
- **Dados Agregados (Banco Destino):**  
  Após a execução do ETL, acesse o endpoint /signal para visualizar os dados transformados:
  
  http://localhost:8000/signal
  ou com filtro de data:
  http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
  
- **Swagger UI:**  
  Documentação interativa disponível em:
  
  http://localhost:8000/docs

### Visualizando os Dados do Banco Destino

Utilize o script de visualização para conferir os registros da tabela signal.
No terminal, na raiz do projeto (ou na pasta scripts/), execute:
  
   python scripts/visualize_signal.py

Isso se conectará ao banco de destino (target_db) e imprimirá os registros.

## Resumo

- Visão Geral: Projeto ETL com dois bancos de dados, uma API para exposição de dados e um processo ETL que extrai, transforma e carrega os dados.
- Estrutura do Projeto: Organizado em módulos para a API, bancos de dados, ETL e scripts de utilidade.
- Pré-requisitos: Docker, Docker Compose e, opcionalmente, Python 3.9+ com as dependências.
- Como Usar: 
   1. Inicialmente, ative o script populate_data.py para popular o banco fonte.
   2. Reinicie o Docker para carregar os dados e execute `docker-compose up --build`.
   3. Acesse os endpoints:
      - Dados do banco fonte: http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power
      - Dados do banco destino (transformados): http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
   4. Utilize o script visualize_signal.py para visualizar os registros diretamente no target_db.
