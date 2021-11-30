# Desenvolvimento em Gtk + Python

## Sobre o Projeto

>   **Quotes** é o aplicativo com interface gráfica desenvolvido com auxílio do software **Glade** em linguagem **Python** que permite registrar e consultar citações de obras literárias. Essa aplicação foi desenvolvida de modo que os registros fossem armazenados em um banco de dados, renderizado na inicialização tal como a cada nova inscrição ou remoção.

>   Assim, foi criada a base de dados `modelo.db`, a qual é renderizada na janela inicial do aplicativo, e a que os novos registros são adicionados. Para tal, é necessário pressionar o botão `Novo`, que desencadeia a abertura da janela de registros, em que é possível acrescentar informações como a autoria e o título da obra.

>   Já, para a adição de uma nova citação, na janela de registros, deve-se clicar no botão `Quote`, de forma a possibilitar o acesso à janela de citações, na qual pode-se digitar o texto pretendido. Então, nesta aba,  deve-se pressionar o botão `Pronto!`, de maneira a retornar à janela anterior, na qual a citação estará disponível. 

>   Para que o conjunto de informações seja compilado e armazenado no database `modelo.db`, é necessário pressionar o botão `Registrar`. Além disso, pensando-se na possibilidade de adicionar múltiplas citações da mesma obra, foi criado um segundo banco de dados `quotes.db`, em que são armazenadas provisoriamente as citações submetidas na janela de registro. 

>   Assim, apesar de ser possível alterar as entradas como aurotia e ano de publicação sem reiniciar a janela de registros, foi programado o descarte da tabela de `quotes.db` a partir do clique do botão `Encerrar`, com a finalidade de manter o display de citações organizado e diminuir o risco de serem realizados registros errôneos. Dessa forma, para a submissão de uma nova citação de diferente obra, é recomendado pressionar o supracitado botão `Encerrar` e, na janela inicial, novamente, o botão `Novo`, de modo que uma nova aba de registros com entradas e display limpos será iniciada.

>   Contudo, tendo em vista eventuais erros, tanto na janela de registros como na aba inicial, constam botões `Remover`, a partir dos quais é possível deletar o item selecionado no display do banco de dados correspondente. Ainda, levando-se em consideração a dificuldade de reconstrução de um item da base `modelo.db`, a remoção de um registro desse banco só é efetuado após a confirmação desse desejo na janela de aviso.

>   Então, selecionado um item na janela inicial, é possível acessar o registro completo pressionando o botão `Abrir`, de modo a inicial uma janela de visualização, na qual se tem acesso ao botão `Editar`. A patir do clique deste, abre-se a janela de edição, em que são apresentados todos os parâmetros da citação selecionada. Nesta janela, pressionando-se o botão `Salvar`, efetua-se a atualização das informações do registro no banco de dados `modelo.db`. 

>   Para efeito de exemplificação, foi deixada uma base de dados com registros, os quais podem ser deletados, bem como os próprios arquivos das bases, recriados novamente na inicialização do aplicativo, caso não sejam encontradas.