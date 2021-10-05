---
title: "Pandas DataFrames"
teaching: 15
exercises: 15
questions:
- "Como posso fazer a análise estatística de dados tabulares?"
objectives:
- "Selecionar valores individuais de um dataframe Pandas."
- "Selecionar linhas inteiras ou colunas inteiras de um dataframe Pandas."
- "Selecionar um subconjunto de colunas E linhas de um dataframe em uma única operação."
- "Selecionar um subset do dataframe por um único critério Booleano (verdadeiro ou falso)."
keypoints:
- "Use `DataFrame.iloc[..., ...]` para selecionar os valores por uma posição de um inteiro."
- "Use `DataFrame.loc[..., ...]` para selecionar valores por sua label."
- "Use `:` para se referir a todas as colunas ou todas as linhas."
- "Selecione múltiplas colunas ou linhas usando `DataFrame.loc` e uma fatia nomeada."
- "O resultado de uma fatia pode ser usado em operações subsequentes."
- "Use comparações para selecionar dados baseados em um valor."
- "Selecionar valores ou NaN usando uma máscara Booleana (*Boolean mask*)."
---

<!-- 
## Nota sobre Pandas DataFrame/Series

A [DataFrame][pandas-dataframe] is a collection of [Series][pandas-series];
The DataFrame is the way Pandas represents a table, and Series is the data-structure
Pandas use to represent a column.

Pandas is built on top of the [Numpy][numpy] library, which in practice means that
most of the methods defined for Numpy Arrays apply to Pandas Series/DataFrames.

What makes Pandas so attractive is the powerful interface to access individual records
of the table, proper handling of missing values, and relational-databases operations
between DataFrames.
 -->

## Nota sobre Pandas DataFrame/Series

Um [DataFrame][pandas-dataframe] é uma coleção de [Series][pandas-series];
O DataFrame é o jeito do Pandas de representar uma tabela, e uma Series (série) é a estrutura de dados
que o Pandas usa para representar uma linha ou coluna.

O Pandas é construído com base na biblioteca [NumPy][numpy], o que na prática significa que 
a maioria dos métodos definidos para os Arrays NumPy se aplicam para Series/DataFrames Pandas.

O que torna Pandas tão atrativo é a interface poderosa para acessar registros individuais da tabela,
lidar adequadamente com valores faltantes (*missing values*), e operações de banco de dados relacionais entre
DataFrames.

<!-- 
## Selecting values

To access a value at the position `[i,j]` of a DataFrame, we have two options, depending on
what is the meaning of `i` in use.
Remember that a DataFrame provides an *index* as a way to identify the rows of the table;
a row, then, has a *position* inside the table as well as a *label*, which
uniquely identifies its *entry* in the DataFrame.
 -->

## Selecionando Valores

Para acessar um valor na posição `[i,j]` de um DataFrame, temos duas opções, dependendo de 
qual é o significado do `i` em uso.
Lembre-se que o DataFrame provê um **index** como uma forma de identificar as linhas da tabela;
uma linha, portanto, tem uma **posição** dentro da tabela bem como um **label**, que 
identifica unicamente aquela **entrada** no DataFrame.

<!-- 
## Use `DataFrame.iloc[..., ...]` para selecionar os valores por uma posição de um inteiro.

*   Can specify location by numerical index analogously to 2D version of character selection in strings.

~~~
import pandas as pd
data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(df.iloc[0, 0])
~~~
{: .language-python}
~~~
1601.056136
~~~
{: .output}
 -->

## Use `DataFrame.iloc[..., ...]` para selecionar os valores por uma posição de um inteiro.

*   Pode especificar uma localidade por um index numérico, de forma analógica a uma versão 2D de seleção de caracteres em strings.

```python
import pandas as pd
df = pd.read_csv("data/EPE/consumo_anual_energia_por_classe_1995-2018.csv", index_col="ANO")
print(df.iloc[0, 0])
```
~~~
63576.09392
~~~
{: .output}

<!-- 
## Use `DataFrame.loc[..., ...]` to select values by their (entry) label.

*   Can specify location by row name analogously to 2D version of dictionary keys.

