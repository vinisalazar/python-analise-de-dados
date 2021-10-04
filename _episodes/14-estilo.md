---
title: "Estilo de Programação"
teaching: 15
exercises: 15
questions:
- "Como posso tornar meus programas mais legíveis?"
- "Como pessoas que programam formatam seus códigos?"
- "Como programas podem checar sua própria operação?"
objectives:
- "Prover boas justificativas para regras básicas de estilo de código."
- "Refatore programas de uma página para torná-los mais legíveis e justifique as mudanças."
- "Use os standards da comunidade Python (PEP-8)."
keypoints:
- "Siga o estilo padrão do Python em seu código."
- "Use docstrings para adicionar ajuda embutida."
---

<!-- 
## Coding style

A consistent coding style helps others (including our future selves) read and understand code more easily. Code is read much more often than it is written, and as the [Zen of Python](https://www.python.org/dev/peps/pep-0020) states, "Readability counts".
Python proposed a standard style through one of its first Python Enhancement Proposals (PEP), [PEP8](https://www.python.org/dev/peps/pep-0008).

Some points worth highlighting:
*   document your code and ensure that assumptions, internal algorithms, expected inputs, expected outputs, etc., are clear
*   use clear, semantically meaningful variable names
*   use white-space, *not* tabs, to indent lines (tabs can cause problems across different text editors, operating systems, and version control systems)
 -->

## Estilo de Código.

Um estilo de código consistente ajuda outras pessoas (incluindo nós mesmos no futuro) a ler e entender o código mais facilmente.
Código é lido com muito mais frequência que é escrito, e o [Zen of Python](https://www.python.org/dev/peps/pep-0020) fala, "Legibilidade conta" ("*readability counts*).
O Python propôs um estilo padrão através de um dos primeiros *Python Enhancement Proposals* (PEP), a [PEP8](https://www.python.org/dev/peps/pep-0008).

Dois pontos que vale destacar:
*   Documente seu código e assegure que suposições, algoritmos internos, inputs e outputs esperados, etc. estejam claros.
*   Use nomes de variáveis que sejam claros e informativos.

<!-- 
## Follow standard Python style in your code.

*   [PEP8](https://www.python.org/dev/peps/pep-0008):
    a style guide for Python that discusses topics such as how to name variables,
    how to indent your code,
    how to structure your `import` statements,
    etc.
    Adhering to PEP8 makes it easier for other Python developers to read and understand your code, and to understand what their contributions should look like.
*   To check your code for compliance with PEP8, you can use the [pycodestyle application](https://pypi.org/project/pycodestyle/) and tools like the [black code formatter](https://github.com/psf/black) can automatically format your code to conform to PEP8 and pycodestyle (a Jupyter notebook formatter also exists [nb_black](https://github.com/dnanhkhoa/nb_black)).
*   Some groups and organizations follow different style guidelines besides PEP8. For example, the [Google style guide on Python](https://google.github.io/styleguide/pyguide.html) makes slightly different recommendations. Google wrote an application that can help you format your code in either their style or PEP8 called [yapf](https://github.com/google/yapf/).
*   With respect to coding style, the key is *consistency*. Choose a style for your project be it PEP8, the Google style, or something else and do your best to ensure that you and anyone else you are collaborating with sticks to it. Consistency within a project is often more impactful than the particular style used. A consistent style will make your software easier to read and understand for others and for your future self.
 -->

## Siga o estilo padrão do Python em seu código.

*   [PEP8](https://www.python.org/dev/peps/pep-0008): um guia de estilo de Python que discute tópicos sobre como nomear variáveis, como indentar seu código, como estruturar os `imports`, e outras coisas.
    Aderir a PEP8 torna mais fácil para que outros desenvolvedores Python consigam ler e entender seu código, e entender como suas contribuições devem ser.
*   Cheque que o seu código está em conformidade com a PEP8, usando [a aplicação pycodestyle](https://pypi.org/project/pycodestyle/) e ferramentas como o [formatador de código Black](https://github.com/psf/black), que pode formatar automaticamente seu código para estar em confirmidade com a PEP8 e o pycodestyle (também existe um foromatador para Jupyter Notebook chamado [nb_black](https://github.com/dnanhkhoa/nb_black)).
*   Alguns grupos e organizaççoes seguem diferentes diretrizes de estilo além da PEP8. Por exemplo, o [estilo de código Python da Google](https://google.github.io/styleguide/pyguide.html) faz recomendações ligeraimente diferentes. O Google escreveu uma aplicação chamada [yapf](https://github.com/google/yapf/) que ajuda a formatar o código no estilo deles ou da PEP8.
*   Em respeito ao estilo de código, a chave é **consistência**. Escolha um estilo para o seu projeto, que seja PEP8, o estilo Google, ou alguma outra coisa e faça o seu melhor para assegurar que você e qualquer outra pessoa que você esteja colaborando se atenham a ele. Consistência dentro de um projeto é mais impactante que qualquer estilo em particular. Um estilo consistente vai fazer com que seu código seja mais fácil de ler e entender para outros e para o seu eu no futuro.

<!-- 
## Use assertions to check for internal errors.

Assertions are a simple but powerful method for making sure that the context in which your code is executing is as you expect.

~~~
def calc_bulk_density(mass, volume):
    '''Return dry bulk density = powder mass / powder volume.'''
    assert volume > 0
    return mass / volume
~~~
{: .language-python}

If the assertion is `False`, the Python interpreter raises an `AssertionError` runtime exception. The source code for the expression that failed will be displayed as part of the error message. To ignore assertions in your code run the interpreter with the '-O' (optimize) switch. Assertions should contain only simple checks and never change the state of the program. For example, an assertion should never contain an assignment.
 -->

## Use asserções para checar por erros internos.

Asserções são uma forma simples mais poderosa de assegurar que o contexto que o seu código está sendo executado é como você espera.

~~~
def calcular_consumo_hora(consumo, tempo):
    '''Retorna o consumo de uma unidade em megawatts/hora.'''
    assert tempo > 0
    return consumo / tempo
~~~
{: .language-python}

Se a asserção é `False`, o interpretador Python lança uma exceção de runtime do tipo `AssertionError`. O código fonte para a expressão que falhou será mostrado como parte da mensagem de erro. Asserções devem conter somente checagens simples e nunca devem alterar o estado do programa. Por exemplo, uma asserção nunca deve conter uma assinalação.

<!-- 
## Use docstrings to provide builtin help.

If the first thing in a function is a character string that is not assigned directly to a variable, Python attaches it to the function, accessible via the builtin help function. This string that provides documentation is also known as a *docstring*.

~~~
def average(values):
    "Return average of values, or None if no values are supplied."

    if len(values) == 0:
        return None
    return sum(values) / len(values)

help(average)
~~~
{: .language-python}
~~~
Help on function average in module __main__:

average(values)
    Return average of values, or None if no values are supplied.
~~~
{: .output}
 -->

## Use docstrings para adicionar ajuda embutida.

Se a primeira coisa em uma função é uma string que não é assinalada diretamente a uma variável, o Python anexa ela à função, tornando-a acessível via a função de ajuda embutida (`help()`). Essa string que provê documentação também é conhecida como **docstring**.

~~~
def media(valores):
    "Retorna a média dos valores, ou None se nenhum valor é dado."

    if len(valores) == 0:
        return None
    return sum(valores) / len(valores)

help(media)
~~~
{: .language-python}
~~~
Help on function average in module __main__:

media(valores)
    Retorna a média dos valores, ou None se nenhum valor é dado.
~~~
{: .output}

<!-- 
> ## Multiline Strings
>
> Often use *multiline strings* for documentation.
> These start and end with three quote characters (either single or double)
> and end with three matching characters.
>
> ~~~
> """This string spans
> multiple lines.
>
> Blank lines are allowed."""
> ~~~
> {: .language-python}
{: .callout}
 -->

> ## Strings Multilinha
>
> É comum usar *strings multilinha* para documentação.
> Elas começam e terminam com três aspas (sejam simples ou duplas).
>
> ~~~
> """Essa string se alonga por
> múltiplas linhas.
>
> Linhas em branco são permitidas."""
> ~~~
> {: .language-python}
{: .callout}

<!-- 
> ## What Will Be Shown?
>
> Highlight the lines in the code below that will be available as online help.
> Are there lines that should be made available, but won't be?
> Will any lines produce a syntax error or a runtime error?
>
> ~~~
> "Find maximum edit distance between multiple sequences."
> # This finds the maximum distance between all sequences.
>
> def overall_max(sequences):
>     '''Determine overall maximum edit distance.'''
> 
>     highest = 0
>     for left in sequences:
>         for right in sequences:
>             '''Avoid checking sequence against itself.'''
>             if left != right:
>                 this = edit_distance(left, right)
>                 highest = max(highest, this)
> 
>     # Report.
>     return highest
> ~~~
> {: .language-python}
{: .challenge}
 -->

> ## O Que Será Mostrado?
>
> Destaque as linhas no código abaixo que estarão disponíveis como ajuda.
> Existem linhas que deviam se tornar disponíveis, mas não serão?
> Alguma linha vai produzir um erro de sintaxe ou erro de runtime?
>
> ~~~
> "Encontra a distância máxima entre múltiplas sequências."
> # Isso encontra a distância máxima entre todas as sequências.
>
> def maxima_geral(sequencias):
>     '''Determina a distância máxima de edição.'''
> 
>     maxima = 0
>     for esquerda in sequencias:
>         for direita in sequencias:
>             '''Evite checar uma sequência contra ela mesma.'''
>             if esquerda != direita:
>                 distancia = editar_distancia(esquerda, direita)
>                 maxima = max(maxima, distancia)
> 
>     # Reportar o valor final.
>     return maxima
> ~~~
> {: .language-python}
{: .challenge}

<!-- 
> ## Document This
>
> Turn the comment in the following function into a docstring
> and check that `help` displays it properly.
>
> ~~~
> def middle(a, b, c):
>     # Return the middle value of three.
>     # Assumes the values can actually be compared.
>     values = [a, b, c]
>     values.sort()
>     return values[1]
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > def middle(a, b, c):
> >     '''Return the middle value of three.
> >     Assumes the values can actually be compared.'''
> >     values = [a, b, c]
> >     values.sort()
> >     return values[1]
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Documente Isso
>
> Transforme o comentário da função a seguir em uma docstring
> e cheque que o `help` mostra ele corretamente.
>
> ~~~
> def meio(a, b, c):
>     # Retorna o valor do meio entre os três elementos.
>     # Assume que os valores podem de fato ser comparados.
>     valores = [a, b, c]
>     valores.sort()
>     return valores[1]
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > def meio(a, b, c):
> >     '''Retorna o valor do meio entre os três elementos.
> >     Assume que os valores podem de fato ser comparados.'''
> >     valores = [a, b, c]
> >     valores.sort()
> >     return valores[1]
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

<!-- 
> ## Clean Up This Code
>
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Remember to run it after each change to ensure its behavior hasn't changed.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
>
> ~~~
> n = 10
> s = 'et cetera'
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > Here's one solution.
> >
> > ~~~
> > def string_machine(input_string, iterations):
> >     """
> >     Takes input_string and generates a new string with -'s and *'s
> >     corresponding to characters that have identical adjacent characters
> >     or not, respectively.  Iterates through this procedure with the resultant
> >     strings for the supplied number of iterations.
> >     """
> >     print(input_string)
> >     input_string_length = len(input_string)
> >     old = input_string
> >     for i in range(iterations):
> >         new = ''
> >         # iterate through characters in previous string
> >         for j in range(input_string_length):
> >             left = j-1
> >             right = (j+1) % input_string_length  # ensure right index wraps around
> >             if old[left] == old[right]:
> >                 new += '-'
> >             else:
> >                 new += '*'
> >         print(new)
> >         # store new string as old
> >         old = new     
> >
> > string_machine('et cetera', 10)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > et cetera
> > *****-***
> > ----*-*--
> > ---*---*-
> > --*-*-*-*
> > **-------
> > ***-----*
> > --**---**
> > *****-***
> > ----*-*--
> > ---*---*-
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}\
 -->
<!-- 
> ## Clean Up This Code
>
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Remember to run it after each change to ensure its behavior hasn't changed.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
>
> ~~~
> n = 10
> s = 'et cetera'
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > Here's one solution.
> >
> > ~~~
> > def string_machine(input_string, iterations):
> >     """
> >     Takes input_string and generates a new string with -'s and *'s
> >     corresponding to characters that have identical adjacent characters
> >     or not, respectively.  Iterates through this procedure with the resultant
> >     strings for the supplied number of iterations.
> >     """
> >     print(input_string)
> >     input_string_length = len(input_string)
> >     old = input_string
> >     for i in range(iterations):
> >         new = ''
> >         # iterate through characters in previous string
> >         for j in range(input_string_length):
> >             left = j-1
> >             right = (j+1) % input_string_length  # ensure right index wraps around
> >             if old[left] == old[right]:
> >                 new += '-'
> >             else:
> >                 new += '*'
> >         print(new)
> >         # store new string as old
> >         old = new     
> >
> > string_machine('et cetera', 10)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > et cetera
> > *****-***
> > ----*-*--
> > ---*---*-
> > --*-*-*-*
> > **-------
> > ***-----*
> > --**---**
> > *****-***
> > ----*-*--
> > ---*---*-
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->
