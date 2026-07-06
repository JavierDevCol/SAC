---
name: refinar-hu
description: Refina Historias de Usuario con criterios de aceptación SMART, desglose técnico vertical, estimación y análisis de riesgos. Soporta modo plano y particionado con tasks funcionales. Ejecuta esta skill cuando el usuario proporcione una HU para refinamiento o solicite refinar una HU existente.
---

## Parámetros

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `id_hu` | string | — | Identificador de la HU a refinar |
| `--proyecto` | string | null | Proyecto destino (requerido en multi-proyecto) |
| `--formato_estimacion` | string | `ambos` | `story_points`, `horas`, `ambos` |
| `--nivel_detalle` | string | `medio` | `alto`, `medio`, `bajo` |
| `--incluir_riesgos` | boolean | true | Incluir análisis de riesgos |
| `--generar_tareas` | boolean | true | Generar desglose técnico |
| `--incluir_testing` | boolean | true | Incluir testing en estimación |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.workspace`, `archivos.backlog`, `artifacts.hu_folder`, `artifacts.contextos_folder`, `plantillas.hu.*`
- Leer `.SAC/config/CONFIG_USER.yaml` (si existe) → obtener idioma, proyecto
- Verificar que existe contexto del proyecto
- Si NO existe contexto → Informar: "Necesito conocer el proyecto primero. Ejecuta >tomar_contexto"

### 2. Detectar Tipo de Workspace

- Leer `{archivos.workspace}` y extraer campo 'Tipo'
- **Multi-Proyecto:** Si parámetro `--proyecto` no especificado → PREGUNTAR proyecto destino. Validar que existe. Cargar contexto desde `{contextos_folder}/[proyecto]_contexto.md`
- **Mono-Proyecto:** Ignorar parámetro `--proyecto`, usar proyecto único. Cargar contexto

### 3. Detectar Modo de Operación

- Verificar si existe `{hu_folder}/[ID-HU]/`
- Si existe con Refinamiento.md → **MODO_AJUSTE** (re-refinamiento)
- Si no existe → **MODO_NUEVO**
- Extraer campo 'Tipo' de la HU (si no existe → asumir Funcional)
- **SI Tipo = Bug:**
  1. Cargar `{hu_folder}/[ID-HU]/RefinamientoBug.md`
  2. Pre-poblar desglose con archivos afectados del bug
  3. Pre-poblar CA: "El bug BUG-NNN no se reproduce tras la corrección"
  4. Incorporar Causa Raíz y Corrección Sugerida si existen
  5. Reducir preguntas de clarificación

### 4. Evaluación de Complejidad

Clasificar según matriz:

| Nivel | Indicadores | Preguntas | Tareas | SP |
|-------|-------------|-----------|--------|-----|
| 🟢 BAJO | CRUD básico, sin integraciones | 1-2 | 3-5 | 2-3 |
| 🟡 MEDIO | Lógica moderada, 1-2 integraciones | 3-5 | 5-10 | 5-8 |
| 🔴 ALTO | Múltiples integraciones, impacto arquitectónico | 6-10+ | 10-20 | 13+ |

### 5. Evaluación de Partición en Tasks

**Condición:** complejidad >= MEDIO AND CAs >= 3

Analizar si la HU contiene múltiples objetivos funcionales independientes:
- CAs que agrupan funcionalidades distintas
- >5 CAs en total
- Slices que podrían entregarse independientemente
- Estimación >= 8 SP

**SI se detecta partición → Proponer al usuario:**
> 📦 Esta HU tiene [N] objetivos funcionales independientes.
> 💡 Recomiendo particionarla en [M] tasks funcionales:
> - TASK-1: [Objetivo 1] (CAs: CA-01, CA-02)
> - TASK-2: [Objetivo 2] (CAs: CA-03, CA-04)
>
> 🤷 ¿Aceptas la partición?
> - ✅ [S] Sí, particionar
> - ✏️ [E] Editar partición
> - ❌ [N] No, mantener formato plano

**La partición es una SUGERENCIA, nunca obligatoria.**

### 6. Preguntas de Clarificación

- Delegar a sub-agente: analizar CAs buscando ambigüedades
- Si hay ambigüedades → Generar preguntas priorizadas:
  - **Alta:** afectan estimación
  - **Media:** mejoran UX
  - **Baja:** detalles de implementación

### 7. Refinamiento de Criterios de Aceptación

- Aplicar criterios SMART a cada CA:
  - **S** (Específico): qué debe ocurrir exactamente
  - **M** (Medible): métricas verificables
  - **A** (Alcanzable): realista en el sprint
  - **R** (Relevante): relacionado con objetivo
  - **T** (Temporal): condiciones de tiempo
- Reformular CA ambiguos
- Agregar CA faltantes (error, validación, performance)

### 8. Desglose Técnico Vertical

**Modo Plano** (sin partición):
- Identificar slices end-to-end mínimos
- Generar tareas por slice: frontend→api→servicio→persistencia→testing
- IDs: HU-XXX-UI-01, HU-XXX-API-01

**Modo Particionado** (con tasks):
Para cada Task funcional:
1. Definir CAs de integración (resumen del objetivo)
2. Definir CAs granulares (verificables de forma aislada)
3. Generar desglose técnico por capa DENTRO de cada task
4. Asignar IDs: [ID-HU]-TASK-N para tasks, [ID-HU]-TASK-N-API-01 para tareas

Estructura jerárquica (cada task tendrá su propia carpeta):
```
HU-001/                              ← HU padre
├── HU.md
└── Refinamiento.md
    ├── CA-01 (integración) → traza a HU-001-TASK-1
    ├── CA-02 (integración) → traza a HU-001-TASK-2
    ├── HU-001-TASK-1 (sección en Refinamiento.md del padre)
    │   ├── CA-TASK1-01 (granular)
    │   └── Desglose: API-01, SVC-01, DB-01, TEST-01
    └── HU-001-TASK-2 (sección en Refinamiento.md del padre)
        ├── CA-TASK2-01 (granular)
        └── Desglose: API-01, SVC-01, TEST-01

