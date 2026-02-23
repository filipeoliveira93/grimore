# Pasta `.grimore/` — Contexto do Projeto

Esta pasta é o **cérebro do seu projeto Grimore**. Ela é criada e gerenciada pelos agentes do Grimore ao longo do desenvolvimento.

> 💡 **Recomendação:** Faça commit desta pasta no seu repositório. Ela contém toda a documentação viva do projeto e garante consistência entre sessões de AI e entre membros da equipe.

---

## Arquivos e Significado

| Arquivo/Pasta | Criado por | Descrição |
|---------------|-----------|-----------|
| `project.md` | `scope-architect` | Escopo, visão, "Estrela Guia" e fronteiras do projeto |
| `requirements.md` | `requirements-engineer` | Stack técnico, requisitos funcionais (FR) e não-funcionais (NFR) |
| `context.md` | Qualquer agente | Decisões arquiteturais, aprendizados e estado global |
| `rules/business-rules.md` | `business-rule-extractor` | Regras de negócio extraídas do código |
| `features/[slug]/` | `feature-manager` | Pasta por feature com marcos e tarefas |
| `features/[slug]/index.md` | `feature-manager` | Visão geral: escopo, requisitos mapeados, aceite |
| `features/[slug]/state.md` | `feature-manager` | Status atual, bloqueios e próximas ações |
| `features/[slug]/MT01.md` | `feature-manager` | Marco executável com tarefas e Definition of Done |
| `logs/executions/` | `implementation-coder` | Logs de execução de cada tarefa |
| `logs/reviews/` | `quality-reviewer` | Relatórios de revisão de código |
| `logs/archive/` | `release-manager` | Logs arquivados de marcos fechados |

---

## Ciclo de Vida

```
Projeto Novo               Projeto Existente
     │                           │
     ▼                           ▼
scope-architect      brownfield-setup
     │                           │
     └───────────┬───────────────┘
                 ▼
     requirements-engineer
                 │
                 ▼
         feature-manager
                 │
         ┌───────┴────────┐
         ▼                ▼
  sdd-implementation   test-engineer
       -coder               │
         │                  │
         └───────┬──────────┘
                 ▼
       quality-reviewer
                 │
                 ▼
       release-manager
```

---

## Esta pasta não existe ainda?

Normal! Ela é criada automaticamente quando você inicia o fluxo Grimore com o `scope-architect`:

```
Use a skill scope-architect para iniciar meu projeto
```
