---
title: "Lendo Dados de Arquivos"
teaching: 5
exercises: 10
questions:
- "Como posso carregar o conteúdo de um arquivo no Python?"
- "Como eu posso processar muitos arquivos com um único comando?"
objectives:
- "Conseguir carregar o conteúdo de um arquivo em uma string ou lista."
- "Conseguir converter dados carregados como strings em valores numéricos."
- "Conseguir escrever valores carregados no Python em um novo arquivo."
- "Ser capaz de escrever expressões de globbing que correspondem a um conjunto de arquivos."
- "Usar glob para criar listas de arquivos."
- "Escrever for loops para executar operações em arquivos, dados seus nomes em uma lista."
keypoints:
- "Use a função embutida `open` para ler arquivos."
- "Use `read` para carregar um arquivo como uma string."
- "Use `readlines` para carregar um arquivo como uma lista de linhas."
- "Os caracteres `'\t'` e `'\n'` simbolizam espaços em branco."
- "Use a função `open(..., mode='w')` para escrever em arquivos."
- "Use um `for` loop para processar arquivos dada uma lista com seus nomes."
- "Use `glob.glob` para encontrar conjuntos de arquivos cujos nomes correspondam a um padrão."
- "Use `glob` e `for` para processar lotes de arquivos."
---

## Use a função embutida [`open`](https://docs.python.org/pt-br/3/library/functions.html#open) para ler arquivos em uma string.

Para ler um arquivo, usamos a expressão `with open(...) as f`, onde `f` é a variável na qual vamos carregar o conteúdo
do arquivo em uma string. Segue a mesma estrutura de um loop for:

~~~
with open('data/consumos/consumos_00.txt') as f:
    string_de_dados = f.read()

print(string_de_dados)
~~~
{: .language-python}

O uso do `with ...` não é obrigatório, mas é recomendado. Podemos abrir e fechar arquivos uma linha por vez.
O bloco de código a seguir é equivalente ao anterior:

~~~
arquivo_de_entrada = open('data/consumos/consumos_00.txt')
string_de_dados = arquivo_entrada.read()
arquivo_de_entrada.close()

print(string_de_dados)
~~~
{: .language-python}

## Use `read` para carregar um arquivo como uma string.

A variável `f` vai ter um **método** `.read` que permite carregar os dados como uma string.
Repare que a variável `f` poderia se chamar qualquer coisa:

~~~
with open('data/consumos/consumos_00.txt') as arquivo_entrada:
    string_de_dados = arquivo_entrada.read()

print(type(string_de_dados))
~~~
{: .language-python}

## Use `readlines` para carregar um arquivo como uma lista de linhas.

Ler um arquivo como string pode ser útil, mas muitas vezes queremos criar
coleções de valores (listas) com o conteúdo do arquivo. O método `readlines`
carrega o conteúdo do arquivo em uma lista, na qual cada elemento é uma linha do arquivo.

~~~
with open('data/consumos/consumos_00.txt') as f:
    lista_de_dados = f.readlines()

print(type(lista_de_dados))
~~~
{: .language-python}

## Os caracteres `'\t'` e `'\n'` simbolizam espaços em branco.

Diferente da nossa `string_de_dados`, se imprimirmos nossa lista, o resultado não é muito bonito:

~~~
print(lista_de_dados)
~~~
{: .language-python}

Isso acontece por que cada linha do nosso arquivo (e cada elemento na nossa lista) é uma **string**,
e não um número. Essas strings possuem o caracter `'\n'` no final. Esse caracter é utilizado para simbolizar
um espaço de nova linha:

~~~
print("Uma linha com espaço no final.\nOutra linha.")
~~~
{: .language-python}

O caracter TAB também simboliza um espaço em branco, mas de um TAB, ou parágrafo:

~~~
print("Antes do TAB:\tDepois.")
~~~
{: .language-python}

