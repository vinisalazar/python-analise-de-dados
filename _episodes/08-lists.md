---
title: "Listas"
teaching: 10
exercises: 10
questions:
- "Como eu posso armazenar muitos valores?"
objectives:
- "Explicar por que programas precisam de coleções de valores."
- "Escrever programas que criem, indexem, fatiem e modifiquem listas planas através de assinalação e chamadas de métodos."
keypoints:
- "Uma lista armazena muitos valores em uma única estrutura."
- "Use o index de um item para selecioná-lo na lista."
- "Os valores da lista podem ser substituídos por assinalação."
- "Apendar itens para uma lista aumenta ela."
- "Use `del` para remover inteiramente itens de uma lista."
- "Uma lista vazia não contém valores."
- "Listas podem conter valores de diferentes tipos."
- "Strings de caracteres podem ser indexadas como listas."
- "Strings de caracteres são imutáveis."
- "Indexar além do fim de uma coleção é um erro."
---
<!-- 
## A list stores many values in a single structure.

*   Doing calculations with a hundred variables called `pressure_001`, `pressure_002`, etc.,
    would be at least as slow as doing them by hand.
*   Use a *list* to store many values together.
    *   Contained within square brackets `[...]`.
    *   Values separated by commas `,`.
*   Use `len` to find out how many values are in a list.

~~~
pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))
~~~
{: .language-python}
~~~
pressures: [0.273, 0.275, 0.277, 0.275, 0.276]
length: 5
~~~
{: .output}
 -->

## Uma lista armazena muitos valores em uma única estrutura

*   Fazer operações com cem variáveis chamadas `consumo_001`, `consumo_002`, etc.
    seriam pelo menos tão lento quanto fazer isso na mão.
*   Use uma *lista* (`list`) para armazenar vários valores juntos.
    *   A lista fica entre colchetes `[...]`.
    *   Valores são separados por vírgula.
*   Use `len` para descobrir quantos valores tem uma lista.

~~~
consumos = [0.273, 0.275, 0.277, 0.275, 0.276]
print('consumos:', consumos)
print('comprimento:', len(consumos))
~~~
{: .language-python}
~~~
consumos: [0.273, 0.275, 0.277, 0.275, 0.276]
comprimento: 5
~~~
{: .output}
<!-- 
## Use an item's index to fetch it from a list.

*   Just like strings.

~~~
print('zeroth item of pressures:', pressures[0])
print('fourth item of pressures:', pressures[4])
~~~
{: .language-python}
~~~
zeroth item of pressures: 0.273
fourth item of pressures: 0.276
~~~
{: .output}
 -->

## Use o index de um item para selecioná-lo na lista.

*   Assim como strings.

~~~
print('primeiro item de consumos:', consumos[0])
print('quinto item de consumos:', consumos[4])
~~~
{: .language-python}
~~~
primeiro item de consumos: 0.273
quinto item de consumos: 0.276
~~~
{: .output}
<!-- 
## Lists' values can be replaced by assigning to them.

*   Use an index expression on the left of assignment to replace a value.

~~~
pressures[0] = 0.265
print('pressures is now:', pressures)
~~~
{: .language-python}
~~~
pressures is now: [0.265, 0.275, 0.277, 0.275, 0.276]
~~~
{: .output}
 -->

## Os valores da lista podem ser substituídos por assinalação.

*   Use uma expressão de index na esquerda da assinalação para substituir um valor.

~~~
consumos[0] = 0.265
print('consumos agora é:', consumos)
~~~
{: .language-python}
~~~
consumos agora é: [0.265, 0.275, 0.277, 0.275, 0.276]
~~~
{: .output}
<!-- 
## Appending items to a list lengthens it.

*   Use `list_name.append` to add items to the end of a list.

~~~
primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
print('primes has become:', primes)
~~~
{: .language-python}
~~~
primes is initially: [2, 3, 5]
primes has become: [2, 3, 5, 7]
~~~
{: .output}

*   `append` is a *method* of lists.
    *   Like a function, but tied to a particular object.
*   Use `object_name.method_name` to call methods.
    *   Deliberately resembles the way we refer to things in a library.
*   We will meet other methods of lists as we go along.
    *   Use `help(list)` for a preview.
