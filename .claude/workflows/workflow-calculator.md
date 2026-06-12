# Workflow: Gerar Calculadora de Rendimento

> **Agente responsável:** `agente-calculator.md` (nesta mesma pasta)
> **Template de referência:** `templates/product-calculator-template.html` (v2.1)
> **Última revisão:** 2026-06-02

---

## O que este workflow faz

Transforma os dados técnicos do `product.md` em um bloco HTML interativo (`calculator.html`) que permite ao comprador estimar a quantidade de produto — com contexto de aplicação (revestimento final, tipo de obra, sobreposição) influenciando a lista de "Compre Junto" exibida no resultado.

O arquivo de saída é **separado** do `index.html`. Contém JavaScript (intencional — é o único arquivo do e-commerce que usa JS).

---

## Quando gerar

| Gerar | Não gerar |
|---|---|
| Produto aplicado em superfície contínua com rendimento em m²/kg ou m²/L | Produto de uso pontual sem área definível |
| Campo `RENDIMENTO` com relação mensurável entre quantidade e área | Selante de junta (rendimento em metros lineares) |
| Espessura ou condição da camada afeta o rendimento | Dados insuficientes para fórmula confiável |

Se os dados forem insuficientes, **não gere** — informe o usuário.

---

## Versão do Template: v2.1

O template atual (`product-calculator-template.html`) é a **v2.1**, com estrutura diferente das versões anteriores. Diferenças críticas em relação a versões antigas:

| Aspecto | Versão antiga | v2.1 |
|---|---|---|
| Passo 2 (condição) | Radio pills (Quase nivelado / Algumas imperfeições / Bem irregular) | Input numérico livre em mm (`min=1`, `max=15`, `step=0.5`) |
| Fórmula de rendimento | Lookup table (`RENDIMENTO = {'2': 5, '3': 3.3, '4': 2.5}`) | Fórmula linear: `rendimento = CONSTANTE / espessura_mm` |
| Context row | Não existia | Grid 3 colunas antes do formulário: revestimento final + área de uso + checkbox piso sobre piso |
| Compre Junto | Objeto estático `PRIMER[substrato]` | Função `buildCompreJunto(substrato, revFinal, sobreposicao)` — combina 3 variáveis |
| Nota dinâmica | Texto fixo por condição | Calculada em tempo real conforme o usuário digita os mm |
| Estado de aviso | Não existia | `.calc-rend-note.is-warning` para valores extremos (> max permitido) |

---

## Estrutura do Arquivo de Saída

```
products/{marca-slug}/{linha-slug}/{produto-slug}/{variante-slug}/calculator.html
```

Bloco raiz: `<div class="product-calc">` — sem `<html>`, `<head>` ou `<body>`.

---

## Anatomia da v2.1

```
<div class="product-calc">
  <style>              ← CSS completo embutido
  <div class="calc-card">
    <div class="calc-panel">
      .calc-header         ← h2 + .calc-subtitle
      .calc-divider
      .calc-context-row    ← [NOVO v2.1] 3 colunas: select revestimento + select uso + checkbox sobreposição
      .calc-divider
      <form>
        .calc-layout
          .calc-col-left   ← Passo 1: área (modo ambiente × ou m² direto)
          .calc-col-right  ← Passo 2: espessura em mm (input numérico livre)
        .calc-step-full    ← Passo 3: substrato (radio pills)
      </form>
      .calc-result         ← resultado oculto → aparece via JS
        .calc-result-main  ← contagem + breakdown
        .calc-alerts       ← compre-junto (dinâmico) + ferramentas (estático)
        .calc-safety-note
      .calc-divider
      .calc-support        ← CTA WhatsApp
    </div>
  </div>
  <script>             ← IIFE strict mode, JS puro
```

---

## Passo a Passo de Execução

### 1. Extrair dados do `product.md`

