from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

# Configurações para evitar bloqueio
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executar o navegador em modo headless
options.add_argument("--no-sandbox")  # Bypass do erro de "sandbox" no Linux
options.add_argument("--disable-dev-shm-usage")  # Bypass de erro de "dev-shm-usage" no Linux

# Inicialização do driver
driver = webdriver.Chrome(options=options)

# Esperar um tempo para garantir que a página seja totalmente carregada
driver.implicitly_wait(10)

# URL para scraping
url = 'https://kworb.net/spotify/artist/06HL4z0CvFAxyc27GXpf02_songs.html'

# Acessar a página
driver.get(url)

# Esperar um tempo para garantir que a página seja totalmente carregada
time.sleep(5)

# Encontrar a tabela
table = driver.find_element("xpath", '/html/body/div[1]/div[5]/table[2]')

# Extrair dados da tabela e escrever em um arquivo CSV
with open('TS_table.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    # Encontrar os cabeçalhos da tabela
    header_row = table.find_elements(By.TAG_NAME, 'th')
    # Extrair os nomes das colunas
    column_names = [header.text.strip() for header in header_row]
    # Escrever os nomes das colunas no arquivo CSV
    writer.writerow(column_names)
    
    # Iterar sobre as linhas da tabela
    for row in table.find_elements(By.TAG_NAME,'tr'):
        # Extrair dados de cada célula da linha e limpar espaços em branco
        row_data = [cell.text.strip().replace(',', '-').replace('*', '') if index == 0 else cell.text.strip() for index, cell in enumerate(row.find_elements(By.TAG_NAME,'td'))]
        # Escrever os dados no arquivo CSV
        writer.writerow([str(data).encode('utf-8').decode('utf-8') for data in row_data])

# Fechar o navegador
driver.quit()
