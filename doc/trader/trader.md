# Módulo Trader 

O trader é instanciado com um nome de metadata, a fim de que sejam
localizados alguns detalhes como:
    
    - Posicionador
        - Nome 
        - Setup_id
    - Stop
        - Nome
        - Setup_id
    - Detalhes da corretora:
        - Nome
        - Chave API
        - API secret
    - Ativo
    - Memória de posição
        - Lado
        - Tamanho
        - Referência de preço para stop
## Ações esperadas em linhas gerais
 
Dada uma estratégia (composta, grosso modo, de um módulo ***posicionador*** 
e outro de ***stop***) o robô deve, periodicamente, aplicar os crtirérios da 
estratégia sobre a amostra de dados corrente.  

Caso a estratégia emita algum sinal de trade, o robô deve:
- disparar e checkar a ordem equivalente para a corretora (em caso de trade real) ou
- appendar no histórico teste (em caso de trade em *"backtesting"*), atualizando a *"memória 
de posição"*.

## Métodos

### __init()__
1 - Localizar os metadados do trade  
2 - Instanciar um posicionador  
3 - Instanciar um stop

### run_for_real()
