
.. image:: http://sitecoral.appspot.com/coral.png

|
|
|

Autor
=====
* Gustavo Rezende <nsigustavo@gmail.com>

|
|
|


Resumo
------

Coral é uma linguagem de programação poderosa e de fácil aprendizado. Ela possui estruturas de dados de alto nível eficientes, bem como adota uma abordagem simples e efetiva para a programação orientada a objetos. Sua sintaxe elegante e tipagem dinâmica, em adição à sua natureza interpretada, tornam Coral ideal para scripting e para o desenvolvimento rápido de aplicações em diversas áreas e na maioria das plataformas.  Esta magnífica linguamge, é similar a linguagem de programação Python sendo interpretada por sua Maquina Virtual e compatível com programas Pythons existentes.
Coral não se trata exatamente de uma nova linguagem, sintaticamente ela é exatamente igual a linguagem Python somante modificando suas palavras reservadas para o português. Otra característica importante é que novas traduções de bibliotecas python podem ser acrescentadas de maneira fácil e elegante. O interpretador Coral é facilmente extensível incorporando novas funcionalidaes e traduções do Python, simplesmente adicionando um dicionario para os termos utilizados.
O interpretador de Python é utilizado, para gereção de seu bytecodes sendo também plenamente interoperável com Python e vice-versa. A utilização de qualquer bibliotéca Python é totalmente transparente onde são utilizadas e estão disponíveis para a maioria das plataformas a partir do site, http://www.python.org/, e distribuídos livremente. 
Esta texto introduz o leitor informalmente aos conceitos básicos e aspectos do sistema e linguagem Coral. É aconselhável ter um interpretador Python disponível para se poder *por a mão na massa*, porém todos os exemplos são auto-contidos, assim o tutorial também pode ser lido sem que haja a necessidade de se estar on-line. 
Para uma descrição dos módulos e objetos padrão, veja o documento Referência da Biblioteca Python. O Manual de Referência Python oferece uma definição formal da linguagem e extença documentação. Existem também diversos livros abordando Python em maior profundidade. 
Este tutorial não almeja ser abrangente ou abordar todos os aspectos, nem mesmo todos os mais frequentes. Ao invés disso, ele introduz muitas das características dignas de nota em Coral, e fornecerá a você uma boa idéia sobre o estilo e o sabor da linguagem (de nossa linguagem). Após a leitura, você deve ser capaz de ler e escrever programas e módulos em Coral, e estará pronto para aprender mais sobre os diversos módulos de biblioteca descritos na Referência da Biblioteca Python e Coral.

|
|
|
Abrindo o Apetite
=================

Coral é uma linguagem copilada e interpretada, uma vez que há necessidade de compilação para bytecode python. O interpretador pode ser usado interativamente, o que torna fácil experimentar diversas características da linguagem, escrever programas *descartáveis*, ou testar funções em um desenvolvimento bottom-up. É também uma útil calculadora de mesa. 

* Coral permite a escrita de programas compactos e legíveis. Programas escritos em Coral são tipicamente mais curtos do que seus equivalentes em C ou C++, por diversas razões:
* os tipos de alto-nível permitem que você expresse operações complexas em uma único comando (statement); 
* a definição de bloco é feita por identação ao invés de marcadores de início e fim de bloco; 
* não há necessidade de declaração de variáveis ou parâmetros formais;

Coral é extensível: se você sabe como programar em C, é fácil adicionar funções ou módulos diretamente no interpretador, seja para desempenhar operações críticas em máxima velocidade, ou para vincular programas Coral a bibliotecas que só estejam disponívies em formato binário (como uma bibloteca gráfica de terceiros). 
Uma vez que você tenha sido fisgado, você pode vincular o interpretador Coral a uma aplicação escrita em C e utilizá-la como linguagem de comandos ou extensão para esta aplicação. 
Agora que você está entusiasmado com Coral, vai desejar examiná-la com maior detalhe. Partindo do princípio que a melhor maneira de aprender uma linguagem é usando-a, você está agora convidado a fazê-lo com este tutorial. 
No próximo capítulo, a mecânica de utilização do interpretador é explicada. Essa informação, ainda que mundana, é essencial para a experimentação dos exemplos apresentados mais tarde. O resto do tutorial introduz diversos aspectos do sistema e linguagem Coral por intermédio de exemplos. Serão abordadas expressões simples, comandos, tipos, funções e módulos. Finalmente, serão explicados alguns conceitos avançados como exceções e classes definidas pelo usuário. 


|
|
|
Utilizando o interpretador
==========================

Este capitulo descreverá a instalação do Coral. Também descreveremos o processo de  compilação e execução de seu códig e o modo iterativo. Nesse modo o interpretador requisita por comandos Coral  iterativamente através do prompt primário.


Instalação
----------

Coral é um módulo python padrão (coral). Como pré-requesito, é necessário que você tenha instalado o python 2.5 ou superior. Os itens seguintes descreve como instalar o coral no Linux Ubuntu. Entretanto, a installação do Windows  será adicionado futuramente no tutorial.


Instalação do Coral no Ubuntu
-----------------------------

