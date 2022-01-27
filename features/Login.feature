Feature: Login

  Scenario: Login com Sucesso
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho "teste@iterasys.com" e "pwd123"
    And clico em Login
    Then exibe a mensagem de pagina expirada

  Scenario Outline: Varios Logins com Sucesso
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho "<email>" e "<senha>"
    And clico em Login
    Then exibe a mensagem de pagina expirada
    Examples:
      | email               | senha  |
      | teste1@iterasys.com | abc123 |
      | testes@iterasys.com | 123456 |