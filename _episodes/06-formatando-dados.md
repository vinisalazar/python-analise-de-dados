---
title: "Formatando Dados em Planilhas"
teaching: 15
exercises: 20
questions:
- "Como formatar dados em planilhas para uso efetivo dos dados?"
objectives:
- "Descrever as melhores práticas para entrada e formatação dos dados em planilhas."
- "Aplicar as melhores práticas para organizar variáveis e observações em uma planilha."
keypoints:
- "Nunca modifique seus dados brutos. Sempre faça uma cópia antes de fazer suas próprias modificações."
- "Mantenha um registro de todos os passos que você toma para limpar os seus dados em um arquivo de texto plano."
- "Organize seus dados conforme os princípios de '*tidy data*'."
---

Um erro comum é tratar programas de planilhas como cadernos, ou seja,
depender de contexto, notas na margem, e outras formas de representar informação.
Como humanos, nós (geralmente) conseguimos interpretar essas coisas, mas computadores não veem informações da mesma forma,
e a não ser que expliquemos para o computador o que cada coisa significa (e isso pode ser difícil!), ele não será capaz
de entender o que os dados significam.

Usando computadores, podemos gerenciar e analisar dados de formas muito mais rápidas e efetivas,
mas para usar esse poder, precisamos arrumar nossos dados de uma forma que o computador possa entendê-los
(e computadores são muito literais).

Por isso, é muito importante organizar e mantar tabelas bem formatadas
desde o início - antes de mesmo de começar a registrar ou gerar algum tipo de dado.
Organização de dados é a fundação de um projeto de análise. Pode ser o que torna sua
análise muito fácil ou muito difícil, então vale a pena pensar sobre como você vai fazer
a entrada e armazenamento dos dados. Você pode fazer o set up de suas planilhas de diferentes formas,
mas algumas dessas escolhas podem limitar sua habilidade de trabalhar com dados em outros programas
ou como você-do-futuro ou seu colaborador vai trabalhar com os dados.

> ## Formatos de arquivo
> Nota: the best layouts/formats (as well as software and
> interfaces) for data entry and data analysis might be
> different. It is important to take this into account, and ideally
> automate the conversion from one to another.
{: .callout}

### Mantendo um registro de suas análises

Quando estamos trabalhando com planilhas, é
muito fácil acabar com uma planilha que é totalmente diferente da que começamos.
Para que possamos reproduzir as análises ou recapitular o que fizemos quando
alguém pedir para mudar alguma coisa, devemos:

- criar um novo arquivo somente com os dados limpos e/ou analisados. 
Não modifique o dataset original, ou você nunca vai saber por onde começou!
- mantenha um registro de todos os passos que você usou para limpar ou analisar os dados.
Você deve registrar esses passos assim como qualquer outro protocolo da sua operação.
Uma sugestão é manter isso num arquivo de texto na mesma pasta que o arquivo com os dados.

Esse pode ser um exemplo de um registro dos passos usados para limpar os dados:

![spreadsheet setup](../fig/spreadsheet-setup-updated.png)

### Estruturando dados em planilhas

A regra cardinal para usar programas de planilhas é manter os dados "arrumadinhos", ou "*tidy*":

1. Coloque todas as suas variáveis em colunas. A coisa que você está medindo,
como 'peso' ou 'temperatura'.
2. Coloque cada observação em sua própria linha.
3. Não combine múltiplas informações em uma mesma célula.
4. Deixe os dados brutos como estão - não modifique-os!
5. Exporte os dados limpos em um formato de texto como CSV (valores separados por vírgula).
   Isso garante que qualquer usuário(a) ou programa consiga ver os dados com facilidade.

<!-- 
> ## Exercise
> 
> We're going to take a messy version of the survey data and describe how we would clean it up.
>
> 1. Download the data by clicking [here](https://ndownloader.figshare.com/files/2252083) to get it from FigShare.
> 2. Open up the data in a spreadsheet program. 
> 3. You can see that there are two tabs. Two field assistants conducted the surveys, one
in 2013 and one in 2014, and they both kept track of the data in their own way in tabs `2013` and `2014` of the dataset, 
>respectively. Now
you're the person in charge of this project and you want to be able to 
start analyzing the data.   
> 4. With the person next to you, identify what is wrong with this spreadsheet. Also discuss the steps you would need to take to clean up the `2013` and `2014` tabs, and to put them all together in one spreadsheet. 
>
> **Important** Do not forget our first piece of advice: to
> create a new file (or tab) for the cleaned data, never
> modify your original (raw) data.
> 
> After you go through this exercise, we'll discuss as a group what was wrong
> with this data and how you would fix it. 
> 
> > ## Solution
> > - Take about 10 minutes to work on this exercise.
> > - All the mistakes in [02-common-mistakes](../02-common-mistakes) are present in the messy dataset. If the
> > exercise is done during a workshop, ask people what they saw as wrong with
> > the data. As they bring up different points, you can refer to [02-common-mistakes](../02-common-mistakes)
> > or expand a bit on the point they brought up.  
> > - Note that there is a problem with dates in table 'plot 3' in `2014` tab. The field assistant who collected the data
> > for year 2014 initially forgot to include their data for 'plot 3'. They came back in 2015 to include the missing data and 
> > entered the dates for 'plot 3' in the dataset without the year. Excel automatically filled in the missing year as the
> > current year (i.e. 2015) - introducing an error in the data without the field assistant realising. If you get a response 
> > from the participants that they've spotted and fixed the problem with date, you can say you'll come back to dates again 
> > towards the end of lesson in episode [03-dates-as-data](../03-dates-as-data). If participants have not spotted the 
> > problem with dates in 'plot 3' table, that's fine as you will address peculiarities of working with dates in 
> > spreadsheets in episode [03-dates-as-data](../03-dates-as-data).  
> {: .solution}
{: .challenge}

> Hadley Wickham, *Tidy Data*, Vol. 59, Issue 10, Sep 2014, Journal of
> Statistical Software. [http://www.jstatsoft.org/v59/i10](http://www.jstatsoft.org/v59/i10).
 -->

