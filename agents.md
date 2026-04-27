# Agentes do Grimore

Guia de referência rápida de todas as skills disponíveis no ecossistema **Grimore**. As skills são carregadas automaticamente pelo agente quando o contexto da solicitação corresponde aos gatilhos descritos em cada uma.

> Todas as skills estão em `.agent/skills/<nome>/SKILL.md`.

---

## Ciclo de Vida de um Projeto

As skills abaixo seguem a ordem natural de uso em um projeto, do setup inicial à entrega.

```
gmr-scope-architect → gmr-stack-interview → gmr-detect-manifest → gmr-brownfield-setup
      ↓
gmr-requirements-engineer → gmr-doc-coauthor
      ↓
gmr-feature-manager → gmr-feature-templates
      ↓
gmr-implementation-coder → gmr-backend-architect / gmr-frontend-architect / gmr-frontend-designer
              ↓                       ↓
     gmr-database-architect          gmr-api-documenter
      ↓
gmr-test-engineer → gmr-webapp-testing → gmr-quality-reviewer → gmr-security-auditor / gmr-pentester-expert
      ↓
gmr-devops-engineer
      ↓
gmr-release-manager → gmr-conventional-commits → gmr-handover-protocol
```

---

## Skills por Categoria

### Inicializacao e Escopo

| Skill | Quando usar |
|---|---|
| `gmr-scope-architect` | Definir ou formalizar o escopo do projeto em `.grimore/project.md`; entrevistas de visão; cenários greenfield/brownfield/pivô |
| `gmr-stack-interview` | Entrevistar colaborativamente o usuário para definir a stack quando ela não está definida em `requirements.md` |
| `gmr-detect-manifest` | Detectar automaticamente a stack de um projeto existente (lê `package.json`, `go.mod`, `Cargo.toml`, etc.) |
| `gmr-brownfield-setup` | Configurar a estrutura `.grimore/` em projetos que já têm código mas não têm documentação padrão |

---

### Documentacao e Requisitos

| Skill | Quando usar |
|---|---|
| `gmr-requirements-engineer` | Gerar `requirements.md` com requisitos funcionais, não-funcionais e de negócio (FR, NFR, BR) |
| `gmr-doc-coauthor` | Co-autoria de documentos técnicos estruturados: specs, RFCs, ADRs, PRDs, propostas |
| `gmr-business-rule-extractor` | Extrair exclusivamente lógica de negócio do código para `.grimore/rules/business-rules.md` |

---

### Planejamento de Funcionalidades

| Skill | Quando usar |
|---|---|
| `gmr-feature-manager` | Criar estrutura em `.grimore/features/[slug]/`, converter requisitos em milestones e tarefas com DoD |
| `gmr-feature-templates` | Gerar estrutura de diretórios padronizada para uma nova feature (`index.md`, `state.md`, `MTxx.md`) |

---

### Implementacao

| Skill | Quando usar |
|---|---|
| `gmr-implementation-coder` | Executar um `Task_ID` específico de um milestone: escrever código, rodar lint/testes, atualizar `state.md` |
| `gmr-backend-architect` | Projetar/implementar sistemas server-side: APIs REST/GraphQL/tRPC, autenticação, autorização |
| `gmr-database-architect` | Modelar schemas, criar migrations, configurar ORMs, otimizar queries e proteger dados sensíveis |
| `gmr-api-documenter` | Gerar spec OpenAPI 3.x, coleções Postman, READMEs de API e changelogs de breaking changes |
| `gmr-frontend-architect` | Projetar/implementar interfaces: React/Vue/Svelte/Angular/Vanilla JS, CSS, animações, acessibilidade |
| `gmr-frontend-designer` | Design visual premium de componentes e páginas; evita visual genérico de IA com atenção a tipografia e cor |
| `gmr-design-system-extractor` | Navegar em sites externos e extrair tokens de design (paleta, tipografia, espaçamento, componentes) |
| `gmr-mcp-builder` | Criar servidores MCP (Model Context Protocol) para integrar LLMs com APIs externas — TypeScript ou Python |
| `gmr-prompt-architect` | Criar ou refinar system prompts e definições de agentes com estrutura de 12 seções, Few-Shot e CoT |

---

### Qualidade e Seguranca

