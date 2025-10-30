# 🐳 Gerenciador de Tarefas — API com Docker e FastAPI

## 📘 Introdução

Este projeto tem como objetivo consolidar conhecimentos em **Dockerfile**, **Docker Compose**, **redes** e **volumes**.  
Foi desenvolvida uma **API de Gerenciamento de Tarefas (CRUD)** com **persistência de dados** em banco de dados relacional e **configuração segura via variáveis de ambiente**.

---

## 🚀 Funcionalidades

- Criar, listar, atualizar e excluir tarefas (CRUD completo)
- Persistência de dados em banco de dados relacional
- Comunicação entre containers (app + banco)
- Variáveis de ambiente configuráveis
- Volume para persistência do banco de dados
- Usuário dedicado no banco (sem uso do root)
- Totalmente containerizado via **Docker Compose**

---



---

## ⚙️ Configuração do Ambiente

### 🔐 Arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o conteúdo:

```env
# Configurações do Banco de Dados
DB_USER=app_user
DB_PASSWORD=securepassword
DB_NAME=tasks_db
DB_HOST=db
DB_PORT=5432

# Configurações da Aplicação
APP_PORT=5000
```

---

## 🐋 Execução do Projeto

### 1️⃣ Construir e iniciar os containers
```bash
docker compose up -d --build
```

### 2️⃣ Verificar se estão rodando
```bash
docker ps
```

Você deverá ver algo como:
```
meu_projetopython-app-1
meu_projetopython-db-1
```

---

## 🧠 Endpoints da API

A API ficará disponível em:  
👉 `http://localhost:5000`

| Método | Endpoint | Descrição |
|---------|-----------|-----------|
| `POST` | `/tasks/` | Cria uma nova tarefa |
| `GET` | `/tasks/` | Lista todas as tarefas |
| `GET` | `/tasks/{id}` | Obtém uma tarefa pelo ID |
| `PUT` | `/tasks/{id}` | Atualiza uma tarefa existente |
| `DELETE` | `/tasks/{id}` | Exclui uma tarefa |

---

## 🧪 Testando com Insomnia

1. Abra o **Insomnia**  
2. Crie uma nova **collection** chamada “Gerenciador de Tarefas”
3. Adicione os seguintes requests:

### ➕ Criar tarefa
`POST http://localhost:5000/tasks/`
```json
{
  "title": "Estudar Docker",
  "description": "Finalizar desafio de containers"
}
```

### 📋 Listar tarefas
`GET http://localhost:5000/tasks/`

### ✏️ Atualizar tarefa
`PUT http://localhost:5000/tasks/1`
```json
{
  "title": "Estudar Docker e FastAPI",
  "description": "Finalizar o desafio prático",
  "completed": true
}
```

### ❌ Deletar tarefa
`DELETE http://localhost:5000/tasks/1`

---

## 💾 Persistência de Dados (Volumes)

O volume configurado no `docker-compose.yml` garante que os dados sejam mantidos mesmo após reiniciar os containers:

```yaml
volumes:
  db_data:
```

- Local do volume dentro do container: `/var/lib/postgresql/data`
- Dados permanecem mesmo após `docker compose down`

---

## 🌐 Rede Customizada

A comunicação entre os containers é feita por uma rede interna do Docker definida no `docker-compose.yml`:

```yaml
networks:
  app_network:
    driver: bridge
```

---

## 🔒 Segurança

- O banco **não utiliza o usuário root**.  
- Um usuário `app_user` com senha segura foi criado no `.env`.
- Nenhum dado sensível está hardcoded no código-fonte.
- As variáveis de ambiente são injetadas no container pelo `docker-compose.yml`.

---

## 📜 Comandos Úteis

| Comando | Descrição |
|----------|------------|
| `docker compose up -d --build` | Inicia e constrói os containers |
| `docker compose down` | Para e remove os containers |
| `docker logs meu_projetopython-app-1` | Exibe logs da aplicação |
| `docker exec -it meu_projetopython-db-1 psql -U app_user -d tasks_db` | Acessa o banco de dados via terminal |
| `docker volume ls` | Lista os volumes ativos |
| `docker network ls` | Lista as redes configuradas |

---

## 🧾 Resultados Esperados — Validados ✅

| Requisito | Status |
|------------|---------|
| Multi-container funcional | ✅ |
| CRUD com persistência | ✅ |
| Volume configurado | ✅ |
| Variáveis de ambiente seguras | ✅ |
| Usuário sem root | ✅ |
| Documentação completa | ✅ |

---

## 👨‍💻 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Uvicorn**


