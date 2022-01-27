import time

from behave import when, then
from selenium.webdriver.common.by import By

debug = 2

@when(u'clico no Link Forgot Your Password?')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()

@then(u'vejo a pagina de reiniciar a senha')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Reset Password'

@when(u'preencho o "{email}" e clico no botao Send Password Reset Link')
def step_impl(context, email):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

@then(u'vejo a mensagem de confirmacao')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    time.sleep(debug)