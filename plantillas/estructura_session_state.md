# 📦 Estructura del Archivo `session_state.json`

> **Versión:** 3.0  
> **Fecha de Actualización:** 5 de enero de 2026  
> **Estado:** Activo - Simplificado según principio de mínima complejidad

Este documento describe la estructura oficial del archivo `session_state.json` utilizado por el Sistema COCHAS para mantener el estado de la sesión, tracking de HUs y contexto entre roles.

---

## 🎯 Propósito

El `session_state.json` es el **archivo central de estado** que permite:
- Persistir información entre cambios de rol
- Trackear el progreso de HUs a través del ciclo de vida
- Registrar eventos clave y herramientas utilizadas
- Mantener contexto de ejecución activa

---

## 📋 Estructura Base (Esqueleto)

```json
{
  "version": "3.0",
  "timestamp": "string ISO 8601",
  
  "proyecto": {
    "nombre": "string",
    "descripcion": "string",
    "fase_actual": "string (Diseño|Implementación|Testing|Deploy)",
    "contexto_archivo": "string (ruta relativa a contexto_proyecto.md)"
  },
  
  "rol_activo": {
    "nombre": "string",
    "comando": "string",
    "archivo": "string (ruta relativa al archivo del rol)",
    "activado_en": "string ISO 8601"
  },
  
  "historial_roles": [
    {
      "rol": "string",
      "comando": "string",
      "timestamp_inicio": "string ISO 8601",
      "timestamp_fin": "string ISO 8601 | null"
    }
  ],
  
  "hu_activa": {
    "id": "string (ej: ARCHDEV-001)",
    "titulo": "string",
    "estado": "string ([ ]|[R]|[A]|[P]|[E]|[X]|[B])",
    "refinamiento": "string (ruta) | null",
    "plan": "string (ruta) | null",
    "ejecucion": "string (ruta) | null"
  },
  
  "ejecucion_activa": {
    "hu_id": "string",
    "plan_archivo": "string (ruta)",
    "seccion_actual": "number",
    "total_secciones": "number",
    "paso_actual": "number",
    "total_pasos": "number",
    "progreso_porcentaje": "number (0-100)",
    "tracking_archivo": "string (ruta)"
  },
  
  "tablero_tareas": {
    "total": "number",
    "pendientes": "number",
    "en_progreso": "number",
    "completadas": "number",
    "bloqueadas": "number",
    "tareas": [
      {
        "id": "string",
        "titulo": "string",
        "estado": "string ([ ]|[R]|[A]|[P]|[E]|[X]|[B])",
        "prioridad": "string (alta|media|baja)",
        "rol_asignado": "string | null",
        "rol_origen": "string | null",
        "dependencias": ["array de IDs"],
        "bloqueada_por": ["array de IDs"],
        "estimacion_sp": "number | null",
        "estimacion_horas": "number | null",
        "refinamiento_archivo": "string | null",
        "plan_archivo": "string | null",
        "fecha_completada": "string ISO 8601 | null"
      }
    ]
  },
  
  "herramientas_usadas": ["array de strings (nombres de herramientas)"],
  
  "log_eventos_clave": [
    {
      "timestamp": "string ISO 8601",
      "rol": "string",
      "herramienta": "string | null",
      "tipo": "string",
      "id_hu": "string | null",
      "detalle": "string"
    }
  ],
  
  "metadata": {
    "total_cambios_rol": "number",
    "sesion_iniciada": "string ISO 8601",
    "ultima_actividad": "string ISO 8601",
    "roles_unicos_usados": ["array de strings"],
    "total_tareas_completadas": "number",
    "total_artefactos_generados": "number"
  }
}
```

---

## 📖 Descripción de Campos

### Campos Raíz

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `version` | string | Versión del esquema (actualmente "3.0") |
| `timestamp` | ISO 8601 | Última actualización del archivo |

### Sección `proyecto`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre del proyecto |
| `descripcion` | string | Descripción breve del proyecto |
| `fase_actual` | enum | Fase actual: `Diseño`, `Implementación`, `Testing`, `Deploy` |
| `contexto_archivo` | string | Ruta al archivo `contexto_proyecto.md` |

