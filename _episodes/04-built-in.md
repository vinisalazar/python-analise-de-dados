---
title: "Funções Embutidas e Ajuda"
teaching: 15
exercises: 10
questions:
- "Como posso usar funções embutidas?"
- "Como posso descobrir o que elas fazem?"
- "Que tipos de erros podem ocorrer em progamas?"
objectives:
- "Explique o propósito de funções."
- "Chame corretamente funções Python."
- "Aninhe chamadas de funções corretamente."
- "Use o help para mostrar documentação para funções embutidas."
- "Corretamente descreva situações nas quais `SyntaxError` e `NameError` podem ocorrer."
keypoints:
- "Use comentários para adicionar documentação a programas."
- "Uma função pode receber zero ou mais argumentos."
- "Funções embutidas comumente utilizadas incluem `max`, `min` e `round`."
- "Funções podem funcionar somente para certos(as) (combinações de) argumentos."
- "Funções podem ter valores padrão para alguns argumentos."
- "Use a função embutida `help` para conseguir ajuda sobre uma função."
- "O Jupyter Notebook tem duas formas de obter ajuda."
- "Toda função retorna algo."
- "Python reporta um erro de sintaxe quando ele não consegue entender a fonte de um programa."
- "Python reporta um erro de *runtime* quando algo dá errado enquanto o programa está sendo executado."
- "Conserte erros de sintaxe lendo o código fonte do programa, e erros de *runtime* monitorando a execução do programa."
---
## Use comentários para adicionar documentação a programas.
<!-- 
~~~
# This sentence isn't executed by Python.
adjustment = 0.5   # Neither is this - anything after '#' is ignored.
~~~
{: .language-python}
 -->

~~~
# Essa frase não é executada pelo Python
ajuste = 0.5   # Nem essa - qualquer coisa depois do '#' é ignorado.
~~~
{: .language-python}

## Uma função pode receber zero ou mais argumentos.
<!-- 
*   We have seen some functions already --- now let's take a closer look.
*   An *argument* is a value passed into a function.
*   `len` takes exactly one.
*   `int`, `str`, and `float` create a new value from an existing one.
*   `print` takes zero or more.
*   `print` with no arguments prints a blank line.
    *   Must always use parentheses, even if they're empty,
        so that Python knows a function is being called.

~~~
print('before')
print()
print('after')
~~~
{: .language-python}
~~~
before

after
~~~
{: .output}
 -->

*   Já vimos algumas funções --- agora vamos olhar mais de perto.
*   Um *argumento* é um valor passado para uma função.
*   `len` recebe exatamente um.
*   `int`, `str`, e `float` criam um novo valor de um existente.
*   `print` recebe zero ou mais.
*   `print` sem nenhum argumento imprime uma linha em branco.
    *   É sempre necessário usar parênteses, mesmo que em branco,
        para que o Python saiba que uma função está sendo chamada.


~~~
print('antes')
print()
print('depois')
~~~
{: .language-python}
~~~
antes

depois
~~~
{: .output}

<!-- 
## Every function returns something.

*   Every function call produces some result.
*   If the function doesn't have a useful result to return,
    it usually returns the special value `None`. `None` is a Python
    object that stands in anytime there is no value.
~~~
result = print('example')
print('result of print is', result)
~~~
{: .language-python}
~~~
example
result of print is None
~~~
{: .output}
 -->

## Toda função retorna algo.

*   Toda chamada de função produz algum resultado.
*   Se a função não tem um resultado útil para retornar,
    normalmente ela retorna o valor especial `None`. `None` é um objeto
    Python que pode substituir quando não temos nenhum valor.

~~~
resultado = print('exemplo')
print('resultado de print é', resultado)
~~~
{: .language-python}
~~~
exemplo
resultado de print é None
~~~
{: .output}

<!-- 
## Commonly-used built-in functions include `max`, `min`, and `round`.

*   Use `max` to find the largest value of one or more values.
*   Use `min` to find the smallest.
*   Both work on character strings as well as numbers.
    *   "Larger" and "smaller" use (0-9, A-Z, a-z) to compare letters.

~~~
print(max(1, 2, 3))
print(min('a', 'A', '0'))
~~~
{: .language-python}
~~~
3
0
~~~
{: .output}
 -->

