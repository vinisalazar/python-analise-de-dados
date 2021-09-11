---
title: "Tipos de Dados e Conversão de Tipos"
teaching: 10
exercises: 10
questions:
- "Que tipos de dados um programa armazena?"
- "Como posso converter de um tipo para outro?"
objectives:
- "Explicar as principais diferenças entre inteiros e números de ponto flutuante."
- "Explicar as principais diferenças entre strings e números."
- "Usar funções embutidas para converter entre inteiros, números de ponto flutuante e strings."
keypoints:
- "Todo valor tem um tipo."
- "Use a função embutida `type` para encontrar o tipo de um valor."
- "Tipos determinam que operações podem ser feitas em um valor."
- "Strings podem ser somadas e multiplicadas."
- "Strings têm um comprimento (mas números não)."
- "Preciso converter números para strings ou vice-versa quando fazendo operações entre eles."
- "Posso misturar inteiros e *floats* livremente entre operações."
- "Variáveis só mudam de valor quando algo é assinalado a elas."
---
<!-- 
*   Every value in a program has a specific type.
*   Integer (`int`): represents positive or negative whole numbers like 3 or -512.
*   Floating point number (`float`): represents real numbers like 3.14159 or -2.5.
*   Character string (usually called "string", `str`): text.
    *   Written in either single quotes or double quotes (as long as they match).
    *   The quote marks aren't printed when the string is displayed.
 -->

## Todo valor tem um tipo.

*  Todo valor de um programa tem um tipo específico.
*  Integer (`int`): representa um número inteiro positivo ou negativo como 3 ou -512.
*  Número de ponto flutuante (`float`): representa números reais como 3.14159 ou -2.5.
*  String de caracteres (geralmente chamado de "string", `str`): texto.
    *   Escritas entre aspas simples ou duplas (desde que sejam do mesmo tipo).
    *   As aspas não são impressas quando usamos `print()`.

<!-- 
*   Use the built-in function `type` to find out what type a value has.
*   Works on variables as well.
    *   But remember: the *value* has the type --- the *variable* is just a label.
 -->

## Use a função embutida `type` para descobrir o tipo de um valor.

*   Use a função embutida `type` para descobrir qual é o tipo de um determinado valor.
*   Também funciona como variáveis.
    *   Mas lembre-se: o *valor* tem o tipo --- a *variável* é só uma etiqueta.

~~~
print(type(52))
~~~
{: .language-python}
~~~
<class 'int'>
~~~
{: .output}

~~~
forma = 'redonda'
print(type(forma))
~~~
{: .language-python}
~~~
<class 'str'>
~~~
{: .output}

<!-- 
*   A value's type determines what the program can do to it.
 -->

## Tipos controlam que operações (ou métodos) podem ser executados em um dado valor.

*   O tipo de um valor determina o que o programa pode fazer com ele.

~~~
print(5 - 3)
~~~
{: .language-python}
~~~
2
~~~
{: .output}

