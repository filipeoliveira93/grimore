# Especificacao: Conventional Commits v1.0.0

Referencia completa para uso com a skill `conventional-commits`.

---

## Tabela de Tipos

| Tipo | Quando usar | Aparece no CHANGELOG? |
|---|---|---|
| `feat` | Nova funcionalidade visivel ao usuario | Sim - Adicionado |
| `fix` | Correcao de bug visivel ao usuario | Sim - Corrigido |
| `docs` | Alteracoes somente em documentacao | Opcional |
| `style` | Formatacao, ponto-e-virgula, etc. (sem logica) | Nao |
| `refactor` | Refatoracao sem adicionar feature ou corrigir bug | Opcional |
| `perf` | Mudanca que melhora desempenho | Sim - Desempenho |
| `test` | Adicionar ou corrigir testes | Nao |
| `build` | Sistema de build ou dependencias externas | Sim - Infraestrutura |
| `ci` | Alteracoes em arquivos/scripts de CI/CD | Sim - Infraestrutura |
| `chore` | Outras tarefas de manutencao (nao afetam src/test) | Nao |
| `revert` | Reverter um commit anterior | Sim - Revertido |

---

## Regras de Escopo

- **Opcional** - use apenas quando adicionar clareza real
- Entre **parenteses**, em **minusculo**, sem espacos: `feat(auth):`, `fix(api/users):`
- Use o nome do modulo, componente, pacote ou arquivo (sem extensao)
- Seja consistente com os escopos ja usados no historico do projeto
- Evite escopos muito genericos (`core`, `app`) ou muito especificos (nome de funcao)

---

## Breaking Changes

Duas formas equivalentes (podem ser combinadas):

**Forma 1 - `!` na linha de assunto:**
```
feat(api)!: remove endpoint GET /v1/users/all
```

**Forma 2 - footer `BREAKING CHANGE:`:**
```
feat(api): remove endpoint GET /v1/users/all

BREAKING CHANGE: The GET /v1/users/all endpoint has been removed.
Use GET /v1/users with pagination parameters instead.
```

**Combinada (recomendada para mudancas criticas):**
```
feat(api)!: remove endpoint GET /v1/users/all

BREAKING CHANGE: The GET /v1/users/all endpoint has been removed.
Use GET /v1/users with pagination parameters instead.

Closes #89
```

---

## Estrutura Completa

```
<tipo>[escopo opcional][! opcional]: <descricao>
<linha em branco>
[corpo - paragrafo(s) explicando o porque]
<linha em branco>
[footer(s): um por linha]
```

### Footers validos

| Footer | Uso |
|---|---|
| `BREAKING CHANGE: <descricao>` | Quebra de compatibilidade |
| `Closes #<numero>` | Fecha issue ao fazer merge |
| `Fixes #<numero>` | Equivalente a Closes para bugs |
| `Refs #<numero>` | Referencia sem fechar |
| `Co-authored-by: Nome <email>` | Co-autoria |
| `Reviewed-by: Nome <email>` | Revisor |

---

## Exemplos Completos

### Commit simples sem escopo
```
docs: add contributing guide
```

### Commit com escopo
```
feat(checkout): add credit card payment option
```

### Commit com corpo
```
fix(auth): prevent session expiry on tab switch

Previously the session timer was reset on every focus event, causing
premature logouts when users switched tabs quickly. Now only genuine
idle periods trigger the timeout.
```

### Commit com escopo, corpo e footer
```
refactor(database): migrate from raw SQL to query builder

Using Knex.js simplifies parameterization and prevents SQL injection
without adding significant overhead. All existing tests pass.

Refs #102
Co-authored-by: Maria Silva <maria@example.com>
```

### Breaking change completo
```
feat(config)!: rename DATABASE_URL to DB_CONNECTION_STRING

Align environment variable naming with the project-wide DB_ prefix
convention established in the infrastructure team's standards.

BREAKING CHANGE: The environment variable DATABASE_URL has been renamed
to DB_CONNECTION_STRING. Update all deployment configs, CI variables,
and local .env files before upgrading.

Closes #310
```

### Revert
```
revert: feat(auth): add biometric login

Refs: a3f5c12
```

---

## Formato do CHANGELOG (Keep a Changelog)

```markdown
# Changelog

Todas as mudancas notaveis serao documentadas aqui.

## [Unreleased]

### Adicionado
- Descricao da nova funcionalidade (#PR)

### Corrigido
- Descricao do bug corrigido (#issue)

### Quebra de Compatibilidade
- `DATABASE_URL` renomeado para `DB_CONNECTION_STRING` (#310)

## [1.2.0] - 2026-02-23

### Adicionado
- ...

[Unreleased]: https://github.com/org/repo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/org/repo/releases/tag/v1.2.0
```

### Regras do CHANGELOG

1. Versoes em **ordem cronologica inversa** (mais recente no topo)
2. Data no formato **YYYY-MM-DD**
3. `[Unreleased]` sempre presente no topo para acumular mudancas
4. Ao lancar versao: renomeie `[Unreleased]` para `[X.Y.Z] - DATA` e crie novo `[Unreleased]` vazio
5. Links de comparacao ao final do arquivo (opcional mas recomendado)
