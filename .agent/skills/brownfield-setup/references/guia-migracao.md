# Guia de Migração Brownfield

## O que é um Projeto Brownfield?

Um projeto Brownfield já possui código existente mas não segue a estrutura do Grimore. A migração consiste em **formalizar** o que já existe — nunca em jogar fora ou reescrever.

---

## Diagnóstico: Estrutura Legada Comum

```bash
# Verificar se a estrutura legada existe
ls -la .grimore/

# Sinais de projeto legado:
# - .grimore/spec.md (arquivo único com tudo)
# - .grimore/MT01.md (marcos na raiz)
# - .grimore/tasks/ (pasta de tarefas antiga)
```

---

## Passos da Migração

### Passo 1: Detectar Estrutura Legada
Use `detect-manifest` para identificar a stack automaticamente.
Liste os arquivos legados existentes antes de qualquer ação.

### Passo 2: Extrair Funcionalidades do `spec.md`
Se o `spec.md` existir:
1. Identifique cada funcionalidade descrita
2. Liste os marcos associados a cada uma
3. Mapeie as tarefas já executadas (✅ ou ⏳)

### Passo 3: Criar Nova Estrutura

Para cada funcionalidade encontrada:

```
.grimore/
├── features/
│   └── [feature-slug]/
│       ├── index.md      # Visão geral da funcionalidade
│       ├── state.md      # Progresso + contexto + arquivos
│       ├── MT01.md       # Marco 1
│       └── MT02.md       # Marco 2
├── context.md            # Matriz global de funcionalidades
├── requirements.md       # Stack técnica + regras
├── project.md            # Princípios do projeto
└── system.md             # Estado do sistema
```

### Passo 4: Migrar Conteúdo

**a) Criar `index.md`:**
```markdown
# 🚀 Funcionalidade: [Nome]

## Visão Geral
- **Objetivo:** [Extraído do spec.md]
- **Requisitos Vinculados:** [FR-XXX]

## Roadmap
- **MT01:** [Nome do Marco]
- **MT02:** [Nome do Marco]
```

**b) Criar `state.md`:**
```markdown
# 📊 Funcionalidade: [Nome] - Estado

## Progresso
- **MT01:** ✅ Concluído (migrado do legado)
- **MT02:** ⏳ Não Iniciado

## Contexto Técnico
[Arquivos já existentes no código]
```

**c) Migrar marcos do `spec.md`:**
Cada marco torna-se um arquivo separado seguindo o padrão do `feature-templates`.

### Passo 5: Atualizar `context.md`

```markdown
# 📋 Matriz de Funcionalidades

| Funcionalidade | Status | Marcos |
|----------------|--------|--------|
| [Nome] | 🔄 Em Migração | MT01-MT02 |
```

### Passo 6: Arquivar Estrutura Legada

```bash
mkdir -p .grimore/logs/archive/legacy
mv .grimore/spec.md .grimore/logs/archive/legacy/
mv .grimore/MT*.md .grimore/logs/archive/legacy/ 2>/dev/null
```

---

## Checklist de Migração

- [ ] Estrutura legada identificada com `detect-manifest`
- [ ] Funcionalidades extraídas do `spec.md`
- [ ] Diretórios de funcionalidades criados
- [ ] `index.md` e `state.md` para cada funcionalidade
- [ ] Marcos migrados para arquivos separados
- [ ] `context.md` atualizado com status "Em Migração"
- [ ] Arquivos legados arquivados (NUNCA deletados)
