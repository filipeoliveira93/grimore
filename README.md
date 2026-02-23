# Grimore — Standalone

> **Um esquadrão de agentes de IA especializados para desenvolvimento de software, pronto para usar em qualquer projeto.**

O **Grimore** é uma coleção de skills para ferramentas de AI coding (Gemini CLI, Antigravity, etc.) que instala um processo estruturado de desenvolvimento diretamente no contexto do seu assistente de IA favorito.

A ideia central: para de criar prompts do zero. Clone este repositório, copie a pasta `.agent/skills/` para o seu projeto e tenha um time completo de Agentes de Desenvolvimento prontos para trabalhar.

---

## 🚀 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/filipeoliveira93/grimore.git
```

### 2. Copie as skills para o seu projeto

```bash
# No root do seu projeto:
cp -r grimore/stand-alone/.agent ./
```

> **Windows (PowerShell):**
> ```powershell
> Copy-Item -Path .\grimore\stand-alone\.agent -Destination .\ -Recurse
> ```

### 3. Pronto!

A sua ferramenta de AI irá detectar automaticamente as skills na pasta `.agent/skills/` e as disponibilizará como agentes especializados.

Veja o [GETTING-STARTED.md](./GETTING-STARTED.md) para um guia detalhado por ferramenta.

---

## 👥 O Esquadrão

### 🏗️ Agentes Estratégicos

| Skill | Função |
|-------|--------|
| `scope-architect` | Define o escopo e a visão do projeto em `project.md` |
| `requirements-engineer` | Entrevista o stack técnico e gera `requirements.md` |
| `stack-interview` | Protocolo de entrevista para definição de stack |
| `brownfield-setup` | Configura projetos existentes na estrutura Grimore |

### ⚡ Agentes de Execução

| Skill | Função |
|-------|--------|
| `feature-manager` | Gerencia features, marcos e tarefas |
| `implementation-coder` | Implementa código de produção seguindo os marcos |
| `feature-templates` | Gera templates padrão de features/milestones |

### 🧠 Agentes de Especialidade

| Skill | Função |
|-------|--------|
| `backend-architect` | Arquitetura de APIs, banco de dados, autenticação |
| `frontend-architect` | Componentes UI, sistemas de design, acessibilidade |
| `frontend-designer` | Design premium, tipografia, animações, UI/UX visual |
| `mcp-builder` | Criação de servidores MCP (Model Context Protocol) |
| `prompt-architect` | Criação e refinamento de system prompts e agentes |
| `doc-coauthor` | Co-autoria de documentação técnica estruturada |
| `design-system-extractor` | Engenharia reversa de design systems |
| `business-rule-extractor` | Extração de regras de negócio do código |

### 🛡️ Agentes de Qualidade

| Skill | Função |
|-------|--------|
| `quality-reviewer` | Revisão de código contra critérios de aceite |
| `test-engineer` | TDD, testes unitários, integração e E2E |
| `webapp-testing` | Testes de UI com Playwright |
| `security-auditor` | Auditoria OWASP Top 10 |
| `pentester-expert` | Testes de invasão e PoC de exploits |
| `release-manager` | Changelog, arquivamento e gestão de releases |

### 🔧 Utilitários

| Skill | Função |
|-------|--------|
| `detect-manifest` | Detecta stack do projeto (package.json, go.mod, etc.) |
| `handover-protocol` | Protocolo de passagem de bastão entre agentes |
| `skill-creator` | Cria novas skills seguindo as melhores práticas |

---

## 📁 Estrutura Gerada no Seu Projeto

Após iniciar o fluxo Grimore, é criada a pasta `.grimore/` no seu projeto:

```
.grimore/
├── project.md          # Escopo e visão do projeto
├── requirements.md     # Stack técnico e requisitos
├── context.md          # Contexto global e decisões
├── features/
│   └── [nome-feature]/
│       ├── index.md    # Visão geral da feature
│       ├── state.md    # Status atual
│       └── MT01.md     # Marcos e tarefas executáveis
└── logs/
    ├── executions/     # Logs de execução de tarefas
    ├── reviews/        # Relatórios de revisão de código
    └── archive/        # Trabalho concluído arquivado
```

---

## 🔄 Fluxo de Desenvolvimento Grimore

```
1. /scope-architect   → Define project.md (O QUÊ?)
2. /requirements-engineer → Define requirements.md (COMO?)
3. /feature-manager   → Cria features e milestones
4. /implementation-coder → Implementa cada tarefa
5. /quality-reviewer  → Revisa e valida
6. /release-manager   → Fecha o marco e gera changelog
```

---

## 📖 Documentação

- [GETTING-STARTED.md](./GETTING-STARTED.md) — Guia de configuração por ferramenta de AI
- [.grimore/README.md](./.grimore/README.md) — Sobre a pasta de contexto do projeto

---

## 📄 Licença

MIT
