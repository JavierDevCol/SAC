# 📝 CHANGELOG - SAC

> **Sistema:** SAC - Sistema Agéntico COCHAS  
> **Archivo:** Índice centralizado de versiones de todos los componentes

---

## 📊 Estado Actual de Componentes

| Componente | Versión Actual | Última Actualización |
|------------|----------------|----------------------|
| **Sistema SAC** | 7.10.0 | 2026-04-24 |
| **Configuración Sistema** (`config/CONFIG_SYSTEM.yaml`) | 7.10.0 | 2026-04-24 |
| **Configuración Usuario** (`config/CONFIG_USER.template.yaml`) | 7.9.0 | 2026-04-24 |
| **Roles SAC** (`agentes/*.rol.md`) | 7.10.0 | 2026-04-24 |
| **Herramientas** (`herramientas/*.tool.md`) | 7.10.0 | 2026-04-24 |
| **Plantillas** (`plantillas/`) | 7.10.0 | 2026-04-24 |
| **Guía de Comandos** (`guias/guia_comandos.md`) | 7.3.0 | 2026-04-23 |
| **Guía de Roles** (`guias/guia_roles_activos.md`) | 3.0 | 2026-01-05 |
| **Guía Ciclo de Vida** (`guias/guia_ciclo_vida_tareas.md`) | 7.3.0 | 2026-04-23 |

---

## 🚀 Historial de Versiones

### [7.10.0] - 2026-04-24

#### 🎯 Optimización de Carga del Backlog (Ahorro de Tokens)

**Objetivo:** Reducir el consumo de tokens al cargar el backlog, pasando de lectura completa (~5000 tokens para 50+ HUs) a carga parcial (~200 tokens) con búsqueda dirigida bajo demanda.

#### ✅ Cambios en Plantillas

| Plantilla | Cambio |
|-----------|--------|
| `backlog_desarrollo_plantilla.md` | Nueva sección `## 📇 Índice Rápido` — tabla compacta (1 fila por HU: ID, Título, Estado, Prioridad, Tipo) |

#### ✅ Cambios en Roles

| Archivo | Cambio |
|---------|--------|
| `_base.rol.md` | Carga obligatoria cambiada: leer solo hasta `## 🎯 Historias de Usuario` (índice + metadatos) |
| `_base.rol.md` | Nueva instrucción de búsqueda dirigida: grep heading `### [ID-HU]` + read_file por rango |
| `_base.rol.md` | Instrucción explícita: NUNCA leer backlog completo para consultar una sola HU |

#### ✅ Cambios en Herramientas

| Herramienta | Cambio |
|-------------|--------|
| `sincronizar_backlog.tool.md` | Nuevo paso obligatorio `Regenerar Índice Rápido` — reconstruye tabla compacta tras sincronización |

---

### [7.9.0] - 2026-04-24

#### 🎯 Ruta de Artifacts Personalizable en Instalación

**Objetivo:** Permitir al usuario elegir la ruta relativa donde se generan los artifacts durante la instalación de SAC, en lugar de usar siempre `artifacts/`.

#### ✅ Cambios en Instalador

| Componente | Cambio |
|------------|--------|
| `instalar.py` | Nueva pregunta en configuración: ruta de artifacts (default: `artifacts/`) |
| `instalar.py` | Reordenamiento del flujo: configuración se pregunta ANTES de instalar |
| `instalar.py` | Nueva función `replace_artifacts_path()` para inyectar ruta custom en CONFIG_SYSTEM |
| `instalar.py` | Nueva función `collect_user_settings()` (recolección) separada de `write_user_config()` (escritura) |
| `instalar.py` | `upgrade_installation()` lee `artifacts_rel` del CONFIG_USER existente para preservar ruta custom |

#### ✅ Cambios en Configuración

