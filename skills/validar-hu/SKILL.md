---
name: validar-hu
description: Valida HUs refinadas contra reglas arquitectónicas, criterios de aceptación y dependencias. Emite veredicto de aprobación, ajustes, bloqueo o rechazo. Ejecuta esta skill cuando una HU esté en estado [R] Refinada y necesite validación antes de planificar.
---

## Parámetros

| Parámetro | Tipo | Default | Valores posibles | Descripción |
|-----------|------|---------|------------------|-------------|
| `id_hu` | string | — | Ej: `HU-001`, `HU-012` | Identificador de la HU a validar |
| `--proyecto` | string | null | Ej: `mi-app`, `backend` | Proyecto específico (auto-detectado) |
| `--nivel_validacion` | option | `completo` | `basico`, `completo`, `exhaustivo` | Profundidad de la validación |

## Veredictos

| Veredicto | Estado | Siguiente |
|-----------|--------|-----------|
| APROBADA | `[A] Aprobada` | `>planificar_hu [ID-HU]` |
| AJUSTES | `[R] Refinada + observaciones` | `>refinar_hu [ID-HU]` |
| BLOQUEADA | `[B] Bloqueada` | Resolver dependencia → revalidar |
| RECHAZADA | `[B] Bloqueada` | Requiere rediseño significativo |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `artifacts.hu_folder`, `artifacts.contextos_folder`, `artifacts.adr_folder`
- Leer `.SAC/config/CONFIG_USER.yaml` (si existe) → obtener idioma

### 2. Cargar HU y Contexto

- Verificar que existe `{hu_folder}/[ID-HU]/`
- Leer `{hu_folder}/[ID-HU]/HU.md`
- Leer `{hu_folder}/[ID-HU]/Refinamiento.md`
- Verificar que Refinamiento.md NO tiene sección '## Aprobación' (ya aprobada)
- Extraer campo 'Tipo' de la HU (si no existe → asumir Funcional)
- **SI Tipo = Bug y severidad Crítica:**
  - Aplicar `nivel_validacion='basico'` automáticamente
  - Informar: "⚡ Bug crítico detectado — validación acelerada activa"
- Extraer campo 'Proyecto' de la HU
- **SI Proyecto = 'compartida':** Cargar contextos de todos los proyectos afectados
- **SI Proyecto = [nombre]:** Cargar contexto desde `{contextos_folder}/[proyecto]_contexto.md`
- **SI HU tiene campo ADR_Ref:** Cargar ADR referenciado desde `{adr_folder}`

### 3. Validación de Criterios de Aceptación

**Ejecutar en paralelo con múltiples sub-agentes:**

**Sub-agente 1 — Ambigüedades:**
- Analizar CAs buscando ambigüedades, vaguedades o suposiciones
- Retornar: SIN_AMBIGÜEDADES / CON_AMBIGÜEDADES + lista de preguntas

**Sub-agente 2 — SMART + Cobertura:**
- Verificar que cada CA cumple criterios SMART:
  - **S** (Específico): qué debe ocurrir exactamente
  - **M** (Medible): métricas verificables
  - **A** (Alcanzable): realista en el sprint
  - **R** (Relevante): relacionado con objetivo
  - **T** (Temporal): condiciones de tiempo
- Validar cobertura: casos de error, validación, performance

**Sub-agente 3 — Trazabilidad (solo si Modo=Particionada):**
- Verificar que cada CA del padre tiene traza a una Task
- Verificar que cada Task tiene CAs granulares verificables
- Verificar cadena de satisfacción: CAs granulares TASK-N → CA-[N] padre

**Consolidar resultados:**
- Si hay ambigüedades → Listar preguntas claras y específicas
- **PAUSAR** y esperar respuestas del usuario antes de continuar
- **Si Modo=Plano y complejidad >= MEDIO y CAs >= 6:**
  - Sugerir partición (es sugerencia, no bloqueo)

### 4. Validación contra ADR 

**Condición:** HU tiene ADR_Ref definido (no 'ninguno')

- Leer sección '## Decisión' del ADR referenciado
- Verificar que la HU implementa la decisión correctamente
- Detectar contradicciones entre HU y ADR
- Si hay contradicción → Agregar a observaciones

### 5. Validación Arquitectónica

**Nota:** Valida la HU como REQUISITO, no define implementación

