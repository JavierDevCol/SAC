# 📋 Backlog de Desarrollo

> **Proyecto:** [Nombre del Proyecto]  
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
| `[E]` En Ejecución | 0 | En progreso por ArchDev |
| `[X]` Completada | 0 | Finalizada |
| `[B]` Bloqueada | 0 | Con dependencias no resueltas |

---

## 📖 Guía de Estados

```
[ ] Pendiente
  ↓ refinar_hu (REFINADOR)
[R] Refinada
  ↓ validar_hu (ONAD)
[A] Aprobada
  ↓ planificar-hu (ONAD)
[P] Planificada
  ↓ ejecutar-plan (ARCHDEV)
[E] En Ejecución
  ↓ (finaliza)
[X] Completada

[B] Bloqueada (puede ocurrir en cualquier momento)
```

---

## 🎯 Historias de Usuario

---

### [ID-HU]: [Título de la HU]
- **Estado:** [ ] Pendiente
- **Origen:** [ID de la tarea/decisión que la originó]
- **Prioridad:** [Alta | Media | Baja]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

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
- **Estado:** [ ] Pendiente
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

-->

<!--
### PLANTILLA: Estado [R] Refinada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [R] Refinada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]
- [ ] CA2: [descripción]
- [ ] CA3: [descripción]

**Dependencias Técnicas:**
- [Dependencia 1]
- [Dependencia 2]

-->

<!--
### PLANTILLA: Estado [A] Aprobada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [A] Aprobada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Fecha aprobación:** [timestamp]
- **Aprobado por:** Arquitecto Onad

**Notas de Aprobación:**
- ✅ [Nota de validación 1]
- ✅ [Nota de validación 2]
- ⚠️ [Advertencia o recomendación]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]
- [ ] CA2: [descripción]
- [ ] CA3: [descripción]

-->

<!--
### PLANTILLA: Estado [P] Planificada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [P] Planificada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Fecha aprobación:** [timestamp]
- **Plan:** `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md`
- **Fecha planificación:** [timestamp]
- **Secciones:** [N]
- **Archivos a modificar:** [N]
- **Tests a crear:** [N]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]
- [ ] CA2: [descripción]
- [ ] CA3: [descripción]

-->

<!--
### PLANTILLA: Estado [E] En Ejecución
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [E] En Ejecución
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Plan:** `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md`
- **Fecha planificación:** [timestamp]
- **Inicio ejecución:** [timestamp]
- **Progreso:** [X]% ([Y]/[Z] pasos)
- **Sección actual:** [N]/[M] - [Nombre sección]
- **Tracking:** `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json`

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- ✅ CA1: [descripción] (completado)
- ✅ CA2: [descripción] (completado)
- ⏳ CA3: [descripción] (en progreso)
- [ ] CA4: [descripción] (pendiente)

-->

<!--
### PLANTILLA: Estado [X] Completada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [X] Completada
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Plan:** `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md`
- **Completado:** [timestamp]
- **Duración:** [X]h [Y]min
- **Commit:** `[hash]`

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- ✅ CA1: [descripción]
- ✅ CA2: [descripción]
- ✅ CA3: [descripción]

**Implementación:**
- ✅ [Logro 1]
- ✅ [Logro 2]
- ✅ Tests: [X] unitarios + [Y] integración
- ✅ Cobertura: [Z]%

-->

<!--
### PLANTILLA: Estado [B] Bloqueada
─────────────────────────────────────

### [ID-HU]: [Título]
- **Estado:** [B] Bloqueada
- **Estado previo:** [estado anterior al bloqueo]
- **Origen:** [ID origen]
- **Prioridad:** [Alta | Media | Baja]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp]
- **Estimación:** [X] SP / [Y] horas
- **Motivo bloqueo:** [descripción del bloqueo]
- **Tipo bloqueo:** [DEPENDENCIA_HU | DEPENDENCIA_EXTERNA | DECISION_PENDIENTE | RECURSO_NO_DISPONIBLE]
- **Fecha bloqueo:** [timestamp]
- **Acción requerida:** [qué debe resolverse]

**Descripción:**
Como [rol], quiero [funcionalidad] para [beneficio].

**Criterios de Aceptación:**
- [ ] CA1: [descripción]
- [ ] CA2: [descripción]

**Dependencias:**
- [ID-HU-dependencia] - [estado] [descripción]
- [Recurso externo] - [estado]

-->

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

| Fecha | HU | Cambio | Responsable |
|-------|-----|--------|-------------|
| [timestamp] | [ID-HU] | [descripción del cambio] | [rol] |

---

*Última actualización automática por el sistema Cochas*
