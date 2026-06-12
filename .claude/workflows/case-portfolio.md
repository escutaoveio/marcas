# Case de Portfólio — Guia de Componentes, Estrutura e Narrativa

> **Arquivo de referência:** `apresentação/case.html`
> **Última revisão:** 2026-06-02

---

## O que é este documento

Guia completo para construir, entender e reutilizar o template de case de portfólio. Cobre a narrativa estratégica de cada seção, a estrutura HTML de cada componente, os tokens de design e as regras de preenchimento.

---

## Visão Geral da Estrutura

O case é uma página HTML single-file com 8 seções em sequência narrativa:

```
Header (sticky)
  ├── 01 Hero / Capa
  ├── 02 Resultados (Big Numbers)
  ├── 03 Sobre o Projeto
  ├── 04 Processo
  ├── 05 Detalhes Técnicos
  ├── 06 Conclusão
  └── Footer
```

**Princípio de navegação:** o `<header>` é sticky com links âncora para cada seção (`#resultados`, `#sobre`, `#processo`, `#detalhes`, `#conclusao`). Toda seção com `id` recebe âncora.

---

## Design Tokens

Todas as cores, tipografias e espaçamentos são definidos como variáveis CSS em `:root`. Altere aqui para mudar o visual inteiro.

### Cores

| Token | Valor | Uso |
|---|---|---|
| `--veio-preto` | `#2D2D2B` | Fundo dark, texto principal |
| `--veio-preto-soft` | `#1F1F1E` | Variação mais escura |
| `--veio-branco` | `#FFFFFF` | Fundo padrão |
| `--veio-cinza` | `#EEEDEE` | Fundo suave de seções alternadas |
| `--veio-cinza-2` | `#D9D9D9` | Bordas, barras de progresso vazias |
| `--veio-cinza-3` | `#B4B3B3` | Texto terciário, textos em dark |
| `--veio-amarelo` | `#FEBF13` | Accent principal — destaques, CTAs, ícones |
| `--veio-laranja` | `#FAA900` | Accent secundário |

**Semântica de cor:**
- `--bg-page` = branco · `--bg-soft` = cinza · `--bg-dark` = preto
- `--fg-1` = texto primário · `--fg-2` = texto secundário · `--fg-3` = texto terciário
- `--accent` = amarelo
- `--fg-on-dark` = branco (texto sobre fundos escuros)

### Tipografia

| Token | Fonte | Uso |
|---|---|---|
| `--font-body` | Inter | Corpo de texto, labels, parágrafos |
| `--font-display` | Poppins | Títulos, números grandes, headings de seção |

Pesos utilizados: Inter 300–800 · Poppins 600, 700, 800.

**Escala de tamanhos:**

| Token | Valor | Uso típico |
|---|---|---|
| `--text-xs` | 12px | Labels uppercase, eyebrows, chips |
| `--text-sm` | 14px | Parágrafos secundários, tags |
| `--text-base` | 16px | Corpo principal |
| `--text-md` | 18px | Parágrafos de destaque, step titles |
| `--text-xl` | 24px | Subtítulos de card |
| `--text-2xl` | 32px | Títulos de seção |
| `--text-3xl` | 44px | — |
| `--text-4xl` | 60px | Heading do Hero |

Títulos de seção usam `clamp()`: `clamp(22px, 3vw, 32px)` — responsivo sem media query.

### Espaçamento

Escala em múltiplos de 4px: `--space-4` a `--space-96`. Uso padrão: `--space-96` para padding vertical de seções (`.wrap`), `--space-48` para margens entre blocos, `--space-24` para gaps de grid.

### Outros tokens

```css
--radius-sm: 8px   --radius-md: 12px   --radius-lg: 16px
--radius-xl: 24px  --radius-pill: 999px

--shadow-rest:  0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.04)
--shadow-hover: 0 2px 4px rgba(0,0,0,.06), 0 16px 40px rgba(0,0,0,.08)

--ease-standard: cubic-bezier(0.2, 0.8, 0.2, 1)
--dur-normal: 180ms
```

---

## Layout Base

**Wrapper de seção:**

```html
<section id="ancora" class="bg-soft">
  <div class="wrap">
    <!-- conteúdo -->
  </div>
</section>
```

`.wrap` = `max-width: 1100px`, `margin: 0 auto`, `padding: 96px 32px`.

