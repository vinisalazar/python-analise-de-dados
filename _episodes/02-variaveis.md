---
title: "Variáveis e Assinalação"
teaching: 10
exercises: 10
questions:
- "Como posso armazenar dados em programas?"
objectives:
- "Escrever programas que assinalam valores escalares a variáveis e realizar operações com esses valores."
- "Traçar corretamente mudanças de valores em programas que usam assinalamento de escalares."
keypoints:
- "Usar variáveis para armazenar valores."
- "Usar `print` para mostrar valores."
- "Variáveis persistem entre células."
- "Variáveis precisam ser criadas antes de serem usadas."
- "Variáveis podem ser usadas em operações."
- "Use um índice para pegar um único caracter de uma string."
- "Use uma fatia para pegar uma substring."
- "Use a função embutida `len` para encontrar o comprimento de uma string."
- "Python é *case-sensitive*."
- "Use nomes informativos para variáveis."
---
## Use variáveis para armazenar valores
<!-- 
*   **Variables** are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Here, Python assigns an age to a variable `age`
    and a name in quotes to a variable `first_name`.
 -->
*   **Variáveis** são nomes para valores.
*   No Python o símbolo `=` assinala o valor da direita ao nome na esquerda.
*   A variável é criada quando o valor é assinalado a ela.
*   Aqui, o Python assinala uma idade à variável `idade`
    e um nome em aspas à variável `primeiro_nome`.

    ~~~
    idade = 42
    primeiro_nome = 'Felipe'
    ~~~
    {: .language-python}

<!-- *   Variable names
    * can **only** contain letters, digits, and underscore `_` (typically used to separate words in long variable names)
    * cannot start with a digit
    * are **case sensitive** (age, Age and AGE are three different variables)
*   Variable names that start with underscores like `__alistairs_real_age` have a special meaning
    so we won't do that until we understand the convention.

## Use `print` to display values.

*   Python has a built-in function called `print` that prints things as text.
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (i.e., the things to print) in parentheses.
*   To add a string to the printout, wrap the string in single or double quotes.
*   The values passed to the function are called **arguments**
 -->
*   Nomes de variáveis
    * podem conter **somente** letras, números e underline `_` (geralmente usado para separar palavras em nomes compridos de variáveis)
    * não podem começar com um número
    * são **case sensitive** (idade, Idade e IDADE são três variáveis diferentes)
*   Nomes de variáveis que começam com underline como `__campeao_de_87` têm um significado especial,
    então vamos evitá-los até entendermos essa convenção.

## Use `print` para mostrar valores.

*   Python tem uma função embutida `print` que imprime as coisas como texto.
*   Chame a função (*i.e.*, diga para o Python executá-la) usando o nome da função.
*   Passe valores para uma função (*i.e.*, as coisas a serem imprimidas) entre parênteses.
*   Para adicionar uma string no que vai ser imprimido, coloque a string entre aspas simples ou duplas.
*   Valores passados para uma função são chamados de **argumentos**.

~~~
print(primeiro_nome, 'tem', idade, 'anos de idade.')
~~~
{: .language-python}
~~~
Felipe tem 42 anos de idade.
~~~
{: .output}

<!-- *   `print` automatically puts a single space between items to separate them.
*   And wraps around to a new line at the end.

Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error. (Unlike some languages, which "guess" a default value.) -->
    
*   `print` automaticamente coloca um espaço simples entre items para separá-los.
*   E coloca uma nova linha no final.

## Variáveis devem ser criadas antes de serem utilizadas.

*   Se uma variável não existe ainda, ou se o seu nome foi escrito errado,
    o Python reporta um erro (diferente de outras linguagens, que podem "adivinhar" um valor padrão).

~~~
print(sobrenome)
~~~
{: .language-python}
~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c1fbb4e96102> in <module>()
----> 1 print(sobrenome)

