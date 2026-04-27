---
description: Placeholder — workflows compostos ainda não implementados nesta versão.
---

# Workflows Compostos (Em Desenvolvimento)

Esta pasta é reservada para **workflows multi-agente** que orquestram sequências completas de skills automaticamente.

**Status atual:** não implementado. Use o fluxo manual descrito em `agents.md`.

## O que será aqui no futuro

Workflows são sequências pré-definidas de skills que executam um fluxo completo sem intervenção manual em cada etapa. Exemplos planejados:

| Workflow | Descrição |
|---|---|
| `greenfield-setup` | `gmr-scope-architect` → `gmr-requirements-engineer` → `gmr-feature-manager` em sequência |
| `full-cycle` | Implementação completa de uma tarefa: coder → QA → release |
| `security-review` | `gmr-security-auditor` → `gmr-pentester-expert` → relatório consolidado |

## Como criar um workflow

Até que haja suporte nativo, workflows podem ser simulados instruindo o agente:

```
Execute o fluxo completo: use gmr-scope-architect, depois gmr-requirements-engineer, depois gmr-feature-manager.
```
