# Workflow: Gestão de Sprints e Metodologia Ágil

> **Agente executor:** `.claude/agents/agente-scrum-master.md`
> **Atualizado em:** 2026-06-01

---

## Como retomar o contexto

Diga: **"Retome o contexto de gestão de sprints"**

O agente vai carregar automaticamente:
- Histórico de capacity por colaborador
- Estado atual do Backlog e das Sprints no ClickUp
- Conceitos e decisões já alinhados com o time

---

## O que foi definido até agora

### Time e capacity real (base: Sprints 1–4)

| Colaborador | Capacity real | Efetividade histórica |
|---|---|---|
| Guilherme Pereira | ~4–5 tasks/sprint | 66,7% |
| Gustavo | ~2–3 tasks/sprint | 53,3% |
| Nicholas | ~4 tasks/sprint | 36,4%* |
| Nicolas Rodrigues | 4 tasks/sprint | 100% |

*Nicholas entrou no ciclo na Sprint 4 — amostra única, baixa confiança.

> **Diagnóstico da Sprint 4:** overcommit generalizado. Os três principais membros receberam 5 tasks colaborativas da trilha Qualifica/EOV simultaneamente, criando dependência cruzada e zero entregas nesse bloco.

### Hierarquia de trabalho adotada

```
Epic → Feature → User Story → Task
```

- **User Story:** "Como [quem], eu quero [o quê], para que [benefício]."
- **Task:** 1 responsável, entregável claro, 1–3 dias de trabalho.
- **Estimativa:** Planning Poker com escala Fibonacci (1·2·3·5·8·13·21)

### Conceitos ativos no time

| Conceito | Definição rápida |
|---|---|
| Capacity | Total de trabalho absorvível por pessoa/sprint (meta: 70–80% do máximo) |
| Efetividade | Tasks entregues ÷ tasks comprometidas |
| Velocity | Média de entregas por sprint (base para planejar a próxima) |
| Headroom | Folga intencional para imprevistos (~20–30% da capacity) |
| Overcommit | Comprometer mais trabalho do que a capacity comporta |
| Planning Poker | Estimativa colaborativa sem influência mútua |

---

## Rituais de Sprint (recomendados)

### Sprint Planning (início de cada sprint — ~1h)

1. Revisar tasks pendentes da sprint anterior
2. Priorizar Backlog com o time
3. Estimar tasks novas via Planning Poker (ou P/M/G se o time preferir)
4. Atribuir respeitando capacity real de cada colaborador
5. Definir meta da sprint em 1 frase

**Capacidade total estimada por sprint (time completo):**
```
Guilherme: 4–5 tasks
Gustavo:   2–3 tasks
Nicholas:  3–4 tasks
Nic. Rod:  4 tasks
─────────────────────
Total:     13–16 tasks por sprint (sem overcommit)
```

### Sprint Review (fim de sprint — ~30min)

1. Demonstrar o que foi entregue
2. Calcular efetividade da sprint
3. Mover pendências para o Backlog ou próxima sprint com nova estimativa

### Retrospectiva (após a Review — ~30min)

3 perguntas:
- O que funcionou bem?
- O que travou?
- O que vamos mudar na próxima sprint?

---

## Pendências abertas em 01/06/2026

### Tasks não entregues da Sprint 4 (migrar para Sprint 5 ou Backlog)

| Task | Responsáveis | Decisão sugerida |
|---|---|---|
| [LP] DW240 - Página de Produto | — | Sprint 5 (urgente) |
| Trilha Qualifica e EOV | — | Sprint 5 |
| [EOV] 1.0 - Mestre do Acabamento | Nicholas, Gustavo, Guilherme | Sprint 5 |
| [EOV] 1.2 - Mestre do Acabamento | Nicholas, Gustavo, Guilherme | Sprint 5 |
| [QUALIFICA] 1.0 - Mestre do Acabamento | Nicholas, Guilherme, Gustavo | Sprint 5 |
| [EOV] 1.0 - Engenharia na Prática | Nicholas, Guilherme, Gustavo | Sprint 5 |
| [QUALIFICA] 1.0 - Engenharia na Prática | Nicholas, Guilherme, Gustavo | Sprint 5 |
| Vitrine de impermeabilização Qualifica | Nicholas | Sprint 5 |
| Implementação do Hotsite | Gustavo | Sprint 5 |
| Reels | Guilherme | Sprint 5 |
| Calendário de postagem | Nicholas, Gustavo | Sprint 5 |

### Backlog — itens sem sprint (14 tasks)

Clusters identificados:
- **LT Shine** (2 tasks) — atualizar cores + filtro de cores → Guilherme
- **Cadastro de Clientes** (3 tasks) — campos obrigatórios + segmentação CRM → sem dono
- **Calculadora de Rendimento** (3 tasks) — revisar se são duplicatas da entrega da Sprint 1
- **Widde no Storefront** — prioridade High, venceu 01/06 → Guilherme, entrar na Sprint 5
- **Bloco com 4 banners** — prioridade Normal → Guilherme
- **Panorama de categorias** — prioridade Normal → Gustavo

---

## Próximas ações prioritárias

1. **Planejar Sprint 5** — migrar pendências da Sprint 4, respeitar capacity real (~13–16 tasks total)
2. **Ativar time tracking no ClickUp** — ou adicionar campo de story points nas tasks para capacity em horas
3. **Limpar duplicatas do Backlog** — especialmente o cluster "Calculadora de Rendimento"

---

## Comandos úteis para este contexto

| O que fazer | Como pedir |
|---|---|
| Ver tasks do Backlog e Sprints | "Analise as tasks em backlog e nas sprints" |
| Calcular capacity do time | "Qual a capacity do time?" |
| Planejar próxima sprint | "Planeje a Sprint 5 com base na capacity real" |
| Reescrever task como User Story | "Reescreva [nome da task] como User Story com tasks derivadas" |
| Ver efetividade por colaborador | "Qual a efetividade de cada colaborador?" |
| Diagnóstico completo | "Faça um diagnóstico da Sprint [N]" |
