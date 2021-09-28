---
title: "Escrevendo Funções"
teaching: 10
exercises: 15
questions:
- "Como eu posso criar minhas próprias funções?"
objectives:
- "Explique e identifique a diferença entre a definição da função e a chamada da função."
- "Escreva uma função que receba um número fixo de argumentos e produza um único resultado."
keypoints:
- "Organize programas em funções para que sejam mais fáceis de entender."
- "Defina uma função usado `def` com um nome, parâmetros, e um bloco de código."
- "Definir uma função não roda ela."
- "Argumentos em uma chamada correspondem aos parâmetros na definição."
- "Funções podem retornar um resultado para quem está chamando usando `return`."
---
<!-- 
## Break programs down into functions to make them easier to understand.

*   Human beings can only keep a few items in working memory at a time.
*   Understand larger/more complicated ideas by understanding and combining pieces.
    *   Components in a machine.
    *   Lemmas when proving theorems.
*   Functions serve the same purpose in programs.
    *   *Encapsulate* complexity so that we can treat it as a single "thing".
*   Also enables *re-use*.
    *   Write one time, use many times.
 -->

## Organize programas em funções para que sejam mais fáceis de entender.

*   Seres humanos só conseguem manter algumas coisas "em memória" de cada vez.
*   Entenda ideias maiores/mais complicadas ao entender e combinar peças individuais.
    *   Componentes em uma máquina.
    *   Capítulos e subseções em um grande relatório.
*   Funções servem o mesmo propósito em programas.
    *   *Encapsular* complexidade para que possamos a tratar como uma única "coisa".
*   Também permite o *re-uso*.
    *   Escreva uma vez, use muitas vezes.

<!-- 
## Define a function using `def` with a name, parameters, and a block of code.

*   Begin the definition of a new function with `def`.
*   Followed by the name of the function.
    *   Must obey the same rules as variable names.
*   Then *parameters* in parentheses.
    *   Empty parentheses if the function doesn't take any inputs.
    *   We will discuss this in detail in a moment.
*   Then a colon.
*   Then an indented block of code.
 -->

## Defina uma função usando `def` com um nome, parâmetros, e um bloco de código.

*   Comece a definição de uma nova função com  `def`.
*   Seguido do nome da função.
    *   Deve obedecer as mesmas regras que nomes de variáveis.
*   Coloque os *parâmetros* entre parênteses.
    *   Coloque parênteses em branco se a função não recebe nenhum input.
    *   Vamos discutir isso em detalhe em um momento.
*   Coloque dois pontos.
*   E então um bloco indentado de código.

<!-- 
~~~
def print_greeting():
    print('Hello!')
~~~
{: .language-python}
 -->

~~~
def imprimir_saudacao():
    print('Olá!')
~~~
{: .language-python}

<!-- 
## Defining a function does not run it.

*   Defining a function does not run it.
    *   Like assigning a value to a variable.
*   Must call the function to execute the code it contains.
 -->

## Definir uma função não roda ela.

*   Definir uma função não roda ela.
    *   É como assinalar um valor a uma variável.
*   Precisamos chamar a função para executar o código que ela contém.

<!-- 
~~~
print_greeting()
~~~
{: .language-python}
~~~
Hello!
~~~
{: .output}
 -->

~~~
imprimir_saudacao()
~~~
{: .language-python}
~~~
Olá!
~~~
{: .output}

<!-- 
## Arguments in call are matched to parameters in definition.

*   Functions are most useful when they can operate on different data.
*   Specify *parameters* when defining a function.
    *   These become variables when the function is executed.
    *   Are assigned the arguments in the call (i.e., the values passed to the function).
    *   If you don't name the arguments when using them in the call, the arguments will be matched to 
    parameters in the order the parameters are defined in the function.
 -->

## Argumentos em uma chamada correspondem aos parâmetros na definição.

*   Funções são úteis quando elas podem operar em diferentes dados.
*   Especifique *parâmetros* quando for definir uma função.
    *   Esses se tornam variáveis quando a função é executada.
    *   São assinaladas aos argumentos na chamada, isto é, os valores passados para a função.
    *   Se você não nomear os argumentos quando for usá-los na chamada, os argumentos vão ser correspondidos com os
    parâmetros na ordem quem os parâmetros são definidos na função.

