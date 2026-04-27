# Templates de Funcionalidade — Grimore

> Leia este arquivo antes de criar qualquer funcionalidade nova.
> Siga EXATAMENTE os formatos abaixo para garantir consistência.

---

## Template: `index.md`

```markdown
# 🚀 Funcionalidade: [Nome]

## Visão Geral
- **Objetivo:** [Breve descrição do valor desta funcionalidade]
- **Requisitos Vinculados:** [FR-XXX, FR-YYY]

## Roadmap
- **MT01:** [Nome do Marco]
- **MT02:** [Nome do Marco]

## Dependências
- **Depende de:** [outras funcionalidades ou "Nenhuma"]
- **Bloqueia:** [outras funcionalidades ou "Nenhuma"]

## Notas
[Contexto adicional ou decisões importantes]
```

---

## Template: `state.md`

```markdown
# 📊 Funcionalidade: [Nome] - Estado

## Progresso
| Marco | Status | Tarefas |
|-------|--------|---------|
| MT01 | ⏳ Não Iniciado | 0/X |
| MT02 | ⏳ Não Iniciado | 0/Y |

## Trabalho Atual
- **Última Tarefa:** Nenhuma
- **Tarefa Atual:** MT01-task 1 (aguardando início)
- **Próxima Tarefa:** MT01-task 2

## Contexto Técnico
### Arquivos Criados
Nenhum arquivo criado ainda.

### Decisões Tomadas
| Data | Tipo | Descrição |
|------|------|-----------|
| - | - | Nenhuma decisão registrada |

## Problemas Conhecidos
Nenhum problema relatado.
```

---

## Template: `MTxx.md` (Marco/Milestone)

```markdown
# 🏁 MT01: [Nome do Marco]

**Objetivo:** [O que será entregue e testado ao final desta etapa]

## Tarefas

### MT01-task 1 — [Título]
- **Descrição:** [O que deve ser feito]
- **Referência:** [FR-XXX / BR-YYY]
- **DoD:** [Definição de Pronto - resultado verificável]
- **Status:** ⏳ Não Iniciado
- **Executado em:** —
- **Revisão QA:** ⏳ Pendente

### MT01-task 2 — [Título]
- **Descrição:** [O que deve ser feito]
- **Referência:** [FR-XXX / BR-YYY]
- **DoD:** [Definição de Pronto - resultado verificável]
- **Status:** ⏳ Não Iniciado
- **Executado em:** —
- **Revisão QA:** ⏳ Pendente

## Critérios de Aceitação do Marco
- [ ] Todas as tarefas concluídas
- [ ] Código revisado pelo Engenheiro de QA (`✅ APROVADO`)
- [ ] Testes passando (se aplicável)
- [ ] `state.md` atualizado com progresso do marco

## Consolidação do Marco
> Preenchido pelo Release Manager ao fechar o marco

| Tarefa | Status Final | QA | Log |
|--------|--------------|----|-----|
| MT01-task 1 | — | — | — |
| MT01-task 2 | — | — | — |
```

---

## Convenções de Nomenclatura

| Elemento | Formato | Exemplo |
|---|---|---|
| Slug da Funcionalidade | `kebab-case` | `autenticacao-usuario` |
| Marco | `MTXX` | `MT01`, `MT02` |
| Tarefa | `MTXX-task Y` | `MT01-task 1` |
| Hotfix | `fix-[nome]` | `fix-bug-login` |
| Refactor | `refactor-[nome]` | `refactor-camada-api` |

---

## Regras e Limites

- **Máximo de 5 tarefas por marco** — Se exceder, crie um novo marco
- **Máximo de 4-5 marcos por funcionalidade** — Se exceder, divida a funcionalidade
- **Toda tarefa deve ter um DoD verificável** — Sem DoD = tarefa inválida

## Sequência Lógica das Tarefas

1. Setup/Configuração (primeiro)
2. Lógica de negócio (segundo)
3. Testes (por último, ou junto com a lógica se TDD)