~~~
print(df.loc["Albania", "gdpPercap_1952"])
~~~
{: .language-python}
~~~
1601.056136
~~~
{: .output}
 -->

## Use `DataFrame.loc[..., ...]` para selecionar valores por sua label.

```python
print(df.loc[1995, "INDUSTRIAL"])
```

~~~
111626.16092999998
~~~
{: .output}

<!-- 
## Use `:` para se referir a todas as colunas ou todas as linhas.

*   Just like Python's usual slicing notation.

~~~
print(df.loc["Albania", :])
~~~
{: .language-python}
~~~
gdpPercap_1952    1601.056136
gdpPercap_1957    1942.284244
gdpPercap_1962    2312.888958
gdpPercap_1967    2760.196931
gdpPercap_1972    3313.422188
gdpPercap_1977    3533.003910
gdpPercap_1982    3630.880722
gdpPercap_1987    3738.932735
gdpPercap_1992    2497.437901
gdpPercap_1997    3193.054604
gdpPercap_2002    4604.211737
gdpPercap_2007    5937.029526
Name: Albania, dtype: float64
~~~
{: .output}
 -->

## Use `:` para se referir a todas as colunas ou todas as linhas.

*   Assim como a notação de fatias do Python

~~~
print(df.loc[1995, :])
~~~
{: .language-python}
~~~
RESIDENCIAL     63576.09392
INDUSTRIAL     111626.16093
COMERCIAL       32276.26017
OUTROS          35595.69503
Name: 1995, dtype: float64
~~~
{: .output}
<!-- 
*   Would get the same result printing `df.loc["Albania"]` (without a second index).

~~~
print(df.loc[:, "gdpPercap_1952"])
~~~
{: .language-python}
~~~
country
Albania                    1601.056136
Austria                    6137.076492
Belgium                    8343.105127
⋮ ⋮ ⋮
Switzerland               14734.232750
Turkey                     1969.100980
United Kingdom             9979.508487
Name: gdpPercap_1952, dtype: float64
~~~
{: .output}

*   Would get the same result printing `df["gdpPercap_1952"]`
*   Also get the same result printing `df.gdpPercap_1952` (not recommended, because easily confused with `.` notation for methods)
 -->

*   Teríamos o mesmo resultado imprimindo `df.loc[1995]` (sem um segundo index).

```python
print(df.loc[:, "INDUSTRIAL"])
```

~~~
ANO
1995    111626.160930
1996    117127.595430
1997    121717.133000
1998    121979.135500
1999    123892.588420
2000    131278.172050
2001    122538.811220
2002    130927.331740
2003    136220.613000
2004    156320.675381
2005    159662.496549
2006    163180.400829
2007    174368.774000
2008    175834.058410
2009    161798.661500
2010    179478.307300
2011    183575.548000
2012    183424.839240
2013    184684.557000
2014    179105.677880
2015    169562.779620
2016    165602.890200
2017    167711.086710
2018    170041.486550
2019    167403.936870
Name: INDUSTRIAL, dtype: float64
~~~
{: .output}

*   Teria o mesmo resultado com `df["INDUSTRIAL"]`
*   Também podemos ter o mesmo resultado com `df.INDUSTRIAL` (não recomendado, pois pode dar conflito com a notação de `.` para métodos.

<!-- 
## Selecione múltiplas colunas ou linhas usando `DataFrame.loc` e uma fatia nomeada.

~~~
print(df.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'])
~~~
{: .language-python}
~~~
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993
~~~
{: .output}

In the above code, we discover that **slicing usando `loc` is inclusive at both
ends**, which differs from **slicing usando `iloc`**, where slicing indicates
everything up to but not including the final index. 
 -->

## Selecione múltiplas colunas ou linhas usando `DataFrame.loc` e uma fatia nomeada.

```python
print(df.loc[1995: 2002, "INDUSTRIAL":"COMERCIAL"])
```

~~~
        INDUSTRIAL    COMERCIAL
ANO                            
1995  111626.16093  32276.26017
1996  117127.59543  34387.69450
1997  121717.13300  38197.50400
1998  121979.13550  41544.09420
1999  123892.58842  43587.93405
2000  131278.17205  47626.19304
2001  122538.81122  44433.62070
2002  130927.33174  45221.51735
~~~
{: .output}

No código acima, descobrimos que **fatias usando `loc` são inclusivas em ambas extremidades**, diferente de **fatias usando `iloc`**, aonde a fatia indica
tudo até mas sem incluir o último index. 

<!-- 
## O resultado de uma fatia pode ser usado em operações subsequentes.

*   Usually don't just print a slice.
*   All the statistical operators that work on entire dataframes
    work the same way on slices.
*   E.g., calculate max of a slice.

~~~
print(df.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].max())
~~~
{: .language-python}
~~~
gdpPercap_1962    13450.40151
gdpPercap_1967    16361.87647
gdpPercap_1972    18965.05551
dtype: float64
~~~
{: .output}

~~~
print(df.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].min())
~~~
{: .language-python}
~~~
gdpPercap_1962    4649.593785
gdpPercap_1967    5907.850937
gdpPercap_1972    7778.414017
dtype: float64
~~~
{: .output}
 -->

