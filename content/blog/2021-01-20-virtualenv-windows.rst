Como usar e criar Virtualenv no Windows 10
==========================================

:title: Como usar e criar Virtualenv no Windows 10
:date: 2021-01-20 17:00
:tags: python, virtualenv, windows
:category: Blog
:slug: virtualenv-windows
:summary: Como criar e usar ambientes virtuais com Virtualenv no Windows 10
:authors: António Neves

|

.. image:: /images/antonio_02_01.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Virtualenv no windows 10

|
| Neste artigo vou explicar a necessidade de utilizar ambientes virtuais,
  como usar e criar, com Virtualenv no Windows 10.
| Existem outras boas ferramentas para criar ambientes virtuais, mas sem
  dúvida Virtualenv é um dos mais queridos e usados.
|

------

Ambientes virtuais, porquê?
---------------------------

|
| Vamos imaginar que temos instalado no sistema operativo a versão do
  Python 3.7.9, e vamos começar a desenvolver um sistema com Kivy, instalamos
  a biblioteca Kivy e tudo bem, vai funcionar sem problemas, depois precisamos
  instalar OpenCV, e tudo continua funcionando bem, entretanto começamos
  a desenvolver um sistema web, e instalamos Django e todas as bibliotecas necessárias.
| Reparem que já começa a ficar tudo um pouco confuso, tudo instalado na
  mesma pasta junto da instalação principal do Python.
| Mas agora podemos ter instalado uma biblioteca para usar com o Django
  que não vai funcionar por incompatibilidade com outra biblioteca instalada
  anteriormente para ser usada no nosso projeto Kivy.
| E agora? Desinstalamos uma e deixamos a outra?
| Vamos imaginar outra situação, temos instalado Django 3 e precisamos mexer
  em um projeto antigo desenvolvido com Django 2 com algumas bibliotecas
  que só funcionam com Django 2 e não funcionam com Django 3.
| Entendem agora como o ideal é sempre ter uma instalação Python para cada
  projeto que vamos desenvolver?
| A melhor solução é criarmos um ambiente virtual para cada projeto, ou pelo
  menos criar um para projetos parecidos ou com as mesma necessidade a nível
  de versões e bibliotecas.
| Outra situação em que existe necessidade de utilizar ambientes virtuais,
  é quando queremos experimentar se as nossas aplicações funcionam com
  diferentes versões das mesmas bibliotecas.
| Mas a principal razão, é mantermos as instalações do Python no sistema,
  originais, limpas e sempre prontas para que ambientes virtuais sejam
  criados sem problemas.
|
| É importante também não confundir, versões diferentes do Python no Windows
  com ambientes virtuais diferentes.
| Na prática cada ambiente virtual vai “criar uma cópia” de uma versão do
  Python que escolhermos, versão que já tenha sido instalada anteriormente no sistema.
| Neste artigo explico |python_windows|.
| Podemos ter várias versões do Python diferentes instaladas e podemos ter
  vários ambientes virtuais com a mesma versão do Python, mas em cada ambiente,
  diferentes bibliotecas.
|

.. |python_windows| raw:: html

   <a href="https://python.pt/blog/2021/01/19/instalacao-python-windows" target="_blank" rel="noopener">Como instalar várias versões Python no Windows 10</a>

------

Considerações Iniciais
----------------------

|
| No meu sistema já tenho instalado o Python 3.7.9 e o Python 3.9.0.
|
| Vamos usar o terminal e o explorador do Windows.
|

------

Instalação Virtualenv
---------------------

|
| Vamos começar por ver se o Virtualenv já está instalado, para isso abrimos
  um terminal (prompt de comando) com permissões de administrador e digitamos.
|

.. code-block:: python

   where virtualenv

|
| No caso de não estar instalado simplesmente digitamos.
|

.. code-block:: python

   pip install virtualenv

|
| Na foto abaixo, podemos ver que no meu sistema já tenho o virtualenv instalado.
| Pode parecer uma contradição em relação ao que expliquei anteriormente,
  mas é a única instalação que vamos fazer “junto” da instalação principal
  do Python no Windows.
| No caso de termos várias versões diferentes do Python, vai ser instalado
  junto com a versão que o Windows “considera” como principal, como explicado
  neste |python_windows_2|.
| Se fizermos a instalação usando um terminal sem permissões de administrador,
  a instalação vai ser apenas para o usuário logado no momento.
|
|

.. |python_windows_2| raw:: html

   <a href="https://python.pt/blog/2021/01/19/instalacao-python-windows" target="_blank" rel="noopener">artigo</a>

.. image:: /images/antonio_02_02.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Confirmação instalção do Virtualenv

|
|

------