## Funções embutidas comumente usadas incluem `max`, `min` e `round`.

*   Use `max` para encontrar o maior valor de um ou mais valores.
*   Use `min` para encontrar o menor.
*   Ambos funcionam em strings de caracteres, bem como números.
    *   "Maior" e "menor" usam (0-9, A-Z, a-z) para comparar letras.

~~~
print(max(1, 2, 3))
print(min('a', 'A', '0'))
~~~
{: .language-python}
~~~
3
0
~~~
{: .output}

## Funções podem funcionar somente para certos(as) (combinações de) argumentos.
<!-- 
*   `max` and `min` must be given at least one argument.
    *   "Largest of the empty set" is a meaningless question.
*   And they must be given things that can meaningfully be compared.

~~~
print(max(1, 'a'))
~~~
{: .language-python}
~~~
TypeError                                 Traceback (most recent call last)
<ipython-input-52-3f049acf3762> in <module>
---- 1 print(max(1, 'a'))

TypeError: '>' not supported between instances of 'str' and 'int'
~~~
{: .error}
 -->

*   `max` e `min` devem ser dados pelo menos um argumento.
    *   "Maior de um conjunto vazio" é uma pergunta sem sentido.
*   Essas funções devem ser dadas coisas que podem ser comparadas.

~~~
print(max(1, 'a'))
~~~
{: .language-python}
~~~
TypeError                                 Traceback (most recent call last)
<ipython-input-52-3f049acf3762> in <module>
----> 1 print(max(1, 'a'))

TypeError: '>' not supported between instances of 'str' and 'int'
~~~
{: .error}

## Funções podem ter valores padrão para alguns argumentos.
<!-- 
*   `round` will round off a floating-point number.
*   By default, rounds to zero decimal places.

~~~
round(3.712)
~~~
{: .language-python}
~~~
4
~~~
{: .output}

*   We can specify the number of decimal places we want.

~~~
round(3.712, 1)
~~~
{: .language-python}
~~~
3.7
~~~
{: .output}
 -->


*   `round` vai arrendondar um número de ponto flutuante.
*   Por padrão, ele vai arredondar para zero casas decimais.

~~~
round(3.712)
~~~
{: .language-python}
~~~
4
~~~
{: .output}

*   Podemos especificar o número de casas decimais que queremos.

~~~
round(3.712, 1)
~~~
{: .language-python}
~~~
3.7
~~~
{: .output}

## Funções associadas a objetos são chamadas de métodos.
<!-- 
* Functions take another form that will be common in the pandas episodes.
* Methods have parentheses like functions, but come after the variable.
* Some methods are used for internal Python operations, and are marked with double underlines.

~~~
my_string = 'Hello world!'  # creation of a string object 

print(len(my_string))       # the len function takes a string as an argument and returns the length of the string

print(my_string.swapcase()) # calling the swapcase method on the my_string object

print(my_string.__len__())  # calling the internal __len__ method on the my_string object, used by len(my_string)

~~~
{: .language-python}

~~~
12
hELLO WORLD!
12
~~~
{: .output}

* You might even see them chained together.  They operate left to right.

~~~
print(my_string.isupper())          # Not all the letters are uppercase
print(my_string.upper())            # This capitalizes all the letters

print(my_string.upper().isupper())  # Now all the letters are uppercase
~~~
{: .language-python}

~~~
False
HELLO WORLD
True
~~~
{: .output}
 -->

* Funções tomam outra forma que vão ser comum quando chegarmos em Análise de Dados.
* Métodos tem parênteses como funções, mas vem depois da variável.
* Alguns métodos podem ser usados para operações internas do Python, e são marcados com dois underlines.

~~~
minha_string = 'Olá Mundo'    # criação de um objeto string

print(len(minha_string))       # a função len recebe uma string como argumento e retorna o comprimento da string

print(minha_string.swapcase()) # chamando o método swapcase no objeto minha_string

print(minha_string.__len__())  # chamando o método interno __len__ no objeto minha string, usado por len(minha_string)

~~~
{: .language-python}

~~~
9
oLÁ mUNDO
9
~~~
{: .output}

* You might even see them chained together.  They operate left to right.

