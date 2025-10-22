# 🛠️ Herramienta: Validar Aceptación de HU

**Comando:** `validar-hu`  
**Versión:** 1.0  
**Rol Propietario:** Arquitecto Onad

---

## 📋 Descripción

Esta herramienta actúa como el **"Quality Gate" (Control de Calidad) Arquitectónico** final antes de que una Historia de Usuario (HU) sea aprobada para implementación. Utiliza un checklist explícito y el contexto del proyecto para validar coherencia arquitectónica, patrones de diseño y restricciones técnicas.

---

## 🎯 Objetivo

Validar que una HU en estado **`[R] Refinada`** cumple con los estándares arquitectónicos del proyecto antes de cambiarla a estado **`[A] Aprobada`**. Si no cumple, generar un informe detallado de correcciones necesarias y esperar confirmación del usuario antes de aplicar ajustes.

---

## 📥 Entrada

**Parámetro requerido:**
- `ID-HU`: Identificador de la tarea (ej. `ARCHDEV-001`)

**Ejemplo de uso:**
```
validar-hu ARCHDEV-001
```

---

## 🔄 Flujo de Ejecución

### **Fase 1: Solicitud y Carga de Contexto**

1. **Solicitud de Entrada:**
   - Pedir al usuario el ID de la Tarea/HU que está en estado `[R] Refinada`
   - Si el usuario ya proporcionó el ID, omitir este paso

2. **Validar Estado de la HU:**
   - Leer `cochas/artifacts/backlog_desarrollo.md`
   - Buscar la HU con el ID especificado
   - **Validación obligatoria:**
     - **SI la HU NO existe:** Mostrar error y listar IDs disponibles
     - **SI la HU NO está en estado `[R]`:** Mostrar error indicando su estado actual
     - **Solo continuar si está en estado `[R] Refinada`**

3. **Carga de Contexto del Proyecto:**
   - Verificar existencia de `cochas/artifacts/contexto_proyecto.md`
   - **SI NO EXISTE:**
     - Mostrar: "⚠️ El contexto del proyecto no está inicializado. Ejecutando `tomar_contexto`..."
     - Ejecutar herramienta `tomar_contexto` completa
   - **SI EXISTE:**
     - Leer archivo completo y cargar en memoria:
       - Stack tecnológico (lenguaje, frameworks, librerías)
       - Arquitectura detectada (ej. Hexagonal, capas identificadas)
       - Componentes core (controladores, servicios, repositorios, modelos)
       - Migraciones Flyway existentes (si aplica)
       - Patrones de diseño identificados

4. **Cargar Reglas Arquitectónicas:**
   - Leer `cochas/artifacts/reglas_arquitectonicas.md`
   - Cargar en memoria las restricciones y patrones obligatorios del proyecto

---

### **Fase 2: Análisis Exhaustivo (Aplicación del Checklist)**

Aplicar el **Checklist de Validación Arquitectónica** (ver sección Checklist más abajo) a la HU.

Para cada ítem del checklist:
1. **Leer la descripción completa de la HU** desde `backlog_desarrollo.md`
2. **Evaluar si cumple el criterio** basándose en:
   - Contexto del proyecto
   - Reglas arquitectónicas
   - Principios de Clean Architecture / Arquitectura Hexagonal
3. **Marcar como:**
   - ✅ **CUMPLE** - El criterio se satisface
   - ❌ **NO CUMPLE** - El criterio se viola o es ambiguo
   - ⚠️ **REQUIERE ACLARACIÓN** - Falta información para validar

---

### **Fase 3: Generación de Informe**

#### **3A. SI TODOS LOS CRITERIOS SON ✅ CUMPLE:**

**Generar informe de aprobación:**

```markdown
## ✅ VALIDACIÓN EXITOSA: [ID-HU]

### Resumen
La HU **[ID-HU]: [Título]** ha pasado todas las validaciones arquitectónicas.

### Checklist de Validación
- ✅ Coherencia con Arquitectura Hexagonal
- ✅ Validación de Persistencia
- ✅ Análisis de Impacto
- ✅ Pruebas y Calidad

### Justificación
[Explicación breve de por qué la HU es coherente y robusta]

### Acción Automática
El estado de la HU se actualizará a **[A] Aprobada** automáticamente.
```

**Acciones:**
1. Actualizar `cochas/artifacts/backlog_desarrollo.md`:
   - Cambiar estado de `[R] Refinada` → `[A] Aprobada`
2. Actualizar `cochas/session/session_state.json`:
   - Agregar evento al `log_eventos_clave`: tipo "hu_aprobada"
   - Actualizar `tablero_tareas` con el nuevo estado
3. Mostrar informe al usuario
4. Preguntar: "¿Deseas validar otra HU o continuar con otra tarea?"

---

#### **3B. SI HAY CRITERIOS ❌ NO CUMPLE o ⚠️ REQUIERE ACLARACIÓN:**

