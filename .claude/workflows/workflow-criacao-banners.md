# Workflow de Banners — Escuta o Véio!

Documentação completa do sistema de produção de banners no Figma via agentes orquestrados.

---

## 1. Visão geral

Produção automatizada de banners via 4 agentes orquestrados:

```
[Maestro] ← ponto de entrada único
    ↓
[Copywriter] → copy brief
    ↓
[QA]  → APROVADO ou REPROVADO (devolve feedback ao copywriter, max 2x)
    ↓ APROVADO
[Designer] → frames no Figma
```

| Agente | Responsabilidade |
|---|---|
| Maestro | Orquestra o fluxo completo |
| Copywriter | Lê o produto, gera o copy brief |
| QA | Aprova copy contra critérios da marca |
| Designer | Cria frames desktop + mobile no Figma |

---

## 2. Arquivo Figma

- **URL:** https://www.figma.com/design/6rdNvOQr0mxQeqmZQ8A3iq/Escuta-o-V%C3%A9io--%E2%80%94-Banners
- **File Key:** `6rdNvOQr0mxQeqmZQ8A3iq`
- **Time:** OGUSNTS.CO (Pro)

O `fileKey` é permanente — não muda ao mover o arquivo entre pastas ou projetos no Figma.

### Estrutura de páginas

| Página | Propósito |
|---|---|
| `[Guia] Design System` | Referência visual permanente — cores, tipografia, anatomia |
| `[Componentes]` | Componentes reutilizáveis: `Banner/H1`, `Banner/Badge`, `Banner/ProductSpot` |
| `[Template] Formatos` | Frames em branco para duplicar |
| `[Site] Vitrine` | Todos os banners de vitrine (desktop + mobile por produto) |
| `[Marketplace] ML` | Banners para Mercado Livre (900×300) |
| `[Linktree] Bio` | Banners para Linktree / Open Graph (1200×628) |

---

## 3. Formatos suportados

| ID | Dimensão | Uso | Página Figma |
|---|---|---|---|
| `site-desktop` | 1330 × 250 px | Vitrine site — desktop | `[Site] Vitrine` |
| `site-mobile` | 680 × 300 px | Vitrine site — mobile | `[Site] Vitrine` |
| `ml-desktop` | 900 × 300 px | Mercado Livre | `[Marketplace] ML` |
| `linktree` | 1200 × 628 px | Linktree / Open Graph | `[Linktree] Bio` |

---

## 4. Copy Schema

Schema obrigatório para o output do copywriter. Todos os campos seguem a voz do Véio e o ritmo **problema → solução → ação**.

### Campos

| Campo | Obrigatório | Limite | Propósito |
|---|---|---|---|
| `eyebrow` | sim | 24 chars | Identificação da marca e linha |
| `h1` | sim | 45 chars | Headline — problema-primeiro, voz do Véio |
| `subtitle` | sim | 90 chars | Produto + benefício principal |
| `cta` | sim | 20 chars | Ação clara — sentence case, com seta `→` |
| `badge` | não | 15 chars | Destaque opcional — urgência, kit, novidade |
| `alt_text` | sim | 125 chars | Acessibilidade e SEO |

### Regras por campo

**eyebrow**
- Formato: `MARCA · LINHA` (tudo uppercase, espaço antes e depois do `·`)
- Exemplos: `DRYLEVIS · COLAS & REJUNTES`, `ELASTMENT · REPAROS`
- Nunca: descrição de produto, frase longa

**h1**
- Começa com o problema ou situação — nunca com o produto
- Termina com ponto final `.` — nunca com `!`
- Sem palavras corporativas: "inovador", "solução completa", "experiência", "transformar", "jornada"
- Exemplos válidos: `Junta que infiltra tem solução.`, `Umidade no bloco — agora tem jeito.`

**subtitle**
- Nomeia o produto + benefício diferencial
- Pode usar dois-pontos: `DW240: mais forte que silicone, elástico e pronto pra usar.`
- Nunca repete o h1

