---
name: ejecutar-plan
description: Ejecuta planes de implementación para HUs. Soporta modos completo, fase_por_fase, tarea_por_tarea, task_por_task y task_especifica. Actualiza Plan.md en tiempo real. Ejecuta esta skill cuando una HU esté en estado [P] Planificada y necesite implementarse.
---

## Parámetros

| Parámetro | Tipo | Default | Valores posibles | Descripción |
|-----------|------|---------|------------------|-------------|
| `id_hu` | string | — | Ej: `HU-001`, `HU-012` | Identificador de la HU a implementar |
| `--proyecto` | string | null | Ej: `mi-app`, `backend` | Proyecto específico (auto-detectado) |
| `--modo_ejecucion` | option | `fase_por_fase` | `completo`, `fase_por_fase`, `tarea_por_tarea`, `task_por_task`, `task_especifica` | Cómo ejecutar el plan |
| `--task_id` | string | null | Ej: `HU-001-TASK-1`, `HU-012-TASK-3` | ID de task a ejecutar (solo con `task_especifica`) |
| `--auto_commit` | flag | false | `--auto_commit` (activar) | Commit automático sin confirmación |

## Modos de Ejecución

| Modo | HU Plana | HU Particionada |
|------|----------|-----------------|
| `completo` | Ejecuta todo sin pausas | Tasks secuenciales sin pausas |
| `fase_por_fase` | Pausa entre fases | Degradado a `task_por_task` |
| `tarea_por_tarea` | Pausa en cada tarea | Pausa en cada tarea técnica |
| `task_por_task` | Degradado a `fase_por_fase` | Pausa entre tasks |
| `task_especifica` | ⛔ Error | Ejecuta solo una task |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `archivos.reglas_arquitectonicas`, `artifacts.hu_folder`, `artifacts.lecciones_aprendidas`, `plantillas.hu.tracking`
- Leer `.SAC/config/CONFIG_USER.yaml`
- Si existe `{archivos.reglas_arquitectonicas}` → Cargar reglas para aplicar durante implementación:
  - Nomenclatura (nombres de clases, métodos, variables)
  - Estructura de carpetas (domain/, application/, infrastructure/)
  - Patrones obligatorios y prohibidos
  - Nivel de SOLID
  - Política de nulls e inmutabilidad
  - Límites de código (líneas por método/clase)

### 2. Cargar Plan de Implementación

- Verificar que existe `{hu_folder}/[ID-HU]/`
- Leer `{hu_folder}/[ID-HU]/HU.md` y `{hu_folder}/[ID-HU]/Plan.md`
- Verificar que Plan.md tiene campo 'Estado' = 'PENDIENTE'
- Cargar `{artifacts.lecciones_aprendidas}` (si existe)
- Cambiar estado HU a [E] En Ejecución
- Actualizar Plan.md: Estado → 'EN_PROGRESO'
- Crear Tracking.md si no existe

### 3. Resolver Modo de Ejecución

**Validaciones de combinación:**
- `completo` + `auto_commit=true` → ⛔ Prohibido (sin supervisión humana)
- `task_id` + `task_especifica` no activo → ⚠️ task_id ignorado
- `task_especifica` sin task_id → Listar tasks disponibles

**Degradación de modos:**

| Modo pedido | HU Plana | HU Particionada |
|-------------|----------|-----------------|
| `fase_por_fase` | ✅ Funciona | ⚠️ Degradado a `task_por_task` |
| `task_por_task` | ⚠️ Degradado a `fase_por_fase` | ✅ Funciona |
| `task_especifica` | ⛔ Error | ✅ Funciona |

**Para `task_especifica`:**
- Si task_id proporcionado → Verificar dependencias satisfechas
- Si task_id no proporcionado → Listar tasks con estado de ejecutabilidad

### 4. Validar Entorno y Preparar Rama

**Cargar reglas arquitectónicas** (si existen):
- Leer `{archivos.reglas_arquitectonicas}` para aplicar durante la implementación
- Si no existen → Usar mejores prácticas estándar del stack

**Preparar rama Git:**
- Preguntar al usuario: "¿De qué rama debo crear la rama de trabajo?"
  > - [M] main/master
  > - [D] develop
  > - [O] Otra rama (especificar)
- Crear rama de trabajo: `feature/[ID-HU]-[descripcion-corta]`
- Cambiar a la nueva rama

**Validar entorno:**
- Detectar framework de tests (mvn/npm/pytest/vitest/jest/etc.)
- Verificar dependencias instaladas
- Crear backup: `git stash push -m 'backup/[ID-HU]_pre_ejecucion'` (si hay cambios sin commit)

### 5. Ejecutar Plan