**Generar informe de correcciones:**

```markdown
## ⚠️ VALIDACIÓN PENDIENTE: [ID-HU]

### Resumen
La HU **[ID-HU]: [Título]** requiere correcciones antes de ser aprobada.

### Hallazgos y Correcciones Necesarias

#### ❌ [Nombre del Criterio Violado]
**Problema Detectado:**
[Descripción específica de qué viola la HU]

**Impacto:**
[Explicar consecuencias: deuda técnica, acoplamiento, violación de principios, etc.]

**Corrección Sugerida:**
[Explicación detallada de qué debe cambiarse y por qué]

**Ejemplo:**
[Si aplica, mostrar antes/después o pseudocódigo]

---

#### ⚠️ [Criterio que Requiere Aclaración]
**Ambigüedad Detectada:**
[Qué información falta en la HU]

**Pregunta:**
[Qué necesitas saber para validar este criterio]

---

### Resumen de Estado
- ✅ Criterios Aprobados: [X]
- ❌ Criterios Rechazados: [Y]
- ⚠️ Criterios Ambiguos: [Z]

### Opciones
A) **Aplicar correcciones sugeridas** - Actualizaré la HU con los cambios propuestos y la aprobaré
B) **Devolver al refinador_hu** - Cambiaré el estado a `[ ] Pendiente` para que sea refinada nuevamente
C) **Discutir un hallazgo específico** - Podemos analizar juntos alguna corrección antes de decidir
D) **Cancelar validación** - Mantener el estado actual sin cambios

¿Qué deseas hacer?
```

**Esperar respuesta del usuario:**

- **SI elige A (Aplicar correcciones):**
  1. Aplicar las correcciones sugeridas directamente en `backlog_desarrollo.md`
  2. Actualizar estado a `[A] Aprobada`
  3. Documentar en `session_state.json` el evento "hu_corregida_y_aprobada"
  4. Mostrar: "✅ Correcciones aplicadas y HU aprobada."

- **SI elige B (Devolver al refinador):**
  1. Actualizar estado en `backlog_desarrollo.md` a `[ ] Pendiente`
  2. Agregar un comentario en la HU con el resumen de hallazgos
  3. Documentar en `session_state.json` el evento "hu_rechazada"
  4. Mostrar: "↩️ HU devuelta al refinador_hu para correcciones."

- **SI elige C (Discutir):**
  1. Iniciar diálogo interactivo sobre el hallazgo específico
  2. Al finalizar, volver a presentar las opciones A, B, D

- **SI elige D (Cancelar):**
  1. No realizar cambios
  2. Mostrar: "❌ Validación cancelada. Estado sin cambios."

---

### **Fase 4: Cierre**

1. **Actualizar Estado de Sesión:**
   - Agregar tarea completada al `historial_roles` del rol actual
   - Actualizar `metadata.ultima_actividad`

2. **Preguntar al Usuario:**
   > "¿Deseas validar otra HU, ejecutar otra herramienta, o cambiar de rol?"

---

## ✅ Checklist de Validación Arquitectónica

Este checklist se aplica a cada HU durante la validación.

### 1️⃣ Coherencia con Arquitectura Hexagonal

- [ ] **Los cambios en dominio NO importan clases de infraestructura**
  - Validar que `co.com.bmm.modelo` o `co.com.bmm.puerto` NO importen clases de frameworks (Spring, JPA, etc.)
  
- [ ] **Los puertos (interfaces) están en la capa de dominio**
  - Validar que interfaces de repositorios, servicios externos estén en paquete `puerto`
  
- [ ] **Los adaptadores están en la capa de infraestructura**
  - Validar que implementaciones concretas (DB, API, MQ) estén en `adaptador`

- [ ] **Los casos de uso NO conocen detalles de infraestructura**
  - Validar que los casos de uso (`casodeuso`) solo dependan de puertos (interfaces)

---

### 2️⃣ Validación de Persistencia

- [ ] **Las migraciones Flyway son incrementales**
  - Si la HU propone nuevas migraciones, validar que no conflicten con las existentes
  - Validar nomenclatura: `V[numero]__[descripcion].sql`

- [ ] **No hay conflictos de versión**
  - Verificar que el número de versión no esté duplicado

- [ ] **Los cambios de BD están justificados**
  - Validar que los cambios de esquema respondan a requisitos de negocio, no caprichos técnicos

- [ ] **Se consideran migraciones de rollback**
  - Para cambios destructivos (drop column/table), verificar que hay plan de contingencia

---

### 3️⃣ Análisis de Impacto

- [ ] **No introduce deuda técnica evitable**
  - Detectar si la HU propone código duplicado, hardcoding, o soluciones rápidas sin justificación

- [ ] **No afecta negativamente el rendimiento**
  - Validar que no introduce N+1 queries, carga masiva sin paginación, etc.