| Archivo | Cambio |
|---------|--------|
| `CONFIG_USER.template.yaml` | Nueva sección `rutas_override.artifacts_folder` (opcional, comentada por defecto) |
| `CONFIG_SYSTEM.yaml` | Bump versión a 7.9.0 (sin cambios estructurales) |

---

### [7.8.0] - 2026-04-24

#### 🎯 Cambio Mayor: Sistema de Gestión de Bugs y Pendientes con Dispatcher Unificado

**Objetivo:** Implementar un sistema completo para registrar, clasificar y gestionar bugs y pendientes dentro del SAC, con soporte a lo largo de todo el ciclo de vida de HUs.

#### ✅ Nuevas Herramientas

| Herramienta | Descripción |
|-------------|-------------|
| **`>registrar_bug`** | Registro estructurado de bugs con triage: vincular a HU, agregar ajuste, o crear HU tipo Bug |
| **`>registrar_pendiente`** v2 | Registro dual (rápido en tabla / detallado con archivo individual), 6 categorías |
| **`>registrar_hallazgo`** | Dispatcher unificado que clasifica automáticamente y redirige a bug o pendiente |

#### ✅ Nuevas Plantillas

| Plantilla | Descripción |
|-----------|-------------|
| `bug_plantilla.md` | Formato post-mortem: Síntoma, Causa Raíz, Corrección, Lección Aprendida |
| `pendientes_plantilla.md` | Índice con 6 categorías y 4 estados de ciclo de vida |
| `pendiente_detalle_plantilla.md` | Archivo individual para pendientes con logs y evidencia |

#### ✅ Herramientas Adaptadas para HU tipo Bug

| Herramienta | Cambios |
|-------------|--------|
| `planificar_hu.tool.md` | Fases bugfix (Reproducción → Corrección → Testing Regresión), bypass para bugs críticos |
| `refinar_hu.tool.md` | Pre-población automática desde archivo BUG-NNN, auto-generación de CA |
| `validar_hu.tool.md` | Validación acelerada para Bug+Crítica |
| `sincronizar_backlog.tool.md` | Lectura de campos Tipo y Ref_Bug por HU |

#### ✅ Cambios en Configuración y Roles

| Archivo | Cambio |
|---------|--------|
| `CONFIG_SYSTEM.yaml` | Nuevas rutas: `bugs_folder`, `pendientes`, `pendientes_folder` |
| `backlog_desarrollo_plantilla.md` | Campos Tipo y Ref_Bug en todos los estados de HU |
| `_base.rol.md` | Carga bajo demanda de bugs y pendientes |
| `arquitecto_onad.rol.md` | +3 herramientas: `>registrar_bug`, `>registrar_pendiente`, `>registrar_hallazgo` |
| `archdev_pro.rol.md` | +2 herramientas: `>registrar_bug`, `>registrar_hallazgo` |

#### 📋 Flujo de Uso

```
Usuario reporta hallazgo
    └─ >registrar_hallazgo (dispatcher)
        ├─ [B] → >registrar_bug → Triage → HU tipo Bug
        └─ [P] → >registrar_pendiente → Tabla + archivo detalle
```

#### ⚙️ Retrocompatibilidad

Todos los cambios son retrocompatibles: si el campo `Tipo` no existe en una HU, se asume `Funcional`.

---

### [7.3.0] - 2026-04-23

#### 🎯 Cambio Mayor: Mejora de Sistema de Agentes, Roles y Guía de Subagentes

#### ✅ Mejoras

| Funcionalidad | Descripción |
|---------------|-------------|
| **Sistema de Agentes** | Mejoras en la configuración y comportamiento de agentes |
| **Roles** | Actualización de definiciones de roles del sistema |
| **Guía de Subagentes** | Mejoras en la guía de subagentes de VS Code |

---

### [7.2.0] - 2026-04-23

#### 🎯 Cambio Mayor: Subagentes, Extensiones y Limpieza Arquitectónica