## O resultado de uma fatia pode ser usado em operações subsequentes.

*   Normalmente não fazemos somente a impressão de uma fatia.
*   Todos os operadores estatísticos que atuam no DataFrame 
    funcionam da mesma forma em fatias.
*   E.g., calcular o máximo de uma fatia.

```python
print(df.loc[1995: 2002, "INDUSTRIAL":"COMERCIAL"].max())
```
~~~
INDUSTRIAL    131278.17205
COMERCIAL      47626.19304
dtype: float64
~~~
{: .output}

```python
print(df.loc[1995: 2002, "INDUSTRIAL":"COMERCIAL"].min())
```
~~~
INDUSTRIAL    111626.16093
COMERCIAL      32276.26017
dtype: float64
~~~
{: .output}


<!-- 
## Use comparações para selecionar dados baseados em um valor.

*   Comparison is applied element by element.
*   Returns a similarly-shaped dataframe of `True` and `False`.

~~~
# Use a subset of data to keep output readable.
subset = df.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('Subset of data:\n', subset)

# Which values were greater than 10000 ?
print('\nWhere are values large?\n', subset > 10000)
~~~
{: .language-python}
~~~
Subset of data:
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993

Where are values large?
            gdpPercap_1962 gdpPercap_1967 gdpPercap_1972
country
Italy                False           True           True
Montenegro           False          False          False
Netherlands           True           True           True
Norway                True           True           True
Poland               False          False          False
~~~
{: .output}
 -->

## Use comparações para selecionar dados baseados em um valor.

*   A comparação é aplicada elemento por elemento.
*   Retorna um DataFrame com o mesmo shape, mas de `True` e `False`.

