---
title: "For Loops"
teaching: 10
exercises: 15
questions:
- "Como eu posso fazer um programa fazer muitas coisas?"
objectives:
- "Explicar para que *for loops* normalmente são usados."
- "Traçar a execução de um loop simples (não aninhado) e apontar corretamente os valores das variáveis em cada iteração."
- "Escrever for loops que usem o padrão Acumulador para agregar valores."
keypoints:
- "Um *for loop* executa comandos uma vez para cada valor em uma coleção."
- "Um *for loop* consiste de uma coleção, uma variável do loop, e um corpo."
- "A primeira linha de um for loop deve acabar com dois pontos, e o corpo deve ser indentado."
- "Indentação é sempre importante no Python."
- "Variáveis de loop podem ser chamadas de qualquer coisa (mas é fortemente recomendado de que seja usado um nome informativo)."
- "O corpo de um loop pode conter muitos comandos."
- "Use `range` para iterar sobre uma sequência de números."
- "O padrão Acumulador transforma muitos valores em um."
---

<!-- 
## A *for loop* executes commands once for each value in a collection.

*   Doing calculations on the values in a list one by one
    is as painful as working with `pressure_001`, `pressure_002`, etc.
*   A *for loop* tells Python to execute some statements once for each value in a list,
    a character string,
    or some other collection.
*   "for each thing in this group, do these operations"

~~~
for number in [2, 3, 5]:
    print(number)
~~~
{: .language-python}

*   This `for` loop is equivalent to:

~~~
print(2)
print(3)
print(5)
~~~
{: .language-python}

*   And the `for` loop's output is:

~~~
2
3
5
~~~
{: .output}
 -->

## Um *for loop* executa comandos uma vez para cada valor em uma coleção.

*   Fazer operações nos valores de uma lista um por um
    é tão doloroso quanto trabalhar com `consumo_001`, `consumo_002`, etc.
*   Um *for loop* diz ao Python para executar alguns comandos uma vez para cada valor em uma lista,
    string de caracteres,
    ou alguma outra coleção.
*   "para cada coisa nesse grupo, faça essas operações"

~~~
for numero in [2, 3, 5]:
    print(numero)
~~~
{: .language-python}

*   Esse `for loop` é equivalente a:

~~~
print(2)
print(3)
print(5)
~~~
{: .language-python}

*   E a saída do `for loop` é:

~~~
2
3
5
~~~
{: .output}
<!-- 
## A `for` loop is made up of a collection, a loop variable, and a body.

~~~
for number in [2, 3, 5]:
    print(number)
~~~
{: .language-python}

*   The collection, `[2, 3, 5]`, is what the loop is being run on.
*   The body, `print(number)`, specifies what to do for each value in the collection.
*   The loop variable, `number`, is what changes for each *iteration* of the loop.
    *   The "current thing".
 -->

## Um *for loop* consiste de uma coleção, uma variável do loop, e um corpo.

~~~
for numero in [2, 3, 5]:
    print(numero)
~~~
{: .language-python}

*   A coleção, `[2, 3, 5]`, é a coisa sobre a qual o loop está sendo rodado.
*   O corpo, `print(numero)`, especifica o que fazer para cada valor na coleção.
*   O variável do loop, `numero`, é o que muda em cada *iteração* do loop.
    *   A "coisa atual".

<!-- 
## The first line of the `for` loop must end with a colon, and the body must be indented.

*   The colon at the end of the first line signals the start of a *block* of statements.
*   Python uses indentation rather than `{}` or `begin`/`end` to show *nesting*.
    *   Any consistent indentation is legal, but almost everyone uses four spaces.

~~~
for number in [2, 3, 5]:
print(number)
~~~
{: .language-python}
~~~
IndentationError: expected an indented block
~~~
{: .error}

*   Indentation is always meaningful in Python.

~~~
firstName = "Jon"
  lastName = "Smith"
~~~
{: .language-python}
~~~
  File "ipython-input-7-f65f2962bf9c", line 2
    lastName = "Smith"
    ^
