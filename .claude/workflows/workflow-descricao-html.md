# Workflow: Gerar Descrição de Produto em HTML

> **Agente responsável:** `agente-html-description.md` (nesta mesma pasta)
> **Última revisão:** 2026-06-01

---

## Visão Geral

Este workflow converte o `product.md` de uma variante em um ou mais arquivos HTML prontos para publicação no Wake Commerce. O ponto de partida é sempre o `product.md`; os arquivos de saída dependem do tipo de produto e das condições listadas abaixo.

> **Por que inline styles?** O Wake Commerce remove blocos `<style>` das descrições de produto, exibindo o CSS como texto bruto na vitrine. Todo estilo deve estar no atributo `style=""` de cada elemento. Imagens base64 embutidas excedem limites da plataforma — use sempre URLs do host externo.

**Arquivos de saída possíveis:**

| Arquivo | Template de origem | Quando gerar |
|---|---|---|
| `{produto-slug}.html` | `product-description-template.html` | Sempre — é o arquivo principal |
| `{produto-slug}.html` | `product-description-banner-template.html` | Quando há banner dedicado para o produto |
| `{produto-slug}-calculator.html` | `product-calculator-template.html` | Quando o produto tem rendimento mensurável |
| Adendo embutido no `.html` | `packaging-change-adendo.html` | Quando houve reformulação de rótulo/embalagem |
| Texto simples | `kits-description-template.html` | Quando o produto é um kit |

---

## Fonte de Dados

A fonte primária é o **Notion — Catálogo de Produtos**:
`notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`

Busque o produto pelo nome usando o Notion MCP. As seções do produto no Notion mapeiam assim:

| Seção do produto | Campo no Notion | Bloco HTML de destino |
|---|---|---|
| Dados técnicos | `1.0) DADOS DO PRODUTO` | Painel de dados (flex:1.1) |
| Destaques | `2.0) DESTAQUE DO PRODUTO` | Painel de destaques (flex:0.9) |
| FAQ | `3.0) PERGUNTAS FREQUENTES` | Seção de accordion |

---

## Estrutura de Pastas

```
.claude/templates/
├── product-description-template.html        ← T1
├── product-description-banner-template.html  ← T2
├── packaging-change-adendo.html              ← T3
├── product-calculator-template.html          ← T4
└── kits-description-template.html            ← T5

marketing/marcas/                             ← repo escutaoveio/marcas (público)
└── {marca-slug}/
    └── {linha-slug}/
        ├── {produto-slug}.html               ← SAÍDA: descrição HTML
        ├── {produto-slug}-calculator.html    ← SAÍDA: calculadora (quando aplicável)
        └── {imagem.jpg}                      ← imagens hospedadas aqui para URL raw
```

**Regra de slug:** minúsculas, espaços → hífens, acentos removidos, caracteres especiais → hífen.

Exemplos:
- Drylevis / Colas & Rejuntes / Selante Adesivo DW240 → `marketing/marcas/drylevis/colas-e-rejuntes/selante-adesivo-dw240.html`
- Elastment / Impermeabilizantes / Manta Flex → `marketing/marcas/elastment/impermeabilizantes/manta-flex.html`
- Hold Stone / Pedras / Resina para Pedras → `marketing/marcas/hold-stone/pedras/resina-para-pedras.html`

**URL raw das imagens:**
```
https://raw.githubusercontent.com/escutaoveio/marcas/master/marketing/marcas/{marca-slug}/{linha-slug}/{arquivo.jpg}
```

---

## Mapa de Templates

---

### T1 — `product-description-template.html` · Descrição Padrão

Template principal. Gera o HTML com três blocos:

```
<link> (Material Symbols)
wrapper div
  └── card div (flex-direction:column)
        ├── flex row (flex-wrap:wrap)
        │     ├── painel de dados    (flex:1.1 1 300px)  ← seção 1.0
        │     └── painel de destaques (flex:0.9 1 280px) ← seção 2.0
        └── FAQ div                                       ← seção 3.0
```

