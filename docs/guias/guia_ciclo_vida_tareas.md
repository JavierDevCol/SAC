# 🔄 Guía del Ciclo de Vida de Tareas

> **Sistema:** SAC - Sistema Agéntico COCHAS
> **Versión:** 7.25.0
> **Última Actualización:** 27 de junio de 2026

---

## 📖 Índice

- [Introducción](#introducción)
- [Estados de las Tareas](#estados-de-las-tareas)
- [Detección de Estado por Archivos](#detección-de-estado-por-archivos)
- [Flujo de Validación Secuencial](#flujo-de-validación-secuencial)
- [Estructura de Carpetas HU](#estructura-de-carpetas-hu)
- [Roles y Responsabilidades](#roles-y-responsabilidades)
- [Sub-Agentes](#sub-agentes)

---

## Introducción

El sistema SAC implementa un **flujo de validación secuencial** para las tareas de desarrollo, garantizando que cada tarea pase por las etapas necesarias de refinamiento, aprobación, planificación e implementación antes de ser marcada como completada.

### Principios del Sistema

1. **Validación Secuencial:** Las tareas deben pasar por estados específicos en orden
2. **Responsabilidad de Roles:** Solo ciertos roles pueden cambiar estados específicos
3. **Trazabilidad:** Todo cambio de estado queda registrado en archivos de la HU
4. **No Saltar Pasos:** No se puede pasar directamente de Pendiente a Completada
5. **Bloqueos Explícitos:** Las dependencias no resueltas bloquean el avance
6. **Estado por Archivos:** El estado se infiere de la existencia de archivos en la carpeta de la HU

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
| SAC-001 | Implementar Auth Service | [ ] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-001/
└── HU.md  ← Solo existe este archivo
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

**Artefacto generado:** `{{artifacts.hu_folder}}/[ID-HU]/Refinamiento.md`

**Responsable de avanzar:** `Arquitecto Onad` mediante `validar_hu`

**Siguiente estado:** `[A]` Aprobada

**Ejemplo en backlog:**
```markdown
| SAC-001 | Implementar Auth Service | [R] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-001/
├── HU.md              ← Metadata de la HU
└── Refinamiento.md    ← Criterios de aceptación, estimación
```
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

**Artefacto generado:** `{{artifacts.hu_folder}}/[ID-HU]/Plan.md`

**Responsable de avanzar:** `ArchDev Pro` mediante `ejecutar_plan`

**Siguiente estado:** `[E]` En Ejecución

**Ejemplo en backlog:**
```markdown
| SAC-001 | Implementar Auth Service | [P] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-001/
├── HU.md
├── Refinamiento.md
└── Plan.md             ← Plan de implementación
```

---

### ⚡ Estado 5: En Ejecución `[E]`

**Descripción:** ArchDev Pro está ejecutando activamente el plan de implementación.

**Características:**
- Ejecución en progreso
- Tracking de pasos completados
- Progreso porcentual visible
- Puede retomarse si se interrumpe

**Artefacto generado:** `{{artifacts.hu_folder}}/[ID-HU]/Tracking.md`

**Responsable:** `ArchDev Pro` (continúa ejecución)

**Siguiente estado:** `[X]` Completada (éxito) o permanece `[E]` (en progreso)

**Ejemplo en backlog:**
```markdown
| SAC-001 | Implementar Auth Service | [E] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-001/
├── HU.md
├── Refinamiento.md
├── Plan.md
└── Tracking.md         ← Historial de ejecución
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

**Artefacto generado:** `{{artifacts.hu_folder}}/[ID-HU]/Tracking.md` (campo Finalización)

**Responsable:** `ArchDev Pro` (al finalizar ejecución)

**Estado final:** No hay siguiente estado

**Ejemplo en backlog:**
```markdown
| SAC-001 | Implementar Auth Service | [X] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-001/
├── HU.md
├── Refinamiento.md
├── Plan.md             ← Estado: COMPLETADO
└── Tracking.md         ← Estado: FINALIZADO, Commit: a1b2c3d
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

**Proceso para marcar como bloqueada:**

```
1. ROL detecta impedimento durante su trabajo
2. ROL documenta el bloqueo en Refinamiento.md:
   - Sección ## Bloqueo de Validación
   - Motivo del bloqueo
   - Tipo de bloqueo (DEPENDENCIA_HU, DECISION_PENDIENTE, etc.)
   - Acción requerida para desbloquear
   - Estado previo al bloqueo
3. ROL actualiza backbone índice a [B]
4. ROL notifica al usuario sobre el bloqueo
```

**Responsable de desbloquear:** Quien pueda resolver la dependencia (puede ser el mismo rol u otro)

**Siguiente estado:** Estado anterior al bloqueo (una vez resuelto)

**Ejemplo en backlog:**
```markdown
| SAC-003 | Implementar Payment | [B] | P0 | Feature | backend |
```

**Ejemplo en carpeta HU:**
```
artifacts/HU/SAC-003/
├── HU.md
└── Refinamiento.md     ← Contiene ## Bloqueo de Validación
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
| `[A]` → `[P]` | ArchDev Pro | `planificar_hu` | `planificar-hu [ID-HU]` |
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
3. Crea carpeta `SAC-XXX/` con HU.md y Refinamiento.md
4. Define criterios de aceptación SMART
5. Identifica dependencias técnicas
6. Estima esfuerzo con precisión
7. Actualiza backbone índice a `[R]`

---

### 🏛️ Arquitecto Onad

**Transición:** `[R]` → `[A]`
**Herramienta:** `validar_hu`

**Proceso:**
1. Lee HU y Refinamiento desde `SAC-XXX/`
2. Ejecuta `validar_hu [ID-HU]`
3. Valida alineación arquitectónica
4. Agrega sección `## Aprobación` en Refinamiento.md
5. Actualiza backbone índice a `[A]`

---

### 💻 ArchDev Pro

**Transiciones:** `[A]` → `[P]` → `[E]` → `[X]`
**Herramientas:** `planificar_hu`, `ejecutar_plan`, `validar_ca`

**Proceso de planificación:**
1. Lee HU y Refinamiento desde `SAC-XXX/`
2. Ejecuta `planificar_hu [ID-HU]`
3. Crea Plan.md en `SAC-XXX/`
4. Actualiza backbone índice a `[P]`

**Proceso de ejecución:**
1. Lee Plan.md desde `SAC-XXX/`
2. Ejecuta `ejecutar_plan [ID-HU]`
3. Crea Tracking.md en `SAC-XXX/`
4. Actualiza backbone índice a `[E]`
5. Implementa código según plan
6. Actualiza Tracking.md con progreso
7. Al completar: actualiza backbone índice a `[X]`

---

## 📊 Métricas y Visibilidad

### Ver Estado del Backlog

```bash
>sincronizar_backlog --resumen

# Salida incluye:
📊 Resumen del Backlog
━━━━━━━━━━━━━━━━━━━━
[ ] Pendientes: 2 | [R] Refinadas: 1 | [A] Aprobadas: 1
[P] Planificadas: 2 | [E] En Ejecución: 1 | [X] Completadas: 5 | [B] Bloqueadas: 1
Total: 12 HUs
```

---

## 🎯 Resumen Rápido

**Flujo secuencial obligatorio (7 estados):**
```
[ ] Pendiente
  ↓ >refinar_hu (REFINADOR)
[R] Refinada
  ↓ >validar_hu (ONAD)
[A] Aprobada
  ↓ >planificar_hu (ARCHDEV)
[P] Planificada
  ↓ >ejecutar_plan (ARCHDEV)
[E] En Ejecución
  ↓ (finaliza)
[X] Completada

[B] Bloqueada (puede ocurrir en cualquier momento)
```

**Estructura de carpetas:**
```
artifacts/HU/
├── backlog_desarrollo.md     ← Solo índice resumen
├── SAC-001/                  ← Carpeta de HU
│   ├── HU.md
│   ├── Refinamiento.md
│   ├── Plan.md
│   └── Tracking.md
├── SAC-001-TASK-01/          ← Task hija
│   ├── HU.md
│   └── Refinamiento.md
└── deuda_tecnica/            ← Deuda técnica
    └── DT-XXX_descripcion.md
```

**Detección de estado por archivos:**
```
SAC-XXX/HU.md                      → [ ] Pendiente
SAC-XXX/HU.md + Refinamiento.md    → [R] Refinada
+ ## Aprobación en Refinamiento.md → [A] Aprobada
+ Plan.md                          → [P] Planificada
+ Tracking.md                      → [E] En Ejecución
Plan.md Estado: COMPLETADO         → [X] Completada
```

**Comando útil:** `/cochas status` para ver progreso general
