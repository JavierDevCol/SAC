# 🛠️ Herramienta: Ejecutar Plan de Implementación

> **Versión:** 2.0  
> **Fecha de Actualización:** 4 de enero de 2026  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `ejecutar-plan`  
**Comando:** `ejecutar-plan [ID-HU]`  
**Rol Propietario:** ArchDev Pro

---

## 🎯 Objetivo

Ejecutar automáticamente un plan de implementación generado por la herramienta `planificar-hu`, realizando todas las modificaciones de código, creando tests, ejecutando comandos de build, y reportando progreso en tiempo real. Al iniciar, la HU pasa a estado **`[E] En Ejecución`**. Al finalizar exitosamente, pasa a **`[X] Completada`**.

**⚠️ MODO DE EJECUCIÓN ESTRICTA:**
- **ArchDev Pro ejecuta el plan de forma estricta** siguiendo cada instrucción al pie de la letra
- **NO cuestiona** las decisiones del plan (ya fueron validadas por ONAD)
- **Se detiene inmediatamente** ante errores y devuelve control al usuario
- **Pregunta antes de ejecutar comandos Git** (confirmación obligatoria)
- **Modifica archivos de código automáticamente** según las especificaciones del plan

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo | Propósito |
|-------------|--------|-----------|
| `generar_commit` | Al finalizar ejecución exitosa | Generar mensaje de commit estructurado |

### Herramientas que la Invocan

*Esta herramienta es invocada directamente por el usuario después de `planificar-hu`.*

### Prerequisitos

| Herramienta | Obligatoria | Propósito |
|-------------|-------------|-----------|
| `refinar_hu` | ✅ Sí | HU debe estar refinada |
| `validar_hu` | ✅ Sí | HU debe estar aprobada arquitectónicamente |
| `planificar_hu` | ✅ Sí | Debe haberse ejecutado para generar el plan (estado `[P]`) |

---

## 📥 Entradas Requeridas

**Parámetro requerido:**
- `ID-HU`: Identificador de la tarea/HU con plan aprobado (ej. `ARCHDEV-001`)

**Ejemplo de uso:**
```
ejecutar-plan ARCHDEV-001
```

**Archivos requeridos:**
- `{{session_state_location}}` - Estado de sesión con referencia al plan
- `{{backlog_location}}` - Backlog con la HU
- `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md` - Plan de implementación

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `ID-HU` | string | ID válido | requerido | Identificador de la HU a implementar |
| `modo_verbose` | boolean | true\|false | false | Mostrar detalle completo de cada paso |
| `auto_commit` | boolean | true\|false | false | Hacer commit automático sin confirmación |
| `retomar` | boolean | true\|false | auto | Retomar ejecución previa si existe |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (rol principal y único autorizado)

---

## 🔄 Proceso Paso a Paso

**Paso 0 [CRÍTICO - OBLIGATORIO]:** 
Cargar y leer `{{session_state_location}}` y `CONFIG_INIT.yaml` antes de continuar.

### **Fase 1: Adquisición y Confirmación del Plan**

#### **1.1. Solicitud de Entrada**

- Pedir al usuario el ID de la Tarea/HU
- Si el usuario ya proporcionó el ID, omitir este paso

#### **1.2. Validar Estado de la HU**

**Leer `{{backlog_location}}` y `{{session_state_location}}`:**
- Buscar la HU con el ID especificado
- Verificar campo `estado` en `tablero_tareas`

**Validación obligatoria - Estados permitidos:**

| Estado Actual | Acción |
|---------------|--------|
| `[ ]` Pendiente | ❌ Error: "Ejecuta `refinar_hu` primero" |
| `[R]` Refinada | ❌ Error: "Ejecuta `validar_hu` primero" |
| `[A]` Aprobada | ❌ Error: "Ejecuta `planificar-hu` primero" |
| `[P]` Planificada | ✅ Continuar con ejecución |
| `[E]` En Ejecución | ⚠️ "Ejecución previa en progreso. ¿Retomar?" |
| `[X]` Completada | ❌ Error: "HU ya completada" |
| `[B]` Bloqueada | ❌ Error: "Resolver bloqueo primero" |

