# Workflow: Relatório Semanal de Vendas por Produto

Ritual semanal de análise de vendas por produto para embasar decisões táticas da semana seguinte: ofertas, otimizações de listagem, campanhas, alertas de estoque.

**Quando:** Segunda-feira de manhã
**Período analisado:** Sexta-feira → Quinta-feira da semana encerrada
**Responsável:** Gustavo / time comercial

---

## Fontes de Dados

A IVA tem 4 contas no Bling (uma por unidade):

| Conta Bling | Unidade |
|-------------|---------|
| Bling — Escuta o Véio! | E-commerce principal + marketplaces EOV |
| Bling — Obramil | Canal Obramil |
| Bling — Construlivre | Canal Construlivre |
| Bling — Fácil Decor | Loja física + e-commerce Fácil Decor |

---

## Passo a Passo

### PASSO 1 — Exportar do Bling (cada conta)

Em cada conta Bling:
1. Ir em **Relatórios → Notas Fiscais por Produto** (exportação linha a linha)
2. Filtrar o período: **sexta-feira da semana anterior → quinta-feira da semana atual**
3. Exportar como CSV (separador `;`)
4. Repetir para as contas: Escuta o Véio!, Obramil, Construlivre, Fácil Decor

### PASSO 2 — Consolidar no Excel

Abrir o Excel de consolidação e colar os 4 exports lado a lado (um por coluna de seção) na aba `canais-de-vendas`. O arquivo resultante terá **3 seções lado a lado** por linha — uma por conta Bling — separadas por colunas vazias.

Colunas de cada seção (14 por seção):
```
Número | Série | Data de emissão | Situação | Natureza |
Descrição (produto) | Código (SKU) | Quantidade | Valor unitário | Valor total |
Nome da Loja (canal) | Código no fornecedor | Nome (fornecedor) | Marca
```

> **Não é necessário criar aba separada de produtos.** O arquivo `canais-de-vendas` já contém produto, SKU, quantidade, receita, canal e marca — Claude extrai tudo diretamente.

### PASSO 3 — Salvar o CSV no repositório

Nomear com a semana ISO e salvar em `base-de-dados/planilhas/vendas/`:

```
S24_canais-de-vendas.csv    ← único arquivo necessário
```

Convenção de data no nome dos outputs: **data da quinta-feira que encerra a semana**
Exemplo: semana S24 encerra em 12/jun/2026 → `2026-06-12-relatorio-semanal-S24.md`

### PASSO 4 — Invocar Claude

```
/vendas
```

Claude vai:
1. Detectar o CSV mais recente em `base-de-dados/planilhas/vendas/`
2. Parsear as 3 seções (uma por conta Bling), corrigir encoding UTF-8/Windows-1252
3. Comparar com a semana anterior (delta automático)
4. Gerar o relatório usando `arquivos/reports/_template-relatorio-semanal-produtos.md`
5. Salvar em `base-de-dados/relatorios/AAAA-MM-DD-relatorio-semanal-S-XX.md`
6. Gerar dashboard HTML em `base-de-dados/dashboards/AAAA-MM-DD-dashboard-semanal-S-XX.html`

### PASSO 5 — Revisar e Decidir

Revisar o **Plano de Ação** gerado. Para cada item:
- Pedir aprofundamento: "detalha a oferta do item 1"
- Pedir execução: "cria o briefing da campanha para o produto X"
- Ajustar: "o produto Y não está em falta — corrija"

---

## Sinais de Alerta

Fique atento quando:

| Sinal | Ação sugerida |
|-------|---------------|
| Produto do top-5 da semana passada sumiu do top-20 | Investigar: ruptura de estoque? concorrência? anúncio pausado? |
| Canal com queda > 20% sem campanha encerrada | Verificar saúde do canal (anúncios, listing, preço) |
| Receita total < 80% da semana anterior | Verificar todos os canais; acionar time comercial |
| Produto novo no top-10 pela primeira vez | Aproveitar: criar oferta ou campanha de escala |
| Marca com 0 vendas em algum canal | Verificar ativação no canal |

---

## Sinais Positivos

| Sinal | Ação sugerida |
|-------|---------------|
| Produto crescendo > 30% sem promoção ativa | Escalar com campanha paga ou oferta flash |
| Canal Atendimento Comercial crescendo | Reforçar time de vendas com novos scripts/ofertas |
| Nova marca aparecendo no top-10 | Aumentar investimento de conteúdo nessa linha |
| Ticket médio crescendo no canal Loja Virtual | Considerar bundles ou upsell |

---

## Outputs Gerados

Após cada ciclo semanal, o repositório terá:

```
base-de-dados/
  planilhas/vendas/
    S-XX_canais-de-vendas.csv      ← único arquivo de entrada necessário
  relatorios/
    AAAA-MM-DD-relatorio-semanal-S-XX.md      ← análise + plano de ação
  dashboards/
    AAAA-MM-DD-dashboard-semanal-S-XX.html    ← dashboard visual
```

---

## Relatório Mensal

No final de cada mês, use os relatórios semanais como base para o dashboard mensal:
`arquivos/reports/_template-dashboard-mensal.md`
