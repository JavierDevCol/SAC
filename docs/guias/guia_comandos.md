# 📋 Guía Completa de Comandos del Sistema

> **Sistema:** SAC - Sistema Agéntico COCHAS  
> **Versión:** 7.3.0  
> **Última Actualización:** 23 de abril de 2026

---

## 📖 Índice

- [Sistema de Prefijos](#sistema-de-prefijos)
- [Invocar Agentes (@)](#invocar-agentes-)
- [Ejecución de Herramientas (>)](#ejecución-de-herramientas-)
- [Casos de Uso Comunes](#casos-de-uso-comunes)
- [Gestión de Errores](#gestión-de-errores)

---

## Sistema de Prefijos

El sistema SAC usa **1 prefijo** principal para ejecutar herramientas:

| Prefijo | Propósito | Requiere Agente Activo | Ejemplos |
|---------|-----------|----------------------|----------|
| `@` | **Invocar un Agente** | ❌ No | `@arquitecto`, `@desarrollador` |
| `>` | **Ejecutar una Herramienta** | ✅ Sí | `>refinar_hu`, `>generar_commit` |

### Regla Principal

```
@ = Invocar agente en Copilot Chat
> = Ejecutar herramienta (con agente activo)
```

---

## Invocar Agentes (`@`)

En Copilot Chat escribe `@nombre_agente` para activar un agente SAC.

---

### Tabla de Agentes

| Invocación | Agente | Herramientas Disponibles |
|------------|--------|--------------------------|
| `@arquitecto` | Arquitecto | `>tomar_contexto`, `>analizar_stack`, `>init_reglas_arquitectonicas`, `>generar_adr`, `>validar_hu`, `>planificar_hu` |
| `@desarrollador` | Desarrollador | `>tomar_contexto`, `>analizar_stack`, `>generar_adr`, `>ejecutar_plan`, `>crear_pruebas`, `>analizar_code_smells`, `>generar_commit` |
| `@devops` | DevOps | `>tomar_contexto`, `>generar_adr`, `>diagnosticar_devops`, `>generar_commit` |
| `@analista_historias` | Analista de Requisitos | `>tomar_contexto`, `>refinar_hu`, `>generar_commit` |
| `@cronista_de_cambios` | Cronista de Cambios | `>generar_commit` |

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

**Con @arquitecto activo:**
```
>tomar_contexto
>analizar_stack
>generar_adr ADR-001
```

**Con @desarrollador activo:**
```
>crear_pruebas src/services/UserService.java
>analizar_code_smells
```

**Con @analista_historias activo:**
```
>refinar_hu HU-001
>validar_hu HU-001
>planificar_hu HU-001
```

**Con @cronista_de_cambios activo:**
```
>generar_commit
```

**Con @devops activo:**
```
>diagnosticar_devops
```

---

## Casos de Uso Comunes

### Caso 1: Primera Vez en el Sistema

```bash
# Paso 1: Analizar el proyecto con el Arquitecto
@arquitecto
>tomar_contexto

# Paso 2: Analizar el stack tecnológico
>analizar_stack
```

---

### Caso 2: Refinar una Historia de Usuario

```bash
# Activar agente de refinamiento
@analista_historias

# Refinar la HU específica
>refinar_hu HU-001

# Validar el refinamiento con Arquitecto
@arquitecto
>validar_hu HU-001
```

---

### Caso 3: Implementar Código

```bash
# Activar agente de desarrollo
@desarrollador

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
# Activar agente de commits
@cronista_de_cambios

# Generar mensaje de commit
>generar_commit
```

---

### Caso 5: Cambiar Entre Agentes

```bash
# Abrir nuevo chat con otro agente
@desarrollador

# Continuar trabajando
>ejecutar_plan HU-001
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
❌ La herramienta 'refinar_hu' no está disponible en el rol 'Cronista de Cambios'.

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

- **[Roles Activos](guia_roles_activos.md)** - Lista completa de roles
- **[Herramientas](../HERRAMIENTAS.md)** - Lista de herramientas
- **[Ciclo de Vida](guia_ciclo_vida_tareas.md)** - Flujo de tareas

---

**¿Necesitas ayuda?** Usa `*help` en cualquier momento.
