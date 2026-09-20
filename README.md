# Sistema de Estoque

API REST para gerenciamento de produtos e movimentações de estoque, criada com Python e FastAPI.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00)](https://www.sqlalchemy.org/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)](#roadmap)

## Sobre o projeto

Sistema de portfólio para controlar produtos, quantidades e movimentações de entrada e saída de estoque.

## Funcionalidades

- Cadastro, consulta, atualização e exclusão de produtos
- SKU único por produto
- Categorias, preço e estoque mínimo
- Entradas e saídas de estoque
- Bloqueio de saída acima do estoque disponível
- Histórico de movimentações
- Validação automática com Pydantic
- Banco SQLite com SQLAlchemy
- Documentação interativa com Swagger

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.10+ | Linguagem principal |
| FastAPI | API REST e documentação |
| SQLAlchemy | ORM e persistência |
| SQLite | Banco de dados local |
| Pydantic | Validação dos dados |
| Pytest | Testes planejados |

## Como executar

```bash
git clone -b feature/estoque-inicial https://github.com/FerSigma0301/sistema-estoque-python.git
cd sistema-estoque-python
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse a documentação em `http://127.0.0.1:8000/docs`.

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está online |
| GET | `/health` | Health check |
| POST | `/products/` | Cadastra produto |
| GET | `/products/` | Lista produtos |
| GET | `/products/{product_id}` | Busca produto |
| PUT | `/products/{product_id}` | Atualiza produto |
| DELETE | `/products/{product_id}` | Exclui produto |
| POST | `/products/{product_id}/movements` | Registra entrada ou saída |
| GET | `/products/{product_id}/movements` | Lista movimentações |

## Exemplo de produto

```json
{
  "name": "Teclado USB",
  "sku": "TEC-001",
  "category": "Periféricos",
  "price": 89.90,
  "quantity": 10,
  "minimum_stock": 3
}
```

## Exemplo de movimentação

```json
{
  "movement_type": "entry",
  "quantity": 5
}
```

Para uma saída, use `"movement_type": "exit"`.

## Estrutura

```text
app/
├── database.py
├── main.py
├── models.py
├── schemas.py
└── routes/
    ├── products.py
    └── movements.py
```

## Roadmap

- [ ] Testes automatizados
- [ ] Filtro por categoria e estoque baixo
- [ ] Autenticação de usuários
- [ ] Migrações com Alembic
- [ ] Interface web
- [ ] Docker e deploy

## Licença

Este projeto está sob a licença MIT.
