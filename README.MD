# Teste de Nivelamento - Lara Gabrielly

Vaga para estágio em engenharia de dados

## Documentação

Primeiramente é importante salientar as tecnologias utilizadas.

### -> Python

### -> Jupyter Notebook

Utilizado nos 2 primeiros testes que já rodam no próprio arquivo, é necessário instalar as seguintes bibliotecas caso a IDE não reconheça:

```python
pip install requests wget zipfile tabula-py pandas
```

Para o terceiro teste, utilizei o

### -> Postgresql

Os arquivos `DemonstraçoesContabeisSQL.ipynb` e `OperadorasAtivasSQL.ipynb` podem ser executados criando as querys no Banco de Dados.

Os outros 2 arquivos se referem as duas query analíticas, sendo a 3.5.1 referente a pergunta

`Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?`

#### ❗ É importante frisar que levei em consideração a data 31-12-2023 para criar essa query, já que com current_date não obtive resultados. Engloba os meses de outubro, novembro e dezembro de 2023.

e a segunda referente a pergunta

`Quais as 10 operadoras com maiores despesas nessa categoria no último ano?`

### -> Python com Flask

Para o último teste, utilizei Python com Flask no backend, a api possui 2 endpoints:

`/api/dados` - retorna todos os dados sem uma filtragem, é a requisição feita quando o usuário entra na aplicação pela primeira vez.

`/api/busca/<query>` - retorna resultados relevantes com a query pesquisada, que pode ser qualquer coisa relevante a pesquisa, como:
Registro ANS,CNPJ, Razao Social Nome Fantasia, Modalidade, Logradouro,
Número,
Complemento,
Bairro,
Cidade,
UF,
CEP,
DDD,
Telefone,
Endereco eletrônico ou
Representante.

## ❗ Caso não possua as bibliotecas, rodar o seguinte comando dentro da pasta da api:

```python
pip install flask flask-cors psycopg2-binary python-dotenv
```

### Vue e Typescript

No frontend utilizei o Vue com o Vuetify para criação e customização da tabela. Também utilizei o Typescript para uma melhor tipagem dos dados e, para fazer a conexão dos dados com o backend, utilizei o Axios.

No frontend é possivel filtrar clicando no header das células `Modalidade`, `Cidade` e `UF`,

Escolhi apenas as colunas CNPJ, RAZÃO SOCIAL, MODALIDADE, CIDADE E UF para uma melhor visualização dos dados, porém sendo facilmente possivel adicionar outras colunas para uma visualização mais detalhada.

## Variáveis de Ambiente

Para rodar o projeto, você vai precisar adicionar as seguintes variáveis de ambiente em um .env para o banco de dados da API:

`DB_HOST`
`DB_NAME`
`DB_USER`
`DB_PASSWORD`

## Demonstração

https://youtu.be/GGtOxh29lOs

Nesse link possui um vídeo mostrando as funcionalidades mencionadas.
