---
title: "Escopo de Variáveis"
teaching: 10
exercises: 10
questions:
- "Como chamadas de função realmente funcionam?"
- "Como posso determinar onde erros ocorreram?"
objectives:
- "Identificar variáveis locais e globais."
- "Identificar parâmetros como variáveis locais."
- "Leia um *traceback* e determine o arquivo, função e número da linha no qual o erro ocorreu, o tipo de erro, e a mensagem de erro."
keypoints:
- "O escopo de uma variável é a parte do programa que pode 'ver' essa variável."
---
<!-- 
## The scope of a variable is the part of a program that can 'see' that variable.

*   There are only so many sensible names for variables.
*   People using functions shouldn't have to worry about
    what variable names the author of the function used.
*   People writing functions shouldn't have to worry about
    what variable names the function's caller uses.
*   The part of a program in which a variable is visible is called its *scope*.
 -->

## O escopo de uma variável é a parte do programa que pode 'ver' essa variável.

*   Só existem tantos nomes sensíveis para variáveis.
*   Quando estamos usando funções, não devemos ter que nos preocupar com
    os nomes das variáveis que quem escreveu a função escolheu.
*   Pessoas escrevendo funções não devem ter que se preocupar com
    que nomes de variáveis quem está chamando a função usa.
*   A parte de um programa na qual uma variável está visível é o seu **escopo**.

<!-- 
~~~
pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature
~~~
{: .language-python}
 -->

~~~
pressao = 103.9

def ajustar(t):
    temperatura = t * 1.43 / pressao
    return temperatura
~~~
{: .language-python}

<!-- 
*   `pressure` is a *global variable*.
    *   Defined outside any particular function.
    *   Visible everywhere.
*   `t` and `temperature` are *local variables* in `adjust`.
    *   Defined in the function.
    *   Not visible in the main program.
    *   Remember: a function parameter is a variable
        that is automatically assigned a value when the function is called.
 -->

*   `pressao` é uma *variável global*.
    *   Definida fora de uma função em particular.
    *   Visível em todos os lugares.
*   `t` e `temperatura` são *variáveis locais* em `ajustar`.
    *   Definidas nas função.
    *   Não visíveis no programa principal. 
    *   Lembre-se: um parâmetro de função é uma variável
        que é automaticamente assinalada a um valor quando a função é chamada.

<!-- 
~~~
print('adjusted:', adjust(0.9))
print('temperature after call:', temperature)
~~~
{: .language-python}
~~~
adjusted: 0.01238691049085659
~~~
{: .output}
~~~
Traceback (most recent call last):
  File "/Users/swcarpentry/foo.py", line 8, in <module>
    print('temperature after call:', temperature)
NameError: name 'temperature' is not defined
~~~
{: .error}
 -->

~~~
print('ajustada:', ajustar(0.9))
print('temperatura depois da chamada:', temperatura)
~~~
{: .language-python}
~~~
ajustada: 0.01238691049085659
~~~
{: .output}
~~~
Traceback (most recent call last):
  File "/Users/xlab/temp.py", line 8, in <module>
    print('temperatura depois da chamada:', temperatura)
NameError: name 'temperature' is not defined
~~~
{: .error}

<!-- 
> ## Local and Global Variable Use
>
> Trace the values of all variables in this program as it is executed.
> (Use '---' as the value of variables before and after they exist.)
>
> ~~~
> limit = 100
>
> def clip(value):
>     return min(max(0.0, value), limit)
>
> value = -22.5
> print(clip(value))
> ~~~
> {: .language-python}
{: .challenge}
 -->

> ## Uso Local e Global de Variáveis
>
> Trace os valores de todas as variáveis nesse programa conforme ele é executado.
> (Use '---' como o valor das variáveis antes e depois deles existirem.)
>
> ~~~
> limite = 100
>
> def limitar(valor):
>     return min(max(0.0, valor), limite)
>
> valor = -22.5
> print(limitar(valor))
> ~~~
> {: .language-python}
{: .challenge}

<!-- 
> ## Reading Error Messages
>
> Read the traceback below, and identify the following:
>
> 1. How many levels does the traceback have?
> 2. What is the file name where the error occurred?
> 3. What is the function name where the error occurred?
> 4. On which line number in this function did the error occur?
> 5. What is the type of error?
> 6. What is the error message?
>
> ~~~
> ---------------------------------------------------------------------------
> KeyError                                  Traceback (most recent call last)
> <ipython-input-2-e4c4cbafeeb5> in <module>()
>       1 import errors_02
> ---- 2 errors_02.print_friday_message()
>
> /Users/ghopper/thesis/code/errors_02.py in print_friday_message()
>      13
>      14 def print_friday_message():
> --- 15     print_message("Friday")
>
> /Users/ghopper/thesis/code/errors_02.py in print_message(day)
>       9         "sunday": "Aw, the weekend is almost over."
>      10     }
> --- 11     print(messages[day])
>      12
>      13
>
> KeyError: 'Friday'
> ~~~
> {: .error}
> > ## Solution
> > 1. Three levels.
> > 2. `errors_02.py`
> > 3. `print_message`
> > 4. Line 11
> > 5. `KeyError`. These errors occur when we are trying to look up a key that does not exist (usually in a data
> > structure such as a dictionary). We can find more information about the `KeyError` and other built-in exceptions
> > in the [Python docs](https://docs.python.org/3/library/exceptions.html#KeyError).
> > 6. `KeyError: 'Friday'`
> {: .solution}
{: .challenge}
 -->

> ## Lendo Mensagens de Erro
>
> Leia o erro abaixo, e identifique o seguinte:
>
> 1. Quantos níveis tem o traceback?
> 2. Qual é o nome do arquivo onde o erro ocorreu?
> 3. Qual é o nome da função onde o erro ocorreu?
> 4. Em que número de linha da função esse erro ocorreu?
> 5. Qual é o tipo de erro?
> 6. Qual é a mensagem de erro?
>
> ~~~
> ---------------------------------------------------------------------------
> KeyError                                  Traceback (most recent call last)
> <ipython-input-2-e4c4cbafeeb5> in <module>()
>       1 import erros_02
> ----> 2 erros_02.imprimir_mensagem_sexta()
>
> /Users/vini/xlab/cpfl/erros_02.py in imprimir_mensagem_sexta()
>      13
>      14 def imprimir_mensagem_sexta():
> ---> 15     imprimir_mensagem("Sexta")
>
> /Users/vini/xlab/cpfl/erros_02.py in imprimir_mensagem(dia)
>       9         "domingo": "A semana está quase acabando."
>      10     }
> ---> 11     print(messages[dia])
>      12
>      13
>
> KeyError: 'Sexta'
> ~~~
> {: .error}
> > ## Solução
> > 1. Três níveis.
> > 2. `erros_02.py`
> > 3. `imprimir_mensagem`
> > 4. Linha 11.
> > 5. `KeyError`. Esses erros ocorrem quando estamos tentando procurar uma chave que não existe (geralmente em uma estrutura
> > de dados como um dicionário). Podemos encontrar mais informações sobre o `KeyError` e outras exceções embutidas
> > na [documentação do Python](https://docs.python.org/pt-br/3/library/exceptions.html#KeyError).
> > 6. `KeyError: 'Sexta'`
> {: .solution}
{: .challenge}