**Alternância de fundo entre seções:**
- Seção clara (padrão): sem classe extra → fundo `#FFFFFF`
- Seção acinzentada: adicionar `.bg-soft` → fundo `#EEEDEE`
- Seção escura: adicionar `.bg-dark` → fundo `#2D2D2B`

**Padrão de abertura de seção:**

```html
<p class="eyebrow eyebrow--dark">Rótulo curto</p>
<p class="section-title">Título da seção</p>
```

`.eyebrow` = texto 12px uppercase com letter-spacing. Variantes: `.eyebrow--accent` (amarelo) · `.eyebrow--dark` (cinza).
`.section-title` = Poppins 700, `clamp(22px, 3vw, 32px)`, `margin-bottom: 48px`.

---

## Componentes por Seção

---

### Header (sticky)

**Narrativa:** presença permanente na tela. Ancora a identidade do case e permite navegação rápida.

```html
<header class="header">
  <img class="header__logo" src="logo.svg" alt="Nome do Projeto">
  <nav class="header__nav">
    <a href="#resultados">Resultados</a>
    <a href="#sobre">Sobre</a>
    <!-- demais links -->
  </nav>
  <div class="header__badge">Case <strong>E-commerce</strong></div>
</header>
```

**CSS key:** `position: sticky; top: 0; z-index: 50; backdrop-filter: blur(10px); background: rgba(255,255,255,.92)`.

**Regras:**
- O `.header__nav` some em telas < 900px
- O `.header__badge` identifica o tipo de case (substitua o texto)
- A logo deve ter `height: 40px`

---

### 01 — Hero / Capa

**Narrativa:** primeira impressão. Deve comunicar em 5 segundos: o que foi feito, para quem, em que contexto e o resultado principal. Fundo escuro cria contraste visual com o resto da página.

```html
<section class="hero">
  <!-- meta tags: tipo de case, plataforma, período -->
  <div class="hero__meta">
    <span class="hero__tag hero__tag--accent">Case de Portfólio</span>
    <span class="hero__tag">Wake Commerce</span>
    <span class="hero__tag">2024–2025</span>
  </div>

  <!-- título principal: conciso, impactante, com destaque em cor -->
  <h1>E-commerce do <span class="hi">Zero</span> ao Ar.</h1>

  <!-- subtítulo: resume o problema resolvido e a abordagem -->
  <p class="hero__sub">
    De dados históricos fragmentados e resultados imprevisíveis a uma operação
    estruturada em três fases — Tráfego, Conversão e Relacionamento.
  </p>

  <!-- placeholder para screenshot ou mockup -->
  <div class="hero__mockup">
    [ Mockup da loja ao vivo — substituir por <img> após lançamento ]
  </div>

  <!-- metadados: projeto, segmento, plataforma, escala -->
  <div class="hero__info">
    <div class="hero__info-item"><strong>Projeto:</strong> Nome</div>
    <div class="hero__info-item"><strong>Segmento:</strong> Setor</div>
    <div class="hero__info-item"><strong>Plataforma:</strong> Plataforma</div>
    <div class="hero__info-item"><strong>Marcas:</strong> N</div>
  </div>
</section>
```

**CSS key:** `min-height: 88vh; background: var(--veio-preto); color: var(--fg-on-dark)`. O `::before` adiciona um gradiente radial amarelo sutil saindo da parte inferior — dá profundidade sem poluir.

**`.hero__tag--accent`** = tag em destaque (amarelo + texto preto). Use para o tipo principal do case.

**`.hi`** = `color: var(--veio-amarelo)`. Use para destacar a palavra mais impactante do título.

**`.hero__mockup`** = placeholder `16:9` com borda sutil. Substitua pelo `<img>` ou `<video>` real quando disponível.

---

### 02 — Resultados (Big Numbers)

**Narrativa:** prova concreta. Números grandes antes da explicação — cria expectativa e ancora o valor entregue. **Não publicar com campos em branco.** Preencher somente com dados reais.

