Como instalar várias versões Python no Windows 10
=================================================

:title: Como instalar várias versões Python no Windows 10
:date: 2021-01-19 17:00
:tags: python, windows, instalação
:category: Blog
:slug: instalacao-python-windows
:summary: Como instalar várias versões Python no Windows 10, de maneira simples e rápida
:authors: António Neves

|

.. image:: /images/antonio_01_01.jpeg
    :class: img-fluid rounded mx-auto d-block
    :align: center
    :alt: Python no windows 10

|
| Neste post vou explicar como instalar várias versões Python no Windows 10.
| Python é uma incrível linguagem de programação, e no momento que escrevo este
  artigo encontra-se na versão 3.9.1.
| Existem várias razões para que seja necessário ter instaladas várias versões
  do Python, no meu caso, utilizo Kivy para criar aplicações e sistemas desktop,
  mas o Kivy não funciona, pelo menos na altura em que estou a escrever este artigo,
  com versões do Python superiores a 3.7.9.
| Outra razão para ter várias versões instaladas pode ser a necessidade
  de usar ou alterar um programa criado com uma versão do Python diferente
  da que usamos atualmente.
| Aproveito para lembrar que sempre devemos utilizar ambientes virtuais para
  desenvolvermos algo, como explico neste artigo:
| |virtualenv_windows|.
|
| Eu só instalo no sistema operativo as versões de Python que necessito
  e em seguida todas as instalações de bibliotecas necessárias, como por
  exemplo Django, Kivy e outras vão ser instaladas nos ambientes virtuais.
|

-----

Considerações Iniciais
----------------------

|
| Vou explicar como instalar duas versões do Python no Windows 10.
|
| |python390|.

.. |python390| raw:: html

   <a href="https://www.python.org/downloads/release/python-390/" target="_blank" rel="noopener">Python 3.9.0</a>

| |python379|.

.. |python379| raw:: html

   <a href="https://www.python.org/downloads/release/python-379/" target="_blank" rel="noopener">Python 3.7.9</a>

|

------

Downloads necessários
---------------------

|
| Vamos na página de downloads do Python para Windows para escolhermos a versões que necessitamos.
|
| |windows_download|

.. |windows_download| raw:: html

   <a href="https://www.python.org/downloads/windows/" target="_blank" rel="noopener">www.python.org/downloads/windows/</a>

|
| Para o nosso tutorial vou escolher as opções ” Windows x86-64 executable installer “
|

.. image:: /images/antonio_01_02.jpeg
    :class: img-fluid rounded d-block
    :align: center
    :alt: Versões do Python

|

------

Instalação Python 3.9.0
-----------------------

|
| Vamos começar a instalação.
| Depois de iniciar o arquivo baixado anteriormente, recomendo que deixem
  marcadas as opções, como mostro na foto, em seguida apertamos em “Customize Installation”.
|

.. image:: /images/antonio_01_03.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Agora que estamos na seção de instalação customizável, (custumize installation),
  marcamos todas as opções como na foto abaixo e depois apertamos “Next”.
|

.. image:: /images/antonio_01_04.png
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Na próxima seção marcamos as opções como no foto abaixo.
| Eu deixo a opção de associação de arquivos .py desmarcada,
  por que sempre prefiro abrir diretamente os arquivos com um editor de texto,
  eu uso |sublime_text|, é muito rápido, leve e muito customizável, para
  desenvolver um projeto completo, um sistema, uma aplicação, utilizo |pycharm|,
  mas para abrir um arquivo, fazer um teste, uma alteração simples, Sublime é o ideal.
|
| O local de instalação deixo em: C:\\Program Files\\Python39.
|
| Em seguida podemos finalmente apertar em “Install”.

.. |sublime_text| raw:: html

   <a href="https://www.sublimetext.com/" target="_blank" rel="noopener">Sublime Text 3</a>

.. |pycharm| raw:: html

   <a href="https://www.jetbrains.com/pt-br/pycharm/" target="_blank" rel="noopener">PyCharm</a>

