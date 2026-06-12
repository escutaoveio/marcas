# PDR — Loja Física Escuta o Véio!

**Plano de Definição de Requisitos**
Versão: 1.2
Atualizado em: 2026-06-05
Status: 🟡 Em especificação — bloco jurídico pesquisado, roteiro contador pronto, demo Wake pendente

---

## 1. Contexto e Oportunidade

O Escuta o Véio! opera hoje exclusivamente no digital (e-commerce próprio + marketplaces). A abertura de uma loja física surge como **oportunidade identificada** — não como expansão planejada de longo prazo, mas como movimento estratégico de resposta rápida.

**Por que faz sentido:**
- A IVA já tem marca, catálogo e logística estruturada — o custo marginal de abrir uma loja física é menor do que para uma empresa do zero
- A loja física estende o alcance para o cliente que prefere o presencial e para o profissional que quer ver o produto antes de comprar
- Funciona como hub de Click & Collect, reduzindo custo de frete e aumentando tráfego na loja
- Reforça credibilidade da marca — "a empresa que tem loja" transmite solidez

**Decisões fixadas:**
| Atributo | Decisão |
|---|---|
| Modelo | Loja própria Escuta o Véio! |
| Público | Cliente final + Profissional (pintor, marceneiro, aplicador) |
| Integração digital | OMS (estoque unificado) + Click & Collect |
| ERP | Bling (já em uso) |
| Prazo | Urgente — oportunidade de curta janela |

---

## 2. Conceito da Loja

> "Novas Soluções para Velhos Problemas".

Não é uma loja de tintas. É um **ponto de solução**: o cliente chega com um problema e sai com a resposta certa — produto + orientação técnica. O vendedor é consultor, não repositor de prateleira.

### Zonas do Espaço

| Zona | Função | Prioridade |
|---|---|---|
| Fachada / vitrine | Atração, identidade visual, visibilidade da marca | Alta |
| Balcão de atendimento | Consultoria técnica, PDV, caixa | Alta |
| Área de exposição | Produtos organizados por problema/categoria | Alta |
| Área Click & Collect | Separação e entrega de pedidos do e-commerce | Alta |
| Estoque interno | Reposição, volumes maiores | Alta |
| Totem / tablet | Acesso ao catálogo completo via Wake Commerce | Média |

---

## 3. Localização

**Cidade confirmada:** São Bernardo do Campo — SP
**Ponto específico:** A definir (bairro, endereço, metragem)

### Por que SBC faz sentido para o perfil Escuta o Véio!

São Bernardo do Campo é o coração do ABC Paulista — uma das regiões com maior concentração de mão de obra qualificada em construção, metalurgia e indústria do Brasil. O perfil do profissional (pintor, marceneiro, aplicador) e do consumidor final que faz reforma é exatamente o público da marca.

| Fator | Contexto de SBC |
|---|---|
| Perfil do entorno | Alta concentração de profissionais da construção civil e indústria |
| Adensamento residencial | Região com forte mercado de reforma e acabamento |
| Infraestrutura | Boa malha viária (Via Anchieta, Imigrantes, Av. Kennedy) |
| Concorrência | Presença de redes como C&C, Leroy Merlin, Telhanorte — a diferenciar pela consultoria técnica |

### Critérios de seleção do ponto

- **Fluxo:** tráfego de profissionais (pintores, aplicadores) e consumidor final fazendo reforma
- **Entorno:** bairros com atividade de construção ou próximos a condomínios e residências
- **Acesso:** carga/descarga e estacionamento — profissional vem de carro ou van
- **Área mínima:** estimativa 80–150 m² (estoque + área de venda + balcão técnico + C&C)
- **Custo:** validar com planilha de viabilidade (Seção 9)

### Checklist de validação do ponto

- [ ] Visita técnica ao imóvel
- [ ] Análise de fluxo e perfil do entorno
- [ ] Avaliação jurídica do contrato de locação
- [ ] Verificação de adequação elétrica e estrutural
- [ ] Aprovação financeira (aluguel + reforma dentro da viabilidade)

---

## 4. Mix de Produtos

> **⚠️ A definir** — aguardando dados de giro do e-commerce.

### Recomendação de abordagem

**Curadoria de top sellers + catálogo digital no totem.**

Os produtos físicos na loja = top 80–120 SKUs por giro e margem. O restante do catálogo (1.200+ SKUs) fica acessível via tablet/totem na loja, com opção de pedir para entrega em casa ou retirar na semana.

| Vantagem | Risco mitigado |
|---|---|
| Estoque físico enxuto e rotativo | Loja não vira depósito |
| Profissional encontra o que mais usa | Custo de capital em giro menor |
| Catálogo completo via digital | Nenhum cliente sai sem opção |

### Metodologia de seleção do mix — definida

1. Relatório Bling/Wake: top 150 SKUs por **quantidade vendida nos últimos 90 dias**
2. Filtrar: remover SKUs com **margem < 20%** e **peso > 20 kg** (volumes pesados são entregues — o cliente não leva na mão)
3. Resultado esperado: ~80–100 SKUs para o estoque físico inicial
4. Restante do catálogo (1.200+ SKUs): disponível via tablet/totem na loja, com entrega em casa ou via C&C em dias

### Próximos passos

- [ ] Extrair relatório de top 150 SKUs por quantidade — últimos 90 dias (Bling ou Wake)
- [ ] Aplicar filtros de margem e peso
- [ ] Validar mix final com equipe comercial antes da montagem do estoque inicial

---

## 5. Requisitos de Integração e Sistemas

> Esta é a seção mais crítica para a fase de especificação técnica.

### Arquitetura de sistemas

Dois cenários possíveis — definição depende da demo do Wake U (ver Seção 5.2):

**Cenário A — Bling FC como PDV**
```
[Loja Física]
      │
      ▼
[Bling Frente de Caixa] ←── [Maquininha]
      │
      ├──▶ [Bling ERP]
      │         ├──▶ Depósito "Loja Física SBC"
      │         ├──▶ NFC-e / NF-e
      │         └──▶ Clientes EOV (tag: loja-fisica)
      │
      └──▶ [Wake Commerce]
                ├──▶ Click & Collect
                └──▶ CD sync diário ou OMS
```

**Cenário B — Wake U como PDV (preferencial se NF resolvida)**
```
[Loja Física]
      │
      ▼
[Wake U] ←── [Maquininha]
  ├── On Hands (PDV mobile)
  ├── Prateleira Infinita (catálogo completo sem estoque físico total)
  ├── Agenda do Vendedor (histórico online + IA cross-sell)
  └── Unified Fulfillment (OMS + C&C nativo)
      │
      ↕ integração (a confirmar)
      │
[Bling ERP]
  ├── Depósito "Loja Física SBC" (estoque master)
  └── NFC-e / NF-e (ou módulo próprio Wake U)
```

**Cenário C — Bling FC como PDV + Wake OMS via API (arquitetura híbrida)**
```
[Loja Física]
      │
      ▼
[Bling Frente de Caixa] ←── [Maquininha]
  ├── NFC-e / NF-e (nativo Bling)
  └── Estoque Bling (depósito "Loja Física SBC")
      │
      ↕ API agnóstica Wake OMS
      │
[Wake OMS]
  ├── Fulfillment inteligente (roteamento CD vs. loja)
  ├── Click & Collect
  └── Visibilidade de estoque em tempo real
```

> O Wake OMS possui **APIs de integração agnóstica com PDVs** — documentado em:
> [WAKE OMS — APIs de Integração agnóstica com PDVs](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407-WAKE-OMS-APIs-de-Integra%C3%A7%C3%A3o-agn%C3%B3stica-com-PDVs)
> *(requer login no portal Wake para acesso)*
>
> Isso significa que o Bling FC pode ser o PDV (cuidando de NF e caixa) enquanto o Wake OMS cuida da inteligência de fulfillment — sem depender do Wake U para resolver a questão fiscal. O Cenário C elimina a dependência de o Wake U ter NF nativo.

---

### 5.1 Bling ERP

**Status:** Já em uso como ERP principal do e-commerce.
**Papel na loja física:** fonte de verdade de estoque, cadastro de produtos, clientes e emissão de notas fiscais.

#### Configurações necessárias no Bling

| Requisito | Descrição | Status |
|---|---|---|
| Criar depósito "Loja Física EOV" | Separar o estoque da loja do estoque do CD no Bling | 🔴 Pendente |
| Configurar transferência entre depósitos | NF de transferência interna (CD → Loja Física) para abastecimento | 🔴 Pendente |
| Cadastro de clientes com tag de canal | Campo de origem "Loja Física" no cadastro de cliente EOV | 🔴 Pendente |
| Emissão de NFC-e | Habilitar NFC-e para vendas balcão a pessoa física | 🔴 Pendente — depende do estado |
| Emissão de NF-e | Para vendas a PJ / profissional com CNPJ | 🔴 Pendente — verificar config atual |
| Certificado digital A1 | Para emissão de NF pela loja (se em CNPJ diferente) | 🔴 Verificar com contador |
| Usuários e permissões | Criar usuário do gerente/vendedor da loja com acesso restrito | 🔴 Pendente |

