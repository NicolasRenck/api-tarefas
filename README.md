# API de Tarefas

API REST para gerenciamento de tarefas pessoais, com autenticação JWT e controle de acesso por usuário.

Desenvolvida com **Django** e **Django REST Framework**.

---

## Tecnologias

- Python 3.13
- Django 6.0
- Django REST Framework
- PostgreSQL
- SimpleJWT — autenticação via token
- django-filter — filtros e busca
- drf-spectacular — documentação automática (Swagger)
- Docker + Docker Compose

---

## Como rodar localmente

### Com Docker (recomendado)

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
# Clone o repositório
git clone https://github.com/NicolasRenck/api-tarefas.git
cd api-tarefas

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas configurações

# Suba os containers
docker compose up --build

# Em outro terminal, rode as migrations
docker compose exec web python manage.py migrate

# (Opcional) Crie um superusuário
docker compose exec web python manage.py createsuperuser
```

A API estará disponível em `http://localhost:8000`.

### Sem Docker

**Pré-requisitos:** Python 3.13+ e PostgreSQL instalados.

```bash
git clone https://github.com/NicolasRenck/api-tarefas.git
cd api-tarefas

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

cp .env.example .env
# Edite o .env com as credenciais do seu banco

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Autenticação

A API utiliza **JWT (JSON Web Token)**. Para acessar os endpoints protegidos, é necessário incluir o token no header de cada requisição.

### Obtendo o token

```http
POST /api/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### Usando o token

```http
Authorization: Bearer <seu_access_token>
```

### Renovando o token

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "seu_refresh_token"
}
```

---

## Endpoints

### Tarefas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/tarefas/` | Lista todas as tarefas do usuário autenticado |
| `POST` | `/api/tarefas/` | Cria uma nova tarefa |
| `GET` | `/api/tarefas/{id}/` | Retorna os detalhes de uma tarefa |
| `PUT` | `/api/tarefas/{id}/` | Atualiza uma tarefa completa |
| `PATCH` | `/api/tarefas/{id}/` | Atualiza parcialmente uma tarefa |
| `DELETE` | `/api/tarefas/{id}/` | Remove uma tarefa |
| `POST` | `/api/tarefas/{id}/concluir/` | Marca uma tarefa como concluída |

### Filtros disponíveis

```
GET /api/tarefas/?concluida=true     # Filtra por status
GET /api/tarefas/?search=reunião     # Busca por título ou descrição
```

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/token/` | Obtém access e refresh token |
| `POST` | `/api/token/refresh/` | Renova o access token |

---

## Documentação interativa

Com o projeto rodando, acesse:

```
http://localhost:8000/api/docs/
```

Interface Swagger com todos os endpoints documentados e testáveis.

---

## Estrutura do projeto

```
api-tarefas/
├── api_app/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── api_tarefas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

## Segurança

Cada usuário tem acesso **apenas às suas próprias tarefas**. A API filtra automaticamente os dados pelo usuário autenticado, não é possível acessar ou modificar tarefas de outros usuários.

---


## Deploy

API em produção: https://api-tarefas-y7s7.onrender.com


## Documentação

Swagger UI: https://api-tarefas-y7s7.onrender.com/api/docs/


## Autenticação

A API usa JWT. Para testar:
1. Crie um usuário em `POST /api/register/`
2. Obtenha o token em `POST /api/token/`
3. Use o token no header: `Authorization: Bearer seu_token`


## Autor

**Nicolas Renck**  
[github.com/NicolasRenck](https://github.com/NicolasRenck)