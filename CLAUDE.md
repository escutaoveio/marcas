# IVA Química — Inteligência Operacional

## A Empresa
IVA Química é uma indústria química brasileira focada em inovação para construção civil, decoração, marcenaria, limpeza e artesanato. Catálogo com mais de 1.200 produtos ativos. **Independente de ponta a ponta:** fabrica, distribui e vende diretamente ao cliente final.

**Documentação completa do ecossistema:** `docs/ecossistema-iva-quimica.md`

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

### Unidades de Negócio
- **Escuta o Véio!** *(ativo)* — e-commerce principal, catálogo completo + terceiros. *"Novas Soluções para Velhos Problemas"*
- **Fácil Decor** *(ativo/em desenvolvimento)* — loja física + e-commerce + franquia OMS, catálogo LT Shine. *"A Etiqueta da Sua Casa"*
- **ConstruLivre** *(pausado)* · **ObraMil** *(pausado)*

---

## Estrutura do Repositório

```
marcas/                        → identidade, voz e ativos por marca
  drylevis/ (elastment/ smart/)
  hold-stone/ · lt-shine/ · cristal/

marketing/                     → campanhas, briefings, calendário editorial
redes-sociais/                 → conteúdo por plataforma (instagram/ tiktok/ youtube/ linkedin/ whatsapp-broadcast/)
vendas/                        → por público (cliente-final/ profissional/ b2b/)
crm/                           → segmentos/ reguas/ templates/
  segmentos/ (cliente-final/ profissional/ b2b/)

unidades-de-negocio/
  escuta-o-veio/ (loja-virtual/ marketplaces/ time-de-vendas/)
  facil-decor/   (loja-fisica/ loja-virtual/ marketplaces/ time-de-vendas/ franquia/)

qualifica-pro/                 → cursos/ eventos/
confia/                        → programa/ materiais/

docs/
  ecossistema-iva-quimica.md
  reports/
  inteligencia-de-mercado/ (concorrentes/ tendencias/ pesquisas/)

playbooks/                     → SOPs cross-funcionais
```

---

## Interconexões Chave

```
marcas/[marca]/identidade/   → alimenta → marketing/ e redes-sociais/
redes-sociais/               → gera leads → crm/segmentos/
qualifica-pro/               → forma profissionais → crm/segmentos/profissional/
confia/                      → afiliados → crm/segmentos/profissional/
unidades-de-negocio/         → dados de venda → crm/ e docs/reports/
vendas/[público]/            → espelha → crm/segmentos/[público]/
```

---

## Comandos Disponíveis

| Comando | Especialidade |
|---|---|
| `/marketing` | Campanhas e estratégia de marketing por marca |
| `/social` | Conteúdo para redes sociais por plataforma e marca |
| `/marca` | Posicionamento, narrativa e identidade de marca |
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
- Dados sensíveis de clientes nunca vão para o repositório