**Fonte dos ícones:** `<link rel="stylesheet">` para Google Fonts Material Symbols Outlined. **Nunca usar `@import` dentro de `<style>`.**

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0">
```

**Responsividade:** o layout de duas colunas é obtido com `flex-wrap:wrap` + `flex:1.1 1 300px` / `flex:0.9 1 280px`. Sem `@media queries` necessárias.

---

### T2 — `product-description-banner-template.html` · Descrição com Banner

Variante do T1. Use quando o produto tem banner dedicado. Adiciona dois blocos:

**Banner no topo** — primeiro filho do card, antes do flex row:

```html
<div style="border-radius:16px;overflow:hidden;">
  <picture>
    <source media="(max-width:640px)" srcset="URL-BANNER-MOBILE">
    <img src="URL-BANNER-DESKTOP" alt="Banner [Nome do Produto]" style="width:100%;display:block;" width="1160" height="160">
  </picture>
</div>
```

Dimensões: **desktop** `1160 × 160px` · **mobile** `640 × 320px`.

**Bloco "Nova Embalagem"** — último filho do card, após o FAQ:

```html
<div style="box-sizing:border-box;background:#f7f7f7;border-radius:16px;padding:32px;">
  <h2 style="margin:0 0 16px;font-size:1.25rem;line-height:1.1;font-weight:700;">Nova Embalagem</h2>
  <p style="margin:0 0 24px;font-size:0.9375rem;color:#4d4d4d;line-height:1.6;">Texto descritivo sobre a nova embalagem.</p>
  <div style="display:flex;flex-wrap:wrap;gap:16px;">
    <figure style="flex:1 1 200px;margin:0;position:relative;border-radius:12px;overflow:hidden;">
      <img src="URL-ANTES" alt="Embalagem anterior do [Nome]" style="width:100%;display:block;" width="1080" height="1080">
      <span style="position:absolute;bottom:8px;left:8px;background:rgba(0,0,0,0.5);color:#fff;font-size:0.625rem;font-weight:800;padding:3px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.08em;">Antes</span>
    </figure>
    <figure style="flex:1 1 200px;margin:0;position:relative;border-radius:12px;overflow:hidden;">
      <img src="URL-DEPOIS" alt="Nova embalagem do [Nome]" style="width:100%;display:block;" width="1080" height="1080">
      <span style="position:absolute;bottom:8px;left:8px;background:rgba(0,0,0,0.5);color:#fff;font-size:0.625rem;font-weight:800;padding:3px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.08em;">Agora</span>
    </figure>
  </div>
</div>
```

---

### T3 — `packaging-change-adendo.html` · Adendo de Mudança de Rótulo

**Não é um template standalone.** É um snippet HTML que se insere dentro de um `.html` já gerado via T1 ou T2, quando um produto passou por reformulação de rótulo ou embalagem.

**Quando usar:** usuário menciona "rótulo novo", "mudança de embalagem", "adendo de rótulo", ou o `product.md` indica reformulação.

**Posição:** primeiro filho do card, antes do flex row de dados + destaques.

**O que fazer:**

1. Inserir o bloco T3 (inline styles, sem CSS extra) como **primeiro filho** do card
2. Substituir os placeholders:

| Placeholder | Exemplo |
|---|---|
| `{{IMG_BEFORE_URL}}` | `https://raw.githubusercontent.com/escutaoveio/marcas/main/{marca}/{linha}/{arquivo_antes.jpg}` |
| `{{IMG_AFTER_URL}}` | `https://raw.githubusercontent.com/escutaoveio/marcas/main/{marca}/{linha}/{arquivo_novo.jpg}` |
| `{{IMG_BEFORE_ALT}}` | `Embalagem anterior — SOS Umidade Inject Gel 250g` |
| `{{IMG_AFTER_ALT}}` | `Nova embalagem — SOS Umidade Inject Gel 250g` |
| `{{BRAND_COLOR}}` | Hex da cor de destaque da marca |
| `{{BRAND_COLOR_ALPHA}}` | rgba com 0.12 de opacidade |

3. Atualizar o `<link>` para range ampliado (necessário para o ícone `info` preenchido):

```html
<!-- Padrão T1/T2: -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0">

<!-- Com adendo T3: -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0..1,0">
```

