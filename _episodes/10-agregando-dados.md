---
title: "Agregando Dados com Pandas"
teaching: 20
exercises: 10
questions:
- "Como eu posso agrupar dados categóricos com Pandas?"
objectives:
- "Descrever uso do método `describeg`."
- "Descrever uso do método `value_counts`."
- "Descrever uso do método `groupby`."
- "Lidando com valores omissos (*missing values*)."
keypoints:
- "Fazer sumários de variáveis numéricas e categóricas é um requisito muito comum."
- "Dados omissos podem interferir em como sumários estatísticos são calculados."
- "Dados omissos podem ser substituídos dependendo da situação."
- "Sumários e agregações podem ser feitos com múltiplas variáveis."
---

## Usando Pandas para sumarizar dados

Já vimos o método `.describe()` que traz um sumário de estatísticas
para as colunas que contém números no DataFrame. Vamos importar os
dados de balanço dos centros de transformação e rodar o método `describe`.

```python
df = pd.read_csv("data/EPE/balanco_centros_transformacao.csv")
df.describe()
```

Diversas outras medidas podem ser calculadas com os métodos do DataFrame, como `df.mean()`, `df.median()`, `df.max()`, etc...

## Lidando com variáveis categóricas

O método `.describe()` é útil para ver sumários de variáveis numéricas, mas como podemos
ver o total de variáveis categóricas? Para isso, usamos o método `.value_counts()`, que
calcula a quantidade de valores em cada categoria de uma variável. Por exemplo, podemos 
ver as contagens para a variável `"IDENTIFICAÇÃO"`:

```python
df["IDENTIFICAÇÃO"].value_counts()
```

~~~
CENTRAIS ELÉTRICAS    25
PETRÓLEO              12
GÁS NATURAL            6
Name: IDENTIFICAÇÃO, dtype: int64
~~~
{: .output}

Quando usamos o método `value_counts()`, criamos uma nova `pd.Series` na qual o atributo `index` (o nome das linhas) são os valores das variáveis categóricas que estamos contando. Os valores (atributo `values`) são as contagens.

## Agrupando dados

Também podemos usar variáveis categóricas para agrupar dados, e calcular estatísticas a partir deles. Para isso, usamos o método `groupby`.

```python
df.groupby("IDENTIFICAÇÃO")
```

~~~
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x143561130>
~~~
{: .output}

Esse objeto `groupby` parece meio críptico, no entanto, isso é por que precisamos escolher como queremos sumarizar os dados. Queremos a média, o máximo, o mínimo, etc.

```python
df.groupby("IDENTIFICAÇÃO").min()
df.groupby("IDENTIFICAÇÃO").max()
df.groupby("IDENTIFICAÇÃO").sum()
df.groupby("IDENTIFICAÇÃO").mean()
```

Também é possível especificar múltiplos níveis para o `groupby`:

```python
gb = df.groupby(["IDENTIFICAÇÃO", "FONTES"]).mean()
```

Isso gera um **MultiIndex**, com mais de um nível hierárquico:

```python
gb.loc[("CENTRAIS ELÉTRICAS", "BAGAÇO DE CANA")]
```

## Substituindo valores nulos

Podemos reparar que no nosso DataFrame agrupado `gb`, temos valores do tipo `NaN`, ou **Not a Number**. Esses valores são valores "nulos", e serão ignorados ao calcularmos estatísticas de sumário. Podemos substituí-los com o método `.fillna()`:

```python
gb.fillna(0)
```