```html
<section id="resultados" class="bg-soft">
  <div class="wrap">
    <p class="eyebrow eyebrow--dark">Big Numbers</p>
    <p class="section-title">Resultados</p>

    <div class="results-grid">
      <!-- Repita este bloco para cada métrica (máx. 6 para 3 colunas) -->
      <div class="result-card">
        <div class="result-card__num">12</div>
        <div class="result-card__label">Semanas do zero ao lançamento</div>
      </div>
      <!-- ... -->
    </div>

    <!-- Nota de contexto ou ressalva sobre os dados -->
    <div class="results-note">
      <strong>Nota.</strong> Texto explicativo sobre metodologia ou período de medição.
    </div>
  </div>
</section>
```

**`.results-grid`** = `grid-template-columns: repeat(3, 1fr)`. Para 4 cards, muda para `repeat(2, 1fr)` ou `repeat(4, 1fr)`.

**`.result-card__num`** = Poppins 700, `clamp(36px, 5vw, 52px)`. Números grandes com `letter-spacing: -0.02em`.

Use `.placeholder` no `__num` enquanto aguarda dados reais:
```html
<div class="result-card__num"><span class="placeholder">—</span></div>
```
`.placeholder` = `color: var(--veio-cinza-2)` — cinza claro que sinaliza campo vazio.

**`.results-note`** = barra lateral amarela com fundo amarelo suave. Use para contexto, ressalvas ou alertas sobre os dados.

---

### 03 — Sobre o Projeto

**Narrativa:** contexto e problema. Explica quem é o cliente, qual era o cenário antes, qual é o objetivo estratégico. Divide em dois lados: a descrição do projeto (esquerda) e o problema real (direita, em card escuro).

```html
<section id="sobre">
  <div class="wrap">
    <p class="eyebrow">Contexto</p>
    <p class="section-title">Sobre o projeto</p>

    <div class="sobre-layout">  <!-- grid 2 colunas -->

      <!-- Coluna esquerda: descrição + metadados -->
      <div>
        <p class="sobre-descricao">
          Parágrafo principal descrevendo o cliente e o cenário.
          Borda esquerda amarela. Fonte 18px cinza.
        </p>

        <div class="sobre-meta">  <!-- grid 2×2 -->
          <div class="meta-item">
            <div class="meta-item__label">Objetivo</div>
            <div class="meta-item__value">Texto do objetivo</div>
          </div>
          <div class="meta-item">
            <div class="meta-item__label">Público-alvo</div>
            <div class="meta-item__value">Descrição do público</div>
          </div>
          <div class="meta-item">
            <div class="meta-item__label">Plataformas</div>
            <div class="meta-item__value">Ferramentas principais</div>
          </div>
          <div class="meta-item">
            <div class="meta-item__label">Link da loja</div>
            <div class="meta-item__value placeholder">— a preencher —</div>
          </div>
        </div>
      </div>

      <!-- Coluna direita: card escuro com o problema real -->
      <div class="desafio-card">
        <h3>O problema real</h3>
        <p>Descrição objetiva do problema central.</p>
        <ul class="objetivo-list">
          <li>Problema específico 1</li>
          <li>Problema específico 2</li>
          <li>Problema específico 3</li>
        </ul>
      </div>

    </div>
  </div>
</section>
```

**`.sobre-descricao`** = `border-left: 3px solid var(--veio-amarelo)`, `padding-left: 24px`, fonte 18px.

**`.desafio-card`** = fundo `--veio-preto`, `border-radius: 24px`. O `<h3>` é amarelo. Os `<li>` usam `→` amarelo como bullet (via `::before`).

**`.meta-item__label`** = eyebrow style (12px uppercase). **`.meta-item__value`** = 14px peso 500.

---

### 04 — Processo

**Narrativa:** o "como foi feito". Lista cronológica de etapas com número, título, descrição e tags de contexto. Funciona como linha do tempo vertical.

```html
<section id="processo" class="bg-soft">
  <div class="wrap">
    <p class="eyebrow eyebrow--dark">Como foi feito</p>
    <p class="section-title">Processo</p>

    <div class="processo-steps">

      <!-- Repita este bloco para cada etapa -->
      <div class="step">
        <div class="step__num">01</div>
        <div class="step__body">
          <div class="step__title">Título da etapa</div>
          <div class="step__desc">
            Descrição da etapa — o que foi feito, por quê, qual foi o resultado ou aprendizado.
          </div>
          <div class="step__tags">
            <span class="step__tag">tag 1</span>
            <span class="step__tag">tag 2</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
```

**`.step`** = `grid-template-columns: 48px 1fr`. O número fica em coluna fixa de 48px.