**cta**
- Sentence case (primeira letra maiúscula, restante minúsculo)
- Termina com `→` (sem espaço antes)
- Exemplos: `Ver solução→`, `Comprar agora→`, `Falar com o Véio→`
- Nunca: ALL CAPS, ponto final

**badge** (opcional)
- Só quando há destaque real: kit, lançamento, oferta ativa
- Exemplos: `Kit completo`, `LANÇAMENTO`, `Leve 2 pague 1`

**alt_text**
- Formato: `MARCA PRODUTO | Descrição`
- Primeira parte: marca + nome comercial em caixa alta
- Separador: ` | ` (espaço, pipe, espaço)
- Segunda parte: sentence case — oferta ativa ou proposta de valor com SEO
- Exemplos:
  - `ELASTMENT SCUDO PRO | Tinta Cimentícia Impermeável para Piso e Área Úmida`
  - `DRYLEVIS SELANTE ADESIVO DW240 | Vede, fixe e proteja diferentes superfícies`

### Formato do arquivo copy brief

```markdown
---
produto: [nome do produto]
marca: [nome da marca]
linha: [linha do produto]
formatos: [desktop, mobile]
---

## Copy

**eyebrow:** `[texto]`
**h1:** `[texto]`
**subtitle:** `[texto]`
**cta:** `[texto]`
**badge:** `[texto ou — se não aplicável]`
**alt_text:** `[texto]`

## Notas do copywriter

[Justificativa breve das escolhas — qual problema foi priorizado e por quê.]
```

---

## 5. Voz da marca — o Véio

- Direto, sem rodeios. Uma ideia por frase.
- Warm authority: fala como quem já viu o problema mil vezes e sabe a solução.
- **Ritmo:** problema → solução → ação
- Tuteia o leitor ("você", nunca "o cliente" ou "o senhor")
- Imperativos bem-vindos: "Olha aqui.", "Resolve de vez."
- **Proibido:** "soluções inovadoras", "experiência única", "transformamos", "jornada"
- Sem emoji. Sem exclamações desnecessárias.

---

## 6. Critérios de QA

O QA verifica todos os critérios abaixo antes de aprovar. Todos são obrigatórios.

### Limites de caracteres

| Campo | Limite |
|---|---|
| `eyebrow` | ≤ 24 chars |
| `h1` | ≤ 45 chars |
| `subtitle` | ≤ 90 chars |
| `cta` | ≤ 20 chars |
| `badge` | ≤ 15 chars (quando presente) |
| `alt_text` | ≤ 125 chars |

### Checklist de formato

**eyebrow**
- [ ] Formato `MARCA · LINHA` em uppercase
- [ ] Separador é `·` com espaço antes e depois
- [ ] Sem descrição de produto ou frase

**h1**
- [ ] Começa com o problema ou situação
- [ ] Termina com `.` — nunca com `!`
- [ ] Sem palavras corporativas

**subtitle**
- [ ] Nomeia o produto explicitamente
- [ ] Avança a narrativa — não repete o h1
- [ ] Entrega benefício, não lista de features

**cta**
- [ ] Sentence case
- [ ] Termina com `→` sem espaço antes
- [ ] Sem ponto final, nunca ALL CAPS

**alt_text**
- [ ] Formato `MARCA PRODUTO | Descrição` respeitado
- [ ] Sem emoji e sem exclamação

### Output do QA

**Se aprovado:**
```
STATUS: APROVADO

Resumo: [1-2 linhas explicando por que a copy passa]
```

**Se reprovado:**
```
STATUS: REPROVADO

Problemas encontrados:
- [campo]: [descrição do problema] → [sugestão de direção]

Instrução para o copywriter: [o que revisar e por quê]
```

Limite: máximo 2 reprovações. Na 3ª, escalar para o usuário.

---

## 7. Design System — Visual

### Paleta de cores

| Token | HEX | Uso no banner |
|---|---|---|
| `preto` | `#2D2D2B` | Seção, placa escura |
| `branco` | `#FFFFFF` | Texto H1, badge, product spot |
| `cinza` | `#DADADA` | Fill do banner (placeholder) |
| `cinza-overlay` | `#E7E7E7` | Overlay (100% opacidade) |
| `amarelo` | `#FEBF13` | Reservado para CTA — não usar no banner |
| `laranja` | `#FAA900` | h1-bar |

