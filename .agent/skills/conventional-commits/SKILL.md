---
name: conventional-commits
description: >
  Skill para documentacao de commits seguindo o padrao Conventional Commits v1.0.0.
  Use esta skill quando o usuario pedir para: gerar uma mensagem de commit, formatar
  um commit, revisar/corrigir uma mensagem de commit existente, criar entradas no
  CHANGELOG, ou documentar alteracoes de codigo no padrao conventional commits.
  Gatilhos tipicos: "gera o commit", "formata o commit", "cria a mensagem de commit",
  "atualiza o CHANGELOG", "documenta as mudancas".
---

# Conventional Commits

Skill para gerar mensagens de commit e entradas de CHANGELOG no padrao [Conventional Commits v1.0.0](https://www.conventionalcommits.org/).

Para a referencia completa de tipos, escopos, breaking changes e exemplos, leia `references/spec.md`.

---

## Formato base

```
<tipo>[escopo opcional]: <descricao curta>

[corpo opcional]

[footer(s) opcionais]
```

**Regras obrigatorias:**
- Linha de assunto: max **72 caracteres**
- `<descricao curta>` em **imperativo, minusculo, sem ponto final**
- Corpo separado do assunto por **linha em branco**
- Tipos validos: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

---

## Fluxo de geracao de commit

1. **Analisar as alteracoes** - examine o diff ou a descricao fornecida pelo usuario
   - Identifique o **tipo** que melhor descreve o impacto principal (consulte `references/spec.md` para a tabela de tipos)
   - Identifique o **escopo** (modulo, componente, arquivo) se for relevante
   - Verifique se ha **breaking change** (API incompativel, renomeacao, remocao de funcionalidade)

2. **Montar a mensagem**
   - Tipo unico por commit. Se as alteracoes misturarem tipos, sugira dividir os commits
   - Breaking change: adicione `!` apos o tipo/escopo **e** inclua `BREAKING CHANGE: <descricao>` no footer
   - Corpo: explique o **"por que"**, nao o "o que" (o codigo ja mostra o que mudou)
   - Referencie issues no footer: `Closes #123`, `Fixes #456`, `Refs #789`

3. **Apresentar ao usuario**
   - Exiba a mensagem formatada em bloco de codigo
   - Se houver ambiguidade (ex.: poderia ser `feat` ou `refactor`), explique a escolha
   - Oferea alternativas apenas se a diferenca for significativa

---

## Fluxo de atualizacao de CHANGELOG

Quando o usuario pedir para atualizar o `CHANGELOG.md`:

1. Leia o arquivo `CHANGELOG.md` existente para identificar o formato atual
2. Localize a secao `## [Unreleased]` (crie-a se nao existir, logo abaixo do titulo)
3. Insira a entrada na subsecao correta de acordo com o tipo do commit:

| Tipo do commit | Subsecao no CHANGELOG |
|---|---|
| `feat` | `### Adicionado` |
| `fix` | `### Corrigido` |
| `docs` | `### Documentacao` |
| `perf` | `### Desempenho` |
| `refactor` | `### Alterado` |
| `build`, `ci` | `### Infraestrutura` |
| `chore`, `style`, `test` | `### Manutencao` |
| `revert` | `### Revertido` |
| breaking change | `### Quebra de Compatibilidade` |

4. Formato de cada entrada: `- <descricao> ([#PR ou #issue](<link>))` (link opcional)
5. Mantenha a ordem cronologica inversa dentro de cada subsecao (mais recente primeiro)

---

## Exemplos rapidos

**Simples:**
```
feat(auth): add JWT-based authentication
```

**Com corpo e issue:**
```
fix(api): correct pagination offset on empty results

Without this fix the API returned page 2 data when requesting page 1
after a filter that yields zero results.

Closes #234
```

**Breaking change:**
```
feat(config)!: rename DATABASE_URL to DB_CONNECTION_STRING

BREAKING CHANGE: The environment variable DATABASE_URL has been renamed
to DB_CONNECTION_STRING. Update all deployment configs and .env files.
```

Para mais exemplos e detalhes completos da especificacao, consulte `references/spec.md`.