> ## Recuperando Valores Numéricos
> Para poder fazer operações numéricas com o conteúdo desses arquivos,
> precisamos de valores de tipo numéricos, e não strings.  
> Utilize **conversão de tipos** e o **padrão acumulador** para carregar
> o conteúdo do arquivo `consumos_00.txt` em uma lista de **floats**.
> 
> > ## Solução
> > ~~~
> > lista_floats = []
> > with open("data/consumos/consumos_00.txt") as f:
> >     lista_strings = f.readlines()
> > 
> > for linha in lista_strings:
> >     lista_floats.append(float(linha))
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Removendo espaços em branco
> No exercício anterior, usamos conversão de tipos para converter as strings que carregamos
> do arquivo para remover o espaço em branco (`'\n'`). No entanto, as strings também tem
> os métodos `strip` que podem fazer isso.
> 
> ~~~
> linha_um = "\nUma linha com espaço em branco no início e fim.\n\n\n"
> linha_dois = "\nOutra linha, com espaço em branco no início."
> print(linha_um + linha_dois)
> ~~~
> {: .language-python}
> ~~~
> 
> Uma linha com espaço em branco no início e fim.
> 
> 
> 
> Outra linha, com espaço em branco no início.
> ~~~
> {: .output}
> 
> Se aplicarmos o método `strip` na `linha_um`, removemos o espaço em branco do **início** e **final** da linha.:
> 
> ~~~
> linha_um = "\nUma linha com espaço em branco no início e fim.\n\n\n"
> linha_dois = "\nOutra linha, com espaço em branco no início."
> print(linha_um.strip() + linha_dois)
> ~~~
> {: .language-python}
> ~~~
> Uma linha com espaço em branco no início e fim.
> Outra linha, com espaço em branco no início.
> ~~~
> {: .output}
> 
> Também existe o método `lstrip` para somente para espaços no início da linha, e `rstrip` somente para espaços no fim:
> 
> ~~~
> linha_um = "\nUma linha com espaço em branco no início e fim.\n\n\n"
> linha_dois = "\nOutra linha, com espaço em branco no início."
> print(linha_um.rstrip() + linha_dois.lstrip())
> ~~~
> {: .language-python}
> ~~~
> 
> Uma linha com espaço em branco no início e fim.Outra linha, com espaço em branco no início.
> ~~~
> {: .output}
{: .callout}

## Use um `for` loop para processar arquivos dada uma lista com seus nomes.

*   Um nome de arquivo é uma string de caracteres.
*   Podemos criar uma lista de nomes de arquivos e rodar um `for` loop.

~~~
lista_de_arquivos = [
    "data/consumos/consumos_00.txt",
    "data/consumos/consumos_01.txt",
    "data/consumos/consumos_02.txt",
    "data/consumos/consumos_03.txt",
    "data/consumos/consumos_04.txt",
]

for arquivo in lista_de_arquivos:
    numeros = []
    with open(arquivo) as f:
        linhas = f.readlines()

    print("Nome do arquivo:", arquivo)
    print("Número de medições:", len(linhas))
    print("\n")
~~~
{: .language-python}

~~~
Nome do arquivo: data/consumos/consumos_00.txt
Número de medições: 54

Nome do arquivo: data/consumos/consumos_01.txt
Número de medições: 81

Nome do arquivo: data/consumos/consumos_02.txt
Número de medições: 70

Nome do arquivo: data/consumos/consumos_03.txt
Número de medições: 52

Nome do arquivo: data/consumos/consumos_04.txt
Número de medições: 62
~~~
{: .output}

No entanto, ter que criar manualmente a lista de arquivos pode ser bem custoso.
Existem soluções práticas para isso.


## Use [`glob.glob`](https://docs.python.org/pt-br/3/library/glob.html#glob.glob) para encontrar conjuntos de arquivos cujos nomes correspondam a um padrão.

*   Em UNIX/Linux, o termo "globbing" significa "corresponder um conjunto de arquivos a um padrão".
*   Os padrões mais comuns são:
    *   `*` que significa "corresponde zero ou mais caracteres".
    *   `?` que significa "corresponde pelo menos um caracter".
