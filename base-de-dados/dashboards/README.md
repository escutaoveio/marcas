# Dashboards — IVA Química

Dashboards em HTML com visibilidade pública via **GitHub Pages**.

---

## Como funciona

Cada arquivo `.html` salvo aqui fica acessível publicamente pela URL:

```
https://[usuario].github.io/[repositorio]/base-de-dados/dashboards/[arquivo].html
```

Basta fazer commit e push — o GitHub Pages publica automaticamente.

---

## Convenção de nomenclatura

```
AAAA-MM-[contexto]-[descricao].html

Exemplos:
2026-05-ecommerce-performance.html
2026-06-vendas-mensal.html
2026-Q2-marketing-overview.html
```

---

## Estrutura sugerida para cada dashboard

Cada arquivo HTML deve ser autossuficiente (CSS inline, sem dependências externas) para garantir que funcione corretamente via GitHub Pages sem configuração adicional.

---

## Configuração do GitHub Pages

Para ativar:
1. Repositório → **Settings** → **Pages**
2. Source: `Deploy from a branch`
3. Branch: `main` · Folder: `/ (root)`
4. Salvar — o GitHub publicará todos os `.html` do repositório
