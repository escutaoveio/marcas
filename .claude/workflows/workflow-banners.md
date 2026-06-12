# Banner Migration Workflow

Distribui um banner aprovado de site para formatos adicionais de plataforma (ML, Linktree, etc.).

---

## Configuração — preencher antes de usar

| Variável | Onde obter | Exemplo |
|---|---|---|
| `FIGMA_FILE_KEY` | URL do arquivo Figma: `figma.com/design/[KEY]/...` | `6rdNvOQr0mxQeqmZQ8A3iq` |
| `PRODUCTS_ROOT` | Caminho raiz dos produtos no workspace | `products/` ou `e-commerce/products/` |

---

## Quando usar

Após o banner de site (`banner-desktop` + `banner-mobile`) estar aprovado e criado no Figma.
Entrada: um `banner-copy-brief.md` aprovado.

---

## Formatos suportados

| ID | Dimensão | Destino | Página Figma |
|---|---|---|---|
| `ml-desktop` | 900 × 300 px | Mercado Livre — cabeçalho de anúncio | `[Marketplace] ML` |
| `linktree` | 1200 × 628 px | Linktree / Open Graph | `[Linktree] Bio` |

> Próximos formatos: Meta Ads 1200×628, Meta Ads 1080×1080, Shopee.

---

## Pré-requisitos

- [ ] `banner-copy-brief.md` aprovado pelo QA no diretório do produto
- [ ] Banner de site já criado no Figma (section do produto em `[Site] Vitrine`)

---

## Como invocar

```
Usando o prompt em [caminho/para/migration-agent.md],
migre o banner para [formatos] a partir de:
[PRODUCTS_ROOT]/[marca]/[linha]/[produto]/banner-copy-brief.md
```

Exemplo:
```
Usando o prompt em .claude/migração/migration-agent.md,
migre o banner para ml-desktop e linktree a partir de:
products/cristal/revestimentos/nex-floor/banner-copy-brief.md
```

---

## Fluxo

```
[INPUT] banner-copy-brief.md + formatos solicitados
    ↓
① Lê o copy brief aprovado
    ↓
② Para cada formato:
   a) Avalia se copy precisa adaptação
   b) Salva brief de plataforma se houver adaptação
   c) Cria frame no Figma na página correta
    ↓
[OUTPUT] Frames no Figma + relatório com URL e copy usada
```

---

## Adaptação de copy

O `banner-copy-brief.md` é a fonte de verdade. **Adaptar somente se:**

| Situação | Ação |
|---|---|
| Badge com conteúdo editorial inadequado para ML | Substituir por destaque comercial (`Kit`, `Oferta`, `Novidade`) |
| H1 com referência interna que o canal não entende | Reescrever mantendo o limite de 45 chars |
| alt_text com urgência de campanha que expira | Substituir por proposta de valor perene |

Se adaptar: salvar `banner-ml-brief.md` ou `banner-linktree-brief.md` no diretório do produto usando os templates em `templates/`.
Se não adaptar: usar o copy do `banner-copy-brief.md` diretamente.

---

## Diferenças estruturais por formato

| Elemento | site-desktop | site-mobile | ml-desktop | linktree |
|---|---|---|---|---|
| ProductSpot | ✓ | ✓ | ✗ | ✗ |
| Badge | ✓ | ✓ | ✓ | ✓ |
| H1 fontSize | 36 px | 24 px | 28 px | 48 px |
| Padding | 25 px | 20 px | 25 px | 40 px |

---

## Output esperado

```
Migração concluída.

Produto: [nome]
Formatos criados: [lista]

[formato]:
  Página Figma: [nome]
  H1: "[texto]"
  Badge: "[texto]"
  Copy adaptada: sim/não

URL Figma: https://www.figma.com/design/[FIGMA_FILE_KEY]
```

---

## Arquivos do pack

| Arquivo | Função |
|---|---|
| `workflow.md` | Este manual |
| `migration-agent.md` | Agente executor — contém todas as specs inlineadas |
| `templates/brief-ml.md` | Template de brief adaptado para Mercado Livre |
| `templates/brief-linktree.md` | Template de brief adaptado para Linktree / Open Graph |
