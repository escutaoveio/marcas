# PDR — Confia! PRO
## Product Design Requirements — Plataforma de Orçamento e Afiliados para Profissionais

**Versão:** 0.2 — Detalhamento Técnico  
**Data:** 2026-06-11  
**Responsável:** IVA Química — Produto & Tecnologia  
**Status:** Em validação de viabilidade

---

## 1. Sumário Executivo

O Confia! existe hoje como um programa de afiliados para a IVA Química — qualquer pessoa pode indicar produtos e ganhar comissão. O programa tem potencial, mas opera de forma isolada, sem tooling para o principal público-alvo: o profissional da construção civil.

Este PDR descreve a evolução do Confia! para uma **plataforma de orçamento e recomendação de produtos** integrada ao Qualifica PRO. O profissional formado pela plataforma passa a ter acesso a uma ferramenta que o ajuda a **orçar obras**, **recomendar produtos de múltiplos e-commerces** e **receber comissão** sobre as vendas geradas — tudo em um único lugar.

A arquitetura é **agnóstica de plataforma**, capaz de integrar qualquer e-commerce independente da tecnologia subjacente (Wake Commerce, Shopify, Tray, Nuvemshop etc.). A confirmação de comissão é unificada via **Bling** — disponibilizada apenas após emissão da NF-e, eliminando risco de pagamento sobre pedidos cancelados.

---

## 2. Contexto e Diagnóstico

### 2.1 Estado Atual

| Produto | Estado | Limitação |
|---|---|---|
| **Qualifica PRO** | Ativo — cursos e eventos presenciais | Não há continuidade pós-formação |
| **Confia!** | Ativo — programa de afiliados | Focado em IVA Química; sem ferramentas de trabalho |
| **Escuta o Véio!** | Ativo — e-commerce principal IVA | Não tem programa de afiliados nativo estruturado |
| **Fácil Decor** | Em desenvolvimento | Sem integração com profissionais |

### 2.2 O Gap

O profissional formado pelo Qualifica PRO termina o curso e enfrenta um vazio: **nenhuma ferramenta para operacionalizar o que aprendeu no dia a dia**. Para fechar uma obra, precisa:

- Pesquisar produtos em múltiplos e-commerces
- Montar planilhas manuais de orçamento
- Compartilhar listas de produtos com o cliente por WhatsApp
- Perder a comissão porque não tem como rastrear a venda

### 2.3 A Oportunidade

Profissionais com acesso a ferramentas vendem mais, recomendam mais e geram mais lealdade à marca. O Confia! pode ser o CRM ativo do profissional — ao mesmo tempo que gera receita para a IVA Química e receita extra para o profissional.

---

## 3. Visão do Produto

> **"Do curso à obra, com uma ferramenta só."**

O Confia! PRO é uma plataforma (web + app mobile) onde o profissional:

1. **Monta orçamentos de obra** com produtos de qualquer e-commerce integrado
2. **Compartilha o orçamento** com o cliente como link ou PDF
3. **Ganha comissão** quando o cliente compra através do orçamento
4. **Acompanha suas métricas** — vendas geradas, comissões, histórico de orçamentos

O Confia! PRO é uma **unidade de negócio dentro do ecossistema Qualifica PRO**, com acesso exclusivo (ou prioritário) para alunos certificados.

---

## 4. Personas

### Persona A — O Profissional Aplicador (usuário primário)

| Campo | Descrição |
|---|---|
| **Quem é** | Pintor, impermeabilizador, aplicador de gesso, marceneiro |
| **Formação** | Aluno atual ou ex-aluno do Qualifica PRO |
| **Dor** | Perde tempo montando orçamentos manuais; não recebe comissão das indicações |
| **Motivação** | Ganhar dinheiro extra; parecer mais profissional para o cliente |
| **Device** | Principalmente smartphone; acesso mobile é crítico |

### Persona B — O Cliente Final (usuário secundário)

| Campo | Descrição |
|---|---|
| **Quem é** | Proprietário de imóvel, síndico, pequeno construtor |
| **Relação** | Recebe o orçamento do profissional |
| **Comportamento** | Não cria conta; acessa orçamento por link e conclui a compra |

### Persona C — O Gestor de Canal (usuário interno)

| Campo | Descrição |
|---|---|
| **Quem é** | Equipe IVA Química / Qualifica PRO |
| **Papel** | Gerencia lojas parceiras, valida comissões, acompanha métricas |

---

## 5. Requisitos Funcionais

### Módulo 1 — Autenticação e Perfil Profissional

| ID | Requisito | Prioridade |
|---|---|---|
| F-101 | Login via SSO com conta do Qualifica PRO | Alta |
| F-102 | Perfil com dados profissionais (especialidade, região, certificações) | Alta |
| F-103 | Badge de "Profissional Certificado Qualifica PRO" no perfil | Média |
| F-104 | Histórico de orçamentos e comissões no painel | Alta |
| F-105 | Configuração de dados bancários/PIX para recebimento de comissões | Alta |

### Módulo 2 — Catálogo Unificado

| ID | Requisito | Prioridade |
|---|---|---|
| F-201 | Busca de produtos por nome, SKU ou categoria em todas as lojas integradas | Alta |
| F-202 | Filtro por loja de origem, marca, categoria, faixa de preço | Alta |
| F-203 | Exibição de estoque em tempo real (ou com cache curto) | Alta |
| F-204 | Página de detalhe do produto com fotos, descrição técnica e link para loja | Média |
| F-205 | Favoritar produtos para rápida adição a orçamentos futuros | Baixa |

### Módulo 3 — Orçamentador de Obras

| ID | Requisito | Prioridade |
|---|---|---|
| F-301 | Criar novo orçamento com nome do projeto e dados do cliente | Alta |
| F-302 | Adicionar produtos ao orçamento com quantidade e unidade de medida | Alta |
| F-303 | Campo de serviço/mão-de-obra (item livre, sem integração com e-commerce) | Média |
| F-304 | Aplicação de margem do profissional (percentual ou valor fixo por item) | Média |
| F-305 | Cálculo automático de subtotais e total do orçamento | Alta |
| F-306 | Geração de link único do orçamento (modo visualização para o cliente) | Alta |
| F-307 | Exportação do orçamento em PDF com logo do profissional e identidade visual | Alta |
| F-308 | Envio do orçamento por WhatsApp com mensagem pré-formatada | Alta |
| F-309 | Controle de validade do orçamento (expiração configurável) | Média |
| F-310 | Status do orçamento: Rascunho / Enviado / Aprovado / Expirado | Média |
| F-311 | Duplicar orçamento para reaproveitar como base | Baixa |

