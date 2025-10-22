# 🛠️ Herramienta: Ejecutar Plan de Implementación

**Comando:** `ejecutar-plan`  
**Versión:** 1.0  
**Rol Propietario:** ArchDev Pro

---

## 📋 Descripción

Esta herramienta actúa como el **Implementador Estricto** que ejecuta planes de implementación generados por ONAD de forma literal, paso a paso, sin desviaciones ni cuestionamiento. ArchDev Pro se convierte en el ejecutor automatizado que traduce el plan técnico en código funcional.

**⚠️ IMPORTANTE - MODO DE EJECUCIÓN:**
- **ArchDev Pro ejecuta el plan de forma estricta** siguiendo cada instrucción al pie de la letra
- **NO cuestiona** las decisiones del plan (ya fueron validadas por ONAD)
- **Se detiene inmediatamente** ante errores y devuelve control al usuario
- **Pregunta antes de ejecutar comandos Git** (según restricción de confirmación obligatoria)
- **Modifica archivos de código automáticamente** según las especificaciones del plan

---

## 🎯 Objetivo

Ejecutar automáticamente un plan de implementación generado por la herramienta `planificar-hu`, realizando todas las modificaciones de código, creando tests, ejecutando comandos de build, y reportando progreso en tiempo real.

---

## 📥 Entrada

**Parámetro requerido:**
- `ID-HU`: Identificador de la tarea/HU con plan aprobado (ej. `ARCHDEV-001`)

**Ejemplo de uso:**
```
ejecutar-plan ARCHDEV-001
```

---

## 🔄 Flujo de Ejecución

### **Fase 1: Adquisición y Confirmación del Plan**

#### **1.1. Solicitud de Entrada**
- Pedir al usuario el ID de la Tarea/HU
- Si el usuario ya proporcionó el ID, omitir este paso

---

#### **1.2. Búsqueda del Plan**

**Paso 1: Leer `cochas/session/session_state.json`**
- Buscar la HU en `tablero_tareas`
- Verificar campo `plan_implementacion`

**Validación obligatoria:**

**SI `plan_implementacion` es `null`:**
```
❌ La HU [ID-HU] no tiene un plan de implementación generado.

💡 Debes cambiar al rol ONAD y ejecutar:
   /cochas +onad
   planificar-hu [ID-HU]

Una vez generado el plan, vuelve a activarme con:
   /cochas +archdev
   ejecutar-plan [ID-HU]

¿Deseas que cambie automáticamente a ONAD para generar el plan? (S/N)
```

**Si el usuario dice S:**
- Cambiar automáticamente al rol ONAD
- Sugerir: `planificar-hu [ID-HU]`
- Finalizar (el usuario debe ejecutar planificar-hu y volver)

---

**Paso 2: Cargar el archivo del plan**

Leer el archivo especificado en `plan_implementacion`:
```
Ruta: cochas/artifacts/planes_implementacion/plan_[ID-HU]_[timestamp].md
```

**SI el archivo NO existe:**
```
⚠️ El plan de [ID-HU] está registrado en el sistema pero el archivo no existe:
   Ruta esperada: [ruta_del_plan]

Posibles causas:
- El archivo fue eliminado manualmente
- La ruta está corrupta en session_state.json

¿Deseas que ONAD regenere el plan? (S/N)
```

**Si el usuario dice S:**
- Cambiar automáticamente al rol ONAD
- Sugerir: `planificar-hu [ID-HU]`
- Finalizar

---

**Paso 3: Validar actualidad del plan**

Comparar timestamps:
- `fecha_generacion_plan` (metadata del plan)
- `fecha_aprobacion_hu` (desde backlog o session_state)

**SI el plan fue generado ANTES de la última modificación de la HU:**
```
⚠️ ADVERTENCIA: Plan potencialmente desactualizado

Plan generado: [fecha_plan]
HU modificada: [fecha_hu_modificacion]
Diferencia: [X] horas después

El plan puede no reflejar los cambios más recientes de la HU.

¿Deseas:
A) Continuar con el plan existente (bajo tu propio riesgo)
B) Pedir a ONAD que regenere el plan actualizado
C) Cancelar ejecución
```