#### Perguntas abertas — Bling

- A loja física vai operar no mesmo CNPJ do e-commerce ou em CNPJ separado?
- Qual o estado (UF) da loja? (define o tipo de nota fiscal obrigatória)
- O Bling atual já está com NF-e habilitada? Qual série?

---

### 5.2 PDV — Frente de Caixa

**Status: decisão pendente — Wake U muda a arquitetura**

A análise inicial apontava o Bling Frente de Caixa como PDV. Com o Wake U mapeado, a decisão precisa ser revisitada antes de qualquer implementação.

---

#### Opção A — Bling Frente de Caixa

PDV nativo do Bling, sem custo adicional. A loja entra como mais um ponto de venda dentro do ERP que já opera o e-commerce.

**Referência:** [bling.com.br/funcionalidades/frente-de-caixa](https://www.bling.com.br/funcionalidades/frente-de-caixa)

| Critério | Avaliação |
|---|---|
| Integração com estoque Bling | ✅ Nativa — atualização instantânea após cada venda |
| Múltiplos depósitos | ✅ Confirmado — baixa do depósito "Loja Física SBC" especificamente |
| Emissão NFC-e | ✅ Confirmado — emitida automaticamente no balcão |
| Emissão NF-e (para PJ) | ✅ Bling já emite NF-e — mesma lógica do e-commerce |
| Pix integrado | ✅ Via Bling Conta Digital — conciliação automática |
| Cartão de crédito/débito | ✅ Smart POS integrado — conciliação automática |
| Dinheiro / controle de caixa | ✅ Sangria, suprimento e fechamento por operador |
| Múltiplos operadores | ✅ Cada vendedor tem seu caixa individual |
| Sincronização com e-commerce | ✅ Estoque compartilhado entre loja física e canais online |
| Histórico do cliente (e-commerce) | ❌ Não exibe comportamento digital — só cadastro |
| Catálogo completo / Prateleira Infinita | ❌ Não nativo |
| Inteligência de venda (IA, cross-sell) | ❌ Não |
| Funciona offline | ❓ Não mencionado — confirmar com Bling |
| Compatibilidade tablet/celular | ✅ Tablet, celular, smartphone e SmartPOS Android |
| Maquininha específica | ✅ Ver lista completa abaixo |
| Custo adicional | ✅ Incluso no plano Bling atual |

**Melhor para:** operação simples de balcão, fase inicial, equipe pequena. NF e estoque 100% resolvidos nativamente.

##### Descoberta: CPlug — modo offline para o Bling FC

O Bling FC nativo é **100% online** — sem internet, não opera. A solução para contingência é a **CPlug**, parceiro oficial do Bling que oferece PDV móvel (smartphones, tablets e SmartPOS) com **modo offline**: vendas registradas normalmente sem internet e sincronizadas automaticamente com o Bling quando a conexão é restaurada.

> Para a loja de SBC, a recomendação é: Bling FC como PDV principal + chip 4G como conexão de backup (infraestrutura mínima). Avaliar CPlug apenas se o risco de queda de internet for alto no ponto escolhido.

- Referência CPlug: [ajuda.bling.com.br — Conheça a CPlug](https://ajuda.bling.com.br/hc/pt-br/articles/25940324197783-Conhe%C3%A7a-a-CPlug-Solu%C3%A7%C3%B5es-que-facilitam-o-seu-neg%C3%B3cio) *(requer login Bling)*

---

#### Opção B — Wake U (Unified Commerce)

Plataforma completa de unified commerce da Wake. Integra operação física e digital com inteligência de vendas em tempo real.

**Módulos relevantes para a loja EOV:**

| Módulo | O que faz | Impacto direto |
|---|---|---|
| **On Hands** | PDV mobile no tablet/celular do vendedor — cliente finaliza compra com o vendedor, sem ir ao caixa | PDV portátil nativo, exatamente o modelo desejado |
| **Prateleira Infinita** | Vendedor acessa inventário completo da rede (CD + loja) sem limitação de estoque físico | A loja não precisa estocar 1.200 SKUs — vende qualquer produto do catálogo EOV, o sistema roteia a entrega |
| **Agenda do Vendedor** | Histórico de compras do cliente (inclusive do e-commerce), 15+ gatilhos comportamentais, sugestões de cross-sell/upsell por IA | Vendedor sabe o que o cliente comprou online antes de chegar na loja |
| **Unified Fulfillment** | Gestão de picking, packing e roteamento entre canais | C&C e pedidos OMS gerenciados nativamente |
| **Dashboard 360°** | Visibilidade em tempo real de vendas, estoque e desempenho | Reporting unificado loja + e-commerce sem planilha manual |

**Referência:** [wake.tech/wake-u](https://wake.tech/wake-u/)
**Clientes:** Calvin Klein, Farm, Reserva, Shoulder, Ellus, Richards — base fashion; confirmar casos em construção/materiais.

> **Wake U = Wake OMS — confirmado pela pesquisa:** o app Wake U é a interface mobile do Wake OMS para lojas físicas (era chamado de "SinOMS" antes do rebranding). Usar Wake U **implica** contratar Wake OMS. Não são produtos separáveis. A pergunta relevante para a demo é: o Wake OMS já inclui a interface On Hands/mobile para o vendedor, ou é módulo com custo adicional?

| Critério | Avaliação |
|---|---|
| Integração com estoque Bling | **A confirmar** — ponto crítico |
| Emissão NFC-e / NF-e | **A confirmar** — depende de integração com Bling ou módulo próprio |
| Histórico do cliente (e-commerce) | Sim — unifica dados online e offline nativamente |
| Catálogo completo na loja | Sim — Prateleira Infinita resolve o problema de mix |
| Inteligência de venda | Sim — IA para cross-sell/upsell em tempo real |
| Custo adicional | A negociar com Wake |
| Funciona offline | A confirmar |

**Melhor para:** operação que quer vender o catálogo completo sem estocar tudo, e que valoriza a conexão digital-físico do cliente.

---

#### Comparativo final

| Critério | Bling FC | Wake U | Bling FC + Wake OMS |
|---|---|---|---|
| PDV mobile (tablet/celular) | ❓ A confirmar | ✅ On Hands | ❓ A confirmar |
| Emissão NFC-e nativa | ✅ Confirmado | ❓ A confirmar | ✅ Confirmado |
| Múltiplos depósitos / estoque por loja | ✅ Confirmado | ❓ A confirmar | ✅ Confirmado |
| Pix e cartão integrados | ✅ Confirmado | ❓ A confirmar | ✅ Confirmado |
| Catálogo completo / Prateleira Infinita | ❌ | ✅ | ❌ (só OMS, não catálogo) |
| Histórico do cliente online na loja | ❌ | ✅ | ❌ |
| IA de cross-sell/upsell | ❌ | ✅ | ❌ |
| Fulfillment inteligente / OMS | ❌ | ✅ | ✅ (via API agnóstica) |
| Click & Collect nativo | ❌ | ✅ | ✅ |
| Custo adicional | ✅ Zero | ❓ A negociar | ❓ Custo Wake OMS |
| Complexidade de implantação | Baixa | Média-Alta | Média |
| Funciona offline | ❓ | ❓ | ❓ |

> **Leitura do comparativo:** o Bling FC está bem posicionado para NF, estoque e caixa — os bloqueadores de abertura. O Wake U adiciona inteligência de vendas e catálogo infinito, mas tem mais incógnitas técnicas. O Cenário C (Bling FC + Wake OMS via API) é o caminho híbrido: segurança do Bling para fiscal + inteligência da Wake para fulfillment, conectados pela [API agnóstica de PDVs](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407-WAKE-OMS-APIs-de-Integra%C3%A7%C3%A3o-agn%C3%B3stica-com-PDVs).

#### Resultados de pesquisa — pontos do bloco D

| Item | Status | Achado |
|---|---|---|
| Prateleira Infinita requer OMS? | ✅ Fechado | Contratável isoladamente — OMS maximiza, mas não é obrigatório |
| On Hands aceita Pix e cartão? | ✅ Parcial | Suporta pagamentos digitais (Pix, cartão) via terminal unificado |
| **On Hands aceita dinheiro?** | 🔴 Crítico | **Não encontrado** — plataforma desenhada para digital. Confirmar na demo |
| NF-e / NFC-e no On Hands | ⚠️ Parcial | Wake emite NF via OMS — confirmar se On Hands tem esse fluxo isolado |
| Preço Wake U | ❌ Sem dado público | Sob consulta |
| Preço Wake OMS | ❌ Sem dado público | Referência de parceiro: a partir de R$ 2.700 + 2,3% sobre pedidos (Wake Commerce — não necessariamente OMS isolado) |

> **Alerta de arquitetura:** se o Wake U não suportar caixa em dinheiro com troco, o Cenário B (Wake U puro) é inviável — a EOV confirmou aceitar dinheiro. O Cenário C (Bling FC + Wake OMS via API) se torna o caminho preferencial: Bling cuida do caixa físico e dinheiro, Wake OMS cuida do fulfillment.

**Referências:**
- [wake.tech/wake-u/prateleira-infinita](https://wake.tech/wake-u/prateleira-infinita/)

---

#### Roteiro para demo Wake U + Wake OMS

> Usar na reunião com CS/AE da Wake. A resposta do item 1 define o cenário de arquitetura.

**Bloco 1 — Eliminatórias (definem o cenário antes de avançar)**

1. **O On Hands suporta pagamento em dinheiro com controle de troco e fechamento de caixa?**
   — Se não → Cenário B descartado; seguir com Cenário C (Bling FC + Wake OMS)
2. **A emissão de NFC-e / NF-e é nativa no On Hands ou depende do Bling?**
   — Se depende do Bling → Cenário C (híbrido) independente da resposta anterior

**Bloco 2 — Arquitetura e integração**

3. Cenário C: integrar Bling FC com Wake OMS via API agnóstica — é configuração ou requer desenvolvimento?
4. Com Wake Commerce + Wake OMS já contratados, a Prateleira Infinita ativa sem precisar do Wake U completo?
5. Como o Wake U sincroniza estoque com o Bling? O Bling continua como master de estoque?
6. O On Hands funciona offline (queda de internet na loja)?

**Bloco 3 — Negócio e custo**

7. **Wake U = Wake OMS? O On Hands/mobile já está incluso no contrato Wake OMS, ou é módulo com custo separado?**
8. Custo mensal do Wake OMS para 1 loja + 1 CD (já com Wake Commerce ativo)?
9. Wake OMS pode ser contratado separadamente do Wake Commerce já ativo?
10. Há clientes no segmento de construção civil, tintas ou produtos químicos?

---

**Bling FC — o que precisa contratar**

| Item | Custo | Observação |
|---|---|---|
| Módulo Frente de Caixa | ✅ Incluso no plano Titânio+ | Verificar qual plano a IVA usa hoje |
| NFC-e / NF-e | ✅ Incluso no plano | — |
| Depósito "Loja Física EOV" | ✅ Incluso — só configuração | — |
| **Certificado Digital e-CNPJ A1** | **~R$109–210/ano** | **Obrigatório para NFC-e** — comprar via Bling ([bling.com.br/funcionalidades/venda-certificado-digital](https://www.bling.com.br/funcionalidades/venda-certificado-digital)) ou outro parceiro |
| Usuários adicionais | Depende do plano atual | Se bater o limite de usuários → upgrade de plano |
| CPlug (modo offline) | A consultar | Só se o ponto tiver histórico de queda de internet |
| Maquininha SmartPOS | Custo da adquirente | Não é Bling — ver lista abaixo |

> **Checklist antes da abertura:**
> - [ ] Confirmar qual plano Bling a IVA usa hoje — inclui FC?
> - [ ] Confirmar quantos usuários o plano suporta — precisa de upgrade?
> - [ ] Comprar certificado digital e-CNPJ A1 para o CNPJ da loja (~R$109 via Bling)

**Bling FC — pontos confirmados pela pesquisa:**
- ✅ Funciona em tablet Android, celular e SmartPOS Android
- ✅ Não funciona offline nativamente — CPlug resolve (ver descoberta acima)
- ✅ Maquininhas SmartPOS homologadas (apenas Android SmartPOS):

| Adquirente | Modelos confirmados |
|---|---|
| **Stone** | P2 |
| **Cielo** | SmartPOS (verificar modelos) |
| **Vero** | SmartPOS |
| **Smart Vindi** | SmartPOS |
| **PagSeguro** | SmartPOS |
| **Safra** | SmartPOS |
| **Sicredi** | SmartPOS |
| **Bin** | SmartPOS |
| **Caixa** | DX8000, P2-A11 |
| **Rede** | L400, n960k |

> ⚠️ Apenas maquininhas **SmartPOS Android** são compatíveis com integração no Bling FC. Maquininhas convencionais (ex.: Ton da Stone) não têm integração — só aceitam pagamento de forma independente.

- Referência: [Guia geral — Configuração da máquina de cartão POS no Bling FC](https://ajuda.bling.com.br/hc/pt-br/articles/17793394706711-Guia-geral-Configura%C3%A7%C3%A3o-da-m%C3%A1quina-de-cart%C3%A3o-POS-no-Frente-de-Caixa-do-Bling) *(requer login Bling)*
- Referência: [Bling — Integração POS](https://www.bling.com.br/funcionalidades/integracao-pos)

**Wake OMS + API agnóstica (se Cenário C):**
- [ ] Ler documentação completa: [APIs de Integração agnóstica com PDVs](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407-WAKE-OMS-APIs-de-Integra%C3%A7%C3%A3o-agn%C3%B3stica-com-PDVs) *(requer login Wake)*
- [ ] Responder perguntas do roteiro de demo acima antes de avançar para implantação

---

### 5.3 Wake Commerce — Estoque, OMS e Click & Collect

**Status:** Wake já operacional no e-commerce com apenas 1 CD. A loja física exige a criação de um segundo nó de estoque e, potencialmente, a contratação do módulo OMS da Wake.

#### Modelo de gestão de estoque — duas opções

**Opção A — CD na Wake com atualização diária (sem OMS)**

A loja física é cadastrada como um segundo depósito na Wake. O estoque é sincronizado uma vez por dia (batch noturno via Bling).

| Prós | Contras |
|---|---|
| Sem custo adicional de módulo | Risco de overselling: venda na loja + venda online do mesmo item antes do sync |
| Simples de configurar | Sem inteligência de roteamento — regras manuais |
| Adequado para fase inicial | Requer disciplina operacional para evitar ruptura |

**Opção B — Wake OMS (assinatura do módulo)**

O Wake OMS é a plataforma de orquestração de pedidos da Wake. Centraliza estoque e fulfillment de todos os canais em tempo real.

**Funcionalidades confirmadas pela pesquisa:**

| Funcionalidade | Descrição |
|---|---|
| Múltiplos CDs e lojas | ✅ Suporta nativamente — cada CD/loja como nó independente |
| Roteamento inteligente | ✅ Direciona pedidos por disponibilidade, prazo e custo de frete |
| Change Seller | ✅ Redireciona para outro CD/loja se o principal não consegue atender |
| Prateleira Infinita | ✅ Presente também no OMS — não exclusivo do Wake U |
| Click & Collect | ✅ Nativo — vincula lojas físicas como pontos de retirada |
| Multi-freight | ✅ Diferentes transportadoras por origem de produto no mesmo pedido |
| Integração com transportadoras | ✅ Conexão direta para cotação e rastreio |

| Prós | Contras |
|---|---|
| Estoque em tempo real — elimina overselling | Custo adicional (sem preço público — sob consulta) |
| Roteamento automático inteligente | Configuração mais complexa que sync diário |
| Base para expansão: novos CDs e lojas sem mudar arquitetura | — |
| API agnóstica para integrar qualquer PDV (inclusive Bling FC) | — |

**Preço:** não divulgado publicamente. Requer contato com equipe comercial Wake.

- Referência produto: [wake.tech/wake-oms](https://wake.tech/wake-oms/)
- Referência blog: [Conheça o Wake OMS](https://wake.tech/blog/conheca-wake-oms/)
- Referência CDs: [Centros de Distribuição — Wake](https://atendimento.wake.tech/hc/pt-br/articles/21406540759575-Centros-de-Distribui%C3%A7%C3%A3o) *(requer login Wake)*
- API agnóstica PDVs: [WAKE OMS — APIs de Integração agnóstica com PDVs](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407-WAKE-OMS-APIs-de-Integra%C3%A7%C3%A3o-agn%C3%B3stica-com-PDVs) *(requer login Wake)*

> **Recomendação revisada:** o Wake OMS suporta nativamente múltiplos CDs — é o caminho certo para a loja física. A questão é quando contratar: na abertura (Cenário C) ou após estabilizar a operação. O sync diário (Opção A) é aceitável só se o volume de itens compartilhados entre loja e e-commerce for baixo.

- [ ] Solicitar proposta e demo do Wake OMS — confirmar custo para 1 loja + 1 CD
- [ ] Ler documentação da API agnóstica (requer login Wake) para mapear esforço de integração com Bling FC

#### Configurações necessárias na Wake (Fase 1 — sem OMS)

| Requisito | Descrição | Status |
|---|---|---|
| Criar CD "Loja Física SBC" na Wake | Segundo nó de estoque, mesmo que com sync diário | 🔴 Pendente |
| Ativar Click & Collect | Endereço da loja como opção de retirada no checkout | 🔴 Pendente |
| Configurar prazo de separação C&C | Ex.: pedido até 14h → retirada no mesmo dia | 🔴 Pendente |
| Notificação "pedido pronto para retirada" | E-mail/SMS automático quando C&C estiver separado | 🔴 Pendente |
| Definir regra de roteamento | Fase 1: loja só atende C&C, entregas web saem do CD | 🔴 Pendente |
| Sincronização estoque Bling → Wake | Confirmar se integração atual suporta múltiplos depósitos | 🔴 A verificar com Wake |

#### Fluxo Click & Collect (operacional)

```
Cliente compra no site → seleciona "Retirar na loja SBC"
        ↓
Wake cria pedido com fulfillment = Loja Física SBC
        ↓
Equipe da loja recebe alerta (via Bling FC ou painel Wake)
        ↓
Separa o pedido — confirma no sistema
        ↓
Cliente recebe notificação "Pedido pronto para retirada"
        ↓
Cliente vai à loja → se identifica pelo CPF ou código do pedido → recebe
```

- [ ] Definir prazo máximo de retirada (sugestão: 3 dias corridos)
- [ ] Definir o que acontece se o cliente não retirar (cancelamento + reposição de estoque)
- [ ] Definir como o cliente se identifica na retirada


---

### 5.4 Gestão de Estoque — Fluxo Bling ↔ Loja Física

**Modelo:** Bling como master de estoque. Wake consome via integração.

#### Fluxo de abastecimento da loja

```
CD IVA (estoque Bling - Depósito "CD")
      ↓
Pedido de transferência interno no Bling
      ↓
NF de transferência emitida (CFOP 5.152 ou equivalente)
      ↓
Mercadoria chega na loja → entrada no Bling (Depósito "Loja Física EOV")
      ↓
Saldo atualizado automaticamente na Wake Commerce
```

- [ ] Definir frequência de reposição (diária, semanal, por ponto de pedido mínimo)
- [ ] Definir responsável por acionar a reposição (gerente da loja ou automático por gatilho de estoque mínimo)
- [ ] Configurar alertas de estoque mínimo no Bling por SKU

---

### 5.5 Formas de Pagamento

| Meio | Solução | Observação | Status |
|---|---|---|---|
| Cartão de crédito (à vista) | Maquininha | Apenas à vista — sem parcelamento sem juros na fase inicial | 🔴 Definir maquininha |
| Cartão de débito | Maquininha | — | 🔴 Definir maquininha |
| Pix | QR Code via maquininha | Automático na maioria das máquinas | 🔴 Definir maquininha |
| Dinheiro | Caixa físico | Requer módulo de sangria/suprimento no Bling FC | 🔴 Validar no Bling FC |

> Parcelamento sem juros e crédito faturado para PJ: **não previstos na fase inicial.** Podem ser adicionados em fase posterior.

#### Escolha da maquininha — critérios

A maquininha precisa ser compatível com o Bling Frente de Caixa. Verificar suporte TEF ou Bluetooth com:

- **Stone** — boa integração com Bling, suporte técnico ativo
- **Cielo** — líder de mercado, ampla compatibilidade
- **PagBank** — custo menor, verificar integração com Bling FC

- [ ] Confirmar com Bling quais maquininhas têm integração homologada com a Frente de Caixa
- [ ] Verificar taxas e prazo de recebimento de cada operadora

---

### 5.6 Cadastro de Clientes e CRM

**CRM em uso:** [DITO](https://dito.com.br/) — já integrado ao Bling via API.

#### DITO + Bling na loja física — integração confirmada

A DITO possui integração nativa com o Bling ([documentação](https://developers.dito.com.br/docs/bling-integra%C3%A7%C3%A3o-facilitada)). Dados sincronizados automaticamente:

| Dado | Sincronização |
|---|---|
| Cadastro do cliente | CPF, nome, e-mail, telefone, endereço |
| Histórico de compras | Total, desconto, forma de pagamento |
| Produtos comprados | SKU, preço, quantidade por transação |
| Vendedor | Código do vendedor vinculado à loja |

**Frequência:** D-1 (sincroniza no dia seguinte à venda)  
**Chave de unificação:** CPF — cliente que comprou online e vai à loja vira **uma visão única no DITO**

> Isso significa que a loja física **não precisa de nenhuma integração extra de CRM** — basta capturar o CPF no Bling FC e o DITO absorve a compra offline automaticamente no dia seguinte.

#### Impacto na decisão de PDV e Wake U

| Módulo Wake U | Status após DITO |
|---|---|
| **Agenda do Vendedor** (histórico online do cliente na loja) | ⚠️ **Parcialmente substituído** — DITO já oferece histórico unificado. Diferença: DITO é D-1, Agenda do Vendedor é tempo real. Avaliar se D-1 é suficiente para o vendedor. |
| **Prateleira Infinita** | ✅ Continua relevante — DITO não resolve catálogo infinito |
| **On Hands** (PDV mobile nativo Wake) | Depende de NF — Bling FC resolve se NF for a prioridade |

#### Modelo operacional no balcão

| Cenário | Ação |
|---|---|
| Cliente novo (PF) | Cadastrar no Bling: nome + CPF + WhatsApp → DITO absorve automaticamente |
| Cliente novo (PJ/Profissional) | Cadastrar com CNPJ + origem = "loja-fisica" |
| Cliente já existe no Bling | Vincular CPF → venda une o histórico online no DITO |
| Click & Collect | CPF já vinculado ao pedido do e-commerce — nenhuma ação extra |

#### Identificação na loja (sem fricção)

O vendedor consulta o cliente pelo CPF/CNPJ antes de fechar a venda:
1. Tem cadastro → vincula a venda → DITO registra automaticamente
2. Não tem → cria cadastro na hora (nome + CPF + WhatsApp — mínimo)

- [ ] Confirmar com DITO: a integração Bling já está ativa na conta IVA ou precisa ativar o módulo de loja física?
- [ ] Definir código de loja para o depósito "Loja Física SBC" no DITO (para separar no reporting)
- [ ] Configurar campo "vendedor" no Bling FC (para DITO rastrear performance por vendedor)
- [ ] Verificar se o PDV escolhido permite consultar/criar clientes no Bling na hora da venda

---

### 5.7 Fiscal e Nota Fiscal — SP (São Bernardo do Campo)

**Estado confirmado: São Paulo.** SP tem um dos ambientes fiscais mais exigentes do Brasil para o varejo.

#### Como funciona em SP — achados confirmados pela pesquisa

São Paulo exige documento fiscal eletrônico para toda venda no varejo. As opções válidas hoje são:

| Modalidade | Quando usar | Situação em SP |
|---|---|---|
| **NFC-e** (Nota Fiscal de Consumidor Eletrônica) | Venda balcão para pessoa física | ✅ **Obrigatória em SP a partir de 01/01/2026 para novos estabelecimentos** |
| **SAT-CF** (Sistema Autenticador e Transmissor) | Venda balcão para pessoa física | ❌ **Descontinuado — impossível ativar para novos estabelecimentos desde nov/2024** |
| **NF-e** (modelo 55) | Venda para PJ / profissional com CNPJ | Já habilitada no Bling — verificar série e config |

> **✅ SAT FECHADO:** não há mais opção de SAT para loja nova em SP. NFC-e é o único caminho — e já é o que o Bling FC emite nativamente.

**Requisitos para credenciar NFC-e na SEFAZ-SP:**
1. **Certificado digital e-CNPJ** — modelo A1 (arquivo) ou A3 (token/cartão) vinculado ao CNPJ da loja
2. **Credenciamento no Portal SEFAZ-SP** → solicitar o **CSC** (Código de Segurança do Contribuinte) de produção
3. **Inscrição Estadual (IE) em SP** — necessária antes do credenciamento (ver Seção 6.1)
4. **Configuração no Bling** — série de NFC-e separada da série do e-commerce (cada estabelecimento usa sua própria série)

- Referência SEFAZ-SP: [nfce.fazenda.sp.gov.br](https://www.nfce.fazenda.sp.gov.br/NFCeSiteContribuinte/?c=s)
- Referência obrigatoriedade 2026: [NFC-e obrigatória em SP — Certisign](https://certisign.com.br/blog/nfc-e-obrigatoria-sp)

#### ICMS-ST em SP — tintas e impermeabilizantes

Muitos produtos do catálogo IVA (tintas, impermeabilizantes, solventes) estão sujeitos a **substituição tributária (ICMS-ST)** em SP. O imposto é recolhido na indústria (IVA já recolhe) e o varejista vende sem tributar ICMS novamente — mas precisa configurar corretamente o Bling e o PDV para não tributar em duplicidade.

**Contexto 2026:** SP vem excluindo categorias da ST ao longo de 2026 (alimentos, lâmpadas, perfumaria, higiene saíram). Tintas, impermeabilizantes e material de construção **não constam nas exclusões publicadas** até jun/2026 — continuam sujeitos à ST. Confirmar com contador usando a tabela NCM da SEFAZ-SP.

> **Por que isso importa na loja física:** a NF de venda ao consumidor final deve ter o CSOSN ou CST correto indicando que o ICMS já foi recolhido por ST. Configuração errada no Bling gera recolhimento em duplicidade.

- [ ] Validar com contador quais NCMs do catálogo têm ST em SP (usando [buscadorncm.com.br/icms-st](https://buscadorncm.com.br/icms-st))
- [ ] Configurar tributação por NCM no Bling para o depósito "Loja Física EOV"
- Referência: [ICMS-ST 2026: O que muda em SP — Tributei](https://tributei.net/blog/icms-st-2026-sao-paulo/)

#### Checklist fiscal — SP

- [ ] Confirmar CNPJ de operação da loja (filial da IVA com IE em SP — ver Seção 6.1)
- [ ] Obter Inscrição Estadual (IE) em SP via SEFAZ-SP (prazo estimado: 15-30 dias)
- [ ] Adquirir certificado digital e-CNPJ A1 ou A3 para o estabelecimento de SBC
- [ ] Credenciar CNPJ na SEFAZ-SP para emissão de NFC-e → solicitar CSC de produção
- [x] ~~Verificar se SAT é obrigatório~~ → **FECHADO:** SAT descontinuado para novos estabelecimentos em SP desde nov/2024. NFC-e é o único caminho.
- [ ] Configurar série de NFC-e no Bling separada da série do e-commerce (nova série por estabelecimento)
- [ ] Mapear NCMs do catálogo com ICMS-ST em SP e configurar no Bling (depósito Loja Física EOV)
- [ ] Testar emissão de NFC-e em ambiente de homologação antes da abertura

---

### 5.8 Requisitos de Infraestrutura Tecnológica na Loja

| Item | Especificação mínima | Observação |
|---|---|---|
| Internet | Fibra com no mínimo 50 Mbps + chip 4G como backup | PDV online-dependente |
| Tablet/celular PDV | iPad ou Android robusto — 1 por caixa | Suporte ao PDV escolhido |
| Impressora de cupom não-fiscal | Para pedidos internos, C&C, listas | Térmica 80mm, Bluetooth |
| Impressora NFC-e / NF-e | Integrada ao PDV ou compartilhada | Verificar se o PDV imprime diretamente |
| Leitor de código de barras | Bluetooth, para agilizar o caixa | Opcional se câmera do tablet suprir |
| TV/monitor | Totem com catálogo digital | Tablet na parede ou monitor 32" |
| Roteador Wi-Fi | Cobertura de toda a área de venda e estoque | TP-Link ou Intelbras |

---

## 6. Requisitos Jurídicos e Regulatórios

> Esta seção mapeia o que precisa ser resolvido com advogado, contador e prefeitura antes da abertura. Não são decisões operacionais — são pré-requisitos legais sem os quais a loja não pode funcionar.

### 6.1 Estrutura Jurídica — Matriz / Filial

A primeira decisão jurídica é: a loja de SBC vai operar como **filial da IVA** (mesmo CNPJ, com sufixo de estabelecimento) ou como uma **empresa separada**?

| Modelo | Como funciona | Implicações |
|---|---|---|
| **Filial (recomendado)** | Mesmo CNPJ da IVA com novo estabelecimento em SP. A loja é mais um CNPJ/estabelecimento da mesma empresa | Contabilidade unificada, simplificado. Exige abrir filial na Junta Comercial e obter IE em SP |
| **Empresa separada** | Novo CNPJ específico para a loja | Mais complexo, custos contábeis adicionais. Faz sentido só se houver razão societária específica |

#### Como funciona o processo de filial — pesquisa confirmada

O registro de filial em SP é feito via **JUCESP** (Junta Comercial de SP), mas o arquivamento deve ser feito na **Junta Comercial da UF da SEDE** — não em SP. O processo integrado é o **Via Rápida Empresa (VRE)** / REDESIM.

**Etapas principais:**
1. Verificar se o endereço de SBC consta no contrato social — se não, fazer **aditivo contratual** primeiro
2. Arquivar abertura de filial na Junta Comercial da UF sede via **REDESIM**
3. Obter viabilidade locacional em SBC (contato: viabilidade.vre@saobernardo.sp.gov.br)
4. Obter Inscrição Estadual (IE) em SP via SEFAZ-SP
5. Obter Alvará de Funcionamento na Prefeitura SBC (ver Seção 6.2)

> **Encaminhar ao contador (ver roteiro completo na Seção 6.4):** "Precisamos abrir a loja de SBC como filial da IVA. O contrato social já permite? Como fazemos a abertura? Precisamos de Inscrição Estadual em SP? O regime tributário atual se aplica à filial?"

#### Checklist — estrutura jurídica

- [ ] Verificar se o contrato social já permite operação em SP (filial SBC)
- [ ] Definir com contador: aditivo contratual necessário?
- [ ] Arquivar abertura de filial na Junta Comercial da UF sede via REDESIM
- [ ] Obter consulta de viabilidade locacional em SBC (e-mail: viabilidade.vre@saobernardo.sp.gov.br)
- [ ] Obter Inscrição Estadual (IE) em SP via SEFAZ-SP (necessária antes do credenciamento NFC-e)
- [ ] Verificar se o regime tributário atual (Simples, LP, LR) se aplica à filial e à venda de tintas em SP
- [ ] Atualizar cadastro do CNPJ no Bling com o estabelecimento de SBC

---

### 6.2 Alvarás e Licenças — São Bernardo do Campo

Para abrir uma loja física em SBC, a IVA precisará de uma série de documentos municipais e estaduais. Alguns levam semanas — precisam ser solicitados assim que o ponto for confirmado.

| Documento | Órgão emissor | Prazo estimado | Urgência |
|---|---|---|---|
| **IE em SP** | SEFAZ-SP | 15–30 dias | 🔴 Bloqueador — necessária antes do credenciamento NFC-e |
| **Licença Ambiental** | CETESB ou Prefeitura SBC | 30–90 dias | 🔴 Bloqueador — iniciar no dia da assinatura do ponto |
| **Alvará de Funcionamento** | Prefeitura SBC via VRE/REDESIM | 5–30 dias úteis | 🔴 Necessário para abertura |
| **AVCB** (Auto de Vistoria do Corpo de Bombeiros) | Corpo de Bombeiros SP | 30–60 dias | 🟡 Após PPCI aprovado — iniciar junto com a obra |
| **Licença Sanitária** | Vigilância Sanitária SBC | 15–30 dias | 🟡 Verificar com contador se aplica ao segmento |
| **Inscrição no CCM** (Cadastro de Contribuintes Mobiliários) | Prefeitura SBC | 5–10 dias | 🟢 Rápido, depois do CNPJ |

#### Detalhamento por item

**Alvará de Funcionamento — SBC**
- Processo via **Via Rápida Empresa (VRE)** — portal REDESIM integrado com Prefeitura SBC
- Atividades de baixo risco: até **5 dias úteis**
- Atividades com produtos químicos/inflamáveis: pode exigir documentação extra + prazo 15–30 dias
- Contato consulta de viabilidade: viabilidade.vre@saobernardo.sp.gov.br
- Referência: [guiadeservicos.saobernardo.sp.gov.br — Alvará de Funcionamento](https://guiadeservicos.saobernardo.sp.gov.br/guia-de-servicos/servicos/213452/mostrar)

**AVCB — Auto de Vistoria do Corpo de Bombeiros SP**
- Validade: 1 a 5 anos (conforme avaliação de risco)
- **PPCI obrigatório para área ≥ 750 m²** — para loja de 80–150 m², verificar se é exigido PPCI completo ou apenas CLCB (certificado simplificado)
- Laudos técnicos necessários: SPDA (para-raios), instalação elétrica, combate a incêndio, gás (se houver)
- Decreto vigente: Decreto 69.118/2024 — Corpo de Bombeiros SP
- Contratar engenheiro/arquiteto assim que o ponto for confirmado — o PPCI precisa de levantamento do imóvel

**Licença Ambiental — CETESB**
- **Alta probabilidade de exigência** para varejo de tintas, solventes e impermeabilizantes — enquadramento pelo CNAE e Porte Potencial Poluidor (PPP)
- Processo: até 3 fases (LP → LI → LO); para varejo de menor porte pode ser simplificado
- SBC tem competência municipal para licenciamento de alguns empreendimentos — verificar se a competência é CETESB ou Prefeitura SBC para o porte/CNAE da loja
- **Este é o item de maior risco de prazo** — iniciar o processo de enquadramento assim que o endereço for confirmado
- Portal: [e.cetesb.sp.gov.br](https://e.cetesb.sp.gov.br/portal-servicos-frontend/)
- Licenciamento ambiental SBC: [guiadeservicos.saobernardo.sp.gov.br — Licença Ambiental](https://guiadeservicos.saobernardo.sp.gov.br/guia-de-servicos/servicos/213672/mostrar)

> **Caminho crítico de abertura:**
> ```
> Confirmar ponto → IE em SP + Licença Ambiental (em paralelo)
>                                    ↓
>                        Alvará de Funcionamento
>                                    ↓
>                         AVCB (durante a obra)
>                                    ↓
>                               Abertura da loja
> ```

#### Checklist — alvarás e licenças

- [ ] Confirmar endereço e metragem do ponto → base para todos os pedidos
- [ ] Consultar viabilidade locacional em SBC (viabilidade.vre@saobernardo.sp.gov.br)
- [ ] Iniciar processo de enquadramento na CETESB (produto químico) — prazo longo
- [ ] Protocolar pedido de Alvará de Funcionamento via VRE/REDESIM
- [ ] Contratar engenheiro para laudo PPCI / AVCB (Corpo de Bombeiros SP)
- [ ] Verificar com contador/advogado se Vigilância Sanitária se aplica ao segmento
- [ ] Protocolar IE em SP via SEFAZ-SP (ver Seção 5.7)

---

### 6.3 Outros Requisitos Regulatórios

| Item | Relevância | Ação |
|---|---|---|
| FISPQ (Fichas de Segurança) | Obrigatório para produtos químicos na loja | Ter as FISPQs dos produtos no estabelecimento |
| EPI e treinamento | Manuseio de produtos químicos (tintas, solventes) | Treinar equipe, disponibilizar EPIs básicos |
| Sinalização de segurança | ABNT NBR 13434 | Placas de saída de emergência, extintores, etc. |
| Cadastro INMETRO | Alguns produtos podem exigir | Verificar com equipe técnica da IVA |

---

### 6.4 Roteiro para Reunião com Contador / Advogado

> Usar na reunião com o contador/advogado da IVA. As perguntas do **Bloco 1** são pré-requisito para qualquer decisão de sistema (CNPJ, NF, etc).

**Bloco 1 — Estrutura Jurídica (define arquitetura fiscal)**

1. **A loja de SBC vai ser filial da IVA (mesmo CNPJ) ou empresa separada?**
   — Resposta esperada: filial. Se empresa separada, precisa de novo CNPJ, novo Bling, novo contrato Wake → complexidade muito maior.
2. **O contrato social atual da IVA já permite operação em SP / comércio varejista? Ou precisa de aditivo?**
   — Se precisar de aditivo: qual o prazo? Isso bloqueia o processo de filial.
3. **O regime tributário atual (Simples/LP/LR) se aplica à filial de SP? Alguma restrição?**
   — Tintas com ICMS-ST podem ter implicação no Simples Nacional — confirmar.

**Bloco 2 — Fiscal SP (define configurações no Bling)**

4. **Qual o prazo para obter a Inscrição Estadual (IE) em SP? O processo começa antes ou depois do CNPJ filial?**
   — IE em SP é pré-requisito para credenciar NFC-e na SEFAZ-SP.
5. **Quais NCMs do catálogo IVA têm ICMS-ST em SP? Como isso aparece na NFC-e?**
   — O contador deve mapear a lista de NCMs com ST para configuração no Bling.
6. **Como funciona a transferência de estoque CD → Loja Física? Qual CFOP, qual documentação?**
   — Relevante para configurar a NF de transferência interna no Bling.

**Bloco 3 — Licenças e Alvarás (define o caminho crítico de abertura)**

7. **A venda de tintas, solventes e impermeabilizantes exige Licença Ambiental da CETESB em SBC? Ou a competência é da Prefeitura de SBC?**
   — Esta é a pergunta mais crítica de prazo. Licença CETESB pode levar 30–90 dias.
8. **Qual o enquadramento do CNAE para comércio varejista de tintas e produtos de construção em SBC? É atividade de "alto risco" para fins de alvará?**
   — Define o prazo e a complexidade do Alvará de Funcionamento.
9. **O AVCB (Corpo de Bombeiros) para loja de 80–150 m² em SP exige PPCI completo ou apenas CLCB?**
   — Define se precisará contratar projeto de engenharia ou se é processo simplificado.

**Bloco 4 — Cronograma (define o prazo real de abertura)**

10. **Qual o menor prazo possível para ter CNPJ filial + IE SP + Alvará SBC em ordem?**
    — O contador deve montar o cronograma paralelo de abertura. A resposta define se a loja abre em 30, 60 ou 90 dias.

---

## 7. Operação

### 6.1 Equipe Mínima — Fase de Abertura

| Função | Qtd | Perfil |
|---|---|---|
| Gerente de loja | 1 | Varejo + conhecimento técnico em construção, acesso a todos os sistemas |
| Vendedor técnico | 1–2 | Sabe indicar produto para o problema do cliente |
| Operador de estoque | 1 (pode acumular com vendedor) | Recebe mercadoria, dá entrada no Bling, processa OMS e C&C |

### 6.2 Processos a Documentar (em `operacoes/`)

- [ ] Abertura e fechamento de caixa
- [ ] Recebimento de mercadoria (entrada Bling + conferência física)
- [ ] Reposição de estoque e inventário rotativo
- [ ] Atendimento e venda consultiva no balcão
- [ ] Processamento de pedidos OMS (pedidos online atendidos pela loja)
- [ ] Atendimento Click & Collect (identificação, separação, entrega)
- [ ] Política de troca e devolução (definida — ver Seção 7.2)

### 7.2 Políticas Operacionais Definidas

#### Troca e Devolução

| Situação | Regra |
|---|---|
| Produto com defeito | Troca imediata — **obrigatório por lei** (CDC art. 26: 90 dias para produtos duráveis) |
| Produto errado (escolha do cliente) | Troca por outro produto em até **7 dias corridos** com NF e produto intacto — política voluntária |
| Devolução em dinheiro | **Não** — crédito ou troca apenas |
| Cliente não gostou (sem defeito) | **Não** — loja física não tem obrigação de aceitar arrependimento |
| Compra do site com problema | **Não processar na loja** — encaminhar ao SAC do e-commerce |
| Click & Collect com problema | Troca na loja — mesmo fluxo do presencial |

#### Abastecimento e Reposição

**Fase 1 — meses 1 e 2 (sem histórico de vendas):**
- Reposição semanal fixa: gerente solicita **toda segunda-feira**, mercadoria chega **quarta ou quinta**
- Gerente consolida pedido de transferência no Bling → Logística IVA aprova e despacha

**Fase 2 — a partir do mês 3:**
- Configurar **estoque mínimo por SKU** no Bling → alerta automático de reposição
- Reposição sob demanda, mantendo cadência semanal para os itens de alto giro

**Lead time interno:** CD → Loja SBC estimado em 1–2 dias.

#### Confia! na Loja Física

Programa atual é 100% digital (link rastreado). Integração presencial prevista para **Fase 2 pós-abertura**:
- Campo customizado "Código Confia!" no fechamento da venda no Bling FC
- Vendedor pergunta no caixa: "Você tem um código de afiliado?"
- Exportação semanal manual para o painel do Confia! até haver integração nativa

### 7.3 Reporting — Dashboard Semanal

Gerado toda **segunda-feira** com os dados da semana anterior.

| Indicador | Fonte | Frequência |
|---|---|---|
| Faturamento loja física | Bling FC | Semanal |
| Ticket médio loja | Bling FC (faturamento ÷ nº vendas) | Semanal |
| Top 10 SKUs vendidos | Bling FC — ranking por quantidade | Semanal |
| Novos clientes cadastrados na loja | Bling — tag "loja-fisica" | Semanal |
| Pedidos C&C realizados | Wake Commerce | Semanal |
| Taxa de C&C | C&C entregues ÷ C&C gerados | Semanal |
| Giro de estoque | Vendas ÷ estoque médio | Mensal |

**Comparativo mensal (todo dia 1):**
- Faturamento loja vs. e-commerce
- Ticket médio loja vs. e-commerce
- C&C como % do total de pedidos online

---

## 7. Identidade Visual da Loja

DNA visual: rústico, direto, sem frescura — fiel ao Escuta o Véio!
Referências de marca em `marca/DNA.md` e `marca/CLAUDE.md`.

- [ ] Aplicação de marca na fachada (letreiro, adesivo de vitrine)
- [ ] Sinalização interna por categoria de problema (impermeabilização, pintura, acabamento)
- [ ] Materiais de PDV: wobblers, stoppers, banners de linha
- [ ] Uniformes com identidade do canal
- [ ] Embalagens e sacolas com marca EOV
- [ ] Artes: briefar em `loja-fisica/identidade-visual/`

---

## 8. Comunicação e Lançamento

### Pré-abertura
- [ ] Teaser nas redes ("algo está chegando")
- [ ] Campanha de expectativa no e-commerce
- [ ] E-mail/WhatsApp para base de clientes EOV da região

### Abertura
- [ ] Evento de inauguração — profissionais da região + clientes
- [ ] Promoção exclusiva de abertura
- [ ] Cobertura em vídeo para redes sociais

### Pós-abertura
- [ ] Monitoramento intensivo: tráfego, ticket médio, conversão, mix mais vendido
- [ ] Ajuste de gôndola e mix com base em dados reais
- [ ] Rotina de conteúdo sobre a loja nos canais digitais

---

## 9. Viabilidade Financeira

> Preencher antes do GO / NO-GO final.

| Item | Estimativa | Status |
|---|---|---|
| Aluguel mensal | — | A levantar |
| Depósito / caução | — | A levantar |
| Reforma e adequação | — | A levantar |
| Estoque inicial (custo) | — | A levantar |
| Equipamentos (tablet, impressora, maquininha) | ~ R$ 3.000–6.000 | Estimativa inicial |
| Sistemas e tecnologia (PDV, NFC-e — SAT descartado) | ~ R$ 500–2.000 | Depende do PDV escolhido |
| Equipe (CLT + encargos, 3 pessoas) | — | A levantar |
| Marketing de abertura | — | A levantar |
| **Investimento total estimado** | — | — |
| **Faturamento mínimo para break-even** | — | — |

---

## 10. Marcos e Próximos Passos

### Fase 0 — Decisão (imediato)

- [ ] Confirmar localização e custo do ponto
- [ ] Confirmar UF → mapear obrigação fiscal com contador
- [ ] Confirmar CNPJ de operação (mesmo do e-commerce ou novo?)
- [ ] Preencher planilha de viabilidade
- [ ] GO / NO-GO

### Fase 1 — Especificação Técnica (semanas 1–2 após GO)

- [ ] Agendar demo com Wake para configuração de OMS multi-fulfillment e C&C
- [ ] Agendar demo com Bling para validar Frente de Caixa (ou definir Wake PDV)
- [ ] Decidir PDV e maquininha
- [ ] Iniciar configuração do depósito no Bling
- [ ] Mapear regras de roteamento de pedido com logística

### Fase 2 — Implantação (semanas 2–5)

- [ ] Obras e adequação do espaço
- [ ] Contratar equipe
- [ ] Configurar Wake OMS: novo fulfillment point + Click & Collect
- [ ] Configurar Bling: depósito, NFC-e, usuários, integração PDV
- [ ] Credenciar NFC-e na SEFAZ
- [ ] Credenciar NFC-e: certificado e-CNPJ A1/A3 + Portal SEFAZ-SP + CSC de produção
- [ ] Montar identidade visual da loja
- [ ] Teste de ponta a ponta: venda presencial + Click & Collect + OMS

### Fase 3 — Abertura (semana 6–8)

- [ ] Evento de inauguração
- [ ] Campanha de abertura nos canais digitais
- [ ] Monitoramento diário nas primeiras 4 semanas

---

## 11. Pendências e Decisões em Aberto

| # | Questão | Urgência | Quem resolve |
|---|---|---|---|
| **ESTOQUE / SISTEMAS** | | | |
| 1 | Definir cenário de PDV: A, B ou C — depende da demo Wake U | 🔴 Alta | Gustavo — após demo |
| 2 | **[CRÍTICO]** On Hands aceita dinheiro/troco/caixa físico? Se não → Cenário B descartado | 🔴 Alta | Wake (demo — item 1 do roteiro) |
| 3 | NFC-e / NF-e no On Hands: nativo ou depende do Bling? | 🔴 Alta | Wake (demo — item 2 do roteiro) |
| 4 | Wake OMS API agnóstica: configuração ou desenvolvimento? ([doc](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407)) | 🔴 Alta | Wake (demo — item 3 do roteiro) |
| 5 | Custo Wake U (1 loja) + Wake OMS (1 loja + 1 CD) | 🔴 Alta | CS Wake (demo — itens 7 e 8) |
| ~~6~~ | ~~Prateleira Infinita requer Wake OMS separado?~~ | ✅ Fechado | Pode ser contratada isoladamente |
| ~~7~~ | ~~Bling FC: tablet/celular, offline, maquininhas?~~ | ✅ Fechado | Ver Seção 5.2 e lista SmartPOS |
| **JURÍDICO / REGULATÓRIO** | | | |
| 6 | Filial ou CNPJ novo para a loja? | 🔴 Alta | Contador — usar roteiro Seção 6.4 |
| 7 | Abrir IE em SP — processo via SEFAZ-SP, prazo 15–30 dias | 🔴 Alta | Contador — pré-requisito para NFC-e |
| ~~8~~ | ~~SAT obrigatório em SP?~~ | ✅ Fechado | **SAT descontinuado para novos estabelecimentos em SP desde nov/2024. NFC-e é o único caminho** |
| 8 | NFC-e em SP: credenciar na SEFAZ-SP, obter CSC, certificado e-CNPJ A1/A3, série separada | 🔴 Alta | Contador — após obter IE |
| 9 | Licença Ambiental (CETESB ou Prefeitura SBC) — enquadramento pelo CNAE | 🔴 Alta | Advogado / Contador — **item de maior risco de prazo** |
| 10 | Alvará de funcionamento Prefeitura SBC — via VRE/REDESIM (viabilidade.vre@saobernardo.sp.gov.br) | 🔴 Alta | Responsável administrativo |
| 11 | AVCB — verificar PPCI completo ou CLCB para loja 80–150 m² | 🟡 Média | Engenheiro / Arquiteto |
| **OPERACIONAL** | | | |
| 12 | Ponto específico em SBC: bairro, endereço, metragem, custo | 🔴 Alta | Gustavo / IVA — trava CETESB e Alvará |
| ~~13~~ | ~~Mix inicial de produtos~~ | ✅ Metodologia definida | Top 150 por volume 90 dias → filtrar por margem > 20% e peso < 20 kg → ~80–100 SKUs. Ver Seção 4. |
| ~~14~~ | ~~Regra de roteamento de pedidos~~ | ✅ Fechado | Fase 1: loja só C&C. Revisão em 90 dias de operação. Ver Seção 5.3. |
| ~~15~~ | ~~Política de troca e devolução~~ | ✅ Definida | Defeito: 90 dias (CDC). Troca por produto errado: 7 dias com NF (voluntária). Devolução em dinheiro: não. Site: SAC e-commerce. Ver Seção 7.2. |
| ~~16~~ | ~~Fluxo de abastecimento~~ | ✅ Definido | Fase 1: reposição semanal fixa (pedido na 2ª, entrega na 4ª/5ª). Fase 2 (mês 3+): ponto de pedido automático no Bling. Ver Seção 7.2. |
| ~~17~~ | ~~Confia! na loja física~~ | ✅ Decisão | Fase 2 (pós-abertura) — campo "Código Confia!" manual no Bling FC. Programa atual é 100% digital, não bloquear abertura. |
| ~~18~~ | ~~Reporting~~ | ✅ Definido | Dashboard semanal: faturamento, ticket médio, top 10 SKUs, novos clientes, C&C realizados, taxa C&C, giro de estoque. Ver Seção 7.3. |

---

## 12. Links e Fontes para Validação

> Links coletados durante a especificação. Itens marcados com *(requer login)* precisam de acesso autenticado para leitura completa.

### Bling

| Link | Conteúdo | Acesso |
|---|---|---|
| [bling.com.br/funcionalidades/frente-de-caixa](https://www.bling.com.br/funcionalidades/frente-de-caixa) | Visão geral do Bling Frente de Caixa | Público |
| [bling.com.br/funcionalidades/integracao-pos](https://www.bling.com.br/funcionalidades/integracao-pos) | Integração com maquininhas SmartPOS | Público |
| [ajuda.bling.com.br — Fazer vendas no FC](https://ajuda.bling.com.br/hc/pt-br/articles/360035625414-Fazer-vendas-no-Frente-de-Caixa) | Como operar o caixa no Bling FC | Requer login |
| [ajuda.bling.com.br — Configuração máquina POS](https://ajuda.bling.com.br/hc/pt-br/articles/17793394706711-Guia-geral-Configura%C3%A7%C3%A3o-da-m%C3%A1quina-de-cart%C3%A3o-POS-no-Frente-de-Caixa-do-Bling) | Guia de configuração SmartPOS no FC | Requer login |
| [ajuda.bling.com.br — Stone POS](https://ajuda.bling.com.br/hc/pt-br/articles/33566478345239-Como-configurar-a-m%C3%A1quina-de-cart%C3%A3o-POS-Stone-no-Bling) | Configuração maquininha Stone P2 | Requer login |
| [ajuda.bling.com.br — Caixa POS](https://ajuda.bling.com.br/hc/pt-br/articles/33612346388503-Como-configurar-a-m%C3%A1quina-de-cart%C3%A3o-POS-Caixa-no-Bling) | Configuração maquininha Caixa DX8000/P2-A11 | Requer login |
| [ajuda.bling.com.br — CPlug](https://ajuda.bling.com.br/hc/pt-br/articles/25940324197783-Conhe%C3%A7a-a-CPlug-Solu%C3%A7%C3%B5es-que-facilitam-o-seu-neg%C3%B3cio) | CPlug — PDV offline integrado ao Bling | Requer login |
| [ajuda.bling.com.br — Frente de Caixa (seção)](https://ajuda.bling.com.br/hc/pt-br/sections/360005577073-Frente-de-Caixa) | Todos os artigos de ajuda do FC | Requer login |

### Wake

| Link | Conteúdo | Acesso |
|---|---|---|
| [wake.tech/wake-u](https://wake.tech/wake-u/) | Wake U — Unified Commerce (On Hands, Prateleira Infinita, Agenda do Vendedor) | Público |
| [wake.tech/wake-oms](https://wake.tech/wake-oms/) | Wake OMS — orquestração de pedidos e múltiplos CDs | Público |
| [wake.tech/wake-commerce](https://wake.tech/wake-commerce/) | Wake Commerce — plataforma de e-commerce | Público |
| [wake.tech/blog/conheca-wake-oms](https://wake.tech/blog/conheca-wake-oms/) | Blog: funcionalidades do Wake OMS | Público |
| [atendimento.wake.tech — Centros de Distribuição](https://atendimento.wake.tech/hc/pt-br/articles/21406540759575-Centros-de-Distribui%C3%A7%C3%A3o) | Configuração de múltiplos CDs na Wake | Requer login |
| [atendimento.wake.tech — API agnóstica PDVs](https://atendimento.wake.tech/hc/pt-br/articles/32054322688407-WAKE-OMS-APIs-de-Integra%C3%A7%C3%A3o-agn%C3%B3stica-com-PDVs) | APIs para integrar qualquer PDV ao Wake OMS | Requer login |

### Fiscal / Jurídico / Licenças

| Link | Conteúdo | Acesso |
|---|---|---|
| [nfce.fazenda.sp.gov.br](https://www.nfce.fazenda.sp.gov.br/NFCeSiteContribuinte/?c=s) | Portal SEFAZ-SP — credenciamento NFC-e e CSC de produção | Público |
| [certisign.com.br — NFC-e obrigatória SP 2026](https://certisign.com.br/blog/nfc-e-obrigatoria-sp) | NFC-e obrigatória em SP a partir de 01/01/2026 — requisitos e prazos | Público |
| [crcsp.org.br — Fim do SAT em SP 2026](https://online.crcsp.org.br/portal/noticias/noticia.asp?c=10087) | SP encerra emissão pelo SAT e torna NFC-e obrigatória | Público |
| [tributei.net — ICMS-ST 2026 SP](https://tributei.net/blog/icms-st-2026-sao-paulo/) | O que muda no ICMS-ST em São Paulo em 2026 | Público |
| [buscadorncm.com.br/icms-st](https://buscadorncm.com.br/icms-st) | Consulta de ICMS-ST por NCM, CEST e Estado | Público |
| [substituicaotributaria.com — alterações 2026](https://www.substituicaotributaria.com/SST/substituicao-tributaria/regra-geral/24/confira-as-alteracoes-da-substituicao-tributaria-para-2026) | Alterações da ST para 2026 — lista de produtos excluídos | Público |
| [e.cetesb.sp.gov.br](https://e.cetesb.sp.gov.br/portal-servicos-frontend/) | Portal de Licenciamento Ambiental CETESB — solicitações online | Público |
| [cetesb.sp.gov.br — Atividades passíveis de licenciamento](https://cetesb.sp.gov.br/licenciamentoambiental/wp-content/uploads/sites/32/2025/02/Atividades-passiveis-de-licenciamento.pdf) | PDF com lista de CNAEs que exigem licença CETESB | Público |
| [guiadeservicos.saobernardo.sp.gov.br — Alvará](https://guiadeservicos.saobernardo.sp.gov.br/guia-de-servicos/servicos/213452/mostrar) | Alvará de Funcionamento via VRE — Prefeitura SBC | Público |
| [guiadeservicos.saobernardo.sp.gov.br — Licença Ambiental SBC](https://guiadeservicos.saobernardo.sp.gov.br/guia-de-servicos/servicos/213672/mostrar) | Renovação de Licença Ambiental — Prefeitura SBC | Público |
| [institutojucesp.sp.gov.br — Filial](https://www.institucional.jucesp.sp.gov.br/) | JUCESP — abertura/alteração de filial em SP | Público |
| [dedcontabilidade.com.br — Abertura de filial SP](https://dedcontabilidade.com.br/abertura-de-filial-em-sao-paulo-estrategias-para-expansao/) | Guia prático de abertura de filial em São Paulo | Público |

---

## Histórico de Decisões

| Data | Decisão |
|---|---|
| 2026-06-05 | Início do PDI — oportunidade identificada, Go/No-Go pendente |
| 2026-06-05 | Localização definida: São Bernardo do Campo — SP (ABC Paulista) |
| 2026-06-05 | Modelo definido: loja própria |
| 2026-06-05 | Integrações: OMS Wake + Click & Collect + Bling ERP |
| 2026-06-05 | PDV: portátil (tablet/celular), integrado ao Bling — opções Bling FC ou Wake PDV |
| 2026-06-05 | Pagamento: cartão, Pix e dinheiro |
| 2026-06-05 | Cadastro de clientes: base EOV unificada no Bling com tag "loja-fisica" |
| 2026-06-05 | Estoque: depósito separado "Loja Física EOV" no Bling; Wake consome via integração |
| 2026-06-05 | PDV definido: Bling Frente de Caixa (Wake PDV descartado para o caixa presencial) |
| 2026-06-05 | Pagamento: cartão à vista, Pix e dinheiro — sem parcelamento sem juros na fase inicial |
| 2026-06-05 | Fluxo Bling + Wake já é automático no e-commerce (modelo a replicar para a loja física) |
| 2026-06-05 | OMS fase 1: loja física atende somente C&C — entregas web seguem pelo CD |
| 2026-06-05 | SAT descartado: novo estabelecimento em SP = NFC-e obrigatória (SAT descontinuado para novos desde nov/2024) |
| 2026-06-05 | Roteiro para contador criado — 10 perguntas em 4 blocos (estrutura jurídica, fiscal SP, licenças, cronograma) |
| 2026-06-05 | Caminho crítico de abertura mapeado: IE SP + Licença Ambiental CETESB são os itens de maior prazo |
| 2026-06-05 | Mix inicial: metodologia definida — top 150 SKUs por volume (90 dias), filtrar margem < 20% e peso > 20 kg |
| 2026-06-05 | Roteamento fase 1 confirmado: loja só C&C — entregas web pelo CD. Revisão em 90 dias |
| 2026-06-05 | Política de troca: defeito 90 dias (CDC), troca voluntária 7 dias, sem devolução em dinheiro |
| 2026-06-05 | Abastecimento: reposição semanal fixa (fase 1) → ponto de pedido automático Bling (fase 2, mês 3+) |
| 2026-06-05 | Confia! na loja física: fase 2 pós-abertura — não bloquear abertura |
| 2026-06-05 | Dashboard semanal definido: 7 KPIs principais + comparativo mensal loja vs. e-commerce |
| 2026-06-05 | Wake U = Wake OMS confirmado — não são produtos separáveis. Usar Wake U implica contratar Wake OMS |
| 2026-06-05 | DITO CRM já integrado ao Bling nativamente (CPF como chave, D-1) — loja física unifica base sem integração extra |
