# Workflow: Otimizador de Produtos

> **Agente responsável:** `agente-otimizador-produto.md` (nesta mesma pasta)
> **Última revisão:** 2026-06-08

---

## Visão Geral

Este workflow enriquece páginas de produto no Catálogo de Produtos do Notion, preenchendo dados comerciais, SEO, classificação e perfil de compra. O repositório hospeda a infraestrutura operacional (agente, template de referência, este workflow); o conteúdo gerado vive inteiramente no Notion.

O ponto de partida é um produto (ou kit) identificado pelo usuário. O agente lê o Notion, gera o checklist no chat para aprovação, e somente após aprovação explícita escreve de volta no Notion.

**O agente nunca escreve no Notion sem aprovação explícita do usuário.**

---

## Quando Usar

- Produto novo adicionado ao catálogo e ainda sem dados comerciais preenchidos
- Produto existente com campos incompletos (sem SEO, sem benefícios-chave, sem FAQ)
- Kit de produtos novo ou reformulado
- Revisão periódica do catálogo para melhoria de conversão

---

## Fonte de Dados

**Fonte primária:** Notion — Catálogo de Produtos
`notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`

**Bases de apoio (no mesmo Notion):**

| Base | Para que serve |
|---|---|
| Lista de Kits de Produtos | Seção 5.1 — kits existentes e sugestões de novos |
| Todos os Departamentos | Seção 5.2 — próximo departamento no ciclo de obra |
| Públicos de Interesse | Seção 11.0 — segmentos de público relevantes |

---

## Estrutura de Arquivos

```
.claude/
  agents/agente-otimizador-produto.md       ← agente executor
  templates/_template-checklist-produto.md  ← template de referência (estrutura)
  workflows/workflow-otimizador-produto.md  ← este arquivo

Notion — Catálogo de Produtos             ← destino do conteúdo gerado
```

---

## Passo a Passo de Execução

### 1. Acionar o agente

O usuário informa o produto a ser otimizado. Pode ser:
- Nome do produto ("Otimize o Manta Flex")
- URL da página no Notion
- Trecho de texto colado diretamente na conversa

### 2. Buscar dados no Notion

O agente usa o Notion MCP para localizar a página do produto e ler:
- Propriedades (marca, linha, categoria, variantes existentes)
- Corpo da página (campos técnicos, textos, PDFs)
- Informações de kits e departamentos nas bases de apoio

Se o produto não for encontrado, o agente informa e pede esclarecimento.

### 3. Gerar o checklist no chat

O agente monta o checklist completo e apresenta no chat como rascunho.

**Produto individual** → Template de Produto (seções 0.0 a 12.0)
**Kit de produtos** → Template de Kit (seções 0.0 a 5.0)

Campos sem informação recebem `"Não informado nos materiais disponíveis"` — nunca ficam em branco.

### 4. Revisar e aprovar

O usuário revisa, ajusta o que for necessário e aprova explicitamente.

Formatos de aprovação aceitos: "aprovado", "pode aplicar", "tá bom", "salva no Notion".

### 5. Aplicar o conteúdo aprovado

Após aprovação, o agente preenche as seções aprovadas na página do produto no Notion usando o Notion MCP.

### 6. Aplicar no Wake Commerce

Com o checklist aprovado, as 3 frentes da fase 01 no Wake Commerce:

| O que aplicar | Seção do checklist | Caminho no Wake | Método |
|---|---|---|---|
| **Categorias** | 4.3 | Produtos → Lista de Produtos → editar produto → aba Categorias | Manual — atribuir categorias e marcar "Categoria Principal" |
| **Atributos** | 4.2 | Produtos → Lista de Produtos → "Atualizar Produtos" → tipo "Atributos" | Planilha — baixar template, preencher colunas, subir |
| **SEO** | 9.0 (por variante) | Produtos → Lista de Produtos → "Importar Dados SEO" | Batch CSV → XLS → ver `workflow-seo-importacao.md` |