### Módulo 4 — Portal do Cliente (visualização do orçamento)

| ID | Requisito | Prioridade |
|---|---|---|
| F-401 | Página pública do orçamento (sem necessidade de criar conta) | Alta |
| F-402 | Botão "Comprar" por item que direciona para a loja com link afiliado | Alta |
| F-403 | Botão "Comprar tudo" que direciona para carrinho unificado (quando possível) | Baixa |
| F-404 | Botão "Aprovar orçamento" que notifica o profissional | Média |
| F-405 | Exibição do nome, foto e certificações do profissional no orçamento | Média |

### Módulo 5 — Comissões e Tracking

| ID | Requisito | Prioridade |
|---|---|---|
| F-501 | Geração de link rastreável por profissional + produto + loja | Alta |
| F-502 | Registro de clique no link e redirecionamento para a loja | Alta |
| F-503 | Recebimento de webhook "pedido criado" das lojas integradas → comissão PENDENTE | Alta |
| F-504 | Atribuição de comissão ao profissional por janela de tempo (30 dias após o clique) | Alta |
| F-505 | Recebimento de webhook `notaFiscal.emitida` do Bling → comissão CONFIRMADA | **Crítico** |
| F-506 | Recebimento de webhook `notaFiscal.cancelada` do Bling → comissão CANCELADA | **Crítico** |
| F-507 | Cruzamento automático NF Bling ↔ pedido e-commerce via `numeroPedidoLoja` | **Crítico** |
| F-508 | Painel de reconciliação: comissões PENDENTES sem NF correspondente após 7 dias | Alta |
| F-509 | Painel de comissões do profissional: PENDENTE / CONFIRMADA / CANCELADA / PAGA | Alta |
| F-510 | Solicitação de saque apenas de comissões CONFIRMADAS | Alta |
| F-511 | Aprovação de saque pela equipe IVA (painel admin) | Alta |
| F-512 | Histórico completo de transações por profissional | Alta |

### Módulo 6 — Painel Administrativo (interno IVA)

| ID | Requisito | Prioridade |
|---|---|---|
| F-601 | Gestão de lojas parceiras (adicionar, remover, configurar comissão base) | Alta |
| F-602 | Gestão de profissionais afiliados (aprovar, suspender, ver métricas) | Alta |
| F-603 | Dashboard de performance: GMV gerado, comissões pagas, profissionais ativos | Alta |
| F-604 | Relatório de orçamentos criados × convertidos × valor gerado | Média |
| F-605 | Configuração de taxa de comissão por loja, categoria ou produto | Alta |

---

## 6. Requisitos Não-Funcionais

| Categoria | Requisito |
|---|---|
| **Performance** | Busca no catálogo em < 1s (com cache); carregamento de página em < 2s |
| **Disponibilidade** | SLA de 99,5% para o app e portal do cliente |
| **Escala** | Suportar 10.000 profissionais ativos sem degradação |
| **Segurança** | Autenticação OAuth 2.0 / OIDC; HTTPS obrigatório; dados de PIX criptografados em repouso |
| **Conformidade** | LGPD: consentimento explícito para uso de dados; IPs não armazenados em texto puro (hash) |
| **Offline** | App deve permitir visualizar orçamentos offline (modo leitura) |
| **Mobile-first** | Interface otimizada para uso em smartphone no campo de obra |
| **Agnóstico** | Adicionar nova plataforma de e-commerce sem alterar a lógica de negócio central |

---

## 7. Arquitetura Técnica

### 7.1 Visão Geral do Sistema

```
┌──────────────────────────────────────────────────────────────────────┐
│                          USUÁRIOS                                    │
│   Profissional (Web/App)    │   Cliente Final (Portal Público)       │
│   Equipe IVA (Admin)        │                                        │
└────────────┬────────────────┴─────────────────────┬─────────────────┘
             │ HTTPS                                 │ HTTPS
┌────────────▼──────────────────────┐  ┌────────────▼─────────────────┐
│   CONFIA! WEB                     │  │   PORTAL PÚBLICO             │
│   Next.js 14 (App Router)         │  │   Next.js SSR /p/[token]     │
│   Vercel                          │  │   Sem autenticação           │
└────────────┬──────────────────────┘  └────────────┬─────────────────┘
             │                                       │
┌────────────▼──────────────────────────────────────▼─────────────────┐
│                       CONFIA! APP MOBILE                             │
│                  React Native + Expo (iOS + Android)                 │
└──────────────────────────────┬───────────────────────────────────────┘
                               │ REST API / HTTPS
┌──────────────────────────────▼───────────────────────────────────────┐
│                    BACKEND — NestJS (Railway)                        │
│                                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  ┌───────────┐ │
│  │ Auth Module │  │ Quote Module │  │Catalog Mod. │  │Track.Mod. │ │
│  └─────────────┘  └──────────────┘  └─────────────┘  └───────────┘ │
│  ┌──────────────────┐  ┌────────────────────┐  ┌─────────────────┐  │
│  │ Commission Module│  │   Payout Module    │  │  Admin Module   │  │
│  └──────────────────┘  └────────────────────┘  └─────────────────┘  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                 INTEGRATION LAYER (Adapters)                 │   │
│  │  WakeAdapter │ NuvemshopAdapter │ ShopifyAdapter │ TrayAdapt.│   │
│  │                  BlingAdapter (único para todas as lojas)    │   │
│  └──────────────────────────────────────────────────────────────┘   │
└───────────┬──────────────────────────────────────────────────────────┘
            │
┌───────────▼──────────────────────────────────────────────────────────┐
│                       DADOS E CACHE                                  │
│   PostgreSQL (Supabase)         │   Redis (Upstash)                  │
│   BullMQ (filas de job)         │   Cloudflare R2 (PDFs)            │
└───────────┬──────────────────────────────────────────────────────────┘
            │
┌───────────▼──────────────────────────────────────────────────────────┐
│                       SISTEMAS EXTERNOS                              │
│  Wake API │ Nuvemshop API │ Shopify API │ Tray API │ Bling API v3    │
│  Asaas (PIX em massa) │ Resend (e-mail) │ WhatsApp (link nativo)    │
└──────────────────────────────────────────────────────────────────────┘
```