**Modo Plano:**
Para cada fase:
1. Anunciar inicio de fase
2. Para cada tarea:
   a. EDITAR Plan.md: `[PENDIENTE]` → `[EN_PROGRESO]`
   b. Ejecutar pasos (crear/modificar código) **aplicando reglas arquitectónicas cargadas en paso 1**:
      - Nomenclatura de clases, métodos, variables
      - Estructura de carpetas
      - Patrones obligatorios y prohibidos
      - Nivel de SOLID
      - Límites de código
   c. EDITAR Plan.md: `- [ ]` → `- [X]` por cada paso
   d. EDITAR Plan.md: `[EN_PROGRESO]` → `[EJECUTADA]`
   e. **Commit por tarea:** `feat([ID-HU]-EJEC-NN): [descripción de la tarea]`
   f. Agregar fila en 'Historial de Ejecución'
   g. Actualizar progreso en 'Progreso General'

**Modo Particionada:**
Para cada task funcional:
1. Anunciar: `═══ Task [ID-HU]-TASK-N: [Título] ═══`
2. Verificar dependencias en [EJECUTADA]
3. Para cada fase interna → Para cada tarea técnica:
   - Actualizar estado en Plan.md de la task
   - Ejecutar código
   - Actualizar progreso
4. Validar CAs granulares: `[ ]` → `[~]` candidato
5. **Commit por task:** Generar commit con mensaje: `feat([ID-HU]-TASK-N): [descripción de la task]`
6. Si `task_por_task` → Pausa de confirmación
7. Si `task_especifica` → Finalizar tras completar

**CRÍTICO:** EDITAR Plan.md en CADA transición. Si el archivo no refleja el estado actual, la ejecución es inválida.

**Reanudación:**
- Si hay tareas [EJECUTADA], saltar a la primera [PENDIENTE]
- Verificar que archivos generados existen en filesystem

**Máximo 2 reintentos por tarea.** Si falla 2 veces → DETENER.

### 6. Validar Criterios de Aceptación (Sub-agente)

**Delegar a sub-agente validador-calidad:**

**Modo Plano:**
- Sub-agente ejecuta: `>validar_ca [ID-HU] --scope todos`
- Retorna: PASS/FAIL + detalle por CA

**Modo Particionada:**
- `task_especifica`: Sub-agente ejecuta `>validar_ca [ID-HU] --task_id [task_id] --scope granulares`
- `completo`/`task_por_task`:
  - Sub-agente 1: Validar CAs granulares de cada task completada
  - Sub-agente 2: Validar CAs de integración al final (cuando todas las tasks estén [EJECUTADA])

**Si FAIL → DETENER.** Revisar código antes de continuar.

### 7. Commit Final

**Condición:** Solo al final de TODA la HU (no por task — esas ya tienen commit propio)

- Mostrar resumen de cambios
- Preguntar: ¿Proceder con commit final?
- Si SÍ → Generar mensaje: `feat([ID-HU]): implementación completa de [título]`
- Si NO → Pausar para revisión

### 8. Finalización

- Verificar que TODAS las tareas están en [EJECUTADA]
- **Si `task_especifica` y quedan tasks pendientes:**
  - NO completar la HU
  - Mostrar progreso y siguiente task
- **Si todo completado:**
  - Plan.md: Estado → 'COMPLETADO'
  - Tracking.md: Estado → 'FINALIZADO'
  - Backbone índice: [E] → [X]

## Restricciones

- Ejecutar tareas en **ORDEN ESTRICTO**
- **DETENERSE** inmediatamente ante cualquier error
- **NO** improvisar ni saltar tareas
- **ACTUALIZAR** plan en tiempo real: `[ ]` → `[X]`
- Respetar dependencias entre tasks
- Delegar compilación y tests a sub-agente
- **Aplicar reglas arquitectónicas** cargadas en paso 1
- **Commit por task:** Cada task funcional tiene su propio commit para historial limpio
- **Commit final:** Solo al completar TODA la HU

## Formato de salida

**Tarea completada:**
```
✅ [EJECUTADA] TASK-1-EJEC-01: [nombre]
   Archivos: [lista]
   Tests: ✅ Pasando
```

**Task completada (modo task_especifica):**
```
✅ TASK COMPLETADA: [task_id]
📊 Tareas: [M/M] | CAs: [Y/Y] | Tests: ✅
📈 Progreso HU: [T_completadas/T_total] tasks
▶️ Siguiente: >ejecutar_plan [ID-HU] --modo_ejecucion task_especifica --task_id [siguiente]
```

**Implementación completa:**
```
✅ IMPLEMENTACIÓN COMPLETADA: [ID-HU]
📊 Tasks: [T/T] | Tareas: [M/M] | CAs: [Y/Y]
✅ Tests: Pasando
Siguiente: >validar_ca [ID-HU]
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Plan no encontrado | No existe Plan.md | Ejecutar >planificar_hu primero |
| Plan no está PENDIENTE | Ya en ejecución o completado | Verificar flujo de estados |
| Error de compilación | Código con errores | Revisar código generado |
| Tests fallando | Lógica o tests incorrectos | Revisar lógica o actualizar tests |

## Después de ejecutar

- `>validar_ca [ID-HU]` — Validar CAs contra código
