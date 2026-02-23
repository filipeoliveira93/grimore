# Template de Veredito de QA

> Use este template para registrar o resultado da revisão em `.grimore/logs/reviews/[Task_ID]-REVIEW.md`.

---

## Cabeçalho do Veredito

```markdown
# 🔍 Revisão de QA — [Task_ID]

**Revisor:** Engenheiro de QA 🔍  
**Data:** [YYYY-MM-DD]  
**Task_ID:** [MT01-task 1]  
**Feature:** [feature-slug]
**Veredito:** ✅ APROVADO | ❌ REJEITADO
```

---

## Template: APROVADO

```markdown
## ✅ VEREDITO: APROVADO

### Evidências de Qualidade
- **Testes:** Passando — [X/X testes OK]
- **Linter:** Sem erros
- **DoD:** Todos os critérios atendidos
- **state.md:** Atualizado corretamente

### Observações
[Comentários opcionais sobre boas práticas encontradas ou melhorias futuras sugeridas]

### Próximo Passo
> Use `/sdd-logs` para consolidar no changelog ou passe para a próxima tarefa com `/sdd-codigo [próximo Task_ID]`.
```

---

## Template: REJEITADO

```markdown
## ❌ VEREDITO: REJEITADO

### Motivo da Rejeição

#### Falha [1]: [Título curto]
- **Tipo:** [DoD não atendido / Erro de linter / Falha de teste / Padrão arquitetural / Segurança]
- **Descrição:** [O que está errado e por quê]
- **Referência Técnica:** [SOLID, OWASP, Padrões em `references/patterns.md`]
- **Como Corrigir:** [Instrução específica para o Coder]

#### Falha [2]: [Título curto]
- **Tipo:** [...]
- **Descrição:** [...]
- **Como Corrigir:** [...]

### Próximo Passo
> Use `/sdd-codigo [Task_ID]` para corrigir os pontos listados acima antes de solicitar nova revisão.
```

---

## Checklist de Revisão

Antes de emitir o veredito, verifique TODOS os itens:

| Item | Verificação |
|---|---|
| DoD | Todos os critérios do marco foram atendidos? |
| Testes | Testes existem e passam? |
| Linter | Zero erros de linter/compilação? |
| `state.md` | Foi atualizado com o progresso correto? |
| Escopo | Apenas arquivos do Task_ID foram modificados? |
| SOLID | Código segue os princípios? |
| Segurança | Sem SQL injection, secrets expostos ou validação ausente? |
