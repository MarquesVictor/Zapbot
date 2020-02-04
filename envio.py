import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import urllib.parse as urllib
import os.path 

def disparo(csv, img, text):
    timeout = 10
    driver = webdriver.Chrome()
    csv = open(csv, 'r')
    dowload_path = os.path.expanduser("~")+"/Downloads/"
    saida = open(dowload_path+'falhas.csv', 'w')
    for line in csv:
        erro = 0
        txt = text
        while True:
            try:
                parametros = {'phone': "55"+line, 'text': txt }
                parametros = urllib.urlencode(parametros)
                url = "https://web.whatsapp.com/send?{0}".format(parametros)
                driver.get(url)
                btn_clip = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="main"]/header/div[3]/div/div[2]/div')))
                btn_clip.click()
                driver.find_elements(By.CSS_SELECTOR, "input[type='file']")[0].send_keys(img)
                btn_envio = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='send-light']")))
                btn_envio.click()
                time.sleep(5)
            except:
                erro += 1
                if erro == 3:
                    #Grava os dados que não foram enviados...
                    msgerro = 'Erro nao detctado'
                    elerro = WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')))

                    if elerro:
                        msgerro = elerro.text

                    saida.write("{0};{1}\n".format(int(line), msgerro))
                    break #fim-while
                continue
            break
    #fim-loop  
    driver.close() 
    csv.close()
    saida.close()
