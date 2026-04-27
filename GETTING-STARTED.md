# Guia de Início Rápido — Grimore

Este guia detalha como instalar e utilizar as skills do Grimore em cada ferramenta de AI coding suportada.

---

## Pré-Requisitos

Antes de tudo, clone o repositório:

```bash
git clone https://github.com/filipeoliveira93/grimore.git
```

---

## Ferramentas Suportadas

### Gemini CLI / Antigravity ⭐ (Nativo)

O **Gemini CLI** e o **Antigravity** reconhecem automaticamente qualquer pasta `.agent/skills/` no diretório do projeto. Nenhuma configuração adicional é necessária.

**Instalação:**

```bash
# Na raiz do seu projeto:
cp -r caminho/para/grimore/stand-alone/.agent ./
```

**Uso:**

As skills aparecem automaticamente no contexto do assistente. Basta invocar pelo nome:

```
Use a skill gmr-scope-architect para definir o escopo do meu projeto.
```

ou diretamente via slash command (se configurado):

```
/gmr-scope-architect
/gmr-feature-manager
/gmr-implementation-coder
```

---

### Claude (Anthropic) / Cursor

O Claude com o sistema de **Projects** ou o **Cursor** com `.cursorrules` podem usar as skills via regras de contexto.

**Opção 1 — Copiar instruções manualmente:**

1. Abra o `SKILL.md` da skill desejada
2. Copie o conteúdo para as instruções do seu Project ou `.cursorrules`

**Opção 2 — Referência direta:**

Inclua no contexto do seu assistente uma instrução como:

```
Leia e siga as instruções em .agent/skills/gmr-scope-architect/SKILL.md
```

---

### OpenCode

O OpenCode suporta skills nativamente na pasta `.opencode/skills/`.

**Instalação:**

```bash
mkdir -p .opencode
cp -r caminho/para/grimore/stand-alone/.agent/skills .opencode/skills
```

---

### Qualquer Outra Ferramenta

Para ferramentas que não reconhecem `.agent/skills/` nativamente, copie o conteúdo do `SKILL.md` desejado para o system prompt ou contexto personalizado da sua ferramenta.

---

## Iniciando o Fluxo Grimore

Após instalar as skills, siga este fluxo para um novo projeto:

### Passo 1 — Definir o Escopo

```
Use a skill gmr-scope-architect
```

O agente irá:
- Entrevistar você sobre a visão do projeto
- Identificar se é Greenfield ou Brownfield
- Criar `.grimore/project.md`

### Passo 2 — Definir Requisitos

```
Use a skill gmr-requirements-engineer
```

O agente irá:
- Detectar sua stack automaticamente
- Entrevistar sobre requisitos funcionais e não-funcionais
- Criar `.grimore/requirements.md`

### Passo 3 — Planejar Features

```
Use a skill gmr-feature-manager para criar a feature [nome da feature]
```

O agente irá:
- Criar `.grimore/features/[slug]/`
- Gerar `index.md`, `state.md` e marcos `MT01.md`, `MT02.md`, etc.

### Passo 4 — Implementar

```
Use a skill gmr-implementation-coder para executar MT01-T01
```

### Passo 5 — Revisar

```
Use a skill gmr-quality-reviewer para revisar MT01-T01
```

### Passo 6 — Fechar o Marco

```
Use a skill gmr-release-manager para fechar o MT01
```

---

## Dicas de Uso

- **Projetos existentes?** Use `gmr-brownfield-setup` para integrar sem destruir o que já existe.
- **Precisa de testes?** Chame `gmr-test-engineer` após cada implementação.
- **Auditoria de segurança?** `gmr-security-auditor` antes do release.
- **Criar novas skills?** Use `gmr-skill-creator` para expandir o toolkit.

---

## Estrutura da Pasta `.agent/skills/`

```
.agent/
└── skills/
    ├── gmr-scope-architect/
    │   └── SKILL.md
    ├── gmr-requirements-engineer/
    │   └── SKILL.md
    ├── gmr-feature-manager/
    │   └── SKILL.md
    ├── ... (28 skills no total)
    └── gmr-skill-creator/
        ├── SKILL.md
        └── scripts/
```

Cada skill é uma pasta auto-contida com um `SKILL.md` principal e, opcionalmente, pastas `references/`, `scripts/` ou `assets/`.
