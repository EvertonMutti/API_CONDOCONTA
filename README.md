API de Produtos para CondoConta.
Esta API fornece endpoints para gerenciar produtos em um estoque.
A API é responsável por gerenciar a autenticação de usuários em uma aplicação web. As principais funcionalidades são a criação de novos usuários e a autenticação de usuários já existentes.

Endpoints:

    Criar Product:
    URL: POST /products/create/product
    Descrição: Cria um novo produto ao estoque.
    Parâmetros:
        name (str): O nome do produto.
        description (str): A descrição do produto.
        price (float): O preço do produto.
        quantity (int): A quantidade do produto no estoque.
    Retorno:
        product_id (int): O ID do produto.
        name (str): O nome do produto.
        description (str): A descrição do produto.
        price (float): O preço do produto.
        quantity (int): A quantidade do produto no estoque.
        created_at (str): A data e hora em que o produto foi criado.
        updated_at (str): A data e a hora em que o produto foi atualizado pela última vez.

    Detalhar Product:
    URL: GET /products/detail/product/{id}
    Descrição: Retorna os detalhes de um produto específico no estoque.
    Retorno:
        product_id (int): O ID do produto.
        name (str): O nome do produto.
        description (str): A descrição do produto.
        price (float): O preço do produto.
        quantity (int): A quantidade do produto no estoque.
        created_at (str): A data e hora em que o produto foi criado.
        updated_at (str): A data e a hora em que o produto foi atualizado pela última vez.

    Atualizar Product:
    URL: PUT /products/edit/product/{id}
    Parâmetros: O id do produto.
    Retorno:
        product_id (int): O ID do produto.
        name (str): O nome do produto.
        description (str): A descrição do produto.
        price (float): O preço do produto.
        quantity (int): A quantidade do produto no estoque.
        created_at (str): A data e hora em que o produto foi criado.
        updated_at (str): A data e a hora em que o produto foi atualizado pela última vez.

    Listar Product:
    URL: GET /products/list/products
    Descrição: Cria um novo produto ao estoque.
    Retorno:
        product_id (int): O ID do produto.
        name (str): O nome do produto.

    Remover Produto
    URL: DELETE /products/delete/product/{id}
    Descrição: Cria um novo produto ao estoque.
    Parâmetros: O id do produto.
    Retorno: Uma mensagem confirmando que o produto foi removido.

    Criar novo usuário
    URL: POST /User/signup
    Descrição: Cria um novo Usuario.
    Parâmetros:
        name (str): O nome do Usuario.
        email (str): O email do usuario.
        Password (float): A senha do usuario.
    Retorno: 
        status code 201
        name (str): O nome do Usuario.
        email (str): O email do usuario.
    
    Login para gerar Token:
    URL: POST /User/Login
    Descrição: Cria um novo Usuario.
    Parâmetros:
        email (str): O email do usuario.
        Password (float): A senha do usuario.
    Retorno: 
        email (str): O nome do Usuario.
        token (str): O token do usuario.

Como utilizar:

1º crie uma database no mysqlworkbench com o nome de bancolegal e teste, o comando é: create database bancolegal; create database teste;

para iniciar a aplicação, abra o terminal, e vá até a pasta local do projeto e siga os seguintes passos e seguintes comandos:

2º python create_database.py

3º uvicorn main:app

Obs: Deixei de brinde um docker-compose para subir um banco mysql, ai você pode testar.