| Skill | Quando usar |
|---|---|
| `gmr-test-engineer` | Escrever testes unitários/integração/E2E com TDD (Red-Green-Refactor); analisar falhas de cobertura |
| `gmr-webapp-testing` | Testar aplicações web locais com Playwright: verificar UI, capturar screenshots, validar interações |
| `gmr-quality-reviewer` | Validar implementação de um Coder contra os critérios de aceitação do milestone; emitir veredito Aprovado/Rejeitado |
| `gmr-security-auditor` | Auditoria defensiva: identificar vulnerabilidades OWASP Top 10 no código-fonte, gerar relatórios |
| `gmr-pentester-expert` | Testes ofensivos: simular ataques, bypass de filtros, criar PoC de exploits, testar robustez real |

---

### Entrega e Publicacao

| Skill | Quando usar |
|---|---|
| `gmr-devops-engineer` | Configurar CI/CD (GitHub Actions), containerizar com Docker, definir estratégia de deploy e monitoramento |
| `gmr-release-manager` | Consolidar logs em Changelog, fechar versão/marco, arquivar logs de `.grimore/logs/`, executar `/dev:release` |
| `gmr-conventional-commits` | Gerar mensagens de commit, formatar/revisar commits existentes e atualizar entradas no `CHANGELOG.md` |
| `gmr-handover-protocol` | Finalizar uma fase e direcionar para o próximo agente com um handover padronizado |

---

### Meta-Skills (Infraestrutura do Ecossistema)

| Skill | Quando usar |
|---|---|
| `gmr-skill-creator` | Criar ou atualizar skills do Grimore: segue 6 etapas (entender → planejar → inicializar → editar → empacotar → iterar) |
| `claude-skill-creator` | Criar, testar, avaliar e otimizar skills do Claude Code com loop de evals, benchmarks e otimização de description — skill oficial da Anthropic |

---

## Estrutura de Pastas e Documentação de Milestones

### Pasta raiz `.grimore/`

```
.grimore/
├── project.md            ← Escopo, visão e princípios do projeto (gmr-scope-architect)
├── requirements.md       ← Stack + FR / NFR / BR (gmr-requirements-engineer)
├── context.md            ← Matriz global de funcionalidades + resumo executivo
├── features/
│   └── [feature-slug]/   ← slug em kebab-case, ex: user-auth
│       ├── index.md      ← Visão geral, objetivo e roadmap da feature
│       ├── state.md      ← Progresso em tempo real (⏳/🔄/✅ por marco)
│       ├── MT01.md       ← Marco 1 com tarefas e DoD
│       ├── MT02.md       ← Marco 2 ...
│       └── ...
├── logs/
│   ├── executions/
│   │   └── [Task_ID].md  ← Log de execução por tarefa (coder)
│   ├── reviews/
│   │   └── [Task_ID]-REVIEW.md ← Veredito do QA por tarefa
│   └── archive/          ← Logs arquivados após release
└── rules/
    └── business-rules.md ← Regras de negócio extraídas (gmr-business-rule-extractor)
```

---

### Convenções de Nomenclatura

| Item | Regra | Exemplo |
|---|---|---|
| Feature slug | `kebab-case`, minúsculo, sem espaços | `user-auth`, `payment-gateway` |
| Marcos | `MT` + número 2 dígitos | `MT01.md`, `MT02.md` |
| Task ID | `MT` + número + `-T` + número | `MT01-T01`, `MT02-T03` |
| Log de execução | `[Task_ID].md` | `MT01-T01.md` |
| Log de revisão | `[Task_ID]-REVIEW.md` | `MT01-T01-REVIEW.md` |

---

### Regras de Criação e Atualização por Fase

#### Fase: Planejamento (`gmr-feature-manager` + `gmr-feature-templates`)

| Arquivo | Ação | Quem |
|---|---|---|
| `.grimore/features/[slug]/index.md` | Criar com visão, objetivo e roadmap | `gmr-feature-manager` |
| `.grimore/features/[slug]/state.md` | Criar com todos os marcos em `⏳ Não Iniciado` | `gmr-feature-manager` |
| `.grimore/features/[slug]/MTxx.md` | Criar um arquivo por marco, com tarefas e DoD | `gmr-feature-manager` |
| `.grimore/context.md` | Atualizar matriz de funcionalidades | `gmr-feature-manager` |

