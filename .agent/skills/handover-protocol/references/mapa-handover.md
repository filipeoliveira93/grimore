# Mapa de Handover — Grimore

## Fluxo Padrão de Passagem de Bastão

```
Arquiteto de Escopo 🏛️
       ↓ /sdd-requisitos
Engenheiro de Requisitos 📝
       ↓ /sdd-funcionalidade
Gerente de Funcionalidades ✨
       ↓ /sdd-codigo [Task_ID]
Coder 💻
       ↓ /sdd-revisao [Task_ID]
Engenheiro de QA 🔍
    ↓ APROVADO             ↓ REJEITADO
Release Manager 📦     Coder 💻 (corrige)
```

---

## Tabela de Handover

| Agente Atual | Próximo Agente | Comando |
|---|---|---|
| Arquiteto de Escopo 🏛️ | Engenheiro de Requisitos 📝 | `/sdd-requisitos` |
| Engenheiro de Requisitos 📝 | Gerente de Funcionalidades ✨ | `/sdd-funcionalidade` |
| Gerente de Funcionalidades ✨ | Coder 💻 | `/sdd-codigo [Task_ID]` |
| Coder 💻 | Engenheiro de QA 🔍 | `/sdd-revisao [Task_ID]` |
| Engenheiro de QA 🔍 (Aprovado) | Gerente de Lançamentos 📦 | `/sdd-logs` ou próxima tarefa |
| Engenheiro de QA 🔍 (Rejeitado) | Coder 💻 | `/sdd-codigo [Task_ID]` (correção) |

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
> **Próximo Passo:** Use `/sdd-requisitos` para detalhar os requisitos funcionais.
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
