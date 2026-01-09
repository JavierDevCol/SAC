# 📝 CHANGELOG - Sistema COCHAS

> **Sistema:** COCHAS - Orquestación de Agentes IA  
> **Archivo:** Índice centralizado de versiones de todos los componentes

---

## 📊 Estado Actual de Componentes

| Componente | Versión Actual | Última Actualización |
|------------|----------------|----------------------|
| **Sistema SAC (COCHAS)** | 6.0 | 2026-01-09 |
| **Configuración Sistema** (`config/CONFIG_SYSTEM.yaml`) | 6.0 | 2026-01-09 |
| **Configuración Usuario** (`config/CONFIG_USER.template.yaml`) | 4.0 | 2026-01-05 |
| **Agentes** (`agentes/*.agent.md`) | 6.0 | 2026-01-09 |
| **Herramientas** (`herramientas/*.tool.md`) | 6.0 | 2026-01-09 |
| **Plantillas** (`plantillas/`) | 6.0 | 2026-01-09 |
| **Guía de Comandos** (`guias/guia_comandos.md`) | 3.0 | 2026-01-05 |
| **Guía de Roles** (`guias/guia_roles_activos.md`) | 3.0 | 2026-01-05 |
| **Guía Ciclo de Vida** (`guias/guia_ciclo_vida_tareas.md`) | 3.1 | 2026-01-05 |

---

## 🚀 Historial de Versiones

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
