# IVA Química — Inteligência Operacional

## A Empresa
IVA Química é uma indústria química brasileira focada em inovação para construção civil, decoração, marcenaria, limpeza e artesanato. Catálogo com mais de 1.200 produtos ativos. **Independente de ponta a ponta:** fabrica, distribui e vende diretamente ao cliente final.

**Documentação completa do ecossistema:** `arquivos/ecossistema-iva-quimica.md`

---

## Princípios Estratégicos

- **Transformação viraliza. Produto não.** Conteúdo sempre parte do resultado — o que muda na vida de quem usa.
- **O produto é um meio, não um fim.** O que se vende é a transformação.
- **Pull, não push.** A estratégia começa no cliente final e sobe — nunca parte do distribuidor para baixo.
- **Independência vertical.** A IVA fabrica, distribui e vende direto via canais próprios.

---

## Os Três Públicos (em ordem de prioridade)

1. **Cliente Final** — deseja a transformação
2. **Profissional** (pintor, marceneiro, decorador, engenheiro) — executa e recomenda
3. **B2B** (lojistas, homecenters) — ativado por demanda dos dois acima

---

## Ecossistema

### Marcas
| Marca | Posicionamento | Público |
|---|---|---|
| **Drylevis** | Alta performance, construção tecnológica | Engenheiro, mestre de obra |
| **Elastment** *by Drylevis* | Impermeabilização referência | Profissional de obra |
| **Smart** *by Drylevis* | Qualidade, praticidade, premium | Arquiteto, acabamento |
| **Hold Stone** | Paisagismo, pioneer no fixador de pedras | Consumidor final, designer |
| **LT Shine** | Acabamento, sofisticação, elegância | Consumidor final, arquiteto |
| **Cristal** | Marca de entrada, alto giro, PDV | Pintor, aplicador |

### Produtos e Plataformas
- **Qualifica PRO** — qualificação profissional (cursos + eventos). *"Quem Faz Aprende, Quem Aprende Cresce!"*
- **Confia!** — programa de afiliados para profissionais e qualquer pessoa

### Canais de Venda
- **Escuta o Véio!** *(ativo)* — e-commerce principal, catálogo completo + terceiros. *"Novas Soluções para Velhos Problemas"*
- **Fácil Decor** *(ativo/em desenvolvimento)* — loja física + e-commerce + franquia OMS, catálogo LT Shine. *"A Etiqueta da Sua Casa"*
- **ConstruLivre** *(pausado)* · **ObraMil** *(pausado)*

---

## Estrutura do Repositório

```
index.md                       → ponto de entrada do repositório (comece aqui)

marketing/                     → estratégia e execução de marketing
  marcas/ (drylevis/ elastment/ smart/ hold-stone/ lt-shine/ cristal/)
  campanhas/

canais-de-vendas/              → operação dos canais de venda diretos
  escuta-o-veio/ (identidade/ loja-virtual/ marketplaces/)
  facil-decor/   (identidade/ loja-fisica/ loja-virtual/ marketplaces/ franquia/)
  atendimento-comercial/

base-de-dados/                 → dados operacionais vivos
  planilhas/ (vendas/ clientes/ produtos/ marketing/)
  dashboards/                  → HTML público via GitHub Pages
  relatorios/                  → consolidações prontas para envio (HTML/PDF)

arquivos/                      → documentação, conhecimento e relatórios
  iva-quimica.md · iva-quimica.html
  ecossistema-iva-quimica.md · ecossistema-visual.html
  catalogo/ · personas/ · mercado/ (concorrentes/ tendencias/ pesquisas/)
  reports/

.claude/
  commands/                    → slash commands (/marketing, /ecommerce, /report…)
  workflows/                   → contextos de trabalho (lidos com "Retome o contexto de X")
  agents/                      → definições de agentes
  skills/                      → skills adicionais
  templates/                   → templates HTML de produto (T1, T2, T3, T4, T5)
```

---

## Interconexões Chave

```
Notion (Catálogo de Produtos)   → alimenta → marketing/marcas/{marca}/{linha}/*.html
arquivos/                       → alimenta → todos os briefings e campanhas
marketing/marcas/               → define posicionamento → marketing/campanhas/ e anúncios pagos
canais-de-vendas/               → dados de venda → arquivos/reports/
```

---

## Processos de Trabalho

### Descrição HTML de Produto

Fluxo padrão para gerar a descrição de produto para e-commerce:

1. **Fonte:** Notion — Catálogo de Produtos (`notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`)
2. **Template:** `.claude/templates/product-description-template.html` (T1 padrão)
3. **Saída:** `marketing/marcas/{marca-slug}/{linha-slug}/{produto-slug}.html`
4. **Workflow completo:** `.claude/workflows/workflow-descricao-html.md`
5. **Agente executor:** `.claude/agents/agente-html-description.md`

Decisão de template:

| Condição | Template |
|---|---|
| Produto padrão | T1 — `product-description-template.html` |
| Produto com banner dedicado | T2 — `product-description-banner-template.html` |
| Reformulação de rótulo/embalagem | T3 — `packaging-change-adendo.html` (inserido no T1 ou T2) |
| Produto com rendimento mensurável | T4 — `product-calculator-template.html` (arquivo separado `calculator.html`) |
| Kit / combo | T5 — `kits-description-template.html` |

---

## Comandos Disponíveis

| Comando | Especialidade |
|---|---|
| `/marketing` | Campanhas e estratégia de marketing por marca |
| `/social` | Conteúdo para redes sociais por plataforma e marca |
| `/marca` | Posicionamento, narrativa e identidade de marca |
| `/vendas` | Relatório semanal de vendas por produto + plano de ação |
| `/sales` | Vendas por público (cliente final, profissional, B2B) |
| `/crm` | Segmentação, réguas e relacionamento com clientes |
| `/ecommerce` | Operações de Escuta o Véio! e Fácil Decor |
| `/qualifica` | Cursos e eventos do Qualifica PRO |
| `/confia` | Programa de afiliados Confia! |
| `/intel` | Inteligência de mercado, concorrentes, tendências |
| `/report` | Relatório executivo consolidado de todas as frentes |

---

## Convenções
- Documentos em português (pt-BR)
- Nomes de arquivo em `kebab-case`
- Datas no formato `YYYY-MM-DD`
- Templates prefixados com `_template-` para se destacar de documentos reais
- Dados sensíveis de clientes nunca vão para o repositório
- Ponto de entrada: `index.md`
