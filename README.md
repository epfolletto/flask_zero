# Flask_zero
Repositório de estudos relacionados ao Flask. Tecnologias utilizadas:
- Framework: Flask
- Banco de dados: PostgreSQL
- Biblioteca de ORM: SQLAlchemy
- Gerenciamento de versões: Alembic
- Autenticação/autorização: Flask-JWT-Extended
- Rotas e módulos: Blueprints
- Validação de dados: Pydantic

## Pré-requisitos
Certifique-se de ter os seguintes itens instalados em sua máquina:
- Python 3.x
- PostgreSQL
- Poetry

## Início
- Clonar o repositório:
  
```
git clone https://github.com/epfolletto/flask_zero.git
```

- Instalar as dependências, utilizando [Poetry](https://python-poetry.org/):
  
```
cd flask_zero && poetry install
```

## Banco de dados
- Criar banco de dados no PostgreSQL:

```
export DATABASE_URL=postgresql://usuario:senha@localhost:5432/meu_banco
```
  
- Executar as migrações:
  
```
alembic upgrade head
```

## Rodar o projeto
- Para iniciar o projeto:
  
```
make run (poetry run flask run)
```
