# Turing-Machine

## Overview
**Criado por: Wendell Reis Milani Matias**

Este projeto conciste na implementação de um algortimo que simula uma Máquina de Turing (TM). É motivado pela disciplina de Linguagens Formais e Autômatos (LFA) ofertada pelo CEFET-MG Campus Leopoldina.

## Guia de Uso
A execução do programa depende da passagem do nome de um arquivo em formato .json que deverá conter todas as informações de uma TM: 

- **alfabeto**: vetor contendo os caracteres aceitos pela linguagem considerando **'&'** como caracter vazio.
- **simbolos**: vetor contendo os caracteres que a TM consegue escrever na fita.
- **estados: vetor** contendo o nome dos estados.
- **estado_inicial**: nome do estado inicial
- **estados_aceitacao**: vetor contendo os estados de aceitação
- **estados_rejeicao**: vetor contendo os estados de rejeição
- **transicoes**: dicionário onde cada chave representa um estado e o seu valor concista em uma lista de transições do tipo **(X,Y,D,S)**, ou seja, uma transição que lê o caracter **X**, escreve **Y**, descoloca a cabeça da TM para a direção **D** (esquerda (L) ou direita (R)) e passa para o estado **S**. Estados sem transições devem possuir valor de lista vazia ([]).
- **palavras**: vetor contendo um conjunto de palavras que serão processadas pela TM.

O presente repositório possui arquivos .json que exemplificam a forma correta que um autômato deve ser descrito. É possível executar um teste com:

```
python3 main.py anbn.json
```

*O correto funcionamento do programa está condicionado a correta descrição da TM através do arquivo de entrada .json.*
