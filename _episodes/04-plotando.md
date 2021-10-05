---
title: "Plotando"
teaching: 15
exercises: 15
questions:
- "Como posso plotar meus dados?"
- "Como posso salvar meus dados para publicação?"
objectives:
- "Crie um plot de série temporal ilustrando um conjunto de dados."
- "Crie um scatter plot para mostrar o relacionamento entre dois conjuntos de dados."
keypoints:
- "[`matplotlib`](https://matplotlib.org/) é a biblioteca de plotagem mais utilizada para o Python."
- "Plote dados diretamente de um dataframe Pandas."
- "Selecione e transforme os dados, e então plote-os."
- "Muitos estilos de plot estão disponíveis: veja a [Python Graph Gallery](https://python-graph-gallery.com/matplotlib/) para mais opções."
- "É possível plotar muitos conjuntos de dados juntos."
---
## [Matplotlib](https://matplotlib.org/) é a biblioteca de plotagem mais utilizada para o Python."

*   Geralmente utiliza o módulo [`matplotlib.pyplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot).
*   O Jupyter Notebook vai renderizar os plots *inline* por padrão.

~~~
from matplotlib import pyplot as plt
~~~
{: .language-python}

*   Plots simples são (relativemente) fáceis de criar

~~~
tempo = [0, 1, 2, 3]
posicao = [0, 100, 200, 300]

plt.plot(tempo, posicao)
plt.xlabel('Tempo (horas)')
plt.ylabel('Posição (km)')
~~~
{: .language-python}

<!-- 
![Simple Position-Time Plot](../fig/9_simple_position_time_plot.svg)
 -->

> ## Mostre a Figura
> 
> Em um notebook Jupyter, executar a célula deve gerar a figura diretamente abaixo do código.
> A figura também é incluída no documento do Notebook para visualização futura.
> No entanto, outros ambientes Python como um interpretador interativo Python
> ou um script Python executado via linha de comando requerem um comando adicional para mostrar a figura.
>
> Instrua o `matplotlib` a mostrar a figura:
> ~~~
> plt.show()
> ~~~
> {: .language-python}
>
> Esse comando pode ser usado dentro de um Notebook - por exemplo, para mostrar múltiplas figuras,
> se muitas são criadas dentro de uma única célula.
>
{: .callout}

## Plote dados diretamente de um dataframe Pandas.

*   Podemos plotar diretamente de um [dataframe Pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).
*   Isso implicitamente usa o módulo [`matplotlib.pyplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot).

~~~
df.plot()
~~~
{: .language-python}

## Selecione e transforme os dados, e então plote-os.

~~~
df['RESIDENCIAL'].plot()
mask = df > 100000
df[mask].plot()
~~~
{: .language-python}

## Muitos estilos de plot estão disponíveis