#### ✅ Nuevas Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| **Protocolo de Delegación** | `_base.rol.md` incluye protocolo activo de escalamiento con `runSubagent` |
| **Soporte Subagentes VS Code** | Activadores con propiedad `agents:` para orchestrar subagentes natively |
| **Guía de Subagentes** | Nueva `guias/guia_subagents_vscode.md` con patrones y recomendaciones |

#### ✅ Cambios en Nombres y Rutas

| Elemento | Antes | Ahora |
|----------|-------|-------|
| Extensión roles SAC | `.agent.md` | `.rol.md` |
| Carpeta roles | `personas/` | `agentes/` |
| `artifacts/` | dentro de `.SAC/` | en raíz del proyecto |
| Activadores Copilot | `arquitecto_onad.agent.md` | `arquitecto.agent.md` |
| Invocaciones | `@arquitecto_onad` | `@arquitecto` |

#### ✅ Correcciones en Configuración

| Elemento | Cambio |
|----------|--------|
| `CONFIG_SYSTEM.yaml` | Eliminadas variables anidadas `{artifacts_folder}/...` |
| `instalar.py` | `artifacts_dir` apunta a raíz del proyecto; nueva función `migrate_artifacts_to_root()` |

#### ✅ Documentación P1 Corregida

| Archivo | Cambio |
|---------|--------|
| `estructura_directorio.md` | Reescrito completo para reflejar estructura real v7.2.0 |
| `INSTALACION.md` | Corregidos nombres de agentes, rutas de artifacts, invocaciones |
| `guias/guia_creacion_roles.md` | Actualizado a v3.0: rutas, extensiones, eliminados pasos legacy |

---

### [7.1.0] - 2026-02-16

#### 🎯 Cambio Mayor: Soporte Completo Multi-Proyecto

**Objetivo:** Unificar el manejo de workspaces mono y multi-proyecto, adaptar backlog y herramientas para soportar HUs compartidas entre proyectos, e implementar análisis automático de impacto.

#### ✅ Nuevas Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| **Workspace Unificado** | `workspace.md` como índice único para mono y multi-proyecto |
| **Campo Proyecto en HUs** | Cada HU indica a qué proyecto pertenece o si es `compartida` |
| **Análisis de Impacto `[AP]`** | Opción en `>refinar_hu` para que el agente analice qué proyectos afecta una HU |
| **Resumen por Proyecto** | Nueva sección en backlog con contadores de HUs por proyecto |
| **Proyectos afectados** | Sección en HUs compartidas listando proyectos involucrados |

#### ✅ Cambios en Plantillas

| Plantilla | Cambio |
|-----------|--------|
| `workspace_plantilla.md` | Simplificada a índice mínimo (tipo, tabla de proyectos, historial) |
| `contexto_proyecto_plantilla.md` | Nueva sección "6. Dependencias de Proyecto" |
| `backlog_desarrollo_plantilla.md` | Campo Workspace/Tipo, Resumen por Proyecto, campo Proyecto en HUs, columna Proyecto en tablas |

#### ✅ Cambios en Herramientas

| Herramienta | Cambios |
|-------------|---------|
| `refinar_hu.tool.md` | Parámetro `--proyecto`, detección de workspace, opción `[AP]` análisis de impacto, soporte respuestas combinadas (`1,2,3 AP`) |
| `validar_hu.tool.md` | Parámetro `--proyecto`, carga contextos de proyectos afectados, validación cross-proyecto |
| `planificar_hu.tool.md` | Parámetro `--proyecto`, carga contextos según campo Proyecto de HU |
| `ejecutar_plan.tool.md` | Parámetro `--proyecto`, CWD por proyecto, actualización Resumen por Proyecto |
| `tomar_contexto.tool.md` | Genera `workspace.md` en ambos modos (mono/multi) |

#### ✅ Cambios en Agentes

| Agente | Cambio |
|--------|--------|
| `_base.agent.md` | Carga unificada desde `{{archivos.workspace}}`, contextos on-demand |

#### ✅ Cambios en Configuración

