---
title: "Lendo Dados Tabulares"
teaching: 10
exercises: 10
questions:
- "Como posso ler dados tabulares?"
objectives:
- "Importe a biblioteca Pandas."
- "Use Pandas para carregar um arquivo CSV simples."
- "Consiga informações básicas sobre um DataFrame Pandas."
keypoints:
- "Use a biblioteca Pandas para conseguir estatísticas básicas de dados tabulares."
- "Use `index_col` para especificar os valores de uma coluna que devem ser usados como nomes de linha."
- "Use `DataFrame.info` para saber mais sobre um dataframe."
- "Use `DataFrame.columns` para acessar o nome das colunas de um dataframe."
- "Use `DataFrame.T` para transpôr um dataframe."
- "Use `DataFrame.describe` para conseguir um sumário de estatísticas sobre os dados."
---

<!-- 
## Use the Pandas library to do statistics on tabular data.

*   Pandas is a widely-used Python library for statistics, particularly on tabular data.
*   Borrows many features from R's dataframes.
    *   A 2-dimensional table whose columns have names
        and potentially have different data types.
*   Load it with `import pandas as pd`. The alias pd is commonly used for Pandas.
*   Read a Comma Separated Values (CSV) data file with `pd.read_csv`.
    *   Argument is the name of the file to be read.
    *   Assign result to a variable to store the data that was read.
 -->

## Use a biblioteca Pandas para conseguir estatísticas básicas de dados tabulares.

*   Pandas is a widely-used Python library for statistics, particularly on tabular data.
*   Borrows many features from R's dataframes.
    *   A 2-dimensional table whose columns have names
        and potentially have different data types.
*   Load it with `import pandas as pd`. The alias pd is commonly used for Pandas.
*   Read a Comma Separated Values (CSV) data file with `pd.read_csv`.
    *   Argument is the name of the file to be read.
    *   Assign result to a variable to store the data that was read.

<!-- 
~~~
import pandas as pd

data = pd.read_csv('data/gapminder_gdp_oceania.csv')
print(data)
~~~
{: .language-python}
~~~
       country  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
0    Australia     10039.59564     10949.64959     12217.22686
1  New Zealand     10556.57566     12247.39532     13175.67800

   gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
0     14526.12465     16788.62948     18334.19751     19477.00928
1     14463.91893     16046.03728     16233.71770     17632.41040

   gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
0     21888.88903     23424.76683     26997.93657     30687.75473
1     19007.19129     18363.32494     21050.41377     23189.80135

   gdpPercap_2007
0     34435.36744
1     25185.00911
~~~
{: .output}
 -->

```python
import pandas as pd

dados = pd.read_csv("data/EPE/consumo_anual_energia_por_classe_1995-2018.csv")
print(dados)
```

~~~
     ANO   RESIDENCIAL     INDUSTRIAL     COMERCIAL        OUTROS
0   1995   63576.09392  111626.160930  32276.260170  35595.695030
1   1996   68581.28330  117127.595430  34387.694500  37233.735790
2   1997   74089.15430  121717.133000  38197.504000  39276.171000
3   1998   79340.00033  121979.135500  41544.094200  41658.909370
4   1999   81291.21490  123892.588420  43587.934050  43416.389640
5   2000   83613.37360  131278.172050  47626.193040  45011.033780
6   2001   73622.20572  122538.811220  44433.620700  42662.689790
7   2002   72718.30670  130927.331740  45221.517350  44359.280450
8   2003   76162.17000  136220.613000  47531.450000  47072.530000
9   2004   78470.11008  156320.675381  49685.887970  47388.500200
10  2005   82644.25645  159662.496549  53034.562150  49994.944560
11  2006   85783.82576  163180.400829  55368.739280  51796.349690
12  2007   89885.37200  174368.774000  58647.003000  54128.865000
13  2008   94746.38880  175834.058410  61812.900370  56079.051400
14  2009  100776.17000  161798.661500  65254.562000  56476.986850
15  2010  107214.67000  179478.307300  69169.996600  59804.783760
16  2011  111970.66600  183575.548000  73481.523000  63987.896860
17  2012  117645.84953  183424.839240  79226.355630  67829.346450
18  2013  124907.96200  184684.557000  83703.880000  69846.094630
19  2014  132301.85000  179105.677880  89840.459000  73575.467010
20  2015  131189.76807  169562.779620  90767.540860  74467.067500
21  2016  132872.08500  165602.890200  87872.838000  75720.961980
22  2017  134368.49800  167711.086710  88292.490000  77102.658050
23  2018  137614.94413  170041.486550  88630.604791  78949.742660
24  2019  141929.62902  167403.936870  92172.590812  80577.342739
~~~
{: .output}