---

#### **1.3. Confirmación de Ejecución**

Presentar resumen del plan al usuario:

```
✅ Plan encontrado para [ID-HU]

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

¿Confirmas la ejecución del plan? (S/N)
```

**Si el usuario dice N:**
- Cancelar ejecución
- Finalizar

**Si el usuario dice S:**
- Continuar a Fase 2
Plan: plan_ARCHDEV-001_20251021_150000.md
Inicio: 2025-10-21 16:30:00
Fin: 2025-10-21 16:45:00 (abortada)

Progreso:
- Sección 1: ✅ Completada (3/3 pasos)
- Sección 2: ⚠️ Parcial (2/4 pasos)
  - Paso 2.1: ✅ Completado
  - Paso 2.2: ✅ Completado
  - Paso 2.3: ❌ FALLIDO (compilación)
  - Paso 2.4: ⏭️ No ejecutado

Error que causó el abort:
- Paso: 2.3 (Actualizar tests de Cliente)
- Tipo: Error de compilación
- Mensaje: cannot find symbol - Email

Archivos modificados:
1. microservicio/dominio/.../Cliente.java ✅
2. microservicio/dominio/.../ClienteTest.java ❌ (parcial)

Archivos creados:
[Ninguno]

Comandos Git ejecutados:
1. git checkout develop ✅
2. git pull origin develop ✅
3. git checkout -b feature/ARCHDEV-001 ✅

Estado actual:
- Rama: feature/ARCHDEV-001
- Cambios sin commit: 2 archivos modificados
- Build: ❌ Fallido

Recomendaciones:
1. Corregir import de clase Email en Cliente.java
Cuando se aborta por error, generar reporte completo:

**El archivo de tracking ya contiene toda la información necesaria:**
- `ejecucion_ARCHDEV-001_20251021_170000_DETENIDA_POR_ERROR.json`

**Adicionalmente, generar reporte en Markdown para lectura humana:**
3. O revertir cambios: git checkout dominio/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 REPORTE DE EJECUCIÓN DETENIDA POR ERROR
Reporte guardado en:
cochas/artifacts/planes_implementacion/ejecucion_ARCHDEV-001_20251021_163000_ABORTADA.md
```

Archivo de tracking: ejecucion_ARCHDEV-001_20251021_170000_DETENIDA_POR_ERROR.json
Inicio: 2025-10-21 17:00:00
Fin: 2025-10-21 17:12:00 (detenida por error)
### **Fase 4: Finalización y Verificación**

#### **4.1. Anuncio de Finalización (Si todos los pasos se completaron)**

  - Paso 2.1: ✅ Completado (45s)
  - Paso 2.2: ✅ Completado (180s)
🎉 EJECUCIÓN COMPLETADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Error que causó la detención:
- Paso: 2.3 (Agregar validación de email)
Resumen de ejecución:
- Secciones ejecutadas: 7/7 (100%)
- Detalle completo: [ver tracking JSON]
- Pasos totales: 42/42 (100%)
- Archivos modificados: 8
- Archivos creados: 5
2. microservicio/dominio/.../ClienteTest.java ✅
3. microservicio/dominio/.../Cliente.java ❌ (fallido)
- Tiempo total: 52 minutos
```

---

#### **4.2. Verificación Final**

Ejecutar comando de verificación final del plan:

```
📌 Verificación Final: Build completo

Ejecutando: gradlew clean build
- Archivo de tracking: GUARDADO (puedes retomar)

> Task :compileJava
> Task :processResources
2. Retomar ejecución: ejecutar-plan ARCHDEV-001
   (Se detectará automáticamente la ejecución previa y preguntará si retomar)
> Task :compileTestJava
> Task :processTestResources
> Task :testClasses
> Task :test
💾 IMPORTANTE: Tu progreso está guardado en el archivo de tracking.
   Puedes retomar la ejecución en cualquier momento ejecutando:
   
   ejecutar-plan ARCHDEV-001
   
   El sistema detectará que hay una ejecución previa y te permitirá continuar
   desde el Paso 2.3 (donde falló).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> Task :build
cochas/artifacts/planes_implementacion/ejecucion_ARCHDEV-001_20251021_170000_ERROR.md
BUILD SUCCESSFUL in 1m 23s
45 tests completed, 45 passed
```

