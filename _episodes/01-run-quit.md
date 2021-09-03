---
title: "Introdução ao JupyterLab"
teaching: 15
exercises: 0
questions:
- "Como eu posso rodar programas Python?"
objectives:
- "Ativar o servidor do JupyterLab." 
- "Criar um novo script Python."  
- "Criar um Jupyter notebook."
- "Desligar o servidor JupyterLab."
- "Entender a diferença entre um script Python e um Jupyter notebook."
- "Criar células Markdown em um notebook."
- "Criar e executar células Python em um notebook."
keypoints:
- "Scripts Python são arquivos de texto plano."
- "Usar o Jupyter Notebook para escrever e executar código Python."
- "O Notebook tem modos de comando e edição."
- "Use o teclado e o mouse para selecionar e editar células."
- "O Notebook vai formatar o Markdown para deixar tudo bonito."
- "Markdown faz quase tudo que HTML faz."
---

<!-- Many software developers will often use an integrated development environment (IDE) or a 
text editor to create and edit their Python programs which can be executed through the IDE or command line directly. While this is a common approach, we are going to use the [Jupyter Notebook][jupyter] via [JupyterLab][jupyterlab] for the remainder of this workshop. -->

<!-- This has several advantages:
  *   You can easily type, edit, and copy and paste blocks of code.
  *   Tab complete allows you to easily access the names of things you are using
      and learn more about them.
  *   It allows you to annotate your code with links, different sized text, bullets, etc.
      to make it more accessible to you and your collaborators.
  *   It allows you to display figures next to the code that produces them
      to tell a complete story of the analysis. -->

Existem várias vantagens de se usar o Jupyter:
  * Você pode facilmente digitar, editar, ou copiar e colar blocos de código.
  * Compleção com <kbd>TAB</kbd> permite que você facilmente acesse o nome de coisas
  que você está usando.
  * Você pode anotar seu código com links, textos de diferentes formatos, *bullet points*, etc.
  * Você pode exibir figuras do lado do código que as produz e contar uma história completa da análise.

<!-- Each notebook contains one or more cells that contain code, text, or images. -->
Cada notebook contém uma ou mais células que contém códigos, texto, ou imagens.

## Introdução ao JupyterLab

<!-- JupyterLab is an application with a web-based user interface from [Project Jupyter][jupyter] that 
enables one to work with documents and activities such as Jupyter notebooks, text editors, terminals,
and even custom components in a flexible, integrated, and extensible manner. JupyterLab requires a
reasonably up-to-date browser (ideally a current version of Chrome, Safari, or Firefox); Internet
Explorer versions 9 and below are *not* supported. -->

JupyterLab é uma aplicação web do [Projeto Jupyter][jupyter] que permite trabalhar com documentos e atividades
como Jupyter Notebooks, editores de texto, terminais, e até componentes personalizados de uma forma flexível e integrada. O JupyterLab requer um navegador atualizado (idealmente uma versão do Chrome, Safari, ou Firefox); Internet Explorer da versão 9 e anteriores *não* são suportados.

<!-- JupyterLab is included as part of the Anaconda Python distribution. If you have not already
installed the Anaconda Python distribution, see [the setup instructions]({{ page.root }}{% link
setup.md %})
for installation instructions. -->

O JupyterLab é incluído na distribuição Anaconda do Python.

<!-- Even though JupyterLab is a web-based application, JupyterLab runs locally on your machine and 
does not require an internet connection.
*   The JupyterLab server sends messages to your web browser.
*   The JupyterLab server does the work and the web browser renders the result.
*   You will type code into the browser and see the result when the web page talks to the 
    JupyterLab server. -->

Apesar do JupyterLab ser uma aplicação web, ele roda localmente em sua máquina e não requer uma conexão a internet.
*   O servidor JupyterLab manda mensagens para o seu navegador.
*   O servidor JupyterLab faz o trabalho e o navegador renderiza o resultado.
*   Você vai codar no navegador e ver o resultado quando a página web se comunicar com o servidor JupyterLab.

