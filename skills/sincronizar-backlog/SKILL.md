---
name: sincronizar-backlog
description: Sincroniza el backlog con el estado real de los artefactos en disco. Deduce estados desde archivos existentes y corrige discrepancias. Ejecuta esta skill cuando se necesite verificar o corregir el estado de las HUs en el backlog.
---

## Parámetros

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `id_hu` | string | null | Sincronizar solo una HU específica |
| `--proyecto` | string | null | Filtrar HUs de un proyecto (multi-proyecto) |
| `--auto` | flag | false | Aplicar correcciones sin confirmación |
| `--dry_run` | flag | false | Solo mostrar reporte, no aplicar cambios |
| `--resumen` | flag | false | Mostrar solo resumen de estados (lectura rápida) |

## Reglas de Deducción de Estados

La fuente de verdad son los **ARTEFACTOS en disco**, no el estado del backlog.

| Estado | Condición |
|--------|-----------|
| `[ ] Pendiente` | No existe refinamiento |
| `[R] Refinada` | Existe refinamiento SIN sección '## Aprobación' |
| `[A] Aprobada` | Refinamiento CON '## Aprobación' + '**Estado** \| ✅ Aprobada' |
| `[P] Planificada` | Existe Plan.md con Estado = 'PENDIENTE' |
| `[E] En Ejecución` | Plan.md con Estado = 'EN_PROGRESO' |
| `[X] Completada` | Plan.md con Estado = 'COMPLETADO' |
| `[B] Bloqueada` | Plan.md con Estado = 'BLOQUEADO' |

**Prioridad:** completada → bloqueada → en_ejecucion → planificada → aprobada → refinada → pendiente

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `artifacts.hu_folder`, `artifacts.contextos_folder`

### 2. Atajo Resumen Rápido (opcional)

**Condición:** `--resumen=true`

- Leer backlog, extraer '## 📊 Resumen de Estados' y '## 📇 Índice Rápido'
- Si `--proyecto` → Filtrar también 'Resumen por Proyecto'
- Mostrar resumen y **TERMINAR** (no escanear artefactos)

### 3. Cargar Backlog

- Leer `{archivos.backlog}`
- Extraer todas las HUs (patrón: `### [ID-HU]: [Título]`)
- Para cada HU: ID, Título, Tipo, Estado, Proyecto
- Si `--id_hu` → Filtrar solo esa HU
- Si `--proyecto` → Filtrar HUs de ese proyecto

### 4. Escanear Artefactos por HU

Para cada HU del backlog:

**4.1 Escanear carpeta padre:**
1. Buscar `{hu_folder}/[ID-HU]/Refinamiento.md`
2. Si existe → Buscar '## Aprobación' con '**Estado** | ✅ Aprobada'
3. Buscar `{hu_folder}/[ID-HU]/Plan.md`
4. Si existe plan → Leer campo '| **Estado** |'

**4.2 Escanear carpetas hijas (tasks):**
1. Buscar carpetas `{hu_folder}/[ID-HU]-TASK-*/`
2. Para cada task hija:
   - Leer `Refinamiento.md` → Verificar CAs granulares
   - Leer `Plan.md` → Verificar estado de la task
   - Registrar estado de cada task

**4.3 Aplicar reglas de deducción:**
- Para HU padre: usar reglas estándar
- Para tasks hijas: deducir estado desde sus propios artefactos

**4.4 Registrar:** `{id, estado_backlog, estado_deducido, artefactos, tasks[]}`

### 5. Generar Reporte de Discrepancias

Clasificar cada HU:
- ✅ **SINCRONIZADA** — estado_backlog == estado_deducido
- ⚠️ **DESINCRONIZADA** — estado_backlog != estado_deducido
- ❓ **HUÉRFANA** — HU en backlog sin artefactos (y no es Pendiente)

**Si `--dry_run=true` → Mostrar reporte y TERMINAR**

### 6. Solicitar Confirmación

**Condición:** `--auto=false` AND hay discrepancias

> 🤷 ¿Aplicar las correcciones?
> - ✅ [S] Sí, aplicar todas
> - 🔍 [P] Seleccionar cuáles aplicar
> - ❌ [N] No aplicar cambios

### 7. Aplicar Correcciones al Backlog

Para cada HU a corregir:
1. Buscar sección `### [ID-HU]` en el backlog
2. Actualizar campo `- **Estado:**` al estado deducido
3. Actualizar campos adicionales según estado:
   - `[R]`: Refinamiento, Fecha, Estimación
   - `[A]`: Fecha aprobación, Aprobado por
   - `[P]`: Plan, Fecha planificación
   - `[E]`: Inicio ejecución, Progreso
   - `[X]`: Completado, Duración
4. Si Multi-Proyecto → Recalcular contadores
5. Recalcular 'Resumen de Estados'

### 8. Regenerar Índice Rápido

- Localizar '## 📇 Índice Rápido' en el backlog
- Regenerar tabla completa recorriendo TODAS las HUs
- Para cada HU: ID, Título, Estado (corregido), Prioridad, Tipo
- Reemplazar tabla existente

### 9. Reporte Final

- Mostrar resumen de cambios aplicados
- Actualizar 'Última Actualización' del backlog con timestamp

## Restricciones

- **NUNCA** modificar estados sin evidencia en artefactos
- Mostrar reporte de discrepancias **ANTES** de aplicar cambios
- Solicitar confirmación antes de sobrescribir estados
- La fuente de verdad son los **ARTEFACTOS**, no el backlog

## Formato de salida

```
✅ SINCRONIZACIÓN COMPLETADA

📊 Resumen:
- HUs escaneadas: [N]
- Correcciones aplicadas: [X]
- Sin cambios: [Y]

📁 Backlog actualizado: {archivos.backlog}
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Backlog no encontrado | No existe | Ejecutar >refinar_hu para crear backlog |
| HU no encontrada | ID incorrecto | Verificar ID con la lista de HUs |
| Artefacto corrupto | Estructura incorrecta | Revisar manualmente el archivo |
| Estado ambiguo | Artefactos no coinciden | Revisar manualmente |

## Después de ejecutar

- `>refinar_hu [ID-HU]` — Refinar HUs en estado Pendiente
- `>validar_hu [ID-HU]` — Validar HUs Refinadas
- `>planificar_hu [ID-HU]` — Planificar HUs Aprobadas
