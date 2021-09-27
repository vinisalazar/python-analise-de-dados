---
title: "Bibliotecas"
teaching: 10
exercises: 10
questions:
- "Como posso usar software que outras pessoas escreveram"
- "Como posso descobrir o que um software faz?"
objectives:
- "Explicar o que são bibliotecas de software e por que pessoas programadoras as criam e usam."
- "Escrever programas que importam e usam módulos da biblioteca padrão do Python."
- "Encontre e leia documentação para a biblioteca padrão interativamente (no interpretador) e online."
keypoints:
- "A maior parte do poder de uma linguagem de programação está em suas bibliotecas."
- "Um programa deve importar um módulo de uma biblioteca para poder utilizá-lo."
- "Use `help` para aprender sobre os conteúdos de um módulo de uma biblioteca."
- "Importe itens específicos de uma biblioteca para encurtar programas."
- "Crie um atalho para uma biblioteca quando importá-la para encurtar programas."
---
<!-- 
## Most of the power of a programming language is in its libraries.

*   A *library* is a collection of files (called *modules*) that contains
    functions for use by other programs.
    *   May also contain data values (e.g., numerical constants) and other things.
    *   Library's contents are supposed to be related, but there's no way to enforce that.
*   The Python [standard library][stdlib] is an extensive suite of modules that comes
    with Python itself.
*   Many additional libraries are available from [PyPI][pypi] (the Python Package Index).
*   We will see later how to write new libraries.
 -->
## A maior parte do poder de uma linguagem de programação está em suas bibliotecas.

*   Uma biblioteca é uma coleção de arquivos (chamados *módulos*) que contém
    funções para uso em outros programas.
    *   Também pode conter dados específicos (e.g., constantes numéricas) e outras coisas.
    *   O conteúdo de uma biblioteca deve ser relacionado, mas não há uma forma de garantir isso.
*   A [biblioteca padrão do Python][stdlib] é uma suíte extensa de módulos que vem
    com o próprio Python.
*   Muitas bibliotecas adicionais estão disponíveis no [PyPI][pypi] (o *Python Package Index*).
*   Vamos ver depois como escrever novas bibliotecas.

<!-- 
> ## Libraries and modules
>
> A library is a collection of modules, but the terms are often used
> interchangeably, especially since many libraries only consist of a single
> module, so don't worry if you mix them.
{: .callout}
 -->

> ## Bibliotecas e Módulos
>
> Uma biblioteca é uma coleção de módulos, mas os termos são frequentemente
> usados de forma intercambiável, especialmente porque muitas bibliotecas consistém de um único
> módulo, então não se preocupe se você misturar os termos.
{: .callout}

<!-- 
## A program must import a library module before using it.

*   Use `import` to load a library module into a program's memory.
*   Then refer to things from the module as `module_name.thing_name`.
    *   Python uses `.` to mean "part of".
*   Using `math`, one of the modules in the standard library:

~~~
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))
~~~
{: .language-python}
~~~
pi is 3.141592653589793
cos(pi) is -1.0
~~~
{: .output}

*   Have to refer to each item with the module's name.
    *   `math.cos(pi)` won't work: the reference to `pi`
        doesn't somehow "inherit" the function's reference to `math`.
 -->

## Um programa deve importar um módulo de uma biblioteca para poder utilizá-lo.

*   Use `import` para carregar uma biblioteca na memória de um programa.
*   Se refira a coisas do módulo como `nome_modulo.nome_coisa`.
    *   Python usa `.` para se referir a "parte de".
*   Usando `math`, um dos módulos da biblioteca padrão:

~~~
import math

print('pi é', math.pi)
print('cosseno de pi é', math.cos(math.pi))
~~~
{: .language-python}
~~~
pi is 3.141592653589793
cosseno de pi é -1.0
~~~
{: .output}

*   Temos que nos referir a cada item com o nome do módulo.
    *   `math.cos(pi)` não vai funcionar: a referência para `pi`
        não "herda" a referência da função para `math`.

## Use `help` para aprender sobre os conteúdos de um módulo de uma biblioteca.

*   Funciona assim como help para uma função.

~~~
help(math)
~~~
{: .language-python}
~~~
Help on module math:

NAME
    math

MODULE REFERENCE
    http://docs.python.org/3/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
⋮ ⋮ ⋮
~~~
{: .output}
<!-- 
## Import specific items from a library module to shorten programs.

*   Use `from ... import ...` to load only specific items from a library module.
*   Then refer to them directly without library name as prefix.

~~~
from math import cos, pi

print('cos(pi) is', cos(pi))
~~~
{: .language-python}
~~~
cos(pi) is -1.0
~~~
{: .output}
 -->