### 7.2 Padrão Adapter — Núcleo da Plataformização

Cada plataforma de e-commerce implementa a mesma interface interna. Novos e-commerces são integrados implementando apenas o `EcommerceAdapter` — o resto do sistema não muda.

```typescript
interface EcommerceAdapter {
  // Catálogo
  searchProducts(query: string, filters: ProductFilter): Promise<Product[]>;
  getProduct(externalId: string): Promise<Product>;
  getStock(externalId: string): Promise<StockInfo>;

  // Afiliado
  generateAffiliateLink(productId: string, affiliateId: string): Promise<string>;

  // Pedido criado (atribuição) — confirmação vem do Bling, não do e-commerce
  registerOrderWebhook(callbackUrl: string): Promise<void>;
  parseOrderCreatedWebhook(payload: unknown): OrderCreatedEvent;
}

// Confirmação e cancelamento: interface única, independente de plataforma
interface BlingAdapter {
  parseNfEmitidaWebhook(payload: unknown): NfEvent;     // → CONFIRMADA
  parseNfCanceladaWebhook(payload: unknown): NfEvent;   // → CANCELADA
  getOrderByNf(nfNumero: string): Promise<BlingOrder>;  // para cruzar IDs
}
```

### 7.3 Estratégia de Tracking por Plataforma

O tracking opera em **dois eventos distintos com fontes diferentes**:

| Evento | Fonte | Ação no Confia! |
|---|---|---|
| **Pedido criado** | Webhook do e-commerce (por plataforma) | Comissão → `PENDENTE` |
| **NF emitida** | **Bling** (único para todas as lojas) | Comissão → `CONFIRMADA` |
| **NF cancelada** | **Bling** | Comissão → `CANCELADA` |

| Plataforma | Mecanismo de Tracking | Webhook "pedido criado" |
|---|---|---|
| **Shopify** | UTM params + redirect rastreável | `orders/create` |
| **Wake Commerce** | UTM params + redirect rastreável | Wake Order Webhook |
| **Nuvemshop** | UTM params + redirect rastreável | `orders/created` |
| **Tray** | UTM params + redirect rastreável | Tray Order Webhook |
| **Loja genérica** | UTM params + redirect rastreável | Polling via API (fallback) |

**Janela de atribuição:** 30 dias após o clique. O server-side log é a fonte de verdade; cookie é auxiliar.

**Formato do link rastreável:**
```
https://api.confia.pro/t/{affiliateToken}/{productToken}?ref={quoteId}
```
Quando acessado: (1) registra o clique no banco, (2) acrescenta UTM params à URL da loja, (3) retorna HTTP 302 para a loja.

### 7.4 Fluxo de Orçamento → Compra → Comissão

```
── ATRIBUIÇÃO (fonte: e-commerce) ──────────────────────────────────
1.  Profissional cria orçamento no Confia! PRO
2.  Confia! gera link rastreável por item (redirect server + UTM)
3.  Profissional envia orçamento ao cliente (WhatsApp / PDF)
4.  Cliente acessa portal público do orçamento
5.  Cliente clica em "Comprar" → hit no Tracking Service
6.  Tracking Service: registra {affiliateId, productId, quoteId, ip_hash, ts}
7.  Cliente é redirecionado para a loja e finaliza a compra
8.  Loja dispara webhook "pedido criado" para o Confia!
9.  Tracking Service: cruza pedido com o clique (janela 30 dias)
        → Comissão criada: status PENDENTE
        → Dados gravados: {orderId, orderValue, affiliateId, storeId}

── CONFIRMAÇÃO (fonte: Bling) ───────────────────────────────────────
10. Loja fatura o pedido no Bling (emite NF-e)
11. Bling dispara webhook "notaFiscal.emitida" para o Confia!
12. Confia! chama GET /nfe/{id} → obtém numeroPedidoLoja
13. Cruza numeroPedidoLoja com orderId registrado no passo 9
        → Comissão: PENDENTE → CONFIRMADA
        → Valor confirmado = valor da NF (pode diferir do pedido original)

── CANCELAMENTO (fonte: Bling) ──────────────────────────────────────
14. NF cancelada no Bling → webhook "notaFiscal.cancelada"
        → Comissão: CONFIRMADA → CANCELADA

── PAGAMENTO ────────────────────────────────────────────────────────
15. Profissional solicita saque das comissões CONFIRMADAS
16. Equipe IVA aprova e processa pagamento via PIX (Asaas)
17. Comissão: CONFIRMADA → PAGA
```

### 7.5 Máquina de Estados — Comissões

```
           (clique registrado + webhook order.created)
                              │
                              ▼
                          PENDENTE ──────────────────────► EXPIRADA
                              │                        (30d sem NF)
                 (bling notaFiscal.emitida)
                              │
                              ▼
                 ┌────── CONFIRMADA ──────────┐
                 │                            │
    (bling notaFiscal.cancelada)   (profissional solicita saque)
                 │                            │
                 ▼                            ▼
             CANCELADA                   EM_SAQUE
                                             │
                                (IVA processa PIX via Asaas)
                                             │
                                             ▼
                                           PAGA
```

### 7.6 Sincronização do Catálogo

- Job agendado a cada **6 horas** por loja via BullMQ
- **Cache Redis com TTL de 1 hora** para resultados de busca
- Consulta em tempo real ao adicionar item ao orçamento (valida preço e estoque atual)
- Invalidação antecipada de cache via webhook de alteração de produto (quando disponível na plataforma)

---

## 8. Serviços Backend — Endpoints e Schema

### 8.1 Auth Module

**Tecnologia:** Clerk SDK (`@clerk/nestjs`). O backend valida JWTs emitidos pelo Clerk; a autenticação é hospedada externamente.

```
POST /auth/webhook              → eventos Clerk (user.created, user.updated)
GET  /auth/me                   → perfil do profissional autenticado
PUT  /auth/me/pix               → salva chave PIX (criptografada)
PUT  /auth/me/qualifica-link    → vincula e-mail do Qualifica PRO (MVP manual)
```