<!-- > ## JupyterLab? What about Jupyter notebooks?
> 
> JupyterLab is the [next stage in the evolution of the Jupyter Notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#overview).
> If you have prior experience working with Jupyter notebooks, then you will have a a good idea of what to expect from JupyterLab. 
> 
> Experienced users of Jupyter notebooks interested in a more detailed discussion of the similarities and differences
> between the JupyterLab and Jupyter notebook user interfaces can find more information in the 
> [JupyterLab user interface documentation][jupyterlab-ui].
{: .callout} -->

> ## JupyterLab? E Jupyter Notebooks?
> 
> JupyterLab é [o próximo estágio na evolução do Jupyter notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#overview).
> Se você tem experiência prévia com notebooks Jupyter, então você vai ter uma boa ideia do que esperar do JupyterLab.
{: .callout}

<!-- 
## Starting JupyterLab

You can start the JupyterLab server through the command line or through an application called 
`Anaconda Navigator`. Anaconda Navigator is included as part of the Anaconda Python distribution.
 -->

## Iniciando o JupyterLab

Você pode iniciar o servidor JupyterLab através da linha de comando ou através de uma aplicação chamada
`Anaconda Navigator`. O Anaconda Navigator é incluído na distribuição Anaconda do Python.

<!-- 
### macOS - Command Line
To start the JupyterLab server you will need to access the command line through the Terminal. 
There are two ways to open Terminal on Mac.

1. In your Applications folder, open Utilities and double-click on Terminal
2. Press <kbd>Command</kbd> + <kbd>spacebar</kbd> to launch Spotlight. Type `Terminal` and then 
double-click the search result or hit <kbd>Enter</kbd>

After you have launched Terminal, type the command to launch the JupyterLab server.

~~~
$ jupyter lab
~~~
{: .bash}
 -->
<!-- 
### Windows Users - Command Line
To start the JupyterLab server you will need to access the Anaconda Prompt.

Press <kbd>Windows Logo Key</kbd> and search for `Anaconda Prompt`, click the result or press enter.

After you have launched the Anaconda Prompt, type the command:

~~~
$ jupyter lab
~~~
{: .bash}
 -->

### Windows - Linha de Comando
Para ativar o servidor JupyterLab você vai precisar acessar o Anaconda Prompt.

Aperte <kbd>Windows-Key</kbd> e pesquisa por `Anaconda Prompt`, clique no resultado e aperte Enter. 

Depois de ter acessado o Anaconda Prompt, digite o seguinte comando:

~~~
$ jupyter lab
~~~
{: .bash}

###  Anaconda Navigator

<!-- To start a JupyterLab server from Anaconda Navigator you must first [start Anaconda Navigator (click for detailed instructions on macOS, Windows, and Linux)](https://docs.anaconda.com/anaconda/navigator/getting-started/#starting-navigator). You can search for Anaconda Navigator via Spotlight on macOS (<kbd>Command</kbd> + <kbd>spacebar</kbd>), the Windows search function (<kbd>Windows Logo Key</kbd>) or opening a terminal shell and executing the `anaconda-navigator` executable from the command line.

After you have launched Anaconda Navigator, click the `Launch` button under JupyterLab. You may need
to scroll down to find it.

Here is a screenshot of an Anaconda Navigator page similar to the one that should open on either macOS
or Windows. -->

Para ativar o servidor Jupyter do Anaconda Navigator, primeiro, [abra o Anaconda Navigator (clique para instruções detalhadas)](https://docs.anaconda.com/anaconda/navigator/getting-started/#starting-navigator). Você pode pesquisar pelo Anaconda Navigator pela função pesquisar do Windows (<kbd>Windows-Key</kbd>) ou pelo Spotlight do MacOS. Depois de ter ativado o Anaconda Navigator, procure pelo JupyterLab e clique em `Launch`.

<p align='center'>
  <img alt="Anaconda Navigator landing page" src="../fig/0_anaconda_navigator_landing_page.png" width="750"/>
</p>

Uma tab assim deve abrir no seu navegador: 

<p align='center'>
  <img alt="JupyterLab landing page" src="../fig/0_jupyterlab_landing_page.png" width="750"/>
</p>

## A interface JupyterLab
<!-- 
JupyterLab has many features found in traditional integrated development environments (IDEs) but 
is focused on providing flexible building blocks for interactive, exploratory computing.

The [JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) 
consists of the Menu Bar, a collapsable Left Side Bar, and the Main Work Area which contains tabs 
of documents and activities.
 -->

A [interface JupyterLab](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) 
consiste de uma barra de menu, uma barra lateral colapsável, e a área de trabalho principal que contém documentos e atividades.

### Barra de Menu
<!-- 
The Menu Bar at the top of JupyterLab has the top-level menus that expose various actions 
available in JupyterLab along with their keyboard shortcuts (where applicable). The following 
menus are included by default.
-->

A Barra de Menu no topo do JupyterLab tem os menus top-level que expõe as diferentes ações disponíveis no JupyterLab junto dos seus atalhos no teclado. Os seguintes menus são incluídos por padrão.

<!--
*   **File:** Actions related to files and directories such as *New*, *Open*, *Close*, *Save*, etc. The *File* menu also includes the *Shut Down* action used to shutdown the JupyterLab server.
*   **Edit:** Actions related to editing documents and other activities such as *Undo*, *Cut*, *Copy*, *Paste*, etc.
*   **View:** Actions that alter the appearance of JupyterLab.
*   **Run:** Actions for running code in different activities such as notebooks and code consoles (discussed below).
*   **Kernel:** Actions for managing kernels. Kernels in Jupyter will be explained in more detail below.
*   **Tabs:** A list of the open documents and activities in the main work area.
*   **Settings:** Common JupyterLab settings can be configured using this menu. There is also an *Advanced Settings Editor* option in the dropdown menu that provides more fine-grained control of JupyterLab settings and configuration options.
*   **Help:** A list of JupyterLab and kernel help links.
 -->


*   **File:** Ações relacionadas a arquivos como *New*, *Open*, *Close*, *Save*, etc. O menu *File* também inclui a ação *Shut Down* que é usada para desativar o servidor JupyterLab.
*   **Edit:** Ações relacionadas a editar documentos, tais como *Undo*, *Cut*, *Copy*, *Paste*, etc.
*   **View:** Ações que alteram a aparência do JupyterLab.
*   **Run:** Ações para executar código em diferentes atividades como notebooks e consoles de código (discutidos abaixo).
*   **Kernel:** Ações para gerenciar kernels. Kernels no Jupyter serão explicados com mais detalhes abaixo.
*   **Tabs:** Uma lista de documentos e atividades abertos na área principal.
*   **Settings:** Configurações comuns do Jupyter podem ser modificadas nesse menu. Ele também contém a opção *Advanced Settings Editor* no menu dropdown que provê um controle mais fino das opções do JupyterLab.
*   **Help:** Uma lista de links de ajuda para o JupyterLab e o kernel.

> ## Kernels
> A [documentação do JupyterLab](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html) 
> define kernels como "processos separados iniciados pelo servidor que roda o seu código em diferentes linguagens de programação e ambientes."
> Quando abrimos um Jupyter Notebook, abrimos um kernel - um processo - que vai rodar o código.
> Nessa aula, vamos usar o kernel IPython do Jupyter, que permite rodar código Python 3 interativamente.
> 
> Usar outros [kernels Jupyter para outras linguagens de programação](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) nos permitiria
> escrever e executar código de outras linguagens de programação na mesma interface do JupyterLab, como R, Java, Julia, Ruby, JavaScript, Fortran, etc.
{: .callout}

Abaixo um screenshot da Barra de Menu:

<p align='center'>
    <img alt="JupyterLab Menu Bar" src="../fig/0_jupyterlab_menu_bar.png" width="750"/>
</p>

### Barra Lateral
<!-- 
The left sidebar contains a number of commonly used tabs, such as a file browser (showing the 
contents of the directory where the JupyterLab server was launched), a list of running kernels 
and terminals, the command palette, and a list of open tabs in the main work area. A screenshot of 
the default Left Side Bar is provided below.
 -->

A barra lateral que fica à esquerda contém um número de abas comumente usadas, como um navegador de arquivos (que mostra o conteúdo do diretório aonde o servidor JupyterLab foi iniciado), uma lista dos kernels e terminais em execução, a paleta de comandos, e uma lista de abas abertas na área de trabalho principal. 

<p align='center'>
    <img alt="JupyterLab Left Side Bar" src="../fig/0_jupyterlab_left_side_bar.png" width="250"/>
</p>
<!-- 
The left sidebar can be collapsed or expanded by selecting “Show Left Sidebar” in the View menu or 
by clicking on the active sidebar tab.
 -->

A barra lateral pode ser colapsada ou expandida selecionando "Show Left Sidebar" no Menu *View* ou clicando na aba ativa da barra lateral.

### Área de Trabalho Principal
<!-- 
The main work area in JupyterLab enables you to arrange documents (notebooks, text files, etc.) 
and other activities (terminals, code consoles, etc.) into panels of tabs that can be resized or 
subdivided. A screenshot of the default Menu Bar is provided below.
 -->

A área de trabalho principal do JupyterLab permite que você arranje documentos (notebooks, arquivos de texto, etc.) e outras atividades (terminais, consoles de código, etc.) em paineis de abas que podem ter o tamanho ajustado ou ser subdivididas. Abaixo um screenshot da barra de menu.

<p align='center'>
    <img alt="JupyterLab Main Work Area" src="../fig/0_jupyterlab_main_work_area.png" width="750"/>
</p>
<!-- 
Drag a tab to the center of a tab panel to move the tab to the panel. Subdivide a tab panel by 
dragging a tab to the left, right, top, or bottom of the panel. The work area has a single current 
activity. The tab for the current activity is marked with a colored top border (blue by default).
 -->

Arraste um tab do centro do painel de abas para mover a aba para o painel. Subdivida um painel de abas arrastando a aba para a esquerda, direita, topo, ou base do painel. A área de trabalho tem uma única atividade no momento. A aba para a atividade corrente é marcada como uma borda colorida no topo (azul por padrão).

## Criando um script Python
<!-- 
*   To start writing a new Python program click the Text File icon under the *Other* header in the Launcher tab of the Main Work Area.
    *   You can also create a new plain text file by selecting the *New -> Text File* from the *File* menu in the Menu Bar.
*   To convert this plain text file to a Python program, select the *Save File As* action from the *File* menu in the Menu Bar and give your new text file a name that ends with the `.py` extension.
    *   The `.py` extension lets everyone (including the operating system) know that this text file is a Python program.
    *   This is convention, not a requirement.
 -->
* Para começar a escrever um novo programa Python, clique no ícone de Arquivo de Texto embaixo do cabeçalho *Other* na aba **Launcher** da área de trabalho principal.
  * Você também pode criar um novo arquivo de texto plano ao selecionar *New -> Text File* do menu *File* na Barra de Menu.
* Para converter esse arquivo de texto plano em um programa Pytohn, selecione a ação *Salvar Arquivo Como* do menu *File* na Barra de Menu e dê ao seu novo arquivo de texto um nome que termine com a extensão `.py`.
  * A extensão `.py` permite que todos (incluindo o sistema operacional) saibam que esse arquivo de texto é um programa Python.
  * Isso é uma convenção, e não um requerimento.

## Criando um Notebook Jupyter
<!-- 
To open a new notebook click the Python 3 icon under the *Notebook* header in the Launcher tab in 
the main work area. You can also create a new notebook by selecting *New -> Notebook* from the *File* menu in the Menu Bar.

Additional notes on Jupyter notebooks.

  *   Notebook files have the extension `.ipynb` to distinguish them from plain-text Python programs.
  *   Notebooks can be exported as Python scripts that can be run from the command line.
Below is a screenshot of a Jupyter notebook running inside JupyterLab. If you are interested in 
more details, then see the [official notebook documentation][jupyterlab-notebook-docs].
 -->

Para criar um novo notebook, clique no ícone do Python 3 embaixo do cabeçalho *Notebook* na aba **Launcher** na área de trabalho principal. Você também pode criar um novo notebook ao selecionar *New -> Notebook* do menu *File* na Barra de Menu.

Notas adicionais sobre notebooks Jupyter:

  *   Arquivos de Notebook tem a extensão `.ipynb` para que os distingue de programas de Python em texto plano.
  *   Notebooks podem ser exportados como scripts Python que podem ser executados da linha de comando.

Abaixo está um screenshot de um Jupyter Notebook rodando dentro do JupyterLab. Se você está interessado em mais detalhes, veja a [documentação oficial dos notebooks][jupyterlab-notebook-docs]

<p align='center'>
    <img alt="Example Jupyter Notebook" src="../fig/0_jupyterlab_notebook_screenshot.png" width="750"/>
</p>

> ## Como É Armazenado
<!-- >
> *   The notebook file is stored in a format called JSON.
> *   Just like a webpage, what's saved looks different from what you see in your browser.
> *   But this format allows Jupyter to mix source code, text, and images, all in one file.
{: .callout} -->
>
> *   O arquivo do notebook é armazenado em um formato chamado JSON.
> *   Assim como a página web, o que é salvo é diferente do que vemos no navegador.
> *   Esse formato permite que o Jupyter possa misturar código, texto, e imagens, tudo em um único arquivo.
{: .callout}

> ## Arranjando Documentos em Paineis de Abas
>
<!-- > In the JupyterLab Main Work Area you can arrange documents into panels of tabs. Here is an 
> example from the [official documentation][jupyterlab].
> 
> <p align='center'>
>    <img alt="Multi-panel JupyterLab" src="../fig/0_multipanel_jupyterlab_screenshot.png" width="750"/>
> </p>
>
> First, create a text file, Python console, and terminal window and arrange them into three 
> panels in the main work area. Next, create a notebook, terminal window, and text file and 
> arrange them into three panels in the main work area. Finally, create your own combination of 
> panels and tabs. What combination of panels and tabs do you think will be most useful for your 
> workflow? -->
> Na área de trabalho principal do JupyterLab você pode arranjar documentos em paineis de abas. Aqui está um
> exemplo da [documentação oficial][jupyterlab].
> 
> <p align='center'>
>    <img alt="Multi-panel JupyterLab" src="../fig/0_multipanel_jupyterlab_screenshot.png" width="750"/>
> </p>
>
> Primeiro, crie um arquivo de texto, console Python, e janela do terminal e os arranje em três
> paineis diferentes na área de trabalho principal. Em seguida, crie um notebook, uma janela do terminal, e um arquivo de texto e
> os arranje em três painéis na área de trabalho principal. Por último, crie sua própria combinação de 
> paineis e abas. Que combinação de paineis e abas você acha que será a mais útil para o seu
> workflow?
>
> > ## Solução
> >
<!-- > > After creating the necessary tabs, you can drag one of the tabs to the center of a panel to 
> > move the tab to the panel; next you can subdivide a tab panel by dragging a tab to the left, 
> > right, top, or bottom of the panel. -->
> > Depois de criar as abas necessárias, você pode arrastar uma delas no centro de um painel para
> > mover a aba para o painel; em seguida você pode subdividir um painel de abas ao arrastar a aba para a esquerda,
> > direita, topo, ou base do painel.
> {: .solution}
{: .challenge}

> ## Código vs. Texto
>
<!--
> Jupyter mixes code and text in different types of blocks, called cells. We often use the term
> "code" to mean "the source code of software written in a language such as Python".
> A "code cell" in a Notebook is a cell that contains software;
> a "text cell" is one that contains ordinary prose written for human beings.
> -->
> O Jupyter mistura código e texto em diferentes tipos de blocos, chamados células. Nós frequentemente usamos 
> o termo "código" para se referir ao "código fonte do software escrito em uma linguagem como Python".
> Uma "célula de código" em um notebook é uma célula que contém software;
> a "célula de texto" é uma que contém prosa escrita para seres humanos.
{: .callout}

## Modos de Comando e de Edição

<!-- *   If you press <kbd>Esc</kbd> and <kbd>Return</kbd> alternately, the outer border of your code cell will change from gray to blue.
*   These are the **Command** (gray) and **Edit** (blue) modes of your notebook.
*   Command mode allows you to edit notebook-level features, and Edit mode changes the content of cells.
*   When in Command mode (esc/gray),
    *   The <kbd>b</kbd> key will make a new cell below the currently selected cell.
    *   The <kbd>a</kbd> key will make one above.
    *   The <kbd>x</kbd> key will delete the current cell.
    *   The <kbd>z</kbd> key will undo your last cell operation (which could be a deletion, creation, etc).
*   All actions can be done using the menus, but there are lots of keyboard shortcuts to speed things up.
 -->
*   Se você apertar <kbd>Esc</kbd> e <kbd>Enter</kbd> alternadamente, a borda exterior da sua célula de código vai mudar de cinza para azul.
*   Esses são os modos de **Comando** (cinza) e **Edição** (azul) do seu notebook.
*   O modo de comando permite que você editar features a nível de notebook, e o modo edição muda o conteúdo das células.
*   Quando no modo de Comando (Esc/Cinza),
    *   A tecla <kbd>b</kbd> vai criar uma nova célula abaixo da célula atual.
    *   A tecla <kbd>a</kbd> vai criar uma acima.
    *   A tecla <kbd>x</kbd> vai deletar a célula atual.
    *   A tecla <kbd>z</kbd> vai desfazer a sua última operação (que pode ser uma deleção, criação, etc.).
* Todas as ações podem ser feitas usando os menus, mas existem vários atalhos no teclado que podem acelerar.

> ## Comando vs. Edição
<!-- >
> In the Jupyter notebook page are you currently in Command or Edit mode?  
> Switch between the modes. 
> Use the shortcuts to generate a new cell. 
> Use the shortcuts to delete a cell.
> Use the shortcuts to undo the last cell operation you performed.
> -->
>
> O Jupyter Notebook atual você está no modo Comando ou Edição?
> Troque entre os modos.
> Use os atalhos para criar uma nova célula.
> Use os atalhos para deletar uma célula.
> Use os atalhos para desfazer a última operação que você fez.
>
> > ## Solução
<!-- > >
> > Command mode has a grey border and Edit mode has a blue border. 
> > Use <kbd>Esc</kbd> and <kbd>Return</kbd> to switch between modes. 
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>b</kbd> or <kbd>a</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>x</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>z</kbd>.
> >  -->
> >
> > O modo de Comando tem uma borda cinza e o de Edição tem uma borda azul.
> > Use <kbd>Esc</kbd> e <kbd>Enter</kbd> para alternar entre os modos. 
> > Você precisa estar no modo de Comando (Aperte <kbd>Esc</kbd> se a sua célula estiver azul).  Aperte <kbd>b</kbd> ou <kbd>a</kbd>.
> > Você precisa estar no modo de Comando (Aperte <kbd>Esc</kbd> se a sua célula estiver azul).  Aperte <kbd>x</kbd>.
> > Você precisa estar no modo de Comando (Aperte <kbd>Esc</kbd> se a sua célula estiver azul).  Aperte <kbd>z</kbd>.
> {: .solution}
{: .challenge}

### Use o teclado e o mouse para alternar entre as células.
<!-- 
*   Pressing the <kbd>Return</kbd> key turns the border blue and engages Edit mode, which allows 
    you to type within the cell.
*   Because we want to be able to write many lines of code in a single cell,
    pressing the <kbd>Return</kbd> key when in Edit mode (blue) moves the cursor to the next line 
    in the cell just like in a text editor.
*   We need some other way to tell the Notebook we want to run what's in the cell.
*   Pressing <kbd>Shift</kbd>+<kbd>Return</kbd> together will execute the contents of the cell.
*   Notice that the <kbd>Return</kbd> and <kbd>Shift</kbd> keys on the right of the keyboard are 
    right next to each other.
 -->
*   Apertar o <kbd>Enter</kbd> transforma a borda azul e ativa o modo de Edição, que permite que
    você digite dentro da célula.
*   Por que queremos ser capazes de escrever muitas linhsa de código em uma única célula,
    apertar o <kbd>Enter</kbd> quando no modo de Edição (azul) move o cursor para a próxima linha
    da célula assim como qualquer outro editor de texto.
*   Precisamos de alguma outra forma de dizer para o Notebook que queremos executar o que está dentro da célula.
*   Apertar <kbd>Shift</kbd>+<kbd>Enter</kbd> juntos vai executar o conteúdo da célula.

### O Notebook vai formatar o Markdown para deixar tudo bonito
<!-- 
*   Notebooks can also render [Markdown][markdown].
    *   A simple plain-text format for writing lists, links, 
        and other things that might go into a web page.
    *   Equivalently, a subset of HTML that looks like what you'd send in an old-fashioned email.
*   Turn the current cell into a Markdown cell by entering the Command mode (<kbd>Esc</kbd>/gray) 
    and press the <kbd>M</kbd> key.
*   `In [ ]:` will disappear to show it is no longer a code cell and you will be able to write in 
    Markdown.
*   Turn the current cell into a Code cell by entering the Command mode (<kbd>Esc</kbd>/gray) and 
    press the <kbd>y</kbd> key.
 -->

*   Notebooks também podem renderizar [Markdown][markdown].
    *   Um formato simples de texto plano para escrever listas, links,
        e outras coisas que poderiam estar em uma página web.
    *   De forma equivalente, é um subset de HTML que parece que você está enviando um email "das antigas".
*   Transforme a célula atual em Markdown ao entrar no modo de Comando (<kbd>Esc</kbd>)
    e aperte a tecla <kbd>M</kbd> (de Markdown).
*   `In [ ]:` vai disparecer para mostrar que não é mais uma célula de código.
*   Transforme a célula atual em Código ao entrar no modo de Comando (<kbd>Esc</kbd>)
    e aperte a tecla <kbd>Y</kbd>.

### Markdown faz quase tudo que HTML faz

<div class="row">
  <div class="col-md-6" markdown="1">

~~~
*   Use asteriscos
*   para criar
*   listas bullet.
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
*   Use asteriscos
*   para criar
*   listas bullet.

  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
1.  Use números
1.  para criar
1.  listas numeradas.
~~~

  </div>
  <div class="col-md-6" markdown="1">

1.  Use números
1.  para criar
1.  listas numeradas.

  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
*  Você aninhar itens
	*  Para criar sublistas 
	*  de mesmo tipo
*  Ou sublistas
	1. De tipos
	1. diferentes
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
*  Você aninhar itens
	*  Para criar sublistas 
	*  de mesmo tipo
*  Ou sublistas
	1. De tipos
	1. diferentes
  
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
# Cabeçalho Nível 1
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
# Cabeçalho Nível 1

  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
## Cabeçalho Nível 2 (etc.)
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
## Cabeçalho Nível 2 (etc.)

  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
Novas linhas
não importam.

Mas linhas em branco
criam novos parágrafos.
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
Novas linhas
não importam.

Mas linhas em branco
criam novos parágrafos.

  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
    
~~~
[Crie links](https://thexlab.com.br/) com `[...](...)`.
Ou use [links com nome][XLab].

[XLab]: https://thexlab.com.br/
~~~

  </div>
  <div class="col-md-6" markdown="1">
  
[Crie links](https://thexlab.com.br/) com `[...](...)`.
Ou use [links com nome][XLab].

[XLab]: https://thexlab.com.br/

  </div>
</div>

> ## Crie listas em Markdown
<!-- >
> Create a nested list in a Markdown cell in a notebook that looks like this:
>
> 1.  Get funding.
> 2.  Do work.
>     *   Design experiment.
>     *   Collect data.
>     *   Analyze.
> 3.  Write up.
> 4.  Publish.
> -->
>
> Crie uma lista aninhada em uma célula de Markdown em um notebook que pareça com isso:
>
> 1.  Planejar projeto.
> 2.  Fazer o trabalho.
>     *   Coletar os dados.
>     *   Analisar.
>     *   Gerar figuras.
> 3.  Escrever relatório.
> 4.  Submeter.
> 
> > ## Solução
<!-- > >
> > This challenge integrates both the numbered list and bullet list. 
> > Note that the bullet list is indented 2 spaces so that it is inline with the items of the numbered list. -->
> >
> > Esse desafio integra uma lista numerada e uma lista bullet.
> > Note que a lista bullet é indentada com 2 espaços para que esteja alinhada com os itens da lista numerada.
> > ~~~
> > 1.  Planejar projeto.
> > 2.  Fazer o trabalho.
> >     *   Coletar os dados.
> >     *   Analisar.
> >     *   Gerar figuras.
> > 3.  Escrever relatório.
> > 4.  Submeter.
> > ~~~
> {: .solution}
{: .challenge}

> ## Mais Matemática
<!-- >
> What is displayed when a Python cell in a notebook
> that contains several calculations is executed?
> For example, what happens when this cell is executed?
> -->
>
> O que aparece quando uma célula Python de um notebook
> que contém várias operações é executada?
> Por exemplo, o que acontece quando essa célula é executada?
>
> ~~~
> 7 * 3
> 2 + 1
> ~~~
> {: .language-python}
> 
> > ## Solução
> >
> > O Python retorna a saída da última operação.
> > ~~~
> > 3
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Mude uma Célula Existente de Código para Markdown
<!-- >
> What happens if you write some Python in a code cell
> and then you switch it to a Markdown cell?
> For example,
> put the following in a code cell:
> -->
>
> O que acontece se você escreve um pouco de Python em uma célula de código
> e depois você troca para uma célula Markdown?
> Por exemplo,
> coloque o seguinte em uma célula de código:
>
> ~~~
> x = 6 * 7 + 12
> print(x)
> ~~~
> {: .language-python}
<!-- >
> And then run it with <kbd>Shift</kbd>+<kbd>Return</kbd> to be sure that it works as a code cell.
> Now go back to the cell and use <kbd>Esc</kbd> then <kbd>m</kbd> to switch the cell to Markdown
> and "run" it with <kbd>Shift</kbd>+<kbd>Return</kbd>.
> What happened and how might this be useful?
>  -->
>
> Execute com <kbd>Shift</kbd>+<kbd>Enter</kbd> para ter certeza que funciona como uma célula de código.
> Agora volte para célula e use <kbd>Esc</kbd> depois <kbd>M</kbd> para mudar a célula para Markdown
> e "execute" como <kbd>Shift</kbd>+<kbd>Enter</kbd>.
> O que aconteceu e como isso pode ser útil?
> 
> > ## Solução
<!-- > >
> > The Python code gets treated like Markdown text.
> > The lines appear as if they are part of one contiguous paragraph.
> > This could be useful to temporarily turn on and off cells in notebooks that get used for multiple purposes. 
> > -->
> > O código Python é tratado como texto Markdown.
> > As linhas aparecem como se fossem parte de um parágrafo contíguo.
> > Isso pode ser útil para temporariamente ligar e desligar células em notebooks que são usados para múltiplos propósitos.
> > ~~~
> > x = 6 * 7 + 12 print(x)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Equações
<!-- >
> Standard Markdown (such as we're using for these notes) won't render equations,
> but the Notebook will.
> Create a new Markdown cell
> and enter the following:
> -->
>
> Markdown Standard (como o que estamos usando para as notas) não vão renderizar equações,
> mas o Notebook vai.
> Cria uma nova célula Markdown
> e escreva o seguinte:
>
> ~~~
> $\sum_{i=1}^{N} 2^{-i} \approx 1$
> ~~~
<!-- >
> (It's probably easier to copy and paste.)
> What does it display?
> What do you think the underscore, `_`, circumflex, `^`, and dollar sign, `$`, do?
> -->
>
> (Talvez seja mais fácil copiar e colar.)
> O que isso mostra?
> O que você acha que o underline, `_`, acento circumflexo, `^`, e cifrão, `$`, fazem?
> 
> > ## Solução
<!-- > >
> > The notebook shows the equation as it would be rendered from LaTeX equation syntax.
> > The dollar sign, `$`, is used to tell Markdown that the text in between is a LaTeX equation.
> > If you're not familiar with LaTeX,  underscore, `_`, is used for subscripts and circumflex, `^`, is used for superscripts.
> > A pair of curly braces, `{` and `}`, is used to group text together so that the statement `i=1` becomes the subscript and `N` becomes the superscript.
> > Similarly, `-i` is in curly braces to make the whole statement the superscript for `2`.
> > `\sum` and `\approx` are LaTeX commands for "sum over" and "approximate" symbols. -->
> >
> > O Notebook mostra a equação como ela seria renderizada na sintaxe de LaTeX.
> > O cifrão, `$`, é usado para dizer ao Markdown que o texto ali dentro é uma equação LaTeX.
> > No LaTeX, o underline, `_`, é usado para *subscript* e o circumflexo, `^`, é usado para *superscript*.
> > Um par de chaves, `{` e `}`, é usado para agrupar texto para que a declaração `i=1` se torne subscript e `N` se torne superscript.
> > Similarmente, `-i` dentro de chaves é utilizado para fazer a declaração toda um superscript para `2`.
> > `\sum` e `\approx` são comandos LaTeX para os símbolos de "somatório" e "aproximadamente". 
> {: .solution}
{: .challenge}

## Fechando o JupyterLab
<!-- 
*   From the Menu Bar select the "File" menu and then choose "Shut Down" at the bottom of the dropdown menu. You will be prompted to confirm that you wish to shutdown the JupyterLab server (don't forget to save your work!). Click "Shut Down" to shutdown the JupyterLab server.
*   To restart the JupyterLab server you will need to re-run the following command from a shell.
 -->
*   Da Barra de Menu, selecione o menu `File` e escolha `Shut Down` na base do menu dropdown. Você vai ter que confirmar que quer fechar o servidor JupyterLab (não esqueça de salvar seu trabalho!). Clique em "Shut Down" para fechar o servidor.
*   Para reiniciar o servidor JupyterLab você vai precisar re-executar o seguinte comando de um terminal (como o Anaconda Prompt) ou usar o Anaconda Navigator.

~~~
$ jupyter lab
~~~

> ## Fechando o JupyterLab
>
> Pratique fechar e reiniciar o JupyterLab.
{: .challenge}
[anaconda]: https://docs.continuum.io/anaconda/install
[jupyterlab-ui]: https://jupyterlab.readthedocs.io/en/stable/user/interface.html
[jupyterlab-notebook-docs]: https://jupyterlab.readthedocs.io/en/stable/user/notebook.html
[markdown]: https://en.wikipedia.org/wiki/Markdown
[newwinlogo]: http://i.stack.imgur.com/B8Zit.png

{% include links.md %}