**Mensaje de error si no está planificada:**
```markdown
❌ La HU [ID-HU] no está en estado [P] Planificada.

Estado actual: [estado_actual]

💡 Flujo requerido:
   1. `refinar_hu [ID-HU]` → Estado [R] Refinada
   2. `validar_hu [ID-HU]` → Estado [A] Aprobada
   3. `planificar-hu [ID-HU]` → Estado [P] Planificada
   4. `ejecutar-plan [ID-HU]` → Estado [E] En Ejecución (estás aquí)

¿Deseas que ejecute el paso faltante? (S/N)
```

#### **1.3. Cargar el Archivo del Plan**

Leer el archivo especificado en `plan_implementacion.archivo`:
```
Ruta: {{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md
```

**SI el archivo NO existe:**
```markdown
⚠️ El plan de [ID-HU] está registrado pero el archivo no existe:
   Ruta esperada: [ruta_del_plan]

Posibles causas:
- El archivo fue eliminado manualmente
- La ruta está corrupta en session_state.json

¿Deseas que ONAD regenere el plan? (S/N)
```

#### **1.4. Verificar Ejecución Previa**

Buscar archivo de tracking en `{{ejecuciones_location}}`:
```
Patrón: ejecucion_[ID-HU]_*_EN_PROGRESO.json
        ejecucion_[ID-HU]_*_DETENIDA_POR_ERROR.json
```

**SI existe ejecución previa incompleta:**
```markdown
⚠️ Se detectó una ejecución previa incompleta de [ID-HU]

Estado anterior: [DETENIDA_POR_ERROR / EN_PROGRESO]
Último paso completado: Sección [X], Paso [Y]
Progreso: [Z]% completado
Fecha: [timestamp]

¿Deseas:
A) Retomar desde donde quedó (Paso [Y+1])
B) Reiniciar ejecución desde el principio
C) Ver detalles de la ejecución anterior
D) Cancelar
```

#### **1.5. Confirmación de Ejecución**

Presentar resumen del plan al usuario:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PLAN ENCONTRADO PARA [ID-HU]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Resumen del Plan:
- Archivo: plan_[ID-HU]_[timestamp].md
- Generado: [fecha]
- Secciones: [X] secciones
- Pasos totales: [Y] pasos
- Archivos a modificar: [Z] archivos
- Tests a crear: [W] tests
- Estimación: [horas] horas

⚠️ MODO DE EJECUCIÓN ESTRICTA:
- Ejecutaré el plan paso a paso sin cuestionamiento
- Me detendré inmediatamente ante errores
- Preguntaré antes de ejecutar comandos Git
- Modificaré archivos de código automáticamente

📋 Estado de la HU cambiará:
- Actual: [P] Planificada
- Durante ejecución: [E] En Ejecución
- Al finalizar: [X] Completada

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿Confirmas la ejecución del plan? (S/N)
```

**Si el usuario dice N:** Cancelar ejecución y finalizar
**Si el usuario dice S:** Continuar a Fase 2

---

### **Fase 2: Ejecución del Plan Paso a Paso**

#### **2.1. Actualizar Estado a [E] En Ejecución**

**Cambiar estado:** `[P] Planificada` → `[E] En Ejecución`

**⚠️ IMPORTANTE:** Usar la estructura exacta de `{{backlog_desarrollo_plantilla}}` para mantener coherencia.

**Actualizar `{{backlog_location}}` con la estructura estándar para estado [E]:**

```markdown
### [ID-HU]: [Título de la HU]
- **Estado:** [E] En Ejecución
- **Origen:** [ID origen - mantener valor existente]
- **Prioridad:** [Alta | Media | Baja - mantener valor existente]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp - mantener valor existente]
- **Estimación:** [X] SP / [Y] horas
- **Plan:** `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md`
- **Fecha planificación:** [timestamp - mantener valor existente]
- **Inicio ejecución:** [timestamp]
- **Progreso:** 0% (0/[Z] pasos)
- **Sección actual:** 1/[N] - [Nombre primera sección]
- **Tracking:** `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json`

