# Template de Regras de Negócio — `business-rules.md`

> Use este template para salvar o resultado da extração em `.grimore/rules/business-rules.md`.

---

## Cabeçalho do Arquivo

```markdown
# 📜 Regras de Negócio — [Nome do Projeto]

**Gerado por:** business-rule-extractor  
**Última Atualização:** [YYYY-MM-DD]  
**Versão:** [X.Y.Z]
```

---

## Estrutura de Cada Regra

```markdown
### BR-[NNN]: [Nome Descritivo da Regra]

- **Categoria:** [Precificação / Autenticação / Fluxo de Pedidos / etc.]
- **Contexto:** [Entidade ou fluxo ao qual a regra se aplica]
- **Lógica (Linguagem Natural):**
  > Se [condição], então [ação/resultado].
  > Exemplo: "Se o usuário não possuir o papel VIP, então o acesso ao catálogo premium é negado."
- **Referência no Código:** [`src/services/UserService.js#L42`]
- **Requisito Vinculado:** [FR-XXX ou BR-YYY]
```

---

## Exemplo Preenchido

```markdown
### BR-001: Validação de Acesso Premium

- **Categoria:** Controle de Acesso
- **Contexto:** Módulo de Catálogo de Produtos
- **Lógica (Linguagem Natural):**
  > Se o usuário não possuir o papel `VIP` ativo, o acesso ao catálogo premium é negado e uma mensagem de upgrade é exibida.
- **Referência no Código:** [`src/services/CatalogService.js#L87`]
- **Requisito Vinculado:** FR-012, BR-005
```

---

## Categorias Sugeridas

| Categoria | Exemplos |
|---|---|
| Precificação | Cálculo de desconto, imposto, frete |
| Autenticação | Regras de senha, expiração de sessão |
| Controle de Acesso | Papéis, permissões, visibilidade de dados |
| Fluxo de Pedidos | Status permitidos, transições de estado |
| Validação de Dados | Formatos obrigatórios, limites numéricos |
| Integridade | Restrições entre entidades relacionadas |

---

## Regras de Escrita

- ❌ **NÃO** mencione tecnologias: sem "banco de dados", "MongoDB", "API", "JSON"
- ❌ **NÃO** descreva HOW (como foi implementado) — apenas WHAT (o que a regra determina)
- ✅ **USE** a forma condicional: "Se X, então Y"
- ✅ **GARANTA** que qualquer desenvolvedor possa reimplementar a regra em qualquer linguagem