**Schema:**
```sql
professionals (
  id            UUID PRIMARY KEY,
  clerk_id      TEXT UNIQUE,
  name          TEXT,
  email         TEXT UNIQUE,
  specialty     TEXT,
  region        TEXT,
  pix_key       TEXT,          -- criptografado (AES-256)
  pix_key_type  TEXT,          -- CPF | EMAIL | PHONE | EVP
  qualifica_verified BOOLEAN DEFAULT FALSE,
  status        ENUM('ACTIVE','SUSPENDED') DEFAULT 'ACTIVE',
  created_at    TIMESTAMPTZ
)
```

**Ponto crítico:** O Qualifica PRO precisa usar a mesma instância do Clerk, ou o Confia! usa vinculação manual por e-mail (profissional informa o e-mail cadastrado no Qualifica PRO; equipe IVA ativa o badge). A solução automática depende de qual plataforma o Qualifica PRO usa hoje — **maior incógnita técnica do projeto**.

---

### 8.2 Catalog Module

**Tecnologia:** NestJS + Redis (cache) + BullMQ (sync agendado via cron).

```
GET /catalog/search?q=tinta&store=wake&category=impermeabilizacao&minPrice=0&maxPrice=500
GET /catalog/products/:id
GET /catalog/stores
```

**Schema:**
```sql
stores (
  id              UUID PRIMARY KEY,
  name            TEXT,
  platform        ENUM('wake','shopify','nuvemshop','tray'),
  api_credentials JSONB,          -- criptografado
  commission_rate DECIMAL(5,2),   -- % base de comissão desta loja
  bling_store_id  TEXT,           -- ID da conta Bling vinculada
  active          BOOLEAN DEFAULT TRUE
)

products (
  id             UUID PRIMARY KEY,
  store_id       UUID REFERENCES stores,
  external_id    TEXT,            -- ID do produto na loja de origem
  name           TEXT,
  price          DECIMAL(10,2),
  stock          INT,
  image_url      TEXT,
  category       TEXT,
  slug           TEXT,
  product_url    TEXT,            -- URL direta na loja
  last_synced_at TIMESTAMPTZ,
  UNIQUE(store_id, external_id)
)
```

---

### 8.3 Quote Module

**Tecnologia:** NestJS + `@react-pdf/renderer` (geração de PDF server-side).

```
POST   /quotes                     → criar orçamento
GET    /quotes                     → listar do profissional autenticado
GET    /quotes/:id                 → detalhe
PUT    /quotes/:id                 → editar
DELETE /quotes/:id
POST   /quotes/:id/publish         → gera public_token, status → ENVIADO
GET    /quotes/public/:token       → portal público (sem auth, SSR via Next.js)
POST   /quotes/:id/approve         → cliente aprova (sem auth, via portal)
POST   /quotes/:id/duplicate
GET    /quotes/:id/pdf             → retorna PDF (stream binary)
```

**Schema:**
```sql
quotes (
  id              UUID PRIMARY KEY,
  professional_id UUID REFERENCES professionals,
  client_name     TEXT,
  client_phone    TEXT,
  title           TEXT,
  status          ENUM('RASCUNHO','ENVIADO','APROVADO','EXPIRADO') DEFAULT 'RASCUNHO',
  public_token    TEXT UNIQUE,
  expires_at      TIMESTAMPTZ,
  margin_percent  DECIMAL(5,2),   -- margem global do profissional
  created_at      TIMESTAMPTZ
)

quote_items (
  id              UUID PRIMARY KEY,
  quote_id        UUID REFERENCES quotes,
  product_id      UUID REFERENCES products,  -- NULL para itens de serviço
  label           TEXT,           -- nome copiado do produto ou livre
  quantity        DECIMAL(10,3),
  unit            TEXT,           -- 'un', 'kg', 'm²', 'L', 'saco'
  unit_price      DECIMAL(10,2),  -- preço snapshot no momento da adição
  margin_override DECIMAL(5,2),   -- margem específica deste item (sobrescreve global)
  is_service      BOOLEAN DEFAULT FALSE,
  sort_order      INT
)
```

---

### 8.4 Tracking Module

**Tecnologia:** NestJS + PostgreSQL + Redis (sessão de clique).

```
GET  /t/:affiliateToken/:productToken  → redirect rastreável (público, sem auth)
POST /webhooks/ecommerce/:storeId      → pedidos criados nas lojas
POST /webhooks/bling/:storeId          → eventos de NF do Bling
```

**Schema:**
```sql
affiliate_clicks (
  id              UUID PRIMARY KEY,
  professional_id UUID REFERENCES professionals,
  product_id      UUID REFERENCES products,
  quote_id        UUID REFERENCES quotes,
  ip_hash         TEXT,           -- SHA-256 do IP (LGPD: nunca IP bruto)
  user_agent_hash TEXT,
  clicked_at      TIMESTAMPTZ
)

orders (
  id                UUID PRIMARY KEY,
  store_id          UUID REFERENCES stores,
  external_order_id TEXT,         -- ID do pedido na loja (chave para cruzar com Bling)
  total_value       DECIMAL(10,2),
  status            ENUM('CREATED','INVOICED','CANCELLED') DEFAULT 'CREATED',
  raw_payload       JSONB,        -- payload original do webhook (auditoria)
  received_at       TIMESTAMPTZ,
  UNIQUE(store_id, external_order_id)
)
```

**Lógica de atribuição (webhook "pedido criado"):**
```
1. Parsear payload com adapter da plataforma → {external_order_id, items[], total}
2. Para cada item:
   a. Buscar affiliate_clicks onde product_id = item.productId
      AND clicked_at > NOW() - INTERVAL '30 days'
      ORDER BY clicked_at DESC LIMIT 1
   b. Se encontrado: INSERT INTO commissions (status=PENDENTE)
3. INSERT INTO orders (status=CREATED)
```

**Lógica de confirmação (webhook Bling `notaFiscal.emitida`):**
```
1. Parsear payload → {nfId}
2. GET /Api/v3/nfe/{nfId} → {pedido.numeroPedidoLoja}
3. SELECT * FROM orders WHERE external_order_id = numeroPedidoLoja AND store_id = :storeId
4. UPDATE commissions SET status='CONFIRMADA', bling_nf_id=nfId, confirmed_at=NOW()
   WHERE order_id = :orderId AND status = 'PENDENTE'
```

---

### 8.5 Commission Module

**Tecnologia:** NestJS + Asaas SDK para processar transferências PIX.