| Archivo | Cambio |
|---------|--------|
| `CONFIG_SYSTEM.yaml` | Unificado a `archivos.workspace` (eliminados `contexto_proyecto` y `workspace_index`) |

#### 📋 Flujo Multi-Proyecto

```
>refinar_hu "nueva funcionalidad"
   ↓
¿A qué proyecto(s) pertenece?
  [1] backend_users
  [2] backend_orders
  [AP] Analizar impacto
   ↓
Usuario: "1,2 AP" → Analiza impacto solo en proyectos 1 y 2
   ↓
📊 Análisis de Impacto:
  - backend_users: ✅ AFECTADO
  - backend_orders: ❌ NO afectado
   ↓
HU creada como Proyecto: backend_users (o compartida si múltiples)
```

---

### [7.0] - 2026-02-13

#### 🎯 Cambio Mayor: Sistema Mandatory Base, Limpieza de Reglas y Mejoras en Herramientas

**Objetivo:** Centralizar instrucciones mandatory comunes en `_base.tool.md` y `_base.agent.md`, eliminar reglas de stack que son conocimiento implícito del LLM, mejorar herramientas de validación y refinamiento, y unificar plantillas.

#### ⚠️ Breaking Changes

| Cambio | Impacto | Migración |
|--------|---------|----------|
| Bloque `mandatory` en herramientas reemplazado por `mandatory_base` + `mandatory_especifico` | Herramientas heredan instrucciones comunes de `_base.tool.md` | Actualizar herramientas personalizadas |
| Reglas de stack eliminadas (`java.rules.md`, `go.rules.md`, etc.) | Movidas a legacy / conocimiento implícito del LLM | No se requiere acción |
| `stack_proyecto_plantilla.md` eliminada | Unificada con `contexto_proyecto_plantilla.md` | Usar plantilla de contexto |
| `session_state_plantilla.md` movida a legacy | Ya deprecada en v6.0 | Sin impacto |

#### ✅ Nuevos Archivos

| Archivo | Propósito |
|---------|----------|
| `agentes/_base.agent.md` | Instrucciones base compartidas por todos los agentes |
| `herramientas/_base.tool.md` | Instrucciones mandatory compartidas por todas las herramientas |
| `plantillas/refinamiento_hu_plantilla.md` | Plantilla estándar para refinamientos de HU |

#### ✅ Cambios en Herramientas

**Todas las herramientas (`herramientas/*.tool.md`):**
- Bloque `mandatory` reemplazado por `mandatory_base` (referencia a `_base.tool.md`) + `mandatory_especifico`
- Eliminadas instrucciones repetidas de idioma y firma (ahora en `_base.tool.md`)

**`validar_hu.tool.md`:**
- Nuevo paso "Detección de Ambigüedades" — NUNCA asumir, preguntar al usuario
- Nuevo paso "Validación contra ADR" — Verificar coherencia con decisiones arquitectónicas
- Validación Arquitectónica mejorada con checklist ampliado
- Acciones desglosadas en formato lista para mayor claridad

**`refinar_hu.tool.md`:**
- Referencia a `{{plantillas.refinamiento_hu}}` para generación de archivo
- Nuevo campo "Iteración" en acciones de modo nuevo y ajuste
- Acciones de modo ajuste mejoradas con sección de ajustes aplicados

**`tomar_contexto.tool.md`:**
- Mandatory reestructurado con mandatory_base + mandatory_especifico

#### ✅ Cambios en Plantillas

**`backlog_desarrollo_plantilla.md`:**
- Nuevo campo `ADR_Ref` en todas las secciones de HU
- Rutas unificadas a `{{artifacts.*}}` en lugar de variables legacy
- Nueva sección "Deuda Técnica" para tracking de tech debt
- Estado `[X]` Completada renombrado a `[C]` Completada

