Feature: Compra de Passagem Aerea
  Scenario Outline: Viagem de Sao Paulo a New York
    Given que acesso o site Blazedemo
    # Parametros fixos
    When pesquiso passagens de 'Sao Paulo' a 'New York'
    # Lista de Parametros
    When pesquiso passagens de <origem> a <destino>
         | origem      | destino    |
         | 'Sao Paulo' | 'New York' |
    And seleciono o primeiro voo
    And preencho os dados de pagamento como <cartao> <titular> <validade> <cvv>
         | cartao   | titular   | validade | cvv |
         | '999999' | 'Juca Yu' | '11/2024'|'123'|
    Then valido se a passagem foi emitida

    Examples:
        | origem      | destino    | cartao   | titular   | validade | cvv |
        | 'Sao Paulo' | 'New York' | '999999' | 'Juca Yu' | '11/2024'|'123'|