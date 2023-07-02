

# Truco 1.0
  
  __Requisitos implementados:__  

 - [x] Suporta execução distribuída
 - [x] Interface gráfica em versão inicial
 - [x] Pedir Truco e suas tratativas agora são funcionais
 - [x] Testado em Python 3.11.4

## Notas importantes: 
Caso sejam instanciados dois jogadores com o mesmo nome, o jogo apresenta erro.

É necessário que os arquivos `pipfile.lock` e `requirements` estejam na pasta "pythonCode".

Para que a interface gŕafica carregue corretamente, a pasta "images" deve estar dentro de `pythonCode -> truco -> game_logic`.

## Instalação e execução

Executar em ambiente virtual:
```python
pipenv install
pipenv shell
python -m truco
```
  
Necessário pillow e pynetgames, instalados no ambiente virtual por meio de `requirements.txt` [^1]


> Written with [StackEdit](https://stackedit.io/).

[^1]: O uso de `requirements.txt` foi feito conforme recomendações da disciplina, no entanto, seu uso possui [vulnerabilidades conhecidas](https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895).