Onde guardar os ambientes virtuais? Nomes e quantidade.
-------------------------------------------------------

|
| Vamos pensar juntos, se tivermos vários projetos que utilizam a mesma
  versão do Python, e as mesmas bibliotecas, basta criar um ambiente virtual
  para esses projetos.
| Bibliotecas diferentes já precisamos de ambientes diferentes.
| Mas resumindo, os ambientes virtuais podem ser guardados onde quiserem
  e terem o nome que quiserem.
| Eu por exemplo, tenho uma pasta chamada devenvs onde guardo alguns.
| Para projetos maiores e em especial com Django eu guardo o ambiente virtual
  dentro da própria pasta do projeto.
|
| Vamos então criar uma pasta dentro da nossa pasta pessoal chamada ‘devenvs’.
|
|

.. image:: /images/antonio_02_03.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Criar ambiente virtual

|
|

------

Criar um ambiente virtual.
--------------------------

|
| Entramos dentro da pasta que criamos anteriormente.
|
| Agora temos 2 opções, ou criamos uma nova pasta com o nome que escolhermos
  para o ambiente virtual e depois dentro da pasta criamos o ambiente,
  ou vamos criar diretamente a pasta e o ambiente ao mesmo tempo.
| Não sei explicar porquê, mas eu costumo criar primeiro a pasta escolhendo
  já o nome do ambiente virtual e depois sim criar o ambiente virtual.
| Mas vou explicar as duas maneiras de fazer isso.
|
| Dentro da pasta onde vamos guardar os ambientes virtuais, vamos
  criar outra pasta chamada py390 (pode ser qualquer nome)
|
|

.. image:: /images/antonio_02_04.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Pasta dos ambientes virtuais

|
|
| Vamos abrir um terminal, não é necessário um terminal com permissões de administrador.
| Podemos usar o comando:
|

.. code-block:: python

   cd

|
| Para chegar dentro da pasta onde vamos criar o ambiente virtual.
| Em seguida digitamos:
|

.. code-block:: python

   virtualenv .

|
| Atenção precisamos digitar ‘ virtualenv ‘ um espaço e um ponto ‘ . ‘
| O ponto é necessário por que já criamos anteriormente a pasta do ambiente virtual.
|
|

.. image:: /images/antonio_02_05.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Ambiente virtual

|
|
| Já temos um ambiente virtual, com a versão Python 3.9.0.
|
| Como utilizamos apenas ‘virtualenv’ sem definir a versão do Python,
  foi criado um ambiente com a versão principal do Windows, recordem que
  no meu caso tenho duas versões instalas no Windows, sendo a 3.9.0 a versão principal.
|
| Agora chegou a hora de aprender como usar o ambiente virtual.
|
|

------

Como usar o Virtualenv
----------------------

| Antes de usar o ambiente virtual, por exemplo para instalar as bibliotecas
  necessárias, é necessário ativa-lo.
|
| No terminal entramos dentro da pasta do ambiente virtual, no nosso caso
  chama-se ‘py390’, e depois precisamos entrar dentro da pasta Scripts.
|
| Dentro da pasta Scripts, digitamos
|

.. code-block:: python

   activate

|
| Este é o comando para ativar o ambiente virtual.
|
| Reparem que agora entre parentes, temos o nome do ambiente virtual
  confirmando que está ativado.
|
| Explicando de uma maneira simples, foi criado temporariamente nas variáveis
  de ambiente, um caminho (path) indicando ao Windows que a versão principal
  do Python, é a versão que está no ambiente virtual ativado.
|
| Podemos continuar dentro da pasta Scripts ou mover para outra, mas os
  comandos ‘pip’ por exemplo para instalarmos bibliotecas necessárias,
  vão instalar essas bibliotecas dentro do ambiente virtual.
|
| Se arrancarmos pelo terminal agora, um arquivo .py, o interpretador
  Python vai ser o do ambiente virtual.
| Se utilizarmos um IDE e indicarmos como interpretador o ambiente virtual,
  a situação vai ser a mesma.
| Com Visual Studio Code ou PyCharm por exemplo, ao abrirmos um projeto e indicarmos o ambiente virtual o próprio IDE ativa o ambiente virtual
|
|

.. image:: /images/antonio_02_06.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Activar ambiente virtual

|
|
| Para desactivar, basta digitar.
|

.. code-block:: python

   deactivate

|
|

.. image:: /images/antonio_02_07.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Desactivar ambiente virtual

|
|

------

Como criar um ambiente virtual com uma versão especifica do Python
------------------------------------------------------------------

|
| Embora a maneira de usar seja igual, dentro da pasta ‘Scripts’
  activamos com ‘activate’, ou desactivamos com o comando ‘deactivate’.
