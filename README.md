# Desafio MPRJ para Backend

Este repositório contém questões e códigos referentes ao desafio para vaga de desenvolvedor backend sênior Python/Django na GADG/MPRJ.

Este desafio é constituido de um desafio técnico voltado para a definição de um projeto e arquitetura de um serviço.

Clone o repositório ou faça um fork para a sua conta do GitHub, para que possa trabalhar sem problemas. Ao terminar, coloque-o como público ou nos dê acesso para que possamos visualizar e avaliar o seu trabalho!

---------

## Desafio Técnico - Projeto e Arquitetura de um Serviço

**Disclaimer Inicial**: Não é necessário (**e nem esperado!**) que você implemente um código funcional para este desafio!!!

O importante é que você saiba estruturar e projetar os componentes do seu código; explicar quais aspectos devem ser levados em consideração; as tecnologias de suporte que poderiam ser utilizadas, de que forma elas se comunicariam com o Django e com que fim; possíveis problemas e limitações da abordagem escolhida; entre outras questões relativas ao processo de design da arquitetura do serviço.

A estrutura básica do código é fornecida **APENAS** para que você tenha uma base onde trabalhar e organizar suas ideias, fazer um esqueleto das suas classes e componentes, e separá-los em módulos distintos da forma que preferir. Não é obrigatório utilizar todos os arquivos fornecidos, e nem mesmo utilizar a mesma estrutura de arquivos. Sinta-se à vontade para modificar tudo de acordo com o seu projeto.

Em nenhum momento da avaliação será utilizado como critério o fato do código rodar ou não. Por isso, não se preocupe com problemas de sintaxe ou de nome de métodos ou o que quer que seja nesse sentido. Caso não lembre exatamente do nome de uma biblioteca e/ou método que faça o que você precisa, é inclusive permitido que se utilize de pseudo-código, desde que isso ajude você a expressar os conceitos necessários para realizar a dada tarefa.

Imagine que o objetivo é simular o design de arquitetura de um serviço para uma demanda de negócio! Sinta-se livre para usar a criatividade para desenhar uma arquitetura que atenda às necessidades da demanda!

Dito isso, considere o seguinte cenário fictício:

Os membros do Ministério Público do Rio de Janeiro (MPRJ) precisam, diariamente, acompanhar a tramitação de seus processos no Tribunal de Justiça do Rio de Janeiro (TJRJ). Com isso em mente, uma demanda foi feita para a implementação de uma aplicação que auxilie os membros nessa tarefa. Um serviço em uma API Rest deverá ser feito, de forma que realize as seguintes tarefas:

- 1) O endpoint do serviço deverá receber um parâmetro inteiro positivo `id`, correspondente ao número de um documento.

- 2) Uma consulta deverá ser feita utilizando `id`, em um banco relacional externo, obtendo um conjunto de dados relativos a esse documento, `dados_documento`. Caso necessário, considere que esse banco é acessível pela rede interna, com um HOST, PORT, USER e PASSWORD já definidos. Não se preocupe com o formato dos dados no banco ou outras questões de implementação da consulta.

- 3) Dentro de `dados_documento`, há uma coluna com um número `id_tjrj`, que deverá ser utilizado para chamar um serviço SOAP externo, disponibilizado pelo TJRJ. Este serviço fornece um objeto XML com a tramitação do documento desejado `tramitacao_documento`. Essa informação, `tramitacao_documento`, será enviada como resposta do nosso endpoint. Caso ache relevante considerar no seu projeto, considere que possuimos um ACCESS_TOKEN, utilizado para acessar esse serviço SOAP. Também caso ache relevante, considere que o XML da resposta venha no seguinte formato:

```
<TRAMITACOES>
<TRAMITACAO idtram="1">
<data>01/01/1999</data>
<doc>Texto falando sobre qual foi a tramitação, transcrições de ata, etc etc</doc>
</TRAMITACAO>
<TRAMITACAO idtram="2">
<data>02/01/1999</data>
<doc>Texto falando sobre qual foi a tramitação, transcrições de ata, etc etc</doc>
</TRAMITACAO>
</TRAMITACOES>
```


