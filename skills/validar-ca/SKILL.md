---
name: validar-ca
description: Valida criterios de aceptación contra código implementado y tests. Soporta validación granular por task, integración y todos. Actualiza estado en Plan.md y Refinamiento.md. Ejecuta esta skill para verificar que el código cumple los CAs del refinamiento.
---

## Parámetros

| Parámetro | Tipo | Default | Valores posibles | Descripción |
|-----------|------|---------|------------------|-------------|
| `id_hu` | string | — | Ej: `HU-001`, `HU-012` | Identificador de la HU a validar |
| `--task_id` | string | null | Ej: `HU-001-TASK-1`, `HU-012-TASK-3` | ID de task funcional (requerido para scope=granulares) |
| `--scope` | option | `todos` | `granulares`, `integracion`, `todos` | Qué CAs validar |

## Scopes de Validación

| Scope | Descripción | Requisito |
|-------|-------------|-----------|
| `granulares` | CAs granulares de una task específica | Requiere `--task_id` |
| `integracion` | CAs de integración (padre) | Todas las tasks en [EJECUTADA] |
| `todos` | Granulares de todas las tasks + integración | — |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `artifacts.hu_folder`

### 2. Cargar Fuentes de Datos

- Verificar que existe `{hu_folder}/[ID-HU]/`
- Cargar `{hu_folder}/[ID-HU]/Refinamiento.md` (fuente de verdad de CAs)
- Cargar `{hu_folder}/[ID-HU]/Plan.md` (estado de verificación)
- Cargar `{hu_folder}/[ID-HU]/HU.md`
- Extraer campo 'Modo' del plan: [Plano | Particionada]
- **Si Modo = Plano Y task_id != null** → ⛔ Error: HU plana no tiene tasks

### 3. Determinar CAs a Validar

**Modo Plano:**
- Extraer CAs de '## 2. Criterios de Aceptación' del refinamiento
- `cas_a_validar = todos los CAs`

**Modo Particionada:**

| Scope | CAs a validar | Prerequisito |
|-------|---------------|--------------|
| `granulares` | CAs granulares de la task indicada | Requiere task_id |
| `integracion` | CAs de integración (padre) | Todas las tasks [EJECUTADA] |
| `todos` | Granulares de TODAS + integración | Tasks completadas para integración |

### 4. Validar Cada CA contra Código y Tests

**Delegar a sub-agente validador-calidad:**

Para cada CA:
1. Sub-agente recibe: CA + rutas de archivos + rutas de tests
2. Sub-agente valida contra código real en filesystem
3. Sub-agente retorna: PASS/FAIL + evidencia

**Veredictos:**
- ✅ **CUMPLIDO:** PASS
- ⚠️ **PARCIAL:** PASS con observaciones
- ❌ **NO CUMPLIDO:** FAIL

**⛔ DETENER al primer CA con veredicto ❌**

### 5. Actualizar Estado en Plan

**EDITAR Plan.md:**

| Modo | Scope | Acción |
|------|-------|--------|
| Plano | — | `[ ]` → `[X]` en 'Fase Final: Validar CAs' |
| Particionada | granulares | `[ ]` → `[X]` en '### Validar CAs de TASK-N' |
| Particionada | integracion | `[~]` → `[X]` en 'Fase Final: Validar CAs de Integración' |

**Propagación ascendente:**
```
CAs granulares TASK-N todos [X]
    ↓
CA de integración padre → [~] candidato
    ↓
>validar_ca --scope integracion confirma [~] → [X]
    ↓
Todos los CAs padre en [X]
    ↓
HU completada [X]
```

**EDITAR Refinamiento.md:** Marcar `[ ]` → `[X]` en CAs validados

### 6. Emitir Reporte

Generar reporte compacto con resultado por CA.

## Restricciones

- Leer CAs **SIEMPRE** desde el refinamiento (fuente de verdad), NUNCA del plan
- Verificar cada CA contra el código real en el filesystem y tests
- Marcar estado en el plan (checkboxes), NO en el refinamiento
- **DETENER** ante el primer CA no cumplido
- Distinguir CAs granulares de CAs de integración
- Delegar validación a sub-agente

## Formato de salida

**Validación completa:**
```
✅ VALIDACIÓN DE CAs COMPLETADA: [ID-HU] [scope]
📊 CAs validados: [X/Y] ✅ | Parciales: [P] ⚠️ | No cumplidos: [F] ❌

| CA | Veredicto | Evidencia |
|----|-----------|-----------|
| CA-01 | ✅ | test_auth.py::test_register |
| CA-02 | ⚠️ | api/register.py (falta validación email) |
```

**Validación parcial (task_especifica):**
```
⚠️ VALIDACIÓN PARCIAL: [ID-HU] Task [task_id]
📊 CAs granulares: [X/Y] ✅
📈 Pendientes CAs integración: ejecutar >validar_ca --scope integracion cuando todas las tasks estén completas
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Refinamiento no encontrado | No refinada | Verificar que la HU fue refinada |
| Plan no encontrado | No planificada | Ejecutar >planificar_hu primero |
| No hay código implementado | No ejecutada | Ejecutar >ejecutar_plan primero |
| Tasks pendientes para integración | Tasks incompletas | Completar todas las tasks primero |

## Después de ejecutar

- `>ejecutar_plan [ID-HU] --modo_ejecucion task_especifica --task_id [siguiente]` — Continuar con siguiente task
