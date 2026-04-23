# 🔄 Guía del Ciclo de Vida de Tareas

> **Sistema:** SAC - Sistema Agéntico COCHAS  
> **Versión:** 7.3.0  
> **Última Actualización:** 23 de abril de 2026

---

## 📖 Índice

- [Introducción](#introducción)
- [Estados de las Tareas](#estados-de-las-tareas)
- [Flujo de Validación Secuencial](#flujo-de-validación-secuencial)
- [El Backlog de Desarrollo](#el-backlog-de-desarrollo)
- [Roles y Responsabilidades](#roles-y-responsabilidades)
- [Ejemplos Prácticos](#ejemplos-prácticos)

---

## Introducción

El sistema SAC implementa un **flujo de validación secuencial** para las tareas de desarrollo, garantizando que cada tarea pase por las etapas necesarias de refinamiento, aprobación, planificación e implementación antes de ser marcada como completada.

### Principios del Sistema

1. **Validación Secuencial:** Las tareas deben pasar por estados específicos en orden
2. **Responsabilidad de Roles:** Solo ciertos roles pueden cambiar estados específicos
3. **Trazabilidad:** Todo cambio de estado queda registrado en `{{session_state_location}}`
4. **No Saltar Pasos:** No se puede pasar directamente de Pendiente a Completada
5. **Bloqueos Explícitos:** Las dependencias no resueltas bloquean el avance

---

## Estados de las Tareas

El sistema define **7 estados** para el ciclo de vida de una HU/Tarea:

| Estado | Símbolo | Descripción | Herramienta | Siguiente |
|--------|---------|-------------|-------------|-----------|
| Pendiente | `[ ]` | HU creada, sin analizar | - | `refinar_hu` |
| Refinada | `[R]` | Analizada con criterios y estimación | `refinar_hu` | `validar_hu` |
| Aprobada | `[A]` | Validada arquitectónicamente | `validar_hu` | `planificar_hu` |
| Planificada | `[P]` | Tiene plan de implementación | `planificar_hu` | `ejecutar_plan` |
| En Ejecución | `[E]` | Agente está ejecutando el plan | `ejecutar_plan` | Continuar |
| Completada | `[X]` | Implementación terminada | `ejecutar_plan` | - |
| Bloqueada | `[B]` | Dependencias no resueltas | Cualquiera | Resolver bloqueo |

---

### 📋 Estado 1: Pendiente `[ ]`

**Descripción:** Tarea creada pero no refinada. Requiere clarificación de requisitos.

**Características:**
- Descripción básica de qué hacer
- Puede tener requisitos ambiguos
- Necesita criterios de aceptación claros
- Estimación inicial puede ser imprecisa

**Responsable de avanzar:** `Refinador HU` mediante `refinar_hu`

**Siguiente estado:** `[R]` Refinada

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [ ] Pendiente
- **Por qué:** Necesario para autenticación de usuarios
- **Origen:** ONAD-001
```

---

### 📝 Estado 2: Refinada `[R]`

**Descripción:** Tarea con criterios de aceptación claros, dependencias identificadas y estimación precisa.

**Características:**
- Criterios de aceptación definidos (SMART)
- Dependencias técnicas identificadas
- Estimación de esfuerzo validada
- Casos de borde considerados
- Desglose técnico vertical

**Artefacto generado:** `{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md`

**Responsable de avanzar:** `Arquitecto Onad` mediante `validar_hu`

**Siguiente estado:** `[A]` Aprobada

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [R] Refinada
- **Refinamiento:** `{{artifacts.hu_refinamientos}}/ARCHDEV-001_refinamiento.md`
- **Fecha refinamiento:** 2026-01-04T10:00:00
- **Estimación:** 8 SP / 12 horas

**Criterios de Aceptación:**
✅ Generación de tokens JWT con RS256
✅ Validación de tokens en cada request
✅ Refresh tokens con expiración de 7 días
✅ Tests unitarios con cobertura > 90%
```

---

### ✅ Estado 3: Aprobada `[A]`

**Descripción:** Tarea validada arquitectónicamente y lista para planificación.

**Características:**
- Alineada con decisiones arquitectónicas
- Trade-offs evaluados y aprobados
- Riesgos identificados y mitigados
- Sin conflictos con otras decisiones
- Cumple reglas de `{{reglas_arquitectonicas_location}}`

**Responsable de avanzar:** `Arquitecto Onad` mediante `planificar-hu`

**Siguiente estado:** `[P]` Planificada

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [A] Aprobada
- **Aprobado por:** ONAD el 2026-01-04T11:30:00

**Notas de Aprobación:**
- ✅ Alineado con arquitectura hexagonal
- ✅ JWT preferido sobre sesiones por escalabilidad
- ⚠️ Considerar rate limiting para endpoints de login
```

---

### 📋 Estado 4: Planificada `[P]`

**Descripción:** Tarea con plan de implementación detallado generado.

**Características:**
- Plan paso a paso generado
- Código de ejemplo incluido
- Comandos exactos documentados
- Tests especificados
- Checklist de validación por sección

**Artefacto generado:** `{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md`

**Responsable de avanzar:** `ArchDev Pro` mediante `ejecutar-plan`

**Siguiente estado:** `[E]` En Ejecución

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [P] Planificada
- **Plan:** `{{artifacts.planes_folder}}/ARCHDEV-001_plan_implementacion.md`
- **Fecha planificación:** 2026-01-04T12:00:00
- **Secciones:** 7
- **Archivos a modificar:** 8
- **Tests a crear:** 15
```

---

### ⚡ Estado 5: En Ejecución `[E]`

**Descripción:** ArchDev Pro está ejecutando activamente el plan de implementación.

**Características:**
- Ejecución en progreso
- Tracking de pasos completados
- Progreso porcentual visible
- Puede retomarse si se interrumpe

**Artefacto generado:** `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json`

**Responsable:** `ArchDev Pro` (continúa ejecución)

**Siguiente estado:** `[X]` Completada (éxito) o permanece `[E]` (en progreso)

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [E] En Ejecución
- **Inicio ejecución:** 2026-01-04T14:00:00
- **Progreso:** 65% (27/42 pasos)
- **Sección actual:** 4/7 - Lógica de Aplicación
- **Tracking:** `{{ejecuciones_location}}/ejecucion_ARCHDEV-001_20260104_140000_EN_PROGRESO.json`
```

---

### 🎉 Estado 6: Completada `[X]`

**Descripción:** Tarea implementada, testeada y lista para deployment.

**Características:**
- Código implementado según diseño
- Tests unitarios y de integración pasando
- Build exitoso
- Commit realizado
- Documentación actualizada

**Artefacto generado:** `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_COMPLETADA.json`

**Responsable:** `ArchDev Pro` (al finalizar ejecución)

**Estado final:** No hay siguiente estado

**Ejemplo en backlog:**
```markdown
### ARCHDEV-001: Implementar Auth Service
- **Estado:** [X] Completada
- **Completado:** 2026-01-04T16:45:00
- **Duración:** 2h 45min
- **Commit:** a3f5c21

**Implementación:**
✅ JwtTokenProvider con generación RS256
✅ 15 tests unitarios + 5 integración
✅ Cobertura: 95%
```

---

### 🚫 Estado 7: Bloqueada `[B]`

**Descripción:** Tarea con dependencias no resueltas que impiden el avance.

**Características:**
- Puede ocurrir desde cualquier estado
- Motivo de bloqueo documentado
- Acción requerida especificada
- No puede avanzar hasta resolver

**Tipos de bloqueo:**
- `DEPENDENCIA_HU` - Requiere otra HU completada
- `DEPENDENCIA_EXTERNA` - Requiere sistema/API externa
- `DECISION_PENDIENTE` - Requiere decisión arquitectónica
- `RECURSO_NO_DISPONIBLE` - Falta infraestructura o acceso

**¿Quién puede marcar una tarea como bloqueada?**

> ✅ **Cualquier rol activo** puede marcar una tarea como `[B]` Bloqueada si detecta un impedimento que bloquea la ejecución de la tarea.

| Rol | Puede Bloquear | Motivos Típicos |
|-----|----------------|-----------------|
| **+ONAD** | ✅ Sí | Decisión arquitectónica pendiente, dependencia técnica no resuelta |
| **+ARCHDEV** | ✅ Sí | Dependencia de código de otra HU, API externa no disponible |
| **+DEVOPS** | ✅ Sí | Infraestructura no disponible, acceso denegado |
| **+REFINADOR** | ✅ Sí | Requisitos ambiguos que requieren clarificación del PO |
| **+ARTESANO** | ✅ Sí | Cambios pendientes de otros commits |

**Proceso para marcar como bloqueada:**

```
1. ROL detecta impedimento durante su trabajo
2. ROL documenta el bloqueo:
   - Motivo del bloqueo
   - Tipo de bloqueo (DEPENDENCIA_HU, DECISION_PENDIENTE, etc.)
   - Acción requerida para desbloquear
   - Estado previo al bloqueo
3. ROL actualiza estado a [B] en session_state.json
4. ROL notifica al usuario sobre el bloqueo
```

**Responsable de desbloquear:** Quien pueda resolver la dependencia (puede ser el mismo rol u otro)

**Siguiente estado:** Estado anterior al bloqueo (una vez resuelto)

**Ejemplo en backlog:**
```markdown
### ARCHDEV-003: Implementar Payment Integration
- **Estado:** [B] Bloqueada
- **Estado previo:** [R] Refinada
- **Bloqueado por:** +ARCHDEV
- **Motivo:** Dependencia de ARCHDEV-001 (Auth Service) no completada
- **Tipo:** DEPENDENCIA_HU
- **Acción requerida:** Completar ARCHDEV-001 primero
- **Fecha bloqueo:** 2026-01-04T10:30:00
```

---

## Flujo de Validación Secuencial

### Diagrama de Flujo Principal

```
┌─────────────┐
│  Pendiente  │  ← Tarea creada
│     [ ]     │
└──────┬──────┘
       │ refinar_hu (REFINADOR)
       ▼
┌─────────────┐
│  Refinada   │  ← Criterios claros, estimación precisa
│     [R]     │
└──────┬──────┘
       │ validar_hu (ONAD)
       ▼
┌─────────────┐
│  Aprobada   │  ← Validación arquitectónica
│     [A]     │
└──────┬──────┘
       │ planificar-hu (ONAD)
       ▼
┌─────────────┐
│ Planificada │  ← Plan de implementación generado
│     [P]     │
└──────┬──────┘
       │ ejecutar-plan (ARCHDEV)
       ▼
┌─────────────┐
│ En Ejecución│  ← Implementación en progreso
│     [E]     │
└──────┬──────┘
       │ (finaliza ejecución)
       ▼
┌─────────────┐
│ Completada  │  ← Código implementado y testeado
│     [X]     │
└─────────────┘

        ┌─────────────┐
        │  Bloqueada  │  ← Puede ocurrir desde cualquier estado
        │     [B]     │
        └─────────────┘
```

### Flujo con Bloqueos

```
[ ] ──→ [R] ──→ [A] ──→ [P] ──→ [E] ──→ [X]
 ↓       ↓       ↓       ↓       ↓
 └───────┴───────┴───────┴───────┘
                 ↓
              [B] Bloqueada
                 ↓
         (resolver bloqueo)
                 ↓
         (vuelve al estado anterior)
```

---

### Reglas Estrictas

#### ❌ Prohibido Saltar Estados

**No se puede:**
- `[ ]` → `[X]` (de Pendiente directamente a Completada)
- `[ ]` → `[A]` (de Pendiente directamente a Aprobada)
- `[R]` → `[X]` (de Refinada directamente a Completada)
- `[R]` → `[P]` (de Refinada directamente a Planificada)
- `[A]` → `[E]` (de Aprobada directamente a En Ejecución)

**Siempre debe ser secuencial:**
```
[ ] → [R] → [A] → [P] → [E] → [X]
```

---

#### 🔒 Solo Roles y Herramientas Autorizadas

| Transición | Rol | Herramienta | Comando |
|------------|-----|-------------|---------|
| `[ ]` → `[R]` | Refinador HU | `refinar_hu` | `refinar_hu [ID-HU]` |
| `[R]` → `[A]` | Arquitecto Onad | `validar_hu` | `validar-hu [ID-HU]` |
| `[A]` → `[P]` | Arquitecto Onad | `planificar_hu` | `planificar-hu [ID-HU]` |
| `[P]` → `[E]` | ArchDev Pro | `ejecutar_plan` | `ejecutar-plan [ID-HU]` |
        "secciones": 7,
        "archivos_a_modificar": 8,
        "tests_a_crear": 15,
        "completado": true
      },
      "ejecucion": null,
      "bloqueado": false,
      "dependencias": []
    }
  ]
}
```

---

## Roles y Responsabilidades

### 👥 Refinador HU

**Transición:** `[ ]` → `[R]`
**Herramienta:** `refinar_hu`

**Proceso:**
1. Lee tarea en estado `[ ]` del backlog
2. Ejecuta `refinar_hu [ID-HU]`
3. Define criterios de aceptación SMART
4. Identifica dependencias técnicas
5. Estima esfuerzo con precisión
6. Genera artefacto de refinamiento
7. Actualiza backlog y session_state a `[R]`

---

### 🏛️ Arquitecto Onad

**Transiciones:** `[R]` → `[A]` y `[A]` → `[P]`
**Herramientas:** `validar_hu`, `planificar_hu`

**Proceso de validación:**
1. Lee tarea en estado `[R]`
2. Ejecuta `validar-hu [ID-HU]`
3. Valida alineación arquitectónica
4. Actualiza a `[A]`

**Proceso de planificación:**
1. Lee tarea en estado `[A]`
2. Ejecuta `planificar-hu [ID-HU]`
3. Genera plan de implementación detallado
4. Actualiza a `[P]`

---

### 💻 ArchDev Pro

**Transiciones:** `[P]` → `[E]` → `[X]`
**Herramienta:** `ejecutar_plan`

**Proceso:**
1. Lee tarea en estado `[P]`
2. Ejecuta `ejecutar-plan [ID-HU]`
3. Estado cambia a `[E]` al iniciar
4. Implementa código según plan
5. Estado cambia a `[X]` al completar

---

## 📊 Métricas y Visibilidad

### Ver Estado del Backlog

```bash
/cochas status

# Salida incluye:
📋 **Tablero de Tareas:**
- [ ] Pendientes: 2
- [R] Refinadas: 1
- [A] Aprobadas: 1
- [P] Planificadas: 2
- [E] En Ejecución: 1
- [X] Completadas: 5
- [B] Bloqueadas: 1
```

---

## 🎯 Resumen Rápido

**Flujo secuencial obligatorio (7 estados):**
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

**Archivos centrales:**
- Workspace: `{{archivos.workspace}}`
- Backlog: `{{archivos.backlog}}`
- Contextos: `{{artifacts.contextos_folder}}/`
- Refinamientos: `{{artifacts.hu_refinamientos}}/`
- Planes: `{{artifacts.planes_folder}}/`
- Ejecuciones: `{{artifacts.ejecuciones}}/`

**Comando útil:** `/cochas status` para ver progreso general