## Importe itens específicos de uma biblioteca para encurtar programas.

*   Use `from ... import ...` para carregar somente itens específicos de um módulo de uma biblioteca.
*   Então se refira a eles diretamente sem o nome da biblioteca como prefixo.

~~~
from math import cos, pi

print('cosseno de pi é', cos(pi))
~~~
{: .language-python}
~~~
cosseno de pi é -1.0
~~~
{: .output}
<!-- 
## Create an alias for a library module when importing it to shorten programs.

*   Use `import ... as ...` to give a library a short *alias* while importing it.
*   Then refer to items in the library using that shortened name.

~~~
import math as m

print('cos(pi) is', m.cos(m.pi))
~~~
{: .language-python}
~~~
cos(pi) is -1.0
~~~
{: .output}

*   Commonly used for libraries that are frequently used or have long names.
    *   E.g., the `matplotlib` plotting library is often aliased as `mpl`.
*   But can make programs harder to understand,
    since readers must learn your program's aliases.
 -->
<!-- 
## Create an alias for a library module when importing it to shorten programs.

*   Use `import ... as ...` to give a library a short *alias* while importing it.
*   Then refer to items in the library using that shortened name.

~~~
import math as m

print('cos(pi) is', m.cos(m.pi))
~~~
{: .language-python}
~~~
cos(pi) is -1.0
~~~
{: .output}

*   Commonly used for libraries that are frequently used or have long names.
    *   E.g., the `matplotlib` plotting library is often aliased as `mpl`.
*   But can make programs harder to understand,
    since readers must learn your program's aliases.
 -->

## Crie um atalho para uma biblioteca quando importá-la para encurtar programas.

*   Use `import ... as ...` para dar um atalho (*alias*) a uma biblioteca quando importá-la.
*   Então se refira aos itens da biblioteca usando aquele nome encurtado.

~~~
import math as m

print('cosseno de pi é', m.cos(m.pi))
~~~
{: .language-python}
~~~
cosseno de pi é -1.0
~~~
{: .output}

*   É comum usar atalhos para bibliotecas que são frequentemente utilizadas ou que têm nomes longos.
    *   E.g., a biblioteca de plotagem `matplotlib` é comumente abreviada de `mpl`.
*   Mas isso pode tornar programas mais difíceis de entender,
    já que leitores precisam aprender os atalhos do seu programa.

<!-- 
> ## Exploring the Math Module
>
> 1. What function from the `math` module can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
>
> > ## Solution
> > 1. Using `help(math)` we see that we've got `pow(x,y)` in addition to `sqrt(x)`,
> >    so we could use `pow(x, 0.5)` to find a square root.
> > 2. The `sqrt(x)` function is arguably more readable than `pow(x, 0.5)` when
> >    implementing equations. Readability is a cornerstone of good programming, so it
> >    makes sense to provide a special function for this specific common case.
> >
> >    Also, the design of Python's `math` library has its origin in the C standard,
> >    which includes both `sqrt(x)` and `pow(x,y)`, so a little bit of the history
> >    of programming is showing in Python's function names.
> {: .solution}
{: .challenge}
 -->

> ## Explorando o módulo `math`
>
> 1. Que função do módulo `math` podemos usar para calcular a raíz quadrada
>    *sem* usar `sqrt`?
> 2. Já que a biblioteca contém essa função, por que `sqrt` existe?
>
> > ## Solução
> > 1. Usando `help(math)`, vemos que temos `pow(x, y)`, além de `sqrt(x)`,
> >    então podemos usar `pow(x, 0.5)` para encontrar a raíz quadrada.
> > 2. A função `sqrt(x)` é consideravelmente mais legível do que `pow(x, 0.5)` quando
> >    estamos implementando equações. Legibilidade é a fundação de boa programação, então
> >    faz sentido prover uma função especial para esse caso de uso comum.
> >
> >    Também, o design do módulo `math` do Python tem sua origem no padrão C,
> >    que inclue ambas `sqrt(x)` e `pow(x, y)`, então é um pouco da história
> >    da programação que aparece nos nomes de função do Python.
> {: .solution}
{: .challenge}
<!-- 
> ## Locating the Right Module
>
> You want to select a random character from a string:
>
> ~~~
> bases = 'ACTTGCTTGAC'
> ~~~
> {: .language-python}
>
> 1. Which [standard library][stdlib] module could help you?
> 2. Which function would you select from that module? Are there alternatives?
> 3. Try to write a program that uses the function.
>
> > ## Solution
> >
> > The [random module][randommod] seems like it could help you.
> >
> > The string has 11 characters, each having a positional index from 0 to 10.
> > You could use either `random.randrange` or `random.randint` functions
> > to get a random integer between 0 and
> > 10, and then pick out the character at that position:
> >
> > ~~~
> > from random import randrange
> >
> > random_index = randrange(len(bases))
> > print(bases[random_index])
> > ~~~
> > {: .language-python}
> >
> > or more compactly:
> >
> > ~~~
> > from random import randrange
> >
> > print(bases[randrange(len(bases))])
> > ~~~
> > {: .language-python}
> >
> > Perhaps you found the `random.sample` function? It allows for slightly
> > less typing:
> >
> > ~~~
> > from random import sample
> >
> > print(sample(bases, 1)[0])
> > ~~~
> > {: .language-python}
> >
> > Note that this function returns a list of values. We will learn about
> > lists in [episode 11]({{ page.root }}/11-lists/).
> >
> > There's also other functions you could use, but with more convoluted
> > code as a result.
> {: .solution}
{: .challenge}
 -->