```
GET  /commissions                       → comissões do profissional autenticado
GET  /commissions/summary               → totais por status (para painel)
POST /payouts/request                   → solicitar saque
GET  /payouts                           → histórico de saques

-- Admin
GET  /admin/payouts/pending
POST /admin/payouts/:id/approve         → dispara transferência PIX via Asaas
POST /admin/payouts/:id/reject
POST /webhooks/asaas                    → recebe confirmação de transferência
```

**Schema:**
```sql
commissions (
  id              UUID PRIMARY KEY,
  professional_id UUID REFERENCES professionals,
  order_id        UUID REFERENCES orders,
  click_id        UUID REFERENCES affiliate_clicks,
  gross_value     DECIMAL(10,2),   -- valor da venda rastreada
  commission_rate DECIMAL(5,2),    -- % aplicado
  net_value       DECIMAL(10,2),   -- valor a receber
  status          ENUM('PENDENTE','CONFIRMADA','CANCELADA','EM_SAQUE','PAGA'),
  bling_nf_id     TEXT,
  confirmed_at    TIMESTAMPTZ,
  payout_id       UUID REFERENCES payouts
)

payouts (
  id                UUID PRIMARY KEY,
  professional_id   UUID REFERENCES professionals,
  amount            DECIMAL(10,2),
  pix_key           TEXT,
  status            ENUM('SOLICITADO','APROVADO','PROCESSANDO','PAGO','REJEITADO'),
  asaas_transfer_id TEXT,           -- ID da transferência na Asaas
  requested_at      TIMESTAMPTZ,
  processed_at      TIMESTAMPTZ
)
```

---

## 9. Integração com Bling (ERP)

### 9.1 Por que o Bling é a fonte de verdade para comissões

O Bling será o ERP de todas as lojas parceiras. A emissão da NF-e no Bling é o único evento que garante que a venda **realmente aconteceu e foi faturada** — sem devolução, sem cancelamento por inadimplência, sem teste. É a barreira definitiva contra pagamento de comissões indevidas.

### 9.2 Webhooks do Bling utilizados

| Evento Bling | Trigger | Ação no Confia! |
|---|---|---|
| `notaFiscal.incluida` | NF criada (ainda não emitida) | Opcional: sinalizar "em faturamento" |
| `notaFiscal.emitida` | **NF autorizada pela SEFAZ** | Comissão: PENDENTE → **CONFIRMADA** |
| `notaFiscal.cancelada` | NF cancelada | Comissão: CONFIRMADA → **CANCELADA** |

> Usar `notaFiscal.emitida` (não `incluida`) garante que a SEFAZ autorizou a nota — sem risco de comissionar uma NF rejeitada.

### 9.3 Cruzamento de IDs (Bling ↔ E-commerce ↔ Confia!)

```
E-commerce Order ID  →  Bling "numeroPedidoLoja"  →  Confia! orderId
```

Fluxo:
1. Webhook `notaFiscal.emitida` chega: `{ "evento": "notaFiscal.emitida", "data": { "id": 98765 } }`
2. `GET /Api/v3/nfe/98765` → `{ "pedido": { "numeroPedidoLoja": "ORD-2891" } }`
3. `SELECT * FROM orders WHERE external_order_id = 'ORD-2891'`
4. Encontrado: comissão atualizada para CONFIRMADA

**Risco crítico:** Se a integração loja→Bling não preencher `numeroPedidoLoja`, o cruzamento falha. Verificar antes do desenvolvimento com um pedido de teste em cada plataforma.

### 9.4 Bling API v3 — Referência

| Endpoint | Uso |
|---|---|
| `GET /Api/v3/nfe/{id}` | Detalhe da NF (inclui `numeroPedidoLoja`) |
| `GET /Api/v3/pedidos/{id}` | Detalhe do pedido no Bling |
| `POST /Api/v3/webhooks` | Registrar URL de webhook |
| `GET /Api/v3/webhooks` | Listar webhooks ativos |

**Autenticação:** OAuth 2.0 (Authorization Code Flow). **Uma credencial Bling por loja parceira.**

**Rate limit:** 3 req/s por conta. O Confia! deve implementar fila com backoff para consultas Bling.

### 9.5 Modelo de Credenciais por Loja

Cada loja autoriza o Confia! como app OAuth no Bling. O Confia! armazena `access_token` + `refresh_token` por loja, com renovação automática antes da expiração.

```
Loja A (Escuta o Véio!) → Bling Account A → credentials_store_A
Loja B (Fácil Decor)    → Bling Account B → credentials_store_B
Loja C (parceiro ext.)  → Bling Account C → credentials_store_C
```

---

## 10. Integrações de E-commerce

### 10.1 Wake Commerce

| Item | Detalhe |
|---|---|
| **Autenticação** | API Key no header `Authorization: Bearer {key}` |
| **Catálogo** | `GET /catalog/product?page=1&pageSize=50` — suporta busca full-text |
| **Estoque** | Campo `stock` no objeto produto; variantes têm estoque individual |
| **Webhook pedido** | Configurado via painel Wake → Integrações → Webhooks. Evento `order.created` |
| **Rate limit** | ~300 req/min (confirmar com Wake) |
| **Documentação** | developers.wake.tech |
| **Dificuldade** | **Baixa** — API bem documentada, REST padrão |

---

### 10.2 Nuvemshop (Tiendanube)

| Item | Detalhe |
|---|---|
| **Autenticação** | OAuth 2.0 — loja autoriza o app Confia! pelo painel Nuvemshop |
| **Catálogo** | `GET /v1/{store_id}/products?per_page=200` — paginação via Link header |
| **Estoque** | Campo `stock` por variante em `variants[]` |
| **Webhook pedido** | `POST /v1/{store_id}/webhooks` com `event: orders/created` |
| **Rate limit** | 40 req/min por loja no plano padrão |
| **SDK oficial** | `@tiendanube/node-sdk` disponível |
| **Documentação** | tiendanube.github.io/api-docs |
| **Dificuldade** | **Baixa** — documentação clara e completa |

---

### 10.3 Shopify