### Tipografia

| Família | Uso | Fonte |
|---|---|---|
| **Poppins Bold** | H1 do banner | Google Fonts |
| **Inter Bold** | Badge | Google Fonts |
| **Inter Medium** | Product spot label | Google Fonts |
| **Raleway** | Somente no logo — nunca no copy do banner | Google Fonts |

### H1 — Tipografia por formato

| Formato | `fontSize` | `lineHeight` | `textCase` |
|---|---|---|---|
| `site-desktop` | `36` | `111%` | `UPPER` |
| `site-mobile` | `24` | `111%` | `UPPER` |
| `ml-desktop` | `28` | `111%` | `UPPER` |
| `linktree` | `48` | `111%` | `UPPER` |

---

## 8. Arquitetura do banner — Auto Layout

O banner inteiro é um frame de auto layout vertical. Nenhum elemento de copy usa coordenadas x/y absolutas — tudo vive dentro do fluxo de auto layout.

```
banner [FRAME, VERTICAL, padding=25, FIXED W×H]
  ├── overlay              [RECT, ABSOLUTE, #E7E7E7 100%, cobre o frame inteiro]
  ├── header-row           [FRAME, HORIZONTAL, FILL×FIXED 25px, badge à direita]
  │   └── Banner/Badge     [INSTANCE — texto = segunda parte do eyebrow]
  └── body-row             [FRAME, HORIZONTAL, FILL×FILL]
      ├── spacer-left      [FRAME, FIXED width × FILL]
      ├── h1-block         [FRAME, VERTICAL, FIXED width × HUG]
      │   ├── Banner/H1    [INSTANCE, FILL×HUG]
      │   └── Banner/ProductSpot [INSTANCE — site-desktop e site-mobile apenas]
      └── fill-block       [FRAME, FILL×FILL]
```

**Overlay:** `#E7E7E7` com opacidade 100% — nunca cor preta nem opacidade parcial.
**Banner fill:** `#DADADA` — o usuário substitui por imagem real.

### Specs por formato

**site-desktop (1330 × 250 px)**

| Propriedade | Valor |
|---|---|
| padding todos os lados | 25 px |
| header-row height | 25 px |
| body-row height | 175 px (FILL) |
| spacer-left width | 165 px |
| h1-block width | 500 px (FIXED) |
| h1-block.itemSpacing | 12 px |

**site-mobile (680 × 300 px)**

| Propriedade | Valor |
|---|---|
| padding todos os lados | 20 px |
| header-row height | 20 px |
| body-row height | 240 px (FILL) |
| spacer-left width | 38 px |
| h1-block width | 280 px (FIXED) |
| h1-block.itemSpacing | 8 px |

---

## 9. Componentes Figma

### Banner/H1

Frame de auto layout vertical com texto (Poppins Bold) e barra laranja.

| Propriedade | Valor |
|---|---|
| `layoutMode` | `"VERTICAL"` |
| `primaryAxisSizingMode` | `"AUTO"` (HUG) |
| Font | Poppins Bold, `textCase: UPPER`, `#FFFFFF` |
| h1-bar | RECT 60×4 px, `#FAA900`, `cornerRadius: 0` |
| `itemSpacing` | 8 px |

No banner, a instância usa `layoutSizingHorizontal = "FILL"` dentro do h1-block.

### Banner/Badge

Frame de auto layout horizontal com texto (Inter Bold) e ícone seta.

| Propriedade | Valor |
|---|---|
| `layoutMode` | `"HORIZONTAL"` |
| `itemSpacing` | 4 px |
| `padding` H/V | 8 / 4 px |
| `cornerRadius` | 10.25 px |
| Fill | `#2D2D2B` a 50% de opacidade |
| Stroke | `#FFFFFF`, 0.5px, `INSIDE` |
| Font | Inter Bold, 9.81 px, UPPER, letterSpacing 8%, `#FFFFFF` |

