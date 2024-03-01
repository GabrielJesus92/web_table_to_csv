# README

## Descrição
Este script Python é um exemplo de como realizar web scraping em uma tabela de uma página da web usando Selenium. Ele acessa a página 'https://kworb.net/spotify/artist/06HL4z0CvFAxyc27GXpf02_songs.html', extrai os dados da tabela presente na página e os salva em um arquivo CSV chamado 'TS_table.csv'.

## Pré-requisitos
- Python 3.x
- Bibliotecas Python: Selenium, WebDriver Manager

## Instalação
Você pode instalar as bibliotecas necessárias através do gerenciador de pacotes pip. Execute o seguinte comando no terminal:

pip install selenium webdriver_manager


## Como usar
1. Clone ou baixe este repositório para sua máquina local.
2. Certifique-se de ter todas as bibliotecas necessárias instaladas.
3. Execute o script Python `web_scraping.py`.
4. Aguarde até que o script termine de executar.
5. O arquivo CSV resultante, `TS_table.csv`, será gerado no mesmo diretório do script.

## Detalhes técnicos
- O script utiliza o Selenium para automatizar o navegador Chrome. É configurado para funcionar em modo headless, evitando a exibição do navegador durante a execução.
- São feitas configurações adicionais para evitar problemas comuns de bloqueio devido à execução automatizada.
- Os dados são extraídos da tabela da página da web e escritos em um arquivo CSV.
- O arquivo CSV contém os nomes das colunas como a primeira linha, seguidos pelos dados das linhas subsequentes.

## Autor
[https://github.com/GabrielJesus92/]
