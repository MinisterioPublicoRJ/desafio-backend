# Desafio MPRJ para Backend

Este repositório contém questões e códigos referentes ao desafio para vaga de desenvolvedor backend Python/Django na GADG/MPRJ.

Este desafio é constituido de 3 etapas:

- Perguntas dissertativas sobre aspectos diversos de código e tomada de decisão;
- Desafio técnico para implementação de um endpoint em uma API Rest;
- Desafio de revisão de Pull Request.

Sinta-se à vontade para realizar as etapas na ordem que preferir!

Clone o repositório ou faça um fork para a sua conta do GitHub, com as branches "main" e "feature_colega", para que possa trabalhar sem problemas. Ao terminar, deixe-o público para que possamos visualizar e avaliar o seu trabalho!

---------

## Perguntas dissertativas

O arquivo etapa1_perguntas.txt possui algumas perguntas que gostaríamos que respondesse! Dê uma olhada no arquivo e coloque suas respostas logo abaixo de cada questão.

---------

## Desafio Técnico - Implementação de um endpoint

A XY Inc. é uma empresa especializada na produção de excelentes receptores GPS (Global Positioning System). A diretoria está empenhada em lançar um dispositivo inovador que promete auxiliar pessoas na localização de locais registrados no sistema (LRs), e precisa muito de sua ajuda. Você foi contratado para desenvolver a plataforma que fornecerá toda a inteligência ao dispositivo! Esta plataforma deve ser baseada em serviços REST, de forma a flexibilizar a integração.

Atualmente, já estão disponíveis serviços para cadastrar novos pontos de interesse, e para listar os pontos de interesse já cadastrados. Ambos podem ser acessados pelo endpoint '/locais', através dos métodos POST e GET. Sua implementação é feita pela LocalRegistradoView, presente no arquivo `desafio/views.py`, e utilizam uma view genérica do django rest framework para este fim.

Construa um serviço para listar LRs por proximidade. Este serviço receberá uma coordenada X e uma coordenada Y, especificando um ponto de referência, bem como uma distância máxima (d-max) em metros. O serviço deverá retornar todos os LRs da base de dados que estejam a uma distância menor ou igual a d-max a partir do ponto de referência.

Exemplo de Base de Dados:

- 'Lanchonete' (x=27, y=12)
- 'Posto' (x=31, y=18)
- 'Joalheria' (x=15, y=12)
- 'Floricultura' (x=19, y=21)
- 'Pub' (x=12, y=8)
- 'Supermercado' (x=23, y=6)
- 'Churrascaria' (x=28, y=2)

Exemplo de Uso:

Dado o ponto de referência (x=20, y=10) indicado pelo receptor GPS, e uma distância máxima de 10 metros, o serviço deve retornar os seguintes LRs:

- Lanchonete
- Joalheria
- Pub
- Supermercado

Não esqueça de fazer um ou mais testes para o seu endpoint!

OBS: É esperado que "x", "y" e "d-max" sejam sempre inteiros com valor >= 0. No entanto, o usuário da API pode acabar enviando valores diversos por engano. Leve isso em consideração ao pensar em tratamentos de erro.

- Pergunta 1 (responda no espaço comentado reservado no arquivo `desafio/views.py`):

Suponha que, ao colocar o serviço em produção e analisando o comportamento dos usuários, você percebe que os requests para (x=20, y=10) correspondam a 90% dos requests feitos para esse endpoint, com os outros 10% distribuidos entre outros valores. Com essa informação em mãos, o que poderia ser feito para otimizar a performance do endpoint?

----------

## Desafio Pull Request

No repositório, há uma branch chamada "feature_colega", onde um(a) colega de trabalho implementou uma nova feature, e pediu para que você a revisasse. Revise o código deste(a) companheiro(a) de trabalho, sugerindo modificações e fazendo comentários onde julgar necessário.

OBS: Caso o PR não esteja aberto de "feature_colega" para "master", abrir um PR pelo GitHub para que o processo fique mais simples.