**`contexto_proyecto_plantilla.md`:**
- Estructura mejorada con subsecciones de Dependencias Core y Herramientas de Desarrollo
- Sección de arquitectura generalizada (no solo "capas")
- Convenciones reorganizadas en Código y Proyecto

**`plan_implementacion_plantilla.md`:**
- Versión actualizada a 2.0
- Fases dinámicas según arquitectura del proyecto (Hexagonal, MVC, Capas, Script, Frontend)
- Comentarios instructivos para `>planificar_hu`
- Eliminados ejemplos hardcodeados Java/Spring

#### ✅ Archivos Eliminados (movidos a legacy o eliminados)

| Archivo | Razón |
|---------|-------|
| `reglas/arquitectura.rules.md` | Conocimiento implícito del LLM |
| `reglas/deteccion_stack.rules.md` | Conocimiento implícito del LLM |
| `reglas/java.rules.md` | Conocimiento implícito del LLM |
| `reglas/javascript.rules.md` | Conocimiento implícito del LLM |
| `reglas/python.rules.md` | Conocimiento implícito del LLM |
| `reglas/dotnet.rules.md` | Conocimiento implícito del LLM |
| `reglas/go.rules.md` | Conocimiento implícito del LLM |
| `reglas/patrones_diseno.rules.md` | Conocimiento implícito del LLM |
| `plantillas/session_state_plantilla.md` | Movida a legacy (deprecada desde v6.0) |
| `plantillas/stack_proyecto_plantilla.md` | Unificada con contexto_proyecto_plantilla.md |

#### ✅ Cambios en Configuración

**`config/CONFIG_SYSTEM.yaml`:**
- Versión actualizada a 7.0
- Eliminado: `archivos.stack_proyecto` (unificado en contexto)
- Agregado: `plantillas.refinamiento_hu`
- Reglas simplificadas: solo `mermaid.rules.md` permanece

---

### [6.0] - 2026-01-09

#### 🎯 Cambio Mayor: Agentes Technology-Agnostic y Deprecación de Session State

**Objetivo:** Hacer el sistema SAC independiente de tecnología específica y simplificar la gestión de estado usando el backlog como única fuente de verdad.

#### ⚠️ Breaking Changes

| Cambio | Impacto | Migración |
|--------|---------|----------|
| `session_state.json` **DEPRECADO** | Proyectos existentes deben migrar | El backlog es ahora la única fuente de verdad |
| Agentes ya no son Java/Spring específicos | Comportamiento genérico por defecto | Ejecutar `>tomar_contexto` para generar `stack_proyecto.md` |
| Nuevo artefacto `stack_proyecto.md` requerido | `>tomar_contexto` tiene nuevo paso obligatorio | Se genera automáticamente |

#### ✅ Nuevos Artefactos y Plantillas

| Archivo | Propósito |
|---------|-----------|
| `plantillas/stack_proyecto_plantilla.md` | Plantilla para información del stack tecnológico |
| `plantillas/plan_implementacion_plantilla.md` | Plantilla para planes de implementación de HUs |
| `.SAC/artifacts/stack_proyecto.md` | Auto-generado con stack detectado del proyecto |

#### ✅ Cambios en Agentes

**Todos los agentes (`agentes/*.agent.md`):**
- Eliminada inicialización de `session_state.json`
- Nueva referencia dinámica: `referencia_stack: "{{archivos.stack_proyecto}}"`
- Principios universales en lugar de prácticas Java-específicas
- `actualizacion_estado` ahora referencia archivos de artefactos

#### ✅ Cambios en Herramientas

**`tomar_contexto.tool.md`:**
- Nuevo `paso_6`: Generación automática de `stack_proyecto.md`
- Detección de lenguajes, frameworks, herramientas de testing, convenciones

**`validar_hu.tool.md`:**
- Nuevo `paso_6`: Persistir feedback de validación en archivo de refinamiento
- Cuando veredicto es AJUSTES, agrega sección `## 📝 Feedback de Validación`

