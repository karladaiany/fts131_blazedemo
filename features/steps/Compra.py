import time

from behave import *
from selenium import *
from selenium.webdriver.support.select import Select

from features import environment


# Before no Java / Setup no C#
from selenium.webdriver.common.by import By

# Atributos / Variaveis para armazenar os localizadores
debug = 0
origem = 'fromPort'

def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )

#TODO: "Desambiguar o passo com o PO"
@given('que acesso o site Blazedemo')
@given('que acesso o portal Blazedemo')
def que_acesso_o_site_Blazedemo(context):
    context.driver.get('https://www.blazedemo.com')
    # Para demonstrar ao usuário o funcionamento
    # introduzimos um conjunto de esperas
    # que são anuladas nas execuções normais
    time.sleep(debug)
    print('Passo 1 - Abriu o site')


@when('pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_origem_a_destino(context, origem, destino):
    # Elemento da página mapeado para o campo origem
    '''
    # Opção 1
    context.driver.find_element(By.NAME, 'fromPort').select(origem)
    # Opção 2
    context.driver.find_element_by_name('fromPort').select(origem)
    # Opção 3
    context.origem = context.driver.find_element(By.NAME, origem)
    '''

    # Campo Origem
    # Cria um elemento a partir da localização do mesmo na página
    elemento_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto que seleciona o elemento (combo)
    objeto_origem = Select(elemento_origem)

    # Usando o objeto você seleciona o elemento na lista (combo)
    objeto_origem.select_by_visible_text(origem)
    time.sleep(debug)

    # Campo Destino
    elemento_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(elemento_destino)
    objeto_destino.select_by_visible_text(destino)
    time.sleep(debug)

    # Clicar no botão de pesquisar Vôos
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print(f'Passo 2 - Pesquisou passagem de {origem} para {destino}')


@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    # Clicar no botão de seleção do 1º vôo
    time.sleep(debug)
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 3 - Selecionou o primeiro voo')


@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    # Escrever na caixa de texto do Nome
    time.sleep(debug)
    context.driver.find_element(By.ID, 'inputName').send_keys('Karla Oliveira')
    time.sleep(debug)
    # Clicar no botão de comprar passagem
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    time.sleep(debug)
    print('Passo 4 - Preencheu os dados de pagamento')


@then('valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    # Validar se o título da guia exibe que está na página de transação confirmada
    assert context.driver.title == 'BlazeDemo Confirmation'
    print('Passo 5 - Validou se a passagem foi emitida')