<!-- 
*   The columns in a dataframe are the observed variables, and the rows are the observations.
*   Pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.
 -->

*   As colunas de um dataframe são as variáveis observadas, e as linhas são as observações.
*   Esse dataframe contém o consumo anual de energia (em GWh) por classe (fonte: [EPE](../data/README.md)).

<!-- 
> ## File Not Found
>
> Our lessons store their data files in a `data` sub-directory,
> which is why the path to the file is `data/gapminder_gdp_oceania.csv`.
> If you forget to include `data/`,
> or if you include it but your copy of the file is somewhere else,
> you will get a [runtime error]({{ page.root }}/04-built-in/#runtime-error)
> that ends with a line like this:
>
> ~~~
> FileNotFoundError: [Errno 2] No such file or directory: 'data/gapminder_gdp_oceania.csv'
> ~~~
> {: .error}
{: .callout}
 -->

> ## Arquivo Não Encontrado
>
> Nossas aulas guardam os arquivos em um diretório `data/`
> e por isso o caminho do arquivo é `data/EPE/consumo_anual_energia_por_classe_1995-2018.csv`
> Se você não incluir o `data/EPE`,
> ou colocar um **caminho de arquivo** inválido, vai receber um erro
> parecido com este:
> ~~~
> FileNotFoundError: [Errno 2] No such file or directory: 'data/consumo_anual_energia_por_classe_1995-2018.csv'
> ~~~
> {: .error}
{: .callout}

<!-- 
## Use `index_col` to specify that a column's values should be used as row headings.

*   Row headings are numbers (0 and 1 in this case).
*   Really want to index by country.
*   Pass the name of the column to `read_csv` as its `index_col` parameter to do this.
 -->

## Use `index_col` para especificar os valores de uma coluna que devem ser usados como nomes de linha.

*   Nomes de linha são números (começando do 0).
*   Queremos indexar pelo ano.
*   Passe o nome OU posição da coluna para `read_csv` como parâmetro para `index_col` para fazer isso: 

<!-- 
~~~
data = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
print(data)
~~~
{: .language-python}
~~~
             gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
country
Australia       10039.59564     10949.64959     12217.22686     14526.12465
New Zealand     10556.57566     12247.39532     13175.67800     14463.91893

             gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
country
Australia       16788.62948     18334.19751     19477.00928     21888.88903
New Zealand     16046.03728     16233.71770     17632.41040     19007.19129

             gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007
country
Australia       23424.76683     26997.93657     30687.75473     34435.36744
New Zealand     18363.32494     21050.41377     23189.80135     25185.00911
~~~
{: .output}
 -->

```python
dados = pd.read_csv("../data/EPE/consumo_anual_energia_por_classe_1995-2018.csv", index_col="ANO")

print(dados)
```
~~~
       RESIDENCIAL     INDUSTRIAL     COMERCIAL        OUTROS
ANO                                                          
1995   63576.09392  111626.160930  32276.260170  35595.695030
1996   68581.28330  117127.595430  34387.694500  37233.735790
1997   74089.15430  121717.133000  38197.504000  39276.171000
1998   79340.00033  121979.135500  41544.094200  41658.909370
1999   81291.21490  123892.588420  43587.934050  43416.389640
2000   83613.37360  131278.172050  47626.193040  45011.033780
2001   73622.20572  122538.811220  44433.620700  42662.689790
2002   72718.30670  130927.331740  45221.517350  44359.280450
2003   76162.17000  136220.613000  47531.450000  47072.530000
2004   78470.11008  156320.675381  49685.887970  47388.500200
2005   82644.25645  159662.496549  53034.562150  49994.944560
2006   85783.82576  163180.400829  55368.739280  51796.349690
2007   89885.37200  174368.774000  58647.003000  54128.865000
2008   94746.38880  175834.058410  61812.900370  56079.051400
2009  100776.17000  161798.661500  65254.562000  56476.986850
2010  107214.67000  179478.307300  69169.996600  59804.783760
2011  111970.66600  183575.548000  73481.523000  63987.896860
2012  117645.84953  183424.839240  79226.355630  67829.346450
2013  124907.96200  184684.557000  83703.880000  69846.094630
2014  132301.85000  179105.677880  89840.459000  73575.467010
2015  131189.76807  169562.779620  90767.540860  74467.067500
2016  132872.08500  165602.890200  87872.838000  75720.961980
2017  134368.49800  167711.086710  88292.490000  77102.658050
2018  137614.94413  170041.486550  88630.604791  78949.742660
2019  141929.62902  167403.936870  92172.590812  80577.342739
~~~
{: .output}

<!-- 
~~~
data.info()
~~~
{: .language-python}
~~~
<class 'pandas.core.frame.DataFrame'>
Index: 2 entries, Australia to New Zealand
Data columns (total 12 columns):
gdpPercap_1952    2 non-null float64
gdpPercap_1957    2 non-null float64
gdpPercap_1962    2 non-null float64
gdpPercap_1967    2 non-null float64
gdpPercap_1972    2 non-null float64
gdpPercap_1977    2 non-null float64
gdpPercap_1982    2 non-null float64
gdpPercap_1987    2 non-null float64
gdpPercap_1992    2 non-null float64
gdpPercap_1997    2 non-null float64
gdpPercap_2002    2 non-null float64
gdpPercap_2007    2 non-null float64
dtypes: float64(12)
memory usage: 208.0+ bytes
~~~
{: .output}
 -->
 ## Use `DataFrame.info()` para saber mais sobre um dataframe.

```python
dados.info()
```

~~~
<class 'pandas.core.frame.DataFrame'>
Int64Index: 25 entries, 1995 to 2019
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   RESIDENCIAL  25 non-null     float64
 1   INDUSTRIAL   25 non-null     float64
 2   COMERCIAL    25 non-null     float64
 3   OUTROS       25 non-null     float64
dtypes: float64(4)
memory usage: 1000.0 bytes
~~~
{: .output}

<!-- 
*   This is a `DataFrame`
*   Two rows named `'Australia'` and `'New Zealand'`
*   Twelve columns, each of which has two actual 64-bit floating point values.
    *   We will talk later about null values, which are used to represent missing observations.
*   Uses 208 bytes of memory.
 -->

*   Isso é um `DataFrame`.
*   Temos 25 linhas, de `1995` and `2019`
*   Quatro colunas, todas do tipo `float` de 64 bits.
    *   Depois também vamos falar de valores nulos.
*   Usa 1000 bytes de memória.

<!-- 
## The `DataFrame.columns` variable stores information about the dataframe's columns.

*   Note that this is data, *not* a method.  (It doesn't have parentheses.)
    *   Like `math.pi`.
    *   So do not use `()` to try to call it.
*   Called a *member variable*, or just *member*.
 -->

## Use `DataFrame.columns` para acessar o nome das colunas de um dataframe.

*   Note que isso são dados, **não** um método (não tem parênteses).
    *   Como `math.pi`.
    *   Não use `()` para tentar "chamá-lo".
*   Chamada uma **variável membro**, ou só **membro**.

```python
print(dados.columns)
```

~~~
Index(['RESIDENCIAL', 'INDUSTRIAL', 'COMERCIAL', 'OUTROS'], dtype='object')
~~~
{: .output}


<!-- 
## Use `DataFrame.T` to transpose a dataframe.

*   Sometimes want to treat columns as rows and vice versa.
*   Transpose (written `.T`) doesn't copy the data, just changes the program's view of it.
*   Like `columns`, it is a member variable.
 -->

## Use `DataFrame.T` para transpôr um dataframe.

*   As vezes queremos tratar colunas como linhas e vice versa.
*   Transpôr (escrito como `.T`) não copia os dados, só muda a visão do programa sobre ele.
*   Assim como `columns`, é uma variável membro.

<!-- 
~~~
print(data.T)
~~~
{: .language-python}
~~~
country           Australia  New Zealand
gdpPercap_1952  10039.59564  10556.57566
gdpPercap_1957  10949.64959  12247.39532
gdpPercap_1962  12217.22686  13175.67800
gdpPercap_1967  14526.12465  14463.91893
gdpPercap_1972  16788.62948  16046.03728
gdpPercap_1977  18334.19751  16233.71770
gdpPercap_1982  19477.00928  17632.41040
gdpPercap_1987  21888.88903  19007.19129
gdpPercap_1992  23424.76683  18363.32494
gdpPercap_1997  26997.93657  21050.41377
gdpPercap_2002  30687.75473  23189.80135
gdpPercap_2007  34435.36744  25185.00911
~~~
{: .output}
 -->

```python
print(dados.T)
```
~~~
ANO                  1995          1996         1997          1998  \
RESIDENCIAL   63576.09392   68581.28330   74089.1543   79340.00033   
INDUSTRIAL   111626.16093  117127.59543  121717.1330  121979.13550   
COMERCIAL     32276.26017   34387.69450   38197.5040   41544.09420   
OUTROS        35595.69503   37233.73579   39276.1710   41658.90937   

ANO                  1999          2000          2001          2002  \
RESIDENCIAL   81291.21490   83613.37360   73622.20572   72718.30670   
INDUSTRIAL   123892.58842  131278.17205  122538.81122  130927.33174   
COMERCIAL     43587.93405   47626.19304   44433.62070   45221.51735   
OUTROS        43416.38964   45011.03378   42662.68979   44359.28045   

ANO                2003           2004  ...          2010          2011  \
RESIDENCIAL   76162.170   78470.110080  ...  107214.67000  111970.66600   
INDUSTRIAL   136220.613  156320.675381  ...  179478.30730  183575.54800   
COMERCIAL     47531.450   49685.887970  ...   69169.99660   73481.52300   
OUTROS        47072.530   47388.500200  ...   59804.78376   63987.89686   

ANO                  2012          2013          2014          2015  \
RESIDENCIAL  117645.84953  124907.96200  132301.85000  131189.76807   
INDUSTRIAL   183424.83924  184684.55700  179105.67788  169562.77962   
COMERCIAL     79226.35563   83703.88000   89840.45900   90767.54086   
OUTROS        67829.34645   69846.09463   73575.46701   74467.06750   

ANO                  2016          2017           2018           2019  
RESIDENCIAL  132872.08500  134368.49800  137614.944130  141929.629020  
INDUSTRIAL   165602.89020  167711.08671  170041.486550  167403.936870  
COMERCIAL     87872.83800   88292.49000   88630.604791   92172.590812  
OUTROS        75720.96198   77102.65805   78949.742660   80577.342739  

[4 rows x 25 columns]
~~~
{: .output}

<!-- 
## Use `DataFrame.describe()` to get summary statistics about data.

`DataFrame.describe()` gets the summary statistics of only the columns that have numerical data. 
All other columns are ignored, unless you use the argument `include='all'`.
~~~
print(data.describe())
~~~
{: .language-python}
~~~
       gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  gdpPercap_1967  \
count        2.000000        2.000000        2.000000        2.000000
mean     10298.085650    11598.522455    12696.452430    14495.021790
std        365.560078      917.644806      677.727301       43.986086
min      10039.595640    10949.649590    12217.226860    14463.918930
25%      10168.840645    11274.086022    12456.839645    14479.470360
50%      10298.085650    11598.522455    12696.452430    14495.021790
75%      10427.330655    11922.958888    12936.065215    14510.573220
max      10556.575660    12247.395320    13175.678000    14526.124650

       gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  gdpPercap_1987  \
count         2.00000        2.000000        2.000000        2.000000
mean      16417.33338    17283.957605    18554.709840    20448.040160
std         525.09198     1485.263517     1304.328377     2037.668013
min       16046.03728    16233.717700    17632.410400    19007.191290
25%       16231.68533    16758.837652    18093.560120    19727.615725
50%       16417.33338    17283.957605    18554.709840    20448.040160
75%       16602.98143    17809.077557    19015.859560    21168.464595
max       16788.62948    18334.197510    19477.009280    21888.889030

       gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  gdpPercap_2007
count        2.000000        2.000000        2.000000        2.000000
mean     20894.045885    24024.175170    26938.778040    29810.188275
std       3578.979883     4205.533703     5301.853680     6540.991104
min      18363.324940    21050.413770    23189.801350    25185.009110
25%      19628.685413    22537.294470    25064.289695    27497.598692
50%      20894.045885    24024.175170    26938.778040    29810.188275
75%      22159.406358    25511.055870    28813.266385    32122.777857
max      23424.766830    26997.936570    30687.754730    34435.367440
~~~
{: .output}

*   Not particularly useful with just two records,
    but very helpful when there are thousands.
 -->

## Use `DataFrame.describe()` para conseguir um sumário de estatísticas sobre os dados.

`DataFrame.describe()` obtém um sumário de estatísticas para todos os dados do tipo numérico.
Todas as outras colunas são ignoradas, a não ser que passemos o argument `include="all"`.

```python
dados.describe()
```


~~~
	RESIDENCIAL	INDUSTRIAL	COMERCIAL	OUTROS
count	25.000000	25.000000	25.000000	25.000000
mean	99092.633904	154362.548693	62470.728059	56560.499768
std	25571.611979	24594.919085	20209.613496	14541.122259
min	63576.093920	111626.160930	32276.260170	35595.695030
25%	78470.110080	130927.331740	45221.517350	44359.280450
50%	89885.372000	163180.400829	58647.003000	54128.865000
75%	124907.962000	174368.774000	83703.880000	69846.094630
max	141929.629020	184684.557000	92172.590812	80577.342739
~~~
{: .output}

*   Muito útil para quando queremos fazer um sumário de muitos dados.

<!-- 
> ## Reading Other Data
>
> Read the data in `gapminder_gdp_americas.csv`
> (which should be in the same directory as `gapminder_gdp_oceania.csv`)
> into a variable called `americas`
> and display its summary statistics.
>
> > ## Solution
> > To read in a CSV, we use `pd.read_csv` and pass the filename `'data/gapminder_gdp_americas.csv'` to it.
> > We also once again pass the column name `'country'` to the parameter `index_col` in order to index by country.
> > The summary statistics can be displayed with the `DataFrame.describe()` method.
> > ~~~
> > americas = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
> > americas.describe()
> > ~~~
> >{: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Lendo Outros Dados
>
> Leia os dados em `balanco_centros_transformacao.csv`
> (que deve estar no mesmo diretório que `consumo_anual.csv`)
> em uma variável chamada `balanco` e rode os métodos `info` e `describe`.
>
> > ## Solução
> > Para ler um arquivo CSV, usamos a função `pd.read_csv` e passamos o nome do arquivo `'data/EPE/balanco_centros_transformacao.csv'`:
> > ```python
> > balanco = pd.read_csv("../data/EPE/balanco_centros_transformacao.csv")
> > balanco.info()
> > balanco.describe()
> > ```
> {: .solution}
{: .challenge}

<!-- 
> ## Inspecting Data
>
> After reading the data for the Americas,
> use `help(americas.head)` and `help(americas.tail)`
> to find out what `DataFrame.head` and `DataFrame.tail` do.
>
> 1.  What method call will display the first three rows of this data?
> 2.  What method call will display the last three columns of this data?
>     (Hint: you may need to change your view of the data.)
>
> > ## Solution
> > 1. We can check out the first five rows of `americas` by executing `americas.head()`
> >    (allowing us to view the head of the DataFrame). We can specify the number of rows we wish
> >    to see by specifying the parameter `n` in our call
> >    to `americas.head()`. To view the first three rows, execute:
> >
> >    ~~~
> >    americas.head(n=3)
> >    ~~~
> >    {: .language-python}
> >    ~~~
> >              continent  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
> >    country
> >    Argentina  Americas     5911.315053     6856.856212     7133.166023
> >    Bolivia    Americas     2677.326347     2127.686326     2180.972546
> >    Brazil     Americas     2108.944355     2487.365989     3336.585802
> >
> >               gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
> >    country
> >    Argentina     8052.953021     9443.038526    10079.026740     8997.897412
> >    Bolivia       2586.886053     2980.331339     3548.097832     3156.510452
> >    Brazil        3429.864357     4985.711467     6660.118654     7030.835878
> >
> >               gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
> >    country
> >    Argentina     9139.671389     9308.418710    10967.281950     8797.640716
> >    Bolivia       2753.691490     2961.699694     3326.143191     3413.262690
> >    Brazil        7807.095818     6950.283021     7957.980824     8131.212843
> >
> >               gdpPercap_2007
> >    country
> >    Argentina    12779.379640
> >    Bolivia       3822.137084
> >    Brazil        9065.800825
> >    ~~~
> >    {: .output}
> > 2. To check out the last three rows of `americas`, we would use the command,
> >    `americas.tail(n=3)`, analogous to `head()` used above. However, here we want to look at
> >    the last three columns so we need to change our view and then use `tail()`. To do so, we
> >     create a new DataFrame in which rows and columns are switched:
> >
> >    ~~~
> >    americas_flipped = americas.T
> >    ~~~
> >    {: .language-python}
> >
> >    We can then view the last three columns of `americas` by viewing the last three rows
> >    of `americas_flipped`:
> >    ~~~
> >    americas_flipped.tail(n=3)
> >    ~~~
> >    {: .language-python}
> >    ~~~
> >    country        Argentina  Bolivia   Brazil   Canada    Chile Colombia  \
> >    gdpPercap_1997   10967.3  3326.14  7957.98  28954.9  10118.1  6117.36
> >    gdpPercap_2002   8797.64  3413.26  8131.21    33329  10778.8  5755.26
> >    gdpPercap_2007   12779.4  3822.14   9065.8  36319.2  13171.6  7006.58
> >
> >    country        Costa Rica     Cuba Dominican Republic  Ecuador    ...     \
> >    gdpPercap_1997    6677.05  5431.99             3614.1  7429.46    ...
> >    gdpPercap_2002    7723.45  6340.65            4563.81  5773.04    ...
> >    gdpPercap_2007    9645.06   8948.1            6025.37  6873.26    ...
> >
> >    country          Mexico Nicaragua   Panama Paraguay     Peru Puerto Rico  \
> >    gdpPercap_1997   9767.3   2253.02  7113.69   4247.4  5838.35     16999.4
> >    gdpPercap_2002  10742.4   2474.55  7356.03  3783.67  5909.02     18855.6
> >    gdpPercap_2007  11977.6   2749.32  9809.19  4172.84  7408.91     19328.7
> >
> >    country        Trinidad and Tobago United States  Uruguay Venezuela
> >    gdpPercap_1997             8792.57       35767.4  9230.24   10165.5
> >    gdpPercap_2002             11460.6       39097.1     7727   8605.05
> >    gdpPercap_2007             18008.5       42951.7  10611.5   11415.8
> >    ~~~
> >    {: .output}
> >    
> >    This shows the data that we want, but we may prefer to display three columns instead of three rows,
> >    so we can flip it back:
> >    ~~~
> >    americas_flipped.tail(n=3).T    
> >    ~~~
> >    {: .language-python}    
> >    __Note:__ we could have done the above in a single line of code by 'chaining' the commands:
> >    ~~~
> >    americas.T.tail(n=3).T
> >    ~~~
> >    {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Inspecionando Dados
>
> Depois de ler os dados de balanço enérgetico,
> use `help(balanco.head)` e `help(balanco.tail)`
> para descobrir o que `DataFrame.head` e `DataFrame.tail` fazem.
>
> 1.  Que método vai mostrar as cinco primeiras linhas dos dados?
> 2.  Que método vai mostrar as cinco últimas linhas dos dados?
> 3.  Como podemos olhar as primeiras 10 ou últimas 10 linhas?
> 4.  Como podemos ver as últimas 3 colunas dos dados?
>
> > ## Solução
> > 1. `balanco.head()`
> > 2. `balanco.tail()`
> > 3. `balanco.head(10)` ou `balanco.tail(10)`
> > 4. `balanco.T.tail(3).T`
> > 
> > ~~~
> > 
> >         2018	        2019	        2020
> > 0	-90904.196102	-91107.647293	-94895.974959
> > 1	35514.63432	34695.791952	35798.423456
> > 2	10838.198217	11709.90988	16763.39577
> > 3	18289.55576	18393.81236	16714.789518
> > 4	18254.2899	18393.81236	16713.09871
> > ...	...	...	...
> > 59	390.575407	432.253552	554.714468
> > 60	2115.552449	2377.459564	2574.294979
> > 61	48475.141214	55985.62168	57050.706316
> > 62	3461.434834	6654.579083	10748.341463
> > 63	388971.075877	397877.056629	396381.195389
> > 64 rows × 3 columns
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Reading Files in Other Directories
>
> The data for your current project is stored in a file called `microbes.csv`,
> which is located in a folder called `dados_consumo_energetico`.
> You are doing analysis in a notebook called `analise.ipynb`
> in a sibling folder called `projeto_regulatorio`:
>
> ~~~
> your_home_directory
> +-- dados_consumo_energetico/
> |   +-- microbes.csv
> +-- projeto_regulatorio/
>     +-- analise.ipynb
> ~~~
> {: .output}
>
> What value(s) should you pass to `read_csv` to read `microbes.csv` in `analise.ipynb`?
> 
> > ## Solution
> > We need to specify the path to the file of interest in the call to `pd.read_csv`. We first need to 'jump' out of
> > the folder `projeto_regulatorio` using '../' and then into the folder `dados_consumo_energetico` using 'dados_consumo_energetico/'. Then we can specify the filename `microbes.csv.
> > The result is as follows:
> > ~~~
> > data_microbes = pd.read_csv('../dados_consumo_energetico/microbes.csv')
> > ~~~
> >{: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Lendo Arquivos de Outros Diretórios
>
> Os dados para o seu projeto atual estão em um arquivo chamado `consumos.csv`,
> que está em uma pasta chamada `dados_consumo_energetico`.
> Você está fazendo análise em um notebook chamado `analise.ipynb`
> em uma pasta irmã chamada `projeto_regulatorio`:
>
> ```
> seu_diretorio_atual
> +-- dados_consumo_energetico/
> |   +-- consumos.csv
> +-- projeto_regulatorio/
>     +-- analise.ipynb
> ```
> 
> Que valores devemos passar para `read_csv` para ler `consumos.csv` em `analise.ipynb`?
> 
> > ## Solução
> > Precisamos especificar o caminho de interesse para passar para `pd.read_csv`. Primeiro precisamos 'sair'
> > da pasta `projeto_regulatorio` usando `'../'`, e então entrar na pasta `dados_consumo_energetico` usando `'dados_consumo_energetico/'`. Podemos então especificar `consumos.csv`:
> > O resultado é o seguinte:
> > ```python
> > dados_consumo = pd.read_csv("../dados_consumo_energetico/consumos.csv")
> > ```
> >
> {: .solution}
{: .challenge}

<!-- 
> ## Writing Data
> 
> As well as the `read_csv` function for reading data from a file,
> Pandas provides a `to_csv` function to write dataframes to files.
> Applying what you've learned about reading from files,
> write one of your dataframes to a file called `processed.csv`.
> You can use `help` to get information on how to use `to_csv`.
> > ## Solution
> > In order to write the DataFrame `americas` to a file called `processed.csv`, execute the following command:
> > ~~~
> > americas.to_csv('processed.csv')
> > ~~~
> >{: .language-python}
> > For help on `to_csv`, you could execute, for example:
> > ~~~
> > help(americas.to_csv)
> > ~~~
> >{: .language-python}
> > Note that `help(to_csv)` throws an error! This is a subtlety and is due to the fact that `to_csv` is NOT a function in 
> > and of itself and the actual call is `americas.to_csv`. 
> {: .solution}
{: .challenge}
 -->

> ## Escrevendo Dados
> 
> Assim como a função `read_csv` lê dados de um arquivo, 
> o Pandas tem a função `to_csv` para escrever dataframes em arquivos.
> Aplicando o que você aprendeu sobre ler de arquivos,
> escreva um dos dataframes em um arquivo chamado `processado.csv`.
> Você pode usar o `help` para obter informação sobre como usar `to_csv`.
> 
> > ## Solução
> > Para escrever o dataframe `balanco` em um arquivo chamado `processado.csv`, execute o seguinte comando:
> > ```python
> > balancos.to_csv('processed.csv')
> > ```
> > Para obter ajuda sobre `to_csv`, você pode usar `help(balanco.to_csv)`.
> > Note que `help(to_csv)` nos dá um erro! Isso é uma sutileza devido ao fato de que `to_csv` NÃO é uma função por si só e sim um método do DataFrame, por isso `balanco.to_csv`. 
> {: .solution}
{: .challenge}