HU-001-TASK-01/                      ← Task hija (carpeta individual)
├── HU.md                            ← Campo "Padre: HU-001"
└── Refinamiento.md                  ← CAs granulares + desglose de la task

HU-001-TASK-02/                      ← Task hija (carpeta individual)
├── HU.md                            ← Campo "Padre: HU-001"
└── Refinamiento.md                  ← CAs granulares + desglose de la task
```

**Regla de trazabilidad:**
- CAs granulares TASK-N completadas → CA-[N] padre → [~] candidato
- `>validar_ca --scope integracion` confirma [~] → [X]
- Todas las CAs padre en [X] → HU completada

### 9. Estrategia y Estimación

- Recomendar enfoque: TDD, incremental, feature toggle
- Calcular Story Points: complejidad + incertidumbre + riesgo
- Si `--formato_estimacion=horas` o `ambos` → Convertir SP a horas

### 10. Análisis de Riesgos

**Condición:** `--incluir_riesgos=true`

- Identificar bloqueadores potenciales
- Proponer mitigaciones
- Detectar dependencias de otras HUs

### 11. Persistencia del Refinamiento

**Modo Nuevo:**
- Crear `{archivos.backlog}` desde plantilla si no existe
- Crear `{hu_folder}/[ID-HU]/` si no existe
- Copiar plantillas: HU.md, Refinamiento.md
- Rellenar Metadata en HU.md (ID, Título, Tipo, Proyecto, Prioridad, etc.)
- Rellenar Metadata en Refinamiento.md (Iteración: 1)
- **Si particionada:**
  - Agregar campo 'Tasks' en HU.md y Refinamiento.md
  - **Crear carpeta por cada task funcional:**
    - `{hu_folder}/[ID-HU]-TASK-1/` con HU.md + Refinamiento.md
    - `{hu_folder}/[ID-HU]-TASK-2/` con HU.md + Refinamiento.md
    - `{hu_folder}/[ID-HU]-TASK-N/` con HU.md + Refinamiento.md
  - **Cada task hija tiene:**
    - `HU.md` → Campo `**Padre:** [ID-HU]`, metadata de la task
    - `Refinamiento.md` → CAs granulares + desglose técnico de la task
- Determinar proyecto de la HU:
  - SI parámetro `--proyecto` especificado → usar ese valor
  - SI Mono-Proyecto → usar nombre del proyecto único
  - SI Multi-Proyecto sin parámetro → PREGUNTAR al usuario
- Actualizar backbone índice: agregar fila en Índice Rápido con estado [R]
- SI Multi-Proyecto → Actualizar sección 'Resumen por Proyecto' en backlog

**Modo Ajuste:**
- Actualizar `{hu_folder}/[ID-HU]/Refinamiento.md` existente
- Si particionada → Actualizar también Refinamiento.md de cada task hija
- Incrementar campo Iteración en Metadata
- Marcar observaciones resueltas: [ ] → [x]

## Restricciones

- **NUNCA** aceptar criterios de aceptación no medibles
- Usar desglose **VERTICAL** (end-to-end), nunca horizontal
- Evaluar partición solo para complejidad MEDIO o ALTO
- **NO** forzar partición en HUs de complejidad BAJO (2-3 SP)
- Delegar detección de ambigüedades a sub-agente
- Crear carpeta `{hu_folder}/[ID-HU]/` si no existe
- Usar plantillas desde `plantillas.hu.hu` y `plantillas.hu.refinamiento`

## Formato de salida

**HU Plana:**
```
✅ REFINAMIENTO COMPLETADO: [ID-HU]
📁 Carpeta: {hu_folder}/[ID-HU]/
📄 Archivos: HU.md, Refinamiento.md
📊 CA: [X] mejorados + [Y] nuevos | SP: [Z] | Riesgos: [N]
Siguiente: >validar_hu [ID-HU]
```

**HU Particionada:**
```
✅ REFINAMIENTO COMPLETADO: [ID-HU]
📁 Carpeta padre: {hu_folder}/[ID-HU]/
📄 Archivos: HU.md, Refinamiento.md
📊 CA: [X] integración | SP: [Z] | Riesgos: [N]
📦 Tasks: [M] carpetas creadas
   ├── {hu_folder}/[ID-HU]-TASK-1/  (SP: [X])
   ├── {hu_folder}/[ID-HU]-TASK-2/  (SP: [Y])
   └── {hu_folder}/[ID-HU]-TASK-N/  (SP: [Z])
Siguiente: >validar_hu [ID-HU]
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| HU incompleta o mal formateada | Formato incorrecto | Solicitar: Como [rol], quiero [func], para [beneficio] |
| HU sin criterios de aceptación | CA faltantes | Generar CA básicos inferidos, solicitar validación |
| HU tamaño épica | Demasiado grande | Sugerir partición en HUs más pequeñas |
| Proyecto no encontrado | Nombre incorrecto | Verificar en workspace.md |

## Después de ejecutar

- `>validar_hu [ID-HU]` — Validación arquitectónica de la HU refinada
