# Sistema de Estoque

API REST para gerenciamento de produtos e movimentações de estoque, desenvolvida com Python e FastAPI.

## Funcionalidades

- Cadastro, consulta, atualização e exclusão de produtos
- SKU único por produto
- Categorias, preço e estoque mínimo
- Entradas e saídas de estoque
- Bloqueio de saída acima do estoque disponível
- Histórico de movimentações
- Validação automática com Pydantic
- Banco SQLite com SQLAlchemy
- Documentação Swagger

## Tecnologias

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

## Instalação

```bash
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
```

## Executar

```bash
uvicorn app.main:app --reload
```

Acesse a documentação em:

```text
http://127.0.0.1:8000/docs
```

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
  "price": 89.9,
  "quantity": 10,
  "minimum_stock": 3
}
```

## Exemplo de movimentação

Entrada:

```json
{
  "movement_type": "entry",
  "quantity": 5
}
```

Saída:

```json
{
  "movement_type": "exit",
  "quantity": 2
}
```

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

## Próximas melhorias

- Testes automatizados
- Filtro por categoria e estoque baixo
- Autenticação de usuários
- Migrações com Alembic
- Interface web
- Docker e deploy