*   `extend` is similar to `append`, but it allows you to combine two lists.  For example:

~~~
teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
primes.extend(teen_primes)
print('primes has now become:', primes)
primes.append(middle_aged_primes)
print('primes has finally become:', primes)
~~~
{: .language-python}
~~~
primes is currently: [2, 3, 5, 7]
primes has now become: [2, 3, 5, 7, 11, 13, 17, 19]
primes has finally become: [2, 3, 5, 7, 11, 13, 17, 19, [37, 41, 43, 47]]
~~~
{: .output}

Note that while `extend` maintains the "flat" structure of the list, appending a list to a list makes the result
two-dimensional - the last element in `primes` is a list, not an integer.
 -->

## Apendar itens para uma lista aumenta ela.

*   Use `list_name.append` para adicionar itens ao fim de uma lista.

~~~
primos = [2, 3, 5]
print('primos inicialmente é:', primos)
primos.append(7)
print('primos agora é:', primos)
~~~
{: .language-python}
~~~
primos inicialmente é: [2, 3, 5]
primos agora é: [2, 3, 5, 7]
~~~
{: .output}

*   `append` é um *método* de listas.
    *   Assim como uma função, mas associado a um objeto em particular.
*   Use `nome_objeto.nome_metodo` para chamar um método.
    *   Deliberadamente lembra o jeito que nos referimos a coisas de uma biblioteca.
*   Vamos encontrar outros métodos de listas a medida que vamos avançando.
    *   Use `help(list)` para um preview.
*   `extend` é similar a `append`, mas permite combinar duas listas.  Por exemplo:

~~~
primos_adolescentes = [11, 13, 17, 19]
primos_meia_idade = [37, 41, 43, 47]
print('primos agora é:', primos)
primos.extend(primos_adolescentes)
print('primos agora virou:', primos)
primos.append(primos_meia_idade)
print('primos finalmente virou:', primos)
~~~
{: .language-python}
~~~
primos agora é: [2, 3, 5, 7]
primos agora virou: [2, 3, 5, 7, 11, 13, 17, 19]
primos finalmente virou: [2, 3, 5, 7, 11, 13, 17, 19, [37, 41, 43, 47]]
~~~
{: .output}

Note que enquanto `extend` mantém a estrutura "plana" da lista, apendar uma lista para outra lista torna o resultado bidimensional - o último elemento de `primos` é uma lista, não um inteiro.

<!-- 
## Use `del` to remove items from a list entirely.

*   We use `del list_name[index]` to remove an element from a list (in the example, 9 is not a prime number) and thus shorten it.
*   `del` is not a function or a method, but a statement in the language.

~~~
primes = [2, 3, 5, 7, 9]
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)
~~~
{: .language-python}
~~~
primes before removing last item: [2, 3, 5, 7, 9]
primes after removing last item: [2, 3, 5, 7]
~~~
{: .output}
 -->

## Use `del` para remover inteiramente itens de uma lista.

*   Usamos `del nome_lista[index]` para remover um elemento de uma lista (no exemplo, 9 não é um número primo) e então encurtá-la.
*   `del` não é uma função ou método, e sim uma declaração (*statement*) da linguagem.

~~~
primos = [2, 3, 5, 7, 9]
print('primos antes de remover o último item:', primos)
del primos[4]
print('primos depois de remover o último item:', primos)
~~~
{: .language-python}
~~~
primos antes de remover o último item: [2, 3, 5, 7, 9]
primos depois de remover o último item: [2, 3, 5, 7]
~~~
{: .output}
<!-- 
## The empty list contains no values.

*   Use `[]` on its own to represent a list that doesn't contain any values.
    *   "The zero of lists."
*   Helpful as a starting point for collecting values
        (which we will see in the [next episode]({{ page.root }}/12-for-loops/)).
 -->

## Uma lista vazia não contém valores.

*   Use `[]` sozinho para representar uma lista que não contém valores.
    *   "O zero das listas."
*   É útil como um 'ponto de partida' para coletar valores
        (o que vamos ver no [próximo episódio]({{ page.root }}/12-for-loops/)).

<!-- 
## Lists may contain values of different types.

*   A single list may contain numbers, strings, and anything else.