```
✅ Verificación final exitosa
✅ Build: OK
✅ Tests: 42/42 pasados
```

---

#### **4.3. Preparación de Commit (CON CONFIRMACIÓN)**

```
📌 Paso Final: Preparar commit

He completado la implementación de ARCHDEV-001 según el plan.

Archivos modificados:
1. dominio/modelo/Cliente.java
2. dominio/modelo/ClienteTest.java
3. infraestructura/adaptador/RepositorioClientePostgres.java
4. infraestructura/resources/db/migration/V005__agregar_columna_email.sql
5. aplicacion/casodeuso/CrearClienteCasoUso.java
... (total: 8 archivos)

¿Deseas que prepare el commit ahora?
A) Sí, hacer git add y git commit con mensaje generado
B) No, yo haré el commit manualmente
C) Mostrarme el diff completo antes de decidir
```

**Si usuario elige A:**
```
Ejecutando: git add .
✅ 8 archivos agregados al stage

Generando mensaje de commit basado en el plan...

Mensaje propuesto:
─────────────────────────────────────────────────
feat: agregar campo email a entidad Cliente

Implementa validación y persistencia de email en Cliente según ARCHDEV-001.

Cambios:
- Agregado campo email a modelo Cliente (inmutable)
- Actualizado RepositorioClientePostgres con mapeo de email
- Creada migración Flyway V005 para columna email
- Agregados tests unitarios completos (42 tests, todos pasando)
- Actualizado CrearClienteCasoUso con validación de email

Refs: ARCHDEV-001
─────────────────────────────────────────────────

¿Confirmas este mensaje de commit? (S/N)
```

**Si usuario dice S:**
```
Ejecutando: git commit -m "feat: agregar campo email..."
✅ Commit creado: a3f5c21

¿Deseas hacer push al remoto? (S/N)
```

---

#### **4.4. Actualización de Estado de la HU**

```
📌 Actualizando estado de la HU en el sistema...

Actualizando cochas/artifacts/backlog_desarrollo.md...
✅ Estado cambiado: [A] Aprobada → [X] Completada
✅ Fecha de completación agregada: 2025-10-21T17:22:00Z

Actualizando cochas/session/session_state.json...
✅ Estado actualizado en tablero_tareas
✅ Evento agregado a log_eventos_clave
```

---

#### **4.5. Informe Final de Éxito**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 REPORTE FINAL DE EJECUCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HU: ARCHDEV-001 - Migrar plantillas faltantes
Plan: plan_ARCHDEV-001_20251021_150000.md
Estado: ✅ COMPLETADA EXITOSAMENTE

Tiempo de ejecución:
- Inicio: 2025-10-21 16:30:00
- Fin: 2025-10-21 17:22:00
- Duración total: 52 minutos
- Estimación original: 60 minutos
- Eficiencia: 87% (8 min bajo estimación)

Métricas de ejecución:
- Secciones: 7/7 (100%)
- Pasos: 42/42 (100%)
- Comandos Git: 5/5 exitosos
- Archivos modificados: 8
- Archivos creados: 5
- Tests ejecutados: 42 (100% pasados)
- Build final: ✅ Exitoso

Artefactos generados:
- Código implementado: ✅
- Tests unitarios: ✅ (42 tests)
- Migración Flyway: ✅ (V005)
- Commit: ✅ (a3f5c21)
- Push: ✅ (origin/feature/ARCHDEV-001)

Estado de la HU:
- Backlog: [X] Completada
- Session state: Actualizado
- Fecha completación: 2025-10-21T17:22:00Z