IndentationError: unexpected indent
~~~
{: .error}

*   This error can be fixed by removing the extra spaces
    at the beginning of the second line.
-->

## A primeira linha de um for loop deve acabar com dois pontos, e o corpo deve ser indentado.

*   Os dois pontos no final da primeira linha indica o início de um *bloco* de comandos (*statements*).
*   Python usa indentação invés de `{}` ou `begin`/`end` para mostrar *aninhamento* (*nesting*).
    *   Qualquer indentação constante pode ser usada, mas normalmente utilizamos quatro espaços.

~~~
for numero in [2, 3, 5]:
print(numero)
~~~
{: .language-python}
~~~
IndentationError: expected an indented block
~~~
{: .error}

*   Indentação é sempre importante no Python.

~~~
primeiro_nome = "Felipe"
  sobrenome = "da Silva"
~~~
{: .language-python}
~~~
  File "<ipython-input-7-f65f2962bf9c>", line 2
    sobrenome = "da Silva"
    ^
IndentationError: unexpected indent
~~~
{: .error}

*   Esse erro pode ser consertado ao remover o espaço extra
    no começo da segunda linha.
<!-- 
## Loop variables can be called anything.

*   As with all variables, loop variables are:
    *   Created on demand.
    *   Meaningless: their names can be anything at all.

~~~
for kitten in [2, 3, 5]:
    print(kitten)
~~~
{: .language-python}
 -->

## Variáveis de loop podem ser chamadas de qualquer coisa.

*   Assim como todas as variáveis, variáveis de loop são:
    *   Criadas por demanda.
    *   Sem significado: os seus nomes podem ser qualquer coisa

~~~
for pessoa in [2, 3, 5]:
    print(pessoa)
~~~
{: .language-python}
<!-- 
## The body of a loop can contain many statements.

*   But no loop should be more than a few lines long.
*   Hard for human beings to keep larger chunks of code in mind.

~~~
primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)
~~~
{: .language-python}
~~~
2 4 8
3 9 27
5 25 125
~~~
{: .output}
 -->

## O corpo de um loop pode conter muitos comandos.

*   Mas nenhum loop deve ter muito mais do que algumas linhas.
*   É difícil para seres humanos manterem grandes pedaços de código em mente.

~~~
primos = [2, 3, 5]
for p in primos:
    quadrado = p ** 2
    cubo = p ** 3
    print(p, quadrado, cubo)
~~~
{: .language-python}
~~~
2 4 8
3 9 27
5 25 125
~~~
{: .output}
<!-- 
## Use `range` to iterate over a sequence of numbers.

