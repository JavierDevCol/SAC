# 📋 Backlog de Desarrollo

> **Workspace:** [Nombre del Workspace]
> **Tipo:** [Mono-Proyecto | Multi-Proyecto]
> **Última Actualización:** [timestamp]
> **Total HUs:** [número]

---

## 📊 Resumen de Estados

| Estado | Cantidad | Descripción |
|--------|----------|-------------|
| `[ ]` Pendiente | 0 | Sin refinar |
| `[R]` Refinada | 0 | Lista para validación arquitectónica |
| `[A]` Aprobada | 0 | Lista para planificación |
| `[P]` Planificada | 0 | Lista para ejecución |
| `[E]` En Ejecución | 0 | En progreso |
| `[X]` Completada | 0 | Finalizada |
| `[B]` Bloqueada | 0 | Con dependencias no resueltas |

---

## 📊 Resumen por Proyecto

> **Nota:** Solo en Multi-Proyecto. Omitir sección completa en Mono-Proyecto.

| Proyecto | [ ] | [R] | [A] | [P] | [E] | [X] | [B] | Total |
|----------|-----|-----|-----|-----|-----|-----|-----|-------|
| [proyecto_1] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Compartidas** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

---

## 📖 Guía de Estados

```
[ ] Pendiente
  ↓ >refinar_hu (REFINADOR)
[R] Refinada
  ↓ >validar_hu (ONAD)
[A] Aprobada
  ↓ >planificar_hu (ARCHDEV)
[P] Planificada
  ↓ >ejecutar_plan (ARCHDEV)
[E] En Ejecución
  ↓ (finaliza)
[X] Completada

[B] Bloqueada (puede ocurrir en cualquier momento)
```

**Detección de estado por archivos:**
```
SAC-XXX/HU.md                      → [ ] Pendiente
SAC-XXX/HU.md + Refinamiento.md    → [R] Refinada
+ ## Aprobación en Refinamiento.md → [A] Aprobada
+ Plan.md                          → [P] Planificada
+ Tracking.md                      → [E] En Ejecución
Plan.md Estado: COMPLETADO         → [X] Completada
```

---

## 📇 Índice Rápido

<!--
  Tabla compacta para carga inicial optimizada (bajo consumo de tokens).
  El agente carga SOLO esta tabla al iniciar sesión.
  Para detalle de una HU, leer SAC-XXX/HU.md directamente.
  Esta tabla se regenera automáticamente con >sincronizar_backlog.
-->

| ID | Título | Estado | Prioridad | Tipo | Proyecto | Tasks |
|----|--------|--------|-----------|------|----------|-------|
| [ID-HU] | [Título] | [ ] | [P0\|P1\|P2\|P3] | [Feature\|Bug\|DeudaTécnica] | [proyecto] | [— \| TASK-1,TASK-2,...] |

---

## 🔧 Deuda Técnica

<!-- Resumen de deuda técnica. Detalle en artifacts/deuda_tecnica/ -->

| ID | Descripción | Prioridad | Estado |
|----|-------------|-----------|--------|
| DT-001 | [Descripción] | [Alta\|Media\|Baja] | [Pendiente\|En progreso\|Resuelta] |

---

## 📈 Métricas del Backlog

| Métrica | Valor |
|---------|-------|
| Total HUs | 0 |
| Completadas | 0 (0%) |
| En progreso | 0 (0%) |
| Pendientes | 0 (0%) |
| Bloqueadas | 0 (0%) |
| Story Points totales | 0 SP |
| Story Points completados | 0 SP (0%) |

---

> **Archivo generado por `>sincronizar_backlog`**
> **Las HUs detalladas viven en `artifacts/HU/[ID-HU]/`**
