# 🚀 ETL Project

## Visão Geral

Este projeto conecta **dois bancos PostgreSQL**, uma **API FastAPI** e um **script ETL**:

Componente        | Função
------------------|--------------------------------------------------------------
Banco Fonte       | Guarda os dados brutos (começa vazio).
API               | • /data   → devolve dados brutos do Banco Fonte  
                  | • /signal → devolve dados agregados gerados pelo ETL
ETL (Python/Pandas)| • Extrai via /data  
                  | • Agrupa em janelas de 10 min (média, mín., máx., desvio-padrão)  
                  | • Carrega na tabela **signal** do Banco Destino

Depois de popular o Banco Fonte e reiniciar os contêineres, você já pode chamar os endpoints.

--------------------------------------------------------------------

## Como Usar

1 — Subir a stack
-----------------
`docker-compose build`   # cria as imagens  
`docker-compose up`    # inicia bancos + API  

2 — Popular o Banco Fonte
-------------------------

Compile o arquivo `populate_data.py` separadamente enquanto o Docker está rodando.  

3 — Reiniciar para a API enxergar os dados
------------------------------------------
Dê control-c e rode `docker-compose up` novamente.

--------------------------------------------------------------------

## Endpoints

Tipo de dado | URL de exemplo
-------------|------------------------------------------------------------------------------------------------------------------------------------
Bruto        | http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power,ambient_temperature
Agregado     | http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59

Dica: ajuste start_date, end_date e (em /data) a lista de fields conforme necessário.

--------------------------------------------------------------------

## Resumo Rápido

1. **Suba** os serviços (docker-compose up -d).  
2. **Popule** o source_db rodando populate_data.py.  
3. **Reinicie** os contêineres.  
4. Consulte **/data** (dados brutos) ou **/signal** (dados transformados).

Pronto! 🎉