- Delegar a sub-agente: verificar que la HU respeta reglas arquitectónicas
- Si FAIL → Agregar violaciones a observaciones
- Checklist:
  - Funcionalidad respeta separación de responsabilidades
  - CA no imponen decisiones técnicas que violen arquitectura
  - No cruza boundaries entre módulos/capas indebidamente
  - Coherente con contexto técnico documentado
  - No contradice ADRs previos

### 6. Verificación de Dependencias

- Extraer dependencias explícitas (APIs, HUs prerequisito, recursos)
- Verificar en backlog si HUs dependientes están en [X] Completada
- Verificar si endpoints/APIs requeridos existen
- **Si hay dependencias no resueltas → Clasificar:**
  - `DEPENDENCIA_HU`: Requiere otra HU completada
  - `DEPENDENCIA_EXTERNA`: Requiere sistema/API externa
  - `DECISION_PENDIENTE`: Requiere ADR
  - `RECURSO_NO_DISPONIBLE`: Falta infraestructura
- **Si bloqueante → Veredicto BLOQUEADA** (no continuar a viabilidad)

### 7. Análisis de Viabilidad Técnica

- Evaluar complejidad de implementación
- Identificar riesgos técnicos
- Validar estimación propuesta

### 8. Emisión de Veredicto

Determinar resultado: **APROBADA | AJUSTES | BLOQUEADA | RECHAZADA**

### 9. Persistir Resultado

**Si APROBADA:**
- Agregar sección '## Aprobación' en Refinamiento.md:

```markdown
## Aprobación

| Campo | Valor |
|-------|-------|
| **Estado** | ✅ Aprobada |
| **Aprobado por** | {nombre usuario} |
| **Fecha aprobación** | [FECHA_ISO_8601] |
| **Nivel validación** | [nivel usado] |
| **Notas** | [resumen o 'Sin observaciones'] |

### Directrices de Planificación
- **Fases sugeridas:** [estilo y orden de fases]
- **Componentes clave:** [componentes a crear/modificar]
- **Dependencias entre HUs:** [HUs prerequisito]
- **Riesgos a mitigar:** [riesgos detectados]
- **Notas adicionales:** [ADRs, patrones, consideraciones]
```

- Actualizar backbone índice: [R] → [A]

**Si AJUSTES:**
- Agregar sección '## Feedback de Validación' en Refinamiento.md
- Incluir fecha, iteración, observaciones pendientes [ ]

**Si BLOQUEADA:**
- Agregar sección '## Bloqueo de Validación' en Refinamiento.md:

```markdown
## Bloqueo de Validación

| Campo | Valor |
|-------|-------|
| **Estado** | 🚫 Bloqueada |
| **Tipo bloqueo** | [TIPO] |
| **Bloqueado por** | [descripción] |
| **Acción requerida** | [qué debe ocurrir] |
| **Fecha bloqueo** | [FECHA_ISO_8601] |
```

- Actualizar backbone índice: [R] → [B]

## Restricciones

- **NO** aprobar HU que violen principios arquitectónicos
- Documentar razones de rechazo o ajustes requeridos
- Verificar dependencias antes de aprobar
- Delegar validación arquitectónica a sub-agente
- **NUNCA** asumir — ante duda, preguntar al usuario

## Formato de salida

**APROBADA:**
```
✅ HU APROBADA: [ID-HU]
✓ CA | ✓ Arquitectura | ✓ Viabilidad
Siguiente: >planificar_hu [ID-HU]
```

**AJUSTES:**
```
⚠️ HU REQUIERE AJUSTES: [ID-HU]
Feedback en: {hu_folder}/[ID-HU]/Refinamiento.md
Siguiente: >refinar_hu [ID-HU]
```

**BLOQUEADA:**
```
🚫 HU BLOQUEADA: [ID-HU]
Tipo: [TIPO_BLOQUEO]
Motivo: [dependencia no resuelta]
Acción requerida: [qué debe ocurrir]
Revalidar: >validar_hu [ID-HU] (cuando se resuelva)
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| HU no encontrada | ID incorrecto | Verificar ID y ejecutar *HU para listar |
| HU no está en estado [R] | No refinada | Ejecutar >refinar_hu primero |
| Sin reglas arquitectónicas | No configuradas | Validación con mejores prácticas generales |

## Después de ejecutar

- `>planificar_hu [ID-HU]` — Si APROBADA
- `>refinar_hu [ID-HU]` — Si AJUSTES
- `>validar_hu [ID-HU]` — Si BLOQUEADA (cuando se resuelva)