**`refinar_hu.tool.md`:**
- Nuevo `paso_0`: Detectar feedback de validación previa
- **MODO AJUSTE**: Re-refinamiento enfocado en resolver observaciones
- Marca observaciones como resueltas `[x]` al completar

**`planificar_hu.tool.md`:**
- Referencia a `{{plantillas.plan_implementacion}}`

**`ejecutar_plan.tool.md`:**
- Nueva sección `actualizacion_plan_tiempo_real` con estados y reglas

**Todas las herramientas:**
- Eliminado `paso_final` que actualizaba `session_state.json`
- Secciones `siguiente` sincronizadas con nombres de agentes correctos
- Nuevo campo `accion_usuario` con instrucciones para flujo cross-chat

#### ✅ Cambios en Configuración

**`config/CONFIG_SYSTEM.yaml`:**
- Eliminado: `rutas.session_folder`
- Eliminado: `archivos.session_state`
- Eliminado: `plantillas.session_state`
- Agregado: `archivos.stack_proyecto`
- Agregado: `plantillas.stack_proyecto`
- Agregado: `plantillas.plan_implementacion`

#### ✅ Archivos Deprecados/Eliminados

| Archivo | Razón |
|---------|-------|
| `plantillas/session_state_plantilla.md` | Backlog es única fuente de verdad |
| `.SAC/session/session_state.json` | Ya no se genera ni utiliza |

#### ✅ Flujo de Feedback Validación ↔ Refinamiento

```
>refinar_hu → [R] Refinada → >validar_hu 
                                   ↓
                        ┌─────────────────────┐
                        │   ¿Veredicto?       │
                        └─────────────────────┘
                           ↓           ↓
                      APROBADA     AJUSTES
                           ↓           ↓
                    >planificar   Persiste feedback
                                  en refinamiento.md
                                          ↓
                                    >refinar_hu
                                    (MODO AJUSTE)
                                          ↓
                                    Resuelve [x]
                                          ↓
                                    >validar_hu
```

---

### [4.0] - 2026-01-05

#### 🎯 Cambio Mayor: Reestructuración Completa del Repositorio

**Objetivo:** Separar configuración del sistema (no editable) de configuración del usuario (editable), crear capa de definiciones compactas y organizar archivos legacy.

#### ✅ Nueva Estructura de Carpetas

```
ia_prompts/
├── config/                          # ⚠️ NUEVO - Configuración separada
│   ├── CONFIG_SYSTEM.yaml           # NO EDITABLE - Rutas del sistema
│   └── CONFIG_USER.template.yaml    # EDITABLE - Preferencias del usuario
├── definiciones/                    # ⚠️ NUEVO - Definiciones compactas
│   ├── personas/                    # 5 archivos YAML de roles
│   │   ├── archdev_pro.yaml
│   │   ├── arquitecto_onad.yaml
│   │   ├── refinador_hu.yaml
│   │   ├── artesano_de_commits.yaml
│   │   └── arquitecto_devops.yaml
│   └── herramientas/                # 15 archivos YAML de herramientas
│       ├── tomar_contexto.yaml
│       ├── refinar_hu.yaml
│       ├── crear_pruebas.yaml
│       └── ... (12 más)
├── guias/                           # ⚠️ NUEVO - Carpeta para guías
├── legacy/                          # ⚠️ NUEVO - Archivos deprecados
│   ├── CONFIG_INIT.yaml             # Configuración antigua
│   ├── cochas.agent.md              # Orquestador anterior
│   ├── personas_antiguas/           # Backup de personas
│   └── herramientas_antiguas/       # Backup de herramientas
├── personas/                        # Archivos completos de personalidad
├── herramientas/                    # Archivos completos de herramientas
├── plantillas/                      # Sin cambios
└── ejemplos/                        # Sin cambios
```

#### ✅ Nuevos Archivos de Configuración

