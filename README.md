# 📚 API de Livros com Python Puro

Este é um projeto de uma API simples desenvolvida em **Python puro (sem frameworks)** que permite listar e adicionar livros via requisições HTTP. O projeto foi criado com foco em aprendizado de:
- Estrutura básica de APIs REST
- Manipulação de JSON
- Rotas GET e POST
- CI/CD com GitHub Actions
- Deploy automatizado via Render

---

## 🚀 Funcionalidades da API

| Método | Rota         | Descrição                                 |
|--------|--------------|-------------------------------------------|
| GET    | /books       | Retorna todos os livros cadastrados       |
| GET    | /books/<id>  | Retorna um livro específico pelo ID       |
| POST   | /books       | Adiciona um novo livro                    |

---

## 🔧 Exemplo de uso

### ▶️ GET /books

**Resposta esperada:**
```json
[
  { "id": 1, "title": "1984", "author": "George Orwell" },
  { "id": 2, "title": "Brave New World", "author": "Aldous Huxley" }
]