Texto = segunda parte do `eyebrow`. Ex: `"DRYLEVIS · REPAROS"` → `"REPAROS"`.
Posição: dentro do `header-row` com `primaryAxisAlignItems = "MAX"`.

### Banner/ProductSpot

Frame de auto layout horizontal com placeholder de imagem e label do produto.

| Propriedade | Valor |
|---|---|
| `layoutMode` | `"HORIZONTAL"` |
| `itemSpacing` | 8 px |
| `padding` todos os lados | 8 px |
| `cornerRadius` | 8 px |
| Fill | `[]` (sem fill) |
| Effect | `glass-effect` |
| `img-placeholder` | RECT 44×44 px, `#FFFFFF`, `cornerRadius: 5` |
| Font | Inter Medium, 10.88 px, `#FFFFFF` |

Texto do label: nome do produto sem a marca (campo `produto:` do brief).
Presente apenas em site-desktop e site-mobile.

**Glass effect (manual):**
```js
spot.effects = [{
  type: "GLASS",
  visible: true,
  lightAngle: 62,
  lightIntensity: 0.8,
  refraction: 0.37,
  depth: 11.88,
  dispersion: 0.31,
  splay: 0.54,
  radius: 2.64
}];
```

---

## 10. Código de criação — site-desktop

```js
const W=1330, H=250, PAD=25, SPACER=165, H1W=500, HEADER_H=25, ITEM_SP=12;

// Banner frame
const banner = figma.createFrame();
banner.name = "banner-desktop";
banner.resize(W, H);
banner.fills = [{ type: "SOLID", color: { r: 0.855, g: 0.855, b: 0.855 } }]; // #DADADA
banner.layoutMode = "VERTICAL";
banner.primaryAxisSizingMode = "FIXED";
banner.counterAxisSizingMode = "FIXED";
banner.paddingTop = banner.paddingBottom = banner.paddingLeft = banner.paddingRight = PAD;
banner.itemSpacing = 0;
banner.clipsContent = true;

// Overlay (ABSOLUTE)
const overlay = figma.createRectangle();
overlay.name = "overlay";
overlay.resize(W, H);
overlay.fills = [{ type: "SOLID", color: { r: 0.906, g: 0.906, b: 0.906 } }]; // #E7E7E7
banner.appendChild(overlay);
overlay.layoutPositioning = "ABSOLUTE";
overlay.constraints = { horizontal: "SCALE", vertical: "SCALE" };
overlay.x = 0; overlay.y = 0;

// header-row
const hdr = figma.createFrame();
hdr.name = "header-row";
hdr.layoutMode = "HORIZONTAL";
hdr.primaryAxisSizingMode = "FIXED";
hdr.counterAxisSizingMode = "FIXED";
hdr.resize(W - PAD*2, HEADER_H);
hdr.fills = [];
hdr.primaryAxisAlignItems = "MAX";    // badge à direita
hdr.counterAxisAlignItems = "CENTER";
banner.appendChild(hdr);
hdr.layoutSizingHorizontal = "FILL"; // FILL só funciona após append

// badge no header-row
const badgeInst = badgeComp.createInstance();
hdr.appendChild(badgeInst);
const badgeTxt = badgeInst.findOne(n => n.type === "TEXT");
await figma.loadFontAsync(badgeTxt.fontName);
badgeTxt.characters = badgeText; // segunda parte do eyebrow

// body-row
const body = figma.createFrame();
body.name = "body-row";
body.layoutMode = "HORIZONTAL";
body.primaryAxisSizingMode = "FIXED";
body.counterAxisSizingMode = "FIXED";
body.resize(W - PAD*2, H - PAD*2 - HEADER_H);
body.fills = [];
body.itemSpacing = 0;
body.counterAxisAlignItems = "MIN";  // top-align
banner.appendChild(body);
body.layoutSizingHorizontal = "FILL";
body.layoutSizingVertical = "FILL";

// spacer-left
const spacer = figma.createFrame();
spacer.name = "spacer-left";
spacer.resize(SPACER, 10);
spacer.fills = [];
body.appendChild(spacer);
spacer.layoutSizingHorizontal = "FIXED";
spacer.layoutSizingVertical = "FILL";

// h1-block (HUG height)
const h1Block = figma.createFrame();
h1Block.name = "h1-block";
h1Block.layoutMode = "VERTICAL";
h1Block.primaryAxisSizingMode = "AUTO";   // HUG
h1Block.counterAxisSizingMode = "FIXED";
h1Block.resize(H1W, 10);
h1Block.fills = [];
h1Block.itemSpacing = ITEM_SP;
h1Block.counterAxisAlignItems = "MIN";
body.appendChild(h1Block);
h1Block.layoutSizingHorizontal = "FIXED";
h1Block.layoutSizingVertical = "HUG";

// H1 — float-first (evita bug de height=0 em auto layout)
const h1Inst = h1Comp.createInstance();
page.appendChild(h1Inst);
h1Block.appendChild(h1Inst);
h1Inst.layoutSizingHorizontal = "FILL";
h1Inst.layoutSizingVertical = "HUG";
const h1Txt = h1Inst.findOne(n => n.type === "TEXT");
await figma.loadFontAsync(h1Txt.fontName);
h1Txt.characters = h1Copy;
h1Txt.fontSize = 36;
h1Txt.layoutSizingHorizontal = "FILL";
h1Txt.layoutSizingVertical = "HUG";

// ProductSpot — float-first
const spotInst = spotComp.createInstance();
page.appendChild(spotInst);
h1Block.appendChild(spotInst);
spotInst.layoutSizingHorizontal = "FIXED";
spotInst.layoutSizingVertical = "HUG";
const spotLabel = spotInst.findOne(n => n.name === "product-label");
await figma.loadFontAsync(spotLabel.fontName);
spotLabel.characters = productName; // nome do produto sem a marca

// fill-block
const fillBlock = figma.createFrame();
fillBlock.name = "fill-block";
fillBlock.fills = [];
fillBlock.resize(10, 10);
body.appendChild(fillBlock);
fillBlock.layoutSizingHorizontal = "FILL";
fillBlock.layoutSizingVertical = "FILL";

// Section nativa
const section = figma.createSection();
section.name = "Nome do Produto";
section.fills = [{ type: "SOLID", color: { r: 0.176, g: 0.176, b: 0.169 } }]; // #2D2D2B
```