| Archivo | Propósito | Editable |
|---------|-----------|----------|
| `config/CONFIG_SYSTEM.yaml` | Rutas internas del sistema COCHAS | ❌ NO |
| `config/CONFIG_USER.template.yaml` | Preferencias del usuario/proyecto | ✅ SÍ |

#### ✅ Nueva Capa de Definiciones

**Propósito:** Archivos YAML compactos que sirven como índice rápido de roles y herramientas.

**Personas (5 definiciones):**
- `archdev_pro.yaml` - Ingeniero Constructor Java/Spring Boot
- `arquitecto_onad.yaml` - Arquitecto Estratégico
- `refinador_hu.yaml` - Experto en Historias de Usuario
- `artesano_de_commits.yaml` - Experto en Conventional Commits
- `arquitecto_devops.yaml` - Mentor DevOps

**Herramientas (15 definiciones):**
- `tomar_contexto.yaml`, `refinar_hu.yaml`, `crear_pruebas.yaml`
- `generar_commit.yaml`, `diagnosticar_devops.yaml`, `define_arquitectura.yaml`
- `generar_adr.yaml`, `analizar_code_smells.yaml`, `solucionar_smells.yaml`
- `refactorizar.yaml`, `verifica_pruebas.yaml`, `ejecutar_plan.yaml`
- `validar_hu.yaml`, `planificar_hu.yaml`, `asignar_responsable.yaml`

#### ✅ Archivos Migrados a Legacy

| Archivo Original | Nueva Ubicación |
|------------------|-----------------|
| `CONFIG_INIT.yaml` | `legacy/CONFIG_INIT.yaml` |
| `cochas.agent.md` | `legacy/cochas.agent.md` |
| `personas/*.md` | `legacy/personas_antiguas/` (backup) |
| `herramientas/*.md` | `legacy/herramientas_antiguas/` (backup) |

#### ✅ Beneficios de la Reestructuración

1. **Separación clara** entre configuración del sistema y del usuario
2. **Definiciones compactas** para referencia rápida sin leer archivos extensos
3. **Preservación de legacy** para rollback si es necesario
4. **Estructura escalable** para agregar nuevos roles/herramientas

---

### [3.2] - 2026-01-05

#### ✅ Correcciones Críticas
- **README.md**: Corregida referencia `core-cochas.md` → `cochas.agent.md`
- **README.md**: Agregado diagrama visual del sistema
- **herramientas-activas.md**: Eliminada herramienta `asignar_responsable` (ORQUESTADOR no es un rol activable)
- **guia_roles_activos.md**: Actualizada a v3.0, sincronizada sintaxis `+ROL`
- **Sincronización**: Herramientas ahora coinciden entre `roles-activos.md` y `herramientas-activas.md`

#### ✅ Nuevas Características
- **CHANGELOG.md** centralizado (este archivo)
- **Documentación de manejo de errores** en `cochas.agent.md`:
  - Session_state.json corrupto → recreación automática desde plantilla
  - Rol no encontrado → sugerencia de roles disponibles
  - Herramienta sin rol activo → indicación de roles compatibles
  - CONFIG_INIT.yaml inválido → mensaje de error claro
- **Sección "Herramientas por Rol"** en herramientas-activas.md

#### ✅ Clarificaciones de Ambigüedades Resueltas
| Ambigüedad | Resolución | Documento |
|------------|------------|-----------|
| Estado [B] Bloqueada: ¿Quién puede marcar? | **Cualquier rol** puede marcar si detecta impedimento | `guia_ciclo_vida_tareas.md` |
| Reglas Arquitectónicas: ¿Borrador o final? | Se genera como **BORRADOR**, requiere confirmación del usuario | `tomar_contexto.md` |
| Session State corrupto | Se **recrea automáticamente** desde plantilla base | `cochas.agent.md` |
| Confirmación de reglas: ¿Y si no responde? | **Siempre esperar** respuesta del usuario (A/B/C/D) | `tomar_contexto.md` |

---

### [3.1] - 2026-01-05

