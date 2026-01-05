# 📋 Guía Completa de Comandos del Sistema

> **Sistema:** COCHAS - Orquestación de Agentes IA  
> **Versión:** 3.0  
> **Última Actualización:** 5 de enero de 2026

---

## 📖 Índice

- [Sistema de Prefijos](#sistema-de-prefijos)
- [Comandos del Orquestador (*)](#comandos-del-orquestador-)
- [Activación de Roles (+)](#activación-de-roles-)
- [Ejecución de Herramientas (>)](#ejecución-de-herramientas-)
- [Casos de Uso Comunes](#casos-de-uso-comunes)
- [Gestión de Errores](#gestión-de-errores)

---

## Sistema de Prefijos

El sistema COCHAS usa **3 prefijos** para diferentes tipos de acciones:

| Prefijo | Propósito | Requiere Rol Activo | Ejemplos |
|---------|-----------|---------------------|----------|
| `*` | **Comandos del Orquestador** | ❌ No | `*roles`, `*status`, `*HU`, `*help` |
| `+` | **Activar un Rol** | ❌ No | `+ONAD`, `+ARCHDEV`, `+REFINADOR` |
| `>` | **Ejecutar una Herramienta** | ✅ Sí | `>refinar_hu`, `>generar_commit` |

### Regla Principal

```
* = Consultar/Utilidades del sistema
+ = Activar rol
> = Ejecutar herramienta (requiere rol activo)
```

---

## Comandos del Orquestador (`*`)

Los comandos con `*` son utilidades del orquestador que no requieren rol activo.

---

### `*roles`

**Descripción:** Lista todos los roles disponibles en el sistema.

**Formato:**
```
*roles
```

**Salida Esperada:**
```
📋 Roles Disponibles en COCHAS:

| # | Rol               | Comando     | Estado      |
|---|-------------------|-------------|-------------|
| 1 | Arquitecto ONAD   | +ONAD       | ⚪ Inactivo |
| 2 | ArchDev Pro       | +ARCHDEV    | 🟢 Activo   |
| 3 | Artesano Commits  | +ARTESANO   | ⚪ Inactivo |
| 4 | Arquitecto DevOps | +DEVOPS     | ⚪ Inactivo |
| 5 | Refinador HU      | +REFINADOR  | ⚪ Inactivo |

💡 Usa +COMANDO para activar un rol.
```

**Cuándo Usarlo:**
- Al iniciar una nueva sesión
- Cuando no recuerdas qué roles están disponibles
- Para verificar el comando exacto de activación

---

### `*status`

**Descripción:** Muestra el estado actual de la sesión.

**Formato:**
```
*status
```

**Salida Esperada:**
```
📊 Estado de Sesión COCHAS

🎭 Rol Activo: ArchDev Pro (+ARCHDEV)
📂 Archivo: personas/archdev_pro.md
🛠️ Herramientas disponibles: >refactorizar, >crear_pruebas, >analizar_code_smells
📅 Última actividad: 2026-01-05 10:30

📁 Proyecto:
- Contexto: INICIALIZADO
- HUs activas: 3
- Tareas pendientes: 5
```

**Cuándo Usarlo:**
- Para verificar qué rol está activo
- Para revisar el progreso de la sesión
- Al retomar una sesión anterior

---

### `*HU`

**Descripción:** Lista las historias de usuario del proyecto.

**Formato:**
```
*HU
```

**Salida Esperada:**
```
📋 Historias de Usuario

| ID | Título | Estado | Prioridad |
|----|--------|--------|-----------|
| HU-001 | Login con OAuth | 🟡 En Refinamiento | Alta |
| HU-002 | Dashboard usuario | 🟢 Refinada | Media |
| HU-003 | Notificaciones push | ⚪ Pendiente | Baja |

📂 Ubicación: .cochas/artifacts/HU/
💡 Usa +REFINADOR y >refinar_hu HU-XXX para trabajar una HU.
```

**Cuándo Usarlo:**
- Para ver el estado del backlog
- Para elegir qué HU trabajar
- Para revisar el progreso general

---

### `*help`

**Descripción:** Muestra ayuda rápida con todos los comandos disponibles.

**Formato:**
```
*help
```

**Salida Esperada:**
```
🤖 Sistema de Comandos COCHAS

┌─────────────────────────────────────────────────────┐
│ PREFIJO │ PROPÓSITO              │ EJEMPLO         │
├─────────────────────────────────────────────────────┤
│    *    │ Comandos orquestador   │ *roles, *status │
│    +    │ Activar rol            │ +ONAD, +ARCHDEV │
│    >    │ Ejecutar herramienta   │ >refinar_hu     │
└─────────────────────────────────────────────────────┘

📋 Comandos del Orquestador (*):
  *roles   - Listar roles disponibles
  *status  - Ver estado de sesión
  *HU      - Listar historias de usuario
  *help    - Mostrar esta ayuda

🎭 Activar Roles (+):
  +ONAD      - Arquitecto ONAD
  +ARCHDEV   - ArchDev Pro
  +REFINADOR - Refinador HU
  +ARTESANO  - Artesano de Commits
  +DEVOPS    - Arquitecto DevOps

🛠️ Herramientas (>) - Requiere rol activo:
  >nombre_herramienta [parámetros]

📚 Documentación: guia_comandos.md
```

---

## Activación de Roles (`+`)

Los comandos con `+` activan un rol específico.

---

### `+<ROL>`

**Descripción:** Activa un rol específico en la sesión.

**Formato:**
```
+ONAD
+ARCHDEV
+REFINADOR
+ARTESANO
+DEVOPS
```

**Proceso Interno:**
1. Busca el rol en `personas/roles-activos.md`
2. Carga el archivo del rol desde `personas/`
3. Actualiza `session_state.json`
4. Presenta el saludo del rol activado

**Salida Esperada:**
```
🔄 Cambio de Rol

Rol anterior: Ninguno
Rol nuevo: Arquitecto ONAD (+ONAD)

---

👋 ¡Hola! Soy el **Arquitecto ONAD**, especialista en arquitectura de software...

🛠️ Herramientas Disponibles:
  >tomar_contexto
  >define_arquitectura
  >generar_adr

💡 Usa >tomar_contexto para analizar el proyecto.
```

**Cuándo Usarlo:**
- Al comenzar una tarea que requiere expertise específica
- Para cambiar de contexto de trabajo

---

### Tabla de Roles y Herramientas

| Comando | Rol | Herramientas Disponibles |
|---------|-----|--------------------------|
| `+ONAD` | Arquitecto ONAD | `>tomar_contexto`, `>define_arquitectura`, `>generar_adr` |
| `+ARCHDEV` | ArchDev Pro | `>refactorizar`, `>crear_pruebas`, `>analizar_code_smells`, `>ejecutar_plan` |
| `+REFINADOR` | Refinador HU | `>refinar_hu`, `>validar_hu`, `>planificar_hu` |
| `+ARTESANO` | Artesano de Commits | `>generar_commit` |
| `+DEVOPS` | Arquitecto DevOps | `>diagnosticar_devops` |

---

## Ejecución de Herramientas (`>`)

Los comandos con `>` ejecutan herramientas del rol activo.

---

### `>herramienta [parámetros]`

**Descripción:** Ejecuta una herramienta del rol activo.

**Formato:**
```
>nombre_herramienta
>nombre_herramienta parámetro1
>nombre_herramienta parámetro1 parámetro2
```

**Requisitos:**
- ✅ Debe haber un rol activo (`+ROL` previo)
- ✅ La herramienta debe pertenecer al rol activo

**Ejemplos por Rol:**

**Con +ONAD activo:**
```
>tomar_contexto
>define_arquitectura
>generar_adr ADR-001
```

**Con +ARCHDEV activo:**
```
>refactorizar src/auth/login.java
>crear_pruebas src/services/UserService.java
>analizar_code_smells
```

**Con +REFINADOR activo:**
```
>refinar_hu HU-001
>validar_hu HU-001
>planificar_hu HU-001
```

**Con +ARTESANO activo:**
```
>generar_commit
```

**Con +DEVOPS activo:**
```
>diagnosticar_devops
```

---

## Casos de Uso Comunes

### Caso 1: Primera Vez en el Sistema

```bash
# Paso 1: Ver ayuda
*help

# Paso 2: Ver roles disponibles
*roles

# Paso 3: Activar primer rol
+ONAD

# Paso 4: Analizar proyecto
>tomar_contexto

# Paso 5: Ver estado
*status
```

---

### Caso 2: Refinar una Historia de Usuario

```bash
# Ver HUs disponibles
*HU

# Activar rol de refinamiento
+REFINADOR

# Refinar la HU específica
>refinar_hu HU-001

# Validar el refinamiento
>validar_hu HU-001
```

---

### Caso 3: Implementar Código

```bash
# Activar rol de desarrollo
+ARCHDEV

# Ejecutar plan de desarrollo
>ejecutar_plan HU-001

# Crear pruebas
>crear_pruebas src/services/AuthService.java

# Analizar code smells
>analizar_code_smells
```

---

### Caso 4: Generar Commit

```bash
# Activar rol de commits
+ARTESANO

# Generar mensaje de commit
>generar_commit
```

---

### Caso 5: Cambiar Entre Roles

```bash
# Verificar rol actual
*status

# Cambiar a otro rol
+ARCHDEV

# Continuar trabajando con nuevo rol
>refactorizar src/main/App.java
```

---

## Gestión de Errores

### Error: Rol No Existe

**Entrada:**
```
+DEVELOPER
```

**Salida:**
```
❌ El rol 'DEVELOPER' no existe en el sistema.
💡 Usa *roles para ver la lista completa de roles disponibles.
```

---

### Error: Herramienta Sin Rol Activo

**Entrada:**
```
>refactorizar
```
(Sin tener un rol activo)

**Salida:**
```
❌ Error: Debes activar un rol primero con +COMANDO
💡 Usa *roles para ver los roles disponibles.
```

---

### Error: Herramienta No Disponible en Rol

**Entrada:**
```
+ARTESANO
>refinar_hu HU-001
```

**Salida:**
```
❌ La herramienta 'refinar_hu' no está disponible en el rol 'Artesano de Commits'.

🛠️ Herramientas disponibles para este rol:
  >generar_commit

💡 Para usar 'refinar_hu', activa el rol con: +REFINADOR
```

---

### Error: Herramienta No Existe

**Entrada:**
```
+ARCHDEV
>compilar_proyecto
```

**Salida:**
```
❌ La herramienta 'compilar_proyecto' no existe en el sistema.

🛠️ Herramientas disponibles para 'ArchDev Pro':
  >refactorizar
  >crear_pruebas
  >analizar_code_smells
  >ejecutar_plan
```

---

## 💡 Tips y Mejores Prácticas

### Tip 1: Siempre Empieza con `*roles`
```bash
*roles  # Ver qué roles hay disponibles
```

### Tip 2: Verifica el Estado Regularmente
```bash
*status  # Ver rol activo y progreso
```

### Tip 3: Analiza el Proyecto Una Vez
```bash
+ONAD
>tomar_contexto  # Se guarda y reutiliza por otros roles
```

### Tip 4: Secuencia Típica de Trabajo
```bash
*HU                    # Ver qué HUs hay
+REFINADOR             # Activar rol
>refinar_hu HU-001     # Trabajar la HU
+ARCHDEV               # Cambiar a desarrollo
>ejecutar_plan HU-001  # Implementar
+ARTESANO              # Cambiar a commits
>generar_commit        # Crear commit
```

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | 2025-10-16 | Versión inicial con comandos `/cochas` |
| 2.0 | 2025-10-16 | Documentación completa de `/cochas` |
| 3.0 | 2026-01-05 | ✅ **Nuevo sistema de prefijos**<br>✅ `*` para comandos orquestador<br>✅ `+` para activar roles<br>✅ `>` para herramientas<br>✅ Eliminados comandos `/cochas` |

---

## 📚 Documentación Relacionada

- **[Orquestador](core-cochas.md)** - Documentación técnica del orquestador
- **[Roles Activos](personas/roles-activos.md)** - Lista completa de roles
- **[Herramientas](herramientas/herramientas-activas.md)** - Lista de herramientas
- **[Ciclo de Vida](guia_ciclo_vida_tareas.md)** - Flujo de tareas

---

**¿Necesitas ayuda?** Usa `*help` en cualquier momento.
