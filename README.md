# Gerador de Rede Social

Este algoritmo faz parte de uma série de trabalhos propostos na cadeira de estruturas de dados II do curso de Ciência da Computação, ministrado na Universidade Federal do Pampa (UNIPAMPA).

<p align="center">
  <img width="250" height="150" src="https://user-images.githubusercontent.com/57903394/76473542-8c3abe80-63d7-11ea-8c32-94f878999198.png">
</p>

## Objetivo do Código
O algoritmo tem como objetivo criar uma rede social entre os estudantes de uma universidade ficticia. Para isso, o algoritmo carrega dados que compunham perfis de estudantes, esses dados estão contidos em documentos .txt e localizados em um diretório informado pelo usuário.
Tais dados correspondem as seguintes variaveis em uma estrutura de dados: Matricula, Nome, Curso, E-mail, Telefone, Cidade, RelacionamentoN1 e RelacionamentoN2, visto que:
- Relacionamento N1: representa os relacionamentos de nível 1 de um determinado estudante.
- Relacionamento N2: representa os relacionamentos de nível 2 de um determinado estudante.

A rede social gerada pelo código é representado por grafos, onde: cada vértice representa um aluno e as arestas representam a relação entre dois vértices. Cada vértice é possuí um ID, sendo este a matricula de um determinado estudante. Ou seja, cada vertice representa um estudante, e a identificação deste vértice é igual a matricula de seu respectivo estudante.

## Entradas

O usuário deve fornecer, no momento de executar o código, o nome do diretório que se encontra os dados que irão gerar o grafo, para isso usa-se da seguinte sintaxe:

`python main.py Diretorio`

O arquivo *main.py* executa um menu simples, que é impresso diretamente no terminal. Através deste menu é possivel escolher a função que deseja executar, destaca-se que a primeira função a ser sempre executada é a de criar um grafo, já que todas as outras função dependem desta.

O arquivo *grafo.py* é possivel encontrar todas as funções implementadas para este programa, desde a criação dos vértices e arestas, até a criação do PDF que mostra de forma gráfica o grafo gerado pelo algoritmo. Já o *gera_dados.py* tem como função gerar aleatóriamente os dados dos perfis utilizados para a criação da rede social, para executar este código basta utilizar o seguinte comando:

`python gera_dado.py diretorio quantidade inicio maxN1 maxN2`

Onde:

- diretorio: refere-se ao nome do diretório que será criado para armazenar os arquivos .txt
- quantidade: número de perfis a serem criados
- inicio: ID do primeiro perfil a ser criado
- maxN1: quantidade máxima de relacionamentos N1 que os estudantes podem ter
- Max N2: quantidade máxima de relacionamentos N2 que os estudantes podem ter

## Saídas

Ao escolher a opção "mostrar N1" ou "Mostrar N2" o algoritmo imprime todos os relacionamentos de determinado nível entre os vértices existentes. Caso a escolha seja "Mostrar todas as relações" o programa irá imprimir todas as relações entre os vértices, independente do nível.

<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/57903394/76473656-e76cb100-63d7-11ea-91cb-a6a0dac812e1.png">
</p>

Caso a escolha "GraphvizN1" ou "GraphvizN2" o algoritmo cria uma representação gráfica (em pdf) de todos os relacionamentos de determinado nível entre os vértices existentes. Por fim, se "Graphviz todos os relacionamentos" for selecionado o programa irá criar uma representação gráfica de todas as relações entre os vértices, independente do nível.

<p align="center">
  <img width="300" height="500" src="https://user-images.githubusercontent.com/57903394/76473946-ceb0cb00-63d8-11ea-89b6-92fa55eeb601.png">
</p>


## Pacotes utilizados

- Graphviz
