# Mapa de Handover — Grimore

## Fluxo Padrão de Passagem de Bastão

```
Arquiteto de Escopo 🏛️
       ↓ /gmr-requirements-engineer
Engenheiro de Requisitos 📝
       ↓ /gmr-feature-manager
Gerente de Funcionalidades ✨
       ↓ /gmr-implementation-coder [Task_ID]
Coder 💻
       ↓ /gmr-quality-reviewer [Task_ID]
Engenheiro de QA 🔍
    ↓ APROVADO                    ↓ REJEITADO          ↓ BLOQUEADO
Release Manager 📦     Coder 💻 (corrige)     Usuário (decisão)
```

---

## Tabela de Handover

| Agente Atual | Próximo Agente | Comando |
|---|---|---|
| Arquiteto de Escopo 🏛️ | Engenheiro de Requisitos 📝 | `/gmr-requirements-engineer` |
| Engenheiro de Requisitos 📝 | Gerente de Funcionalidades ✨ | `/gmr-feature-manager` |
| Gerente de Funcionalidades ✨ | Coder 💻 | `/gmr-implementation-coder [Task_ID]` |
| Coder 💻 | Engenheiro de QA 🔍 | `/gmr-quality-reviewer [Task_ID]` |
| Engenheiro de QA 🔍 (Aprovado) | Gerente de Lançamentos 📦 | `/gmr-release-manager` ou próxima tarefa |
| Engenheiro de QA 🔍 (Rejeitado) | Coder 💻 | `/gmr-implementation-coder [Task_ID]` (correção) |
| Qualquer agente (Bloqueado) | Usuário | Marcar tarefa como `⏸️ Bloqueado` em `MTxx.md` e `state.md`, documentar o bloqueio em `state.md > Bloqueadores` e aguardar decisão |

---

## Formato do Handover

Ao finalizar qualquer fase, use EXATAMENTE este formato:

```markdown
> "🏷️ **[Nome do Artefato] documentado com sucesso.**"
>
> **Arquivo Criado/Atualizado:** `[caminho do arquivo]`
>
> **Resumo:** [1-2 linhas sobre o que foi feito]
>
> **Próximo Passo:** Use `/[comando]` para iniciar a próxima fase.
>
> **Handover para:** [Nome do Próximo Agente] ([emoji])
```

---

## Exemplo Preenchido

```markdown
> "🏛️ **Escopo do projeto documentado com sucesso.**"
>
> **Arquivo Criado:** `.grimore/project.md`
>
> **Resumo:** Definido o escopo conceitual para o projeto NBA Stats Collector v1.0.0.
>
> **Próximo Passo:** Use `/gmr-requirements-engineer` para detalhar os requisitos funcionais.
>
> **Handover para:** Engenheiro de Requisitos 📝
```

---

## Emojis por Agente (Imutáveis)

| Agente | Emoji |
|---|---|
| Arquiteto de Escopo | 🏛️ |
| Engenheiro de Requisitos | 📝 |
| Gerente de Funcionalidades | ✨ |
| Coder | 💻 |
| Engenheiro de QA | 🔍 |
| Gerente de Lançamentos | 📦 |
| Arquiteto Backend | ⚙️ |
| Arquiteto Frontend | 🎨 |
| Auditor de Segurança | 🛡️ |
| Engenheiro de Testes | 🧪 |