- 4) Outra necessidade, é que um log do serviço deverá ser guardado, com informações diversas sobre: o request realizado; o usuário que o realizou; assim como os resultados obtidos do TJRJ. Considere que o serviço do TJRJ pode sofrer alterações no futuro (por exemplo, a resposta XML pode ser extendida no futuro e vir com um número maior de informações), de forma que o formato dos dados no log pode mudar, dependendo da forma que escolher estruturar esse log.

- 5) Suponha que, ao fazer um request para esse endpoint, seja guardado um par `(usuário, id_tjrj)`. De tempos em tempos, a nossa aplicação deverá consultar o serviço SOAP do TJRJ para verificar possíveis mudanças ocorridas na tramitação do documento associado, desde a última consulta. Caso tenha havido mudanças, o nosso serviço deverá disparar o envio de um email para o usuário, de forma assíncrona, alertando-o que houve mudanças no documento.
**OBS**: Não se sinta preso(a) ao Django! Caso julgue que essa tarefa é melhor realizada utilizando outras tecnologias em conjunto para sub-tarefas específicas, explicite isso no seu projeto!

- 6) O nosso endpoint acessa dados sensíveis! Assim, ele não pode estar aberto para todas as pessoas que conheçam sua URL. Apenas usuários autorizados devem conseguir utilizá-lo. Pense numa abordagem de autenticação e/ou autorização que satisfaça esse requisito do serviço. Não esqueça de dizer por que escolheu essa abordagem!

A partir desse ponto, você já deve possuir um esqueleto/projeto bem estruturado para o seu serviço, contemplando essas funcionalidades essenciais! Sua equipe então configura e faz o deploy de um servidor em produção. Algumas situações surgem a partir daí:

- 7) Ao analisar o serviço em produção, você nota que a maioria dos requests são feitos para um conjunto pequeno de `id`s. Nos últimos 7 dias, 80% dos requests, por exemplo, são feitos para o documento com parâmetro `id=1000`. Ao indagar a área de negócios, você descobre que esse comportamento é normal, com um ou mais documentos recebendo muita atenção de tempos em tempos - hoje é o caso do `id=1000`, mas semana que vem poderia ser o `id=1500`. Com essa informação em mãos, você faria alguma modificação no serviço e/ou nas tecnologias utilizadas para o deploy de forma a otimizá-lo? Por quê?

- 8) Por último: suponha que o "Fulano de Tal" esteja sendo investigado pelo MP. Uma demanda foi feita para implementarmos uma funcionalidade que busque, utilizando o log do nosso serviço, os usuários que tiveram acesso a informações de tramitação de documentos em que o "Fulano de Tal" aparece. Considere que um colega seu começou a tarefa, e já implementou algumas funcionalidades, com base no log que você implementou. No entanto, uma das etapas inclui percorrer o log inteiro, buscando no texto completo dos documentos (ou seja, o texto do campo `<doc>` do XML) uma string de busca (ex.: "Fulano de Tal"), e ele pediu sua ajuda. Qual abordagem você sugeriria que seja feita para realizar esse full text search dentro dos documentos das tramitações?

**Lembre-se: não é necessário nem esperado que você escreva um código funcional, é permitido inclusive que utilize pseudo-código se desejar!** Estamos interessados na sua capacidade de projetar um serviço com múltiplas partes! Por isso, não esqueça de fornecer o máximo de detalhes sobre as abordagens que escolher, os motivos que fizeram você escolher essa abordagem - inclusive podendo citar experiências passadas -, tecnologias utilizadas, entre outros.

## Entrega

A entrega do desafio pode ser feita de algumas maneiras diferentes. *De preferência*, seria interessante que fizesse um esqueleto das suas classes e componentes, utilizando-se de comentários no seu código para as explicações das escolhas que fizer, onde entraria a comunicação com outras tecnologias, etc.

Além disso, colocamos um arquivo `respostas_e_comentarios.txt`, onde poderá fazer anotações e comentários relativos a cada um dos pontos do desafio, seja como um rascunho/apanhado geral, seja para mencionar pontos que possam ficar estranhos como comentários no código.

Caso prefira e julgue mais fácil de se expressar, também sinta-se à vontade para fazer um desenho do seu projeto.

Não se esqueça: seja criativo, divirta-se, e boa sorte!
