# Workflow: Remixagem de Vídeos (Video Remix)

> **Agentes:** `agente-analisador-footage.md` · `agente-transcritor.md` · `agente-video-remix.md`
> **Última revisão:** 2026-06-03

---

## Visão Geral

Este workflow transforma múltiplos vídeos de terceiros (influenciadores, parceiros, criadores de conteúdo) sobre um mesmo tema em **um único vídeo autoral** — com co-direção editorial, ritmo variado e sem resquícios de identidade visual de terceiros (vinhetas, lower thirds, CTAs).

O áudio de narração de um dos vídeos se torna a trilha-mestre. Os outros vídeos são analisados quadro a quadro para identificar planos limpos, e os clips são selecionados semanticamente conforme o que está sendo narrado.

**Quando usar:**
- Temos 3+ vídeos de parceiros sobre o mesmo produto/técnica/situação
- Queremos publicar no YouTube sem simplesmente repostar o vídeo original
- Queremos um vídeo autoral que pareça editorial, não uma colagem

---

## Pré-requisitos

- [ ] FFmpeg instalado (`ffmpeg -version` deve retornar sem erro — reiniciar terminal se necessário)
- [ ] Pasta do projeto criada com subpastas `inputs/`, `internal/`, `output/`
- [ ] Vídeos copiados para `inputs/`
- [ ] Ao menos 1 vídeo com narração clara e completa

---

## Estrutura de pastas

```
canais-de-vendas/escuta-o-veio/ações-de-marketing/redes-sociais/youtube/
  {tema-slug}/
    inputs/                  ← vídeos brutos (não editar)
    internal/
      durations.txt          ← inventário de duração/resolução
      frames/                ← frames extraídos para análise (temporários)
        footage-02/
          frame-001.jpg      (0:00 do footage)
          frame-002.jpg      (0:30 do footage)
          ...
      footage-inventory.md   ← catálogo visual: o que aparece em cada momento
      beats.md               ← estrutura da narração: tópico por timestamp
      lista-de-cortes.md     ← mapa de cortes aprovado
      narration.mp3          ← áudio da narração extraído
      clip-01.mp4 ... clip-N.mp4   ← clips cortados
      filelist.txt           ← lista para concatenação
      assembled.mp4          ← vídeo montado antes de trocar áudio
    output/
      video-final.mp4        ← resultado final
```

---

## Pipeline de 3 agentes

```
[1] Analisador de Footage       → footage-inventory.md
[2] Transcritor                 → beats.md
[3] Video Remix (co-direção)    → lista-de-cortes.md → video-final.mp4
```

Os agentes 1 e 2 podem ser executados em paralelo (não dependem um do outro).

---

## Passo a passo

### 1. Preparar a pasta do projeto

```
canais-de-vendas/escuta-o-veio/ações-de-marketing/redes-sociais/youtube/{tema-slug}/
  inputs/       ← copie os vídeos aqui
  internal/
  output/
```

### 2. Analisar os footages (Agente 1)

```
"Analise os footages de {tema-slug}"
```

O agente vai:
- Extrair 1 frame a cada 30s de cada footage
- Classificar cada frame: `clean` / `intro` / `outro` / `graphic`
- Descrever o que aparece em cada frame clean
- Gerar `internal/footage-inventory.md`

**Duração:** 5–15 min dependendo do número de vídeos.

### 3. Segmentar a narração (Agente 2)

```
"Transcreva a narração de {tema-slug}"
```

O agente vai:
- Usar Whisper (se disponível), detecção de silêncio (FFmpeg), ou pedir um outline manual
- Gerar `internal/beats.md` com timestamps e tópicos

**Duração:** 1–5 min (automático) ou imediato (manual).

> **Atalho manual:** você mesmo pode escrever o beats.md com um outline rápido em 5 linhas. Funciona bem para vídeos que você conhece.

### 4. Co-direção e montagem (Agente 3)

```
"Retome o contexto de video-remix para {tema-slug}"
```

O agente vai:
- Verificar que inventário e beats existem
- Propor clips beat a beat, com justificativa editorial
- Aguardar sua aprovação ou ajuste clip a clip
- Após aprovação do mapa completo, montar com FFmpeg
- Entregar `output/video-final.mp4`

**Exemplo de interação na co-direção:**
```
Beat 04 (2:30–4:00): "Forma 1 — aplicação com rolo na parede"

  A (8s)  footage-02 @ 1:30  close de mão com rolo  [abertura]
  B (16s) footage-02 @ 2:00  aplicação contínua     [ação]
  C (12s) footage-04 @ 5:45  textura ao secar        [fechamento]

[A] Aprovar  [1/2/3] Substituir  [+] Adicionar  [X] Rejeitar
```

---

## Notas técnicas importantes

**Frame rate:** Os vídeos de fontes diferentes frequentemente têm frame rates distintos (60fps, 30fps, 29.97fps). Todos os clips são re-encoded para **30fps** durante o corte para evitar perda de frames na concatenação.

**Concatenação:** Usar sempre re-encoding (`-c:v libx264`) em vez de `-c copy` na etapa de concatenação. O `-c copy` causa perda de frames com fontes mistas.

**Resolução:** Clips de fontes 720p são normalizados para 1080p com letterbox (barras pretas) durante o corte.

---

## Roadmap

| Versão | Status | Descrição |
|---|---|---|
| V1 | ✅ Implementado | Rotação mecânica de clips (sem co-direção) |
| V1.5 | ✅ Implementado | Co-direção editorial com inventário visual + beats |
| V2 | 🔜 Planejado | Narração substituída por TTS com voz da IVA Química via Magnific |
| V3 | 💡 Ideia | Geração de footage novo com Magnific/Seedance para cobrir gaps |