*   A biblioteca padrão do Python contém o módulo [`glob`](https://docs.python.org/pt-br/3/library/glob.html) para prover funcionalidade para encontrar padrões.
*   O módulo [`glob`](https://docs.python.org/pt-br/3/library/glob.html) contém uma função também chamada  `glob` para corresponder padrões.
*   Por exemplo, `glob.glob('*.txt')` corresponde a todos os arquivos no diretório atual
    cujos nomes terminam com `.txt`.
*   Resultado é uma lista (possivelmente vazia) de strings.

~~~
import glob
print('Todos os arquivos zippados no diretório `data`:', glob.glob('data/*.zip'))
~~~
{: .language-python}
~~~
['data/consumos.zip']
~~~
{: .output}

> ## Encontre os Arquivos
> Modifique o código acima para encontrar todos os arquivos com dados de consumos.
> Como podemos modificar essa busca para encontrar somente os arquivos 00 até 09?
> 
> > ## Solução
> > Existem muitas buscas que podem dar certo, mas uma simples e direta é:
> > ~~~
> > # Todos os arquivos
> > glob.glob("data/consumos/*.txt")
> > ~~~
> > {: .language-python}
> > ~~~
> > # De 00 até 09
> > glob.glob("data/consumos/consumos_0*.txt")
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Use `glob` e `for` para processar lotes de arquivos.

*   Ajuda bastante se os nomes dos arquivos forem nomeados de forma sistemática e consistente
    para que padrões simples achem os nomes corretos.

~~~
for arquivo in glob("data/consumos/*.txt"):
    numeros = []
    with open(arquivo) as f:
        linhas = f.readlines()

    print("Nome do arquivo:", arquivo)
    print("Número de medições:", len(linhas))
    print("\n")
~~~
{: .language-python}


> ## Processando Lotes de Arquivos
> 
> Usando `glob` e um for loop, escreva um programa que:
> 1. Calcule o número de medições em cada arquivo.
> 2. Calcule o menor e maior consumo e cada arquivo.
> 3. Imprima tudo em um loop.
> 
> Depois que conseguir, modifique seu código para imprimir:
> - O nome do arquivo com mais registros.
> - O nome do arquivo com o maior valor (e o valor.)
> - O nome do arquivo com o menor valor (e o valor.)
> 
> > ## Solução
> > ~~~
> > lista_de_arquivos = glob("data/consumos/*.txt")
> > 
> > for arquivo in lista_de_arquivos:
> >     numeros = []
> >     with open(arquivo) as f:
> >         linhas = f.readlines()
> >         for numero in linhas:
> >             numeros.append(float(numero))
> > 
> >     menor_consumo = min(numeros)
> >     maior_consumo = max(numeros)
> > 
> >     print("Nome do arquivo:", arquivo)
> >     print("Número de medições:", len(numeros))
> >     print("Consumo máximo:", maior_consumo)
> >     print("Consumo mínimo:", menor_consumo)
> >     print("\n")
> > ~~~
> > {: .language-python}
> > 
> > Adicionando as outras métricas:
> > 
> > ~~~
> > lista_de_arquivos = glob("data/consumos/*.txt")
> > 
> > arquivo_mais_registros = ""
> > arquivo_maximo_consumo = ""
> > arquivo_minimo_consumo = ""
> > mais_registros = 0
> > maximo_consumo = 0
> > minimo_consumo = 0
> > 
> > for arquivo in lista_de_arquivos:
> >     numeros = []
> >     with open(arquivo) as f:
> >         linhas = f.readlines()
> >         for numero in linhas:
> >             numeros.append(float(numero))
> >     
> >     n_medicoes = len(numeros)
> >     maior_consumo = max(numeros)
> >     menor_consumo = min(numeros)
> >     if n_medicoes > mais_registros:
> >         mais_registros = n_medicoes
> >         arquivo_mais_registros = arquivo
> >     
> >     if maior_consumo > maximo_consumo:
> >         maximo_consumo = maior_consumo
> >         arquivo_maximo_consumo = arquivo
> >     
> >     if minimo_consumo == 0 or menor_consumo < minimo_consumo:
> >         minimo_consumo = menor_consumo
> >         arquivo_minimo_consumo = arquivo
> > 
> > print("Arquivo com mais medições:", arquivo_mais_registros, "com", mais_registros, "medições.")
> > print("Arquivo com maior valor:", arquivo_maximo_consumo, maximo_consumo)
> > print("Arquivo com menor valor:", arquivo_minimo_consumo, minimo_consumo)
> > print("\n")
> > ~~~
> > {: .language-python}
> > ~~~
> > Arquivo com mais medições: data/consumos/consumos_24.txt com 100 medições.
> > Arquivo com maior valor: data/consumos/consumos_25.txt 117.99
> > Arquivo com menor valor: data/consumos/consumos_23.txt 69.0
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Determining Matches
>
> Which of these files is *not* matched by the expression `glob.glob('data/*as*.csv')`?
>
> 1. `data/gapminder_gdp_africa.csv`
> 2. `data/gapminder_gdp_americas.csv`
> 3. `data/gapminder_gdp_asia.csv`
>
> > ## Solution
> >
> > 1 is not matched by the glob.
> {: .solution}
{: .challenge}

> ## Minimum File Size
>
> Modify this program so that it prints the number of records in
> the file that has the fewest records.
>
> ~~~
> import glob
> import pandas as pd
> fewest = ____
> for filename in glob.glob('data/*.csv'):
>     dataframe = pd.____(filename)
>     fewest = min(____, dataframe.shape[0])
> print('smallest file has', fewest, 'records')
> ~~~
> {: .language-python}
> Note that the [`DataFrame.shape()` method][shape-method]
> returns a tuple with the number of rows and columns of the data frame.
>
> > ## Solution
> > ~~~
> > import glob
> > import pandas as pd
> > fewest = float('Inf')
> > for filename in glob.glob('data/*.csv'):
> >     dataframe = pd.read_csv(filename)
> >     fewest = min(fewest, dataframe.shape[0])
> > print('smallest file has', fewest, 'records')
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Comparing Data
>
> Write a program that reads in the regional data sets
> and plots the average GDP per capita for each region over time
> in a single chart.
> > ## Solution
> > This solution builds a useful legend by using the [string `split` method][split-method] to
> > extract the `region` from the path 'data/gapminder_gdp_a_specific_region.csv'.
> > ~~~
> > import glob
> > import pandas as pd
> > import matplotlib.pyplot as plt
> > fig, ax = plt.subplots(1,1)
> > for filename in glob.glob('data/gapminder_gdp*.csv'):
> >     dataframe = pd.read_csv(filename)
> >     # extract <region> from the filename, expected to be in the format 'data/gapminder_gdp_<region>.csv'.
> >     # we will split the string using the split method and `_` as our separator,
> >     # retrieve the last string in the list that split returns (`<region>.csv`), 
> >     # and then remove the `.csv` extension from that string.
> >     region = filename.split('_')[-1][:-4] 
> >     dataframe.mean().plot(ax=ax, label=region)
> > plt.legend()
> > plt.show()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Dealing with File Paths
> The [`pathlib` module][pathlib-module] provides useful abstractions for file and path manipulation like
> returning the name of a file without the file extension. This is very useful when looping over files and
> directories. In the example below, we create a `Path` object and inspect its attributes.
> ~~~
> from pathlib import Path
> 
> p = Path("data/gapminder_gdp_africa.csv")
> print(p.parent), print(p.stem), print(p.suffix)
> ~~~
> {: .language-python}
> ~~~
> data
> gapminder_gdp_africa
> .csv
> ~~~
> {: .output}
> 
> __Hint:__ It is possible to check all available attributes and methods on the `Path` object with the `dir()`
> function!
{: .callout}
 -->
[pathlib-module]: https://docs.python.org/3/library/pathlib.html
[shape-method]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html
[split-method]: https://docs.python.org/3/library/stdtypes.html#str.split