~~~
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
~~~
{: .language-python}
 -->

## Listas podem conter valores de diferentes tipos.

*   Uma única lista pode conter números, strings, e qualquer outra coisa.

~~~
objetivos = [1, 'Criar listas.', 2, 'Extrair itens de listas.', 3, 'Modificar listas.']
~~~
{: .language-python}
<!-- 
## Character strings can be indexed like lists.

*   Get single characters from a character string using indexes in square brackets.

~~~
element = 'carbon'
print('zeroth character:', element[0])
print('third character:', element[3])
~~~
{: .language-python}
~~~
zeroth character: c
third character: b
~~~
{: .output}
 -->

## Strings de caracteres podem ser indexadas como listas.

*   Pegue caracteres únicos de uma string de caracteres usando índices em colchetes.

~~~
elemento = 'carbono'
print('caracter zero:', elemento[0])
print('caracter três:', elemento[3])
~~~
{: .language-python}
~~~
zeroth character: c
third character: b
~~~
{: .output}
<!-- 
## Character strings are immutable.

*   Cannot change the characters in a string after it has been created.
    *   *Immutable*: can't be changed after creation.
    *   In contrast, lists are *mutable*: they can be modified in place.
*   Python considers the string to be a single value with parts,
    not a collection of values.

~~~
element[0] = 'C'
~~~
{: .language-python}
~~~
TypeError: 'str' object does not support item assignment
~~~
{: .error}

*   Lists and character strings are both *collections*.
 -->

## Strings de caracteres são imutáveis.

*   Não é possível alterar os caracteres de uma string depois que ela foi criada.
    *   *Imutável*: não pode ser alterada depois da criação.
    *   Em contraste, listas são *mutáveis*: elas podem ser modificadas (*in place*).
*   Python considera que uma string é um único valor com várias partes,
    não uma coleção de valores.

~~~
elemento[0] = 'C'
~~~
{: .language-python}
~~~
TypeError: 'str' object does not support item assignment
~~~
{: .error}

*   Listas e strings de caracteres são ambas *coleções*.
<!-- 
## Indexing beyond the end of the collection is an error.