### Regras críticas de código

1. **Float-first para texto em auto layout** — criar nó na page, setar `characters`, depois `appendChild` no container. Evita bug de `height=0`.
2. **FILL após append** — `layoutSizingHorizontal/Vertical = "FILL"` só funciona depois que o nó está dentro de um frame de auto layout.
3. **textCase = "UPPER"** — nunca digitar copy em caixa alta manualmente.
4. **`createVector()` para ícones** — nunca `createNodeFromSvg()` (cria FRAME wrapper com fill branco).
5. **Path com espaço após comando:** `M 0 5.8` não `M0 5.8`.

---

## 11. Layout de página no Figma

### `[Site] Vitrine` — seções por produto

Cada produto fica dentro de uma **Section nativa do Figma** com fill `#2D2D2B`. Desktop e mobile lado a lado com 40 px de gap.

```
[Section: DW240 Selante]
  banner-desktop (1330×250)  |  banner-mobile (680×300)  [gap 40px]

[Section: Nivela+]
  banner-desktop  |  banner-mobile

[Section: Chapisco Flex]
  banner-desktop  |  banner-mobile
```

**Nunca remover sections existentes antes de recriar** — sempre criar uma nova section; nunca incluir `.remove()` em scripts de criação.

---

## 12. Badge — construção via Plugin API