**`.step__num`** = quadrado 48×48px, fundo amarelo, Poppins 700, texto preto.

**`.step__body`** = tem `border-bottom: 1px solid var(--border-1)` entre steps. O último step remove a borda via `:last-child`.

**`.step__tag`** = pill cinza claro. Use para tecnologias, metodologias ou artefatos produzidos.

**Etapas em andamento:** use a classe `.placeholder` na `.step__desc` e apenas a tag `em andamento`:

```html
<div class="step__desc placeholder">A detalhar — descrição futura.</div>
<div class="step__tags"><span class="step__tag">em andamento</span></div>
```

---

### 05 — Detalhes Técnicos

**Narrativa:** a camada técnica do case. Quatro cards em grid 2×2, cada um focado num aspecto diferente: ferramentas, cronograma, arquitetura e desafios.

```html
<section id="detalhes">
  <div class="wrap">
    <p class="eyebrow">Técnico</p>
    <p class="section-title">Detalhes do projeto</p>

    <div class="detalhes-grid">  <!-- grid 2×2 -->

      <!-- Card 1: Ferramentas -->
      <div class="detalhe-card">
        <h3>Ferramentas utilizadas</h3>
        <div class="ferramentas-list">
          <span class="ferramenta-chip">Nome da ferramenta</span>
          <!-- repetir para cada ferramenta -->
        </div>
      </div>

      <!-- Card 2: Cronograma com barras de progresso -->
      <div class="detalhe-card">
        <h3>Cronograma estimado</h3>
        <div class="cronograma-bars">
          <div class="crono-item">
            <div class="crono-item__label">Nome da fase</div>
            <div class="crono-item__bar">
              <div class="crono-item__fill" style="width:100%"></div>
            </div>
          </div>
          <!-- repetir para cada fase; ajuste width: de 0% a 100% -->
        </div>
      </div>

      <!-- Card 3: Arquitetura de agentes / sistemas -->
      <div class="detalhe-card">
        <h3>Arquitetura de agentes</h3>
        <div class="agentes-grid">
          <div class="agente-row">
            <span class="agente-row__name">Nome do agente</span>
            <span class="agente-row__role">Responsabilidade</span>
          </div>
          <!-- repetir para cada agente -->
        </div>
      </div>

      <!-- Card 4: Desafios -->
      <div class="detalhe-card">
        <h3>Principais desafios</h3>
        <ul class="desafio-list">
          <li>Desafio 1</li>
          <li>Desafio 2</li>
        </ul>
      </div>

    </div>
  </div>
</section>
```

**`.detalhe-card`** = fundo branco, borda `var(--border-1)`, `border-radius: 24px`, `box-shadow: var(--shadow-rest)`.

**`.ferramenta-chip`** = pill com `border: 1.5px solid var(--veio-preto)`. Texto preto, fundo transparente.

**`.crono-item__bar`** = barra cinza; **`.crono-item__fill`** = preenchimento amarelo. O `width` inline controla o progresso (0% a 100%).

**`.agente-row`** = `display: flex; justify-content: space-between`. Nome em peso 500, role em cinza.

**`.desafio-list li`** = `border-left: 2px solid var(--veio-cinza-2)`, `padding-left: 16px`.

---

### 06 — Conclusão

**Narrativa:** fechamento reflexivo. Três ângulos em cards coloridos diferentes: aprendizados (neutro), impacto (escuro/sério) e próximos passos (amarelo/otimista). A variação de cor reforça a progressão emocional.

```html
<section id="conclusao" class="bg-soft">
  <div class="wrap">
    <p class="eyebrow eyebrow--dark">Encerramento</p>
    <p class="section-title">Conclusão</p>

    <div class="conclusao-grid">  <!-- grid 3 colunas -->

      <!-- Card 1: Aprendizados — fundo cinza, tom neutro-reflexivo -->
      <div class="conclusao-card conclusao-card--reflexao">
        <h3>Aprendizados</h3>
        <p>O que foi aprendido durante o projeto.</p>
      </div>

      <!-- Card 2: Impacto — fundo preto, tom sério -->
      <div class="conclusao-card conclusao-card--impacto">
        <h3>Impacto</h3>
        <p>Como o projeto impactou o negócio ou o cliente.</p>
      </div>

      <!-- Card 3: Próximos passos — fundo amarelo, tom otimista -->
      <div class="conclusao-card conclusao-card--proximos">
        <h3>Próximos passos</h3>
        <p>O que vem a seguir.</p>
      </div>

    </div>
  </div>
</section>
```

