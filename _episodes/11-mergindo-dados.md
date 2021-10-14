---
title: Combinando DataFrames com Pandas
teaching: 20
exercises: 25
questions:
  - "Como posso trabalhar com dados de múltiplas fontes?"
  - "Como eu posso combinar dados de diferentes datasets?"
objectives:
   - "Combinar dados de múltiplos arquivos em um único DataFrame usando merge e concat."
   - "Combinar dois DataFrames usando um ID único encontrado em ambos os DataFrames."
   - "Empregar `to_csv` para exportar um DataFrame no formato CSV."
   - "Unir DataFrames usando campos em comum (chaves de join)."
keypoints:
   - "As funções `merge` and `concat` do Pandas podem ser usados para combinar subsets de um DataFrame, ou até dados de diferentes arquivos."
   - "O 'join' de dois dataframes pode ser feito de várias formas (*left*, *right*, *outer*, e *inner*) dependendo do que precisa estar no DataFrame final."
   - "`to_csv` pode ser usado para exportar DataFrames."
---

Em muitas situações reais, os dados que queremos utilizar vêm em múltiplos arquivos.
É comum precisarmos combinar esses arquivos em um único DataFrame para poder analisar os dados. O Pandas provê várias funções para combinar DataFrames, vamos ver duas delas: `concat` e `merge`.

## Concatenando DataFrames

A função `concat` permite concatenar DataFrames tanto no eixo horizontal (das linhas)
quanto vertical (das colunas). Para usar o método `concat`, precisamos de uma lista de DataFrames. Nos nossos dados, temos os dados de consumo anual de energia separados por setor. Vamos supôr por um momento que não temos o DataFrame com todos os dados combinados (`consumo_anual_energia_por_classe_1995-2018.csv`). Vamos criar uma lista de arquivos com `glob`, depois uma lista de DataFrames com `pd.read_csv`.

```python
arquivos = glob("data/EPE/consumo_anual_energia_setor_*.csv")

dataframes = []
for arq in arquivos:
   df_setor = pd.read_csv(arq, index_col=0)
   dataframes.append(df_setor)

# Ou com list comprehension
dataframes = [pd.read_csv(arq, index_col=0) for arq in arquivos]
```

Agora temos uma lista de objetos do tipo DataFrame na variável `dataframes`. Podemos rodar `pd.concat` diretamente nela:

```python
setores = pd.concat(dataframes, axis=1)
setores.head()
```
~~~
ANO   COMERCIAL	INDUSTRIAL	   RESIDENCIAL	OUTROS
1995	32276.26017	111626.16093	63576.09392	35595.69503
1996	34387.69450	117127.59543	68581.28330	37233.73579
1997	38197.50400	121717.13300	74089.15430	39276.17100
1998	41544.09420	121979.13550	79340.00033	41658.90937
1999	43587.93405	123892.58842	81291.21490	43416.38964
~~~
{: .output}

> ## Combinando dados
> Na nossa pasta de dados, temos medições de energia da PJM para a EKPC - Eastern 
> Kentucky Power Cooperative.
> Esses dados estão divididos por ano. Use o `glob` e `pd.concat` para juntar todos
> os dados em um único DataFrame.
> **Dica:** copie o exemplo acima, mas omita os parâmetros `index_col` e `axis`.
> > ## Solução
> > Certifique-se que a lista `arquivos` não vai ficar vazia vazia, ou seja, use o caminho certo para o `glob`.
> > ~~~
> > arquivos = glob("data/PJM/EKPC_*")
> > dataframes = [pd.read_csv(arq) for arq in arquivos]
> > ekpc = pd.concat(dataframes)
> > ekpc = df.reset_index(drop=True)
> > ekpc
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Escrevendo Dados Concatenados

Se quisermos escrever qualquer um desses dados uma única tabela, podemos usar o método `.to_csv`, ou `.to_excel` ou qualquer outro.

```python
ekpc.to_csv("data/PJM/EKPC_years.csv", index=False)
setores.to_excel("data/EPE/consumo_anual_setores.xlsx")
```

# Joining DataFrames

Quando concatenamos nosso DataFrame, simplesmente juntamos um no outro, empilhando-os verticalmente ou lado a lado. Outra forma de combinar DataFrames é usar colunas em cada dataset que contém valores comuns (um identificador comum). Combinar DataFrames usando um campo comum é chamado de "joining". As colunas contendo valores comuns são chamadas de "chave(s) de join".

Juntar DataFrames dessa forma é muito útil quando um DataFrame é uma "tabela de lookup", que contém mais informações sobre a entrada que queremos incluir no outro dataframe.

**Exemplo:** Pense numa tabela com transações e outra de clientes. Digamos que queremos o endereço do cliente que fez uma determinada transação. Armazenar o endereço de cada cliente na tabela de transações será muito custoso. Invés disso, armazenamos um único "ID de cliente", e podemos fazer o join da informação da tabela de clientes (que contém o endereço) com a entrada desejada na tabela de transações, através do ID do cliente (o campo em comum entre as duas tabelas). 

NOTA: Esse processo de joins é similar ao que fazemos para fazer join em duas tabelas SQL.

Armazenar dados dessa forma possui vários benefícios, como:

1. Garante consistência na informação adicional que queremos juntar. Se o 'endereço' de cada cliente só aparece uma vez (na tabela de clientes), isso previne erros de repetição.
2. Esse mesmo fator também torna mais fácil modificar os dados. Se um cliente mudar o endereço, basta mudar seu endereço na tabela de clientes, e não precisamos mudar o campo de "endereço do cliente" de cada transação.
3. Isso otimiza o tamanho dos dados.


## Fazendo Joins 

Vamos criar dois DataFrames de exemplo:

```python
df1 = setores.loc[1995:2005, "COMERCIAL":"INDUSTRIAL"].reset_index()
df2 = setores.loc[2000:2010, "RESIDENCIAL":"OUTROS"].reset_index()
```

**Chaves de join**

Como tem a coluna `"ANO"` em comum, podemos fazer o join por ela:

```python
df1.merge(df2, on="ANO")
```

Se as colunas de join tivessem nomes diferentes, podemos especificar as colunas com os argumentos `left_on` e `right_on`:
```python
df1 = df1.rename(columns={"ANO":"YEAR"})
df1.merge(df2, left_on="YEAR", right_on="ANO")
```

## Tipos de Join

![Inner join -- courtesy of codinghorror.com](../fig/inner-join.png)

![Left Join](../fig/left-join.png)

```python
df1.merge(df2, left_on="YEAR", right_on="ANO", how="left")
```


## Outros tipos de Join

```python
df1.merge(df2, left_on="YEAR", right_on="ANO", how="right")
```

```python
df1.merge(df2, left_on="YEAR", right_on="ANO", how="outer")
```

{% include links.md %}
