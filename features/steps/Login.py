import time

from behave import *
from selenium import *
from selenium.webdriver.common.by import By

debug = 2

@when(u'clico em Home')
def clico_em_Home(context):
    #context.driver.find_element(By.LINK_TEXT, 'home').click()
    #context.driver.find_element(By.CSS_SELECTOR, 'a[href=home]').click()
    #context.driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    context.driver.find_element(By.CSS_SELECTOR, 'a:nth-child(3)').click()
    time.sleep(debug)


@then(u'exibe a pagina de Login')
def exibe_a_pagina_de_Login(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'


@when(u'preencho "{email}" e "{senha}"')
def preencho_email_e_senha(context, email, senha):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    time.sleep(debug)


@when(u'clico em Login')
def clico_em_Login(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    time.sleep(debug)


@then(u'exibe a mensagem de pagina expirada')
def exibe_a_mensagem_de_pagina_expirada(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    time.sleep(debug)