### Sección `rol_activo`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre completo del rol (ej: "ArchDev Pro") |
| `comando` | string | Comando de activación (ej: "archdev") |
| `archivo` | string | Ruta al archivo del rol |
| `activado_en` | ISO 8601 | Timestamp de activación |

### Sección `hu_activa`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador de la HU (ej: "ARCHDEV-001") |
| `titulo` | string | Título descriptivo de la HU |
| `estado` | enum | Estado actual según ciclo de vida |
| `refinamiento` | string\|null | Ruta al archivo de refinamiento |
| `plan` | string\|null | Ruta al plan de implementación |
| `ejecucion` | string\|null | Ruta al tracking de ejecución |

### Sección `ejecucion_activa`

Solo se llena cuando `ejecutar_plan` está en progreso.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `hu_id` | string | ID de la HU en ejecución |
| `plan_archivo` | string | Ruta al plan siendo ejecutado |
| `seccion_actual` | number | Sección actual (1-indexed) |
| `total_secciones` | number | Total de secciones en el plan |
| `paso_actual` | number | Paso actual dentro de la sección |
| `total_pasos` | number | Total de pasos en la sección actual |
| `progreso_porcentaje` | number | Progreso global (0-100) |
| `tracking_archivo` | string | Ruta al archivo de tracking JSON |

### Sección `tablero_tareas`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `total` | number | Total de tareas/HUs |
| `pendientes` | number | Cantidad en estado `[ ]` |
| `en_progreso` | number | Cantidad en estados `[R]`, `[A]`, `[P]`, `[E]` |
| `completadas` | number | Cantidad en estado `[X]` |
| `bloqueadas` | number | Cantidad en estado `[B]` |
| `tareas` | array | Lista de tareas/HUs |

### Sección `log_eventos_clave`

Tipos de evento válidos:
- `sesion_iniciada` - Nueva sesión del sistema
- `cambio_rol` - Cambio de rol activo
- `herramienta_ejecutada` - Uso de herramienta
- `hu_refinada` - HU pasó a estado [R]
- `hu_aprobada` - HU pasó a estado [A]
- `hu_planificada` - HU pasó a estado [P]
- `hu_en_ejecucion` - HU pasó a estado [E]
- `hu_completada` - HU pasó a estado [X]
- `hu_bloqueada` - HU pasó a estado [B]
- `artefacto_generado` - Nuevo archivo creado
- `error` - Error durante ejecución

---

## 🔄 Estados de HU (Ciclo de Vida)

```
[ ] Pendiente
  ↓ refinar_hu (REFINADOR)
[R] Refinada
  ↓ validar_hu (ONAD)
[A] Aprobada
  ↓ planificar_hu (ONAD)
[P] Planificada
  ↓ ejecutar_plan (ARCHDEV)
[E] En Ejecución
  ↓ (finaliza)
[X] Completada

[B] Bloqueada (puede ocurrir en cualquier estado)
```

---

## 💡 Ejemplo Mínimo (Sesión Nueva)

```json
{
  "version": "3.0",
  "timestamp": "2026-01-05T10:00:00Z",
  
  "proyecto": {
    "nombre": "Mi Proyecto",
    "descripcion": "Descripción del proyecto",
    "fase_actual": "Implementación",
    "contexto_archivo": ".cochas/artifacts/contexto_proyecto.md"
  },
  
  "rol_activo": {
    "nombre": "Refinador HU",
    "comando": "refinador",
    "archivo": "personas/refinador_hu.md",
    "activado_en": "2026-01-05T10:00:00Z"
  },
  
  "historial_roles": [],
  
  "hu_activa": null,
  
  "ejecucion_activa": null,
  
  "tablero_tareas": {
    "total": 0,
    "pendientes": 0,
    "en_progreso": 0,
    "completadas": 0,
    "bloqueadas": 0,
    "tareas": []
  },
  
  "herramientas_usadas": [],
  
  "log_eventos_clave": [
    {
      "timestamp": "2026-01-05T10:00:00Z",
      "rol": "orquestador",
      "herramienta": null,
      "tipo": "sesion_iniciada",
      "id_hu": null,
      "detalle": "Nueva sesión iniciada"
    }
  ],
  
  "metadata": {
    "total_cambios_rol": 0,
    "sesion_iniciada": "2026-01-05T10:00:00Z",
    "ultima_actividad": "2026-01-05T10:00:00Z",
    "roles_unicos_usados": ["refinador"],
    "total_tareas_completadas": 0,
    "total_artefactos_generados": 0
  }
}
```