| Campo | Seção | Uso na calculadora |
|---|---|---|
| `RENDIMENTO` | `1.0` | Deriva a constante da fórmula linear |
| `CONSUMO` | `1.0` | Confirma a fórmula |
| `EMBALAGEM` | `1.0` | Label do resultado ("sacos de 20 kg", "latas de 18L"…) |
| `LOCAIS DE APLICAÇÃO` | `4.5` | Define as opções de substrato (Passo 3) |
| Primers obrigatórios | `3.0` FAQ + `8.0` Compre Junto | Lógica da função `buildCompreJunto()` |
| Ferramentas | `7.0` | Lista estática no `.calc-alert-info` |
| Revestimentos compatíveis | `5.2` Próximo Departamento + `5.3` Compre Junto | Opções do `<select>` de revestimento final |

### 2. Derivar a constante da fórmula linear

O template v2.1 usa espessura como input numérico livre. O rendimento é calculado por:

```
rendimento_m2_por_embalagem = CONSTANTE / espessura_mm
```

**Como derivar a CONSTANTE a partir do `product.md`:**

1. Pegue um ponto de rendimento conhecido do campo `RENDIMENTO`. Ex: `2mm → 5 m²/saco`
2. `CONSTANTE = rendimento × espessura = 5 × 2 = 10`
3. Verifique com outro ponto: `3mm → 10/3 = 3,33 m²` ✓ | `4mm → 10/4 = 2,5 m²` ✓

**Exemplo do Nivela+:**
```javascript
// Ficha técnica: saco 20kg cobre 5m² a 2mm de espessura
// CONSTANTE = 5 × 2 = 10
var rendimento = 10 / espMM;  // m²/saco
```

Se o produto não tiver relação linear (ex: consumo fixo independente de espessura), use a fórmula:
```javascript
var rendimento = PESO_EMBALAGEM_KG / (CONSUMO_KG_M2);
```

### 3. Definir os limites de espessura

Baseie em `1.3) CONSUMO` e `4.7) NÍVEL DE COMPLEXIDADE` do `product.md`:

```javascript
// No HTML — atributos do input de espessura:
// min="[espessura mínima]" max="[espessura máxima]" step="[incremento]"
// Ex: min="1" max="15" step="0.5"

// No JS — limite de aviso:
if (espMM > [LIMITE]) {
  rendNote.textContent = 'Para desníveis acima de [X] mm, fale com nossa equipe.';
  rendNote.classList.add('is-warning');
  resultEl.classList.remove('is-visible');
  return;
}
```

### 4. Montar a função `buildCompreJunto()`

Esta função recebe 3 parâmetros e retorna um array de strings:

```javascript
function buildCompreJunto(substrato, revFinal, sobreposicao) {
  var items = [];

  // Lógica por substrato + sobreposição (primers obrigatórios)
  if (substrato === '[substrato-A]' || sobreposicao) {
    items.push('[Primer para substrato A ou sobreposição]');
  } else {
    // substrato padrão
    items.push('[Primer padrão — instrução de uso]');
    items.push('[Alternativa — para casos específicos]');
  }

  // Lógica por revestimento final (produtos de acabamento)
  if (revFinal === '[revestimento-1]') {
    items.push('[Produto recomendado para este revestimento]');
  } else if (revFinal === '[revestimento-2]') {
    items.push('[Produto recomendado para este revestimento]');
  }

  return items;
}
```

**Regra:** array vazio é válido — significa que nenhum produto complementar é necessário para aquela combinação. O bloco amarelo de alerta não deve aparecer vazio (use `display: none` quando `items.length === 0`).

### 5. Definir as opções do Context Row

**Select "Revestimento Final"** — o que o cliente vai colocar por cima:
- Use a seção `5.2) PRÓXIMO DEPARTAMENTO` e `5.3) COMPRE JUNTO` do `product.md` para listar os revestimentos compatíveis
- Adicione uma opção vazia inicial: `<option value="">O que vai por cima?</option>`

**Select "Área de Uso"** — tipo de obra:
- Padrão: Residencial / Comercial / Industrial ou Obra
- Adapte conforme o público do `11.0) SUGESTÃO DE PÚBLICO` do `product.md`

**Checkbox "Piso sobre piso"** — quando o produto é aplicado sobre revestimento existente:
- Inclua quando o `product.md` mencionar sobreposição
- Omita se o produto não tiver essa aplicação

