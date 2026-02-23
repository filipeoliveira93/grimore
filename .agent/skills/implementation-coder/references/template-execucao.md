# Template de Log de Execução — Grimore

> Use este template para registrar cada execução em `.grimore/logs/executions/[Task_ID].md`.
> O preenchimento é **obrigatório** — o QA lê este arquivo para emitir o veredito.

---

## Template

```markdown
# 📋 Log de Execução — [Task_ID]

**Executor:** Coder 💻
**Data:** [YYYY-MM-DD]
**Task_ID:** [MT01-task 1]
**Feature:** [feature-slug]
**Marco:** [MT01 — Nome do Marco]
**Status:** ✅ Concluído | ⚠️ Parcial | ❌ Falhou

---

## O Que Foi Feito

[Descrição concisa da implementação — o que foi construído e por quê dessa forma]

---

## Tarefas Executadas vs. Não Executadas

| Subtarefa | Status | Motivo (se não executada) |
|-----------|--------|--------------------------|
| [descrição da subtarefa 1] | ✅ Executada | — |
| [descrição da subtarefa 2] | ❌ Não executada | [motivo claro da omissão] |
| [descrição da subtarefa 3] | ⚠️ Parcial | [o que foi e o que não foi feito] |

> ⚠️ **Jamais omita itens do DoD sem registrar o motivo aqui.**

---

## Arquivos Criados/Modificados

| Arquivo | Ação | Motivo |
|---------|------|--------|
| `path/to/file.ts` | Criado | Implementação da lógica X |
| `path/to/other.ts` | Modificado | Ajuste para suportar a nova feature |

---

## Testes

- **Executados:** Sim / Não
- **Resultado:** X/Y passando
- **Cobertura:** N%
- **Comando usado:** `[npm test / pytest / go test ...]`

---

## Decisões Técnicas

| Decisão | Alternativa Considerada | Justificativa |
|---------|------------------------|---------------|
| [Decisão tomada] | [Alternativa descartada] | [Por que esta foi escolhida] |

> Se nenhuma decisão relevante foi tomada, escreva "Nenhuma decisão arquitetural nesta tarefa."

---

## Bloqueios / Pendências

[Descreva qualquer impedimento encontrado ou item que ficou pendente.
Se não houver nada, escreva "Nenhum".]

---

## Checklist Final (Auto-verificação do Coder)

- [ ] Código implementado conforme descrição do Task_ID
- [ ] Linter/compilação sem erros
- [ ] Testes criados/atualizados (se exigido pelo DoD)
- [ ] `state.md` atualizado com progresso
- [ ] `MTxx.md` atualizado com novo status da tarefa (`🔄 Em Revisão`)
- [ ] Nenhum arquivo fora do escopo foi modificado
- [ ] Este log criado em `.grimore/logs/executions/[Task_ID].md`
```

---

## Guia de Status

| Ícone | Significado |
|-------|-------------|
| ✅ Concluído | Tarefa 100% implementada, testes passando |
| ⚠️ Parcial | Implementado parcialmente — razão documentada acima |
| ❌ Falhou | Não foi possível implementar — bloqueio documentado acima |
| 🔄 Em Revisão | Concluído pelo Coder, aguardando QA |
