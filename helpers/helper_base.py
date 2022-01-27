from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper_Func(object):
    __TIMEOUT = 10  # Definimos um limite de espera de 10 segundos

    # Definição de uma espera explicita
    def __init__(self, driver):  # Criou a Definição de inicialização da classe
        super(Helper_Func, self).__init__()  # Estabele que driver herda de Helper_Func
        # Criação de um objeto para controlar as esperas do Selenium (driver)
        self._driver_wait = WebDriverWait(driver, Helper_Func.__TIMEOUT)
        self._driver = driver

    # Definição da abertura de uma URL / Acessar um site
    def open(self, url):
        self._driver.get(url)

    # Maximizar a janela do browser
    def maximize(self):
        self._driver.maximize_window()

    # Finalizar o objeto do Selenium WebDriver
    def close(self):
        self._driver.quit()

    # Definições uteis para selecionar elementos

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located(By.ID, id))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located(By.NAME, name))

    def find_by_css(self, css):
        return self._driver_wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, css))

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located(By.XPATH, xpath))