- [ ] **No genera acoplamiento entre módulos**
  - Validar que módulos independientes (ej. OTP, Conversación) sigan desacoplados

- [ ] **Respeta principios SOLID**
  - Validar Single Responsibility, Open/Closed, Dependency Inversion

---

### 4️⃣ Pruebas y Calidad

- [ ] **La HU incluye criterios de aceptación claros**
  - Debe tener "Definición de Hecho" (DoD) o criterios verificables

- [ ] **Se especifican casos de prueba**
  - Debe listar al menos:
    - Happy path (flujo exitoso)
    - Edge cases (casos límite)
    - Error handling (manejo de errores)

- [ ] **Se consideran pruebas de integración**
  - Para cambios de BD o API, debe especificar pruebas de integración necesarias

---

### 5️⃣ Coherencia con Reglas del Proyecto

- [ ] **Cumple las reglas documentadas en `reglas_arquitectonicas.md`**
  - Validar contra las restricciones específicas del proyecto

---

## 📤 Salida

### Archivos Modificados

1. **`cochas/artifacts/backlog_desarrollo.md`**
   - Estado de HU actualizado a `[A] Aprobada` o `[ ] Pendiente` según resultado

2. **`cochas/session/session_state.json`**
   - Evento agregado a `log_eventos_clave`
   - Estado de tarea actualizado en `tablero_tareas`

### Respuesta al Usuario

- **Informe de validación** (aprobación o correcciones)
- **Opciones claras** para siguiente acción

---

## 🔧 Dependencias

- **Archivos requeridos:**
  - `cochas/artifacts/contexto_proyecto.md` (se crea si no existe)
  - `cochas/artifacts/reglas_arquitectonicas.md` (se crea si no existe)
  - `cochas/artifacts/backlog_desarrollo.md` (debe existir con HUs)
  - `cochas/session/session_state.json`

- **Herramientas relacionadas:**
  - `tomar_contexto` (si el contexto no está inicializado)
  - `refinar_hu` (para devolver HUs rechazadas)

---

## 📚 Notas de Implementación

### Detección de Violaciones Arquitectónicas

**Para validar importaciones prohibidas:**
1. Leer la descripción de cambios propuestos en la HU
2. Buscar menciones de clases específicas (ej. `@Entity`, `@RestController` en dominio)
3. Si se mencionan archivos concretos, inferir violaciones por convención de nombres

**Para validar persistencia:**
1. Buscar en el contexto del proyecto la sección "Migraciones Flyway"
2. Comparar versiones propuestas con las existentes
3. Detectar conflictos de nomenclatura o versión

**Para validar impacto:**
1. Analizar descripción textual de la HU
2. Identificar palabras clave: "nuevo módulo", "refactor completo", "cambio en core"
3. Aplicar heurísticas de riesgo basadas en alcance

---

## 🎯 Casos de Uso

### Caso 1: HU Aprobada Directamente

```
Usuario: validar-hu ARCHDEV-003

Onad: 
✅ VALIDACIÓN EXITOSA: ARCHDEV-003

La HU "Implementar Catalog Service" ha pasado todas las validaciones.
Todos los criterios del checklist se satisfacen correctamente.

Estado actualizado: [A] Aprobada

¿Deseas validar otra HU?
```

---

### Caso 2: HU con Correcciones Menores

```
Usuario: validar-hu ARCHDEV-005

Onad:
⚠️ VALIDACIÓN PENDIENTE: ARCHDEV-005

Detecté 2 problemas menores:

❌ Criterio: Los puertos deben estar en dominio
Problema: La HU propone crear "RepositorioNotificacion" en infraestructura
Corrección: Mover la interfaz a co.com.bmm.puerto y la implementación a adaptador

❌ Criterio: Migraciones Flyway incrementales
Problema: Propone V003__crear_notificaciones.sql pero ya existe V003__auditoria.sql
Corrección: Renombrar a V004__crear_notificaciones.sql

Opciones:
A) Aplicar correcciones sugeridas y aprobar
B) Devolver al refinador_hu
C) Discutir un hallazgo
D) Cancelar

Usuario: A

Onad: ✅ Correcciones aplicadas y HU aprobada.
```

---

## 🔐 Restricciones

1. **Solo ONAD puede ejecutar esta herramienta** (validación de autoridad)
2. **Solo HUs en estado `[R]` pueden ser validadas**
3. **No se puede aprobar una HU sin resolver todos los ❌**
4. **Toda corrección aplicada automáticamente debe ser documentada en el log**

---

## 📊 Métricas Sugeridas

Puedes trackear en `session_state.json`:
- Total de HUs validadas
- Tasa de aprobación directa (sin correcciones)
- Tasa de rechazo (devueltas al refinador)
- Promedio de correcciones por HU

---

**Fin de la documentación de la herramienta `validar-hu`.**