**Descripción:**
[Mantener descripción existente]

**Criterios de Aceptación:**
- [ ] CA1: [descripción - mantener existentes]
- [ ] CA2: [descripción]
- [ ] CA3: [descripción]
```

**Campos obligatorios para estado [E]:**
| Campo | Fuente | Acción |
|-------|--------|--------|
| `Estado` | Herramienta | Cambiar a `[E] En Ejecución` |
| `Origen` | Existente | **Mantener sin modificar** |
| `Prioridad` | Existente | **Mantener sin modificar** |
| `Refinamiento` | Existente | **Mantener sin modificar** |
| `Fecha refinamiento` | Existente | **Mantener sin modificar** |
| `Estimación` | Existente | **Mantener sin modificar** |
| `Plan` | Existente | **Mantener sin modificar** |
| `Fecha planificación` | Existente | **Mantener sin modificar** |
| `Inicio ejecución` | Herramienta | Agregar timestamp actual |
| `Progreso` | Herramienta | Agregar progreso inicial (0%) |
| `Sección actual` | Herramienta | Agregar primera sección |
| `Tracking` | Herramienta | Agregar ruta del archivo de tracking |
| `Descripción` | Existente | **Mantener sin modificar** |
| `Criterios de Aceptación` | Existente | **Mantener sin modificar** |

**❌ NO agregar campos que no estén en la plantilla.**
**❌ NO eliminar campos existentes.**

**Actualizar `{{session_state_location}}`:**
```json
{
  "id": "[ID-HU]",
  "estado": "[E]",
  "ejecucion": {
    "archivo_tracking": "{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json",
    "estado": "EN_PROGRESO",
    "inicio": "[timestamp]",
    "progreso": 0
  }
}
```

#### **2.2. Inicialización del Tracking**

Crear archivo de tracking en `{{ejecuciones_location}}`:

```json
{
  "id_hu": "ARCHDEV-001",
  "plan_archivo": "{{plan_desarrollo_location}}/plan_ARCHDEV-001_20260104_150000.md",
  "estado_ejecucion": "EN_PROGRESO",
  "timestamp_inicio": "2026-01-04T15:30:00Z",
  "timestamp_fin": null,
  "progreso": {
    "seccion_actual": 1,
    "paso_actual": 1,
    "total_secciones": 7,
    "total_pasos": 42,
    "pasos_completados": 0,
    "porcentaje_completado": 0
  },
  "secciones": [
    {
      "numero": 1,
      "nombre": "Preparación del entorno",
      "estado": "EN_PROGRESO",
      "pasos": [
        { "numero": 1, "descripcion": "Checkout develop", "estado": "PENDIENTE", "timestamp": null },
        { "numero": 2, "descripcion": "Pull últimos cambios", "estado": "PENDIENTE", "timestamp": null },
        { "numero": 3, "descripcion": "Crear rama feature", "estado": "PENDIENTE", "timestamp": null }
      ]
    }
  ],
  "archivos_modificados": [],
  "archivos_creados": [],
  "comandos_git_ejecutados": [],
  "errores": []
}
```

**Nombre del archivo:**
```
ejecucion_[ID-HU]_[timestamp]_EN_PROGRESO.json
```

#### **2.3. Activación del Modo Implementador**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 MODO IMPLEMENTADOR ESTRICTO ACTIVADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Plan: [nombre_archivo_plan]
HU: [ID-HU] - [Título de la HU]
Estado: [E] En Ejecución
Inicio: [timestamp]

Ejecutando Sección 1 de [X]: [Nombre de la sección]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **2.4. Iteración por Secciones y Pasos**

Para cada sección del plan:

```markdown
📂 SECCIÓN [N]/[TOTAL]: [Nombre de la Sección]
────────────────────────────────────────────────
```

Para cada paso dentro de la sección:

```markdown
📌 Paso [N.M]: [Descripción del paso]

