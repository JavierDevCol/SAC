# 🛠️ Herramientas Activas del Sistema

> **Versión:** 3.1  
> **Fecha de Actualización:** 5 de enero de 2026  
> **Estado:** Activo - Registro oficial de herramientas del sistema

---

## 📋 Descripción

Esta es la lista oficial de herramientas disponibles en el sistema COCHAS. Cada herramienta tiene un comando de activación, los roles que pueden ejecutarla y la ruta donde se encuentra su definición completa.

---

## 🎮 Sistema de Comandos

| Prefijo | Propósito | Ejemplo |
|---------|-----------|---------|
| `>` | Ejecutar Herramienta (requiere rol activo) | `>refinar_hu`, `>generar_commit` |
| `+` | Activar un Rol | `+ONAD`, `+ARCHDEV` |
| `*` | Comandos del Orquestador | `*roles`, `*status`, `*HU` |

---

## 📦 Lista de Herramientas Disponibles

| Herramienta | Comando | Roles Compatibles | Ruta |
|-------------|---------|-------------------|------|
| **Tomar Contexto** | `>tomar_contexto` | ONAD, ARCHDEV, DEVOPS, REFINADOR | `herramientas/tomar_contexto.md` |
| **Definir Arquitectura** | `>define_arquitectura` | ONAD | `herramientas/define_arquitectura.md` |
| **Generar ADR** | `>generar_adr` | ONAD, ARCHDEV | `herramientas/generar_adr.md` |
| **Validar HU** | `>validar_hu` | ONAD | `herramientas/validar_hu.md` |
| **Planificar HU** | `>planificar_hu` | ONAD | `herramientas/planificar_hu.md` |
| **Refactorizar** | `>refactorizar` | ARCHDEV | `herramientas/refactorizar.md` |
| **Analizar Code Smells** | `>analizar_code_smells` | ARCHDEV | `herramientas/analizar_code_smells.md` |
| **Solucionar Smells** | `>solucionar_smells` | ARCHDEV | `herramientas/solucionar_smells.md` |
| **Crear Pruebas** | `>crear_pruebas` | ARCHDEV | `herramientas/crear_pruebas.md` |
| **Verificar Pruebas** | `>verifica_pruebas` | ARCHDEV | `herramientas/verifica_pruebas.md` |
| **Ejecutar Plan** | `>ejecutar_plan` | ARCHDEV | `herramientas/ejecutar_plan.md` |
| **Generar Commit** | `>generar_commit` | ARTESANO | `herramientas/generar_commit.md` |
| **Diagnosticar DevOps** | `>diagnosticar_devops` | DEVOPS | `herramientas/diagnosticar_devops.md` |
| **Refinar HU** | `>refinar_hu` | REFINADOR | `herramientas/refinar_hu.md` |

---

## 🚀 Uso

### Ejecutar una Herramienta

Para ejecutar una herramienta, **primero debe haber un rol activo** y luego usar el prefijo `>`:

```bash
+ARCHDEV                    # Primero activo el rol
>analizar_code_smells       # Luego uso la herramienta
>crear_pruebas              # Otra herramienta del mismo rol
```

### Ver Herramientas del Rol Activo

Al activar un rol, el sistema muestra automáticamente las herramientas disponibles:

```
+ARCHDEV

🔄 Rol activado: ArchDev Pro

🛠️ Herramientas disponibles:
  >tomar_contexto
  >refactorizar
  >analizar_code_smells
  >solucionar_smells
  >crear_pruebas
  >verifica_pruebas
  >ejecutar_plan
  >generar_adr
```

---

## ⚠️ Manejo de Errores

### Herramienta Sin Rol Activo

Si se intenta ejecutar una herramienta **sin tener un rol activo**:

```
Usuario: >refactorizar

Sistema: ❌ No hay ningún rol activo. Las herramientas requieren un rol cargado.

         💡 La herramienta 'refactorizar' puede ser ejecutada por:
         
         • ArchDev Pro - Activar con: +ARCHDEV
```

### Herramienta No Compatible con Rol Activo

Si se intenta ejecutar una herramienta **con un rol activo incompatible**:

```
Usuario: >diagnosticar_devops
(Rol activo: ArchDev Pro)

Sistema: ❌ El rol 'ArchDev Pro' no puede ejecutar 'diagnosticar_devops'.

         💡 Esta herramienta puede ser ejecutada por:
         
         • Arquitecto DevOps - Activar con: +DEVOPS
         
         ¿Deseas cambiar de rol?
```

