# 🤖 Sistema de Orquestación de Agentes IA (COCHAS)

> **Versión:** 4.0  
> **Última actualización:** 6 de enero de 2026

---

## 📖 Índice

- [¿Qué es este sistema?](#-qué-es-este-sistema)
- [Conceptos Clave](#-conceptos-clave)
- [Inicio Rápido](#-inicio-rápido)
- [Sistema de Comandos](#-sistema-de-comandos)
- [Roles Disponibles](#-roles-disponibles)
- [Herramientas Disponibles](#-herramientas-disponibles)
- [Documentación Detallada](#-documentación-detallada)
- [Estructura del Proyecto](#-estructura-del-proyecto)

---

## 🎯 ¿Qué es este sistema?

**COCHAS** es un sistema de **agentes de IA especializados** que permite trabajar con roles (personalidades) y herramientas definidas en formato YAML estructurado.

### ¿En qué se diferencia de otros sistemas de prompts?

| Característica | Sistema Tradicional | COCHAS v4.0 |
|----------------|---------------------|-------------|
| **Roles** | Prompt único genérico | Agentes especializados por dominio |
| **Estado de Sesión** | Se pierde entre conversaciones | Persistente en `session_state.json` |
| **Herramientas** | Instrucciones dispersas | Herramientas estructuradas (`.tool.md`) |
| **Contexto del Proyecto** | Debe repetirse | Se analiza una vez con `>tomar_contexto` |
| **Trazabilidad** | Inexistente | Historial completo de tareas |
| **Formato** | Prompts en texto plano | YAML estructurado (`.agent.md`, `.tool.md`) |

### Modelo de Uso

Cada **agente/rol se carga en un chat independiente**. Esto permite:
- 🎯 **Contexto enfocado**: El agente mantiene su personalidad sin interferencias
- 📝 **Historial limpio**: Cada chat tiene su propia conversación
- 🔄 **Estado compartido**: Los agentes comparten información vía `session_state.json` y artefactos en `.SAC/`

---

## 🧩 Conceptos Clave

### 1. **Sistema de Prefijos**

| Prefijo | Propósito | Ejemplo |
|---------|-----------|---------|
| `+` | Identificador del Rol (en archivo) | `+ONAD`, `+ARCHDEV` |
| `>` | Ejecutar Herramienta | `>tomar_contexto`, `>refinar_hu` |
| `*` | Comandos del Sistema | `*roles`, `*status`, `*help` |

### 2. **Roles/Agentes** (`agentes/`)

Agentes especializados con personalidades únicas. **Cada agente se usa en un chat separado**:

| Rol | Archivo | Especialidad |
|-----|---------|--------------|
| **Arquitecto Onad** | `arquitecto_onad.agent.md` | Arquitectura estratégica y decisiones de alto nivel |
| **ArchDev Pro** | `archdev_pro.agent.md` | Implementación de código, refactoring y testing |
| **Arquitecto DevOps** | `arquitecto_devops.agent.md` | Infraestructura, pipelines y deployment |
| **Analista de Historias** | `refinador_hu.agent.md` | Refinamiento de historias de usuario |
| **Narrador de Cambios** | `artesano_de_commits.agent.md` | Creación de mensajes de commit profesionales |

### 3. **Herramientas** (`herramientas/`)

Funcionalidades ejecutables que los roles pueden invocar:

| Herramienta | Comando | Descripción |
|-------------|---------|-------------|
| Tomar Contexto | `>tomar_contexto` | Analiza el proyecto completo |
| Refinar HU | `>refinar_hu` | Refina historias de usuario |
| Validar HU | `>validar_hu` | Validación arquitectónica de HU |
| Planificar HU | `>planificar_hu` | Genera plan de implementación |
| Ejecutar Plan | `>ejecutar_plan` | Ejecuta planes de implementación |
| Crear Pruebas | `>crear_pruebas` | Genera tests unitarios e integración |
| Analizar Code Smells | `>analizar_code_smells` | Detecta problemas de diseño |
| Diagnosticar DevOps | `>diagnosticar_devops` | Analiza madurez DevOps |
| Generar Commit | `>generar_commit` | Crea mensajes Conventional Commits |

### 4. **Sistema de Estado Persistente**

Los agentes comparten información a través de archivos en el proyecto del usuario:

| Archivo | Ubicación | Propósito |
|---------|-----------|-----------|
| `session_state.json` | `.SAC/session/` | Memoria compartida entre agentes |
| `contexto_proyecto.md` | `.SAC/artifacts/` | Análisis del proyecto |
| `backlog_desarrollo.md` | `.SAC/artifacts/` | Backlog de HUs con estados |

---

## 🚀 Inicio Rápido

### Paso 1: Elegir el Agente Adecuado

| Necesitas... | Usa este agente |
|--------------|-----------------|
| Decisiones arquitectónicas | `arquitecto_onad.agent.md` |
| Implementar código/tests | `archdev_pro.agent.md` |
| CI/CD e infraestructura | `arquitecto_devops.agent.md` |
| Refinar historias de usuario | `refinador_hu.agent.md` |
| Crear mensajes de commit | `artesano_de_commits.agent.md` |

### Paso 2: Cargar el Agente en un Chat

1. Abre un **nuevo chat** en tu cliente de IA
2. Carga el archivo `.agent.md` correspondiente como contexto
3. El agente se presentará con su personalidad

### Paso 3: Analizar el Proyecto (Recomendado)

```
>tomar_contexto
```

### Paso 4: Usar Herramientas del Rol

```
>refinar_hu
>validar_hu
>crear_pruebas
```

### Paso 5: Ver Estado

```
*status
```

---

## 📋 Sistema de Comandos

### Comandos del Sistema (`*`)

| Comando | Descripción |
|---------|-------------|
| `*roles` | Lista todos los roles disponibles |
| `*status` | Muestra el estado actual de la sesión |
| `*HU` | Lista historias de usuario del backlog |
| `*help` | Muestra ayuda de comandos disponibles |

### Identificadores de Roles (`+`)

Cada agente tiene un identificador único:

| Identificador | Agente | Archivo |
|---------------|--------|---------|
| `+ONAD` | Arquitecto Onad | `arquitecto_onad.agent.md` |
| `+ARCHDEV` | ArchDev Pro | `archdev_pro.agent.md` |
| `+DEVOPS` | Arquitecto DevOps | `arquitecto_devops.agent.md` |
| `+REFINADOR` | Analista de Historias | `refinador_hu.agent.md` |
| `+ARTESANO` | Narrador de Cambios | `artesano_de_commits.agent.md` |

### Ejecución de Herramientas (`>`)

```
>tomar_contexto
>refinar_hu HU-001
>crear_pruebas --tipo=unitario
```

**Nota:** Las herramientas verifican que el rol activo sea compatible.

---

## 👥 Roles Disponibles

### +ONAD (Arquitecto Onad)
- **Archivo:** `agentes/arquitecto_onad.agent.md`
- **Tipo:** Arquitecto estratégico
- **Principio:** "No Comer Entero"
- **Herramientas:** `>tomar_contexto`, `>validar_hu`, `>planificar_hu`
- **Cuándo usar:** Decisiones arquitectónicas, validación de HUs, planificación

### +ARCHDEV (ArchDev Pro)
- **Archivo:** `agentes/archdev_pro.agent.md`
- **Tipo:** Ingeniero constructor
- **Principio:** "Código con Propósito"
- **Herramientas:** `>crear_pruebas`, `>analizar_code_smells`, `>ejecutar_plan`
- **Cuándo usar:** Implementación, refactoring, testing

### +DEVOPS (Arquitecto DevOps)
- **Archivo:** `agentes/arquitecto_devops.agent.md`
- **Tipo:** Mentor DevOps
- **Principio:** "Seguridad es No Negociable"
- **Herramientas:** `>tomar_contexto`, `>diagnosticar_devops`
- **Cuándo usar:** CI/CD, infraestructura, observabilidad

### +REFINADOR (Analista de Historias)
- **Archivo:** `agentes/refinador_hu.agent.md`
- **Tipo:** Analista técnico
- **Principio:** "Claridad Sobre Velocidad"
- **Herramientas:** `>refinar_hu`, `>tomar_contexto`
- **Cuándo usar:** Refinamiento de HUs, estimación, desglose técnico

### +ARTESANO (Narrador de Cambios)
- **Archivo:** `agentes/artesano_de_commits.agent.md`
- **Tipo:** Comunicador técnico
- **Principio:** "La Historia Importa"
- **Herramientas:** `>generar_commit`
- **Cuándo usar:** Documentar cambios con commits profesionales

---

## 🔧 Herramientas Disponibles

| Herramienta | Comando | Roles Autorizados |
|-------------|---------|-------------------|
| Tomar Contexto | `>tomar_contexto` | ONAD, ARCHDEV, DEVOPS, REFINADOR |
| Refinar HU | `>refinar_hu` | REFINADOR, ARCHDEV, DEVOPS |
| Validar HU | `>validar_hu` | ONAD |
| Planificar HU | `>planificar_hu` | ONAD |
| Ejecutar Plan | `>ejecutar_plan` | ARCHDEV |
| Crear Pruebas | `>crear_pruebas` | ARCHDEV |
| Analizar Code Smells | `>analizar_code_smells` | ARCHDEV |
| Diagnosticar DevOps | `>diagnosticar_devops` | DEVOPS |
| Generar Commit | `>generar_commit` | ARTESANO, ARCHDEV, DEVOPS, REFINADOR |

---

## 📋 Flujos de Trabajo Típicos

### Escenario 1: Nueva Historia de Usuario

```bash
# Chat 1: Cargar refinador_hu.agent.md
>refinar_hu
# El agente refina la HU y genera artefactos en .SAC/

# Chat 2: Cargar arquitecto_onad.agent.md
>validar_hu HU-001
>planificar_hu HU-001
# El agente lee el estado compartido y continúa el flujo

# Chat 3: Cargar archdev_pro.agent.md
>ejecutar_plan HU-001
# El agente implementa según el plan generado
```

### Escenario 2: Análisis de Código Existente

```bash
# Chat: Cargar archdev_pro.agent.md
>analizar_code_smells
>crear_pruebas

# Chat: Cargar artesano_de_commits.agent.md
>generar_commit
```

### Escenario 3: Evaluación DevOps

```bash
# Chat: Cargar arquitecto_devops.agent.md
>tomar_contexto
>diagnosticar_devops
```

---

## 📚 Documentación Detallada

### Guías

| Guía | Ubicación | Descripción |
|------|-----------|-------------|
| Guía de Comandos | `guias/guia_comandos.md` | Explicación detallada de comandos |
| Guía de Roles | `guias/guia_roles_activos.md` | Descripción completa de cada rol |
| Ciclo de Vida de Tareas | `guias/guia_ciclo_vida_tareas.md` | Flujo de tareas en el sistema |
| Creación de Roles | `guias/guia_creacion_roles.md` | Cómo crear roles personalizados |

### Plantillas

| Plantilla | Ubicación | Propósito |
|-----------|-----------|-----------|
| Plantilla de Agente | `plantillas/agente_plantilla.agent.md` | Crear nuevos roles |
| Plantilla de Herramienta | `plantillas/herramienta_plantilla.tool.md` | Crear nuevas herramientas |
| Índice de Plantillas | `README_PLANTILLA.md` | Guía central de plantillas |

### Referencias Técnicas

| Documento | Ubicación | Contenido |
|-----------|-----------|-----------|
| Roles del Sistema | `ROLES.md` | Índice de roles disponibles |
| Herramientas del Sistema | `HERRAMIENTAS.md` | Índice de herramientas disponibles |
| Configuración del Sistema | `config/CONFIG_SYSTEM.yaml` | Variables y rutas del sistema |

---

## 📁 Estructura del Proyecto

```
ia_prompts/
├── README.md                              ← Este archivo
├── README_PLANTILLA.md                    ← Índice de plantillas
├── ROLES.md                               ← Índice de roles del sistema
├── HERRAMIENTAS.md                        ← Índice de herramientas del sistema
├── CHANGELOG.md                           ← Historial de cambios
├── estructura_directorio.md               ← Documentación de estructura
│
├── agentes/                               ← Roles/Agentes (cargar en chat separado)
│   ├── arquitecto_onad.agent.md           ← Arquitecto estratégico
│   ├── archdev_pro.agent.md               ← Desarrollador pragmático
│   ├── arquitecto_devops.agent.md         ← Especialista en infraestructura
│   ├── refinador_hu.agent.md              ← Analista de historias
│   └── artesano_de_commits.agent.md       ← Narrador de cambios
│
├── herramientas/                          ← Herramientas ejecutables
│   ├── tomar_contexto.tool.md             ← Análisis del proyecto
│   ├── refinar_hu.tool.md                 ← Refinamiento de HUs
│   ├── validar_hu.tool.md                 ← Validación arquitectónica
│   ├── planificar_hu.tool.md              ← Planificación de implementación
│   ├── ejecutar_plan.tool.md              ← Ejecución de planes
│   ├── crear_pruebas.tool.md              ← Generación de tests
│   ├── analizar_code_smells.tool.md       ← Detección de problemas
│   ├── diagnosticar_devops.tool.md        ← Análisis DevOps
│   └── generar_commit.tool.md             ← Mensajes de commit
│
├── config/                                ← Configuración del sistema
│   ├── CONFIG_SYSTEM.yaml                 ← Variables del sistema
│   └── CONFIG_USER.template.yaml          ← Plantilla para usuario
│
├── guias/                                 ← Documentación y guías
│   ├── guia_comandos.md                   ← Guía de comandos
│   ├── guia_roles_activos.md              ← Guía de roles
│   ├── guia_ciclo_vida_tareas.md          ← Ciclo de vida de tareas
│   └── guia_creacion_roles.md             ← Crear roles personalizados
│
├── plantillas/                            ← Plantillas del sistema
│   ├── agente_plantilla.agent.md          ← Plantilla para roles
│   ├── herramienta_plantilla.tool.md      ← Plantilla para herramientas
│   ├── backlog_desarrollo_plantilla.md    ← Plantilla de backlog
│   ├── contexto_proyecto_plantilla.md     ← Plantilla de contexto
│   ├── session_state_plantilla.md         ← Estructura del estado
│   └── workspace_plantilla.md             ← Plantilla multi-proyecto
│
├── ejemplos/                              ← Ejemplos de uso
│   └── herramientas/                      ← Ejemplos de herramientas
│
├── legacy/                                ← Archivos de versiones anteriores
│
└── [EN EL PROYECTO DEL USUARIO]
    └── .SAC/                           ← Carpeta del sistema (auto-creada)
        ├── session/                       ← Estado compartido entre agentes
        │   └── session_state.json         ← Estado de la sesión
        └── artifacts/                     ← Artefactos generados
            ├── contexto_proyecto.md       ← Análisis del proyecto
            ├── backlog_desarrollo.md      ← Backlog de tareas
            └── HU/                        ← Historias de usuario
```

---

## 🤝 Contribuir

### Crear un Nuevo Rol

1. Copiar `plantillas/agente_plantilla.agent.md`
2. Guardar en `agentes/[nombre].agent.md`
3. Personalizar secciones YAML
4. Registrar en `ROLES.md`

Ver: **[Guía de Creación de Roles](guias/guia_creacion_roles.md)**

### Crear una Nueva Herramienta

1. Copiar `plantillas/herramienta_plantilla.tool.md`
2. Guardar en `herramientas/[nombre].tool.md`
3. Definir proceso y paso_final obligatorio
4. Registrar en `HERRAMIENTAS.md`

Ver: **[README_PLANTILLA.md](README_PLANTILLA.md)**

---

## 📞 Soporte

| Recurso | Ubicación |
|---------|-----------|
| Comandos | `guias/guia_comandos.md` |
| Roles | `guias/guia_roles_activos.md` |
| Problemas | Usar `*status` para diagnosticar |

---

## 📝 Notas de Versión

### v4.0 (Enero 2026)
- ✅ Migración a formato YAML estructurado
- ✅ Nuevas extensiones: `.agent.md` y `.tool.md`
- ✅ Sistema de prefijos: `+` (roles), `>` (herramientas), `*` (sistema)
- ✅ Modelo de uso: cada agente en chat independiente
- ✅ Estado compartido vía `.SAC/` en proyecto usuario
- ✅ Paso final obligatorio en herramientas
- ✅ Nuevos nombres: "Analista de Historias", "Narrador de Cambios"

### v3.0 (Enero 2026)
- Sintaxis con `@rol` y `> herramienta`

### v2.0 (Octubre 2025)
- Sistema de estado persistente

### v1.0 (Octubre 2025)
- Orquestador básico con 5 roles iniciales

---

**¡Listo para empezar!** 🚀

1. Elige el agente adecuado para tu tarea
2. Cárgalo en un nuevo chat
3. Usa `>tomar_contexto` para analizar tu proyecto
4. Ejecuta las herramientas del rol
