# Workflow: Importação de SEO de Produto — Wake Commerce

> **Última revisão:** 2026-06-08
> **Plataforma:** Wake Commerce (Escuta o Véio!)

---

## Visão Geral

Este workflow define como os dados de SEO gerados pelo Otimizador de Produtos são transformados em arquivos CSV para importação em massa no Wake Commerce.

**Regra central:** nunca enviar um CSV por produto — compilar o dia inteiro e enviar **uma única importação por dia**.

---

## Caminho no Admin Wake Commerce

```
Produtos → Lista de Produtos
  → [botão direito] "Exportar Dados de SEO"   ← para baixar o template atual
  → [botão direito] "Importar Dados SEO"       ← para subir o arquivo editado
```

> Não usar o fluxo "Atualizar Produtos" — esse é para preço, estoque e atributos. O SEO tem entrada própria.

---

## Estrutura de Arquivos

```
canais-de-vendas/escuta-o-veio/loja-virtual/
  ProdutoSeo.csv                  ← exportação original (referência histórica)
  atualizações/
    _base/
      ProdutoSeo.csv              ← versão mais atualizada do estado atual do Wake Commerce
                                     (atualizar após cada importação bem-sucedida)
    pendente/
      YYYY-MM-DD-seo.csv          ← batch do dia em construção (somente produtos alterados)
    enviados/
      YYYY-MM-DD-seo.csv          ← batches já importados (histórico)
```

### Regras dos arquivos

| Arquivo | O que contém | Como usar |
|---|---|---|
| `_base/ProdutoSeo.csv` | Estado atual de todos os produtos já configurados | Consultar para comparar; nunca editar diretamente |
| `pendente/YYYY-MM-DD-seo.csv` | Somente os produtos sendo otimizados hoje | Adicionar linhas ao longo do dia; enviar ao final |
| `enviados/YYYY-MM-DD-seo.csv` | Histórico de importações realizadas | Apenas referência — não reeditar |

---

## Formato do CSV

**Formato de trabalho:** `.csv` separado por `;` — legível, versionável no git
**Formato de importação:** `.xls` — Wake Commerce aceita `.xls` no "Importar Dados SEO"
**Encoding:** UTF-8

**Fluxo de arquivo:**
1. Editar/gerar em `.csv` (arquivo de trabalho, fica em `pendente/`)
2. Converter para `.xls` via PowerShell antes de importar no Wake:
```powershell
$csv = "caminho\pendente\YYYY-MM-DD-seo-[produto].csv"
$xls = $csv -replace '\.csv$', '.xls'
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false; $excel.DisplayAlerts = $false
$wb = $excel.Workbooks.Open($csv, 0, $true, 6, "", "", $true, 2, ";", $false, $false, 0, $true)
$wb.SaveAs($xls, 56)
$wb.Close($false); $excel.Quit()
```

### Header (obrigatório, sempre na linha 1)

```
ProdutoId;Nome Produto;Tipo Dado;Title;Content;Http-Equiv;Name;Scheme
```

### 3 linhas por variante de produto

```
[ID];[Nomenclatura 9.1];title;[Title 9.2];;;;
[ID];[Nomenclatura 9.1];meta;;[Meta Description 9.3];;description;
[ID];[Nomenclatura 9.1];meta;;[Keywords 9.4];;keywords;
```

**Mapeamento do checklist para o CSV:**

| Campo CSV | Seção do checklist |
|---|---|
| `ProdutoId` | ID_WAKE (campo dentro de cada variante em 9.0) |
| `Nome Produto` | 9.1 NOMENCLATURA (TÍTULO) |
| `Title` (linha title) | 9.2 TITLE DA PÁGINA (SEO) |
| `Content` (linha meta description) | 9.3 META-DESCRIPTION (SEO) |
| `Content` (linha meta keywords) | 9.4 PALAVRA-CHAVE (SEO) |

---

## Passo a Passo

### Regra fundamental — sempre baixar o template da Wake

**Nunca criar o arquivo do zero.** O Wake Commerce gera o template com os dados atuais dos produtos. O fluxo correto é sempre:

1. Wake admin → local correto de importação de SEO
2. Baixar template **"Somente Válidos"** (mais leve — apenas produtos ativos)
3. Deletar todas as linhas EXCETO os produtos sendo atualizados
4. Editar os dados nas linhas restantes com os novos valores de SEO
5. Salvar como `.xls` e importar

O template baixado substitui o `_base/` — após cada download, mover o arquivo para `atualizações/_base/ProdutoSeo.csv`.

### Durante o dia — preparar o batch

A cada produto com checklist SEO aprovado:
1. Abrir o template baixado (`_base/ProdutoSeo.csv`)
2. **Buscar as linhas do produto pelo nome** — cada variante tem 3 linhas (title + description + keywords)
3. Copiar apenas as linhas dos produtos sendo atualizados para o arquivo de batch do dia (`pendente/YYYY-MM-DD-seo.csv`)
4. Editar os campos Title, Content e Name conforme o checklist aprovado (9.2, 9.3, 9.4)
5. Se o produto **não estiver no template** (novo cadastro): reportar ao usuário — produto ainda não tem ID no Wake

