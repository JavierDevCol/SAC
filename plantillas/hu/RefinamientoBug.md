# Refinamiento Bug: [BUG-NNN] - [Título]

## Metadata

| Campo | Valor |
|-------|-------|
| **ID** | BUG-NNN |
| **Título** | [Título corto] |
| **Tipo** | Bug |
| **Proyecto** | [nombre-proyecto] |
| **Prioridad** | [P0 \| P1 \| P2 \| P3] |
| **Complejidad** | [🟢 BAJO \| 🟡 MEDIO \| 🔴 ALTO] |
| **Story Points** | [— \| X SP] |
| **Estimación** | [— \| Y horas] |
| **Fecha Creación** | [FECHA_ISO_8601] |
| **Creado por** | registrar_bug |
| **Detectado_en** | [HU-XXX \| contexto] |
| **Iteración** | 1 |
| **Modo** | Plano |

---

## 1. Descripción del Bug

[Descripción clara del problema: qué componentes están involucrados, cuál es la inconsistencia o fallo, y por qué ocurre]

---

## 2. Síntoma

[Comportamiento observable por el usuario o el sistema. Describir el flujo que falla paso a paso]

---

## 3. Causa Raíz

[Análisis técnico de por qué ocurre el bug. Incluir tablas comparativas si hay inconsistencias entre capas/componentes]

---

## 4. Archivos Afectados

| Archivo | Problema |
|---------|----------|
| `[ruta/archivo]` | [Descripción breve del problema en este archivo] |

---

## 5. Criterios de Aceptación

<!-- Para bugs, los CAs verifican que el bug se resuelve -->

- [ ] **CA-01:** Dado [contexto del bug], cuando [se ejecuta la acción que causaba el bug], entonces [el sistema se comporta correctamente]
- [ ] **CA-02:** Dado [contexto], cuando [se prueba el escenario], entonces [no se reproduce el síntoma]

---

## 6. Corrección Sugerida

**SUGERIDA** — Instrucciones de alto nivel para `planificar_hu`:

- **Qué cambiar:** [Descripción del cambio necesario]
- **En qué archivo(s):** [Lista de archivos a modificar]
- **Lógica esperada:** [Descripción de la lógica corregida]

> ⚠️ NO incluir código — solo instrucciones de alto nivel para planificar_hu

---

## 7. Corrección Aplicada

<!-- Se llena cuando el bug ya fue corregido (flag --ya_corregido) -->

**Commit fix:** [`tipo: mensaje del commit`]

```[lenguaje]
// Antes
- [código original]

// Después
+ [código corregido]
```

---

## 8. Lección Aprendida

[Qué se puede hacer para prevenir este tipo de bug en el futuro. Máximo 3 líneas. Recomendaciones concretas y accionables]

---

## 9. Desglose Técnico

<!-- Opcional: para bugs complejos que requieren planificación detallada -->

### Slice 1: [Nombre del slice mínimo]

| ID Tarea | Descripción | Capa | Estimación |
|----------|-------------|------|------------|
| BUG-NNN-API-01 | [Descripción] | API | [X]h |
| BUG-NNN-SVC-01 | [Descripción] | Servicio | [X]h |
| BUG-NNN-TEST-01 | [Descripción] | Testing | [X]h |

---

## 10. Estimación

<!-- Se llena cuando planificar_hu calcula la estimación -->

| Factor | Valor | Justificación |
|--------|-------|---------------|
| Complejidad base | [X] | [Razón] |
| Incertidumbre | [+Y] | [Razón] |
| Riesgo | [+Z] | [Razón] |
| **Total SP** | **[X+Y+Z]** | — |

---

## 11. Riesgos y Dependencias

### Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| [Riesgo 1] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Acción] |

### Dependencias

| Tipo | Referencia | Estado |
|------|------------|--------|
| HU previa | [HU-XXX] | [Estado] |
| API externa | [Nombre] | [Disponible/Pendiente] |

---

## Aprobación

<!-- Generado por >validar_hu al aprobar (bugs saltan validación directa) -->

| Campo | Valor |
|-------|-------|
| **Estado** | ✅ Aprobada (auto) |
| **Aprobado por** | registrar_bug |
| **Fecha aprobación** | [FECHA_ISO_8601] |
| **Notas** | Bug registrado con causa raíz documentada |

---

## Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| [Fecha] | Registro inicial | Bug documentado |
| [Fecha] | Corrección | Commit fix aplicado |

---

> **Archivo:** `{{artifacts.hu_folder}}/BUG-NNN/RefinamientoBug.md`
> **Creado por:** `>registrar_bug`
> **Actualizado por:** `>planificar_hu`, `>ejecutar_plan`