[Acción específica según tipo de paso]
```

**Tipos de pasos y acciones:**

| Tipo de Paso | Acción | Confirmación |
|--------------|--------|--------------|
| Modificar archivo | Editar código automáticamente | No |
| Crear archivo | Crear archivo con contenido | No |
| Ejecutar comando build | Ejecutar `mvn`, `gradle`, `npm` | No |
| Ejecutar tests | Ejecutar suite de tests | No |
| Comando Git | `git checkout`, `git add`, etc. | **SÍ** |
| Comando Git push | `git push` | **SÍ** |
| Eliminar archivo | Borrar archivo | **SÍ** |

**Ejemplo de ejecución de paso:**

```markdown
📌 Paso 2.3: Agregar campo email a entidad Cliente

Archivo: src/main/java/com/empresa/dominio/modelo/Cliente.java
Acción: Agregar campo inmutable 'email' con validación

Modificando archivo...
✅ Campo 'email' agregado correctamente

Ejecutando: mvn compile -q
✅ Compilación exitosa (0 errores, 0 warnings)

[Paso 2.3 completado en 45s]
```

**Ejemplo de paso Git (con confirmación):**

```markdown
📌 Paso 1.3: Crear rama feature

Comando: git checkout -b feature/ARCHDEV-001

⚠️ Este comando Git requiere tu confirmación.
¿Ejecutar? (S/N)
```

#### **2.5. Actualización de Progreso**

Después de cada paso completado:

1. Actualizar archivo de tracking con nuevo estado
2. Mostrar barra de progreso:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Progreso: [████████████░░░░░░░░] 60% (25/42 pasos)
   Sección actual: 4/7 - Implementación de tests
   Tiempo transcurrido: 32 minutos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **2.6. Verificación Post-Sección**

Al completar cada sección, ejecutar verificación:

```markdown
✅ Sección [N] completada: [Nombre]
   - Pasos ejecutados: [X]/[X]
   - Archivos modificados: [Y]
   - Tiempo: [Z] minutos

Verificando integridad...
- Compilación: ✅ OK
- Tests afectados: ✅ 12/12 pasando

