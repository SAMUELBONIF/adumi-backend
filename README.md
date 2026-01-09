# ADUMI Backend

API REST para o sistema de vendas ADUMI, responsável pelo gerenciamento de produtos, clientes, vendas e itens de venda.  
Garante integridade dos dados, incluindo regras de negócio como impedir a exclusão de produtos associados a vendas.

---

## Tecnologias Utilizadas

- Python 3.10  
- Django 5.2  
- Django REST Framework  
- SQLite  

---

## Funcionalidades

- Listar, criar, atualizar e excluir **produtos** (com proteção para produtos associados a vendas).  
- Listar, criar, atualizar e excluir **clientes**.  
- Registrar **vendas** e seus **itens de venda**, associando produtos e clientes.  
- Consultar itens de venda com informações detalhadas de produto e cliente.

---

## Endpoints

| Verbo HTTP | Caminho                      | Descrição                               |
|------------|------------------------------|-----------------------------------------|
| POST       | /ADUMI/api/produtos/         | Criar produto                            |
| GET        | /ADUMI/api/produtos/         | Listar produtos                          |
| GET        | /ADUMI/api/produtos/{id}/    | Visualizar produto específico            |
| PUT/PATCH  | /ADUMI/api/produtos/{id}/    | Atualizar produto                        |
| DELETE     | /ADUMI/api/produtos/{id}/    | Excluir produto (restrição a vendas)     |
| POST       | /ADUMI/api/clientes/         | Criar cliente                            |
| GET        | /ADUMI/api/clientes          | Listar Clientes                          |
| GET        | /ADUMI/api/clientes/{id}     | Visualizar cliente especifico            |
| PUT/PATCH  | /ADUMI/api/clientes/{id}/    | Atualizar cliente                        |
| DELETE     | /ADUMI/api/clients/{id}/     | Excluir cliente (restrição a vendas)     |
| POST       | /ADUMI/api/vendas/           | Criar venda                              |
| GET        | /ADUMI/api/vendas/           | Listar Vendas                            |
| GET        | /ADUMI/api/vendas/{id}/      | Visualizar venda específica              |
| PUT/PATCH  | /ADUMI/api/vendas/{id}/      | Atualizar vendas                         |
| DELETE     | /ADUMI/api/vendas/{id}/      | Excluir venda (restrição a itenvenda)     |
| GET        | /ADUMI/api/itenvenda/        | Listar itens de venda com produto e cliente |


---

## Configuração e Teste

1. Clone o repositório:
 git clone https://github.com/seu-usuario/adumi-backend.git
 cd adumi-backend

2.Criar e ativar ambiente virtual:
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3.Instalar dependências:
pip install -r requirements.txt


4.Migrar o banco de dados:
python manage.py migrate

5.Rodar servidor de desenvolvimento
python manage.py runserver

6.Teste a API no navegador ou via Postman:
http://127.0.0.1:8000/ADUMI/api/itenvenda/

Contribuição
Sinta-se à vontade para contribuir abrindo um issue ou enviando um pull request.

Licença

Licenciado sob a Licença MIT.