| Item | Detalhe |
|---|---|
| **Autenticação** | OAuth 2.0 por loja — requer app criado no Shopify Partners |
| **Catálogo** | `GET /admin/api/2024-04/products.json` (REST) ou GraphQL `products` query |
| **Estoque** | `inventory_quantity` por variant e location |
| **Webhook pedido** | `POST /admin/api/2024-04/webhooks.json` — topic `orders/create` |
| **Rate limit** | 2 req/s REST; GraphQL tem budget de pontos (250/s) |
| **Dificuldade** | **Média-Alta** — requer criação de app Shopify Partners; para lojas externas exige review |

**Ponto de atenção:** Para lojas **próprias** (se Escuta o Véio! ou Fácil Decor usarem Shopify), integração é direta como custom app. Para lojas **de terceiros**, o Confia! precisa ser um app listado no App Store Shopify ou instalado manualmente pelo dono da loja — processo leva semanas.

---

### 10.4 Tray Commerce

| Item | Detalhe |
|---|---|
| **Autenticação** | `GET /web_api/auth?consumer_key={key}&consumer_secret={secret}` → `access_token` |
| **Catálogo** | `GET /web_api/products?access_token={token}` |
| **Estoque** | Campo `stock` no produto |
| **Webhook pedido** | Via painel Tray → Notificações. Menos configurável por API |
| **Documentação** | docs.tray.com.br — menos completa; alguns endpoints sem documentação |
| **Dificuldade** | **Média** — autenticação não-padrão; webhooks menos robustos que concorrentes |

**Fallback para Tray:** Polling a cada 4h consultando pedidos por status, como segurança em caso de webhooks não entregues.

---

### 10.5 Modelo de Comissão por Plataforma

| Modelo | Como funciona | Prós | Contras |
|---|---|---|---|
| **A — IVA como intermediária** | IVA recebe comissão da loja e repassa ao profissional | Controle total; funciona em qualquer plataforma | IVA precisa ter contrato com cada loja |
| **B — Direto na plataforma** | Profissional cadastrado como afiliado direto na loja | Mais simples operacionalmente | Depende de programa nativo de afiliados |
| **C — Híbrido** | Modelo A para lojas IVA + Modelo B para terceiros | Melhor dos dois mundos | Mais complexo de implementar |

> **Recomendação:** Modelo A para o MVP. Garante controle total e consistência da experiência, independente da plataforma da loja parceira.

---

## 11. Frontend — Rotas e Telas

### 11.1 Web (Next.js App Router)

```
app/
  (auth)/
    login/page.tsx               → tela de login (Clerk hosted UI)
    cadastro/page.tsx            → registro + vínculo ao Qualifica PRO

  (dashboard)/
    page.tsx                     → home: resumo de comissões + últimos orçamentos
    catalogo/
      page.tsx                   → busca de produtos (filtros: loja, categoria, preço)
      [productId]/page.tsx       → detalhe do produto
    orcamentos/
      page.tsx                   → lista de orçamentos (filtro por status)
      novo/page.tsx              → criador de orçamento (step-by-step)
      [id]/page.tsx              → edição de orçamento
      [id]/preview/page.tsx      → visualização antes de enviar
    comissoes/
      page.tsx                   → painel de comissões + solicitação de saque
    perfil/page.tsx              → dados do profissional + chave PIX

  (admin)/
    lojas/page.tsx               → gestão de lojas parceiras
    profissionais/page.tsx       → gestão de afiliados
    saques/page.tsx              → aprovação de saques pendentes
    relatorios/page.tsx          → dashboard GMV e comissões

  p/[token]/page.tsx             → PORTAL PÚBLICO DO ORÇAMENTO
                                    SSR, sem autenticação
                                    Botões de compra → redirect rastreável
```

### 11.2 Mobile (React Native + Expo Router)

Estrutura espelha a web. Diferenciais:

- **Bottom tab navigation:** Dashboard / Catálogo / Orçamentos / Comissões
- **Share Sheet nativo** para WhatsApp (sem necessidade de API)
- **MMKV storage** para orçamentos em modo offline (leitura)
- **Expo Notifications** para push: "orçamento aprovado", "comissão confirmada"
- **Camera** (Fase 3): foto da obra para anexar ao orçamento

### 11.3 Portal Público (`/p/[token]`)

Página SSR renderizada para o cliente final. Sem login. Exibe:
- Nome, foto e certificações do profissional
- Itens do orçamento com fotos, quantidades e preços
- Prazo de validade
- Botão "Comprar" por item → tracking server → loja
- Botão "Aprovar orçamento" → notificação ao profissional

---

## 12. Pagamento de Comissões — Asaas

| Item | Detalhe |
|---|---|
| **Produto** | Asaas Transferências — PIX para CPF/CNPJ/chave |
| **Endpoint** | `POST /api/v3/transfers` com `{ value, pixAddressKey, pixAddressKeyType }` |
| **Autenticação** | API Key no header `access_token` |
| **Sandbox** | Disponível em sandbox.asaas.com |
| **Custo por transferência** | ~R$ 0,90–2,00 (verificar tabela atual) |
| **Webhook de confirmação** | `transfer.concluded` → comissão status: PAGA |

**Fluxo completo de saque:**
```
1. Profissional solicita saque → registro em payouts (SOLICITADO)
2. Admin IVA vê painel de saques pendentes
3. Admin aprova → POST /api/v3/transfers na Asaas
4. Asaas retorna asaas_transfer_id → salvo no payout
5. Webhook "transfer.concluded" → payout: PAGO + comissões: PAGAS
```

---

## 13. Envio por WhatsApp e PDF

### WhatsApp

**MVP — Compartilhamento nativo (sem custo, sem API):**
```
Web:    <a href="https://wa.me/?text=Seu orçamento: {link}">Enviar</a>
Mobile: Share Sheet nativo do iOS/Android
```

**Fase 2+ — Envio automatizado (opcional):**
- Z-API (R$ 79/mês) ou Evolution API (open-source, custo de servidor)
- Caso de uso: envio direto do backend sem o profissional abrir o WhatsApp
- Requer número WhatsApp Business ativo

### Geração de PDF

| Opção | Tecnologia | Prós | Contras |
|---|---|---|---|
| **A (recomendado MVP)** | `@react-pdf/renderer` | Zero custo, roda no NestJS | Estilo mais limitado |
| **B (Fase 2)** | Puppeteer via Browserless.io | HTML pixel-perfect | ~US$ 9/mês; 2–5s por PDF |

---

## 14. Stack Tecnológica Completa