Continuando con Sección [N+1]...
```

---

### **Fase 3: Manejo de Errores y Abort**

#### **3.1. Detección de Error**

Tipos de errores que detienen la ejecución:

| Tipo de Error | Ejemplo | Acción |
|---------------|---------|--------|
| Compilación | `cannot find symbol` | Detener inmediatamente |
| Test fallido | `AssertionError` | Detener inmediatamente |
| Archivo no encontrado | `FileNotFoundException` | Detener inmediatamente |
| Comando Git fallido | `merge conflict` | Detener inmediatamente |
| Permiso denegado | `Access denied` | Detener inmediatamente |

#### **3.2. Procedimiento de Abort**

Al detectar un error:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛑 ERROR DETECTADO - EJECUCIÓN DETENIDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Error en Paso [N.M]: [Descripción del paso]

Tipo de error: [COMPILACIÓN / TEST / GIT / SISTEMA]
Mensaje: [mensaje de error completo]

Contexto:
- Archivo: [archivo donde ocurrió]
- Línea: [número de línea si aplica]
- Comando: [comando que falló si aplica]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **3.3. Actualización de Tracking en Error**

```json
{
  "estado_ejecucion": "DETENIDA_POR_ERROR",
  "timestamp_fin": "2026-01-04T16:12:00Z",
  "error": {
    "paso": "2.3",
    "tipo": "COMPILACION",
    "mensaje": "cannot find symbol - Email",
    "archivo": "Cliente.java",
    "linea": 45,
    "timestamp": "2026-01-04T16:12:00Z"
  }
}
```

**Renombrar archivo de tracking:**
```
DE: ejecucion_ARCHDEV-001_20260104_153000_EN_PROGRESO.json
A:  ejecucion_ARCHDEV-001_20260104_153000_DETENIDA_POR_ERROR.json
```

#### **3.4. Reporte de Error y Opciones**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 RESUMEN DE EJECUCIÓN DETENIDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HU: [ID-HU]
Plan: plan_[ID-HU]_[timestamp].md
Inicio: [timestamp_inicio]
Fin: [timestamp_fin] (detenida por error)

Progreso alcanzado:
- Secciones: [X]/[Y] ([Z]%)
- Pasos: [A]/[B] ([C]%)

Archivos modificados antes del error:
1. [archivo1.java] ✅
2. [archivo2.java] ✅
3. [archivo3.java] ❌ (parcial)

Estado Git:
- Rama actual: feature/[ID-HU]
- Cambios sin commit: [N] archivos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿Qué deseas hacer?

A) 🔍 Ver código del archivo que falló
B) 🔧 Corregir manualmente y retomar ejecución
C) ↩️ Revertir todos los cambios (git checkout .)
D) 💾 Mantener cambios y salir (puedes retomar después)
E) 📋 Ver log completo de ejecución

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 Tu progreso está guardado. Puedes retomar ejecutando:
   ejecutar-plan [ID-HU]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **3.5. Generar Reporte de Error (Markdown)**

Crear archivo en `{{ejecuciones_location}}`:

```markdown
# 📄 Reporte de Ejecución Detenida

> **HU:** [ID-HU]  
> **Estado:** DETENIDA_POR_ERROR  
> **Fecha:** [timestamp]

## Resumen

| Métrica | Valor |
|---------|-------|
| Plan | plan_[ID-HU]_[timestamp].md |
| Inicio | [timestamp_inicio] |
| Fin | [timestamp_fin] |
| Progreso | [X]% ([Y]/[Z] pasos) |

## Error que causó la detención

- **Paso:** [N.M] - [Descripción]
- **Tipo:** [COMPILACIÓN/TEST/GIT/SISTEMA]
- **Mensaje:** `[mensaje de error]`
- **Archivo:** [ruta del archivo]
- **Línea:** [número]

## Progreso por Sección

| Sección | Estado | Pasos |
|---------|--------|-------|
| 1. Preparación | ✅ Completada | 3/3 |
| 2. Implementación | ⚠️ Parcial | 2/4 |
| 3. Tests | ⏭️ No iniciada | 0/5 |

## Archivos Modificados

| Archivo | Estado |
|---------|--------|
| Cliente.java | ✅ Completado |
| ClienteTest.java | ❌ Parcial |

## Comandos Git Ejecutados

1. `git checkout develop` ✅
2. `git pull origin develop` ✅
3. `git checkout -b feature/ARCHDEV-001` ✅

## Recomendaciones

1. Corregir el error en [archivo]
2. Ejecutar `ejecutar-plan [ID-HU]` para retomar
3. O revertir con `git checkout .`
```

---

### **Fase 4: Finalización Exitosa**

#### **4.1. Verificación Final**

Al completar todos los pasos:

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Verificación Final
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ejecutando build completo...
> [comando de build del proyecto]

✅ BUILD SUCCESSFUL
   - Compilación: OK
   - Tests: [X]/[X] pasados (100%)
   - Cobertura: [Y]%
   - Tiempo: [Z]s
```

#### **4.2. Preparación de Commit (Con Confirmación)**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Preparar Commit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

He completado la implementación de [ID-HU] según el plan.

Archivos modificados ([N] archivos):
1. dominio/modelo/Cliente.java
2. dominio/modelo/ClienteTest.java
3. infraestructura/adaptador/RepositorioClientePostgres.java
4. resources/db/migration/V005__agregar_columna_email.sql
...