~~~
print(minha_string.isupper())          # Not all the letters are uppercase
print(minha_string.upper())            # This capitalizes all the letters

print(minha_string.upper().isupper())  # Now all the letters are uppercase
~~~
{: .language-python}

~~~
False
OLÁ MUNDO
True
~~~
{: .output}

## Use a função embutida `help` para obter ajuda para uma função.
<!-- 
*   Every built-in function has online documentation.

~~~
help(round)
~~~
{: .language-python}
~~~
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
~~~
{: .output}
 -->

*   Toda função embutida tem documentação online.

~~~
help(round)
~~~
{: .language-python}
~~~
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
~~~
{: .output}

## O Jupyter Notebook tem duas formas de obter ajuda.
<!-- 
*   Option 1: Place the cursor near where the function is invoked in a cell
    (i.e., the function name or its parameters),
    * Hold down <kbd>Shift</kbd>, and press <kbd>Tab</kbd>.
    * Do this several times to expand the information returned.
*   Option 2: Type the function name in a cell with a question mark after it. Then run the cell.
 -->

*   Opção 1: Posicione o cursor onde a função é invocada em uma célula
    (*i.e.*, o nome da função ou seus parâmetros),
    * Segure <kbd>Shift</kbd>, e aperte <kbd>Tab</kbd>.
    * Faça isso algumas vezes para expandir a informação retornada.
*   Opção 2: Digite o nome da função em uma célula com uma interrogação após ele. Execute a célula.


## Python reporta um erro de sintaxe quando ele não consegue entender a fonte de um programa.
<!-- 
*   Won't even try to run the program if it can't be parsed.

~~~
# Forgot to close the quote marks around the string.
name = 'Feng
~~~
{: .language-python}
~~~
  File "<ipython-input-56-f42768451d55>", line 2
    name = 'Feng
                ^
SyntaxError: EOL while scanning string literal
~~~
{: .error}

~~~
# An extra '=' in the assignment.
age = = 52
~~~
{: .language-python}
~~~
  File "<ipython-input-57-ccc3df3cf902>", line 2
    age = = 52
          ^
SyntaxError: invalid syntax
~~~
{: .error}

*   Look more closely at the error message:

