# ETL Project

## Visão Geral

Este projeto implementa um pipeline ETL simples que integra dois bancos de dados PostgreSQL, uma API construída com FastAPI e um script de ETL.
A aplicação consiste em:

- Banco Fonte: Armazena dados brutos, que inicialmente estarão vazios. Após o Docker estar em execução, você deve popular esse banco ativando o script populate_data.py.
- API: Expondo um endpoint /data para consultar os dados brutos do banco fonte e outro endpoint /signal para consultar os dados transformados (agregados) que o ETL processa.
- Processo ETL: Extrai os dados do endpoint /data via httpx, transforma-os utilizando pandas (reagrupar os dados em janelas de 10 minutos e calcular estatísticas como média, mínimo, máximo e desvio padrão) e carrega os resultados na tabela “signal” do banco destino.

![Imagem do WhatsApp de 2025-04-16 à(s) 11 58 30_8327298b](https://github.com/user-attachments/assets/75a3c8d1-d836-417c-8b53-1b4c586a2af3)


Após popular o banco fonte e reiniciar o Docker (para que os dados estejam disponíveis no banco source), os endpoints funcionam conforme abaixo:
- Acessando o link:
  http://localhost:8000/data?start_date=2025-04-05T00:00:00&end_date=2025-04-06T00:00:00&fields=timestamp,wind_speed,power
  Você visualizará o JSON com os dados brutos do banco de dados source.
- Já para o banco de destino, acesse:
  http://localhost:8000/signal?start_date=2025-04-05T00:00:00&end_date=2025-04-05T23:59:59
  Neste endpoint, serão apresentados os dados transformados (agregados) pelo ETL.