* Veja a [Python Graph Gallery](https://python-graph-gallery.com/matplotlib/) para mais opções.
* Por exemplo, faça um boxplot com barras de erro: 

~~~
plt.style.use('ggplot')
df.plot(kind='box')
~~~
{: .language-python}

<!-- 
![GDP barplot for Australia](../fig/9_gdp_bar.svg)
 -->

## Dados também podem ser plotados usando a função `plot` do `matplotlib`

*   O comando é `plt.plot(x, y)`
*   A cor e formato dos marcadores também podem ser especificados como um argumento adicional opcional, por exemplo, `b-` é uma linha azul, `g--` é uma linha tracejada verde.


~~~
anos = df.index

plt.plot(anos, df["RESIDENCIAL"], 'g--')
~~~
{: .language-python}
<!-- 
![GDP formatted plot for Australia](../fig/9_gdp_australia_formatted.svg)
 -->
## É possível plotar muitos conjuntos de dados juntos.

~~~
# Selecione os dois setores
residencial = df["RESIDENCIAL"]
comercial = df["COMERCIAL"]

# Plote com cores diferentes
plt.plot(anos, residencial, 'b-', label='Residencial')
plt.plot(anos, comercial, 'g-', label='Comercial')

# Crie uma legenda
plt.legend(loc='upper left')
plt.xlabel('Ano')
plt.ylabel('Consumo (GWh)')
~~~
{: .language-python}

> ## Adicionando uma legenda
> 
> Normalmente quando plotamos vários dados juntos, queremos ter
> uma legenda descrevendo os dados.
>
> Isso pode ser feito com `matplotlib` em dois estágios.
> 
> * Dê uma legenda para cada conjunto na figura:
>
> ~~~
> plt.plot(anos, residencial, 'b-', label='Residencial')
> plt.plot(anos, comercial, 'g-', label='Comercial')
> ~~~
> {: .language-python}
>
> * Instrua o `matplotlib` a criar a legenda.
>
> ~~~
> plt.legend()
> ~~~
> {: .language-python}
>
> Por padrão o Matplotlib vai tentar criar a legenda em uma posição adequada. Se você
> preferir especificar uma posição, isso pode ser feito com o argumento `loc=`, e.g.
> para colocar a legenda no canto superior esquerdo, use `loc='upper left'`.
>
{: .callout}


<!-- ![GDP formatted plot for Australia and New Zealand](../fig/9_gdp_australia_nz_formatted.svg) -->
*   Crie um scatter plot correlacionando o crescimento do setor 'Comercial' e do setor 'Outros'.

~~~
plt.scatter(df['COMERCIAL'], df['OUTROS'])
~~~
{: .language-python}

Ou, direto do dataframe:

~~~
df.plot.scatter(x="COMERCIAL", y="OUTROS")
~~~
{: .language-python}
<!-- 
![GDP correlation using plt.scatter](../fig/9_gdp_correlation_plt.svg)
~~~
data.T.plot.scatter(x = 'Australia', y = 'New Zealand')
~~~
{: .language-python}

![GDP correlation using data.T.plot.scatter](../fig/9_gdp_correlation_data.svg)
 -->
<!-- 
> ## Mínimos e Máximos
>
> Fill in the blanks below to plot the minimum GDP per capita over time
> for all the countries in Europe.
> Modify it again to plot the maximum GDP per capita over time for Europe.
>
> ~~~
> data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> data_europe.____.plot(label='min')
> data_europe.____
> plt.legend(loc='best')
> plt.xticks(rotation=90)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> > data_europe.min().plot(label='min')
> > data_europe.max().plot(label='max')
> > plt.legend(loc='best')
> > plt.xticks(rotation=90)
> > ~~~
> > {: .language-python}
> > ![Minima Maxima Solution](../fig/9_minima_maxima_solution.png)
> {: .solution}
{: .challenge}

> ## Correlations
>
> Modify the example in the notes to create a scatter plot showing
> the relationship between the minimum and maximum GDP per capita
> among the countries in Asia for each year in the data set.
> What relationship do you see (if any)?
>
>
> > ## Solution
> > ~~~
> > data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> > data_asia.describe().T.plot(kind='scatter', x='min', y='max')
> > ~~~
> > {: .language-python}
> >
> > ![Correlations Solution 1](../fig/9_correlations_solution1.svg)
> >
> > No particular correlations can be seen between the minimum and maximum gdp values
> > year on year. It seems the fortunes of asian countries do not rise and fall together.
> {: .solution}
>
> You might note that the variability in the maximum is much higher than
> that of the minimum.  Take a look at the maximum and the max indexes:
>
> ~~~
> data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> data_asia.max().plot()
> print(data_asia.idxmax())
> print(data_asia.idxmin())
> ~~~
> {: .language-python}
> > ## Solution
> > ![Correlations Solution 2](../fig/9_correlations_solution2.png)
> >
> > Seems the variability in this value is due to a sharp drop after 1972.
> > Some geopolitics at play perhaps? Given the dominance of oil producing countries,
> > maybe the Brent crude index would make an interesting comparison?
> > Whilst Myanmar consistently has the lowest gdp, the highest gdb nation has varied
> > more notably.
> {: .solution}
{: .challenge}

> ## More Correlations
>
> This short program creates a plot showing
> the correlation between GDP and life expectancy for 2007,
> normalizing marker size by population:
>
> ~~~
> data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')
> data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
>               s=data_all['pop_2007']/1e6)
> ~~~
> {: .language-python}
>
> Using online help and other resources,
> explain what each argument to `plot` does.
>
> > ## Solution
> > ![More Correlations Solution](../fig/9_more_correlations_solution.svg)
> >
> > A good place to look is the documentation for the plot function -
> > help(data_all.plot).
> >
> > kind - As seen already this determines the kind of plot to be drawn.
> >
> > x and y - A column name or index that determines what data will be
> > placed on the x and y axes of the plot
> >
> > s - Details for this can be found in the documentation of plt.scatter.
> > A single number or one value for each data point. Determines the size
> > of the plotted points.
> {: .solution}
{: .challenge}
 -->

