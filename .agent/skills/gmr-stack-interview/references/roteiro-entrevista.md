# Roteiro de Entrevista de Stack Tecnológica

## Princípios da Entrevista

### Seja Colaborativo (Não Impositivo)
A definição da stack é uma **decisão conjunta**. Seu papel:
1. **Ouvir** a preferência do usuário
2. **Avaliar** se a escolha é adequada ao escopo (consulte `project.md`)
3. **Discutir** prós e contras quando houver preocupações legítimas
4. **Decidir juntos** o que faz sentido para o projeto

### Exemplos de Diálogo

✅ **Colaborativo:**
> "Você mencionou MongoDB. Considerando que o projeto tem muitos relacionamentos entre entidades (ver `project.md`), um banco relacional como PostgreSQL poderia ajudar. O que você acha? Existe algum motivo específico para NoSQL?"

> "Entendo que quer usar React. Faz sentido! Para este projeto com muitos formulários, já pensou em alguma solução de gerenciamento de forms? Não precisamos decidir agora — apenas para manter no radar."

❌ **Evitar:**
> "MongoDB não é adequado. Use PostgreSQL." *(impositivo)*
> "Ok, MongoDB." *(passivo demais — sem análise)*

---

## Roteiro da Entrevista (4 Rodadas)

### Rodada 1: Frontend
> "Vamos definir a stack tecnológica. Começando pelo **Frontend**:
> 1. Qual framework/biblioteca planeja usar? (ou 'nenhum' se for apenas server-side)
> 2. Como planeja estilizar? (Pure CSS, Tailwind, Styled Components, etc.)
> 3. Vai precisar de gerenciamento de estado? Se sim, qual solução?"

### Rodada 2: Backend
> "Agora para o **Backend**:
> 1. Qual linguagem de programação?
> 2. Qual framework (se houver)?
> 3. Qual estilo de API? (REST, GraphQL, gRPC)
> 4. Como funcionará a autenticação? (JWT, OAuth, sessões, etc.)"

### Rodada 3: Dados
> "Sobre o **Banco de Dados**:
> 1. Qual banco de dados principal?
> 2. Vai usar algum ORM? Qual?
> 3. Como gerenciará as migrações?"

### Rodada 4: Infraestrutura *(opcional)*
> "Por fim, **Infraestrutura** (pode pular se ainda não souber):
> 1. Vai usar containers (Docker)?
> 2. Qual plataforma de CI/CD?
> 3. Onde planeja hospedar?"

---

## Tratamento de Respostas

| Resposta do Usuário | Ação |
|---|---|
| Tecnologia específica | Documentar como definido |
| "Não sei" / "TBD" | Documentar como `TBD` |
| "Nenhum" / "N/A" | Documentar como `N/A` |
| Tecnologia desconhecida | Aceitar e documentar (não questione) |
| Stack parcial (Brownfield) | Use `gmr-detect-manifest` para complementar |

---

## Template de Saída — `requirements.md`

```markdown
## 1. Stack Tecnológica

### Frontend
- **Framework:** [resposta ou TBD]
- **Estilização:** [resposta ou TBD]
- **Estado:** [resposta ou N/A]

### Backend
- **Linguagem:** [resposta]
- **Framework:** [resposta ou Nenhum]
- **API:** [REST / GraphQL / gRPC]
- **Autenticação:** [resposta ou TBD]

### Dados
- **Banco de Dados:** [resposta ou TBD]
- **ORM:** [resposta ou Nenhum]
- **Migrações:** [resposta ou TBD]

### Infraestrutura
- **Containers:** [resposta ou TBD]
- **CI/CD:** [resposta ou TBD]
- **Hospedagem:** [resposta ou TBD]
```

---

## Cenários Especiais

### Projeto Brownfield
1. Execute `gmr-detect-manifest` **antes** de fazer perguntas
2. Apresente ao usuário o que foi detectado automaticamente
3. Pergunte apenas sobre o que **não foi possível detectar**

### Mudança de Stack (Pivô)
1. Confirme o motivo da mudança
2. Avalie impacto no `project.md` e nos requisitos existentes
3. Documente a stack anterior com data de deprecação
4. Atualize o `requirements.md` com a nova stack

### Stack Parcial (apenas Frontend ou apenas Backend)
- Pule as rodadas não aplicáveis ao escopo do projeto
- Marque as seções irrelevantes como `N/A` no output