<!-- 
~~~
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
~~~
{: .language-python}
~~~
1871/3/19
~~~
{: .output}
 -->

~~~
def imprimir_data(ano, mes, dia)
    data_formatada = str(ano) + '/' + str(mes) + '/' + str(dia)
    print(data_formatada)

imprimir_data(2021, 3, 19)
~~~
{: .language-python}
~~~
2021/3/19
~~~
{: .output}
<!-- 
Or, we can name the arguments when we call the function, which allows us to
specify them in any order:
~~~
print_date(month=3, day=19, year=1871)
~~~
{: .language-python}
~~~
1871/3/19
~~~
{: .output}
 -->

Ou, podemos nomear os argumentos quando chamamos a função, o que nos permite
especificá-los em qualquer ordem:
~~~
imprimir_data(mes=3, dia=19, ano=2021)
~~~
{: .language-python}
~~~
2021/3/19
~~~
{: .output}
<!-- 
*   Via [Twitter](https://twitter.com/minisciencegirl/status/693486088963272705):
    `()` contains the ingredients for the function
    while the body contains the recipe.
 -->

*   É como se o `()` contivesse os ingredientes para a função e o corpo contém a receita.

<!-- 
## Functions may return a result to their caller using `return`.

*   Use `return ...` to give a value back to the caller.
*   May occur anywhere in the function.
*   But functions are easier to understand if `return` occurs:
    *   At the start to handle special cases.
    *   At the very end, with a final result.
 -->

## Funções podem retornar um resultado para quem está chamando usando `return`.

*   Use `return ...` para retornar um valor a chamada da função.
*   Pode ocorrer em qualquer lugar da função..
*   Mas funções são mais fáceis de entender se `return` ocorre:
    *   No começo para lidar com casos especiais.
    *   Bem no fim da função, com um resultado final.

<!-- 
~~~
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
~~~
{: .language-python}
 -->

~~~
def calcular_media(valores):
    if len(valores) == 0:
        return None
    return sum(valores) / len(valores)
~~~
{: .language-python}
<!-- 
~~~
a = average([1, 3, 4])
print('average of actual values:', a)
~~~
{: .language-python}
~~~
average of actual values: 2.6666666666666665
~~~
{: .output}
 -->

~~~
a = calcular_media([1, 3, 4])
print('Média de valores reais:', a)
~~~
{: .language-python}
~~~
Média de valores reais: 2.6666666666666665
~~~
{: .output}
<!-- 
~~~
print('average of empty list:', average([]))
~~~
{: .language-python}
~~~
average of empty list: None
~~~
{: .output}
 -->

~~~
print('Média de uma lista vazia:', calcular_media([]))
~~~
{: .language-python}
~~~
Média de uma lista vazia: None
~~~
{: .output}
<!-- 
*   Remember: [every function returns something]({{ page.root }}/04-built-in/).
*   A function that doesn't explicitly `return` a value automatically returns `None`.
 -->

*   Lembre-se: [toda função **retorna algo!**]({{ page.root }}/04-built-in/).
*   Uma função que não tem um valor retornado por `return` automaticamente retorna `None`.

<!-- 
~~~
result = print_date(1871, 3, 19)
print('result of call is:', result)
~~~
{: .language-python}
~~~
1871/3/19
result of call is: None
~~~
{: .output}
 -->

~~~
resultado = imprimir_data(2021, 3, 19)
print('O resultado da chamada é:', resultado)
~~~
{: .language-python}
~~~
2021/3/19
O resultado da chamada é: None
~~~
{: .output}

<!-- 
> ## Identifying Syntax Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3 until you have fixed all the errors.
>
> ~~~
> def another_function
>   print("Syntax errors are annoying.")
>    print("But at least python tells us about them!")
>   print("So they are usually not too hard to fix.")
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > def another_function():
> >   print("Syntax errors are annoying.")
> >   print("But at least Python tells us about them!")
> >   print("So they are usually not too hard to fix.")
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Identificando erros de sintaxe
>
> 1. Leia o código abaixo e tente identificar o que os erros são
>    *sem* rodá-lo.
> 2. Rode o código e leia a mensagem de erro.
>    É do tipo `SyntaxError` ou `IndentationError`?
> 3. Conserte o erro.
> 4. Repita os passos 2 e 3 até que consertar todos os erros.
>
> ~~~
> def outra_funcao
>   print("Erros de sintaxe são irritantes.")
>    print("Mas pelo menos o Python nos avisa sobre eles!")
>   print("Então não são muito difíceis de consertar.")
> ~~~
> {: .language-python}
>
> > ## Solução
> >
> > ~~~
> > def outra_funcao():
> >   print("Erros de sintaxe são irritantes.")
> >   print("Mas pelo menos o Python nos avisa sobre eles!")
> >   print("Então não são muito difíceis de consertar.")
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

<!-- 
> ## Definition and Use
>
> What does the following program print?
>
> ~~~
> def report(pressure):
>     print('pressure is', pressure)
>
> print('calling', report, 22.5)
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > calling <function report at 0x7fd128ff1bf8> 22.5
> > ~~~ 
> > {: .output}
> >
> > A function call always needs parenthesis, otherwise you get memory address of the function object. So, if we wanted to call the function named report, and give it the value 22.5 to report on, we could have our function call as follows
> > ~~~
> > print("calling")
> > report(22.5)
> > ~~~
> > {: .language-python}
> > ~~~
> > calling
> > pressure is 22.5
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Definição e Uso
>
> O que o programa a seguir imprime?
>
> ~~~
> def relatorio(consumo):
>     print('consumo é', consumo)
>
> print('chamando', relatorio, 22.5)
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > chamando <function relatorio at 0x7fd128ff1bf8> 22.5
> > ~~~ 
> > {: .output}
> >
> > Uma chamada de função sempre precisa de parênteses, caso contrário você recebe o endereço de memória do objeto função. Então, se queremos chamar a função chamada `relatorio`, e dar o valor 22.5 para ser reportado, podemos fazer nossa chamada de função assim:
> > ~~~
> > print("chamando")
> > relatorio(22.5)
> > ~~~
> > {: .language-python}
> > ~~~
> > chamando
> > consumo é 22.5
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
<!-- 
> ## Order of Operations
>
> 1. What's wrong in this example?
>
>     ~~~
>     result = print_time(11, 37, 59)
>
>     def print_time(hour, minute, second):
>        time_string = str(hour) + ':' + str(minute) + ':' + str(second)
>        print(time_string)
>     ~~~
>     {: .language-python}
> 
> 2. After fixing the problem above, explain why running this example code:
>
>     ~~~
>     result = print_time(11, 37, 59)
>     print('result of call is:', result)
>     ~~~
>     {: .language-python}
>
>     gives this output:
>
>     ~~~
>     11:37:59
>     result of call is: None
>     ~~~
>     {: .output}
>
> 3. Why is the result of the call `None`?
>
> > ## Solution
> > 
> > 1. The problem with the example is that the function `print_time()` is defined *after* the call to the function is made. Python
> > doesn't know how to resolve the name `print_time` since it hasn't been defined yet and will raise a `NameError` e.g.,
> > `NameError: name 'print_time' is not defined`
> >
> > 2. The first line of output `11:37:59` is printed by the first line of code, `result = print_time(11, 37, 59)` that binds the value 
> > returned by invoking `print_time` to the variable `result`. The second line is from the second print call to print the contents 
> > of the `result` variable.
> >
> > 3. `print_time()` does not explicitly `return` a value, so it automatically returns `None`.
> >
> {: .solution}
{: .challenge}
 -->

> ## Ordem das Operações
>
> 1. O que há de errado nesse exemplo?
>
>     ~~~
>     resultado = imprimir_tempo(11, 37, 59)
>
>     def imprimir_tempo(hour, minute, second):
>        time_string = str(hour) + ':' + str(minute) + ':' + str(second)
>        print(time_string)
>     ~~~
>     {: .language-python}
> 
> 2. After fixing the problem above, explain why running this example code:
>
>     ~~~
>     resultado = imprimir_tempo(11, 37, 59)
>     print('resultado of call is:', resultado)
>     ~~~
>     {: .language-python}
>
>     gives this output:
>
>     ~~~
>     11:37:59
>     resultado of call is: None
>     ~~~
>     {: .output}
>
> 3. Por que o resultado da chamada é `None`?
>
> > ## Solução
> > 
> > 1. O problema no exemploe é que a função `imprimir_tempo()` é definida *após* a chamada ser feita. O Python
> > não sabe como resolver o nome `imprimir_tempo` já que não foi definido e vai retornar um error `NameError` como
> > `NameError: name 'imprimir_tempo' is not defined`
> >
> > 2. A primeira linha da saída `11:37:59` é impressa pela primeira linha de código, `resultado = imprimir_tempo(11, 37, 59)` que assinala o valor
> > retornado por `imprimir_tempo` a variavel `resultado`. A segunda linha linha de c´dogio é o resultado do segundo print, que imprime o conteúdo
> > da variável `resultado`.
> >
> > 3. `imprimir_tempo()` não retorna um valor explicitamente com `return`, então automaticamente retorna `None`.
> >
> {: .solution}
{: .challenge}

<!-- 
> ## Encapsulation
>
> Fill in the blanks to create a function that takes a single filename as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import pandas as pd
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > import pandas as pd
> > 
> > def min_in_data(filename):
> >     data = pd.read_csv(filename)
> >     return data.min()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Encapsulação
>
> Preencha os brancos para criar uma função que recebe um único nome de arquivo como argumento,
> carrega os dados do arquivo, e retorna o **comprimento da maior linha.**
> ~~~
>
> def detectar_tamanho_linha(____):
>     with open(____) as f:
>         dados = f.readlines()
> 
>     comprimentos = []
>     for linha em dados:
>         comprimentos.append(____)
> 
>     maior_comprimento = max(____) 
>     return maior_comprimento
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > def detectar_tamanho_linha(arquivo):
> >     with open(arquivo) as f:
> >         dados = f.readlines()
> > 
> >     comprimentos = []
> >     for linha em dados:
> >         comprimentos.append(len(linha))
> > 
> >     maior_comprimento = max(comprimentos) 
> >     return maior_comprimento
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## Find the First
>
> Fill in the blanks to create a function that takes a list of numbers as an argument
> and returns the first negative value in the list.
> What does your function do if the list is empty? What if the list has no negative numbers?
>
> ~~~
> def first_negative(values):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > def first_negative(values):
> >     for v in values:
> >         if v < 0:
> >             return v
> > ~~~
> > {: .language-python}
> > If an empty list or a list with all positive values is passed to this function, it returns `None`:
> > ~~~
> > my_list = []
> > print(first_negative(my_list))
> > ~~~
> > {: .language-python}
> > ~~~
> > None
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Encontre o Primeiro
>
> Preencha os brancos para criar uma função que receba uma lista de números como argumento
> e imprima o primeiro valor negativo na lista.
> O que a sua função faz se a lista estiver vazia? E se a lista não tiver números negativos?
>
> ~~~
> def primeiro_negativo(valores):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > def primeiro_negativo(valores):
> >     for v in valores:
> >         if v < 0:
> >             return v
> > ~~~
> > {: .language-python}
> > Se uma lista vazia ou uma lista só com valores positivos for passada para essa função, ela retorna `None`:
> > ~~~
> > minha_lista = []
> > print(primeiro_negativo(minha_lista))
> > ~~~
> > {: .language-python}
> > ~~~
> > None
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Calling by Name
>
> Earlier we saw this function:
>
> ~~~
> def print_date(year, month, day):
>     joined = str(year) + '/' + str(month) + '/' + str(day)
>     print(joined)
> ~~~
> {: .language-python}
> We saw that we can call the function using *named arguments*, like this:
> ~~~
> print_date(day=1, month=2, year=2003)
> ~~~
> {: .language-python}
>
> 1.  What does `print_date(day=1, month=2, year=2003)` print?
> 2.  When have you seen a function call like this before?
> 3.  When and why is it useful to call functions this way?
>
> > ## Solution
> > 
> > 1. `2003/2/1`
> > 2. We saw examples of using *named arguments* when working with the pandas library. For example, when reading in a dataset 
> > using `data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')`, the last argument `index_col` is a 
> > named argument.  
> > 3. Using named arguments can make code more readable since one can see from the function call what name the different arguments 
> > have inside the function. It can also reduce the chances of passing arguments in the wrong order, since by using named arguments 
> > the order doesn't matter.
> {: .solution}
{: .challenge}
 -->


<!-- 
> ## Encapsulation of an If/Print Block
>
> The code below will run on a label-printer for chicken eggs.  A digital scale will report a chicken egg mass (in grams) 
> to the computer and then the computer will print a label.  
>
> Please re-write the code so that the if-block is folded into a function.
>
> ~~~
> import random
> for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass = 70 + 20.0 * (2.0 * random.random() - 1.0)
>
>     print(mass)
>    
>     # egg sizing machinery prints a label
>     if mass >= 85:
>        print("jumbo")
>     elif mass >= 70:
>        print("large")
>     elif mass < 70 and mass >= 55:
>        print("medium")
>     else:
>        print("small")
> ~~~
> {: .language-python}
>
>
> The simplified program follows.  What function definition will make it functional?
>
> ~~~
> # revised version
> import random
> for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass = 70 + 20.0 * (2.0 * random.random() - 1.0)
>
>     print(mass, get_egg_label(mass))    
>
> ~~~
> {: .language-python}
>
>
> 1. Create a function definition for `get_egg_label()` that will work with the revised program above.  Note that the `get_egg_label()` function's return value will be important. Sample output from the above program would be `71.23 large`.
> 2. A dirty egg might have a mass of more than 90 grams, and a spoiled or broken egg will probably have a mass that's less than 50 grams.  Modify your `get_egg_label()` function to account for these error conditions. Sample output could be `25 too light, probably spoiled`.
>
> > ## Solution
> >
> > ~~~
> > def get_egg_label(mass):
> >     # egg sizing machinery prints a label
> >     egg_label = "Unlabelled"
> >     if mass >= 90:
> >         egg_label = "warning: egg might be dirty"
> >     elif mass >= 85:
> >         egg_label = "jumbo"
> >     elif mass >= 70:
> >         egg_label = "large"
> >     elif mass < 70 and mass >= 55:
> >         egg_label = "medium"
> >     elif mass < 50:
> >         egg_label = "too light, probably spoiled"
> >     else:
> >         egg_label = "small"
> >     return egg_label
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Encapsulando um bloco If/Else
>
> O código abaixo vai imprimir etiquetas para ovos de galinha. Uma balança digital vai reportar a massa de um ovo (em gramas)
> para o computador e o computador precisa imprimir uma etiqueta.
>
> Por favor reescreva o código abaixo para que o bloco de if seja dobrado em uma função.
>
> ~~~
> import random
> for i in range(10):
>
>     # simulando a massa de um ovo de galinha
>     # o valor (aleatório) será de 70 +/- 20 gramas
>     massa = 70 + 20.0 * (2.0 * random.random() - 1.0)
>
>     print(massa)
>    
>     # a maquinaria de pesos de ovos imprime um valor
>     if massa >= 85:
>        print("jumbo")
>     elif massa >= 70:
>        print("grande")
>     elif massa < 70 and massa >= 55:
>        print("médio")
>     else:
>        print("pequeno")
> ~~~
> {: .language-python}
>
>
> O programa simplificado está a seguir. Que definição de função o tornará funcional?
>
> ~~~
> # versão revisada
> import random
> for i in range(10):
>
>     # simulando a massa de um ovo de galinha
>     # o valor (aleatório) será de 70 +/- 20 gramas
>     massa = 70 + 20.0 * (2.0 * random.random() - 1.0)
>
>     print(massa, calcular_etiqueta(massa))    
>
> ~~~
> {: .language-python}
>
>
> 1. Crie uma definição de função para `calcular_etiqueta()` que vai funcionar com o programa revisado acima.  Note que o valor de retorno da função `calcular_etiqueta()` será importante. Um exemplo de saída desse programa seria `71.23 grande`.
> 2. Um ovo sujo pode ter uma massa de mais de 90 gramas, e um ovo podre ou quebrado provavelmente vai ter uma massa menor que 50 gramas.  Modifique sua função `calcular_etiqueta()` para levar em conta essas condições de erro. Uma saída de exemplo poderia ser `25 muito leve, algo de errado`.
>
> > ## Solução
> >
> > ~~~
> > def calcular_etiqueta(massa):
> >     # egg sizing machinery prints a label
> >     etiqueta_ovo = "sem etiqueta"
> >     if massa >= 90:
> >         etiqueta_ovo = "aviso: o ovo pode estar sujo"
> >     elif massa >= 85:
> >         etiqueta_ovo = "jumbo"
> >     elif massa >= 70:
> >         etiqueta_ovo = "grande"
> >     elif massa < 70 and massa >= 55:
> >         etiqueta_ovo = "médio"
> >     elif massa < 50:
> >         etiqueta_ovo = "muito leve, algo de errado"
> >     else:
> >         etiqueta_ovo = "pequeno"
> >     return etiqueta_ovo
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

<!-- 
> ## Encapsulating Data Analysis
>
> Assume that the following code has been executed:
>
> ~~~
> import pandas as pd
>
> df = pd.read_csv('data/gapminder_gdp_asia.csv', index_col=0)
> japan = df.loc['Japan']
> ~~~
> {: .language-python}
>
> 1. Complete the statements below to obtain the average GDP for Japan
>    across the years reported for the 1980s.
>
>     ~~~
>     year = 1983
>     gdp_decade = 'gdpPercap_' + str(year // ____)
>     avg = (japan.loc[gdp_decade + ___] + japan.loc[gdp_decade + ___]) / 2
>     ~~~
>     {: .language-python}
>
> 2. Abstract the code above into a single function.
>
>     ~~~
>     def avg_gdp_in_decade(country, continent, year):
>         df = pd.read_csv('data/gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
>         ____
>         ____
>         ____
>         return avg
>     ~~~
>     {: .language-python}
>
> 3. How would you generalize this function
>    if you did not know beforehand which specific years occurred as columns in the data?
>    For instance, what if we also had data from years ending in 1 and 9 for each decade?
>    (Hint: use the columns to filter out the ones that correspond to the decade,
>    instead of enumerating them in the code.)
>
> > ## Solution
> >
> > 1. The average GDP for Japan across the years reported for the 1980s is computed with:
> >
> >     ~~~
> >     year = 1983
> >     gdp_decade = 'gdpPercap_' + str(year // 10)
> >     avg = (japan.loc[gdp_decade + '2'] + japan.loc[gdp_decade + '7']) / 2
> >     ~~~
> >     {: .language-python}
> >
> > 2. That code as a function is:
> >
> >     ~~~
> >     def avg_gdp_in_decade(country, continent, year):
> >         df = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
> >         c = df.loc[country]
> >         gdp_decade = 'gdpPercap_' + str(year // 10)
> >         avg = (c.loc[gdp_decade + '2'] + c.loc[gdp_decade + '7'])/2
> >         return avg
> >     ~~~
> >     {: .language-python}
> >
> > 3. To obtain the average for the relevant years, we need to loop over them:
> >
> >    ~~~
> >    def avg_gdp_in_decade(country, continent, year):
> >         df = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
> >         c = df.loc[country]
> >         gdp_decade = 'gdpPercap_' + str(year // 10)
> >         total = 0.0
> >         num_years = 0
> >         for yr_header in c.index: # c's index contains reported years
> >             if yr_header.startswith(gdp_decade):
> >                 total = total + c.loc[yr_header]
> >                 num_years = num_years + 1
> >         return total/num_years
> >     ~~~
> >     {: .language-python}
> >
> > The function can now be called by:
> >
> > ~~~
> > avg_gdp_in_decade('Japan','asia',1983)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > 20880.023800000003
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->
<!-- 
> ## Encapsulating Data Analysis
>
> Assume that the following code has been executed:
>
> ~~~
> import pandas as pd
>
> df = pd.read_csv('data/gapminder_gdp_asia.csv', index_col=0)
> japan = df.loc['Japan']
> ~~~
> {: .language-python}
>
> 1. Complete the statements below to obtain the average GDP for Japan
>    across the years reported for the 1980s.
>
>     ~~~
>     year = 1983
>     gdp_decade = 'gdpPercap_' + str(year // ____)
>     avg = (japan.loc[gdp_decade + ___] + japan.loc[gdp_decade + ___]) / 2
>     ~~~
>     {: .language-python}
>
> 2. Abstract the code above into a single function.
>
>     ~~~
>     def avg_gdp_in_decade(country, continent, year):
>         df = pd.read_csv('data/gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
>         ____
>         ____
>         ____
>         return avg
>     ~~~
>     {: .language-python}
>
> 3. How would you generalize this function
>    if you did not know beforehand which specific years occurred as columns in the data?
>    For instance, what if we also had data from years ending in 1 and 9 for each decade?
>    (Hint: use the columns to filter out the ones that correspond to the decade,
>    instead of enumerating them in the code.)
>
> > ## Solução
> >
> > 1. The average GDP for Japan across the years reported for the 1980s is computed with:
> >
> >     ~~~
> >     year = 1983
> >     gdp_decade = 'gdpPercap_' + str(year // 10)
> >     avg = (japan.loc[gdp_decade + '2'] + japan.loc[gdp_decade + '7']) / 2
> >     ~~~
> >     {: .language-python}
> >
> > 2. That code as a function is:
> >
> >     ~~~
> >     def avg_gdp_in_decade(country, continent, year):
> >         df = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
> >         c = df.loc[country]
> >         gdp_decade = 'gdpPercap_' + str(year // 10)
> >         avg = (c.loc[gdp_decade + '2'] + c.loc[gdp_decade + '7'])/2
> >         return avg
> >     ~~~
> >     {: .language-python}
> >
> > 3. To obtain the average for the relevant years, we need to loop over them:
> >
> >    ~~~
> >    def avg_gdp_in_decade(country, continent, year):
> >         df = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
> >         c = df.loc[country]
> >         gdp_decade = 'gdpPercap_' + str(year // 10)
> >         total = 0.0
> >         num_years = 0
> >         for yr_header in c.index: # c's index contains reported years
> >             if yr_header.startswith(gdp_decade):
> >                 total = total + c.loc[yr_header]
> >                 num_years = num_years + 1
> >         return total/num_years
> >     ~~~
> >     {: .language-python}
> >
> > The function can now be called by:
> >
> > ~~~
> > avg_gdp_in_decade('Japan','asia',1983)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > 20880.023800000003
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

<!-- 
> ## Simulating a dynamical system
>
> In mathematics, a [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) is a system
> in which a function describes the time dependence of a point in a geometrical space. A canonical
> example of a dynamical system is the [logistic map](https://en.wikipedia.org/wiki/Logistic_map),
> a growth model that computes a new population density (between  0 and 1) based on the current
> density. In the model, time takes discrete values 0, 1, 2, ...
>
> 1. Define a function called `logistic_map` that takes two inputs: `x`, representing the current
>    population (at time `t`), and a parameter `r = 1`. This function should return a value 
>    representing the state of the system (population) at time `t + 1`, using the mapping function:
>
>    `f(t+1) = r * f(t) * [1 - f(t)]`
>
> 2. Using a `for` or `while` loop, iterate the `logistic_map` function defined in part 1, starting
>    from an initial population of 0.5, for a period of time `t_final = 10`. Store the intermediate
>    results in a list so that after the loop terminates you have accumulated a sequence of values
>    representing the state of the logistic map at times `t = [0,1,...,t_final]`. Print this list to
>    see the evolution of the population.
>
> 3. Encapsulate the logic of your loop into a function called `iterate` that takes the initial
>    population as its first input, the parameter `t_final` as its second input and the parameter
>    `r` as its third input. The function should return the list of values representing the state of
>    the logistic map at times `t = [0,1,...,t_final]`. Run this function for periods `t_final = 100`
>    and `1000` and print some of the values. Is the population trending toward a steady state?
>
> > ## Solution
> >
> > 1. ~~~
> >    def logistic_map(x, r):
> >        return r * x * (1 - x)
> >    ~~~
> >    {: .language-python}
> >
> > 2. ~~~
> >    initial_population = 0.5
> >    t_final = 10
> >    r = 1.0
> >    population = [initial_population]
> >    for t in range(1, t_final):
> >        population.append( logistic_map(population[t-1], r) )
> >    ~~~
> >    {: .language-python}
> >
> > 3. ~~~
> >    def iterate(initial_population, t_final, r):
> >        population = [initial_population]
> >        for t in range(1, t_final):
> >            population.append( logistic_map(population[t-1], r) )
> >        return population
> >
> >    for period in (10, 100, 1000):
> >        population = iterate(0.5, period, 1)
> >        print(population[-1])
> >    ~~~
> >    {: .language-python}
> >    ~~~
> >    0.07508929631879595
> >    0.009485759503982033
> >    0.0009923756709128578
> >    ~~~
> >    {: .output}
> >    The population seems to be approaching zero.
> {: .solution}
{: .challenge}
 -->
<!-- 
> ## Simulating a dynamical system
>
> In mathematics, a [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) is a system
> in which a function describes the time dependence of a point in a geometrical space. A canonical
> example of a dynamical system is the [logistic map](https://en.wikipedia.org/wiki/Logistic_map),
> a growth model that computes a new population density (between  0 and 1) based on the current
> density. In the model, time takes discrete values 0, 1, 2, ...
>
> 1. Define a function called `logistic_map` that takes two inputs: `x`, representing the current
>    population (at time `t`), and a parameter `r = 1`. This function should return a value 
>    representing the state of the system (population) at time `t + 1`, using the mapping function:
>
>    `f(t+1) = r * f(t) * [1 - f(t)]`
>
> 2. Using a `for` or `while` loop, iterate the `logistic_map` function defined in part 1, starting
>    from an initial population of 0.5, for a period of time `t_final = 10`. Store the intermediate
>    results in a list so that after the loop terminates you have accumulated a sequence of values
>    representing the state of the logistic map at times `t = [0,1,...,t_final]`. Print this list to
>    see the evolution of the population.
>
> 3. Encapsulate the logic of your loop into a function called `iterate` that takes the initial
>    population as its first input, the parameter `t_final` as its second input and the parameter
>    `r` as its third input. The function should return the list of values representing the state of
>    the logistic map at times `t = [0,1,...,t_final]`. Run this function for periods `t_final = 100`
>    and `1000` and print some of the values. Is the population trending toward a steady state?
>
> > ## Solução
> >
> > 1. ~~~
> >    def logistic_map(x, r):
> >        return r * x * (1 - x)
> >    ~~~
> >    {: .language-python}
> >
> > 2. ~~~
> >    initial_population = 0.5
> >    t_final = 10
> >    r = 1.0
> >    population = [initial_population]
> >    for t in range(1, t_final):
> >        population.append( logistic_map(population[t-1], r) )
> >    ~~~
> >    {: .language-python}
> >
> > 3. ~~~
> >    def iterate(initial_population, t_final, r):
> >        population = [initial_population]
> >        for t in range(1, t_final):
> >            population.append( logistic_map(population[t-1], r) )
> >        return population
> >
> >    for period in (10, 100, 1000):
> >        population = iterate(0.5, period, 1)
> >        print(population[-1])
> >    ~~~
> >    {: .language-python}
> >    ~~~
> >    0.07508929631879595
> >    0.009485759503982033
> >    0.0009923756709128578
> >    ~~~
> >    {: .output}
> >    The population seems to be approaching zero.
> {: .solution}
{: .challenge}
 -->
