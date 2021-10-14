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
df = pd.concat(dataframes, axis=1)
df.head()
```
~~~
ANO   COMERCIAL	INDUSTRIAL	RESIDENCIAL	OUTROS				
1995	32276.26017	111626.16093	63576.09392	35595.69503
1996	34387.69450	117127.59543	68581.28330	37233.73579
1997	38197.50400	121717.13300	74089.15430	39276.17100
1998	41544.09420	121979.13550	79340.00033	41658.90937
1999	43587.93405	123892.58842	81291.21490	43416.38964
~~~
{: .output}

> ## Combinando dados
>
> Na nossa pasta de dados, temos medições de energia da PJM para a EKPC - Eastern Kentucky Power Company.
> Esses dados estão divididos por ano. Use o `glob` e `pd.concat` para juntar todos os dados em um único DataFrame.
> **Dica:** copie o exemplo acima, mas omita os parâmetros `index_col` e `axis`.
## Solução

## Writing Out Data to CSV


# Joining DataFrames

When we concatenated our DataFrames we simply added them to each other -
stacking them either vertically or side by side. Another way to combine
DataFrames is to use columns in each dataset that contain common values (a
common unique id). Combining DataFrames using a common field is called
"joining". The columns containing the common values are called "join key(s)".
Joining DataFrames in this way is often useful when one DataFrame is a "lookup
table" containing additional data that we want to include in the other.

NOTE: This process of joining tables is similar to what we do with tables in an
SQL database.

For example, the `species.csv` file that we've been working with is a lookup
table. This table contains the genus, species and taxa code for 55 species. The
species code is unique for each line. These species are identified in our survey
data as well using the unique species code. Rather than adding 3 more columns
for the genus, species and taxa to each of the 35,549 line Survey data table, we
can maintain the shorter table with the species information. When we want to
access that information, we can create a query that joins the additional columns
of information to the Survey data.

Storing data in this way has many benefits including:

1. It ensures consistency in the spelling of species attributes (genus, species
   and taxa) given each species is only entered once. Imagine the possibilities
   for spelling errors when entering the genus and species thousands of times!
2. It also makes it easy for us to make changes to the species information once
   without having to find each instance of it in the larger survey data.
3. It optimizes the size of our data.


## Joining Two DataFrames

To better understand joins, let's grab the first 10 lines of our data as a
subset to work with. We'll use the `.head` method to do this. We'll also read
in a subset of the species table.

~~~
# Read in first 10 lines of surveys table
survey_sub = surveys_df.head(10)

# Import a small subset of the species data designed for this part of the lesson.
# It is stored in the data folder.
species_sub = pd.read_csv('data/speciesSubset.csv', keep_default_na=False, na_values=[""])
~~~
{: .language-python}

In this example, `species_sub` is the lookup table containing genus, species, and
taxa names that we want to join with the data in `survey_sub` to produce a new
DataFrame that contains all of the columns from both `species_df` *and*
`survey_df`.


## Identifying join keys

To identify appropriate join keys we first need to know which field(s) are
shared between the files (DataFrames). We might inspect both DataFrames to
identify these columns. If we are lucky, both DataFrames will have columns with
the same name that also contain the same data. If we are less lucky, we need to
identify a (differently-named) column in each DataFrame that contains the same
information.

~~~
>>> species_sub.columns

Index([u'species_id', u'genus', u'species', u'taxa'], dtype='object')

>>> survey_sub.columns

Index([u'record_id', u'month', u'day', u'year', u'plot_id', u'species_id',
       u'sex', u'hindfoot_length', u'weight'], dtype='object')
~~~
{: .language-python}

In our example, the join key is the column containing the two-letter species
identifier, which is called `species_id`.

Now that we know the fields with the common species ID attributes in each
DataFrame, we are almost ready to join our data. However, since there are
[different types of joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/), we
also need to decide which type of join makes sense for our analysis.

## Inner joins

The most common type of join is called an _inner join_. An inner join combines
two DataFrames based on a join key and returns a new DataFrame that contains
**only** those rows that have matching values in *both* of the original
DataFrames.

Inner joins yield a DataFrame that contains only rows where the value being
joins exists in BOTH tables. An example of an inner join, adapted from [this
page](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is below:

![Inner join -- courtesy of codinghorror.com](../fig/inner-join.png)

The pandas function for performing joins is called `merge` and an Inner join is
the default option:

~~~
merged_inner = pd.merge(left=survey_sub,right=species_sub, left_on='species_id', right_on='species_id')
# In this case `species_id` is the only column name in  both dataframes, so if we skipped `left_on`
# And `right_on` arguments we would still get the same result

# What's the size of the output data?
merged_inner.shape
merged_inner
~~~
{: .language-python}

~~~
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  \
0          1      7   16  1977        2         NL   M               32
1          2      7   16  1977        3         NL   M               33
2          3      7   16  1977        2         DM   F               37
3          4      7   16  1977        7         DM   M               36
4          5      7   16  1977        3         DM   M               35
5          8      7   16  1977        1         DM   M               37
6          9      7   16  1977        1         DM   F               34
7          7      7   16  1977        2         PE   F              NaN

   weight       genus   species    taxa
0     NaN     Neotoma  albigula  Rodent
1     NaN     Neotoma  albigula  Rodent
2     NaN   Dipodomys  merriami  Rodent
3     NaN   Dipodomys  merriami  Rodent
4     NaN   Dipodomys  merriami  Rodent
5     NaN   Dipodomys  merriami  Rodent
6     NaN   Dipodomys  merriami  Rodent
7     NaN  Peromyscus  eremicus  Rodent
~~~
{: .output}

The result of an inner join of `survey_sub` and `species_sub` is a new DataFrame
that contains the combined set of columns from `survey_sub` and `species_sub`. It
*only* contains rows that have two-letter species codes that are the same in
both the `survey_sub` and `species_sub` DataFrames. In other words, if a row in
`survey_sub` has a value of `species_id` that does *not* appear in the `species_id`
column of `species`, it will not be included in the DataFrame returned by an
inner join.  Similarly, if a row in `species_sub` has a value of `species_id`
that does *not* appear in the `species_id` column of `survey_sub`, that row will not
be included in the DataFrame returned by an inner join.

The two DataFrames that we want to join are passed to the `merge` function using
the `left` and `right` argument. The `left_on='species'` argument tells `merge`
to use the `species_id` column as the join key from `survey_sub` (the `left`
DataFrame). Similarly , the `right_on='species_id'` argument tells `merge` to
use the `species_id` column as the join key from `species_sub` (the `right`
DataFrame). For inner joins, the order of the `left` and `right` arguments does
not matter.

The result `merged_inner` DataFrame contains all of the columns from `survey_sub`
(record id, month, day, etc.) as well as all the columns from `species_sub`
(species_id, genus, species, and taxa).

Notice that `merged_inner` has fewer rows than `survey_sub`. This is an
indication that there were rows in `surveys_df` with value(s) for `species_id` that
do not exist as value(s) for `species_id` in `species_df`.

## Left joins

What if we want to add information from `species_sub` to `survey_sub` without
losing any of the information from `survey_sub`? In this case, we use a different
type of join called a "left outer join", or a "left join".

Like an inner join, a left join uses join keys to combine two DataFrames. Unlike
an inner join, a left join will return *all* of the rows from the `left`
DataFrame, even those rows whose join key(s) do not have values in the `right`
DataFrame.  Rows in the `left` DataFrame that are missing values for the join
key(s) in the `right` DataFrame will simply have null (i.e., NaN or None) values
for those columns in the resulting joined DataFrame.

Note: a left join will still discard rows from the `right` DataFrame that do not
have values for the join key(s) in the `left` DataFrame.

![Left Join](../fig/left-join.png)

A left join is performed in pandas by calling the same `merge` function used for
inner join, but using the `how='left'` argument:

~~~
merged_left = pd.merge(left=survey_sub,right=species_sub, how='left', left_on='species_id', right_on='species_id')
merged_left
~~~
{: .language-python}
~~~
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  \
0          1      7   16  1977        2         NL   M               32
1          2      7   16  1977        3         NL   M               33
2          3      7   16  1977        2         DM   F               37
3          4      7   16  1977        7         DM   M               36
4          5      7   16  1977        3         DM   M               35
5          6      7   16  1977        1         PF   M               14
6          7      7   16  1977        2         PE   F              NaN
7          8      7   16  1977        1         DM   M               37
8          9      7   16  1977        1         DM   F               34
9         10      7   16  1977        6         PF   F               20

   weight       genus   species    taxa
0     NaN     Neotoma  albigula  Rodent
1     NaN     Neotoma  albigula  Rodent
2     NaN   Dipodomys  merriami  Rodent
3     NaN   Dipodomys  merriami  Rodent
4     NaN   Dipodomys  merriami  Rodent
5     NaN         NaN       NaN     NaN
6     NaN  Peromyscus  eremicus  Rodent
7     NaN   Dipodomys  merriami  Rodent
8     NaN   Dipodomys  merriami  Rodent
9     NaN         NaN       NaN     NaN
~~~
{: .output}

The result DataFrame from a left join (`merged_left`) looks very much like the
result DataFrame from an inner join (`merged_inner`) in terms of the columns it
contains. However, unlike `merged_inner`, `merged_left` contains the **same
number of rows** as the original `survey_sub` DataFrame. When we inspect
`merged_left`, we find there are rows where the information that should have
come from `species_sub` (i.e., `species_id`, `genus`, and `taxa`) is
missing (they contain NaN values):

~~~
merged_left[ pd.isnull(merged_left.genus) ]
~~~
{: .language-python}
~~~
   record_id  month  day  year  plot_id species_id sex  hindfoot_length  \
5          6      7   16  1977        1         PF   M               14
9         10      7   16  1977        6         PF   F               20

   weight genus species taxa
5     NaN   NaN     NaN  NaN
9     NaN   NaN     NaN  NaN
~~~
{: .output}

These rows are the ones where the value of `species_id` from `survey_sub` (in this
case, `PF`) does not occur in `species_sub`.


## Other join types

The pandas `merge` function supports two other join types:

* Right (outer) join: Invoked by passing `how='right'` as an argument. Similar
  to a left join, except *all* rows from the `right` DataFrame are kept, while
  rows from the `left` DataFrame without matching join key(s) values are
  discarded.
* Full (outer) join: Invoked by passing `how='outer'` as an argument. This join
  type returns the all pairwise combinations of rows from both DataFrames; i.e.,
  the result DataFrame will `NaN` where data is missing in one of the dataframes. This join type is
  very rarely used.


{% include links.md %}
