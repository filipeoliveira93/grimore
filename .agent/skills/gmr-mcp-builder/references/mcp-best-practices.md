# MCP Best Practices — Diretrizes Universais de Qualidade

> Consulte este guia durante a Fase 1 (Pesquisa & Planejamento) e a Fase 3 (Revisão).

---

## Nomenclatura de Servidores e Ferramentas

### Servidores
- Use nomes kebab-case descritivos: `github-mcp`, `slack-mcp`, `postgres-mcp`
- Inclua o nome do serviço integrado no nome do servidor
- Evite abreviações que não sejam universalmente conhecidas

### Ferramentas
Use prefixo do serviço + verbo de ação + recurso:

| ✅ Bom | ❌ Ruim |
|---|---|
| `github_create_issue` | `create`, `make_issue` |
| `github_list_repos` | `list`, `get_stuff` |
| `slack_send_message` | `send`, `msg` |
| `postgres_execute_query` | `query`, `run_sql` |

**Verbos recomendados:** `create`, `list`, `get`, `update`, `delete`, `search`, `send`, `execute`

---

## Descrições de Ferramentas

Uma boa descrição de ferramenta responde **em uma frase**: "O que faz?" e "Quando usar?"

**Formato recomendado:**
```
[Ação] [recurso] [contexto/quando usar]. [Detalhes de input/output relevantes].
```

**Exemplos:**
- ✅ `"Lista repositórios de uma organização GitHub. Retorna nome, URL, visibilidade e última atualização. Use para descobrir repos antes de criar issues ou PRs."`
- ❌ `"Lista repos"` — muito vago
- ❌ `"Esta ferramenta pode ser usada para listar os repositórios..."` — verbose desnecessariamente

---

## Schemas de Input (Zod/TypeScript)

Inclua sempre:
1. **Descrição** em cada campo — o agente precisa entender o propósito
2. **Exemplos** em campos não óbvios
3. **Restrições** explícitas (min/max, enums, formatos)

```typescript
z.object({
  owner: z.string()
    .describe("Nome do usuário ou organização GitHub. Ex: 'torvalds' ou 'microsoft'"),
  
  repo: z.string()
    .describe("Nome do repositório (sem o owner). Ex: 'linux' ou 'TypeScript'"),
  
  state: z.enum(['open', 'closed', 'all'])
    .default('open')
    .describe("Estado das issues a filtrar"),
  
  per_page: z.number()
    .min(1).max(100)
    .default(30)
    .describe("Número de resultados por página (1-100)")
})
```

---

## Respostas de Ferramentas

### Formato: JSON vs Markdown

| Use JSON quando... | Use Markdown quando... |
|---|---|
| Dados serão processados por outro agente | Resultado será lido pelo usuário |
| Há estrutura hierárquica clara | Há conteúdo textual longo |
| Precisão é mais importante que legibilidade | Legibilidade é mais importante |

### Estrutura de Resposta Recomendada (TypeScript SDK)

```typescript
return {
  content: [{
    type: "text",
    text: JSON.stringify(result, null, 2)  // Para dados estruturados
  }],
  structuredContent: result  // Disponibilize dados estruturados quando possível
};
```

### Tamanho de Resposta
- **Evite respostas massivas** — filtrar e paginar é mais eficiente
- **Paginar por padrão** — inclua `limit/offset` ou `cursor` em listas
- **Resumir quando possível** — retorne campos relevantes, não o objeto inteiro

---

## Mensagens de Erro

Erros devem guiar o agente automaticamente em direção à solução:

```typescript
// ❌ Ruim — genérico
throw new Error("Falha na operação");

// ✅ Bom — acionável
throw new Error(
  `Repository '${owner}/${repo}' not found. ` +
  `Verify the owner and repo names, then try github_list_repos to see available repositories.`
);

// ✅ Bom — com sugestão de próximo passo
throw new Error(
  `Rate limit exceeded (remaining: 0, resets at ${resetTime}). ` +
  `Wait until ${resetTime} or use a different authentication token.`
);
```

**Estrutura ideal de mensagem de erro:**
1. O que falhou (específico, não genérico)
2. Por que falhou (quando identificável)
3. Como corrigir (próximo passo sugerido)

---

## Segurança e Boas Práticas

### Autenticação
- **Nunca hardcode** tokens ou credenciais no código
- Use variáveis de ambiente: `process.env.GITHUB_TOKEN`
- Valide presença do token na inicialização do servidor, não na ferramenta

```typescript
const token = process.env.GITHUB_TOKEN;
if (!token) {
  throw new Error("GITHUB_TOKEN environment variable is required");
}
```

### Anotações de Ferramenta
Sempre declare honestamente o comportamento:

```typescript
annotations: {
  readOnlyHint: false,    // true se só lê, não modifica
  destructiveHint: true,  // true se pode causar perda de dados
  idempotentHint: false,  // true se repetir produz o mesmo resultado
  openWorldHint: true     // true se interage com serviços externos
}
```

### Operações Destrutivas
Para operações que deletam/sobrescrevem dados:
1. Inclua `destructiveHint: true` nas anotações
2. Adicione parâmetro de confirmação quando possível
3. Documente claramente as consequências na descrição da ferramenta

---

## Transporte

| Caso de Uso | Transporte Recomendado |
|---|---|
| Servidor remoto (produção) | HTTP Streamable stateless |
| Servidor local (desenvolvimento) | stdio |
| Integração com ferramentas CLI | stdio |

### HTTP Stateless — Por que preferir
- Mais fácil de escalar (sem sessões)
- Mais simples de debugar
- Compatível com load balancers padrão
- Sem problemas de reconnect

---

## Paginação

Implemente paginação em **toda** ferramenta que retorna listas:

```typescript
// Schema com paginação
z.object({
  cursor: z.string().optional()
    .describe("Cursor para a próxima página (retornado na resposta anterior)"),
  limit: z.number().min(1).max(100).default(20)
    .describe("Número máximo de resultados (1-100)")
})

// Resposta com metadados de paginação
return {
  items: results,
  next_cursor: hasMore ? encodeCursor(lastItem) : null,
  total_count: totalCount,
  has_more: hasMore
};
```