> ## Localizando o Módulo Correto
>
> Você quer selecionar um caracter aleatório dessa string:
>
> ~~~
> bases = 'ACTTGCTTGAC'
> ~~~
> {: .language-python}
>
> 1. Qual módulo da [biblioteca padrão][stdlib] poderia te ajudar?
> 2. Que função você poderia selecionar desse módulo? Existem alternativas?
> 3. Tente escrever um programa que use a função.
>
> > ## Solução
> >
> > O [módulo random][randommod] parece que pode nos ajudar.
> >
> > A string tem 11 caracteres, cada um tendo um índice posicional de 0 até 10.
> > Você pode usar as funções `random.randrange` ou `random.randint`
> > para pegar um integer aleatório entre 0 e
> > 10, e então selecionar um caracter naquela posição.
> >
> > ~~~
> > from random import randrange
> >
> > random_index = randrange(len(bases))
> > print(bases[random_index])
> > ~~~
> > {: .language-python}
> >
> > or more compactly:
> >
> > ~~~
> > from random import randrange
> >
> > print(bases[randrange(len(bases))])
> > ~~~
> > {: .language-python}
> >
> > Perhaps you found the `random.sample` function? It allows for slightly
> > less typing:
> >
> > ~~~
> > from random import sample
> >
> > print(sample(bases, 1)[0])
> > ~~~
> > {: .language-python}
> >
> > Note that this function returns a list of values. We will learn about
> > lists in [episode 11]({{ page.root }}/11-lists/).
> >
> > There's also other functions you could use, but with more convoluted
> > code as a result.
> {: .solution}
{: .challenge}

<!-- 
> ## Jigsaw Puzzle (Parson's Problem) Programming Example
>
> Rearrange the following statements so that a random
> DNA base is printed and its index in the string. 
> Not all statements may be needed.  Feel free to use/add
> intermediate variables.
>
> ~~~
> bases="ACTTGCTTGAC"
> import math
> import random
> ___ = random.randrange(n_bases)
> ___ = len(bases)
> print("random base ", bases[___], "base index", ___)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > import math 
> > import random
> > bases = "ACTTGCTTGAC" 
> > n_bases = len(bases)
> > idx = random.randrange(n_bases)
> > print("random base", bases[idx], "base index", idx)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Quebra Cabeça
>
> Rearranje e complete as seguintes linhas de código para que uma
> base de DNA seja impressa, junto de sua posição na string original.
> Nem todas as linhas precisam ser necessárias.  Fique a vontade para usar/adicionar
> variáveis intermediárias.
>
> ~~~
> bases="ACTTGCTTGAC"
> import math
> import random
> ___ = random.randrange(n_bases)
> ___ = len(bases)
> print("base aleatória", bases[___], "posição da base", ___)
> ~~~
> {: .language-python}
>
> > ## Solução
> >
> > ~~~
> > import math 
> > import random
> > bases = "ACTTGCTTGAC" 
> > n_bases = len(bases)
> > idx = random.randrange(n_bases)
> > print("base aleatória", bases[idx], "posição da base", idx)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

<!-- 
> ## When Is Help Available?
>
> When a colleague of yours types `help(math)`,
> Python reports an error:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> What has your colleague forgotten to do?
>
> > ## Solution
> >
> > Importing the math module (`import math`)
> {: .solution}
{: .challenge}
 -->

> ## Quando a Ajuda está Disponível?
>
> Se um colega seu executou `help(math)`,
> e o Python reportou um erro:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> O que o seu colega esqueceu de fazer?
>
> > ## Solução
> >
> > Importar o módulo `math` (`import math`)
> {: .solution}
{: .challenge}

