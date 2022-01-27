@compra_passagem
Feature: Compra de Passagem Aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site Blazedemo
    # Parametros fixos
    When pesquiso passagens de "São Paolo" a "New York"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi emitida

  Scenario: Viagem de Boston a Dublin
    Given que acesso o portal Blazedemo
    # Parametros fixos
    When pesquiso passagens de "Boston" a "Dublin"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi emitida

  Scenario Outline: Compra de Passagens
    Given que acesso o portal Blazedemo
    # Parametros fixos
    When pesquiso passagens de "<origem>" a "<destino>"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi emitida
    Examples:
      |    origem   |   destino  |
      |  Portland   |   Berlin   |
      |  San Diego  |    Rome    |