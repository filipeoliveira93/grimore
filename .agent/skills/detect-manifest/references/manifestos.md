# Manifestos de Projeto Suportados

## Tabela de Manifestos

| Manifesto | Linguagem/Framework | Informações Extraídas |
|---|---|---|
| `package.json` | Node.js / JavaScript | nome, versão, dependências, devDependencies, scripts |
| `go.mod` | Go | nome do módulo, versão do go, require |
| `Cargo.toml` | Rust | nome do pacote, versão, dependências |
| `pom.xml` | Java (Maven) | groupId, artifactId, versão, dependências |
| `build.gradle` | Java (Gradle) | plugins, dependências |
| `requirements.txt` | Python (pip) | lista de dependências |
| `pyproject.toml` | Python (Poetry/PDM) | nome do projeto, versão, dependências |
| `composer.json` | PHP | nome, require, autoload |
| `*.csproj` | C# / .NET | TargetFramework, PackageReference |
| `Gemfile` | Ruby | dependências de gems |

---

## Fluxo de Busca

```bash
# Verificar manifestos na raiz do projeto
ls -la | grep -E "(package.json|go.mod|Cargo.toml|pom.xml|requirements.txt|pyproject.toml|composer.json|Gemfile)"
```

---

## Template de Resumo de Saída

```markdown
## Manifesto Detectado

- **Tipo:** [package.json / go.mod / etc.]
- **Projeto:** [nome]
- **Versão:** [X.Y.Z]
- **Linguagem:** [JavaScript / Go / etc.]
- **Framework:** [Next.js / Express / Gin / etc.] (se detectado)

### Principais Dependências
- [dep1] @ [versão]
- [dep2] @ [versão]

### Scripts Disponíveis
- `[nome]`: [o que faz]
```

---

## Cenários Especiais

### Nenhum Manifesto Encontrado

```markdown
⚠️ **Aviso:** Nenhum manifesto de projeto encontrado.

**Ação Recomendada:** Inicialize o projeto com:
- Node.js: `npm init -y`
- Go: `go mod init [nome-do-modulo]`
- Python: `pip freeze > requirements.txt`
- Rust: `cargo init`
```

### Múltiplos Manifestos (Monorepo)

```markdown
📦 **Projeto Monorepo Detectado:**

- `package.json` (raiz) — Workspace principal
- `packages/api/package.json` — Backend
- `packages/web/package.json` — Frontend

**Ação:** Confirme com o usuário qual manifesto é a referência principal.
```