NameError: name 'sobrenome' is not defined
~~~
{: .error}
<!-- 
*   The last line of an error message is usually the most informative.
*   We will look at error messages in detail [later]({{ page.root }}/15-scope/#reading-error-messages).
 -->
*   A última linha de uma mensagem de erro costuma ser a mais informativa.
*   Vamos dar uma olhada em mensagens de erro [depois]({{ page.root }}/14-scope/#reading-error-messages).

<!--
>
> Be aware that it is the *order* of execution of cells that is important in a Jupyter notebook, not the order
> in which they appear. Python will remember *all* the code that was run previously, including any variables you have
> defined, irrespective of the order in the notebook. Therefore if you define variables lower down the notebook and then
> (re)run cells further up, those defined further down will still be present. As an example, create two cells with the
> following content, in this order:
>
> ~~~
> print(myval)
> ~~~
> {: .language-python}
>
> ~~~
> myval = 1
> ~~~
> {: .language-python}
>
> If you execute this in order, the first cell will give an error. However, if you run the first cell *after* the second
> cell it will print out `1`. To prevent confusion, it can be helpful to use the `Kernel` -> `Restart & Run All` option which
> clears the interpreter and runs everything from a clean slate going top to bottom.
{: .callout}
 -->
 
> ## Variáveis Persistem entre Células
>
> Fique atento que é a ordem de *execução* das células que importa num Jupyter Notebook, não a ordem
> que elas aparecem. O Python vai se lembrar de *todo* o código que foi executado anteriormente, incluindo quaisquer variáveis que você tenha
> definido, independente da ordem no notebook. Logo se você definir variáveis mais embaixo no notebook e aí 
> re-executar as células em cima, as variáveis definidas embaixo ainda estão presentes. Como um exemplo, crie duas células com o
> seguinte conteúdo, nessa ordem:
>
> ~~~
> print(minha_var)
> ~~~
> {: .language-python}
>
> ~~~
> minha_var = 1
> ~~~
> {: .language-python}
>
> Se você executar nessa orde, a primeira célula vai dar um erro. No entanto, se você executar a primeira célula *depois* da segunda
> célula, ela vai imprimir `1`. Para prevenir confusão, algo que pode ser útil é usar a opção `Kernel -> Restart & Run All` que
> limpa o interpretador e executa tudo de um novo estado, do início até o fim.
{: .callout}

<!-- 
*   We can use variables in calculations just as if they were values.
    *   Remember, we assigned the value `42` to `age` a few lines ago.

~~~
age = age + 3
print('Age in three years:', age)
~~~
{: .language-python}
~~~
Age in three years: 45
~~~
{: .output}
 -->
## Variáveis Podem ser Usadas em Operações

*   Podemos usar variáveis em operações como se fossem valores.
    *   Lembre-se, assinalamos o valor `42` para `idade` algumas linhas atrás.

~~~
idade = idade + 3
print('Idade em três anos:', idade)
~~~
{: .language-python}
~~~
Idade em três anos: 45
~~~
{: .output}


<!--
*   The characters (individual letters, numbers, and so on) in a string are
    ordered. For example, the string `'AB'` is not the same as `'BA'`. Because of
    this ordering, we can treat the string as a list of characters.
*   Each position in the string (first, second, etc.) is given a number. This
    number is called an **index** or sometimes a subscript.
*   Indices are numbered from 0.
*   Use the position's index in square brackets to get the character at that
    position.
     -->
     
## Use um **index** para selecionar um caracter de uma string

*   Os caracteres (letras, números, pontuações, etc) em uma string são
    ordenados. Por exemplo, a string `'AB'` não é o mesmo que `'BA'`.  Por causa
    dessa ordem, podemos tratar a string como uma lista de caracteres.
*   Cada posição na string (primeira, segunda, etc.) é dada um número. Esse
    número é chamado de **index** (ou índice), ou também de subscripto.
*   Índices são numerados do 0.
*   Use a posição do index em colchetes para selecionar o caracter naquela
    posição.
    
![Um exemplo de indexação](../fig/2_indexing.svg)

~~~
atomo = 'helio'
print(atomo[0])
~~~
{: .language-python}
~~~
h
~~~
{: .output}

<!-- 
*   A part of a string is called a **substring**. A substring can be as short as a
    single character.
*   An item in a list is called an element. Whenever we treat a string as if it
    were a list, the string's elements are its individual characters.
*   A slice is a part of a string (or, more generally, any list-like thing).
*   We take a slice by using `[start:stop]`, where `start` is replaced with the
    index of the first element we want and `stop` is replaced with the index of
    the element just after the last element we want.
*   Mathematically, you might say that a slice selects `[start:stop)`.
*   The difference between `stop` and `start` is the slice's length.
*   Taking a slice does not change the contents of the original string. Instead,
    the slice is a copy of part of the original string.
 -->

## Use uma fatia para pegar uma substring

*   Uma parte de uma string é chamada de **substring**. Uma substring pode ter somente
    um único caracter.
*   Um item em uma lista é chamado de um elemento. Sempre que tratamos uma string como se
    fosse uma lista, os elementos da string são seus caracteres individuais.
*   Uma fatia é uma parte de uma string (ou, de forma mais geral, qualquer coisa parecida com uma lista).
*   Pegamos uma fatia de uma string usando `[inicio:fim]`, onde `inicio` é substituido pelo
    index do primeiro elemento que queremos e `fim` é substituído pelo index
    do elemento logo após o último elemento que queremos.
*   Matematicamente, pode-se dizer que uma fatia seleciona `[inicio:fim]`.
*   A diferença entre `fim` e `inicio` é o comprimento (*length*) da fatia.
*   Selecionar uma fatia não altera o conteúdo da string original. Invés disso,
    a fatia é uma cópia de parte da string original.

~~~
nome_atomo = 'sodio'
print(nome_atomo[0:3])
~~~
{: .language-python}
~~~
sod
~~~
{: .output}

## Use a função embutida `len` para descobrir o tamanho de uma string.

~~~
print(len('helio'))
~~~
{: .language-python}
~~~
5
~~~
{: .output}
<!-- 
*   Nested functions are evaluated from the inside out,
     like in mathematics.

Python is case-sensitive.

*   Python thinks that upper- and lower-case letters are different,
    so `Name` and `name` are different variables.
*   There are conventions for using upper-case letters at the start of variable names so we will use lower-case letters for now.

Use meaningful variable names.

*   Python doesn't care what you call variables as long as they obey the rules
    (alphanumeric characters and the underscore).
 -->

*   Funções aninhadas são avaliadas de dentro para fora,
    assim como na matemática

## Python é *case-sensitive*.

*   O Python entende letras maiúsculas e minúsculas são diferentes,
    então `Nome` e `nome` são variáveis diferentes.
*   Existem convenções para usar letras maiúsculas como a primeira letra de uma variável então vamos usar letras minúsculas por enquanto.

## Use nomes informativos para variáveis.

*   Python não liga para o que você chama uma variável, desde que obedeça as regras
    (caracteres alfanuméricos e o underline).

~~~
flabadab = 42
ewr_422_yY = 'Felipe'
print(ewr_422_yY, 'tem', flabadab, 'anos de idade.')
~~~
{: .language-python}
<!-- 
*   Use meaningful variable names to help other people understand what the program does.
*   The most important "other person" is your future self.
 -->

*   Use nomes informativos para variáveis para ajudar outras pessoas a entenderem o que programa faz.
*   A "outra pessoa" mais importante é você no futuro.

<!--
> Fill the table showing the values of the variables in this program
> *after* each statement is executed.
>
> ~~~
> # Command  # Value of x   # Value of y   # Value of swap #
> x = 1.0    #              #              #               #
> y = 3.0    #              #              #               #
> swap = x   #              #              #               #
> x = y      #              #              #               #
> y = swap   #              #              #               #
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > # Command  # Value of x   # Value of y   # Value of swap #
> > x = 1.0    # 1.0          # not defined  # not defined   #
> > y = 3.0    # 1.0          # 3.0          # not defined   #
> > swap = x   # 1.0          # 3.0          # 1.0           #
> > x = y      # 3.0          # 3.0          # 1.0           #
> > y = swap   # 3.0          # 1.0          # 1.0           #
> > ~~~
> > {: .output}
> > 
> > These three lines exchange the values in `x` and `y` using the `swap`
> > variable for temporary storage. This is a fairly common programming idiom.
>{: .solution}
{: .challenge}
 -->

> ## Trocando valores
>
> Preencha a tabela mostrando os valores das variáveis nesse programa
> *depois* que cada linha é executada.
>
> ~~~
> # Comando  # Valor de x   # Valor de y   # Value de swap #
> x = 1.0    #              #              #               #
> y = 3.0    #              #              #               #
> swap = x   #              #              #               #
> x = y      #              #              #               #
> y = swap   #              #              #               #
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > # Comando  # Valor de x   # Valor de y   # Value de swap #
> > x = 1.0    # 1.0          # not defined  # not defined   #
> > y = 3.0    # 1.0          # 3.0          # not defined   #
> > swap = x   # 1.0          # 3.0          # 1.0           #
> > x = y      # 3.0          # 3.0          # 1.0           #
> > y = swap   # 3.0          # 1.0          # 1.0           #
> > ~~~
> > {: .output}
> > 
> > Essas três linhas trocam os valores de `x` e `y` usando a variável `swap`
> > para armazenamento temporário. Isso é uma prática comum de programação.
>{: .solution}
{: .challenge}

<!-- 
> ## Predicting Values
>
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> initial = 'left'
> position = initial
> initial = 'right'
> ~~~
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > 'left'
> > ~~~
> > {: .output}
> >
>> The `initial` variable is assigned the value `'left'`.
> > In the second line, the `position` variable also receives
>> the string value `'left'`. In third line, the `initial` variable is given the
>> value `'right'`, but the `position` variable retains its string value
>> of `'left'`.
>{: .solution}
{: .challenge}
 -->

> ## Predizendo valores
>
> Qual é o valor final de `posicao` no programa abaixo?
> (Tente predizer o valor sem rodar o programa,
> aí cheque se sua predição estava certa.)
>
> ~~~
> inicial = 'acima'
> posicao = inicial
> inicial = 'abaixo'
> ~~~
> {: .language-python}
> > ## Solução
> >
> > ~~~
> > print(posicao)
> > ~~~
> > {: .language-python}
> > ~~~
> > acima
> > ~~~
> > {: .output}
> >
> > A variável `inicial` é assinalada ao valor `'acima'`.
> > Na segunda linha, a variável `posicao` também recebe a
> > a string de valor `'acima'`. Na terceira linha, a variável `inicial` é dada o
> > valor `'abaixo'`, mas a variável `posicao` permanece como seu valor de string
> > `'acima'`.
>{: .solution}
{: .challenge}

<!-- 
> ## Challenge
>
> If you assign `a = 123`,
> what happens if you try to get the second digit of `a` via `a[1]`?
>
> > ## Solution
> > Numbers are not strings or sequences and Python will raise an error if you try to perform an index operation on a
> > number. In the [next lesson on types and type conversion]({{ page.root }}/03-tipos/#convert-numbers-and-strings)
> > we will learn more about types and how to convert between different types. If you want the Nth digit of a number you
> > can convert it into a string using the `str` built-in function and then perform an index operation on that string.
> >
> > ~~~
> > a = 123
> > print(a[1])
> > ~~~
> > {: .language-python}
> > ~~~
> > TypeError: 'int' object is not subscriptable
> > ~~~
> > {: .error}
> > 
> > 
> > ~~~
> > a = str(123)
> > print(a[1])
> > ~~~
> > {: .language-python}
> > ~~~
> > 2
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Desafio
>
> Se você assinalar `a = 123`,
> o que acontece se você tentar pegar o segundo dígito de `a` com `a[1]`?
>
> > ## Solução
> > Números não são strings ou sequências e o Python vai dar um erro quando você tentar fazer uma operação de index em um
> > número. No [próximo episódio sobre tipos e conversão de dados]({{ page.root }}/03-tipos/#convert-numbers-and-strings)
> > vamos aprender mais sobre tipos e como converter entre diferentes tipos. Se você quer o N-ésimo dígito de um número você
> > pode convertê-lo para uma string usando a função embutida `str` e então executar uma operação de index nessa string.
> >
> > ~~~
> > a = 123
> > print(a[1])
> > ~~~
> > {: .language-python}
> > ~~~
> > TypeError: 'int' object is not subscriptable
> > ~~~
> > {: .error}
> > 
> > 
> > ~~~
> > a = str(123)
> > print(a[1])
> > ~~~
> > {: .language-python}
> > ~~~
> > 2
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Choosing a Name
>
> Which is a better variable name, `m`, `min`, or `minutes`?
> Why?
> Hint: think about which code you would rather inherit
> from someone who is leaving the lab:
>
> 1. `ts = m * 60 + s`
> 2. `tot_sec = min * 60 + sec`
> 3. `total_seconds = minutes * 60 + seconds`
>
> > ## Solution
> >
> > `minutes` is better because `min` might mean something like "minimum"
> > (and actually is an existing built-in function in Python that we will cover later).
> {: .solution}
{: .challenge}
 -->

> ## Escolhendo um nome
>
> Qual é o um nome de variável melhor, `m`, `min`, ou `minutos`?
> Por quê?
> Dica: pense sobre qual código você gostaria de herdar
> de alguém que está saindo da empresa:
>
> 1. `ts = m * 60 + s`
> 2. `tot_seg = min * 60 + seg`
> 3. `total_segundos = minutos * 60 + segundos`
>
> > ## Solução
> >
> > `minutos` é melhor, porque `min` pode significar algo como "mínimo"
> > (e também é uma função embutida do Python que vamos ver mais para a frente).
> {: .solution}
{: .challenge}

<!-- 
> ## Slicing practice
>
> What does the following program print?
>
> ~~~
> atom_name = 'carbon'
> print('atom_name[1:3] is:', atom_name[1:3])
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > atom_name[1:3] is: ar
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Praticando fatias
>
> O que o programa a seguir imprime?
>
> ~~~
> nome_atomo = 'carbono'
> print('nome_atomo[1:3] é:', nome_atomo[1:3])
> ~~~
> {: .language-python}
>
> > ## Solução
> >
> > ~~~
> > nome_atomo[1:3] é: ar
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Slicing concepts
>
> 1.  What does `thing[low:high]` do?
> 2.  What does `thing[low:]` (without a value after the colon) do?
> 3.  What does `thing[:high]` (without a value before the colon) do?
> 4.  What does `thing[:]` (just a colon) do?
> 5.  What does `thing[number:some-negative-number]` do?
> 6.  What happens when you choose a `high` value which is out of range? (i.e., try `atom_name[0:15]`) 
>
> > ## Solutions
> >
> > 1. `thing[low:high]` returns a slice from `low` to the value before `high`
> > 2. `thing[low:]` returns a slice from `low` all the way to the end of `thing`
> > 3. `thing[:high]` returns a slice from the beginning of `thing` to the value before `high`
> > 4. `thing[:]` returns all of `thing`
> > 5. `thing[number:some-negative-number]` returns a slice from `number` to `some-negative-number` values from the end of `thing`
> > 6. If a part of the slice is out of range, the operation does not fail. `atom_name[0:15]` gives the same result as `atom_name[0:]`.
> {: .solution}
{: .challenge}
 -->

> ## Conceitos de fatias
>
> 1.  O que `coisa[baixo:cima]` do?
> 2.  O que `coisa[baixo:]` (com um valor antes dos dois pontos) faz?
> 3.  O que `coisa[:cima]` (com um valor depois dos dois pontos) faz?
> 4.  O que `coisa[:]` (somente dois pontos) faz?
> 5.  O que `coisa[numero:algum-numero-negativo]` faz?
> 6.  O que acontece se você escolhar um valor `cima` que está fora de alcance (*i.e.*, tente `nome_atomo[0:15]`)?
>
> > ## Soluções
> >
> > 1. `coisa[baixo:cima]` retorna uma fatia de `baixo` até o valor antes de `cima`.
> > 2. `coisa[baixo:]` retorna uma fatia de `baixo` até o final de coisa `coisa`.
> > 3. `coisa[:cima]` retorna uma fatia do início de `coisa` até o valor antes de `cima`.
> > 4. `coisa[:]` retorna toda a `coisa`.
> > 5. `coisa[numero:algum-numero-negativo]` retorna uma fatia de `numero` até `algum-numero-negativo` valores do fim de `coisa`.
> > 6. Se uma parte de uma fatia está fora de alcance, a operação não falha. `nome_atomo[0:15]` dá o mesmo resultado que `nome_atomo[0:]`.
> {: .solution}
{: .challenge}
