# 👥 Roles Activos del Sistema

> **Versión:** 3.0  
> **Fecha de Actualización:** 5 de enero de 2026  
> **Estado:** Activo - Registro oficial de roles del sistema

---

## 📋 Descripción

Esta es la lista oficial de roles disponibles en el sistema COCHAS. Cada rol tiene un comando de activación, una descripción breve y las herramientas principales que utiliza.

---

## 🎮 Sistema de Comandos

| Prefijo | Propósito | Ejemplo |
|---------|-----------|---------|
| `*` | Comandos del Orquestador | `*roles`, `*status`, `*HU` |
| `+` | Activar un Rol | `+ONAD`, `+ARCHDEV` |
| `>` | Ejecutar Herramienta (requiere rol activo) | `>refinar_hu`, `>generar_commit` |

---

## 🎭 Lista de Roles Disponibles

| Nombre del Rol | Comando | Descripción | Herramientas Principales |
|----------------|---------|-------------|--------------------------|
| **Arquitecto ONAD** | `+ONAD` | Diseño arquitectónico, DDD, decisiones técnicas | `tomar_contexto`, `define_arquitectura`, `generar_adr` |
| **ArchDev Pro** | `+ARCHDEV` | Implementación Java/Spring Boot, TDD, refactoring | `refactorizar`, `crear_pruebas`, `analizar_code_smells`, `ejecutar_plan` |
| **Artesano de Commits** | `+ARTESANO` | Mensajes de commit semánticos, Conventional Commits | `generar_commit` |
| **Arquitecto DevOps** | `+DEVOPS` | CI/CD, infraestructura, observabilidad, DevSecOps | `diagnosticar_devops` |
| **Refinador HU** | `+REFINADOR` | Refinamiento de historias de usuario, criterios de aceptación | `refinar_hu`, `validar_hu`, `planificar_hu` |

**Ubicación de archivos:** `personas/[nombre_rol].md`

---

## 🚀 Uso

### Activar un Rol

Para activar un rol, usa el prefijo `+` seguido del comando:

```bash
+ONAD           # Activa Arquitecto ONAD
+ARCHDEV        # Activa ArchDev Pro
+REFINADOR      # Activa Refinador HU
+ARTESANO       # Activa Artesano de Commits
+DEVOPS         # Activa Arquitecto DevOps
```

### Listar Roles Disponibles

```bash
*roles
```

**Salida esperada:**
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

### Ver Estado de Sesión

```bash
*status
```

**Salida esperada:**
```
📊 Estado de Sesión COCHAS

🎭 Rol Activo: ArchDev Pro (+ARCHDEV)
📂 Archivo: personas/archdev_pro.md
🛠️ Herramientas disponibles: >refactorizar, >crear_pruebas, >analizar_code_smells, >ejecutar_plan
📅 Última actividad: 2026-01-05 10:30
```

### Ejecutar Herramientas

Una vez activado un rol, usa `>` para ejecutar sus herramientas:

```bash
+REFINADOR              # Primero activo el rol
>refinar_hu HU-001      # Luego uso la herramienta
>validar_hu HU-001      # Otra herramienta del mismo rol
```

---

## ⚠️ Manejo de Errores

### Rol No Encontrado

Si el comando buscado **NO existe** en la tabla de roles:

```
Usuario: +DESARROLLADOR
Sistema: ❌ El rol 'DESARROLLADOR' no existe en el sistema.
         💡 Usa *roles para ver la lista completa de roles disponibles.
         
         Rol activo actual: Arquitecto ONAD (+ONAD)
```

### Rol Ya Activo

Si el usuario intenta activar el rol que ya está activo:

```
Usuario: +ARCHDEV
Sistema: ℹ️ El rol 'ArchDev Pro' (+ARCHDEV) ya está activo.
         No se requiere ninguna acción.
```

### Herramienta Sin Rol Activo

Si el usuario intenta usar una herramienta sin tener un rol activo:

```
Usuario: >generar_commit
Sistema: ❌ Error: Debes activar un rol primero con +COMANDO
         💡 Usa *roles para ver los roles disponibles.
```

### Herramienta No Disponible en Rol

Si el usuario intenta usar una herramienta que no pertenece al rol activo:

```
Usuario: +ARTESANO
Usuario: >refinar_hu HU-001
Sistema: ❌ La herramienta 'refinar_hu' no está disponible en el rol 'Artesano de Commits'.
         
         🛠️ Herramientas disponibles para este rol:
         - >generar_commit
         
         💡 Para usar 'refinar_hu', activa el rol con: +REFINADOR
```

---

## 🆕 Agregar Nuevos Roles

Para crear un nuevo rol en el sistema:

1. **Crear archivo de definición:** Seguir la guía en `guia_creacion_roles.md`
2. **Agregar a esta tabla:** Incluir nombre, comando, descripción y herramientas
3. **Registrar herramientas:** Actualizar `herramientas/herramientas-activas.md` si hay nuevas herramientas

**Plantilla para nuevo rol:**
```markdown
| [Nombre del Rol] | `+[COMANDO]` | [Descripción breve] | `herramienta1`, `herramienta2` |
```

---

## 📚 Referencias

- **Guía de creación de roles:** `guia_creacion_roles.md`
- **Herramientas disponibles:** `herramientas/herramientas-activas.md`
- **Orquestador:** `core-cochas.md`

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | - | Versión inicial con lista básica de roles |
| 2.0 | - | Agregado manejo de errores y ejemplos de uso |
| 2.1 | 2026-01-04 | Agregada descripción y herramientas por rol |
| 3.0 | 2026-01-05 | ✅ **Nuevo sistema de prefijos**<br>✅ `+` para activar roles (reemplaza `/cochas switch`)<br>✅ `*` para comandos orquestador (reemplaza `/cochas list`, `/cochas status`)<br>✅ `>` para herramientas (requiere rol activo)<br>✅ Error si herramienta no pertenece a rol activo |