**Cores de marca:**

| Marca | `{{BRAND_COLOR}}` | `{{BRAND_COLOR_ALPHA}}` |
|---|---|---|
| Drylevis / Elastment | `#cf2c1f` | `rgba(207,44,31,0.12)` |
| Wood Wood | `#7a5592` | `rgba(122,85,146,0.12)` |
| Hold Stone | `#3d7a3a` | `rgba(61,122,58,0.12)` |
| LT Shine | `#b89a5a` | `rgba(184,154,90,0.12)` |

**Ícone de seta (SVG compartilhado):** use a URL direta — não copie o arquivo:
```
https://raw.githubusercontent.com/escutaoveio/e-commerce/main/products/hold-stone/pro/resina-para-pedras/arrow-dots.svg
```

**Nota técnica:** `mix-blend-mode:multiply` nas imagens elimina o fundo branco sobre os painéis coloridos. As imagens devem ser preferencialmente quadradas ou ter fundo branco.

---

### T4 — `product-calculator-template.html` · Calculadora de Rendimento

Gera o arquivo `{produto-slug}-calculator.html` — **separado** do `.html` principal. **Contém JavaScript** (intencional e permitido neste arquivo).

**Quando gerar:** produto com campo `RENDIMENTO` ou `CONSUMO` mensuráveis na seção `1.0`. Se os dados forem insuficientes, não gere — informe o usuário.

**O que adaptar no template:**

| Elemento | O que substituir |
|---|---|
| Título `<h2>` | Nome do produto |
| Subtítulo `.calc-subtitle` | Nome do produto + variante/embalagem |
| Objeto `RENDIMENTO` no JS | Valores reais do `product.md` por espessura/condição |
| Objeto `REND_NOTE` no JS | Textos explicativos de rendimento por condição |
| Objeto `PRIMER` no JS | Produtos complementares obrigatórios por substrato |
| Constante `SAFETY_MARGIN` | Margem de segurança (padrão: `1.10` = 10%) |
| URL do WhatsApp no botão de suporte | Link com texto pré-preenchido para o produto específico |

---

### T5 — `kits-description-template.html` · Kits

Template simples para produtos do tipo kit (combos, packs). HTML básico com parágrafos e especificações.

**Placeholders:**

| Placeholder | Exemplo |
|---|---|
| `[[QUANTIDADE]]` | `2 unidades` |
| `[[DESCRIÇÃO CURTA DO PRODUTO]]` | `SOS Umidade Inject Gel 250g` |
| `[[CÓDIGO]]` | Código de produto (EAN/SKU) |
| `[[Especificação N]]` + `[[Valor N]]` | Pares chave-valor de especificação técnica |

---

## Decisão: Qual Template Usar

```
O produto é um kit?
├── Sim → T5 (kits-description-template.html)
└── Não ↓

O produto tem banner dedicado?
├── Sim → T2 (product-description-banner-template.html)
└── Não → T1 (product-description-template.html)

O produto passou por reformulação de rótulo/embalagem?
├── Sim → inserir T3 no HTML gerado (como primeiro filho do card)
└── Não → nenhuma ação adicional

O produto tem dados de rendimento mensuráveis?
├── Sim → T4 → {produto-slug}-calculator.html separado
└── Não → nenhuma ação adicional
```

---

## Passo a Passo de Execução

### 1. Buscar o produto no Notion

Use o Notion MCP para buscar o produto no Catálogo de Produtos:
`notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`

Identifique e anote:
- **Marca** e **Linha** — para construir o path de saída
- Seções **1.0**, **2.0** e **3.0** — são os dados de entrada do HTML

**Path de saída:**
```
marketing/marcas/{marca-slug}/{linha-slug}/{produto-slug}.html
```

Se a pasta da linha não existir, crie-a antes de salvar.

### 2. Verificar os dados mínimos

| Seção | Mínimo obrigatório |
|---|---|
| `1.0` | Pelo menos 3 campos (cor/textura, composição + mais um) |
| `2.0` | Campo `2.1` (intro) + mínimo 2 benefícios-chave (2.2, 2.3) |
| `3.0` | Mínimo 3 perguntas com resposta |

