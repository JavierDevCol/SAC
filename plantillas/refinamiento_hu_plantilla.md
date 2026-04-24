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

---

## 1. Historia de Usuario

**Como** [rol]  
**Quiero** [funcionalidad]  
**Para** [beneficio]

---

## 2. Criterios de Aceptación

<!--
Cada CA debe cumplir SMART:
- Específico: qué ocurre exactamente
- Medible: métricas verificables
- Alcanzable: realista
- Relevante: relacionado al objetivo
- Temporal: condiciones de tiempo
-->

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

### Slice 1: [Nombre del slice mínimo]
| ID Tarea | Descripción | Capa | Estimación |
|----------|-------------|------|------------|
| [ID-HU]-API-01 | [Descripción] | API | [X]h |
| [ID-HU]-SVC-01 | [Descripción] | Servicio | [X]h |
| [ID-HU]-DB-01 | [Descripción] | Persistencia | [X]h |
| [ID-HU]-TEST-01 | [Descripción] | Testing | [X]h |

### Slice 2: [Nombre del slice] <!-- Si aplica -->
| ID Tarea | Descripción | Capa | Estimación |
|----------|-------------|------|------------|
| ... | ... | ... | ... |

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

## 7. Ajustes Aplicados <!-- Solo en MODO_AJUSTE, Iteración >= 2 -->

### Iteración [N] - [Fecha]
| Observación Original | Ajuste Realizado |
|---------------------|------------------|
| [Feedback de validación] | [Cambio aplicado] |

---

## Aprobación <!-- Generado automáticamente por >validar_hu al aprobar -->

| Campo | Valor |
|-------|-------|
| **Estado** | ✅ Aprobada |
| **Aprobado por** | [Nombre del rol aprobador] |
| **Fecha aprobación** | [FECHA_ISO_8601] |
| **Nivel validación** | [basico \| completo \| exhaustivo] |
| **Notas** | [Resumen de validación o 'Sin observaciones'] |

---

## Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| [Fecha] | Refinamiento inicial | Iteración 1 |
| [Fecha] | Ajuste | Iteración N - Respuesta a validación |