### Herramienta No Encontrada

Si la herramienta **NO existe** en el sistema:

```
Usuario: >compilar_proyecto
(Rol activo: ArchDev Pro)

Sistema: ❌ La herramienta 'compilar_proyecto' no existe en el sistema.

         🛠️ Herramientas disponibles para 'ArchDev Pro':
         
         • >tomar_contexto
         • >generar_adr
         • >refactorizar
         • >analizar_code_smells
         • >solucionar_smells
         • >crear_pruebas
         • >verifica_pruebas
         • >ejecutar_plan
```

---

## 📊 Herramientas por Rol

### +ONAD (Arquitecto Onad)
| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Definir Arquitectura | `>define_arquitectura` |
| Generar ADR | `>generar_adr` |
| Validar HU | `>validar_hu` |
| Planificar HU | `>planificar_hu` |

### +ARCHDEV (ArchDev Pro)
| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Refactorizar | `>refactorizar` |
| Analizar Code Smells | `>analizar_code_smells` |
| Solucionar Smells | `>solucionar_smells` |
| Crear Pruebas | `>crear_pruebas` |
| Verificar Pruebas | `>verifica_pruebas` |
| Ejecutar Plan | `>ejecutar_plan` |
| Generar ADR | `>generar_adr` |

### +DEVOPS (Arquitecto DevOps)
| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Diagnosticar DevOps | `>diagnosticar_devops` |

### +REFINADOR (Refinador HU)
| Herramienta | Comando |
|-------------|---------|
| Tomar Contexto | `>tomar_contexto` |
| Refinar HU | `>refinar_hu` |

### +ARTESANO (Artesano de Commits)
| Herramienta | Comando |
|-------------|---------|
| Generar Commit | `>generar_commit` |

---

## 📊 Categorías de Herramientas

### Por Tipo de Función

| Categoría | Herramientas |
|-----------|--------------|
| **Contexto** | `tomar_contexto` |
| **Arquitectura** | `define_arquitectura`, `generar_adr` |
| **Código** | `refactorizar`, `analizar_code_smells`, `solucionar_smells` |
| **Pruebas** | `crear_pruebas`, `verifica_pruebas` |
| **Documentación** | `generar_commit`, `generar_adr` |
| **DevOps** | `diagnosticar_devops` |
| **HU/Requisitos** | `refinar_hu`, `validar_hu`, `planificar_hu` |
| **Ejecución** | `ejecutar_plan` |

### Herramientas Universales vs Especializadas

**Universales (múltiples roles):**
- `tomar_contexto` - ONAD, ARCHDEV, DEVOPS, REFINADOR
- `generar_adr` - ONAD, ARCHDEV

**Especializadas (un solo rol):**
- `diagnosticar_devops` - Solo DEVOPS
- `generar_commit` - Solo ARTESANO
- `refinar_hu` - Solo REFINADOR
- `validar_hu` - Solo ONAD
- `planificar_hu` - Solo ONAD

---

## 🆕 Agregar Nuevas Herramientas

Para crear una nueva herramienta en el sistema:

1. **Crear archivo de definición** en `herramientas/[nombre_herramienta].md`
2. **Agregar a esta tabla** con nombre, comando, roles compatibles y ruta
3. **Actualizar roles afectados** en `personas/[rol].md` si corresponde

**Plantilla para nueva herramienta:**
```markdown
| [Nombre Herramienta] | `>[comando]` | ROL1, ROL2 | `herramientas/[archivo].md` |
```

---

## 📚 Referencias

- **Roles disponibles:** `personas/roles-activos.md`
- **Orquestador:** `cochas.agent.md`
- **Guía de comandos:** `guia_comandos.md`

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | - | Versión inicial con lista básica de herramientas |
| 2.0 | - | Agregado manejo de errores y validaciones |
| 3.0 | 2026-01-05 | ✅ Nuevo sistema de prefijos (`>` para herramientas)<br>✅ Categorización de herramientas |
| 3.1 | 2026-01-05 | ✅ **Eliminada `asignar_responsable`** (no era ejecutable por roles)<br>✅ **Sincronizada con `roles-activos.md`**<br>✅ Agregada sección "Herramientas por Rol"<br>✅ Agregadas `validar_hu` y `planificar_hu` a ONAD<br>✅ Agregado `ejecutar_plan` a ARCHDEV |