¿Deseas que prepare el commit ahora?

A) ✅ Sí, hacer git add y git commit con mensaje generado
B) ❌ No, yo haré el commit manualmente
C) 🔍 Mostrarme el diff completo antes de decidir
```

**Si usuario elige A:**

```markdown
Ejecutando: git add .
✅ [N] archivos agregados al stage

Generando mensaje de commit...

────────────────────────────────────────────────
feat: agregar campo email a entidad Cliente

Implementa validación y persistencia de email en Cliente según [ID-HU].

Cambios:
- Agregado campo email a modelo Cliente (inmutable)
- Actualizado RepositorioClientePostgres con mapeo de email
- Creada migración Flyway V005 para columna email
- Agregados tests unitarios completos ([X] tests)

Refs: [ID-HU]
────────────────────────────────────────────────

¿Confirmas este mensaje de commit? (S/N)
```

**Si confirma:**

```markdown
Ejecutando: git commit -m "feat: agregar campo email..."
✅ Commit creado: [hash]

¿Deseas hacer push al remoto? (S/N)
```

#### **4.3. Actualización de Estado de la HU a [X] Completada**

**Cambiar estado:** `[E] En Ejecución` → `[X] Completada`

**⚠️ IMPORTANTE:** Usar la estructura exacta de `{{backlog_desarrollo_plantilla}}` para mantener coherencia.

**Actualizar `{{backlog_location}}` con la estructura estándar para estado [X]:**

```markdown
### [ID-HU]: [Título de la HU]
- **Estado:** [X] Completada
- **Origen:** [ID origen - mantener valor existente]
- **Prioridad:** [Alta | Media | Baja - mantener valor existente]
- **Refinamiento:** `{{hu_refinamiento_location}}/[ID-HU]_refinamiento_[concepto].md`
- **Fecha refinamiento:** [timestamp - mantener valor existente]
- **Estimación:** [X] SP / [Y] horas
- **Plan:** `{{plan_desarrollo_location}}/plan_[ID-HU]_[timestamp].md`
- **Completado:** [timestamp]
- **Duración:** [X]h [Y]min
- **Commit:** `[hash]`

**Descripción:**
[Mantener descripción existente]

**Criterios de Aceptación:**
- ✅ CA1: [descripción]
- ✅ CA2: [descripción]
- ✅ CA3: [descripción]