Próximos pasos sugeridos:
1. Crear Pull Request en GitHub/GitLab
2. Solicitar code review al equipo
3. Ejecutar CI/CD pipeline
4. Validar en ambiente de QA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reporte completo guardado en:
cochas/artifacts/planes_implementacion/ejecucion_ARCHDEV-001_20251021_163000_EXITOSA.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 MODO IMPLEMENTADOR ESTRICTO DESACTIVADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### **4.6. Cierre**

```
¿Deseas:
A) Ejecutar el plan de otra HU
B) Ver el diff completo de los cambios realizados
C) Cambiar a otro rol
D) Otra cosa
```
**Actualizar archivo de tracking:**
```json
{
  "estado_ejecucion": "COMPLETADA",
  "timestamp_fin": "2025-10-21T17:52:00Z",
  "progreso": {
    "pasos_completados": 42,
    "porcentaje_completado": 100
  }
}
```

**Renombrar archivo de tracking:**
```
DE: ejecucion_ARCHDEV-001_20251021_170000_EN_PROGRESO.json
A:  ejecucion_ARCHDEV-001_20251021_170000_COMPLETADA.json
```


---

## 📤 Salida

### Archivos Modificados

1. **Archivos de código** según el plan (Java, SQL, etc.)
2. **`cochas/artifacts/backlog_desarrollo.md`** - Estado de HU actualizado a `[X]`
3. **`cochas/session/session_state.json`** - Estado y eventos actualizados

### Archivos Creados

1. **Reporte de ejecución:**
   - Éxito: `cochas/artifacts/planes_implementacion/ejecucion_[ID-HU]_[timestamp]_EXITOSA.md`
   - Abortada: `cochas/artifacts/planes_implementacion/ejecucion_[ID-HU]_[timestamp]_ABORTADA.md`

### Commits Git (si se confirmaron)

1. Commit con mensaje generado automáticamente
2. Push al remoto (si se confirmó)

---

## 🔧 Dependencias

- **Archivos requeridos:**
  - Plan de implementación (generado por `planificar-hu`)
  - `cochas/session/session_state.json`
  - `cochas/artifacts/backlog_desarrollo.md`

- **Herramientas relacionadas:**
  - `planificar-hu` (prerequisito: debe haberse ejecutado primero)

---

## 🔐 Restricciones

1. **Solo ArchDev Pro puede ejecutar esta herramienta**
2. **La HU debe tener un plan generado** (`plan_implementacion != null`)
3. **El archivo del plan debe existir** en la ruta especificada
4. **Ejecución estricta:** No se desvía del plan sin aprobación del usuario
5. **Detención ante errores:** Cualquier error detiene la ejecución inmediatamente
6. **Confirmación de Git obligatoria:** Todos los comandos Git requieren confirmación del usuario
7. **No modifica archivos fuera del plan:** Solo trabaja con archivos especificados

---

## 📊 Métricas Sugeridas

Trackear en `session_state.json`:
- Total de planes ejecutados exitosamente
- Total de planes abortados por error
- Tiempo promedio de ejecución vs estimación
- Tasa de éxito en primera ejecución
- Tipos de errores más comunes

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
✅ Commit creado: a3f5c21

Estado: [X] Completada
```

---

### Caso 2: Error en Compilación (Detención)

```
Usuario: ejecutar-plan ARCHDEV-002

ArchDev Pro:
[... ejecutando pasos ...]

📌 Paso 2.3: Actualizar tests de Cliente

❌ ERROR DE COMPILACIÓN
cannot find symbol - Email

🛑 EJECUCIÓN DETENIDA

Progreso: 5/42 pasos (12%)
Estado: Abortada en Paso 2.3

¿Deseas:
A) Ver código modificado
B) Revertir cambios
C) Corregir manualmente
```

---

### Caso 3: Plan No Encontrado

```
Usuario: ejecutar-plan ARCHDEV-005

ArchDev Pro:
❌ La HU ARCHDEV-005 no tiene un plan de implementación generado.

💡 Debes ejecutar primero:
   /cochas +onad
   planificar-hu ARCHDEV-005

¿Deseas que cambie automáticamente a ONAD? (S/N)
```

---

**Fin de la documentación de la herramienta `ejecutar-plan`.**