~~~
print('ola' - 'o')
~~~
{: .language-python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-67f5626a1e07> in <module>()
----> 1 print('ola' - 'o')

TypeError: unsupported operand type(s) for -: 'str' and 'str'
~~~
{: .error}

<!-- 
*   "Adding" character strings concatenates them.
 -->

## Você pode usar os operadores `+` e `*` em strings.

*   "Adding" character strings concatenates them.

~~~
nome_completo = 'Felipe' + ' ' + 'da Silva'
print(nome_completo)
~~~
{: .language-python}
~~~
Felipe da Silva
~~~
{: .output}

<!-- 
*   Multiplying a character string by an integer _N_ creates a new string that consists of that character string repeated  _N_ times.
    *   Since multiplication is repeated addition.
 -->

*   Multiplicar uma string por um inteiro `N` cria uma nova string que consiste da string original repetida `N` vezes.
    *   Já que multiplicação é adição repetida.

~~~
separador = '=' * 10
print(separador)
~~~
{: .language-python}
~~~
==========
~~~
{: .output}

## Strings têm um comprimento (mas números não).

<!--
*   The built-in function `len` counts the number of characters in a string. 
-->
*   A função embutida `len` (*length*) conta o número de caracteres em uma string.

~~~
print(len(nome_completo))
~~~
{: .language-python}
~~~
15
~~~
{: .output}

<!-- 
*   But numbers don't have a length (not even zero).
 -->

*   Mas números não tem um comprimento (nem zero).


~~~
print(len(52))
~~~
{: .language-python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-f769e8e8097d> in <module>()
----> 1 print(len(52))

TypeError: object of type 'int' has no len()
~~~
{: .error}

## <a name='convert-numbers-and-strings'></a> É necessário converter números para strings e vice-versa para poder fazer operações entre eles.

<!-- 
*   Cannot add numbers and strings.
 -->
*   Não é possível somar números e strings.

~~~
print(1 + '2')
~~~
{: .language-python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-fe4f54a023c6> in <module>()
----> 1 print(1 + '2')

TypeError: unsupported operand type(s) for +: 'int' and 'str'
~~~
{: .error}
<!-- 
*   Not allowed because it's ambiguous: should `1 + '2'` be `3` or `'12'`?
*   Some types can be converted to other types by using the type name as a function.
 -->

*   Não é permitido porque é ambíguo: `1 + '2'` deve ser `3` ou `'12'`?
*   Alguns tipos podem ser convertidos para outros tipos ao usar o nome do tipo como um função.

~~~
print(1 + int('2'))
print(str(1) + '2')
~~~
{: .language-python}
~~~
3
12
~~~
{: .output}

## É possível misturar *integers* e *floats* livremente entre operações.
<!-- 
*   Integers and floating-point numbers can be mixed in arithmetic.
    *   Python 3 automatically converts integers to floats as needed.
 -->

*   Números inteiros e de ponto flutuante pode ser misturados em aritmética.
    *   Python 3 automaticamente converte *integers* para *floats* conforme o necessário.

~~~
print('meio é', 1 / 2.0)
print('três ao quadrado é', 3.0 ** 2)
~~~
{: .language-python}
~~~
meio é 0.5
três ao quadrado é 9.0
~~~
{: .output}

## Variáveis só mudam de valor quando algo é assinalado a elas.
<!-- 
*   If we make one cell in a spreadsheet depend on another,
    and update the latter,
    the former updates automatically.
*   This does **not** happen in programming languages.
 -->

*   Se fizermos uma célula em uma planilha depender de outra,
    e fizermos update da última,
    a primeira faz update automaticamente.
*   Isso **não** acontece em linguagens de programação.

~~~
primeiro = 1
segundo = 5 * primeiro
primeiro = 2
print('primeiro é', primeiro, 'e segundo é', segundo)
~~~
{: .language-python}
~~~
primeiro é 2 e segundo é 5
~~~
{: .output}
<!-- 
*   The computer reads the value of `first` when doing the multiplication,
    creates a new value, and assigns it to `second`.
*   After that, `second` does not remember where it came from.
 -->

*   O computador lê o valor de `primeiro` quando faz a multiplicação,
    cria um novo valor, e assinala para `segundo`.
*   Depois disso, `segundo` não lembra da onde veio o valor original.

<!-- 
> ## Fractions
>
> What type of value is 3.4?
> How can you find out?
>
> > ## Solution
> >
> > It is a floating-point number (often abbreviated "float").
> > It is possible to find out by using the built-in function `type()`.
> >
> > ~~~
> > print(type(3.4))
> > ~~~
> > {: .language-python}
> > ~~~
> > <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Frações
>
> Que tipo de valor é `3.4`?
> Como você pode descobrir?
>
> > ## Solução
> >
> > É um número de ponto flutuante (normalmente abreviado de "float").
> > É possível descobrir usando a função embutida `type`.
> >
> > ~~~
> > print(type(3.4))
> > ~~~
> > {: .language-python}
> > ~~~
> > <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Automatic Type Conversion
>
> What type of value is 3.25 + 4?
>
> > ## Solution
> >
> > It is a float:
> > integers are automatically converted to floats as necessary.
> >
> > ~~~
> > result = 3.25 + 4
> > print(result, 'is', type(result))
> > ~~~
> > {: .language-python}
> > ~~~
> > 7.25 is <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Conversão Automática de Tipos
>
> Que tipo é o valor `3.25 + 4`?
>
> > ## Solução
> >
> > É um float:
> > inteiros são automaticamente convertidos para floats conforme o necessário.
> >
> > ~~~
> > resultado = 3.25 + 4
> > print(resultado, 'é', type(resultado))
> > ~~~
> > {: .language-python}
> > ~~~
> > 7.25 is <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Choose a Type
>
> What type of value (integer, floating point number, or character string)
> would you use to represent each of the following?  Try to come up with more than one good answer for each problem.  For example, in  # 1, when would counting days with a floating point variable make more sense than using an integer?  
>
> 1. Number of days since the start of the year.
> 2. Time elapsed from the start of the year until now in days.
> 3. Serial number of a piece of lab equipment.
> 4. A lab specimen's age
> 5. Current population of a city.
> 6. Average population of a city over time.
>
> > ## Solution
> >
> > The answers to the questions are:
> > 1. Integer, since the number of days would lie between 1 and 365. 
> > 2. Floating point, since fractional days are required
> > 3. Character string if serial number contains letters and numbers, otherwise integer if the serial number consists only of numerals
> > 4. This will vary! How do you define a specimen's age? whole days since collection (integer)? date and time (string)?
> > 5. Choose floating point to represent population as large aggregates (eg millions), or integer to represent population in units of individuals.
> > 6. Floating point number, since an average is likely to have a fractional part.
> {: .solution}
{: .challenge}
 -->

> ## Escolha um Tipo
>
> Que tipo de valor (inteiro, número de ponto flutuante, ou string de caracteres)
> você usaria para representar cada um dos seguintes? Tente pensar em mais de uma boa resposta para cada problema. Por exemplo, no número 1, quando contar os dias com uma variável de ponto flutuante faria mais sentido do que usar um inteiro?
>
> 1. Número de dias desde o início do ano.
> 2. Tempo do início do ano até agora em dias.
> 3. Número serial de um patrimônio.
> 4. A validade de uma inspeção de segurança.
> 5. População atual de um município.
> 6. População média de um município ao longo do tempo.
>
> > ## Solução
> >
> > The answers to the questions are:
> > 1. Inteiro, já que o número de dias ficaria entre 1 e 365.
> > 2. Ponto flutuante, já que os dias fracionais são necessários.
> > 3. String se o número serial contém letras e números, se não um integer se o número serial contém apenas números (**e não começa com zero**).
> > 4. Isso pode variar! Como você define a validade? Dias desde a última inspeção (integer)? Data de validade (string)?
> > 5. Float para representar a populações como grandes agregados (como milhões), ou inteiro para representar a população em unidades de indivíduos.
> > 6. Número de ponto flutuante, já que a média provavelmente vai possuir um valor fracional.
> {: .solution}
{: .challenge}

<!-- 
> ## Division Types
>
> In Python 3, the `//` operator performs integer (whole-number) floor division, the `/` operator performs floating-point
> division, and the `%` (or *modulo*) operator calculates and returns the remainder from integer division:
>
> ~~~
> print('5 // 3:', 5 // 3)
> print('5 / 3:', 5 / 3)
> print('5 % 3:', 5 % 3)
> ~~~
> {: .language-python}
>
> ~~~
> 5 // 3: 1
> 5 / 3: 1.6666666666666667
> 5 % 3: 2
> ~~~
> {: .output}
>
> If `num_participantes` is the number of subjects taking part in a study,
> and `num_por_entrevista` is the number that can take part in a single survey,
> write an expression that calculates the number of surveys needed
> to reach everyone once.
>
> > ## Solution
> > We want the minimum number of surveys that reaches everyone once, which is
> > the rounded up value of `num_participantes/ num_por_entrevista`. This is 
> > equivalent to performing a floor division with `//` and adding 1. Before
> > the division we need to subtract 1 from the number of subjects to deal with 
> > the case where `num_participantes` is evenly divisible by `num_por_entrevista`.
> > ~~~
> > num_participantes = 600
> > num_por_entrevista = 42
> > num_entrevistas = (num_participantes - 1) // num_por_entrevista + 1
> >
> > print(num_participantes, 'subjects,', num_por_entrevista, 'per survey:', num_entrevistas)
> > ~~~
> > {: .language-python}
> > ~~~
> > 600 subjects, 42 per survey: 15
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Tipos de Divisão
>
> No Python 3, o operador `//` realiza divisão de inteiros, o operador `/` realiza divisão de ponto flutuante,
> e o operador `%` (ou *módulo*) calcula o resto da divisão de inteiros.
>
> ~~~
> print('5 // 3:', 5 // 3)
> print('5 / 3:', 5 / 3)
> print('5 % 3:', 5 % 3)
> ~~~
> {: .language-python}
>
> ~~~
> 5 // 3: 1
> 5 / 3: 1.6666666666666667
> 5 % 3: 2
> ~~~
> {: .output}
>
> Se `num_participantes` é o número de participantes em um estudo,
> e `num_por_entrevista` é o número que pode participar em uma única entrevista,
> escreva uma expressão que calcula o número mínimo de entrevistas necessárias
> para incluir todos os participantes.
>
> > ## Solução
> > Queremos o mínimo número de entrevistas que inclua todos os participantes,
> > que seria o valor arredondado de `num_participantes / num_por_entrevista`. Isso é
> > equivalente a realizar a divisão de inteiros com `//` e adicionar 1. Antes
> > da divisão precisamos subtrair 1 do número de participantes para lidar com
> > o caso no qual `num_participantes` é dividido igualmente port `num_por_entrevista`.
> > ~~~
> > num_participantes = 600
> > num_por_entrevista = 42
> > num_entrevistas = (num_participantes - 1) // num_por_entrevista + 1
> >
> > print(num_participantes, 'participantes,', num_por_entrevista, 'por entrevista:', num_entrevistas)
> > ~~~
> > {: .language-python}
> > ~~~
> > 600 participantes, 42 por entrevista: 15
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Strings to Numbers
>
> Where reasonable, `float()` will convert a string to a floating point number,
> and `int()` will convert a floating point number to an integer:
>
> ~~~
> print("string to float:", float("3.4"))
> print("float to int:", int(3.4))
> ~~~
> {: .language-python}
>
> ~~~
> string to float: 3.4
> float to int: 3
> ~~~
> {: .output}
>
> If the conversion doesn't make sense, however, an error message will occur.
>
> ~~~
> print("string to float:", float("Hello world!"))
> ~~~
> {: .language-python}
>
> ~~~
> ---------------------------------------------------------------------------
> ValueError                                Traceback (most recent call last)
> <ipython-input-5-df3b790bf0a2> in <module>
> 1 print("string to float:", float("Hello world!"))
>
> ValueError: could not convert string to float: 'Hello world!'
> ~~~
> {: .error}
>
> Given this information, what do you expect the following program to do?
>
> What does it actually do?
>
> Why do you think it does that?
>
> ~~~
> print("fractional string to int:", int("3.4"))
> ~~~
> {: .language-python}
> 
> > ## Solution
> > What do you expect this program to do? It would not be so unreasonable to expect the Python 3 `int` command to
> > convert the string "3.4" to 3.4 and an additional type conversion to 3. After all, Python 3 performs a lot of other
> > magic - isn't that part of its charm?
> >
> > ~~~
> > int("3.4")
> > ~~~
> > {: .language-python}
> > ~~~
> > ---------------------------------------------------------------------------
> > ValueError                                Traceback (most recent call last)
> > <ipython-input-2-ec6729dfccdc> in <module>
> > 1 int("3.4")
> > ValueError: invalid literal for int() with base 10: '3.4'
> > ~~~
> > {: .output}
> > However, Python 3 throws an error. Why? To be consistent, possibly. If you ask Python to perform two consecutive
> > typecasts, you must convert it explicitly in code.
> > ~~~
> > int(float("3.4"))
> > ~~~
> > {: .language-python}
> > ~~~
> > 3
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
 -->

> ## Strings para Números
>
> Quando possível, `float()` vai converter a string em um número de ponto flutuante,
> e `int()` vai converter o número de ponto flutuante em um inteiro.
>
> ~~~
> print("string para float:", float("3.4"))
> print("float para int:", int(3.4))
> ~~~
> {: .language-python}
>
> ~~~
> string para float: 3.4
> float para int: 3
> ~~~
> {: .output}
>
> Se a conversão não fizer sentido, vai ocorrer um erro.
>
> ~~~
> print("string para float:", float("Olá Mundo!"))
> ~~~
> {: .language-python}
>
> ~~~
> ---------------------------------------------------------------------------
> ValueError                                Traceback (most recent call last)
> <ipython-input-5-df3b790bf0a2> in <module>
> ----> 1 print("string para float:", float("Olá Mundo!"))
>
> ValueError: could not convert string to float: 'Olá Mundo!'
> ~~~
> {: .error}
>
> Dada essa informação, o que você espera que o programa abaixo vai fazer?
>
> O que ele realmente faz?
>
> Por que você acha que ele faz isso?
>
> ~~~
> print("string de fração para int:", int("3.4"))
> ~~~
> {: .language-python}
> 
> > ## Solução
> > O que você espera que eswse programa faça? Não seria razoável que o comando `int` do Python 3
> > convertesse a string `"3.4"` para `3.4` e uma conversão adicional para `3`. Afinal, o Python 3 faz mais um monte de
> > mágicas - isso não faz parte do charme?
> >
> > ~~~
> > int("3.4")
> > ~~~
> > {: .language-python}
> > ~~~
> > ---------------------------------------------------------------------------
> > ValueError                                Traceback (most recent call last)
> > <ipython-input-2-ec6729dfccdc> in <module>
> > ----> 1 int("3.4")
> > ValueError: invalid literal for int() with base 10: '3.4'
> > ~~~
> > {: .output}
> > VEmos que o Python 3 dá erro. Por quê? Possivelmente para se manter consistente. Se você pedir para o Python realizar duas
> > conversões de tipo consecutivas, você precisa declarar isso explicitamente no código.
> > ~~~
> > int(float("3.4"))
> > ~~~
> > {: .language-python}
> > ~~~
> > 3
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

<!-- 
> ## Arithmetic with Different Types
>
> Which of the following will return the floating point number `2.0`?
> Note: there may be more than one right answer.
>
> ~~~
> first = 1.0
> second = "1"
> third = "1.1"
> ~~~
> {: .language-python}
>
> 1. `first + float(second)`
> 2. `float(second) + float(third)`
> 3. `first + int(third)`
> 4. `first + int(float(third))`
> 5. `int(first) + int(float(third))`
> 6. `2.0 * second`
>
> > ## Solution
> >
> > Answer: 1 and 4
> {: .solution}
{: .challenge}
 -->

> ## Aritmética com Diferentes Tipos
>
> Qual dos seguintes vai retornar o número de ponto flutuante `2.0`?
> Nota: pode haver mais de uma resposta certa.
>
> ~~~
> primeiro = 1.0
> segundo = "1"
> terceiro = "1.1"
> ~~~
> {: .language-python}
>
> 1. `primeiro + float(segundo)`
> 2. `float(segundo) + float(terceiro)`
> 3. `primeiro + int(terceiro)`
> 4. `primeiro + int(float(terceiro))`
> 5. `int(primeiro) + int(float(terceiro))`
> 6. `2.0 * segundo`
>
> > ## Solução
> >
> > Resposta: 1 e 4.
> {: .solution}
{: .challenge}

<!-- 
> ## Complex Numbers
>
> Python provides complex numbers,
> which are written as `1.0+2.0j`.
> If `val` is a complex number,
> its real and imaginary parts can be accessed using *dot notation*
> as `val.real` and `val.imag`.
>
> ~~~
> complex = 6 + 2j
> print(complex.real)
> print(complex.imag)
> ~~~
> {: .language-python}
>
> ~~~
> 6.0
> 2.0
> ~~~
> {: .output}
>
>
> 1.  Why do you think Python uses `j` instead of `i` for the imaginary part?
> 2.  What do you expect `1+2j + 3` to produce?
> 3.  What do you expect `4j` to be?  What about `4 j` or `4 + j`?
> 
> > ## Solution
> >
> > 1. Standard mathematics treatments typically use `i` to denote an imaginary number. However, from media reports it
> > was an early convention established from electrical engineering that now presents a technically expensive area to
> > change. [Stack Overflow provides additional explanation and
> > discussion.](http://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i)
> > 2. `(4+2j)`
> > 3. `4j` and `Syntax Error: invalid syntax`. In the latter cases, `j` is considered a variable and the statement
> > depends on if `j` is defined and if so, its assigned value.
> {: .solution}
{: .challenge}
 -->

<!-- OC -->
> ## Somando Fatias
> 
> Como substrings também são strings, é possível somá-las da mesma força que somamos strings.
> A partir da variável `empresa`, escreva o código para criar a variável `abrev`, usando
> o index de cada letra e o operador `+`.
>
> ~~~
> empresa = "Companhia Paulista de Força e Luz"
> abrev = __________
> print(abrev)
> ~~~
> {: .language-python}
> ~~~
> CPFL
> ~~~
> {: .output}
> > ## Solução
> > 
> > ~~~
> > empresa = "Companhia Paulista de Força e Luz"
> > abrev = empresa[0] + empresa[10] + empresa[22] + empresa[30]
> > print(abrev)
> > ~~~
> > {: language-python}


> ## Números Complexos
>
> Python vem com números complexos,
> escritos como `1 + 2j`.
> Se `val` é um número complexo,
> suas partes reais e imaginárias podem ser acessadas usando *notação de ponto*
> como `val.real` e `val.imag`.
>
> ~~~
> complexo = 6 + 2j
> print(complexo.real)
> print(complexo.imag)
> ~~~
> {: .language-python}
>
> ~~~
> 6.0
> 2.0
> ~~~
> {: .output}
>
>
> 1.  Por que você acha que usamos `j` e não `i` para a parte imaginária?
> 2.  O que você espera que `1 + 2j + 3` vai produzir?
> 3.  O que você espera `4j` será? E `4 j` ou `4 + j`?
> 
> > ## Solução
> >
> > 1. Tratados padrão da matemática tipicamente usam `i` para denotar um número imaginário. No entanto, isso foi
> > foi uma convenção estabelecida cedo na área de engenharia elétrica e agora representa um área tecnicamente custosa para
> > modificar. [Existe uma explicação e discussão adicional no
> > Stack Overflow.](http://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i)
> > 2. `(4+2j)`
> > 3. `4j` e `Syntax Error: invalid syntax`. Nos dois últimos casos, `j` é considerada uma variável e a declaração
> > depende de se `j` já foi definido, e do seu valor assinalado.
> {: .solution}
{: .challenge}