Se o produto não tiver context row relevante (sem variações de aplicação), remova o bloco `.calc-context-row` e o segundo `.calc-divider` por completo.

### 6. Definir os substratos (Passo 3)

Baseie nos `4.5) LOCAIS DE APLICAÇÃO` do `product.md`. Cada substrato deve ter:
- Um `value` único usado como chave na `buildCompreJunto()`
- Um ícone Material Symbols representativo
- Um label claro para o consumidor final

### 7. Validar a lógica

| Input | Espessura | Substrato | Resultado esperado |
|---|---|---|---|
| 20 m² | 3 mm | Concreto | `CEIL(20 × 1.10 / (10/3))` = `CEIL(6.6)` = **7 sacos** |
| 10 m² | 2 mm | Cerâmica | `CEIL(10 × 1.10 / 5)` = `CEIL(2.2)` = **3 sacos** |
| 0 m² | qualquer | qualquer | Resultado oculto |
| 16 mm | qualquer | qualquer | Aviso de desnível extremo, resultado oculto |

### 8. Salvar

```
products/{marca-slug}/{linha-slug}/{produto-slug}/{variante-slug}/calculator.html
```

---

## Pontos de Adaptação — Resumo

| O que adaptar | Onde | O que mudar |
|---|---|---|
| Título e subtítulo | HTML `.calc-header` + `.calc-subtitle` | Nome do produto + variante/embalagem |
| `SAFETY_MARGIN` | JS | Margem de segurança (padrão `1.10`) |
| Constante da fórmula | JS `var rendimento = X / espMM` | Derivar da ficha técnica |
| Limites do input de espessura | HTML `min`, `max`, `step` | Conforme `1.0 CONSUMO` e `4.7 COMPLEXIDADE` |
| Limites de aviso | JS `if (espMM > X)` | Valor máximo seguro |
| Options do select "Revestimento" | HTML `<select id="…-revestimento">` | Revestimentos compatíveis do `product.md` |
| Options do select "Área de Uso" | HTML `<select id="…-uso">` | Tipos de obra do público-alvo |
| Checkbox de sobreposição | HTML + JS `chkSobreposicao` | Manter, adaptar label ou remover |
| `buildCompreJunto()` | JS | Primers por substrato + revestimento |
| Label da unidade no resultado | JS `.textContent` | "saco de 20 kg", "lata de 18L", "unidade" |
| Substratos (Passo 3) | HTML radios + JS | Conforme `4.5 LOCAIS DE APLICAÇÃO` |
| Ferramentas | HTML `.calc-alert-info` `<li>` | Seção `7.0 FERRAMENTAS` do `product.md` |
| IDs do formulário | HTML + JS | Slug do produto para evitar conflitos |
| URL do WhatsApp | HTML `.calc-support-btn` href | Texto pré-preenchido com nome do produto |

---

## Regras Críticas

| Regra | Detalhe |
|---|---|
| Fórmula derivada de dados reais | Nunca use valores de rendimento inventados |
| JS puro | Sem frameworks (React, Vue, jQuery, Alpine) |
| IIFE obrigatório | Todo JS dentro de `(function(){ 'use strict'; ... }())` |
| `SAFETY_MARGIN` sempre aplicada | `area × SAFETY_MARGIN` antes do `Math.ceil` |
| Resultado só com todos os inputs válidos | `area > 0` **e** `espMM > 0` **e** `espMM ≤ max` |
| Alerta vazio = escondido | `buildCompreJunto()` vazio → ocultar `.calc-alert-required` |
| IDs únicos por produto | `calc-[slug]-form`, `calc-[slug]-result` — evita conflito se duas calculadoras na mesma página |
| Sem `<html>`, `<head>`, `<body>` | Bloco começa com `<div class="product-calc">` |

---

## Referências de Arquivo

| Arquivo | Papel |
|---|---|
| `templates/product-calculator-template.html` | Template v2.1 — copiar e adaptar |
| `agente-calculator.md` | Agente executor com CSS embutido e JS documentado |
| `workflow-descricao-html.md` | Workflow da descrição HTML (T4 referencia este workflow) |