**Implementación:**
- ✅ [Logro 1]
- ✅ [Logro 2]
- ✅ Tests: [X] unitarios + [Y] integración
- ✅ Cobertura: [Z]%
```

**Campos obligatorios para estado [X]:**
| Campo | Fuente | Acción |
|-------|--------|--------|
| `Estado` | Herramienta | Cambiar a `[X] Completada` |
| `Origen` | Existente | **Mantener sin modificar** |
| `Prioridad` | Existente | **Mantener sin modificar** |
| `Refinamiento` | Existente | **Mantener sin modificar** |
| `Fecha refinamiento` | Existente | **Mantener sin modificar** |
| `Estimación` | Existente | **Mantener sin modificar** |
| `Plan` | Existente | **Mantener sin modificar** |
| `Completado` | Herramienta | Agregar timestamp de finalización |
| `Duración` | Herramienta | Calcular duración total |
| `Commit` | Herramienta | Agregar hash del commit |
| `Descripción` | Existente | **Mantener sin modificar** |
| `Criterios de Aceptación` | Herramienta | Marcar todos con ✅ |
| `Implementación` | Herramienta | Agregar resumen de logros |

**❌ NO agregar campos que no estén en la plantilla.**
**❌ NO eliminar campos existentes.**
**❌ ELIMINAR campos temporales:** `Inicio ejecución`, `Progreso`, `Sección actual`, `Tracking`

**Actualizar `{{session_state_location}}`:**

```json
{
  "id": "[ID-HU]",
  "estado": "[X]",
  "ejecucion": {
    "archivo_tracking": "{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_COMPLETADA.json",
    "estado": "COMPLETADA",
    "inicio": "[timestamp_inicio]",
    "fin": "[timestamp_fin]",
    "duracion_minutos": [N],
    "progreso": 100
  }
}
```

**Agregar evento a `log_eventos_clave`:**
```json
{
  "timestamp": "[timestamp_actual]",
  "rol": "ArchDev Pro",
  "herramienta": "ejecutar_plan",
  "tipo": "hu_completada",
  "id_hu": "[ID-HU]",
  "detalle": "HU completada. Duración: [X]min. Commit: [hash]"
}
```

#### **4.4. Actualización de Tracking Final**

```json
{
  "estado_ejecucion": "COMPLETADA",
  "timestamp_fin": "2026-01-04T17:22:00Z",
  "progreso": {
    "pasos_completados": 42,
    "porcentaje_completado": 100
  },
  "commit": {
    "hash": "a3f5c21",
    "mensaje": "feat: agregar campo email...",
    "push": true
  }
}
```

**Renombrar archivo:**
```
DE: ejecucion_ARCHDEV-001_20260104_153000_EN_PROGRESO.json
A:  ejecucion_ARCHDEV-001_20260104_153000_COMPLETADA.json
```

#### **4.5. Reporte Final de Éxito**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 EJECUCIÓN COMPLETADA EXITOSAMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HU: [ID-HU] - [Título]
Plan: plan_[ID-HU]_[timestamp].md
Estado: ✅ COMPLETADA

Tiempo de ejecución:
- Inicio: [timestamp_inicio]
- Fin: [timestamp_fin]
- Duración: [X] minutos
- Estimación original: [Y] minutos
- Eficiencia: [Z]%

Métricas:
- Secciones: [A]/[A] (100%)
- Pasos: [B]/[B] (100%)
- Archivos modificados: [C]
- Archivos creados: [D]
- Tests ejecutados: [E] (100% pasados)
- Build final: ✅ Exitoso

Artefactos:
- ✅ Código implementado
- ✅ Tests unitarios ([X] tests)
- ✅ Migración Flyway (V005)
- ✅ Commit: [hash]
- ✅ Push: origin/feature/[ID-HU]

Estado HU:
- Backlog: [X] Completada
- Session state: Actualizado

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Próximos pasos sugeridos:
1. Crear Pull Request en GitHub/GitLab
2. Solicitar code review
3. Ejecutar CI/CD pipeline
4. Validar en ambiente de QA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reporte guardado en:
{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_COMPLETADA.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 MODO IMPLEMENTADOR ESTRICTO DESACTIVADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **4.6. Cierre**

```markdown
¿Deseas:
A) Ejecutar el plan de otra HU
B) Ver el diff completo de los cambios realizados
C) Cambiar a otro rol
D) Finalizar
```

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Plan no encontrado | Sugerir ejecutar `planificar-hu` primero |
| Archivo de plan eliminado | Ofrecer regenerar con ONAD |
| Plan desactualizado | Advertir y ofrecer regenerar |
| Ejecución previa incompleta | Ofrecer retomar o reiniciar |
| Error de compilación | Detener, mostrar error, ofrecer opciones |
| Test fallido | Detener, mostrar error, ofrecer opciones |
| Conflicto de Git | Detener, mostrar conflicto, requerir resolución manual |
| Permiso denegado | Detener, informar, sugerir verificar permisos |
| Archivo bloqueado | Reintentar 3 veces, luego detener |
| Timeout en comando | Detener después de timeout configurable |

---

## 📤 Formato de Salida Esperado

**Archivos generados:**

| Artefacto | Ubicación | Descripción |
|-----------|-----------|-------------|
| Tracking de ejecución | `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_[ESTADO].json` | Estado detallado de la ejecución |
| Reporte Markdown | `{{ejecuciones_location}}/ejecucion_[ID-HU]_[timestamp]_[ESTADO].md` | Reporte legible |

**Archivos modificados:**

| Archivo | Cambio |
|---------|--------|
| `{{backlog_location}}` | Estado de HU actualizado |
| `{{session_state_location}}` | tablero_tareas y log actualizado |
| Archivos de código | Según especificaciones del plan |

---

## 🔧 Dependencias

**Archivos requeridos:**
- `{{session_state_location}}` - Estado de sesión
- `{{backlog_location}}` - Backlog con la HU
- `{{plan_desarrollo_location}}/plan_[ID-HU]_*.md` - Plan generado

**Herramientas prerequisito:**
- `planificar-hu` - Debe ejecutarse primero para generar el plan

---

## 🔐 Restricciones

1. **Solo ArchDev Pro puede ejecutar esta herramienta**
2. **La HU debe tener un plan generado** (`plan_implementacion != null`)
3. **El archivo del plan debe existir** en la ruta especificada
4. **Ejecución estricta:** No se desvía del plan sin aprobación
5. **Detención ante errores:** Cualquier error detiene inmediatamente
6. **Confirmación Git obligatoria:** Todos los comandos Git requieren confirmación
7. **No modifica archivos fuera del plan:** Solo trabaja con archivos especificados

---

## 📊 Métricas Sugeridas

Trackear en `{{session_state_location}}`:

| Métrica | Descripción |
|---------|-------------|
| planes_ejecutados_exitosos | Total de ejecuciones completadas |
| planes_abortados | Total de ejecuciones detenidas por error |
| tiempo_promedio_ejecucion | Promedio vs estimación |
| tasa_exito_primera_ejecucion | % que completan sin errores |
| errores_mas_comunes | Tipos de error frecuentes |

---

## 🎯 Casos de Uso

### Caso 1: Ejecución Exitosa Completa

```
Usuario: ejecutar-plan ARCHDEV-001

