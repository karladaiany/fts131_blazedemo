@Cadastro
Feature: Cadastro de Usuario
  Scenario: Cadastro com Sucesso
    Given que acesso o portal Blazedemo
    When clico em home
    And clico em Register
    Then vejo o formulario de cadastro
    When preencho "<nome>" "<empresa>" "<email>" "<senha>"
    And clico no botão Register
    Then exibe a confirmação do cadastro
