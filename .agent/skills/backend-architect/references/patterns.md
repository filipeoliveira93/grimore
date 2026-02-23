# Backend Design Patterns

## 📂 Clean Architecture & Domain-Driven Design (DDD)

A arquitetura deve ser centrada no domínio, isolando a lógica de negócio de preocupações técnicas (frameworks, bancos de dados).

### Dependency Rule
- As dependências devem apontar apenas para as camadas internas.
- **Entidades** não conhecem nada além de si mesmas.
- **Casos de Uso** conhecem Entidades, mas não conhecem Controllers ou Repositories.
- Use **Inversão de Dependência (DI)**: A camada de infraestrutura deve implementar interfaces definidas na camada de domínio.

### Camadas Recomendadas
1. **Domain (Core)**: Entidades e interfaces (ex: `IRepository`).
2. **Application (Use Cases)**: Lógica de negócio e orquestração.
3. **Infrastructure**: Implementação de DB, chamadas de API externas.
4. **Interface (Adapters)**: Controllers, DTOs e presenters.

---

## 🔐 Segurança (Mitigação OWASP)

### Autenticação e Autorização
- **JWT Best Practices**: Use `HttpOnly` e `Secure` cookies para armazenar tokens. Nunca em `localStorage`.
- **RBAC (Role-Based Access Control)**: Implemente autorização baseada em papéis em todas as rotas protegidas.
- **MFA**: Sempre que possível, sugira autenticação de dois fatores para ações críticas.

### Proteção de Dados
- **Sanitização de Entrada**: Valide e limpe todo input do usuário (Zod/Pydantic) antes de processar.
- **Parametrização de Queries**: NUNCA concatene strings em SQL. Use placeholders para evitar SQL Injection.
- **Criptografia**: Armazene senhas com algoritmos de derivação de chave fortes (Argon2id ou BCrypt com salt).

---

## 💾 Persistência e Performance

### Padrão Repository
- Isole a lógica de busca de dados da lógica de negócio.
- O repositório deve retornar modelos de domínio ou entidades, não objetos puros do DB.

### Otimização de Queries
- **Problema N+1**: Evite loops que fazem uma query para cada item de uma lista. Use `JOINs` ou `DataLoader`.
- **Paginação**: Sempre implemente paginação (preferencialmente baseada em cursor para grandes volumes).
- **Caching**: Use Redis/Upstash para dados lidos com frequência e que mudam raramente.

---

## 🛠️ Observabilidade e Erros

### Log Estruturado
- Use formato JSON para logs para facilitar a ingestão por logs aggregators (Datadog, ELK).
- Inclua metadados: `trace_id`, `user_id`, `environment`, `latency`.

### Tratamento de Erros de Negócio
- Diferencie erros de **validação** (400), **negócio** (422) e **infraestrutura** (500).
- Forneça mensagens de erro amigáveis para o cliente, mas logs detalhados (com stack trace) para os desenvolvedores.

---

## ✅ Checklist de Design
- [ ] O domínio está isolado de frameworks?
- [ ] Existe validação em TODAS as fronteiras da API?
- [ ] As senhas estão sendo armazenadas de forma segura?
- [ ] Foi implementado Rate Limiting para rotas públicas?
- [ ] As queries ao banco estão protegidas contra SQL Injection?