ArchDev Pro:
✅ Plan encontrado para ARCHDEV-001
[... confirmación ...]

🤖 MODO IMPLEMENTADOR ESTRICTO ACTIVADO
[... 52 minutos de ejecución ...]

🎉 EJECUCIÓN COMPLETADA
✅ 42/42 pasos ejecutados
✅ Build: OK
✅ Tests: 42/42 pasados
✅ Commit: a3f5c21

Estado: [X] Completada
```

### Caso 2: Error en Compilación

```
Usuario: ejecutar-plan ARCHDEV-002

ArchDev Pro:
[... ejecutando pasos ...]

🛑 ERROR DETECTADO - EJECUCIÓN DETENIDA

❌ Error en Paso 2.3: Actualizar tests de Cliente
Tipo: COMPILACIÓN
Mensaje: cannot find symbol - Email

Progreso: 5/42 pasos (12%)

¿Qué deseas hacer?
A) Ver código del archivo
B) Corregir manualmente y retomar
C) Revertir cambios
D) Mantener y salir
```

### Caso 3: Retomar Ejecución Previa

```
Usuario: ejecutar-plan ARCHDEV-001

ArchDev Pro:
⚠️ Se detectó una ejecución previa incompleta

Estado: DETENIDA_POR_ERROR
Último paso: Sección 2, Paso 3
Progreso: 12%

¿Deseas:
A) Retomar desde Paso 2.4
B) Reiniciar desde el principio
C) Ver detalles
D) Cancelar
```

### Caso 4: Plan No Encontrado

```
Usuario: ejecutar-plan ARCHDEV-005

ArchDev Pro:
❌ La HU ARCHDEV-005 no tiene plan de implementación.

💡 Ejecuta primero:
   /cochas +onad
   planificar-hu ARCHDEV-005

¿Cambiar automáticamente a ONAD? (S/N)
```

---

## 💡 Ejemplo de Uso Completo

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/ejecutar_plan_ejemplo.md`

---

**Fin de la documentación de la herramienta `ejecutar-plan`.**

