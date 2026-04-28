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
  ↓ >planificar_hu (ONAD)
[P] Planificada
  ↓ >ejecutar_plan (ARCHDEV)
[E] En Ejecución
  ↓ (finaliza)
[X] Completada

[B] Bloqueada (puede ocurrir en cualquier momento)
```

---

## 📇 Índice Rápido

<!-- 
  Tabla compacta para carga inicial optimizada (bajo consumo de tokens).
  El agente carga SOLO esta tabla al iniciar sesión.
  Para detalle de una HU, buscar su heading ### [ID-HU] más abajo.
  Esta tabla se regenera automáticamente con >sincronizar_backlog.
-->

| ID | Título | Estado | Prioridad | Tipo | Tasks |
|----|--------|--------|-----------|------|-------|
| [ID-HU] | [Título] | [ ] | [Alta\|Media\|Baja] | [Funcional\|Bug\|Técnica] | [— \| T1,T2,...] |

---

## 🎯 Historias de Usuario

<!-- 
================================================================================
ESTRUCTURA SEGÚN TIPO DE WORKSPACE
================================================================================

MONO-PROYECTO: Las HUs van directamente aquí, sin secciones de proyecto.

MULTI-PROYECTO: Crear una sección por proyecto:
  ### 📁 [nombre_proyecto]
  (HUs del proyecto)
  
  ### 📁 Compartidas
  (HUs cross-proyecto)
================================================================================
-->

---

### [ID-HU]: [Título de la HU]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [ ] Pendiente
- **Origen:** [ID de la tarea/decisión que la originó]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

<!-- SI Tipo=Bug: Usar descripción técnica breve (1-2 líneas).
     El detalle completo vive en el archivo Ref_Bug. -->

---

<!-- 
================================================================================
PLANTILLAS POR ESTADO - Copiar según corresponda
================================================================================
-->

<!--
### PLANTILLA: Estado [ ] Pendiente
─────────────────────────────────────

### [ID-HU]: [Título]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [ ] Pendiente
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]
- [proyecto_2]

-->

<!--
### PLANTILLA: Estado [R] Refinada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [R] Refinada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Tasks:** [— | [ID-HU]-T1, [ID-HU]-T2, ...] (solo si particionada)

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]
- [ ] CA2: [descripción]

**Dependencias Técnicas:**
- [Dependencia 1]

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

<!--
### PLANTILLA: Estado [A] Aprobada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [A] Aprobada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Tasks:** [— | [ID-HU]-T1, [ID-HU]-T2, ...] (solo si particionada)
- **Fecha aprobación:** [timestamp]
- **Aprobado por:** Arquitecto Onad

**Notas de Aprobación:**
- ✅ [Nota de validación 1]
- ⚠️ [Advertencia o recomendación]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

<!--
### PLANTILLA: Estado [P] Planificada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [P] Planificada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Tasks:** [— | [ID-HU]-T1, [ID-HU]-T2, ...] (solo si particionada)
- **Fecha aprobación:** [timestamp]
- **Plan:** `{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md`
- **Fecha planificación:** [timestamp]
- **Secciones:** [N]
- **Archivos a modificar:** [N]
- **Tests a crear:** [N]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

<!--
### PLANTILLA: Estado [E] En Ejecución
─────────────────────────────────────

### [ID-HU]: [Título]
- **Tipo:** [Funcional | Bug | Técnica]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [E] En Ejecución
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Ref_Bug:** [BUG-NNN / —] (solo si Tipo=Bug)
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Plan:** `{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md`
- **Inicio ejecución:** [timestamp]
- **Progreso:** [X]% ([Y]/[Z] pasos)
- **Sección actual:** [N]/[M] - [Nombre sección]
- **Tracking:** `{{artifacts.ejecuciones_folder}}/ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json`

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- ✅ CA1: [descripción] (completado)
- ⏳ CA2: [descripción] (en progreso)
- [ ] CA3: [descripción] (pendiente)

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

<!--
### PLANTILLA: Estado [X] Completada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [X] Completada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Plan:** `{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md`
- **Completado:** [timestamp]
- **Duración:** [X]h [Y]min
- **Commit:** `[hash]`

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- ✅ CA1: [descripción]
- ✅ CA2: [descripción]

**Implementación:**
- ✅ Tests: [X] unitarios + [Y] integración
- ✅ Cobertura: [Z]%

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

<!--
### PLANTILLA: Estado [B] Bloqueada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Proyecto:** [nombre_proyecto | compartida]
- **Estado:** [B] Bloqueada
- **Estado previo:** [estado anterior al bloqueo]
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **ADR_Ref:** [ADR-XXX]({{artifacts.adr_folder}}/ADR-XXX.md) | ninguno
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`
- **Motivo bloqueo:** [descripción del bloqueo]
- **Tipo bloqueo:** [DEPENDENCIA_HU | DEPENDENCIA_EXTERNA | DECISION_PENDIENTE | RECURSO_NO_DISPONIBLE]
- **Fecha bloqueo:** [timestamp]
- **Acción requerida:** [qué debe resolverse]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Dependencias:**
- [ID-HU-dependencia] - [estado] [descripción]

**Proyectos afectados:** (solo si Proyecto = compartida)
- [proyecto_1]

-->

---

## 🔧 Deuda Técnica

| ID | Proyecto | Descripción | Origen | Prioridad | Estado |
|----|----------|-------------|--------|-----------|--------|
| DT-001 | [proyecto] | [Descripción] | [HU-XXX \| Análisis] | [Alta \| Media \| Baja] | [Pendiente \| Resuelta] |

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

## 📝 Historial de Cambios

| Fecha | Proyecto | HU | Cambio | Responsable |
|-------|----------|-----|--------|-------------|
| [timestamp] | [proyecto] | [ID-HU] | [descripción] | [rol] |

---

> **Archivo generado automáticamente por el sistema SAC**