### Frontend — Web

| Tecnologia | Versão | Justificativa |
|---|---|---|
| **Next.js** | 14+ | SSR para portal do cliente (SEO), App Router, caching nativo |
| **Tailwind CSS** | 3.x | Produtividade de UI, consistência visual |
| **Shadcn/ui** | latest | Componentes acessíveis e customizáveis |
| **Zustand** | 4.x | State do orçamento em construção (client-side) |
| **React Query** | 5.x | Cache e sync de dados do servidor |

### Mobile

| Tecnologia | Versão | Justificativa |
|---|---|---|
| **React Native + Expo** | SDK 51+ | Codebase único iOS/Android; compartilha lógica com web |
| **Expo Router** | 3.x | Navegação baseada em arquivos |
| **MMKV** | 2.x | Storage local rápido para modo offline |
| **Expo Notifications** | — | Push notifications multiplataforma |

### Backend

| Tecnologia | Versão | Justificativa |
|---|---|---|
| **Node.js** | 20 LTS | Estável, amplo ecossistema |
| **NestJS** | 10.x | TypeScript nativo, DI para adapters, módulos isolados |
| **PostgreSQL** | 16 | Modelo relacional para dados de negócio |
| **Redis** | 7.x | Cache de catálogo, rate limiting |
| **BullMQ** | 5.x | Filas para sync de catálogo e jobs assíncronos |
| **Prisma** | 5.x | ORM type-safe, migrações automáticas |

### Autenticação

| Tecnologia | Justificativa |
|---|---|
| **Clerk** *(recomendado)* | SSO, webhooks de usuário, SDK React/Next nativo, free tier generoso |
| **Auth0** *(alternativa)* | Mais robusto para enterprise, custo maior |
| **Keycloak** *(self-hosted)* | Controle total; considerar se escalar para > 50k usuários |

### Infraestrutura e Deploy

| Serviço | Plataforma | Config MVP | Custo Estimado |
|---|---|---|---|
| Frontend Web | **Vercel** | Deploy automático via git | R$ 0–150/mês |
| Backend API | **Railway** | NestJS em container Docker | R$ 150–600/mês |
| Workers BullMQ | **Railway** | Processo separado do API | incluso |
| Banco de dados | **Supabase** | PostgreSQL gerenciado, plano Pro | R$ 125/mês (US$ 25) |
| Cache / Filas | **Upstash** | Redis serverless pay-as-you-go | R$ 0–100/mês |
| Arquivos (PDFs) | **Cloudflare R2** | Object storage S3-compatible | R$ 0–50/mês |
| CDN + Domínio | **Cloudflare** | app.confia.pro / api.confia.pro | R$ 50–100/mês |

**Custo total de infraestrutura (MVP):** R$ 325–1.125/mês

### Serviços de Terceiros

| Serviço | Uso | Custo |
|---|---|---|
| **Clerk** | Autenticação e SSO | Grátis até 10k MAU |
| **Resend** | E-mails transacionais | Grátis até 3k/mês |
| **Asaas** | PIX em massa para profissionais | ~R$ 1,50/transferência |
| **Bling API v3** | ERP — fonte de verdade das comissões | Sem custo adicional (conta já ativa) |
| **Browserless** *(Fase 2)* | Geração de PDF fiel | ~R$ 45/mês |
| **Z-API** *(Fase 2+)* | WhatsApp automatizado | R$ 79/mês/instância |

---

## 15. Pontos de Viabilidade — Validação Obrigatória

Ordenados por criticidade. Os três primeiros precisam ser validados **antes de iniciar o desenvolvimento**.

| # | Ponto | Como validar | Risco se inviável |
|---|---|---|---|
| 1 | **`numeroPedidoLoja` no Bling** | Fazer pedido de teste em cada loja; verificar no Bling se o campo foi preenchido com o order ID da loja | Alto — cruzamento NF↔pedido falha; exige fallback por valor+data (menos confiável) |
| 2 | **Wake dispara webhook `order.created` para URL externa** | Configurar URL de teste no painel Wake e fazer pedido; verificar se o payload chega | Alto para MVP — sem isso a atribuição de comissão é impossível |
| 3 | **Modelo de comissão acordado com as lojas** | Reunião com times de Escuta o Véio! e Fácil Decor para formalizar % e modelo (IVA como intermediária) | Alto — sem acordo o modelo de negócio não fecha |
| 4 | **SSO com Qualifica PRO** | Identificar qual plataforma o Qualifica PRO usa (Hotmart, Kiwify, própria?) | Médio — MVP funciona com vínculo manual; SSO automático fica para Fase 2 |
| 5 | **App Shopify Partners** | Acessar partners.shopify.com e criar app de desenvolvimento | Médio — só impacta lojas Shopify; Wake e Nuvemshop não dependem disso |
| 6 | **Conta Asaas verificada (KYC)** | Iniciar processo de verificação de conta PJ na Asaas | Baixo — processo rápido, mas pode atrasar 1–2 semanas se deixado para o fim |

---

## 16. Fases de Desenvolvimento

### Fase 0 — Fundação (Semanas 1–4)

**Objetivo:** Validar as premissas críticas e preparar a base técnica.

- [ ] Teste de integração Wake→Bling: verificar `numeroPedidoLoja`
- [ ] Teste de webhook Wake: confirmar `order.created` para URL externa
- [ ] Definição do modelo de comissão com as lojas (reunião)
- [ ] Identificar plataforma do Qualifica PRO e estratégia de SSO
- [ ] Design do schema completo de banco de dados
- [ ] Setup do monorepo (Turborepo: web + mobile + backend)
- [ ] Configuração do Clerk e fluxo de auth
- [ ] Wireframes de baixa fidelidade (orçamento + portal cliente)

**Equipe:** 1 Tech Lead + 1 Designer  
**Entregável:** ADRs validados + protótipo navegável + premissas confirmadas

### Fase 1 — MVP Funcional (Semanas 5–14)

**Objetivo:** Plataforma web com uma loja integrada (Escuta o Véio!).