|

.. image:: /images/antonio_01_05.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Terminando a instalação, eu desabilito a limitação do limite de 260 caracteres para o Path.
|
| Apertamos em Close e já temos o Python 3.9.0 no Windows 10.
|

.. image:: /images/antonio_01_06.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

-----

Confirmar a instalação
-----------------------

|
| Para confirmar a instalação podemos abrir o terminal e digitar alguns comandos.
|

.. code-block:: python

   python
   py
   where python
   python -V


|

.. image:: /images/antonio_01_07.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

------

Instalação Python 3.7.9
-----------------------

|
| Chegamos no momento de instalar outra versão do Python, neste caso
  vamos usar Python 3.7.9.
| Abrimos o arquivo e seguimos os mesmos passos da instalação anterior,
  vou deixar umas fotos com as opções que eu deixo selecionadas.
|
|

.. image:: /images/antonio_01_08.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

.. image:: /images/antonio_01_09.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

.. image:: /images/antonio_01_10.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

------

Confirmar a instalação do Python 3.7.9
--------------------------------------

|
| No menu de programas do Windows, já podemos ver que temos as duas versões do Python que instalámos.
|

.. image:: /images/antonio_01_11.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

| Mas **ATENÇÂO** ao abrirmos o terminal e usarmos os comandos para utilizar
  ou para confirmar a versão do Python, descobrimos que talvez a versão
  principal não seja a que preferimos.
|

.. image:: /images/antonio_01_12.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Um problema que podemos resolver facilmente, alterando as variáveis de ambiente, para que possamos ter no Windows, como versão principal do Python a que nós preferirmos.
|
|

------

Variáveis de ambiente (PATH)
----------------------------

|
| Existem várias maneiras de chegarmos às variáveis de ambiente.
| Eu costumo ir pelo explorador do Windows.
|

.. image:: /images/antonio_01_13.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

.. image:: /images/antonio_01_14.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

.. image:: /images/antonio_01_15.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Ao entrarmos na janela “Variáveis de Ambiente” selecionamos “Path” e
  apertamos em “Editar”, como na foto abaixo.
|

.. image:: /images/antonio_01_16.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Nesta janela selecionamos com um clik do mouse o caminho (path).
| **C:\\Program Files\\Python39\\Scripts**
|
| Em seguida apertamos em “Mover para Cima” até que seja o primeiro.
|
| Vamos agora fazer o mesmo com o caminho.
| **C:\\Program Files\\Python39\\.**
|
|

.. image:: /images/antonio_01_17.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

.. image:: /images/antonio_01_18.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|
| Para terminar, o nosso PATH deve ficar como na foto abaixo. Finalmente
  apertamos em “OK” em todas as janelas para fechar.
|

.. image:: /images/antonio_01_19.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

------

Confirmação
-----------

|
| Na seção anterior eu mostrei como escolher a versão 3.9.0 para que seja o Python principal do Windows.
| Vamos agora confirmar que tudo está certo digitando no terminal os comandos já conhecidos.
|
|

.. image:: /images/antonio_01_20.jpeg
    :class: img-fluid rounded d-block
    :align: left
    :alt: Versões do Python

|
|

------

Como instalar várias versões Python no Windows 10
-------------------------------------------------

|
| Quero lembrar que qualquer instalação do Python no sistema operativo
  deve ficar “limpa” e sem alterações.
| Para desenvolver um projeto, sistema, programa, etc, que necessite utilizar
  outras bibliotecas, devemos utilizar ambientes virtuais, como explico
  neste artigo:
| |virtualenv_windows|.
|
| Para finalizar, agradeço por teres chegado até aqui, e desejo que este post tenha sido útil.
|
|

.. |virtualenv_windows| raw:: html

   <a href="https://python.pt/blog/2021/01/20/virtualenv-windows" target="_blank" rel="noopener">Como usar e criar Virtualenv no Windows 10</a>
