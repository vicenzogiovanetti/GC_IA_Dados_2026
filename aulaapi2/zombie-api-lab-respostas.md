# Zombie API Lab — respostas

**Estudante:** vicenzoteste1
**Data de exportação:** 28/10/2026
**Progresso:** 7 de 16 missões

> Laboratório didático: requisições simuladas no navegador; código Python sujeito a execução e revisão em ambiente real.

## Missão 01 — O servidor está vivo?

**Etapa:** Explorar o Swagger
**Objetivo:** Execute GET / e identifique o status de sucesso.
**Situação:** Concluída

**Requisição:** `GET /`
**Status HTTP:** 200

**Resposta do simulador:**

```json
{
  "mensagem": "Bem-vindo ao Zombie API Lab!",
  "docs": "/docs"
}
```

**Minha resposta / o que aprendi:**

status 200

---

## Missão 02 — Encontre os filmes

**Etapa:** Explorar o Swagger
**Objetivo:** Execute GET /filmes e veja quantos filmes há.
**Situação:** Concluída

**Requisição:** `GET /filmes`
**Status HTTP:** 200

**Resposta do simulador:**

```json
[
  {
    "id": 1,
    "titulo": "A Última Meia-Noite",
    "genero": "zumbi",
    "ano": 2022,
    "nota": 8.1
  },
  {
    "id": 2,
    "titulo": "O Trem dos Mortos",
    "genero": "zumbi",
    "ano": 2023,
    "nota": 7.6
  },
  {
    "id": 3,
    "titulo": "A Mansão das Sombras",
    "genero": "fantasma",
    "ano": 2019,
    "nota": 8.5
  },
  {
    "id": 4,
    "titulo": "O Chamado da Lua",
    "genero": "lobisomem",
    "ano": 2021,
    "nota": 7.2
  },
  {
    "id": 5,
    "titulo": "Espelhos do Além",
    "genero": "fantasma",
    "ano": 2020,
    "nota": 6.9
  }
]
```

**Minha resposta / o que aprendi:**

status 200

---

## Missão 03 — Um filme específico

**Etapa:** Explorar o Swagger
**Objetivo:** Execute GET /filmes/2 e encontre o título retornado.
**Situação:** Concluída

**Requisição:** `GET /filmes/2`
**Status HTTP:** 200

**Resposta do simulador:**

```json
{
  "id": 2,
  "titulo": "O Trem dos Mortos",
  "genero": "zumbi",
  "ano": 2023,
  "nota": 7.6
}
```

**Minha resposta / o que aprendi:**

consulta o filme trem dos mortos

---

## Missão 04 — Só filmes de zumbi

**Etapa:** Explorar o Swagger
**Objetivo:** Use GET /filmes com genero=zumbi.
**Situação:** Concluída

**Requisição:** `GET /filmes?genero=zumbi`
**Status HTTP:** 200

**Resposta do simulador:**

```json
[
  {
    "id": 1,
    "titulo": "A Última Meia-Noite",
    "genero": "zumbi",
    "ano": 2022,
    "nota": 8.1
  },
  {
    "id": 2,
    "titulo": "O Trem dos Mortos",
    "genero": "zumbi",
    "ano": 2023,
    "nota": 7.6
  }
]
```

**Minha resposta / o que aprendi:**

consulta são filmes com genero zumbi

---

## Missão 05 — O filme desaparecido

**Etapa:** Explorar o Swagger
**Objetivo:** Consulte GET /filmes/99. Qual status aparece?
**Situação:** Concluída

**Requisição:** `GET /filmes/99`
**Status HTTP:** 404

**Resposta do simulador:**

```json
{
  "detail": "Filme não encontrado"
}
```

**Minha resposta / o que aprendi:**

erro 404

---

## Missão 06 — Minha primeira FastAPI

**Etapa:** Criar a API
**Objetivo:** Importe FastAPI, crie app e devolva um dicionário em GET /.
**Situação:** Em andamento

**Código Python:**

```python
from fastapi import FastAPI

app = FastAPI()


```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 07 — Disponibilizar a lista

**Etapa:** Criar a API
**Objetivo:** Crie GET /filmes com uma função que devolva a variável filmes.
**Situação:** Em andamento

**Código Python:**

```python
filmes = [{"id": 1, "titulo": "A Última Meia-Noite"}]


```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 08 — Buscar pelo ID

**Etapa:** Criar a API
**Objetivo:** Crie GET /filmes/{filme_id}, receba filme_id: int e devolva um dicionário.
**Situação:** Em andamento

**Código Python:**

```python
@app.get("/filmes/{filme_id}")

```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 09 — Preparar o POST

**Etapa:** Criar a API
**Objetivo:** Crie a classe NovoFilme(BaseModel) com titulo: str e nota: float.
**Situação:** Em andamento

**Código Python:**

```python
from pydantic import BaseModel


```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 10 — Receber um filme por POST

**Etapa:** Criar a API
**Objetivo:** Crie POST /filmes com uma função que receba NovoFilme e devolva os dados.
**Situação:** Em andamento

**Código Python:**

```python
@app.post("/filmes")

```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 11 — Cadastre um novo terror

**Etapa:** Testar a API
**Objetivo:** Execute POST /filmes com título A Névoa do Pântano e nota válida.
**Situação:** Concluída

**Requisição:** `POST /filmes`
**Status HTTP:** 201

**Resposta do simulador:**

```json
{
  "titulo": "A Névoa do Pântano",
  "genero": "zumbi",
  "ano": 2026,
  "nota": 8.8,
  "id": 6
}
```

**Minha resposta / o que aprendi:**

código 201 envia um json com os dados de um novo filme com o titulo a névoa do pantano

---

## Missão 12 — Cadastre e consulte

**Etapa:** Testar a API
**Objetivo:** Consulte o filme que acabou de cadastrar com GET /filmes/{id}.
**Situação:** Concluída

**Requisição:** `GET /filmes/6`
**Status HTTP:** 200

**Resposta do simulador:**

```json
{
  "titulo": "A Névoa do Pântano",
  "genero": "zumbi",
  "ano": 2026,
  "nota": 8.8,
  "id": 6
}
```

**Minha resposta / o que aprendi:**

código 200

---

## Missão 13 — A nota impossível

**Etapa:** Testar a API
**Objetivo:** Envie POST /filmes com nota 12 e observe o erro 422.
**Situação:** Em andamento

**Requisição:** ainda não registrada no simulador.

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 14 — Consuma uma API

**Etapa:** Consumir e conectar
**Objetivo:** No cliente simulado, consulte GET /resumo e identifique total_filmes.
**Situação:** Em andamento

**Requisição:** ainda não registrada no simulador.

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 15 — Cliente com Requests

**Etapa:** Consumir e conectar
**Objetivo:** Use requests.get("http://127.0.0.1:8000/resumo") e resposta.json().
**Situação:** Em andamento

**Código Python:**

```python
import requests


```

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Missão 16 — API é inteligência artificial?

**Etapa:** Consumir e conectar
**Objetivo:** Envie POST /perguntar e observe o campo usa_ia.
**Situação:** Em andamento

**Requisição:** ainda não registrada no simulador.

**Minha resposta / o que aprendi:**

_Não preenchido._

---

## Observação final

As APIs permitem que aplicações consultem ou enviem dados para serviços. O laboratório ilustra esses conceitos, mas o simulador não executa código Python nem acessa uma API externa.