**Limites obrigatórios:**
- ❌ Máximo **5 tarefas por marco** — crie um novo marco se necessário
- ❌ Toda tarefa **deve ter DoD verificável** — sem DoD = tarefa inválida
- ❌ Slug de feature sem letras maiúsculas ou espaços

---

#### Fase: Implementação (`gmr-implementation-coder`)

Após cada `Task_ID` executado, o coder **deve** atualizar:

| Arquivo | O que atualizar |
|---|---|
| `.grimore/features/[slug]/MTxx.md` | Status da tarefa → `🔄 Em Revisão` + data de execução |
| `.grimore/features/[slug]/state.md` | Progresso do marco, trabalho atual, contexto técnico, próximos passos |
| `.grimore/logs/executions/[Task_ID].md` | Criar log com seção "Tarefas Executadas vs. Não Executadas" (obrigatória) |

**Protocolo de leitura em camadas (L1 → L2 → L3):**

```
L1 (SEMPRE): context.md + requirements.md
L2 (por feature): index.md + state.md + MTxx.md
L3 (sob demanda): log de execução anterior + log de revisão anterior
```

---

#### Fase: Revisão (`gmr-quality-reviewer`)

| Arquivo | Ação |
|---|---|
| `.grimore/logs/reviews/[Task_ID]-REVIEW.md` | Criar com veredito `APROVADO` ou `REJEITADO` + justificativa |
| `.grimore/features/[slug]/MTxx.md` | Atualizar status → `✅ Aprovado` ou `❌ Rejeitado` |

---

#### Fase: Release (`gmr-release-manager`)

| Arquivo | Ação |
|---|---|
| `CHANGELOG.md` | Adicionar entradas consolidadas dos logs aprovados |
| `.grimore/context.md` | Marcar funcionalidade como `Concluída` |
| `.grimore/logs/executions/` | Mover para `.grimore/logs/archive/` após confirmação |
| `.grimore/logs/reviews/` | Mover para `.grimore/logs/archive/` após confirmação |

> ❌ **Proibido** fazer release sem veredito `APROVADO` do `gmr-quality-reviewer`  
> ❌ **Proibido** deletar logs — apenas arquivar

---

## Regras Globais do Agente

As regras abaixo se aplicam a **todas** as interações, independentemente da skill ativa:

| Regra | Detalhe |
|---|---|
| **Idioma** | Todas as respostas e documentos gerados em **Português do Brasil** (exceto quando explicitamente solicitado em outro idioma) |
| **Arquivos de planejamento** | `task.md` e `implementation_plan.md` devem ser escritos em PT-BR |
| **Conventional Commits** | Mensagens de commit seguem o padrão Conventional Commits v1.0.0 (skill `gmr-conventional-commits`) |

---

## Estrutura de Diretórios de Skills

```
.agent/
└── skills/
    ├── claude-skill-creator/
    ├── gmr-api-documenter/
    ├── gmr-backend-architect/
    ├── gmr-brownfield-setup/
    ├── gmr-business-rule-extractor/
    ├── gmr-conventional-commits/
    ├── gmr-database-architect/
    ├── gmr-design-system-extractor/
    ├── gmr-detect-manifest/
    ├── gmr-devops-engineer/
    ├── gmr-doc-coauthor/
    ├── gmr-feature-manager/
    ├── gmr-feature-templates/
    ├── gmr-frontend-architect/
    ├── gmr-frontend-designer/
    ├── gmr-handover-protocol/
    ├── gmr-implementation-coder/
    ├── gmr-mcp-builder/
    ├── gmr-pentester-expert/
    ├── gmr-prompt-architect/
    ├── gmr-quality-reviewer/
    ├── gmr-release-manager/
    ├── gmr-requirements-engineer/
    ├── gmr-scope-architect/
    ├── gmr-security-auditor/
    ├── gmr-skill-creator/
    ├── gmr-stack-interview/
    ├── gmr-test-engineer/
    └── gmr-webapp-testing/
```

> **29 skills disponíveis** (28 `gmr-*` + 1 `claude-skill-creator`) — atualize este arquivo sempre que adicionar ou remover uma skill.
