# Workflow: Criação de Ofertas

> **Agente responsável:** `migração/promotions-designer.agent.md`  
> **Última revisão:** 2026-06-03

---

## Visão Geral

Este workflow transforma dados de produto em ofertas prontas para ativação multicanal. Segue dois passos obrigatórios e sequenciais: ideação (para aprovação) e execução (somente após aprovação).

```
product.md + briefing-crm.md
        ↓
PASSO 1 — Proposta no chat (6–8 ideias em tabela)
        ↓
Gustavo marca [x] nas ideias aprovadas
        ↓
PASSO 2 — Expansão das aprovadas em arquivo .md completo
        ↓
Gustavo ativa nos canais conforme checklist
        ↓
INDEX.md atualizado com status da oferta
        ↓
Oferta encerra → status "Histórico" (arquivo permanece)
```

---

## Inputs Necessários

Antes de acionar o agente, confirme que os seguintes arquivos estão disponíveis:

| Arquivo / Dado | Onde está | Seções / Campos mínimos |
|---|---|---|
| `product.md` | `products/{marca}/{linha}/{produto}/{variante}/` | `5.0`, `11.0`, `12.0`, `13.0` |
| `briefing-crm.md` | Mesmo path do `product.md` | Seção "Ações de CRM" |
| **Preço de custo** | Notion — Catálogo de Produtos (campo `Preço de Custo`) | Obrigatório para qualquer desconto |
| **Preço de venda** | Notion — Catálogo de Produtos (campo `Preço de Venda`) | Obrigatório para qualquer desconto |
| Reports comerciais | `atendimento-comercial/analise-comercial/reports/` | Opcional |

Se o `product.md` estiver incompleto nas seções `11.0` ou `13.0`, o agente não consegue justificar margem nem segmentar público — pare e complete antes de continuar.

Se `preço de custo` ou `preço de venda` estiverem ausentes no Notion, o agente sinaliza com ⚠️ e continua a geração. Os % de desconto seguem o teto de 15%, mas valores em R$ e cálculo de margem ficam como "a confirmar após preço no Notion".

---

## PASSO 1 — Proposta de Ofertas

### Como acionar

Envie ao Promotions Designer:

```
"Gere uma proposta de ofertas para o produto [Nome do Produto] ([marca]).
product.md: [caminho]
briefing-crm.md: [caminho]
Objetivo: [Faturamento / Queima de Estoque / Upsell / Crosssell / Retenção / B2B]"
```

### O que o agente entrega

- Uma linha de Objetivo/Direcionamento
- Tabela com 6–8 ideias (tipo distinto cada)
- Checkboxes de aprovação ao final

### O que você faz

Revise a tabela e marque `[x]` nas ideias que deseja executar. Você pode:

- Aprovar uma ou mais ideias diretamente
- Pedir ajuste em uma ideia antes de aprovar
- Reprovar todas e pedir nova rodada com direcionamento diferente

**Nunca acionar o Passo 2 sem aprovação explícita.**

---

## PASSO 2 — Expansão das Ofertas Aprovadas

### Como acionar

Após marcar as aprovações, envie:

```
"Expanda as ofertas aprovadas (#X, #Y) para o arquivo de execução."
```

### O que o agente entrega

Um único arquivo por produto em `canais-de-vendas/[canal-slug]/marketing/campanhas/ofertas/[marca-slug]/[produto-slug].md` com:

**Seção A — Briefing** (por oferta)
- Tipo + Mecânica + Público + Narrativa + Gatilho + Canais + Justificativa de Margem

**Seção B — Copy por Canal**
- WhatsApp · E-mail (assunto + corpo) · Post · Anúncio Meta/Google

**Seção C — Checklist de Ativação**
- Wake Commerce · Meta Ads · Google Ads · E-mail/CRM · WhatsApp

**Tabela de Resumo**
- `# | Oferta | Preço | Margem | Desconto | Canal de Venda`

---

## PASSO 3 — Ativação nos Canais (Responsabilidade de Gustavo)

Siga o checklist gerado na Seção C de cada oferta. Ordem sugerida:

1. **Wake Commerce** — configurar a promoção no painel antes de qualquer disparo
2. **E-mail/CRM** — agendar ou acionar o fluxo
3. **WhatsApp** — disparo direto ou script de abordagem
4. **Meta Ads / Google Ads** — ativar campanha ou boost com o criativo

### Após ativar

Atualizar `e-commerce/ofertas/INDEX.md`:
- Mover a oferta de "Aprovadas" para "Ativas"
- Preencher data de início

---

## PASSO 4 — Encerramento

Quando uma oferta encerra (por data, estoque ou decisão):

1. Abrir `e-commerce/ofertas/dados/[marca]/[produto].md`
2. Alterar `Status: Ativa` → `Status: Histórico` na oferta correspondente
3. Atualizar `e-commerce/ofertas/INDEX.md`: mover para "Histórico"

**Nunca deletar arquivos de oferta.** O histórico serve como referência para futuras campanhas.

---

## Nomenclatura de Arquivos

Padrão do arquivo de oferta expandida: um arquivo por produto (não por oferta), dentro do canal trabalhado.

```
canais-de-vendas/[canal-slug]/marketing/campanhas/ofertas/[marca-slug]/[produto-slug].md
```

Exemplos:
- `canais-de-vendas/escuta-o-veio/marketing/campanhas/ofertas/drylevis/dw240.md`
- `canais-de-vendas/escuta-o-veio/marketing/campanhas/ofertas/elastment/inject-gel.md`
- `canais-de-vendas/facil-decor/marketing/campanhas/ofertas/lt-shine/marmorato.md`

---

## Ciclo de Vida de uma Oferta

| Status | Significado | Onde no INDEX |
|---|---|---|
| **Rascunho** | Proposta no chat, aguardando aprovação | "Propostas Pendentes" |
| **Aprovada** | Arquivo expandido criado, aguarda ativação | "Aprovadas (Aguardando Ativação)" |
| **Ativa** | Em execução nos canais | "Ativas" |
| **Histórico** | Encerrada — arquivo permanece | "Histórico" |

---

## Restrições Globais (Não Negociáveis)

| Restrição | Detalhe |
|---|---|
| Desconto máximo | 15% sobre o **preço de venda do Notion** — nenhuma oferta ultrapassa esse teto |
| Verificação de margem | O agente calcula `preço_venda × (1 – desconto%)` e verifica se o resultado cobre o custo com margem mínima. Oferta que não passa é bloqueada automaticamente. |
| Cálculo de margem obrigatório | Toda oferta com desconto exibe: custo · preço de venda · preço campanha · margem resultante (% e R$) |
| Preços do Notion são a fonte de verdade | Nunca usar valores estimados ou inventados. Sempre extrair do campo `Preço de Custo` e `Preço de Venda` do Notion. |
| Sem frete grátis | Substituir por desconto, brinde ou kit |
| Sem garantia de devolução | Risk Reversal usa suporte técnico, guia ou consultoria |
| Narrativa antes da mecânica | Copy sempre conecta pessoa → dor → oferta antes de explicar o desconto |

---

## Integração com Outros Módulos

| Módulo | Relação |
|---|---|
| `e-commerce/ofertas/INDEX.md` | Registro central — atualizar a cada mudança de status |
| `e-commerce/ofertas/templates/` | `proposta-template.md` e `oferta-aprovada-template.md` |
| `e-commerce/crm/flows/` | Fluxos acionados pelas ofertas (referenciados no Checklist C) |
| `e-commerce/planilhas/meta-ads/` | Públicos para Meta Ads (referenciados no Checklist C) |
| `e-commerce/comunidades/` | Canal de divulgação — WhatsApp, Instagram, Telegram |

---

## Quem Faz o Quê

| Ação | Responsável |
|---|---|
| Gerar proposta de ideias | Promotions Designer (agente) |
| Aprovar ideias | Gustavo |
| Expandir ofertas aprovadas | Promotions Designer (agente) |
| Ativar nos canais | Gustavo / time |
| Acionar flows de CRM | CRM Strategist (agente) + Gustavo |
| Atualizar INDEX.md | Quem executa a ação |