---

## 💡 Ejemplo Completo (Sesión con HU en Ejecución)

```json
{
  "version": "3.0",
  "timestamp": "2026-01-05T14:30:00Z",
  
  "proyecto": {
    "nombre": "Sistema de Tareas",
    "descripcion": "Aplicación web para gestión de tareas",
    "fase_actual": "Implementación",
    "contexto_archivo": ".cochas/artifacts/contexto_proyecto.md"
  },
  
  "rol_activo": {
    "nombre": "ArchDev Pro",
    "comando": "archdev",
    "archivo": "personas/archdev_pro.md",
    "activado_en": "2026-01-05T14:00:00Z"
  },
  
  "historial_roles": [
    {
      "rol": "Refinador HU",
      "comando": "refinador",
      "timestamp_inicio": "2026-01-05T10:00:00Z",
      "timestamp_fin": "2026-01-05T11:30:00Z"
    },
    {
      "rol": "Arquitecto Onad",
      "comando": "onad",
      "timestamp_inicio": "2026-01-05T11:30:00Z",
      "timestamp_fin": "2026-01-05T14:00:00Z"
    }
  ],
  
  "hu_activa": {
    "id": "ARCHDEV-001",
    "titulo": "Implementar modelo Task con validaciones",
    "estado": "[E]",
    "refinamiento": ".cochas/artifacts/HU/refinamientos/ARCHDEV-001_refinamiento_modelo_task.md",
    "plan": ".cochas/artifacts/planes_de_desarrollo/plan_ARCHDEV-001_20260105.md",
    "ejecucion": ".cochas/artifacts/ejecuciones/ejecucion_ARCHDEV-001_20260105_EN_PROGRESO.json"
  },
  
  "ejecucion_activa": {
    "hu_id": "ARCHDEV-001",
    "plan_archivo": ".cochas/artifacts/planes_de_desarrollo/plan_ARCHDEV-001_20260105.md",
    "seccion_actual": 2,
    "total_secciones": 4,
    "paso_actual": 3,
    "total_pasos": 5,
    "progreso_porcentaje": 45,
    "tracking_archivo": ".cochas/artifacts/ejecuciones/ejecucion_ARCHDEV-001_20260105_EN_PROGRESO.json"
  },
  
  "tablero_tareas": {
    "total": 3,
    "pendientes": 1,
    "en_progreso": 1,
    "completadas": 1,
    "bloqueadas": 0,
    "tareas": [
      {
        "id": "ARCHDEV-001",
        "titulo": "Implementar modelo Task con validaciones",
        "estado": "[E]",
        "prioridad": "alta",
        "rol_asignado": "archdev",
        "rol_origen": "onad",
        "dependencias": [],
        "bloqueada_por": [],
        "estimacion_sp": 5,
        "estimacion_horas": 8,
        "refinamiento_archivo": ".cochas/artifacts/HU/refinamientos/ARCHDEV-001_refinamiento_modelo_task.md",
        "plan_archivo": ".cochas/artifacts/planes_de_desarrollo/plan_ARCHDEV-001_20260105.md",
        "fecha_completada": null
      },
      {
        "id": "ARCHDEV-002",
        "titulo": "Implementar TaskController con CRUD",
        "estado": "[ ]",
        "prioridad": "alta",
        "rol_asignado": "archdev",
        "rol_origen": "onad",
        "dependencias": ["ARCHDEV-001"],
        "bloqueada_por": ["ARCHDEV-001"],
        "estimacion_sp": 8,
        "estimacion_horas": 12,
        "refinamiento_archivo": null,
        "plan_archivo": null,
        "fecha_completada": null
      },
      {
        "id": "ONAD-001",
        "titulo": "Diseñar arquitectura REST",
        "estado": "[X]",
        "prioridad": "alta",
        "rol_asignado": "onad",
        "rol_origen": null,
        "dependencias": [],
        "bloqueada_por": [],
        "estimacion_sp": 3,
        "estimacion_horas": 4,
        "refinamiento_archivo": null,
        "plan_archivo": null,
        "fecha_completada": "2026-01-05T12:00:00Z"
      }
    ]
  },
  
  "herramientas_usadas": [
    "tomar_contexto",
    "refinar_hu",
    "validar_hu",
    "planificar_hu",
    "ejecutar_plan"
  ],
  
  "log_eventos_clave": [
    {
      "timestamp": "2026-01-05T10:00:00Z",
      "rol": "orquestador",
      "herramienta": null,
      "tipo": "sesion_iniciada",
      "id_hu": null,
      "detalle": "Nueva sesión iniciada"
    },
    {
      "timestamp": "2026-01-05T10:05:00Z",
      "rol": "Refinador HU",
      "herramienta": "tomar_contexto",
      "tipo": "herramienta_ejecutada",
      "id_hu": null,
      "detalle": "Contexto del proyecto inicializado"
    },
    {
      "timestamp": "2026-01-05T11:00:00Z",
      "rol": "Refinador HU",
      "herramienta": "refinar_hu",
      "tipo": "hu_refinada",
      "id_hu": "ARCHDEV-001",
      "detalle": "HU refinada con 5 criterios de aceptación, estimación: 5 SP"
    },
    {
      "timestamp": "2026-01-05T11:30:00Z",
      "rol": "orquestador",
      "herramienta": null,
      "tipo": "cambio_rol",
      "id_hu": null,
      "detalle": "Refinador HU → Arquitecto Onad"
    },
    {
      "timestamp": "2026-01-05T12:00:00Z",
      "rol": "Arquitecto Onad",
      "herramienta": "validar_hu",
      "tipo": "hu_aprobada",
      "id_hu": "ARCHDEV-001",
      "detalle": "HU aprobada arquitectónicamente"
    },
    {
      "timestamp": "2026-01-05T13:00:00Z",
      "rol": "Arquitecto Onad",
      "herramienta": "planificar_hu",
      "tipo": "hu_planificada",
      "id_hu": "ARCHDEV-001",
      "detalle": "Plan generado con 4 secciones y 15 pasos"
    },
    {
      "timestamp": "2026-01-05T14:00:00Z",
      "rol": "orquestador",
      "herramienta": null,
      "tipo": "cambio_rol",
      "id_hu": null,
      "detalle": "Arquitecto Onad → ArchDev Pro"
    },
    {
      "timestamp": "2026-01-05T14:05:00Z",
      "rol": "ArchDev Pro",
      "herramienta": "ejecutar_plan",
      "tipo": "hu_en_ejecucion",
      "id_hu": "ARCHDEV-001",
      "detalle": "Iniciada ejecución del plan"
    }
  ],
  
  "metadata": {
    "total_cambios_rol": 2,
    "sesion_iniciada": "2026-01-05T10:00:00Z",
    "ultima_actividad": "2026-01-05T14:30:00Z",
    "roles_unicos_usados": ["refinador", "onad", "archdev"],
    "total_tareas_completadas": 1,
    "total_artefactos_generados": 3
  }
}
```

---

## ⚠️ Reglas de Actualización [CRITICO=OBLIGATORIO] [MANDATORIO]

1. **Siempre actualizar `timestamp`** al modificar el archivo
2. **Siempre actualizar `metadata.ultima_actividad`** con cada cambio
3. **Agregar entrada a `log_eventos_clave`** para eventos significativos
4. **Mantener sincronizado `tablero_tareas`** con `backlog_desarrollo.md`
5. **Limpiar `ejecucion_activa`** (poner `null`) cuando finaliza una ejecución

---

## 📚 Referencias

- **Plantilla de Backlog:** `plantillas/backlog_desarrollo_plantilla.md`
- **Guía de Ciclo de Vida:** `guia_ciclo_vida_tareas.md`
- **Configuración:** `CONFIG_INIT.yaml` (define `session_state_location`)

---

*Última actualización: 5 de enero de 2026*