#### ✅ Cambios en Orquestador
- Nuevo sistema de prefijos (`*`, `+`, `>`)
- Eliminada tabla de roles duplicada (ver `roles-activos.md`)

---

### [3.0] - 2026-01-05

#### 🎯 Cambio Mayor: Nuevo Sistema de Prefijos

| Antes (v2.x) | Ahora (v3.0) | Propósito |
|--------------|--------------|-----------|
| `/cochas list` | `*roles` | Listar roles |
| `/cochas switch ONAD` | `+ONAD` | Activar rol |
| `/cochas status` | `*status` | Ver estado |
| `-> herramienta` | `>herramienta` | Ejecutar herramienta |

#### ✅ Componentes Actualizados
- `cochas.agent.md` - Orquestador simplificado con 5 responsabilidades
- `guia_comandos.md` - Nueva documentación de prefijos
- `roles-activos.md` - Actualizada tabla de roles
- `herramientas-activas.md` - Nuevo formato de comandos

#### ✅ Nuevos Comandos del Orquestador
- `*roles` - Lista roles disponibles
- `*status` - Muestra estado de sesión
- `*HU` - Lista historias de usuario
- `*help` - Ayuda de comandos
- `*actualizar_config` - Recarga configuración

#### ✅ Validación de Estructura (Paso 3.5)
- Nuevo paso obligatorio en protocolo de inicio
- Detecta archivos mal ubicados en artifacts/
- Sugiere correcciones automáticas

---

### [2.1] - 2026-01-04

#### ✅ Mejoras en Roles
- `arquitecto_onad.md` - Integración con placeholders y session_state
- Paso 0 crítico con `{{session_state_location}}`
- Secciones formales de Restricciones y Métricas

#### ✅ Nuevas Herramientas
- `validar_hu` - Validación arquitectónica de HUs
- `planificar_hu` - Planificación de implementación
- `ejecutar_plan` - Ejecución de planes de desarrollo

---

### [2.0] - 2025-10-16

#### 🎯 Cambio Mayor: Sistema de Estado Persistente

- **session_state.json** - Memoria de sesión entre cambios de rol
- **Validación secuencial** - Tareas pasan por estados obligatorios
- **Backlog automatizado** - Tracking de HUs con estados

#### ✅ Nuevos Componentes
- `plantillas/estructura_session_state.md` - Schema del estado
- `plantillas/backlog_desarrollo_plantilla.md` - Plantilla de backlog
- `guia_ciclo_vida_tareas.md` - Documentación de estados

#### ✅ Ciclo de Vida de Tareas
```
[ ] Pendiente → [R] Refinada → [A] Aprobada → [P] Planificada → [E] En Ejecución → [X] Completada
                                                                          ↓
                                                                    [B] Bloqueada
```

---

### [1.0] - 2025-10-01

#### 🎯 Versión Inicial

- **Orquestador básico** con cambio de roles
- **5 roles iniciales**: ONAD, ARCHDEV, DEVOPS, REFINADOR, ARTESANO
- **Sistema de herramientas** modular
- **Herramienta `tomar_contexto`** para análisis de proyectos

---

## 📋 Guía de Versionado

### Convención de Versiones

| Tipo | Cuándo | Ejemplo |
|------|--------|---------|
| **Major (X.0)** | Cambios que rompen compatibilidad | Nuevo sistema de comandos |
| **Minor (X.Y)** | Nuevas funcionalidades compatibles | Nueva herramienta |
| **Patch (X.Y.Z)** | Correcciones de bugs | Fix de documentación |

### Al Actualizar un Componente

1. **Incrementar versión** en el header del archivo
2. **Actualizar fecha** de última actualización
3. **Agregar entrada** en este CHANGELOG
4. **Actualizar tabla** de Estado Actual de Componentes

---

## 🔗 Referencias

- **README Principal**: `README.md`
- **Orquestador**: `cochas.agent.md`
- **Configuración**: `CONFIG_INIT.yaml`