~~~
# Use um subset de dados para manter os dados legíveis
subset = df.loc['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('Subset de dados:\n', subset)

# Que valores são maiores que 100000 ?
print('\nQue valores são grandes?\n', subset > 100000)
~~~
{: .language-python}
~~~
Subset de dados:
        INDUSTRIAL    COMERCIAL
ANO                            
1995  111626.16093  32276.26017
1996  117127.59543  34387.69450
1997  121717.13300  38197.50400
1998  121979.13550  41544.09420
1999  123892.58842  43587.93405
2000  131278.17205  47626.19304
2001  122538.81122  44433.62070
2002  130927.33174  45221.51735

Que valores são grandes?
      INDUSTRIAL  COMERCIAL
ANO                        
1995        True      False
1996        True      False
1997        True      False
1998        True      False
1999        True      False
2000        True      False
2001        True      False
2002        True      False
~~~
{: .output}

<!-- 
## Selecionar valores ou NaN usando uma máscara Booleana (*Boolean mask*).

*   A frame full of Booleans is sometimes called a *mask* because of how it can be used.

~~~
mask = subset > 10000
print(subset[mask])
~~~
{: .language-python}
~~~
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy                   NaN     10022.40131     12269.27378
Montenegro              NaN             NaN             NaN
Netherlands     12790.84956     15363.25136     18794.74567
Norway          13450.40151     16361.87647     18965.05551
Poland                  NaN             NaN             NaN
~~~
{: .output}

*   Get the value where the mask is true, and NaN (Not a Number) where it is false.
*   Useful because NaNs are ignored by operations like max, min, average, etc.

~~~
print(subset[subset > 10000].describe())
~~~
{: .language-python}
~~~
       gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
count        2.000000        3.000000        3.000000
mean     13120.625535    13915.843047    16676.358320
std        466.373656     3408.589070     3817.597015
min      12790.849560    10022.401310    12269.273780
25%      12955.737547    12692.826335    15532.009725
50%      13120.625535    15363.251360    18794.745670
75%      13285.513523    15862.563915    18879.900590
max      13450.401510    16361.876470    18965.055510
~~~
{: .output}
 -->

## Selecionar valores ou NaN usando uma máscara Booleana (*Boolean mask*).

*   Um frame cheio de valores Booleanos também é chamado de *mask* por causa de como pode ser usado:

```python
mask = subset > 100000
print(subset[mask])
```

~~~
	INDUSTRIAL	COMERCIAL
ANO		
1995	111626.16093	NaN
1996	117127.59543	NaN
1997	121717.13300	NaN
1998	121979.13550	NaN
1999	123892.58842	NaN
2000	131278.17205	NaN
2001	122538.81122	NaN
2002	130927.33174	NaN
~~~
{: .output}

*   Retorna o valor aonde a condição é verdadeira, e NaN (*Not a Number*) aonde é falsa.
*   Útil por que NaNs são ignorados por operações como max, min, average, etc.

```python
print(subset[subset > 100000].describe())
```

~~~
          INDUSTRIAL  COMERCIAL
count       8.000000        0.0
mean   122635.866036        NaN
std      6523.108861        NaN
min    111626.160930        NaN
25%    120569.748608        NaN
50%    122258.973360        NaN
75%    125651.274250        NaN
max    131278.172050        NaN
~~~
{: .output}

<!-- 
## Group By: split-apply-combine

Pandas vectorizing methods and grouping operations are features that provide users 
much flexibility to analyse their df.

For instance, let's say we want to have a clearer view on how the European countries 
split themselves according to their GDP.

1.  We may have a glance by splitting the countries in two groups during the years surveyed,
    those who presented a GDP *higher* than the European average and those with a *lower* GDP.
2.  We then estimate a *wealthy score* based on the historical (from 1962 to 2007) values,
    where we account how many times a country has participated in the groups of *lower* or *higher* GDP

~~~
mask_higher = data > df.mean()
wealth_score = mask_higher.aggregate('sum', axis=1) / len(df.columns)
wealth_score
~~~
{: .language-python}
~~~
country
Albania                   0.000000
Austria                   1.000000
Belgium                   1.000000
Bosnia and Herzegovina    0.000000
Bulgaria                  0.000000
Croatia                   0.000000
Czech Republic            0.500000
Denmark                   1.000000
Finland                   1.000000
France                    1.000000
Germany                   1.000000
Greece                    0.333333
Hungary                   0.000000
Iceland                   1.000000
Ireland                   0.333333
Italy                     0.500000
Montenegro                0.000000
Netherlands               1.000000
Norway                    1.000000
Poland                    0.000000
Portugal                  0.000000
Romania                   0.000000
Serbia                    0.000000
Slovak Republic           0.000000
Slovenia                  0.333333
Spain                     0.333333
Sweden                    1.000000
Switzerland               1.000000
Turkey                    0.000000
United Kingdom            1.000000
dtype: float64
~~~
{: .output}

Finally, for each group in the `wealth_score` table, we sum their (financial) contribution
across the years surveyed usando chained methods:

~~~
df.groupby(wealth_score).sum()
~~~
{: .language-python}
~~~
          gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
0.000000    36916.854200    46110.918793    56850.065437    71324.848786   
0.333333    16790.046878    20942.456800    25744.935321    33567.667670   
0.500000    11807.544405    14505.000150    18380.449470    21421.846200   
1.000000   104317.277560   127332.008735   149989.154201   178000.350040   

          gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
0.000000    88569.346898   104459.358438   113553.768507   119649.599409   
0.333333    45277.839976    53860.456750    59679.634020    64436.912960   
0.500000    25377.727380    29056.145370    31914.712050    35517.678220   
1.000000   215162.343140   241143.412730   263388.781960   296825.131210   

          gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007  
0.000000    92380.047256   103772.937598   118590.929863   149577.357928  
0.333333    67918.093220    80876.051580   102086.795210   122803.729520  
0.500000    36310.666080    40723.538700    45564.308390    51403.028210  
1.000000   315238.235970   346930.926170   385109.939210   427850.333420
~~~
{: .output}
 -->
<!-- 
## Group By: divide-aplique-combine

Os métodos de vetorização e operações de agregação do Pandas são funcionalidades que provém os usuários de muita flexibilidade para analisar seu DataFrame.

For instance, let's say we want to have a clearer view on how the European countries 
split themselves according to their GDP.

1.  We may have a glance by splitting the countries in two groups during the years surveyed,
    those who presented a GDP *higher* than the European average and those with a *lower* GDP.
2.  We then estimate a *wealthy score* based on the historical (from 1962 to 2007) values,
    where we account how many times a country has participated in the groups of *lower* or *higher* GDP

~~~
mask_higher = data > df.mean()
wealth_score = mask_higher.aggregate('sum', axis=1) / len(df.columns)
wealth_score
~~~
{: .language-python}
~~~
country
Albania                   0.000000
Austria                   1.000000
Belgium                   1.000000
Bosnia and Herzegovina    0.000000
Bulgaria                  0.000000
Croatia                   0.000000
Czech Republic            0.500000
Denmark                   1.000000
Finland                   1.000000
France                    1.000000
Germany                   1.000000
Greece                    0.333333
Hungary                   0.000000
Iceland                   1.000000
Ireland                   0.333333
Italy                     0.500000
Montenegro                0.000000
Netherlands               1.000000
Norway                    1.000000
Poland                    0.000000
Portugal                  0.000000
Romania                   0.000000
Serbia                    0.000000
Slovak Republic           0.000000
Slovenia                  0.333333
Spain                     0.333333
Sweden                    1.000000
Switzerland               1.000000
Turkey                    0.000000
United Kingdom            1.000000
dtype: float64
~~~
{: .output}

Finally, for each group in the `wealth_score` table, we sum their (financial) contribution
across the years surveyed usando chained methods:

~~~
df.groupby(wealth_score).sum()
~~~
{: .language-python}
~~~
          gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
0.000000    36916.854200    46110.918793    56850.065437    71324.848786   
0.333333    16790.046878    20942.456800    25744.935321    33567.667670   
0.500000    11807.544405    14505.000150    18380.449470    21421.846200   
1.000000   104317.277560   127332.008735   149989.154201   178000.350040   

          gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
0.000000    88569.346898   104459.358438   113553.768507   119649.599409   
0.333333    45277.839976    53860.456750    59679.634020    64436.912960   
0.500000    25377.727380    29056.145370    31914.712050    35517.678220   
1.000000   215162.343140   241143.412730   263388.781960   296825.131210   

          gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007  
0.000000    92380.047256   103772.937598   118590.929863   149577.357928  
0.333333    67918.093220    80876.051580   102086.795210   122803.729520  
0.500000    36310.666080    40723.538700    45564.308390    51403.028210  
1.000000   315238.235970   346930.926170   385109.939210   427850.333420
~~~
{: .output}
 -->

> ## Seleção de Valores Individuais
>
> Escreva uma expressão para os seguintes valores:
>
> 1. Consumo do setor 'Industrial' em 2002.
> 2. Consumo do setor 'Comercial' durante 2000-2010.
> 3. Consumo dos setores 'Residencial' e 'Outros' no ano 2000.
> 4. Consumo do setor 'Outros' em todos os anos.
> 
> > ## Solução
> > 1. `df.loc[2002, "Industrial"]`
> > 2. `df.loc[2000:2010, "Comercial"]`
> > 3. `df.loc[2000, ["Residencial", "Outros"]]`
> > 4. `df["Outros"]` ou `df.loc[:, "Outros"]`
> {: .solution}
{: .challenge}

> ## Extensão de uma Fatia
>
> 1.  As duas declarações abaixo imprimem a mesma coisa?
> 2.  Baseado nisso, que regra governa o que é incluído (ou não) em fatias numéricas e nomeadas no Pandas?
> 
> ~~~
> print(df.iloc[0:2, 0:2])
> print(df.loc[1995:1997, "RESIDENCIAL":"COMERCIAL"])
> ~~~
> {: .language-python}
> 
> > ## Solução
> > Não, não produzem a mesma saída. A primeira declaração imprime:
> > ~~~
> >       RESIDENCIAL    INDUSTRIAL
> > ANO                            
> > 1995  63576.09392  111626.16093
> > 1996  68581.28330  117127.59543
> > ~~~
> >{: .output}
> > E a segunda imprime:
> > ~~~
> >       RESIDENCIAL    INDUSTRIAL    COMERCIAL
> > ANO                                         
> > 1995  63576.09392  111626.16093  32276.26017
> > 1996  68581.28330  117127.59543  34387.69450
> > 1997  74089.15430  121717.13300  38197.50400
> > ~~~
> >{: .output}
> > A fatia com `iloc` **omite** o valor do fim, enquanto a com `loc` **inclui** o valor do fim.
> {: .solution}
{: .challenge}
<!-- 
> ## Reconstructing Data
>
> Explain what each line in the following short program does:
> what is in `first`, `second`, etc.?
>
> ~~~
> first = pd.read_csv('data/gapminder_all.csv', index_col='country')
> second = first[first['continent'] == 'Americas']
> third = second.drop('Puerto Rico')
> fourth = third.drop('continent', axis = 1)
> fourth.to_csv('result.csv')
> ~~~
> {: .language-python}
>
> > ## Solution
> > Let's go through this piece of code line by line.
> > ~~~
> > first = pd.read_csv('data/gapminder_all.csv', index_col='country')
> > ~~~
> > {: .language-python}
> > This line loads the dataset containing the GDP data from all countries into a dataframe called 
> > `first`. The `index_col='country'` parameter selects which column to use as the 
> > row labels in the dataframe.  
> > ~~~
> > second = first[first['continent'] == 'Americas']
> > ~~~
> > {: .language-python}
> > This line makes a selection: only those rows of `first` for which the 'continent' column matches 
> > 'Americas' are extracted. Notice how the Boolean expression inside the brackets, 
> > `first['continent'] == 'Americas'`, is used to select only those rows where the expression is true. 
> > Try printing this expression! Can you print also its individual True/False elements? 
> > (hint: first assign the expression to a variable)
> > ~~~
> > third = second.drop('Puerto Rico')
> > ~~~
> > {: .language-python}
> > As the syntax suggests, this line drops the row from `second` where the label is 'Puerto Rico'. The 
> > resulting dataframe `third` has one row less than the original dataframe `second`.
> > ~~~
> > fourth = third.drop('continent', axis = 1)
> > ~~~
> > {: .language-python}
> > Again we apply the drop function, but in this case we are dropping not a row but a whole column. 
> > To accomplish this, we need to specify also the `axis` parameter (we want to drop the second column 
> > which has index 1).
> > ~~~
> > fourth.to_csv('result.csv')
> > ~~~
> > {: .language-python}
> > The final step is to write the data that we have been working on to a csv file. Pandas makes this easy 
> > with the `to_csv()` function. The only required argument to the function is the filename. Note that the 
> > file will be written in the directory from which you started the Jupyter or Python session.
> {: .solution}
{: .challenge}
 -->

> ## Selecionando Índices
>
> Explique em termos simples o que `idxmin` e `idxmax` fazem no programa abaixo.
> Quando usaríamos esses métodos?
>
> ~~~
> df = pd.read_csv("../data/EPE/consumo_anual_energia_por_classe_1995-2018.csv", index_col="ANO")
> print(df.idxmin())
> print(df.idxmax())
> ~~~
> {: .language-python}
>
> > ## Solução
> > Para cada coluna em `df`, `idxmin` vai retornar o index correspondo ao valor mínimo da coluna.
> > `idxmax` vai fazer o mesmo, mas com o valor máximo.
> >
> > Podemos usar essas funções sempre que quisermos pegar o index da linha do valor mínimo/máximo e não o valor mínimo/máximo em si.
> {: .solution}
{: .challenge}
<!-- 
> ## Practice with Selection
>
> Assume Pandas has been imported and the Gapminder GDP data for Europe has been loaded.
> Write an expression to select each of the following:
>
> 1.  GDP per capita for all countries in 1982.
> 2.  GDP per capita for Denmark for all years.
> 3.  GDP per capita for all countries for years *after* 1985.
> 4.  GDP per capita for each country in 2007 as a multiple of 
>     GDP per capita for that country in 1952.
>
> > ## Solution
> > 1:
> > ~~~
> > df['gdpPercap_1982']
> > ~~~
> > {: .language-python}
> >
> > 2:
> > ~~~
> > df.loc['Denmark',:]
> > ~~~
> > {: .language-python}
> >
> > 3:
> > ~~~
> > df.loc[:,'gdpPercap_1985':]
> > ~~~
> > {: .language-python}
> > Pandas is smart enough to recognize the number at the end of the column label and does not give you an error, although no column named `gdpPercap_1985` actually exists. This is useful if new columns are added to the CSV file later.
> >
> > 4:
> > ~~~
> > df['gdpPercap_2007']/df['gdpPercap_1952']
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Muitas Formas de Acesso
>
> Existem pelo menos duas formas de acessar um valor ou fatia de um DataFrame: por nome ou por index (posição).
> No entanto, existem muitas outras. Por exemplo, uma única coluna ou linha pode ser acessada tanto como `DataFrame` quanto
> como um objeto do tipo `Series`.
>
> Sugira diferentes formas de fazer o seguinte:
> 1. Acessar uma única coluna
> 2. Acessar uma única linha
> 3. Acessar um elemento individual do DataFrame
> 4. Acessar muitas colunas
> 5. Acessar muitas linhas
> 6. Acessar um subset de linhas e colunas específicas
> 7. Acessar um subset de intervalos específicos de linhas e colunas
>
> > ## Solução
> > 1\. Acessar uma única coluna
> > ~~~
> > # por nome
> > df["nome_coluna"]   # como Series
> > df[["nome_coluna"]] # como DataFrame
> >
> > # por nome usando .loc
> > df.T.loc["nome_coluna"]  # como Series
> > df.T.loc[["nome_coluna"]].T  # como DataFrame
> >
> > # notação de ponto (Series)
> > df.nome_coluna
> >
> > # por index (iloc)
> > df.iloc[:, col_index]   # como Series
> > df.iloc[:, [col_index]] # como DataFrame
> >
> > # usando a mask
> > df.T[df.T.index == "nome_coluna"].T
> > ~~~
> > {: .language-python}
> >
> > 2\. Acessar uma única linha
> > ~~~
> > # por nome usando .loc
> > df.loc["nome_linha"] # como Series
> > df.loc[["nome_linha"]] # como DataFrame
> >
> > # por nome
> > df.T["nome_linha"] # como Series
> > df.T[["nome_linha"]].T como DataFrame
> >
> > # por index
> > df.iloc[row_index]   # como Series
> > df.iloc[[row_index]]   # como DataFrame
> >
> > # usando mask
> > df[df.index == "nome_linha"]
> > ~~~
> > {: .language-python}
> >
> > 3\. Acessar um elemento individual do DataFrame
> > ~~~
> > # por nome de linha/coluna
> > df["nome_coluna"]["nome_linha"]         # como Series
> >
> > df[["nome_coluna"]].loc["nome_linha"]  # como Series
> > df[["nome_coluna"]].loc[["nome_linha"]]  # como DataFrame
> >
> > df.loc["nome_linha"]["nome_coluna"]  # como um valor
> > df.loc[["nome_linha"]]["nome_coluna"]  # como Series
> > df.loc[["nome_linha"]][["nome_coluna"]]  # como DataFrame
> >
> > df.loc["nome_linha", "nome_coluna"]  # como um valor
> > df.loc[["nome_linha"], "nome_coluna"]  # como Series.
> > df.loc["nome_linha", ["nome_coluna"]]  # como Series.
> > df.loc[["nome_linha"], ["nome_coluna"]]  # como DataFrame
> >
> > # por nome de linha/coluna: notação de ponto
> > df.nome_coluna.nome_linha
> >
> > # por index de linha/coluna
> > df.iloc[row_index, col_index] # como um valor
> > df.iloc[[row_index], col_index] # como Series.
> > df.iloc[row_index, [col_index]] # como Series.
> > df.iloc[[row_index], [col_index]] # como DataFrame
> >
> > # column name + row index
> > df["nome_coluna"][row_index]
> > df.nome_coluna[row_index]
> > df["nome_coluna"].iloc[row_index]
> >
> > # column index + row name
> > df.iloc[:, [col_index]].loc["nome_linha"]  # como Series
> > df.iloc[:, [col_index]].loc[["nome_linha"]]  # como DataFrame
> >
> > # usando masks
> > df[df.index == "nome_linha"].T[df.T.index == "nome_coluna"].T
> > ~~~
> > {: .language-python}
> > 4\. Acessar muitas colunas
> > ~~~
> > # por nome
> > df[["col1", "col2", "col3"]]
> > df.loc[:, ["col1", "col2", "col3"]]
> >
> > # por index
> > df.iloc[:, [col1_index, col2_index, col3_index]]
> > ~~~
> > {: .language-python}
> > 5\. Acessar muitas linhas
> > ~~~
> > # por nome
> > df.loc[["row1", "row2", "row3"]]
> >
> > # por index
> > df.iloc[[row1_index, row2_index, row3_index]]
> > ~~~
> > {: .language-python}
> > 6\. Acessar um subset de linhas e colunas específicas
> > ~~~
> > # por nomes
> > df.loc[["row1", "row2", "row3"], ["col1", "col2", "col3"]]
> >
> > # by indices
> > df.iloc[[row1_index, row2_index, row3_index], [col1_index, col2_index, col3_index]]
> >
> > # column names + row indices
> > df[["col1", "col2", "col3"]].iloc[[row1_index, row2_index, row3_index]]
> >
> > # column indices + row names
> > df.iloc[:, [col1_index, col2_index, col3_index]].loc[["row1", "row2", "row3"]]
> > ~~~
> > {: .language-python}
> > 7\. Acessar um subset de intervalos específicos de linhas e colunas
> > ~~~
> > # por nome
> > df.loc["row1":"row2", "col1":"col2"]
> >
> > # por index
> > df.iloc[row1_index:row2_index, col1_index:col2_index]
> >
> > # column names + row indices
> > df.loc[:, "col1_name":"col2_name"].iloc[row1_index:row2_index]
> >
> > # column indices + row names
> > df.iloc[:, col1_index:col2_index].loc["row1":"row2"]
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Explorando métodos disponíveis usando a função `dir()`
>
> Python inclui a função `dir()` que pode ser usada para mostrar todos os métodos (funções) disponíveis em um dado objeto. Já usamos alguns métodos com as strings e listas. Podemos ver que existem muitos métodos de string usando `dir()`:
>
> ~~~
> minha_string = "Olá Mundo!"
> dir(minha_string)
> ~~~
> {: .language-python}
>
> Esse comando retorna:
>
> ~~~
> ['__add__',
> ...
> '__subclasshook__',
> 'capitalize',
> 'casefold',
> 'center',
> ...
> 'upper',
> 'zfill']
> ~~~
> {: .language-python}
>
> Você pode usar o `help()` ou <kbd>Shift</kbd>+<kbd>Tab</kbd> para obter mais informações sobre o que esses métodos fazem.
>
> Use o `dir` para encontrar o método que traz o valor da mediana para as colunas do DataFrame.
> 
> > ## Solução
> > Podemos ver que existe um método `median` no DataFrame, então podemos rodar:
> > ~~~
> > df.median()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

[pandas-dataframe]: https://pandas.pydf.org/pandas-docs/stable/generated/pandas.DataFrame.html
[pandas-series]: https://pandas.pydf.org/pandas-docs/stable/generated/pandas.Series.html
[numpy]: http://www.numpy.org/