| Variante | Fundo | `<h3>` | `<p>` |
|---|---|---|---|
| `--reflexao` | `--veio-cinza` | `--fg-2` | `--fg-2` |
| `--impacto` | `--veio-preto` | `--veio-amarelo` | `--veio-cinza-3` |
| `--proximos` | `--veio-amarelo` | `--veio-preto` | `--veio-preto` (opacity .75) |

Use `.placeholder` nos cards enquanto os dados não estiverem disponíveis — aplica `font-style: italic; opacity: .5`.

---

### Footer

```html
<footer class="footer">
  <strong>Nome do Projeto</strong> — Tipo de Case · Subtítulo
</footer>
```

Fundo `--veio-preto`, texto `--veio-cinza-3`, `<strong>` branco. Padding 32px, texto centralizado.

---

## Responsividade

Breakpoints:

| Breakpoint | Mudanças |
|---|---|
| `max-width: 900px` | `.results-grid`, `.conclusao-grid` → 1 coluna · `.sobre-layout`, `.detalhes-grid` → 1 coluna · `.header__nav` → `display: none` · `.wrap` padding lateral reduzido |
| `max-width: 480px` | `.sobre-meta` → 1 coluna |

---

## Narrativa: Sequência Estratégica das Seções

A ordem das seções não é aleatória — segue a lógica de uma apresentação de vendas ou portfólio:

| Posição | Seção | Função narrativa |
|---|---|---|
| 1 | Hero | Impacto imediato — o que foi feito e para quem |
| 2 | Resultados | Prova — os números antes da explicação criam credibilidade |
| 3 | Sobre | Contexto — o problema que justifica o projeto |
| 4 | Processo | Método — como foi pensado e executado |
| 5 | Detalhes | Profundidade técnica — para quem quer entender os bastidores |
| 6 | Conclusão | Reflexão e continuidade — o que foi aprendido e o que vem a seguir |

**Princípio:** o leitor pode parar em qualquer ponto e já ter extraído valor. Quem lê só o Hero e os Resultados entende o impacto. Quem lê tudo entende o método.

---

## Placeholders e Campos a Preencher

Campos marcados como `placeholder` (cor cinza claro, italic) devem ser preenchidos antes de publicar:

| Seção | Campo | Quando preencher |
|---|---|---|
| Hero | `.hero__mockup` | Após ter screenshot da loja ao vivo |
| Resultados | `.result-card__num` | Após primeiras semanas de operação real |
| Sobre | `Link da loja` | Após publicação da URL |
| Processo | Steps "em andamento" | Conforme as fases avançam |
| Conclusão | Aprendizados e Impacto | Após 2–3 meses de operação |

**Regra:** não compartilhar o case com campos `placeholder` visíveis. Use a classe `.placeholder` durante o desenvolvimento para sinalizar visualmente o que falta.

---

## Guia de Adaptação para Outro Projeto

Para reutilizar o template em um novo case:

1. **Tokens de cor** — substitua `--veio-amarelo` pela cor accent do novo projeto em `:root`
2. **Logo** — troque o `src` do `.header__logo`
3. **Tags do Hero** — atualize tipo de case, plataforma e período
4. **Título do Hero** — mantenha a estrutura curta + destaque colorido (`.hi`)
5. **Big Numbers** — defina as 4–6 métricas mais impactantes antes de escrever qualquer outra coisa
6. **Sobre** — a `.sobre-descricao` deve responder: quem é o cliente + qual era o problema
7. **Desafio Card** — liste os problemas como `<li>` curtos, factuais, específicos
8. **Steps de Processo** — um step por decisão estratégica ou fase, não por tarefa
9. **Ferramentas** — apenas as que aparecem no processo — sem "laundry list"
10. **Conclusão** — os três cards devem ter tons emocionalmente distintos (reflexão / peso / otimismo)

---

## Referências de Arquivo

| Arquivo | Papel |
|---|---|
| `apresentação/case.html` | Fonte — HTML completo do case |
| `brand-system/escuta-o-v-io-design-system/project/assets/logo-*.svg` | Logo usada no header |