*   Python reports an `IndexError` if we attempt to access a value that doesn't exist.
    *   This is a kind of [runtime error]({{ page.root }}/04-built-in/#runtime-error).
    *   Cannot be detected as the code is parsed
        because the index might be calculated based on data.

~~~
print('99th element of element is:', element[99])
~~~
{: .language-python}
~~~
IndexError: string index out of range
~~~
{: .output}
 -->

## Indexar além do fim de uma coleção é um erro.

*   Python reporta um `IndexError` se tentamos acessar um valor que não existe.
    *   Isso é um tipo de erro de [runtime]({{ page.root }}/04-built-in/#runtime-error).
    *   Não pode ser detectado quando o código é avaliado
        porque o index pode ser calculado baseado nos dados.

~~~
print('99ésimo elemento de elemento é:', elemento[99])
~~~
{: .language-python}
~~~
IndexError: string index out of range
~~~
{: .output}
<!-- 
> ## Fill in the Blanks
>
> Fill in the blanks so that the program below produces the output shown.
>
> ~~~
> values = ____
> values.____(1)
> values.____(3)
> values.____(5)
> print('first time:', values)
> values = values[____]
> print('second time:', values)
> ~~~
> {: .language-python}
>
> ~~~
> first time: [1, 3, 5]
> second time: [3, 5]
> ~~~
> {: .output}
>
> > ## Solução
> > ~~~
> > values = []
> > values.append(1)
> > values.append(3)
> > values.append(5)
> > print('first time:', values)
> > values = values[1:]
> > print('second time:', values)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
 -->

> ## Preencha os Brancos
>
> Preencha os campos em branco para que o programa abaixo produza a saída correta.
>
> ~~~
> valores = ____
> valores.____(1)
> valores.____(3)
> valores.____(5)
> print('primeira vez:', valores)
> valores = valores[____]
> print('segunda vez:', valores)
> ~~~
> {: .language-python}
>
> ~~~
> primeira vez: [1, 3, 5]
> segunda vez: [3, 5]
> ~~~
> {: .output}
>
> > ## Solução
> > ~~~
> > valores = []
> > valores.append(1)
> > valores.append(3)
> > valores.append(5)
> > print('primeira vez:', valores)
> > valores = valores[1:]
> > print('segunda vez:', valores)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
<!-- 
> ## How Large is a Slice?
>
> If 'low' and 'high' are both non-negative integers,
> how long is the list `values[low:high]`?
>
> > ## Solução
> > The list `values[low:high]` has `high - low` elements.  For example,
> > `values[1:4]` has the 3 elements `values[1]`, `values[2]`, and `values[3]`.
> > Note that the expression will only work if `high` is less than the total
> > length of the list `values`.
> {: .solution}
{: .challenge}
 -->

> ## Quão Grande é uma Fatia?
>
> Se `baixo` e `cima`são ambos inteiros não-negativos,
> quão longa é a lista `valores[baixo:cima]`?
>
> > ## Solução
> > A lista `valores[baixo:cima]` tem `cima - baixo` elementos.  Por exemplo,
> > `valores[1:4]` tem 3 elementos `valores[1]`, `valores[2]`, and `valores[3]`.
> > Note que a expressão só vai funcionar se `cima` for menos que o comprimento
> > total da lista `valores`.
> {: .solution}
{: .challenge}
<!-- 
> ## From Strings to Lists and Back
>
> Given this:
>
> ~~~
> print('string to list:', list('tin'))
> print('list to string:', ''.join(['g', 'o', 'l', 'd']))
> ~~~
> {: .language-python}
> ~~~
> string to list: ['t', 'i', 'n']
> list to string: gold
> ~~~
> {: .output}
>
> 1.  What does `list('some string')` do?
> 2.  What does `'-'.join(['x', 'y', 'z'])` generate?
>
> > ## Solução
> > 1. [`list('some string')`](https://docs.python.org/3/library/stdtypes.html#list) converts a string into a list containing all of its characters.
> > 2. [`join`](https://docs.python.org/3/library/stdtypes.html#str.join) returns a string that is the _concatenation_
> >    of each string element in the list and adds the separator between each element in the list. This results in
> >    `x-y-z`. The separator between the elements is the string that provides this method.
> {: .solution}
{: .challenge}
 -->

> ## De Strings para Listas e de Volta
>
> Dado isso:
>
> ~~~
> print('string para lista:', list('latão'))
> print('lista para string:', ''.join(['o', 'u', 'r', 'o']))
> ~~~
> {: .language-python}
> ~~~
> string para lista: ['l', 'a', 't', 'ã', 'o']
> lista para string: ouro
> ~~~
> {: .output}
>
> 1.  O que `list('alguma string')` faz?
> 2.  O que `'-'.join(['x', 'y', 'z'])` gera?
>
> > ## Solução
> > 1. [`list('alguma string')`](https://docs.python.org/pt-br/3/library/stdtypes.html#list) converte uma string em uma lista contendo todos os caracteres.
> > 2. [`join`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.join) retorna uma string que é uma _concatenação_
> >    de cada elemento de string na lista e adicionar o separador entre cada elemento da lista. Isso resulta é 
> >    `x-y-z`. O separador entre os elementos é a string que provê esse método.
> {: .solution}
{: .challenge}
<!-- 
> ## Working With the End
>
> What does the following program print?
>
> ~~~
> element = 'helium'
> print(element[-1])
> ~~~
> {: .language-python}
>
> 1.  How does Python interpret a negative index?
> 2.  If a list or string has N elements,
>     what is the most negative index that can safely be used with it,
>     and what location does that index represent?
> 3.  If `values` is a list, what does `del values[-1]` do?
> 4.  How can you display all elements but the last one without changing `values`?
>     (Hint: you will need to combine slicing and negative indexing.)
>
> > ## Solução
> > The program prints `m`.
> > 1. Python interprets a negative index as starting from the end (as opposed to
> >    starting from the beginning).  The last element is `-1`.
> > 2. The last index that can safely be used with a list of N elements is element
> >    `-N`, which represents the first element.
> > 3. `del values[-1]` removes the last element from the list.
> > 4. `values[:-1]`
> {: .solution}
{: .challenge}
 -->

> ## Trabalhando com o Fim
>
> O que o seguinte programa imprime?
>
> ~~~
> elemento = 'helio'
> print(elemento[-1])
> ~~~
> {: .language-python}
>
> 1.  Como o Python interpreta um index negativo?
> 2.  Se uma lista ou string tem N elementos,
>     qual é o index mais negativo que pode ser usado corretamente com ela,
>     e que localidade esse index representa?
> 3.  Se `valores` é uma lista, o que `del valores[-1]` faz?
> 4.  Como você pode mostrar todos os elementos menos o último sem modificar `valores`?
>     (Dica: você vai precisar combinar fatias e índices negativos.
>
> > ## Solução
> > The program prints `o`.
> > 1. Python interpreta um index negativo como começando do fim (ao oposto de 
> >    começar do início).  O último elemento é `-1`.
> > 2. O último index que pode ser utilizado corretamente com uma lista de N elementos é o elemento
> >    `-N`, que representa o primeiro elemento da lista.
> > 3. `del values[-1]` remove o último elemento da lista.
> > 4. `values[:-1]`
> {: .solution}
{: .challenge}
<!-- 
> ## Stepping Through a List
>
> What does the following program print?
>
> ~~~
> element = 'fluorine'
> print(element[::2])
> print(element[::-1])
> ~~~
> {: .language-python}
>
> 1.  If we write a slice as `low:high:stride`, what does `stride` do?
> 2.  What expression would select all of the even-numbered items from a collection?
>
> > ## Solução
> > The program prints
> > ~~~
> > furn
> > eniroulf
> > ~~~
> > {: .language-python}
> > 1. `stride` is the step size of the slice.
> > 2. The slice `1::2` selects all even-numbered items from a collection: it starts
> >    with element `1` (which is the second element, since indexing starts at `0`),
> >    goes on until the end (since no `end` is given), and uses a step size of `2`
> >    (i.e., selects every second element).
> {: .solution}
{: .challenge}
 -->

> ## Degraus em Uma Lista
>
> O que o seguinte programa imprime?
>
> ~~~
> cidade = "florianopolis"
> print(cidade[::2])
> print(cidade[::-1])
> ~~~
> {: .language-python}
>
> 1.  Se escrevermos uma fatia como `inicio:fim:degrau`, o que `degrau` faz?
> 2.  Que expressão iria selecionar todos os elementos em posições pares de uma coleção?
>
> > ## Solução
> > Esse programa imprime
> > ~~~
> > foinpls
> > siloponairolf
> > ~~~
> > {: .language-python}
> > 1. `degrau` é o número do 'passo' de uma fatia.
> > 2. A fatia `1::2` seleciona todos os elementos em posições pares de uma lista: começa
> >    com o elemento `1` (que é o segundo elemento, já que a indexação começa com `0`),
> >    vai até o fim (já que `fim` não é dado), usa um passo de tamanho `2
> >    (*i.e.*, seleciona a cada dois elementos).
> {: .solution}
{: .challenge}
<!-- 
> ## Slice Bounds
>
> What does the following program print?
>
> ~~~
> element = 'lithium'
> print(element[0:20])
> print(element[-1:3])
> ~~~
> {: .language-python}
>
> > ## Solução
> > ~~~
> > lithium
> > 
> > ~~~
> > {: .output}
> The first statement prints the whole string, since the slice goes beyond the total length of the string.
> The second statement returns an empty string, because the slice goes "out of bounds" of the string.
> {: .solution}
{: .challenge}
 -->

> ## Limites de Fatias
>
> What does the following program print?
>
> ~~~
> cidade = 'sorocaba'
> print(cidade[0:20])
> print(cidade[-1:3])
> ~~~
> {: .language-python}
>
> > ## Solução
> > ~~~
> > sorocaba
> > 
> > ~~~
> > {: .output}
> A primeira linha imprime a string inteira, já que a fatia vai além do comprimento total da string.
> A segunda linha retorna uma string vazia, já que a fatia "sai dos limites" da string.
> {: .solution}
{: .challenge}
<!-- 
> ## Sort and Sorted
>
> What do these two programs print?
> In simple terms, explain the difference between `sorted(letters)` and `letters.sort()`.
>
> ~~~
> # Program A
> letters = list('gold')
> result = sorted(letters)
> print('letters is', letters, 'and result is', result)
> ~~~
> {: .language-python}
>
> ~~~
> # Program B
> letters = list('gold')
> result = letters.sort()
> print('letters is', letters, 'and result is', result)
> ~~~
> {: .language-python}
>
> > ## Solução
> > Program A prints
> > ~~~
> > letters is ['g', 'o', 'l', 'd'] and result is ['d', 'g', 'l', 'o']
> > ~~~
> > {: .output}
> > Program B prints
> > ~~~
> > letters is ['d', 'g', 'l', 'o'] and result is None
> > ~~~
> > {: .output}
> > `sorted(letters)` returns a sorted copy of the list `letters` (the original
> > list `letters` remains unchanged), while `letters.sort()` sorts the list
> > `letters` in-place and does not return anything.
> {: .solution}
{: .challenge}
 -->

> ## Ordenar e Ordenada
>
> O que esses dos programas imprimem?
> Em termos simples, explique a diferença entre `sorted(letras)` e `letras.sort()`.
>
> ~~~
> # Programa A
> letras = list('ouro')
> resultado = sorted(letras)
> print('letras é', letras, 'e resultado é', resultado)
> ~~~
> {: .language-python}
>
> ~~~
> # Programa B
> letras = list('ouro')
> resultado = letras.sort()
> print('letras é', letras, 'e resultado é', resultado)
> ~~~
> {: .language-python}
>
> > ## Solução
> > Programa A imprime
> > ~~~
> > letras é ['o', 'u', 'r', 'o'] e resultado é ['o', 'o', 'r', 'u']
> > ~~~
> > {: .output}
> > Programa B imprime
> > ~~~
> > letras é ['o', 'o', 'r', 'u'] e resultado é None
> > ~~~
> > {: .output}
> > `sorted(letras)` retorna uma cópia ordenada da lista `letras` (a lista original
> > `letras` permanece inalterada), enquanto `letras.sort()` ordena a lista
> > `letras` *in-place* e retorna None.
> {: .solution}
{: .challenge}
<!-- 
> ## Copying (or Not)
>
> What do these two programs print?
> In simple terms, explain the difference between `new = old` and `new = old[:]`.
>
> ~~~
> # Program A
> old = list('gold')
> new = old      # simple assignment
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .language-python}
>
> ~~~
> # Program B
> old = list('gold')
> new = old[:]   # assigning a slice
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .language-python}
>
> > ## Solução
> > Program A prints
> > ~~~
> > new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
> > ~~~
> > {: .output}
> > Program B prints
> > ~~~
> > new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
> > ~~~
> > {: .output}
> > `new = old` makes `new` a reference to the list `old`; `new` and `old` point
> > towards the same object.
> > 
> > `new = old[:]` however creates a new list object `new` containing all elements
> > from the list `old`; `new` and `old` are different objects.
> {: .solution}
{: .challenge}
 -->

> ## Copiando (ou Não)
>
> O que esses dois programas imprimem?
> Em termos simples, explique a diferença entre `novo = velho` e `novo = velho[:]`.
>
> ~~~
> # Program A
> velho = list('ouro')
> novo = velho      # simple assignment
> novo[0] = 'D'
> print('novo é', novo, 'e velho é', velho)
> ~~~
> {: .language-python}
>
> ~~~
> # Program B
> velho = list('ouro')
> novo = velho[:]   # assigning a slice
> novo[0] = 'D'
> print('novo é', novo, 'e velho é', velho)
> ~~~
> {: .language-python}
>
> > ## Solução
> > Program A imprime
> > ~~~
> > novo é ['D', 'u', 'r', 'o'] e velho é ['D', 'u', 'r', 'o']
> > ~~~
> > {: .output}
> > Program B imprime
> > ~~~
> > novo é ['D', 'u', 'r', 'o'] e velho é ['o', 'u', 'r', 'o']
> > ~~~
> > {: .output}
> > `novo = velho` torna `novo` uma referência à lista `velho`; `novo` e `velho` apontam
> > para o mesmo objeto
> > 
> > `novo = velho[:]` no entanto cria um novo objeto `novo` contendo todos os elementos
> > da lista `velho`; `novo` e `velho` são objetos diferentes.
> {: .solution}
{: .challenge}