```js
const KAR_PATH = "M 0 5.8 L 2.39 3.29 L 0 0.77 L 0.74 0 L 3.87 3.29 L 0.74 6.57 L 0 5.8 Z";

const badge = figma.createComponent();
badge.name = "Banner/Badge";
badge.layoutMode = "HORIZONTAL";
badge.primaryAxisSizingMode = "AUTO";
badge.counterAxisSizingMode = "AUTO";
badge.primaryAxisAlignItems = "MIN";
badge.counterAxisAlignItems = "CENTER";
badge.itemSpacing = 4;
badge.paddingLeft = badge.paddingRight = 8;
badge.paddingTop  = badge.paddingBottom = 4;
badge.cornerRadius = 10.25;
badge.fills   = [{ type: "SOLID", color: { r: 0.176, g: 0.176, b: 0.169 }, opacity: 0.5 }];
badge.strokes = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
badge.strokeWeight = 0.5;
badge.strokeAlign  = "INSIDE";
badge.clipsContent = false;

const txt = figma.createText();
txt.fontName = { family: "Inter", style: "Bold" };
txt.fontSize = 9.81;
txt.textCase = "UPPER";
txt.letterSpacing = { value: 8, unit: "PERCENT" };
txt.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
txt.textAutoResize = "WIDTH_AND_HEIGHT";
txt.characters = badgeText;
badge.appendChild(txt);

const icon = figma.createVector();
icon.name = "badge-icon";
icon.vectorPaths = [{ windingRule: "NONZERO", data: KAR_PATH }];
icon.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
icon.strokes = [];
badge.appendChild(icon);
```

---

## 13. Adaptação para outros formatos

### Mercado Livre (`ml-desktop`, 900×300)

- **Badge:** trocar nome de linha por destaque comercial
  - `REPAROS` → `Kit`, `Oferta`, `Novidade`
- **H1:** manter; adaptar apenas se contiver gíria de marca não reconhecida em ML
- **alt_text:** focar em termos de busca do marketplace; evitar linguagem de marca
- **ProductSpot:** não usar
- Página: `[Marketplace] ML`, frame name: `banner-ml`

### Linktree / Open Graph (`linktree`, 1200×628)

- **Badge:** manter linha editorial (`REPAROS`, `REVESTIMENTOS`)
- **H1:** manter; adaptar apenas se contiver referência de vitrine ou urgência de estoque
- **alt_text:** proposta de valor perene — sem desconto, sem percentual (fica cacheado meses)
- **ProductSpot:** não usar
- Página: `[Linktree] Bio`, frame name: `banner-linktree`

---

## 14. Regras que nunca quebrar

1. **Overlay obrigatório** — sempre `#E7E7E7` a 100% de opacidade; nunca cor preta nem opacidade parcial
2. **Float-first para texto em auto layout** — criar nó na page, setar `characters`, depois `appendChild`
3. **FILL após append** — `layoutSizingHorizontal/Vertical = "FILL"` só funciona após o nó estar no auto layout
4. **textCase = "UPPER"** — nunca digitar copy em caixa alta manualmente
5. **Badge sempre presente** — texto = segunda parte do `eyebrow`. O campo `badge:` do copy brief é para destaque promocional — ignorar para o badge de navegação
6. **ProductSpot sempre presente em site-desktop e site-mobile** — texto = nome do produto sem a marca
7. **Ordem das camadas** — overlay → header-row → body-row
8. **h1-block HUG height** — nunca FIXED; o h1-block deve crescer com o conteúdo
9. **Sem emoji, textura ou padrão decorativo no fundo**
10. **Nunca usar Raleway no copy** (apenas no logo)
11. **Nunca remover sections existentes** — sempre criar nova section

---

## 15. Fluxo de invocação do Maestro

### Input mínimo

Fornecer o conteúdo do produto — pode ser um `product.md` ou uma descrição direta com:
- Nome do produto e marca
- Problema principal que resolve
- Benefício-chave / diferencial
- Público prioritário
- Eventual badge/destaque comercial

### Output esperado

```
Banner criado com sucesso.

Produto: [nome]
Página no Figma: [Marca] Produto
URL: https://www.figma.com/design/6rdNvOQr0mxQeqmZQ8A3iq/...

Copy aprovada pelo QA:
- H1: "[texto]"
- Subtitle: "[texto]"
- CTA: "[texto]"
```

### Expansão futura

Próximos formatos: Meta Ads (1200×628 e 1080×1080), Shopee, TikTok Ads.