> **Ordem recomendada:** Categorias → Atributos → SEO. Categorias definem o contexto; Atributos habilitam filtros; SEO usa os dois como base.
>
> **Categoria Principal:** somente a categoria marcada como principal é enviada para o XML do Google Shopping. Definir antes de qualquer ação de mídia paga.

**Atributos — fluxo resumido:**
1. Wake admin → Produtos → Lista de Produtos → filtrar o produto
2. "Atualizar Produtos" → selecionar tipo "Atributos" → baixar planilha modelo
3. Preencher valores da seção 4.2 nas colunas correspondentes (cada atributo = uma coluna)
4. Salvar e subir a planilha

**SEO — detalhado em:** `.claude/workflows/workflow-seo-importacao.md`

---

## Árvore de Decisão: Template

```
O item é um kit (combo/pack)?
├── Sim → Template de Kit (seções 0.0 a 5.0)
└── Não → Template de Produto (seções 0.0 a 12.0)
```

---

## Regras do Workflow

| Regra | Detalhe |
|---|---|
| Aprovação obrigatória | Nenhuma escrita no Notion sem aprovação explícita |
| Sem invenção de dados | Campo vazio = `"Não informado nos materiais disponíveis"` |
| Títulos de seção intocáveis | Copiar exatamente como no template |
| Atributos somente quando se aplicam | Não preencher `[ACABAMENTO]`, `[PESO]` etc. se o produto não os tiver |
| Segmentos de público somente quando relevantes | Omitir segmentos que não fazem sentido para o produto |
| Departamentos com nomes exatos | Consultar a base Todos os Departamentos; não criar nomes novos |

---

## Checklist de Revisão (pré-aprovação)

Antes de apresentar o rascunho ao usuário, verifique:

**Completude:**
- [ ] Seção 0.0 com menos de 180 caracteres
- [ ] Seção 1.0 com pelo menos cor/textura, composição e mais um campo
- [ ] Seção 2.0 com descrição comercial + mínimo 2 benefícios-chave
- [ ] Seção 3.0 com mínimo 3 perguntas e respostas
- [ ] Seção 4.0 com marca/linha, categoria e nível de complexidade
- [ ] Seção 6.0 com title, meta description e palavras-chave

**Qualidade:**
- [ ] Benefícios-chave em 2 a 4 palavras
- [ ] Tipo de vitrine definido ([INOVAÇÃO] ou [CONCEITO])
- [ ] Atributos preenchidos somente quando aplicáveis
- [ ] Segmentos de público omitidos quando não relevantes
- [ ] Kits e departamentos consultados nas bases de apoio (nomes exatos)
- [ ] Nenhum campo em branco — todos com dado ou com `"Não informado nos materiais disponíveis"`

**Copy:**
- [ ] Seção 11.0 COPY com ganho + narrativa + CTA
- [ ] Breve descrição (0.0) factual e vendedora

---

## Erros Comuns

| Erro | Consequência | Como evitar |
|---|---|---|
| Escrever no Notion antes da aprovação | Conteúdo incorreto publicado | Sempre aguardar "aprovado" explícito |
| Deixar campos em branco | Template incompleto, dados perdidos | Usar `"Não informado nos materiais disponíveis"` |
| Inventar departamentos | Classificação errada no Notion | Consultar a base Todos os Departamentos |
| Preencher atributos que não se aplicam | Filtros errados no e-commerce | Preencher somente os atributos pertinentes |
| Benefícios-chave longos demais | Não cabe no layout das vitrines | Máximo 4 palavras por benefício |

---

## Referências de Arquivo

| Arquivo | Papel |
|---|---|
| `.claude/agents/agente-otimizador-produto.md` | Agente executor — templates completos e regras de qualidade |
| `.claude/templates/_template-checklist-produto.md` | Template de referência — estrutura do checklist |
| `.claude/workflows/workflow-seo-importacao.md` | Como compilar e enviar os dados SEO ao Wake Commerce via CSV |

**Fonte de dados:** Notion Catálogo de Produtos — `notion.so/iva-digital/342c28ee80ae80d2bc59fc52c73f2450`