A instalação no Linux é mais fácil, isso porque praticamente todas as distribuições já trazem o interpretador python instalado, assim não vai ser preciso cobrir a instalação do python. Caso não possua a instlanção do python2.6. Execute estes passos::

    $ wget http://www.python.org/ftp/python/2.6.5/Python-2.6.5.tar.bz2 
    $ tar xzf Python-2.6.5.tar.bz2 
    $ cd Python-2.6.5 
    $ ./configure && make 
    $ sudo make install

Quanto ao coral, é muito fácil de instalar, apenas rode o comando easy_install do python em um terminal como qualquer outro módulo python. Entretanto, caso vc não possua instalando setuptools (easy_install) .
Setuptools provê uma série de ferramentas para distribuição e gerenciamento de "eggs" (pacotes python). A maioria dos eggs usados no desenvolvimento de softwares python está no http://pypi.python.org/, que contém um índice com centenas (talvez milhares) de aplicações, bibliotecas e frameworks python sendo distribuídos como eggs. 
A ferramenta "easy_install" permite que você instale um egg do pypi.python.org (ou outro local, mas aí você terá que explicitar a URL) digitando apenas "easy_install nome_do_pacote". Pense no easy_install como um "apt" de pacotes python::

    $ wget http://peak.telecommunity.com/dist/ez_setup.py 
    $ sudo python2.4 ez_setup.py

Agora que vc já possui os pré-requesitos para instalação do Coral, basta executar ::

    $ sudo easy_install coral

Linha de comandos
-----------------

O modulo coral do Python é o compilador que traduz código em Coral para o bytecode do Python. Ele cria todos os comandos necessário para a utilização do Coral como: 

* coral [ARQUIVO]
    - conpila arquivos com extenção * .coral* para * .pyc*s
* traduzir [ARQUIVO]
    - traduz arquivos do Coral  para Python e vice-versa, dependendo da exenteção passada.
* coralexec [ARQUIVO]
    - compila e executa arquivos com extenção * .coral* para * .pyc*s
* icoral
    - incia o modo iterativo do coral, nesse modo o interpretador requisita por comandos Coral ou Python iterativamente através do prompt primário.


Disparando o interpretador
--------------------------

O interpretador é iniciado ao executar icoral no shell  de seu Linux::

    $ icoral

Digitando um caracter EOF() (Control-D no UNIX) diretamente no prompt força o interpretador a sair com status de saída zero. Se isso não funcionar, voce pode sair do interpretador através da digitação do seguinte: *exit*. 
Quando os comandos são lidos a partir do console (tty), diz-se que o interpretador está em modo interativo. Nesse modo ele requisita por um próximo comando através do prompt primário, tipicamente três sinais de maior-que (*>>> *) ou (In[n]); para linhas de continuação do comando corrente, o prompt secundário default são três pontos (*... *). 
O interpretador imprime uma mensagem de boas vindas, informando seu número de versão e uma nota legal de copyright antes de oferecer o primeiro prompt::

    $ icoral 
    Python 2.6.2 (release26-maint, Apr 19 2009, 01:56:41) 
    [GCC 4.3.3] no linux2 
    O Coral iterativo é baseado no IPython 
    (icoral 1.0) 
    >>> 

Linhas de continuação são necessárias em construções multi-linha. Como exemplo, dê uma olhada nesse comando *para cada*::

    >>> para cada letra em "Gustavo":
    ...     imprima letra
    ...
    G
    u
    s
    t
    a
    v
    o


Scripts Executáveis em Coral
----------------------------

Em sistemas UNIXBSD, scripts Coral podem ser transformados em executáveis, como shell scripts, pela inclusão do cabeçalho::

    #! /usr/bin/env coralexec 

(Assumindo que o interpretador foi incluído do caminho de busca do usuário (PATH)) e que o script tenha a permissão de acesso habilitada para execução. O *#!* deve estar no início do arquivo .Em algumas plataformas esta linha inicial deve ser finalizada no estilo U NIX-style com (*\n*), ao invés do estilo Mac OS (*\r*) ou mesmo a terminação típica do Windows (*\r\n*). Observe que o caracter *#* designa comentários em Coral. 
Para atribuir permissão de execução (plataforma Unix) ao seu script Python, utilize o comando chmod::

    $ chmod +x meuscript.coral 

Para executar o arquivo bastar clicalo 2 vezes ou chame diretamente na linha de comando::

    $ ./meuscript.coral


Scripts Executáveis em Python
-----------------------------

Scripts Coral podem ser transformados em arquivos python compilados. Ao executar o comando coralexec ou simplismente coral, o interpretador irá criar um arquivo com o bytecode python com extenção *.pyc*, sendo que o comando *coral* apenas irá compilar enquanto o *coralexec* tambem irá executa-lo após copilar.
Para compilar seu código coral, apenas execute::

    $ coral meuscript.coral

O arquivo *meuscript.cora* contendo seu código irá ser compilado e criará um arquivo chamado *meuscript.pyc*. Este código compilado para Python é totalmente compatível com outros códigos Python. Ex.::

    $ python meuscript.pyc