| Para criar este ambiente com uma versão do Python diferente, precisamos
  digitar um parâmetro a mais.
| Vamos começar por criar uma nova pasta, onde vamos criar o novo ambiente virtual.
| Vamos chamar de py379.
|
| Entramos no terminal, e usamos o comando:
|

.. code-block:: python

   cd

|
| Até entrarmos dentro da nova pasta, e digitamos:
|

.. code-block:: python

   virtualenv . --python=3.7.9

|
| E já temos um ambiente virtual com o Python 3.7.9.
|
| Se neste momento, apareceu algum erro, mais abaixo tem uma nota importante,
  onde explico outra forma de escolher a versão do Python para criar o ambiente virtual.
|
| Aproveito para recordar que esta versão do Python já tinha sido instalada
  anteriormente no Windows e está no PATH.
| Vejam este artigo: |python_windows3|, se têm alguma dúvida.
|
|

.. |python_windows3| raw:: html

   <a href="https://python.pt/blog/2021/01/19/instalacao-python-windows" target="_blank" rel="noopener">Como instalar várias versões Python no Windows 10</a>

.. image:: /images/antonio_02_08.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Escolher a versão do Python

|
|
| Vamos digitar alguns comandos para que seja possivel entender mais facilmente
  como utilizar um ambiente virtual.
|
| Podemos continuar no terminal, dentro da pasta do novo ambiente virtual,
  e digitamos o comando:
|

.. code-block:: python

   python

|
| Reparem que o ambiente virtual não está ativado e por isso, o Python
  é o 3.9.0, a versão principal do Windows.
|
|

.. image:: /images/antonio_02_09.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Python 3.9.0

|
|
| Continuamos digitando:
|

.. code-block:: python

   exit()

|
| Para sair do Python.
| Dentro da pasta do ambiente virtual py379, para entrarmos na pasta
  Scripts, usamos:
|

.. code-block:: python

   cd Scripts

|
| E depois:
|

.. code-block:: python

   activate

|
| Agora que já ativamos o ambiente virtual, digitamos novamente.

.. code-block:: python

   python

|
| Neste momento estamos a usar o Python 3.7.9.
|
|

.. image:: /images/antonio_02_10.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Python 3.7.9

|
|
| **Nota importante**
|
| Até agora criámos dois ambientes virtuais com Virtualenv,
  com diferentes versões de Python já instaladas anteriormente.
| Mas as duas versões que usei neste tutorial, além de já estarem instaladas,
  também estão no PATH do Windows.
|
| No caso de termos necessidade de criar um ambiente virtual com uma versão
  do Python que não esteja no path, precisamos utilizar um comando que
  indique o caminho completo do Python executável.
|
| Podemos encontrar o caminho de várias maneiras, mas eu costumo usar o explorador do Windows.
|
|

.. image:: /images/antonio_02_11.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Python

|
|
| Voltamos para o terminal, criamos uma nova pasta dentro da pasta onde
  guardamos os ambientes, desta vez vamos criar a pasta pelo terminal
  em vez de usar o explorador do Windows.
|
| Dentro da pasta ‘devenvs’, usamos o comando:
|

.. code-block:: python

   mkdir venv379

|
| para criar a pasta ‘venv379’, depois entramos nela com o comando:
|

.. code-block:: python

   cd venv379

|
| Dentro da pasta onde vai ser criado o novo ambiente virtual em vez de usarmos
| ‘virtualenv . –python=3.7.9’, vamos utilizar o comando:
|

.. code-block:: python

   virtualenv . --python "C:\Program Files\Python37\python.exe"

|
|

.. image:: /images/antonio_02_12.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Python

|
|

------

Considerações finais e resumo
-----------------------------

|
| Creio que neste momento já entenderam a necessidade de sempre desenvolvermos
  nossos projetos utilizando ambientes virtuais, acredito também que já
  todos conseguem criar e utilizar sem problemas Virtualenv.
|
| Agora é possível instalar e desinstalar com segurança, novas  bibliotecas
  e experimentarmos o que quisermos.
|
| Para apagar um ambiente virtual basta apagar a pasta.
|
| Como boa prática a primeira coisa que faço sempre, depois de criar um
  ambiente virtual, é atualizar o ‘pip’ e o ‘setuptools’
|
| E nunca esqueçam de ativar o ambiente para ser usado.
| No caso de mudarem as pastas de lugar lembrem também que é necessário
  informar os IDEs que utilizam.
|
| Autor: |antonio_neves|
|
|

.. |antonio_neves| raw:: html

   <a href="https://github.com/Antonio-Neves" target="_blank" rel="noopener">António Manuel Neves</a>
