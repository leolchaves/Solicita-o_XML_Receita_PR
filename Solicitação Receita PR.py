from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from tqdm import tqdm
from datetime import datetime, timedelta

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

solicitacao_df = pd.read_excel(r'Solicitação XML NFe.xlsx')
pela_receita = solicitacao_df['OBSERVAÇÕES'] == 'Pela ReceitaPR' # Faz um filtro de True ou False, True é = 'Pela Receita'
receita_df = solicitacao_df[pela_receita] # Armazena o DF pelo filtro que criamos acima
receita_df.reset_index(inplace=True, drop=True) # Reseta o indice das linhas
somente_dest = solicitacao_df['OBSERVAÇÕES'] == 'Somente Destinadas'# Faz um filtro de True ou False, True é = 'Somente Destinadas'
destinadas_df = solicitacao_df[somente_dest]
destinadas_df.reset_index(inplace=True, drop=True) # Reseta o indice das linhas

hoje = datetime.now()
ontem = str(hoje - timedelta(days=1))
ultimo_dia = ontem[8:10]
mes = ontem[5:7]
ano = ontem[0:4]

navegador.get('https://receita.pr.gov.br/')
navegador.find_element(By.ID, 'cpfusuario').send_keys('COLOQUE SEU LOGIN') # Por questões de privacidade foi apagado o login
navegador.find_element(By.NAME, 'senha').send_keys('COLOQUE SUA SENHA') # Por questões de privacidade foi apagado a senha
navegador.find_element(By.XPATH , '/html/body/div[2]/form[1]/div[4]/button').click()

navegador.find_element(By.XPATH, '//*[@id="menulateral"]/div/a[12]').click()
navegador.find_element(By.XPATH, '//*[@id="menulateral215"]/div/a').click()
navegador.find_element(By.XPATH, '//*[@id="menulateral238"]/div/a').click()
navegador.find_element(By.ID, 'menuLink750').click()
navegador.find_element(By.ID, 'ext-gen1030').clear()
navegador.find_element(By.ID, 'ext-gen1030').send_keys(f'01/{mes}/{ano}')
navegador.find_element(By.ID, 'ext-gen1022').clear()
navegador.find_element(By.ID, 'ext-gen1022').send_keys('00:00:00')
navegador.find_element(By.ID, 'ext-gen1032').clear()
navegador.find_element(By.ID, 'ext-gen1032').send_keys(f'{ultimo_dia}/{mes}/{ano}')
navegador.find_element(By.ID, 'ext-gen1023').clear()
navegador.find_element(By.ID, 'ext-gen1023').send_keys('23:59:59', Keys.ENTER)
navegador.find_element(By.ID, 'ext-gen1081').send_keys('26.899.016/0001-71', Keys.ENTER, Keys.TAB)
sleep(1)

for i in tqdm(range(len(receita_df))):
    cnpj = receita_df['CNPJ'][i]
    navegador.find_element(By.ID, 'ext-gen1112').click()
    navegador.find_element(By.ID, 'ext-gen1081').clear()
    navegador.find_element(By.ID, 'ext-gen1081').send_keys(cnpj, Keys.ENTER, Keys.TAB)
    sleep(2)
    navegador.find_element(By.ID, 'ucs20_ToolBarbtnAtualizar-btnWrap').click()
    navegador.find_element(By.ID, 'ucs20_BtnAgendar-btnInnerEl').click()
    sleep(0.5)
    try:
        elemento = WebDriverWait(navegador, 1).until(EC.presence_of_element_located((By.ID, 'button-1009-btnInnerEl')))
        sleep(1)
        elemento.click()
    except:
        pass
    navegador.find_element(By.ID, 'ext-gen1116').click()
    navegador.find_element(By.ID, 'ucs20_BtnAgendar-btnInnerEl').click()
    sleep(0.5)
    try:
        elemento = WebDriverWait(navegador, 1).until(EC.presence_of_element_located((By.ID, 'button-1009-btnInnerEl')))
        sleep(1)
        elemento.click()
    except:
        pass

sleep(1)
for i1 in tqdm(range(len(destinadas_df))):
    cnpj_1 = destinadas_df['CNPJ'][i1]
    navegador.find_element(By.ID, 'ext-gen1116').click()
    navegador.find_element(By.ID, 'ext-gen1081').clear()
    navegador.find_element(By.ID, 'ext-gen1081').send_keys(cnpj_1, Keys.ENTER, Keys.TAB)
    sleep(2)
    navegador.find_element(By.ID, 'ucs20_ToolBarbtnAtualizar-btnWrap').click()
    navegador.find_element(By.ID, 'ucs20_BtnAgendar-btnInnerEl').click()
    sleep(0.5)
    try:
        elemento = WebDriverWait(navegador, 1).until(EC.presence_of_element_located((By.ID, 'button-1009-btnInnerEl')))
        sleep(1)
        elemento.click()
    except:
        pass
