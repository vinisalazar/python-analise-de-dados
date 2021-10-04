---
title: "Revisão Fundamentos Básicos"
teaching: 10
exercises: 10
questions:
- "Quais são os fundamentos básicos do Python?"
objectives:
- "Descrever o que são variáveis e tipos de dados."
- "Descrever o que são funções embutidas."
- "Descrever o que são métodos."
- "Descrever como importar bibliotecas."
- "Descrever o que são listas e demonstrar o uso do for loop."
- "Descrever o que são condicionais e demonstrar o uso `if/elif/else`."
- "Descrever o que são funções e escrever uma função."
keypoints:
- "Variáveis são nomes que assinalamos a valores, ou objetos."
- "Funções embutidas já vem no Python e servem para operações comuns."
- "Métodos são funções associadas a objetos."
- "Bibliotecas podem ser usadas para importar outras funções."
- "A biblioteca padrão conta com vários módulos que já vem com o Python."
- "Listas são um tipo de coleção para armazenar múltiplos valores."
- "Condicionais são usadas para controlar o fluxo de um programa."
- "Funções recebem zero ou mais argumentos e sempre retornam algum valor."
- "Funções são usadas para decompôr programas em partes menores."
---

## Variáveis são nomes que assinalamos a valores, ou objetos.

```python
a = "Uma string"
b = 3.14
c = 42

for variavel in a, b, c:
    print(variavel, "é um valor do tipo", type(variavel))
```

## Funções embutidas já vem no Python e servem para operações comuns.

```python

a = "CPFL"
b = [1, 2, 3]
c = 3.14


print(len(a))
print(type(a))
print(list(a))
print(max(b))
print(min(b))
print(sum(b))
print(round(c))
```

## Métodos são funções associadas a objetos.

Use `valor.` + `Shift + TAB` para ver os métodos disponíveis para um objeto.

```python
# Métodos de lista
valor = "uma string"

print(valor.upper())
```

```python
lista = [1, 2, 3]
print("Lista é", lista)
print("O método .pop() remove o último valor da lista:", lista.pop())
print("Lista agora é", lista)
```

## Bibliotecas podem ser usadas para importar outras funções.

```python
import math

print("O cosseno de pi é", math.cos(math.pi))
```

## A biblioteca padrão conta com vários módulos que já vem com o Python.

Explore a [documentação oficial do Python](https://docs.python.org/pt-br/3/library/index.html) para saber mais sobre a biblioteca padrão.

## Listas são um tipo de coleção para armazenar múltiplos valores.

```python
uma_lista = [42, 65, -12, 104, 76, 43, 21]

for numero in uma_lista:
    if numero % 2 == 0:
        print(numero, "é par")
```

## Condicionais são usadas para controlar o fluxo de um programa.

```python
consumo = 250

print("Consumo é:", consumo)
if consumo > 100:
    print("Consumo está muito alto! Diminuindo.")
    consumo = 50
    print("Consumo agora é:", consumo)
```

## Funções recebem zero ou mais argumentos e sempre retornam algum valor.

- A função `print` recebe zero ou mais argumentos e retorna o valor None.
- As funções `max` e `min` recebem um ou mais argumentos do mesmo tipo e retornam o maior ou menor valor.

## Funções são usadas para decompôr programas em partes menores.

Se eu tenho, por exemplo, um programa que lê um arquivo, calcula uma estatística, e envia ela para um email, poderíamos dividi-lo em três funções:

1. Uma para ler o arquivo:
    ```python
    def ler_arquivo(caminho_do_arquivo):
        with open(caminho_do_arquivo) as f:
            ...
    ```
2. Uma para calcular a estatística (que poderia receber o conteúdo do arquivo como uma string ou lista):
    ```python
    def calcular_estatistica(conteudo_do_arquivo):
        maior_valor, menor_valor = None, None
        for valor in conteudo_do_arquivo:
            ...
    ```

3. Uma para enviar o email:
    ```python
    def enviar_email(estatistica, endereco_email):
        ...
    ```

Assim poderia escrever algo assim no programa:

```python
arquivos = [
    ...
]

for caminho in arquivos:
    conteudo = ler_arquivo(caminho)
    estatistica = calcular_estatistica(conteudo)
    enviar_email(estatistica, "usuario@mail.com")

```