<!-- 
> ## Importing With Aliases
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Rewrite the program so that it uses `import` *without* `as`.
> 3. Which form do you find easier to read?
>
> ~~~
> import math as m
> angulo = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > import math as m
> > angulo = m.degrees(m.pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > can be written as
> >
> > ~~~
> > import math
> > angulo = math.degrees(math.pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > Since you just wrote the code and are familiar with it, you might actually
> > find the first version easier to read. But when trying to read a huge piece
> > of code written by someone else, or when getting back to your own huge piece
> > of code after several months, non-abbreviated names are often easier, except
> > where there are clear abbreviation conventions.
> {: .solution}
{: .challenge}
 -->

> ## Importando com Atalhos
>
> 1. Preencha os brancos para que o programa abaixo imprima `90.0`.
> 2. Reescreva o programa para que use `import` *sem* `as`.
> 3. Que forma você acha mais fácil de ler?
>
> ~~~
> import math as m
> angulo = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .language-python}
>
> > ## Solução
> >
> > ~~~
> > import math as m
> > angulo = m.degrees(m.pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > pode ser escrito como
> >
> > ~~~
> > import math
> > angulo = math.degrees(math.pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > Já que você escreveu o código e está familiar com ele, talvez você
> > ache a primeira versão mais fácil de ler. Mas quando tentamos ler um pedaço enorme
> > de código escrito por outra pessoa, ou mesmo quando voltamos para o nosso próprio pedação
> > de código depois de vários meses, nomes não-abreviados costumam ser mais fáceis de ler, exceot
> > onde existem convenções de abreviação mais claras.
> {: .solution}
{: .challenge}

<!-- 
> ## There Are Many Ways To Import Libraries!
>
> Match the following print statements with the appropriate library calls.
>
> Print commands:
>
> 1. `print("sin(pi/2) =", sin(pi/2))`
> 2. `print("sin(pi/2) =", m.sin(m.pi/2))`
> 3. `print("sin(pi/2) =", math.sin(math.pi/2))`
>
> Library calls:
>
> 1. `from math import sin, pi`
> 2. `import math`
> 3. `import math as m`
> 4. `from math import *`
>
> > ## Solution
> >
> > 1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` without
> >    the library name as prefix, you need to use the `from ... import ...`
> >    statement. Whereas library call 1 specifically imports the two functions
> >    `sin` and `pi`, library call 4 imports all functions in the `math` module.
> > 2. Library call 3. Here `sin` and `pi` are referred to with a shortened library
> >    name `m` instead of `math`. Library call 3 does exactly that using the
> >    `import ... as ...` syntax - it creates an alias for `math` in the form of
> >    the shortened name `m`.
> > 3. Library call 2. Here `sin` and `pi` are referred to with the regular library
> >    name `math`, so the regular `import ...` call suffices.
> >
> > __Note:__ although library call 4 works, importing all names from a module using a wildcard 
> > import is [not recommended][pep8-imports] as it makes it unclear which names from the module
> > are used in the code. In general it is best to make your imports as specific as possible and to 
> > only import what your code uses. In library call 1, the `import` statement explicitly tells us
> > that the `sin` function is imported from the `math` module, but library call 4 does not
> > convey this information.
> {: .solution}
{: .challenge}
 -->

> ## Existem Muitas Formas de Importar Bibliotecas!
>
> Corresponda os seguintes *prints* com as chamadas de biblioteca corretas.
>
> Comandos printi:
>
> 1. `print("sin(pi/2) =", sin(pi/2))`
> 2. `print("sin(pi/2) =", m.sin(m.pi/2))`
> 3. `print("sin(pi/2) =", math.sin(math.pi/2))`
>
> Library calls:
>
> 1. `from math import sin, pi`
> 2. `import math`
> 3. `import math as m`
> 4. `from math import *`
>
> > ## Solução
> >
> > 1. Chamadas 1 e 4. Para nos referirmos diretamente a `sin` e `pi` sem
> >    o nome da biblioteca como prefixo, você precisa usar a declaração `from ... import ...`.
> >    Enquanto a Chamada 1 importa especificamente as funções
> >    `sin` e `pi`, a Chamada 4 importa todas as funções do módulo `math`.
> > 2. Chamada 3. Aqui `sin` e `pi` são referidas com um nome de atalho
> >    `m` invés de `math`. A chamada 3 faz exatamente isso usando a sintaxe
> >    `import ... as ...` ela cria um atalho para o módulo `math` na forma do
> >    atalho `m`.
> > 3. Chamada 2. Aqui `sin` e `pi` são referidas com o nome completo
> >    do módulo `math`, então basta a chamada `import ...`.
> >
> > __Nota:__ apesar da Chamada 4 funcionar, importar todos os nomes de um módulo usando um *wildcard* (o caracter `*`)
> > [não é recomendado][pep8-imports] por que isso não torna claro quais nomes de um módulo
> > são usados no código. Em geral é melhor fazer seus imports os mais específicos possíveis e 
> > importar somente o que o seu código usa. Na Chamada 1, a declaração de `import` explicitamente nos diz
> > que a função `sin` é importada do módulo `math`, mas a Chamada 4 não
> > traz essa informação.
> {: .solution}
{: .challenge}

<!-- 
> ## Importing Specific Items
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Do you find this version easier to read than preceding ones?
> 3. Why *wouldn't* programmers always use this form of `import`?
>
> ~~~
> ____ math import ____, ____
> angulo = degrees(pi / 2)
> print(angulo)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > from math import degrees, pi
> > angulo = degrees(pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > Most likely you find this version easier to read since it's less dense.
> > The main reason not to use this form of import is to avoid name clashes.
> > For instance, you wouldn't import `degrees` this way if you also wanted to
> > use the name `degrees` for a variable or function of your own. Or if you
> > were to also import a function named `degrees` from another library.
> {: .solution}
{: .challenge}
 -->

> ## Importando Itens Específicos
>
> 1. Preencha os espaços vazios para que o programa abaixo imprima `90.0`.
> 2. Você acha essa versão mais fácil de ler do que as anteriores?
> 3. Por que programadores *não* sempre usariam essa forma de import?
>
> ~~~
> ____ math import ____, ____
> angulo = degrees(pi / 2)
> print(angulo)
> ~~~
> {: .language-python}
>
> > ## Solução
> >
> > ~~~
> > from math import degrees, pi
> > angulo = degrees(pi / 2)
> > print(angulo)
> > ~~~
> > {: .language-python}
> >
> > É provável que você ache essa versão mais fácil de ler por ser menos densa.
> > A razão principal para não usar essa forma de import é para evitar conflitos de nome.
> > Por exemplo, você não importaria `degrees` se lá embaixo no seu código você quisesse
> > usar o nome `degrees` para uma variável ou função sua. Ou se você fosse
> > importar uma função chamada `degrees` de outra biblioteca.
> {: .solution}
{: .challenge}

<!-- 
> ## Reading Error Messages
>
> 1. Read the code below and try to identify what the errors are without running it.
> 2. Run the code, and read the error message. What type of error is it?
>
> ~~~
> from math import log
> log(0)
> ~~~
> {: .language-python}
>
> > ## Solution
> > ~~~
> > ---------------------------------------------------------------------------
> > ValueError                                Traceback (most recent call last)
> > <ipython-input-1-d72e1d780bab> in <module>
> >       1 from math import log
> > ---- 2 log(0)
> > 
> > ValueError: math domain error
> > ~~~
> > {: .output}
> >
> > 1. The logarithm of `x` is only defined for `x > 0`, so 0 is outside the
> >    domain of the function.
> > 2. You get an error of type `ValueError`, indicating that the function
> >    received an inappropriate argument value. The additional message
> >    "math domain error" makes it clearer what the problem is.
> {: .solution}
{: .challenge}
 -->

> ## Lendo Mensagens de Erro
>
> 1. Leia o código abaixo e tente identificar o que os erros vão ser sem rodá-lo.
> 2. Rode o código, e leia a mensagem de erro. Que tipo de erro que é?
>
> ~~~
> from math import log
> log(0)
> ~~~
> {: .language-python}
>
> > ## Solução
> > ~~~
> > ---------------------------------------------------------------------------
> > ValueError                                Traceback (most recent call last)
> > <ipython-input-1-d72e1d780bab> in <module>
> >       1 from math import log
> > ----> 2 log(0)
> > 
> > ValueError: math domain error
> > ~~~
> > {: .output}
> >
> > 1. O logaritmo de `x` só é definido para `x > 0`, então 0 está fora do
> >    domínio da função.
> > 2. Você recebe um erro do tipo `ValueError`, indicando que a função
> >    recebeu um argumento com um valor inapropriado. A mensagem adicional
> >    "math domain error" torna mais claro qual é o problema.
> {: .solution}
{: .challenge}

[pypi]: https://pypi.python.org/pypi/
[stdlib]: https://docs.python.org/pt-br/3/library/
[randommod]: https://docs.python.org/pt-br/3/library/random.html
[pep8-imports]: https://pep8.org/#imports