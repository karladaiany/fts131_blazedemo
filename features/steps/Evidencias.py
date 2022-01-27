import os
import time
from datetime import datetime

from selenium import webdriver      # Referencia ao Selenium WebDriver
import pytest                       # Referencia ao Framework de Testes Unitário
from selenium.webdriver.common.by import By


caminho_print = '../prints/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'
# '..prints/2021-11-24 21-37-54/'

def testar_blazedemo():
    #Criação da pasta para guardar os prints desta execução
    os.makedirs(caminho_print)

    # Definindo que controlará o Chrome e apontando onde está o ChromeDriver
    driver = webdriver.Chrome(executable_path='../../drivers/chrome/97/chromedriver.exe')


    driver.get("https://www.blazedemo.com")
    time.sleep(30) # pausa de 30 segundos - precisa remover depois - "Alfinete"
    # Usa o próprio Selenium para tirar o print e salvar no disco
    driver.get_screenshot_as_file(f'{caminho_print} home.png')
    time.sleep(3)  # pausa de 3 segundos - precisa remover depois - "Alfinete"
    driver.find_element(By.CSS_SELECTOR,'input.btn.btn-primary').click()
    time.sleep(10)
    driver.get_screenshot_as_file(f'{caminho_print} voos.png')
    time.sleep(3)