- [ ] Wake Adapter completo (catálogo + webhook)
- [ ] Catálogo com busca e filtros (1 loja)
- [ ] Orçamentador completo (criar, editar, publicar)
- [ ] Portal público do orçamento (`/p/[token]`)
- [ ] Redirect rastreável + registro de clique
- [ ] Webhook de pedido Wake + atribuição de comissão (PENDENTE)
- [ ] Integração Bling: webhooks NF emitida/cancelada (CONFIRMADA/CANCELADA)
- [ ] Painel de comissões do profissional
- [ ] Geração de PDF (`@react-pdf/renderer`)
- [ ] Envio por WhatsApp (link nativo)
- [ ] Painel admin básico (lojas, profissionais, saques)
- [ ] Integração Asaas para pagamento de saques

**Equipe:** 1 Tech Lead (backend) + 1 Frontend Dev + 1 Designer  
**Entregável:** Versão web em produção; beta com 20–50 profissionais piloto

### Fase 2 — Expansão de Plataformas (Semanas 15–22)

**Objetivo:** Multi-loja e primeiro app mobile.

- [ ] Nuvemshop Adapter
- [ ] Shopify Adapter
- [ ] Tray Adapter (com fallback de polling)
- [ ] Catálogo multi-loja com filtro por loja
- [ ] App React Native (iOS + Android) — paridade com web
- [ ] Notificações push (comissão confirmada, orçamento aprovado)
- [ ] Painel de reconciliação (comissões PENDENTES sem NF há > 7 dias)
- [ ] PDF via Browserless (alta fidelidade)

**Equipe:** +1 Mobile Dev  
**Entregável:** App nas lojas + 3 novas plataformas integradas

### Fase 3 — Crescimento (Semanas 23–30)

**Objetivo:** Ferramentas avançadas de retenção e ticket.

- [ ] Calculadora de material por m² integrada ao orçamento
- [ ] Histórico de orçamentos agrupado por obra/projeto
- [ ] Portal do cliente com assinatura digital do orçamento
- [ ] White-label: logo do profissional customizável no PDF/portal
- [ ] Ranking de profissionais por GMV gerado
- [ ] Badge automatizado para certificados do Qualifica PRO
- [ ] Envio automatizado por WhatsApp Business (Z-API)

---

## 17. Estimativa de Recursos

### 17.1 Equipe Necessária

| Papel | Fase | Dedicação | Custo Estimado (PJ) |
|---|---|---|---|
| Tech Lead / Backend Senior | 0–3 | 160h/mês | R$ 8.000–14.000/mês |
| Frontend Developer (Next.js) | 1–3 | 160h/mês | R$ 5.000–9.000/mês |
| Mobile Developer (React Native) | 2–3 | 160h/mês | R$ 6.000–10.000/mês |
| UX Designer | 0–2 | 80h/mês (part-time) | R$ 3.000–5.000/mês |
| Product Manager | 0–3 | 40h/mês (interno) | — |

### 17.2 Estimativa por Fase

| Fase | Duração | Custo de Equipe | Infra + Serviços | Total |
|---|---|---|---|---|
| Fase 0 | 4 semanas | R$ 14.000 | R$ 500 | ~R$ 15.000 |
| Fase 1 | 10 semanas | R$ 55.000 | R$ 2.000 | ~R$ 57.000 |
| Fase 2 | 8 semanas | R$ 70.000 | R$ 3.000 | ~R$ 73.000 |
| Fase 3 | 8 semanas | R$ 80.000 | R$ 4.000 | ~R$ 84.000 |
| **Total** | **~30 semanas** | **~R$ 219.000** | **~R$ 9.500** | **~R$ 229.000** |

### 17.3 Custo de Infraestrutura Recorrente

| Cenário | Usuários Ativos | Custo/mês |
|---|---|---|
| Lançamento (beta) | < 500 | R$ 325–600 |
| Crescimento | 500–5.000 | R$ 600–1.500 |
| Escala | 5.000–50.000 | R$ 1.500–5.000 |

---

## 18. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| **`numeroPedidoLoja` ausente no Bling** | Média | Alto | Validar na Fase 0 com pedido de teste; fallback por valor+data+cliente |
| **Webhook Bling não entregue** | Média | Alto | Reconciliação diária via `GET /nfe?dataEmissao={hoje-7d}`; painel de comissões órfãs |
| **Wake não suporta webhook para URL externa** | Baixa | Alto | Polling a cada 4h como fallback imediato |
| **APIs de plataformas mudam** | Média | Médio | Adapter pattern isola a mudança; testes de integração automatizados com alertas |
| **Loja parceira sem acordo de comissão** | Baixa | Alto | Modelo A (IVA intermediária) não depende de programa nativo da loja |
| **Fraude de cliques** | Média | Médio | Máximo 1 comissão por IP+device em 24h; revisão manual de saques > R$ 500 |
| **Qualifica PRO sem SSO viável** | Alta | Médio | MVP usa vínculo por e-mail com ativação manual do badge; SSO em Fase 2 |
| **LGPD — dados de clientes** | Baixa | Alto | IPs armazenados apenas como hash SHA-256; portal do cliente sem coleta de PII |
| **KYC Asaas atrasado** | Baixa | Médio | Iniciar processo no início da Fase 0; não bloqueia desenvolvimento |

---

## 19. Métricas de Sucesso

### KPIs de Produto (6 meses pós-lançamento)

| Métrica | Meta |
|---|---|
| Profissionais cadastrados | 500 |
| Orçamentos criados/mês | 1.000 |
| Taxa de conversão orçamento → compra | > 15% |
| GMV gerado (vendas rastreadas) | R$ 200.000/mês |
| Comissões pagas | R$ 10.000/mês |

### KPIs de Retenção

| Métrica | Meta |
|---|---|
| DAU/MAU ratio | > 30% |
| Profissionais com ≥ 3 orçamentos/mês | > 40% da base ativa |
| NPS do profissional | > 60 |

---

## 20. Próximos Passos

1. **Validar os 3 pontos críticos de viabilidade** (seção 15, itens 1–3) antes de qualquer desenvolvimento
2. **Workshop técnico** (2–4h): mapear plataforma atual do Qualifica PRO e definir estratégia de SSO
3. **Criar conta Asaas** e iniciar KYC com o CNPJ da IVA Química
4. **Criar app no Shopify Partners** para ter credenciais de desenvolvimento prontas
5. **Contratar/alocar Tech Lead** para conduzir Fase 0
6. **Definir profissionais piloto** (20–50 alunos Qualifica PRO) para beta da Fase 1

---

*Documento vivo — atualizar após cada decisão de arquitetura validada.*
