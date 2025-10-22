# 📘 Protocolo: Cómo ArchDev Pro Carga el Plan de Implementación

**Versión:** 1.0  
**Fecha:** 2025-10-21

---

## 🎯 Objetivo

Este documento explica el mecanismo de enlace entre una Historia de Usuario (HU) y su plan de implementación, y cómo el rol **ArchDev Pro** lo carga automáticamente.

---

## 🔗 Mecanismo de Enlace

### **1. Generación del Plan (ONAD)**

Cuando ONAD ejecuta `planificar-hu ARCHDEV-001`, sucede lo siguiente:

1. **Plan generado:**
   ```
   cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md
   ```

2. **Backlog actualizado automáticamente:**
   ```markdown
   ### ARCHDEV-001: Migrar plantillas faltantes
   - **Estado:** [A] Aprobada
   - **Plan de Implementación:** `cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md`
   - **Estimación:** 3 SP / 4.5 horas
   ```

3. **Estado de sesión actualizado automáticamente:**
   ```json
   {
     "id": "ARCHDEV-001",
     "plan_implementacion": "cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md"
   }
   ```

---

## 🤖 Protocolo de Carga para ArchDev Pro

### **Paso 1: Activación del Rol**

El usuario activa ArchDev Pro:
```
/cochas +archdev
```

---

### **Paso 2: ArchDev Pro Busca HUs con Planes**

Al activarse, ArchDev Pro automáticamente:

1. **Lee `cochas/session/session_state.json`**
2. **Busca en `tablero_tareas` las HUs con estado `[A] Aprobada`**
3. **Filtra las que tienen `plan_implementacion != null`**

**Ejemplo de búsqueda:**
```json
"tablero_tareas": {
  "tareas": [
    {
      "id": "ARCHDEV-001",
      "estado_actual": "aprobada",
      "plan_implementacion": "cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md"
    },
    {
      "id": "ARCHDEV-002",
      "estado_actual": "aprobada",
      "plan_implementacion": null  // ← No tiene plan, se omite
    }
  ]
}
```

---

### **Paso 3: ArchDev Pro Pregunta al Usuario**

Si encuentra HUs con planes, presenta opciones:

```
🤖 ArchDev Pro activado.

Detecté las siguientes HUs aprobadas con planes de implementación:

1. ARCHDEV-001: Migrar plantillas faltantes
   Plan: plan_ARCHDEV-001_20251021_150000.md
   Estimación: 4.5 horas

2. ARCHDEV-003: Agregar verificación de nombres sobrantes
   Plan: plan_ARCHDEV-003_20251021_152000.md
   Estimación: 3 horas

¿Qué HU deseas implementar?
A) ARCHDEV-001
B) ARCHDEV-003
C) Especificar otro ID
D) Cancelar
```

---

### **Paso 4: Carga del Plan Específico**

Cuando el usuario elige (ej. **A**), ArchDev Pro:

1. **Extrae la ruta del plan:**
   ```
   plan_implementacion: "cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md"
   ```

2. **Lee el archivo del plan completo**

3. **Parsea las 7 secciones del plan:**
   - Sección 1: Configuración de Tarea
   - Sección 2: Modificaciones de Dominio
   - Sección 3: Modificaciones de Persistencia
   - Sección 4: Lógica de Aplicación
   - Sección 5: Controladores
   - Sección 6: Pruebas
   - Sección 7: Verificación Final

4. **Carga en memoria el plan completo para ejecución secuencial**

---

### **Paso 5: Ejecución Guiada por el Plan**

ArchDev Pro ejecuta el plan paso a paso:

```
🤖 Ejecutando Plan: ARCHDEV-001
📄 Plan: plan_ARCHDEV-001_20251021_150000.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ SECCIÓN: Configuración de Tarea
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Paso 1.1: Actualizar rama principal
¿Ya tienes la rama develop actualizada?
A) Sí, ya hice git pull
B) No, ejecuta: git checkout develop && git pull origin develop
C) Prefiero hacerlo manualmente

[Usuario elige B]

Ejecutando: git checkout develop && git pull origin develop
✅ Rama develop actualizada

Paso 1.2: Crear rama de trabajo
¿La rama feature/ARCHDEV-001 ya existe?
A) Sí, ya existe (hacer checkout)
B) No, créala
C) Prefiero hacerlo manualmente

[Usuario elige B]

Ejecutando: git checkout -b feature/ARCHDEV-001-migrar-plantillas-flyway
✅ Rama creada: feature/ARCHDEV-001-migrar-plantillas-flyway

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ SECCIÓN: Modificaciones de Dominio
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ArchDev Pro continúa con cada sección del plan...]
```

---

## 🔍 Validaciones Automáticas

### **Validación 1: HU sin Plan**

Si el usuario intenta implementar una HU sin plan:

```
Usuario: Quiero implementar ARCHDEV-002

ArchDev Pro:
❌ La HU ARCHDEV-002 no tiene un plan de implementación generado.

💡 Debes cambiar al rol ONAD y ejecutar:
   /cochas +onad
   planificar-hu ARCHDEV-002

Una vez generado el plan, vuelve a activarme con /cochas +archdev
```

---

### **Validación 2: Archivo de Plan No Encontrado**

Si el campo `plan_implementacion` tiene una ruta pero el archivo no existe:

```
ArchDev Pro:
⚠️ El plan de ARCHDEV-001 está registrado pero el archivo no existe:
   Ruta esperada: cochas/artifacts/planes_implementacion/plan_ARCHDEV-001_20251021_150000.md

Posibles causas:
- El archivo fue eliminado manualmente
- La ruta está corrupta

¿Deseas que ONAD regenere el plan? (S/N)
```

---

### **Validación 3: Plan Desactualizado**

Si la HU fue modificada después de generar el plan:

```
ArchDev Pro:
⚠️ Detecté que el plan de ARCHDEV-001 fue generado el 2025-10-21 a las 15:00
   pero la HU fue modificada el 2025-10-21 a las 16:30 (1.5 horas después).

El plan puede estar desactualizado. ¿Deseas:
A) Continuar con el plan existente (bajo tu propio riesgo)
B) Pedir a ONAD que regenere el plan actualizado
C) Cancelar
```

---

## 📊 Diagrama de Flujo Completo

```
Usuario: planificar-hu ARCHDEV-001
         ↓
[ONAD genera plan.md]
         ↓
[Actualiza backlog_desarrollo.md]
         ↓
[Actualiza session_state.json]
         ↓
Usuario: /cochas +archdev
         ↓
[ArchDev Pro lee session_state.json]
         ↓
[Busca HUs aprobadas con plan_implementacion != null]
         ↓
[Muestra lista de HUs disponibles]
         ↓
Usuario: Selecciona ARCHDEV-001
         ↓
[ArchDev Pro lee plan_ARCHDEV-001_20251021_150000.md]
         ↓
[Ejecuta plan paso a paso con confirmaciones]
         ↓
[Build, tests, commit, push]
         ↓
[Actualiza HU a estado Completada]
```

---

## 🎯 Resumen

### **¿Cómo sabe ArchDev Pro qué plan usar?**

1. **Lee el campo `plan_implementacion`** de la HU en `session_state.json`
2. **Carga el archivo** especificado en ese campo
3. **Ejecuta el plan** paso a paso con confirmaciones del usuario

### **¿Qué pasa si no hay plan?**

ArchDev Pro **no puede implementar sin plan**. Pedirá que se genere uno primero.

### **¿Qué pasa si hay múltiples HUs con planes?**

ArchDev Pro **presenta una lista** y el usuario elige cuál implementar.

---

## 🔐 Seguridad

- ✅ ArchDev Pro **solo puede ejecutar HUs con planes generados por ONAD**
- ✅ El usuario **siempre confirma** comandos Git antes de ejecución
- ✅ Validaciones automáticas previenen ejecución de planes corruptos o desactualizados

---

**Última actualización:** 2025-10-21  
**Responsable:** Arquitecto Onad