> O agente gera os novos valores de SEO no chat como referência — o preenchimento no arquivo deve ser feito a partir das linhas já existentes no template.

### Final do dia — revisar e importar

**Checklist antes de importar:**
- [ ] Arquivo tem apenas os produtos sendo alterados (linhas extras deletadas)
- [ ] Cada produto tem exatamente 3 linhas (title + description + keywords)
- [ ] Nenhum travessão `—` em nenhum campo (usar `|`)
- [ ] Arquivo salvo como `.xls`

**Após importar com sucesso:**
1. Mover arquivo de `pendente/` para `enviados/`
2. Baixar novo template "Somente Válidos" do Wake → substituir `_base/ProdutoSeo.csv`

---

## Regras Críticas

| Regra | Motivo |
|---|---|
| Importar sempre via "Importar Dados SEO" | Caminho correto — "Atualizar Produtos" é para preço/estoque/atributos |
| Uma importação por dia | Upload em massa é sensível — consolidar reduz risco de conflito |
| Somente produtos alterados | Arquivo menor = menor chance de erro na plataforma |
| Nunca editar `_base/` diretamente | O base é a fonte de verdade — atualizar só após importação confirmada |
| `—` proibido em todos os campos | Wake Commerce não processa travessão — usar `\|` |
| Encoding UTF-8 obrigatório | Evita corrupção de caracteres especiais (ã, ç, é, etc.) |
| Title: máx ~65 caracteres | Recomendação do buscador — palavra-chave principal no início, marca no final |
| Description: máx 165 caracteres | Limite recomendado — usar CTA (ex: "Compre agora", "Parcele sem juros") |
| Content (campo): máx 1.000 caracteres | Limite técnico da plataforma |

---

## Exemplo de linhas prontas (Nex Floor Granito Líquido)

```csv
ProdutoId;Nome Produto;Tipo Dado;Title;Content;Http-Equiv;Name;Scheme
[ID];Nex Floor Granito Líquido Cristal 4kg | Piso Autonivelante Epóxi de Alta Resistência para Pisos Internos e Externos;title;Nex Floor Granito Líquido 4kg | Comprar Piso Epóxi Autonivelante Cristal;;;;
[ID];Nex Floor Granito Líquido Cristal 4kg | Piso Autonivelante Epóxi de Alta Resistência para Pisos Internos e Externos;meta;;Nex Floor Granito Líquido Cristal 4kg: piso epóxi autonivelante de alta resistência para áreas internas e externas. Fácil aplicação. Parcele sem juros!;;description;
[ID];Nex Floor Granito Líquido Cristal 4kg | Piso Autonivelante Epóxi de Alta Resistência para Pisos Internos e Externos;meta;;piso epóxi autonivelante, nex floor, granito líquido, piso epóxi cristal, piso autonivelante epóxi, resina para piso, piso monolítico, piso epóxi preço, piso epóxi 4kg;;keywords;
```

> Substituir `[ID]` pelo ID real da variante no Wake Commerce antes de enviar.

---

## Caminhos no Admin Wake Commerce (referência rápida)

| O que fazer | Caminho no admin |
|---|---|
| **SEO produto** — exportar base | Produtos → Lista de Produtos → "Exportar Dados de SEO" |
| **SEO produto** — importar batch | Produtos → Lista de Produtos → "Importar Dados SEO" |
| **SEO hotsite/categoria** — exportar | Vitrines → Hotsites → "Exportar Dados SEO" |
| **SEO hotsite/categoria** — importar | Vitrines → Hotsites → "Importar Dados SEO" |
| **Atributos** — criar novo | Produtos → Atributos → "+ Adicionar Atributo" |
| **Atributos** — importar em massa | Produtos → Atributos → "Mais Opções" → baixar modelo → "Importar Atributos" |
| **Atributos** — atualizar valor em produto existente | Produtos → Lista de Produtos → "Atualizar Produtos" → tipo "Atributos" |
| **Categorias** — criar/editar | Produtos → Categorias → "Adicionar Categoria" |
| **Categorias** — vincular Categoria Google em lote | Produtos → Categorias → "Exportar Categoria Google" → editar coluna C → "Importar Categorias Google" |
| **Categoria principal do produto** (Google Shopping) | Produtos → Lista de Produtos → editar produto → marcar "Categoria Principal" |
| **Preço / Estoque / Completa** | Produtos → Lista de Produtos → "Atualizar Produtos" → selecionar tipo |

---

## Referências

| Arquivo | Papel |
|---|---|
| `.claude/agents/agente-otimizador-produto.md` | Gera os campos SEO (9.0–9.4) e as linhas CSV prontas |
| `.claude/workflows/workflow-otimizador-produto.md` | Workflow principal de otimização de produto |
| `canais-de-vendas/escuta-o-veio/loja-virtual/atualizações/_base/ProdutoSeo.csv` | Estado atual de SEO no Wake Commerce |
