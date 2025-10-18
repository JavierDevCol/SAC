# 🤖 Sistema de Orquestación de Agentes IA (Cochas)

> **Versión:** 2.0  
> **Última actualización:** 16 de octubre de 2025

---

## 📖 Índice

- [¿Qué es este sistema?](#-qué-es-este-sistema)
- [Conceptos Clave](#-conceptos-clave)
- [Inicio Rápido](#-inicio-rápido)
- [Comandos Principales](#-comandos-principales)
- [Documentación Detallada](#-documentación-detallada)
- [Estructura del Proyecto](#-estructura-del-proyecto)

---

## 🎯 ¿Qué es este sistema?

**Cochas** es un sistema avanzado de **orquestación de agentes de IA especializados** que permite gestionar múltiples roles (personalidades) y herramientas de forma eficiente y coordinada.

### ¿En qué se diferencia de otros sistemas de prompts?

| Característica | Sistema Tradicional | Cochas |
|----------------|---------------------|---------|
| **Gestión de Roles** | Manual, reiniciando sesión | Cambio dinámico con `/cochas switch` |
| **Estado de Sesión** | Se pierde entre conversaciones | Persistente en `session_state.json` |
| **Herramientas** | Cargadas todas al inicio | Lazy loading (carga bajo demanda) |
| **Coordinación** | Usuario decide todo | Orquestador sugiere roles proactivamente |
| **Contexto del Proyecto** | Debe repetirse | Se analiza una vez con `tomar_contexto` |
| **Trazabilidad** | Inexistente | Historial completo de tareas y roles |

---

## 🧩 Conceptos Clave

### 1. **El Orquestador** (`/cochas`)
El núcleo del sistema. Gestiona:
- ✅ Activación y cambio de roles
- ✅ Estado persistente de la sesión
- ✅ Carga optimizada de herramientas
- ✅ Sugerencias proactivas de roles
- ✅ Validaciones automáticas

### 2. **Roles/Personas** (`/personas/`)
Agentes especializados con personalidades únicas:
- **ONAD** (`Arquitecto Onad`) - Arquitectura estratégica y decisiones de alto nivel
- **ARCHDEV** (`ArchDev Pro`) - Implementación de código y refactoring
- **DEVOPS** (`Arquitecto DevOps`) - Infraestructura, pipelines y deployment
- **REFINADOR** (`Refinador HU`) - Refinamiento de historias de usuario
- **ARTESANO** (`Artesano de Commits`) - Creación de mensajes de commit profesionales

### 3. **Herramientas** (`/herramientas/`)
Funcionalidades ejecutables que los roles pueden invocar:
- `tomar_contexto` - Analiza el proyecto completo
- `define_arquitectura` - Diseña arquitecturas
- `refactorizar` - Mejora código existente
- `crear_pruebas` - Genera tests
- `diagnosticar_devops` - Analiza infraestructura
- `generar_commit` - Crea mensajes de commit
- Y más...

### 4. **Sistema de Estado Persistente**
- **`session_state.json`** - Memoria de la sesión (roles, tareas, eventos)
- **`contexto_proyecto.md`** - Análisis del proyecto (se crea una vez)
- **`backlog_desarrollo.md`** - Tareas pendientes con estados de validación

---

## 🚀 Inicio Rápido

### Paso 1: Iniciar el Orquestador
```
/cochas help
```
Esto te mostrará todos los comandos disponibles y verificará el estado del sistema.

### Paso 2: Ver Roles Disponibles
```
/cochas list
```
Muestra la lista completa de roles con sus comandos de activación.

### Paso 3: Activar tu Primer Rol
```
/cochas +ONAD
```
o
```
/cochas switch ONAD
```

### Paso 4: Analizar el Proyecto (Recomendado)
```
> tomar_contexto
```
Esto creará un análisis completo del proyecto que persistirá entre sesiones.

### Paso 5: Usar Herramientas del Rol
```
> define_arquitectura
> refactorizar
> crear_pruebas
```

---

## 📋 Comandos Principales

### Comandos del Orquestador

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `/cochas list` | Lista todos los roles disponibles | - |
| `/cochas +<ROL>` | Activa un rol | `/cochas +ONAD` |
| `/cochas switch <ROL>` | Activa un rol (alternativa) | `/cochas switch ARCHDEV` |
| `/cochas status` | Muestra el estado actual de la sesión | - |
| `/cochas assign <tarea>` | Sugiere el mejor rol para una tarea | `/cochas assign "Necesito optimizar base de datos"` |
| `/cochas history` | Muestra historial completo de la sesión | - |
| `/cochas reload` | Recarga el rol activo | - |
| `/cochas reset` | Reinicia la sesión (con confirmación) | - |
| `/cochas export` | Exporta el estado de la sesión | - |
| `/cochas help` | Muestra ayuda de comandos | - |

### Comandos de Herramientas

| Comando | Descripción | Requiere Rol Activo |
|---------|-------------|---------------------|
| `> <herramienta>` | Ejecuta una herramienta | ✅ Sí |
| `-> <herramienta>` | Ejecuta una herramienta (alternativa) | ✅ Sí |

**Ejemplo:**
```
> tomar_contexto
-> refactorizar
```

---

## 📚 Documentación Detallada

### Guías Especializadas

Para profundizar en aspectos específicos del sistema, consulta estas guías:

- **[📋 Guía de Comandos](guia_comandos.md)** - Explicación detallada de cada comando con ejemplos
- **[👥 Guía de Roles Activos](guia_roles_activos.md)** - Descripción completa de cada rol y cuándo usarlo
- **[🔄 Guía del Ciclo de Vida de Tareas](guia_ciclo_vida_tareas.md)** - Cómo fluyen las tareas por el sistema
- **[🛠️ Guía de Creación de Roles](guia_creacion_roles.md)** - Cómo crear tus propios roles personalizados

### Documentación Técnica Avanzada

- **[`core-cochas.md`](core-cochas.md)** - Arquitectura completa del orquestador
- **[`README_PLANTILLA.md`](README_PLANTILLA.md)** - Sistema completo de plantillas para roles
- **[`help/estructura_session_state.md`](help/estructura_session_state.md)** - Estructura del archivo de estado

---

## 📁 Estructura del Proyecto

```
ia_prompts/
├── README.md                          ← Este archivo
├── core-cochas.md                     ← Núcleo del orquestador
├── guia_comandos.md                   ← Guía de comandos del sistema
├── guia_roles_activos.md              ← Guía de roles disponibles
├── guia_ciclo_vida_tareas.md          ← Ciclo de vida de tareas
├── guia_creacion_roles.md             ← Crear roles personalizados
│
├── personas/                          ← Roles/Agentes disponibles
│   ├── roles-activos.md               ← Registro central de roles
│   ├── arquitecto_onad.md             ← Arquitecto estratégico
│   ├── archdev_pro.md                 ← Desarrollador pragmático
│   ├── arquitecto_devops.md           ← Especialista en infraestructura
│   ├── refinador_hu.md                ← Refinador de historias
│   └── artesano_de_commits.md         ← Especialista en commits
│
├── herramientas/                      ← Herramientas ejecutables
│   ├── herramientas-activas.md        ← Registro central de herramientas
│   ├── tomar_contexto.md              ← Análisis profundo del proyecto
│   ├── refactorizar.md                ← Mejora de código
│   ├── define_arquitectura.md         ← Diseño arquitectónico
│   ├── crear_pruebas.md               ← Generación de tests
│   ├── analizar_code_smells.md        ← Detección de problemas
│   ├── solucionar_smells.md           ← Solución de code smells
│   ├── verifica_pruebas.md            ← Validación de tests
│   ├── diagnosticar_devops.md         ← Análisis de infraestructura
│   ├── refinar_hu.md                  ← Refinamiento de historias
│   ├── generar_commit.md              ← Mensajes de commit profesionales
│   ├── generar_adr.md                 ← Documentación de decisiones
│   └── asignar_responsable.md         ← Asignación inteligente de roles
│
├── help/                              ← Ayuda y referencias
│   └── estructura_session_state.md    ← Estructura del estado de sesión
│
├── ejemplos/                          ← Ejemplos de uso
│   └── herramientas/                  ← Ejemplos de herramientas en acción
│
└── [EN EL PROYECTO DEL USUARIO]
    └── cochas/                        ← Carpeta del sistema (auto-creada)
        ├── session/                   ← Estado temporal (en .gitignore)
        │   ├── session_state.json     ← Estado de la sesión
        │   └── exports/               ← Backups exportados
        └── artifacts/                 ← Documentación del proyecto
            ├── contexto_proyecto.md   ← Análisis del proyecto
            ├── backlog_desarrollo.md  ← Backlog de tareas
            └── adr/                   ← Architecture Decision Records
```

---

## 🚀 Inicio Rápido

### Paso 1: Activar el Orquestador

Carga el archivo `core-cochas.md` en tu herramienta de IA (Claude, GPT-4, etc.)

### Paso 2: Ver Roles Disponibles

```bash
/cochas list
```

Verás una lista de todos los roles disponibles con sus comandos de activación.

### Paso 3: Activar un Rol

```bash
/cochas +ONAD
```

O alternativamente:

```bash
/cochas switch ONAD
```

### Paso 4: Usar Herramientas

Una vez activado un rol, puedes ejecutar sus herramientas:

```bash
> tomar_contexto
```

O alternativamente:

```bash
-> define_arquitectura
```

### Paso 5: Ver el Estado

```bash
/cochas status
```

Te mostrará:
- Rol activo actual
- Estado del contexto del proyecto
- Tareas completadas
- Historial de la sesión

---

## 📋 Flujo de Trabajo Típico

### Escenario 1: Nuevo Proyecto

```bash
# 1. Activar el arquitecto estratégico
/cochas +ONAD

# 2. Analizar el proyecto (automático al saludar a ONAD)
# Se crea automáticamente cochas/artifacts/contexto_proyecto.md

# 3. Diseñar la arquitectura
> define_arquitectura

# 4. Cambiar al desarrollador
/cochas +ARCHDEV

# 5. Implementar código
> refactorizar

# 6. Crear tests
> crear_pruebas
```

### Escenario 2: Refactoring de Código Existente

```bash
# 1. Activar el desarrollador pragmático
/cochas +ARCHDEV

# 2. Analizar problemas de código
> analizar_code_smells

# 3. Solucionar los problemas detectados
> solucionar_smells

# 4. Validar con tests
> verifica_pruebas
```

### Escenario 3: Sprint Planning

```bash
# 1. Activar el refinador de historias
/cochas +REFINADOR

# 2. Refinar historias de usuario
> refinar_hu

# 3. Cambiar al arquitecto para validación técnica
/cochas +ONAD
# Revisar viabilidad arquitectónica de las historias

# 4. Cambiar al desarrollador para estimación
/cochas +ARCHDEV
# Estimar esfuerzo de implementación
```

---

## 🔄 Gestión del Estado

### Persistencia Automática

El sistema mantiene el estado en:
- **`cochas/session/session_state.json`** - Estado de la sesión actual
- **`cochas/artifacts/contexto_proyecto.md`** - Contexto del proyecto analizado
- **`cochas/artifacts/backlog_desarrollo.md`** - Backlog de tareas de desarrollo

### Comandos de Estado

```bash
# Ver estado actual
/cochas status

# Ver historial completo
/cochas history

# Exportar estado (backup)
/cochas export
# Crea: cochas/session/exports/session_state_export_[fecha].json

# Reiniciar sesión (confirmación requerida)
/cochas reset
```

---

## 🤝 Contribuir

### Crear un Nuevo Rol
Consulta la **[Guía de Creación de Roles](guia_creacion_roles.md)** para aprender a:
1. Copiar la plantilla base
2. Definir personalidad y comandos
3. Registrar el rol en el sistema

### Crear una Nueva Herramienta
1. Crear archivo en `/herramientas/nueva_herramienta.md`
2. Registrarla en `/herramientas/herramientas-activas.md`
3. Asignarla a uno o más roles

---

## 📞 Soporte

- **Comandos:** Consulta [`guia_comandos.md`](guia_comandos.md)
- **Roles:** Consulta [`guia_roles_activos.md`](guia_roles_activos.md)
- **Arquitectura:** Consulta [`core-cochas.md`](core-cochas.md)
- **Problemas:** Usa `/cochas status` para diagnosticar el estado

---

## 📝 Notas de Versión

### v2.0 (Octubre 2025)
- ✅ Sistema de estado persistente con `session_state.json`
- ✅ Validación secuencial de tareas
- ✅ Comando `/cochas assign` para sugerencias inteligentes
- ✅ Backlog de desarrollo automatizado
- ✅ Mejoras en lazy loading de herramientas

### v1.0 (Octubre 2025)
- ✅ Orquestador básico con cambio de roles
- ✅ 5 roles iniciales (ONAD, ARCHDEV, DEVOPS, REFINADOR, ARTESANO)
- ✅ Sistema de herramientas modular

---

**¡Listo para empezar!** 🚀

Usa `/cochas help` para ver todos los comandos disponibles y comenzar tu primera sesión.
````