Se os dados estiverem incompletos, pare e informe o usuário.

### 3. Decidir os templates

Use a árvore de decisão acima.

### 4. Gerar o HTML

#### 4.1 — Tag de fonte dos ícones

Primeira linha do arquivo:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0">
```
Se T3 presente: use `0..1,0` em vez de `0,0`.

#### 4.2 — Seção 1.0 → Painel de Dados

Para cada campo `1.X) LABEL: valor`:

```html
<div style="display:grid;grid-template-columns:140px 1fr;gap:16px;align-items:start;padding:14px 0;">
  <span style="display:block;color:#8c8c8c;font-size:0.625rem;font-weight:400;text-transform:uppercase;letter-spacing:0.06em;">LABEL:</span>
  <span style="display:block;color:#1a1a1a;font-size:0.8125rem;font-weight:600;">Valor exato.</span>
</div>
<div style="height:1px;background:#e6e6e6;"></div>
```

Após o último campo (sempre, independente do produto):
```html
<p style="margin:16px 0 0;font-size:0.6875rem;color:#8c8c8c;line-height:1.4;">*Rendimento pode variar conforme a porosidade e absorção da base ou o método de aplicação.</p>
```

#### 4.3 — Seção 2.0 → Painel de Destaques

- `2.1)` → `<p>` de introdução
- `2.2)` em diante → `<li>` com ícone `check_circle` (use apenas o texto após `BENEFÍCIO-CHAVE 0X:`, sem o label):

```html
<li style="display:flex;align-items:center;gap:12px;font-size:0.875rem;font-weight:600;color:#1a1a1a;">
  <span style="font-family:'Material Symbols Outlined';font-weight:normal;font-style:normal;font-size:20px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-flex;white-space:nowrap;direction:ltr;-webkit-font-smoothing:antialiased;flex-shrink:0;width:24px;height:24px;align-items:center;justify-content:center;color:#6a5b16;" aria-hidden="true">check_circle</span>
  Texto do benefício
</li>
```

#### 4.4 — Seção 3.0 → FAQ

Para cada `3.X) PERGUNTA FREQUENTE XX: texto?` + blockquote de resposta:

```html
<details style="border:0.5px solid rgba(38,38,38,0.83);border-radius:7px;background:#ffffff;overflow:hidden;">
  <summary style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;cursor:pointer;list-style:none;font-size:0.667rem;font-weight:600;letter-spacing:0.015em;text-transform:uppercase;color:#262626;">
    TEXTO DA PERGUNTA EM MAIÚSCULAS?
    <span style="font-family:'Material Symbols Outlined';font-weight:normal;font-style:normal;font-size:20px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-flex;white-space:nowrap;direction:ltr;-webkit-font-smoothing:antialiased;flex-shrink:0;color:#262626;" aria-hidden="true">keyboard_arrow_down</span>
  </summary>
  <div style="padding:0 16px 16px;font-size:0.875rem;color:#4d4d4d;line-height:1.6;">Texto exato do blockquote.</div>