*   The built-in function [`range`](https://docs.python.org/3/library/stdtypes.html#range) produces a sequence of numbers.
    *   *Not* a list: the numbers are produced on demand
        to make looping over large ranges more efficient.
*   `range(N)` is the numbers 0..N-1
    *   Exactly the legal indices of a list or character string of length N

~~~
print('a range is not a list: range(0, 3)')
for number in range(0, 3):
    print(number)
~~~
{: .language-python}
~~~
a range is not a list: range(0, 3)
0
1
2
~~~
{: .output}
 -->

## Use `range` para iterar sobre uma sequência de números.

*   A função embutida [`range`](https://docs.python.org/pt-br/3/library/stdtypes.html#range) produz uma sequência de números.
    *   *Não* é uma lista: os números são produzidos sob demanda
        para tornar o loop de grandes ranges mais eficiente.
*   `range(N)` são os números `0 ... N-1`.
    *   Exatamente os mesmos índices de uma lista ou string de tamanho `N`.

~~~
print('Uma range não é uma lista: range(0, 3)')
for numero in range(0, 3):
    print(numero)
~~~
{: .language-python}
~~~
Uma range não é uma lista: range(0, 3)
0
1
2
~~~
{: .output}
<!-- 
## The Accumulator pattern turns many values into one.

*   A common pattern in programs is to:
    1.  Initialize an *accumulator* variable to zero, the empty string, or the empty list.
    2.  Update the variable with values from a collection.

~~~
# Sum the first 10 integers.
total = 0
for number in range(10):
   total = total + (number + 1)
print(total)
~~~
{: .language-python}
~~~
55
~~~
{: .output}

*   Read `total = total + (number + 1)` as:
    *   Add 1 to the current value of the loop variable `number`.
    *   Add that to the current value of the accumulator variable `total`.
    *   Assign that to `total`, replacing the current value.
*   We have to add `number + 1` because `range` produces 0..9, not 1..10.
 -->

## O padrão Acumulador transforma muitos valores em um.

*   Uma padrão comum em programas é:
    1.  Inicializar uma variável *acumuladora* como zero, uma string vazia, uma lista vazia.
    2.  Fazer update da variável com valores de uma coleção.

~~~
# Some os 10 primeiros inteiros.
total = 0
for numero in range(10):
   total = total + (numero+ 1)
print(total)
~~~
{: .language-python}
~~~
55
~~~
{: .output}

*   Leia `total = total + (numero + 1)` como:
    *   Some 1 ao valor atual da variável `numero`.
    *   Some isso ao valor atual da variável acumuladora `total`.
    *   Assinalar isso à `total`, substituindo o valor atual.
*   Temos que botar `numero + 1` porque `range` produz `0..9`, e não `1..10`.
<!-- 
> ## Classifying Errors
>
> Is an indentation error a syntax error or a runtime error?
> > ## Solution
> > An IndentationError is a syntax error. Programs with syntax errors cannot be started.
> > A program with a runtime error will start but an error will be thrown under certain conditions.
> {: .solution}
{: .challenge}
 -->

> ## Classificando Erros
>
> Indentação é um erro de sintaxe ou um erro de *runtime*?
> > ## Solução
> > Um IndentationError é um erro de sintaxe. Programas que têm erros de sintaxe não podem ser iniciados.
> > Um programa com um erro de *runtime* vai iniciar mas o erro vai ocorrer em certas condições.
> {: .solution}
{: .challenge}
<!-- 
> ## Tracing Execution
>
> Create a table showing the numbers of the lines that are executed when this program runs,
> and the values of the variables after each line is executed.
>
> ~~~
> total = 0
> for char in "tin":
>     total = total + 1
> ~~~
> {: .language-python}
> > ## Solution
> >
> > | Line no | Variables            |
> > |---------|----------------------|
> > | 1       | total = 0            |
> > | 2       | total = 0 char = 't' |
> > | 3       | total = 1 char = 't' |
> > | 2       | total = 1 char = 'i' |
> > | 3       | total = 2 char = 'i' |
> > | 2       | total = 2 char = 'n' |
> > | 3       | total = 3 char = 'n' |
> {: .solution}
{: .challenge}
 -->

> ## Traçando Execução
>
> Crie uma tabela mostra os números de cada linha quando esse programa é executado,
> e os valores das variáveis depois de que cada linha é executada.
>
> ~~~
> total = 0
> for char in "rio":
>     total = total + 1
> ~~~
> {: .language-python}
> > ## Solução
> >
> > | Line no | Variables            |
> > |---------|----------------------|
> > | 1       | total = 0            |
> > | 2       | total = 0 char = 'r' |
> > | 3       | total = 1 char = 'r' |
> > | 2       | total = 1 char = 'i' |
> > | 3       | total = 2 char = 'i' |
> > | 2       | total = 2 char = 'o' |
> > | 3       | total = 3 char = 'o' |
> {: .solution}
{: .challenge}
<!-- 
> ## Reversing a String
>
> Fill in the blanks in the program below so that it prints "nit"
> (the reverse of the original character string "tin").
>
> ~~~
> original = "tin"
> result = ____
> for char in original:
>     result = ____
> print(result)
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > original = "tin"
> > result = ""
> > for char in original:
> >     result = char + result
> > print(result)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Invertendo uma String
>
> Preencha os brancos no programa abaixo para que ele imprima "oir"
> o inverso da string original "rio".
>
> ~~~
> original = "rio"
> resultado = ____
> for letra in original:
>     result = ____
> print(result)
> ~~~
> {: .language-python}
> > ## Solução
> > ~~~
> > original = "rio"
> > resultado = ""
> > for letra in original:
> >     resultado = letra + resultado
> > print(resultado)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## Practice Accumulating
>
> Fill in the blanks in each of the programs below
> to produce the indicated result.
>
> ~~~
> # Total length of the strings in the list: ["red", "green", "blue"] => 12
> total = 0
> for word in ["red", "green", "blue"]:
>     ____ = ____ + len(word)
> print(total)
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > total = 0
> > for word in ["red", "green", "blue"]:
> >     total = total + len(word)
> > print(total)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> ~~~
> # List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
> lengths = ____
> for word in ["red", "green", "blue"]:
>     lengths.____(____)
> print(lengths)
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > lengths = []
> > for word in ["red", "green", "blue"]:
> >     lengths.append(len(word))
> > print(lengths)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> ~~~
> # Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
> words = ["red", "green", "blue"]
> result = ____
> for ____ in ____:
>     ____
> print(result)
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > words = ["red", "green", "blue"]
> > result = ""
> > for word in words:
> >     result = result + word
> > print(result)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> __Create an acronym:__ Starting from the list `["red", "green", "blue"]`, create the acronym `"RGB"` using
> a for loop.
> 
> __Hint:__ You may need to use a string method to properly format the acronym.
> > ## Solution
> > ~~~
> > acronym = ""
> > for word in ["red", "green", "blue"]:
> >     acronym = acronym + word[0].upper()
> > print(acronym)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Pratique Acumulação
>
> Preencha os brancos do programas abaixo
> para produzir o resultado indicado.
>
> ~~~
> # Comprimento total das strings na lista: ["vermelho", "verde", "azul"] => 17
> total = 0
> for palavra in ["vermelho", "verde", "azul"]:
>     ____ = ____ + len(palavra)
> print(total)
> ~~~
> {: .language-python}
> > ## Solução
> > ~~~
> > total = 0
> > for palavra in ["vermelho", "verde", "azul"]:
> >     total = total + len(palavra)
> > print(total)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> ~~~
> # Lista com os comprimentos (lengths) de cada palavra: ["vermelho", "verde", "azul"] => [8, 5, 4]
> comprimentos = ____
> for palavra in ["vermelho", "verde", "azul"]:
>     comprimentos.____(____)
> print(comprimentos)
> ~~~
> {: .language-python}
> > ## Solução
> > ~~~
> > comprimentos = []
> > for palavra in ["vermelho", "verde", "azul"]:
> >     comprimentos.append(len(palavra))
> > print(comprimentos)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> ~~~
> # Concatene (junte) todas as palavras: ["vermelho", "verde", "azul"] => "redgreenblue"
> palavras = ["vermelho", "verde", "azul"]
> resultado = ____
> for ____ in ____:
>     ____
> print(resultado)
> ~~~
> {: .language-python}
> > ## Solução
> > ~~~
> > palavras = ["vermelho", "verde", "azul"]
> > resultado = ""
> > for palavra in palavras:
> >     resultado = resultado + palavra
> > print(resultado)
> > ~~~
> > {: .language-python}
> {: .solution}
>
> __Create an acronym:__ Starting from the list `["vermelho", "verde", "azul"]`, create the acronym `"RGB"` using
> a for loop.
> 
> __Hint:__ You may need to use a string method to properly format the acronym.
> > ## Solução
> > ~~~
> > acronym = ""
> > for palavra in ["vermelho", "verde", "azul"]:
> >     acronym = acronym + palavra[0].upper()
> > print(acronym)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## Cumulative Sum
>
> Reorder and properly indent the lines of code below
> so that they print a list with the cumulative sum of data.
> The result should be `[1, 3, 5, 10]`.
>
> ~~~
> cumulative.append(total)
> for number in data:
> cumulative = []
> total += number
> total = 0
> print(cumulative)
> data = [1,2,2,5]
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > total = 0
> > data = [1,2,2,5]
> > cumulative = []
> > for number in data:
> >     total += number
> >     cumulative.append(total)
> > print(cumulative)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Soma Acumulativa
>
> Reordene e indente corretamente as linhas de código abaixo
> para que imprimam a lista com a soma acumulativa dos dados.
> O resultado deve ser `[1, 3, 5, 10]`.
>
> ~~~
> acumulativa.append(total)
> for numero in dados:
> acumulativa = []
> total += numero
> total = 0
> print(acumulativa)
> dados = [1,2,2,5]
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > total = 0
> > dados = [1,2,2,5]
> > acumulativa = []
> > for numero in dados:
> >     total += numero
> >     acumulativa.append(total)
> > print(acumulativa)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## Identifying Variable Name Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    What type of `NameError` do you think this is?
>    Is it a string with no quotes, a misspelled variable, or a
>    variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
>
> ~~~
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + a
>     else:
>         message = message + "b"
> print(message)
> ~~~
> {: .language-python}
> > ## Solution
> > - Python variable names are case sensitive: `number` and `Number` refer to different variables.
> > - The variable `message` needs to be initialized as an empty string.
> > - We want to add the string `"a"` to `message`, not the undefined variable `a`.
> >
> > ~~~
> > message = ""
> > for number in range(10):
> >     # use a if the number is a multiple of 3, otherwise use b
> >     if (number % 3) == 0:
> >         message = message + "a"
> >     else:
> >         message = message + "b"
> > print(message)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Identificando Nomes em Erros de Variáveis
>
> 1. Leia o código abaixo e tente identificar quais são os erros
>    *sem* rodá-lo.
> 2. Rode o código e leia a mensagem de erro.
>    Que tipo de `NameError` você acha que é esse?
>    É uma string sem aspas, uma variável escrita errada, ou
>    uma variável que deria ser definida mas não foi?
> 3. Conserte o erro.
> 4. Repita os passos 2 e 3, até consertar todos os erros.
>
> ~~~
> for numero in range(10):
>     # use a if the numero is a multiple of 3, otherwise use b
>     if (Numero % 3) == 0:
>         mensagem = mensagem + a
>     else:
>         mensagem = mensagem + "b"
> print(mensagem)
> ~~~
> {: .language-python}
> > ## Solução
> > - Nomes de variável do Python são *case-sensitive*: `numero` e `Numero` se referem a variáveis distintas.
> > - A variável mensagem `mensagem` precisa ser inicializada com uma string vazia.
> > - Queremos adicionar uma string `"a"` para `mensagem`, não uma variável indefinida `a`.
> >
> > ~~~
> > mensagem = ""
> > for numero in range(10):
> >     # use a if the numero is a multiple of 3, otherwise use b
> >     if (numero % 3) == 0:
> >         mensagem = mensagem + "a"
> >     else:
> >         mensagem = mensagem + "b"
> > print(mensagem)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## Identifying Item Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code, and read the error message. What type of error is it?
> 3. Fix the error.
>
> ~~~
> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> print('My favorite season is ', seasons[4])
> ~~~
> {: .language-python}
> > ## Solution
> > This list has 4 elements and the index to access the last element in the list is `3`.
> > ~~~
> > seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> > print('My favorite season is ', seasons[3])
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Identificando Erros de Itens
>
> 1. Leia o código abaixo e tente identificar o que são os erros
>    *sem* rodá-lo.
> 2. Rode o código, e leia a mensagem de erro. Que tipo de erro é esse?
> 3. Conserte o erro.
>
> ~~~
> estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']
> print('Minha estação favorita é', estacoes[4])
> ~~~
> {: .language-python}
> > ## Solução
> > Essa lista tem 4 elementos e o index para acessar o último elemento da lista é `3`.
> > ~~~
> > estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']
> > print('Minha estação favorita é', estacoes[3])
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