~~~
print("hello world"
~~~
{: .language-python}
~~~
  File "<ipython-input-6-d1cc229bf815>", line 1
    print ("hello world"
                        ^
SyntaxError: unexpected EOF while parsing
~~~
{: .error}

*   The message indicates a problem on first line of the input ("line 1").
    *   In this case the "ipython-input" section of the file name tells us that
        we are working with input into IPython,
        the Python interpreter used by the Jupyter Notebook.
*   The `-6-` part of the filename indicates that
    the error occurred in cell 6 of our Notebook.
*   Next is the problematic line of code,
    indicating the problem with a `^` pointer.
 -->

*   O Python nem vai tentar rodar o programa se ele não pode ser avaliado.

~~~
# Esqueceu de fechar as apas na string
nome = 'CPFL
~~~
{: .language-python}
~~~
  File "<ipython-input-56-f42768451d55>", line 2
    nome = 'CPFL
                ^
SyntaxError: EOL while scanning string literal
~~~
{: .error}

~~~
# Um '=' a mais na assinalação
idade = = 52
~~~
{: .language-python}
~~~
  File "<ipython-input-57-ccc3df3cf902>", line 2
    idade = = 52
            ^
SyntaxError: invalid syntax
~~~
{: .error}

*   Olhe mais de perto essa mensagem de erro:

~~~
print("olá mundo"
~~~
{: .language-python}
~~~
  File "<ipython-input-6-d1cc229bf815>", line 1
    print ("olá mundo"
                      ^
SyntaxError: unexpected EOF while parsing
~~~
{: .error}

*   Essa mensagem indica um problema na primeira linha de input ("line 1").
    *   Nesse caso a seção "ipython-input" do arquivo nos diz
        que estamos trabalhando com input no IPython,
        o interpretador Python usado pelo Jupyter Notebook.
*   A parte `-6-` do nome de arquivo indica que
    o erro ocorreu na célula 6 do nosso Notebook.
*   Em seguida está a linha de código problemática,
    indicando o problema com um ponteiro `^`.

## <a name='runtime-error'></a> Python reporta um erro de *runtime* quando algo dá errado enquanto o programa está sendo executado.
<!-- 
~~~
age = 53
remaining = 100 - aege # mis-spelled 'age'
~~~
{: .language-python}
~~~
NameError                                 Traceback (most recent call last)
<ipython-input-59-1214fb6c55fc> in <module>
      1 age = 53
---- 2 remaining = 100 - aege # mis-spelled 'age'

NameError: name 'aege' is not defined
~~~
{: .error}

*   Fix syntax errors by reading the source and runtime errors by tracing execution.
 -->

~~~
pessoas = 53
restantes = 100 - ppessoas # escreveu 'pessoas' errado
~~~
{: .language-python}
~~~
NameError                                 Traceback (most recent call last)
<ipython-input-59-1214fb6c55fc> in <module>
      1 pessoas = 53
----> 2 restantes = 100 - ppessoas # escreveu 'pessoas' errado

NameError: name 'ppessoas' is not defined
~~~
{: .error}

*   Conserte os erros de sintaxe lendo a fonte e os erros de *runtime* monitorando a execução.

<!-- 
> ## What Happens When
>
> 1. Explain in simple terms the order of operations in the following program:
>    when does the addition happen, when does the subtraction happen,
>    when is each function called, etc.
> 2. What is the final value of `radiance`?
>
> ~~~
> radiance = 1.0
> radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
> ~~~
> {: .language-python}
> > ## Solution
> > 1. Order of operations:
> >    1. `1.1 * radiance = 1.1`
> >    2. `1.1 - 0.5 = 0.6`
> >    3. `min(radiance, 0.6) = 0.6`
> >    4. `2.0 + 0.6 = 2.6`
> >    5. `max(2.1, 2.6) = 2.6`
> > 2. At the end, `radiance = 2.6`
> {: .solution}
{: .challenge}
 -->

> ## O Que Acontece Quando
>
> 1. Explique em termos simples de ordem de operações o seguinte programa:
>    quando a adição acontece, quando a subtração acontece,
>    o que cada função é chamada, etc.
> 2. Qual é o valor final de `radiancia`?
>
> ~~~
> radiancia = 1.0
> radiancia = max(2.1, 2.0 + min(radiancia, 1.1 * radiancia - 0.5))
> ~~~
> {: .language-python}
>
> > ## Solução
> > 1. Ordem das operações:
> >    1. `1.1 * radiancia = 1.1`
> >    2. `1.1 - 0.5 = 0.6`
> >    3. `min(radiancia, 0.6) = 0.6`
> >    4. `2.0 + 0.6 = 2.6`
> >    5. `max(2.1, 2.6) = 2.6`
> > 2. No fim, `radiancia = 2.6`
> {: .solution}
{: .challenge}
<!-- 
> ## Spot the Difference
>
> 1. Predict what each of the `print` statements in the program below will print.
> 2. Does `max(len(rich), poor)` run or produce an error message?
>    If it runs, does its result make any sense?
>
> ~~~
> easy_string = "abc"
> print(max(easy_string))
> rich = "gold"
> poor = "tin"
> print(max(rich, poor))
> print(max(len(rich), len(poor)))
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > print(max(easy_string))
> > ~~~
> > {: .language-python}
> > ~~~
> > c
> > ~~~
> > {: .output}
> > ~~~
> > print(max(rich, poor))
> > ~~~
> > {: .language-python}
> > ~~~
> > tin
> > ~~~
> > {: .output}
> > ~~~
> > print(max(len(rich), len(poor)))
> > ~~~
> > {: .language-python}
> > ~~~
> > 4
> > ~~~
> > {: .output}
> > `max(len(rich), poor)` throws a TypeError. This turns into `max(4, 'tin')` and 
> > as we discussed earlier a string and integer cannot meaningfully be compared.
> > ~~~
> > TypeError                                 Traceback (most recent call last)
> > <ipython-input-65-bc82ad05177a> in <module>
> > ---- 1 max(len(rich), poor)
> > 
> > TypeError: '>' not supported between instances of 'str' and 'int'
> > ~~~
> > {: .error }
> {: .solution}
{: .challenge}
 -->

> ## Identifique a Diferença
>
> 1. Faça um predição do que cada declaração `print` no programa abaixo vai imprimir.
> 2. A linha `max(len(rich), poor)` roda ou produz uma mensagem de erro?
>    Se ela roda, o resultado faz sentido?
>
> ~~~
> string_facil = "abc"
> print(max(string_facil))
> rico = "ouro"
> pobre = "latão"
> print(max(rico, pobre))
> print(max(len(rico), len(pobre)))
> ~~~
> {: .language-python}
> > ## Solução
> > ~~~
> > print(max(string_facil))
> > ~~~
> > {: .language-python}
> > ~~~
> > c
> > ~~~
> > {: .output}
> > ~~~
> > print(max(rico, pobre))
> > ~~~
> > {: .language-python}
> > ~~~
> > ouro
> > ~~~
> > {: .output}
> > ~~~
> > print(max(len(rico), len(pobre)))
> > ~~~
> > {: .language-python}
> > ~~~
> > 5
> > ~~~
> > {: .output}
> > `max(len(rico), pobre)` retorna um TypeError. Essa avalia para `max(4, 'latão')` e 
> > e como discutimos mais cedo uma string e um inteiro não podem ser comparados com sentido.
> > ~~~
> > TypeError                                 Traceback (most recent call last)
> > <ipython-input-65-bc82ad05177a> in <module>
> > ----> 1 max(len(rico), pobre)
> > 
> > TypeError: '>' not supported between instances of 'str' and 'int'
> > ~~~
> > {: .error }
> {: .solution}
{: .challenge}
<!-- 
> ## Why Not?
>
> Why is it that `max` and `min` do not return `None` when they are called with no arguments?
>
> > ## Solution
> > `max` and `min` return TypeErrors in this case because the correct number of parameters
> > was not supplied. If it just returned `None`, the error would be much harder to trace as it
> > would likely be stored into a variable and used later in the program, only to likely throw
> > a runtime error.
> {: .solution}
{: .challenge}
 -->

> ## Por que não?
>
> Por que `max` e `min` não retornam `None` quando são chamados sem argumentos?
>
> > ## Solução
> > `max` e `min` retornam TypeErrors nesse caso porque o número correto de argumentos
> > não foi utilizado. Se só retornasse `None`, o erro seria bem mais difícil de encontrar pois
> > provavelmente seria armazenado em uma variável e usado mais a frente no programa, para então causar
> > um erro de *runtime*.
> {: .solution}
{: .challenge}
<!-- 
> ## Last Character of a String
>
> If Python starts counting from zero,
> and `len` returns the number of characters in a string,
> what index expression will get the last character in the string `name`?
> (Note: we will see a simpler way to do this in a later episode.)
>
> > ## Solution
> >
> > `name[len(name) - 1]`
> {: .solution}
{: .challenge}
 -->

> ## Último Caracter de Uma String
>
> Se o Python começa a contar do zero,
> e `len` retorna o número de caracteres de uma string,
> que expressão de index vai dar o último caracter da string `nome`?
> (Nota: vamos ver uma maneira mais simples de fazer isso em um episódio mais para frente.)
>
> > ## Solução
> >
> > `nome[len(nome) - 1]`
> {: .solution}
{: .challenge}
<!-- 
> ## Explore the Python docs!
>
> The [official Python documentation](https://docs.python.org/3/) is arguably the most complete
> source of information about the language. It is available in different languages and contains a lot of useful
> resources. The [Built-in Functions page](https://docs.python.org/3/library/functions.html) contains a catalogue of
> all of these functions, including the ones that we've covered in this lesson. Some of these are more advanced and 
> unnecessary at the moment, but others are very simple and useful.
> 
{: .callout}
 -->
> ## Explore a Documentação do Python!
>
> A [documentação oficial do Python](https://docs.python.org/pt-br/3/) é provavelmente a mais completa
> fonte de informação sobre a linguagem. Está disponível em diferentes idiomas e contém muitos recursos
> úteis. A [página de funções embutidas](https://docs.python.org/pt-br/3/library/functions.html) contém um catálogo de
> todas essas funções, incluindo aquelas que cobrimos nessa aula. Algumas dessas são mais avançadas e
> desnecessárias nesse momento, mas outras são muito simples e úteis.
> 
{: .callout}