</details>
```

#### 4.5 — (Condicional T3) Adendo de rótulo

- Inserir bloco T3 (inline styles, sem CSS extra) como **primeiro filho** do card
- Substituir todos os placeholders `{{...}}`
- Atualizar `<link>` para range `0..1,0`
- Verificar que as imagens estão hospedadas no repo `escutaoveio/marcas`

### 5. Gerar o calculator.html (condicional T4)

- Adapte o template com os valores de rendimento, substrato e primer
- Salve como `marketing/marcas/{marca-slug}/{linha-slug}/{produto-slug}-calculator.html`

### 6. Salvar e fazer push

| Arquivo | Path |
|---|---|
| Descrição HTML | `marketing/marcas/{marca-slug}/{linha-slug}/{produto-slug}.html` |
| Calculadora | `marketing/marcas/{marca-slug}/{linha-slug}/{produto-slug}-calculator.html` |
| Imagens de produto | `marketing/marcas/{marca-slug}/{linha-slug}/{arquivo.jpg}` |

Após salvar, fazer commit e push no repo `escutaoveio/marcas` (pasta `marketing/marcas/`):

```
cd marketing/marcas
git add {marca-slug}/{linha-slug}/
git commit -m "feat: adiciona {produto-slug} ({marca})"
git push
```

---

## Estrutura HTML Completa de Saída (T1 padrão)

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0">

<div style="box-sizing:border-box;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,sans-serif;font-size:16px;line-height:1.5;color:#1a1a1a;background:#ffffff;padding:32px 24px 40px;">
  <div style="max-width:1160px;margin:0 auto;display:flex;flex-direction:column;gap:24px;">

    <!-- SE T3: bloco de adendo aqui -->

    <div style="display:flex;flex-wrap:wrap;gap:24px;">

      <div style="flex:1.1 1 300px;box-sizing:border-box;background:#ffffff;border-radius:16px;box-shadow:0 1px 2px rgba(18,18,18,0.04);padding:32px;">
        <h1 style="margin:0 0 24px;font-size:1.25rem;line-height:1.1;font-weight:700;">Dados do Produto</h1>
        <!-- grid de linha + divider para cada campo de 1.0 -->
        <p style="margin:16px 0 0;font-size:0.6875rem;color:#8c8c8c;line-height:1.4;">*Rendimento pode variar conforme a porosidade e absorção da base ou o método de aplicação.</p>
      </div>

      <div style="flex:0.9 1 280px;box-sizing:border-box;background:#f5f5f5;border-radius:16px;box-shadow:0 1px 2px rgba(18,18,18,0.04);padding:32px;">
        <h2 style="margin:0 0 24px;font-size:1.25rem;line-height:1.1;font-weight:700;">Destaques do Produto</h2>
        <p style="margin:0 0 24px;font-size:0.9375rem;color:#4d4d4d;line-height:1.6;"><!-- campo 2.1 --></p>
        <ul style="list-style:none;padding:0;margin:0;display:grid;gap:12px;">
          <!-- <li> com check_circle para cada benefício de 2.2 em diante -->
        </ul>
      </div>

    </div>

    <div style="box-sizing:border-box;background:#f7f7f7;border-radius:16px;box-shadow:0 1px 2px rgba(18,18,18,0.04);padding:32px;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;">
        <span style="font-family:'Material Symbols Outlined';font-weight:normal;font-style:normal;font-size:20px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-flex;white-space:nowrap;direction:ltr;-webkit-font-smoothing:antialiased;width:28px;height:28px;align-items:center;justify-content:center;border-radius:50%;color:#262626;" aria-hidden="true">help</span>
        <p style="margin:0;font-size:0.75rem;font-weight:800;letter-spacing:0.13em;text-transform:uppercase;color:#1a1a1a;">Perguntas Frequentes</p>
      </div>
      <div style="display:grid;gap:8px;">
        <!-- <details>/<summary> com keyboard_arrow_down para cada pergunta de 3.0 -->
      </div>
    </div>

  </div>
</div>
```

---

## Ícones por Posição

| Localização | Ícone Material Symbols | `text-transform:none` obrigatório? |
|---|---|---|
| Cada `<li>` de benefício | `check_circle` | Sim |
| Header do bloco FAQ | `help` | Sim |
| Cada `<summary>` do accordion | `keyboard_arrow_down` | Sim — `<summary>` herda `uppercase` |
| Disclaimer do adendo T3 | `info` (com `font-variation-settings:'FILL' 1`) | Sim |

---

## Regras Críticas

| Regra | Detalhe |
|---|---|
| Nunca usar `<style>` com classes | Wake Commerce exibe o CSS como texto na vitrine |
| Nunca embutir imagens base64 | Inflam o arquivo para >1MB; usar sempre URLs raw do GitHub |
| Nunca reescrever conteúdo | Transcrever os valores do `product.md` exatamente |
| Nunca inventar dados ausentes | Campo ausente = elemento HTML omitido |
| `text-transform:none` inline obrigatório | Em todo `<span>` de ícone — ícones dentro de `<summary>` viram texto sem isso |
| `aria-hidden="true"` em todos os ícones | Todos os `<span>` de ícone são decorativos |
| `<summary>` sempre em MAIÚSCULAS | O `<span>` do `keyboard_arrow_down` vem **após** o texto |
| Sem JavaScript no `.html` principal | Accordion usa `<details>/<summary>` nativos |
| Sem frameworks CSS | Não usar Bootstrap, Tailwind ou similares |
| Nenhum placeholder restante | Nenhum `{{...}}` ou `[[...]]` pode permanecer no output |