> ## Salvado Plots em um Arquivo
> 
> Se você está satisfeito com um plot, talvez você queira salvá-lo,
> seja para enviar para outra pessoa ou para incluir em um relatório. Existe uma função
> no módulo `pyplot` que faz isso: 
> [savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html).
> Chamando essa função, por exemplo, dessa forma:
> ~~~
> plt.savefig('minha_figura.png')
> ~~~
> {: .language-python}
> 
> vai salvar a figura atual como `minha_figura.png`. O formato de arquivo
> vai ser automaticamente deduzido da extensão do nome de arquivo (formatos válidos
> são png, pdf, ps, eps e svg).
>
> Note que métodos chamados com `plt.` se referem a uma variável de figura global
> e depois que a figura for mostrada na tela (por exemplo, com `plt.show`)
> essa variável vai se referir a uma figura vazia.
> Portanto, certifique-se de chamar `plt.savefig` **ANTES** do plot ser mostrado na tela,
> caso contrário você pode acabar com um plot vazio.
>
> Quando usamos dataframes, os dados costumam ser gerados e plotados em uma única linha,
> e `plt.savefig` não parece uma abordagem possível.
> Uma possibilidade para salvar a figura em um arquivo é:
>
> * salvar uma referência para a figura atual em uma variável local (com `plt.gcf`),
> * chamar a função `savefig` daquela variável.
>
> ~~~
> fig = plt.gcf() # pega a figura atual
> data.plot(kind='bar')
> fig.savefig('minha_figura.png')
> ~~~
> {: .language-python}
{: .callout}
<!-- 
> ## Making your plots accessible
>
> Whenever you are generating plots to go into a paper or a presentation, there are a few things you can do to make sure that everyone can understand your plots.
> * Always make sure your text is large enough to read. Use the `fontsize` parameter in `xlabel`, `ylabel`, `title`, and `legend`, and [`tick_params` with `labelsize`](https://matplotlib.org/latest/api/_as_gen/matplotlib.pyplot.tick_params.html) to increase the text size of the numbers on your axes.
> * Similarly, you should make your graph elements easy to see. Use `s` to increase the size of your scatterplot markers and `linewidth` to increase the sizes of your plot lines.
> * Using color (and nothing else) to distinguish between different plot elements will make your plots unreadable to anyone who is colorblind, or who happens to have a black-and-white office printer. For lines, the `linestyle` parameter lets you use different types of lines. For scatterplots, `marker` lets you change the shape of your points. If you're unsure about your colors, you can use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) or [Color Oracle](https://colororacle.org/) to simulate what your plots would look like to those with colorblindness.
{: .callout}
 -->

> ## Tornando seus plots acessíveis
>
> Sempre que você está gerando plots para colocar em um relatório ou apresentação, 
> * Sempre assegure que seu texto está grande o suficiente para ler. Use os parâmetros `fontsize` em `xlabel`, `ylabel`, `title`, e `legend`, e outros para customizar seu plots.
> * Similarmente, torne os elementos do seu gráfico fáceis de enxergar. Use `s` para aumentar o tamanho do marcador do scatterplot e `linewdith` para aumentar o tamanho das linhas do plot.
> * Usar cor (e mais nada) para distinguir entre diferentes elementos do plot pode torná-lo ilegível para quem for daltônico, ou só tem uma impressora/display preto-e-branco. Para linhas, use `linestyle` ou `marker` para customizar suas linhas e marcadores.
{: .callout}
