# Refinamiento: [ID-HU] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **ID** | [ID-HU] |
| **Título** | [Título corto] |
| **Complejidad** | [🟢 BAJO \| 🟡 MEDIO \| 🔴 ALTO] |
| **Story Points** | [X] SP |
| **Estimación Horas** | [Y] horas |
| **Fecha refinamiento** | [FECHA_ISO_8601] |
| **Iteración** | [N] |
| **Modo** | [Plano \| Particionada] |
| **Tasks** | [— \| [ID-HU]-TASK-1, [ID-HU]-TASK-2, ...] |

---

## 1. Historia de Usuario

**Como** [rol]
**Quiero** [funcionalidad]
**Para** [beneficio]

---

## 2. Criterios de Aceptación

<!-- Cada CA debe cumplir SMART. Los CAs son la fuente de verdad para validación. -->

- [ ] **CA-01:** Dado [contexto], cuando [acción], entonces [resultado esperado]
- [ ] **CA-02:** Dado [contexto], cuando [acción], entonces [resultado esperado]
- [ ] **CA-03:** Dado [contexto], cuando [acción errónea], entonces [manejo de error]

---

## 3. Preguntas de Clarificación

### Resueltas ✅

| # | Pregunta | Respuesta | Impacto |
|---|----------|-----------|---------|
| 1 | [Pregunta] | [Respuesta] | [Alto/Medio/Bajo] |

### Pendientes ❓

| # | Pregunta | Prioridad |
|---|----------|-----------|
| 1 | [Pregunta sin resolver] | [Alta/Media/Baja] |

---

## 4. Desglose Técnico (Vertical)

### MODO PLANO

#### Slice 1: [Nombre del slice mínimo]

| ID Tarea | Descripción | Capa | Estimación |
|----------|-------------|------|------------|
| [ID-HU]-API-01 | [Descripción] | API | [X]h |
| [ID-HU]-SVC-01 | [Descripción] | Servicio | [X]h |
| [ID-HU]-DB-01 | [Descripción] | Persistencia | [X]h |
| [ID-HU]-TEST-01 | [Descripción] | Testing | [X]h |

### MODO PARTICIONADO

<!-- Cada task funcional tiene sus propios CAs granulares y desglose -->

#### Task [ID-HU]-TASK-1: [Objetivo funcional]

**Traza CA padre:** CA-01
**Estimación:** [X] SP

##### Criterios de Aceptación (granulares)

- [ ] **CA-TASK1-01:** Dado [contexto], cuando [acción], entonces [resultado]
- [ ] **CA-TASK1-02:** Dado [contexto], cuando [acción], entonces [resultado]

##### Desglose Técnico

| ID Tarea | Descripción | Capa | Estimación |
|----------|-------------|------|------------|
| [ID-HU]-TASK-1-API-01 | [Descripción] | API | [X]h |
| [ID-HU]-TASK-1-SVC-01 | [Descripción] | Servicio | [X]h |
| [ID-HU]-TASK-1-DB-01 | [Descripción] | Persistencia | [X]h |
| [ID-HU]-TASK-1-TEST-01 | [Descripción] | Testing | [X]h |

---

## 5. Estimación

### Desglose

| Factor | Valor | Justificación |
|--------|-------|---------------|
| Complejidad base | [X] | [Razón] |
| Incertidumbre | [+Y] | [Razón] |
| Riesgo | [+Z] | [Razón] |
| **Total SP** | **[X+Y+Z]** | — |

### Estrategia Recomendada

- **Enfoque:** [TDD \| Incremental \| Feature Toggle \| Spike primero]
- **Razón:** [Justificación]

---

## 6. Riesgos y Dependencias

### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| [Riesgo 1] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Acción] |

### Dependencias

| Tipo | Referencia | Estado |
|------|------------|--------|
| HU previa | [HU-XXX] | [Estado] |
| API externa | [Nombre] | [Disponible/Pendiente] |
| Decisión | [ADR-XXX] | [Aprobado/Pendiente] |

---

## Aprobación

<!-- Generado por >validar_hu al aprobar -->

| Campo | Valor |
|-------|-------|
| **Estado** | ✅ Aprobada |
| **Aprobado por** | Arquitecto Onad |
| **Fecha aprobación** | [FECHA_ISO_8601] |
| **Nivel validación** | [basico \| completo \| exhaustivo] |
| **Notas** | [Resumen de validación] |

### Directrices de Planificación

- **Fases sugeridas:** [Estilo arquitectónico y orden recomendado]
- **Componentes clave:** [Componentes a crear/modificar]
- **Dependencias entre HUs:** [HUs que deben completarse antes]
- **Riesgos a mitigar:** [Riesgos detectados durante validación]
- **Notas adicionales:** [ADRs relevantes, patrones recomendados]

---

## Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| [Fecha] | Refinamiento inicial | Iteración 1 |
| [Fecha] | Aprobación | Validación completada |

---

> **Archivo:** `{{artifacts.hu_folder}}/[ID-HU]/Refinamiento.md`
> **Creado por:** `>refinar_hu`
> **Actualizado por:** `>validar_hu`