---

## Checklist de Revisão

**Estrutura:**
- [ ] Sem `<html>`, `<head>`, `<body>` ou `<script>` no arquivo principal
- [ ] Começa com `<link rel="stylesheet">` para Material Symbols
- [ ] Nenhum bloco `<style>` no arquivo

**Ícones:**
- [ ] `<link>` com range `0..1,0` quando há adendo T3; `0,0` nos demais casos
- [ ] Todo `<span>` de ícone tem `font-family:'Material Symbols Outlined'` inline
- [ ] Todo `<span>` de ícone tem `text-transform:none` inline
- [ ] Todos os `<span>` de ícone com `aria-hidden="true"`

**Seção 1.0:**
- [ ] Cada campo tem grid de linha + divider
- [ ] Nota de rodapé após o último campo

**Seção 2.0:**
- [ ] Campo 2.1 no `<p>` do painel
- [ ] Cada benefício tem `<li>` com `check_circle`, sem o label numerado

**Seção 3.0:**
- [ ] Cada pergunta tem `<details>/<summary>`
- [ ] Texto do `<summary>` em MAIÚSCULAS
- [ ] `keyboard_arrow_down` após o texto no `<summary>`

**Contagem:**
- [ ] Exatamente um `<h1>` (`Dados do Produto`)
- [ ] `<h2>` (`Destaques do Produto`) vem após o `<h1>`

**Adendo T3 (se aplicável):**
- [ ] Bloco T3 é o **primeiro filho** do card
- [ ] `<link>` com range `0..1,0`
- [ ] Todos os placeholders `{{...}}` substituídos
- [ ] Imagens hospedadas no repo `escutaoveio/marcas` com URL raw

---

## Erros Comuns

| Erro | Consequência | Como evitar |
|---|---|---|
| Usar `<style>` com classes CSS | Wake Commerce exibe CSS como texto na vitrine | Todo estilo deve estar em `style=""` inline |
| Imagem base64 embutida no HTML | Arquivo >1MB, falha no Wake Commerce | Hospedar no repo `escutaoveio/marcas` e usar URL raw |
| Omitir `text-transform:none` no span do ícone | Ícones do FAQ viram texto dentro do `<summary>` | Copiar o inline style completo do ícone |
| `<span>` do accordion antes do texto no `<summary>` | Layout invertido | Ícone sempre **após** o texto |
| Incluir label `BENEFÍCIO-CHAVE 01:` no `<li>` | Texto errado na vitrine | Usar apenas o valor após os dois pontos |
| `<link>` com range `0,0` quando há adendo T3 | Ícone `info` não renderiza preenchido | Mudar para `0..1,0` quando T3 estiver presente |
| Inserir adendo T3 após o flex row | Ordem visual incorreta | T3 é sempre **primeiro filho** do card |
| Gerar `calculator.html` sem dados reais de rendimento | Calculadora imprecisa | Parar e informar o usuário se os dados forem insuficientes |

---

## Referências de Arquivo

| Arquivo | Papel |
|---|---|
| `.claude/templates/product-description-template.html` | T1 — template padrão (inline styles) |
| `.claude/templates/product-description-banner-template.html` | T2 — variante com banner |
| `.claude/templates/packaging-change-adendo.html` | T3 — adendo de reformulação de rótulo |
| `.claude/templates/product-calculator-template.html` | T4 — calculadora de rendimento |
| `.claude/templates/kits-description-template.html` | T5 — descrição de kits |
| `.claude/agents/agente-html-description.md` | Agente executor — exemplos inline e checklist |

**Fonte de dados:** Notion Catálogo de Produtos — `notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`

**Host de imagens:** `https://github.com/escutaoveio/marcas` (público) — repo `marketing/marcas/` deste repositório
