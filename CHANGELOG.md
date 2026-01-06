# 📝 CHANGELOG - Sistema COCHAS

> **Sistema:** COCHAS - Orquestación de Agentes IA  
> **Archivo:** Índice centralizado de versiones de todos los componentes

---

## 📊 Estado Actual de Componentes

| Componente | Versión Actual | Última Actualización |
|------------|----------------|----------------------|
| **Sistema COCHAS** | 4.0 | 2026-01-05 |
| **Configuración Sistema** (`config/CONFIG_SYSTEM.yaml`) | 4.0 | 2026-01-05 |
| **Configuración Usuario** (`config/CONFIG_USER.template.yaml`) | 4.0 | 2026-01-05 |
| **Definiciones Personas** (`definiciones/personas/*.yaml`) | 2.1 | 2026-01-05 |
| **Definiciones Herramientas** (`definiciones/herramientas/*.yaml`) | 2.0-2.1 | 2026-01-05 |
| **Roles Activos** (`personas/roles-activos.md`) | 3.0 | 2026-01-05 |
| **Herramientas Activas** (`herramientas/herramientas-activas.md`) | 3.1 | 2026-01-05 |
| **Guía de Comandos** (`guia_comandos.md`) | 3.0 | 2026-01-05 |
| **Guía de Roles** (`guia_roles_activos.md`) | 3.0 | 2026-01-05 |
| **Guía Ciclo de Vida** (`guia_ciclo_vida_tareas.md`) | 3.1 | 2026-01-05 |
| **Session State Schema** (`plantillas/estructura_session_state.md`) | 3.0 | 2026-01-05 |
| **Tomar Contexto** (`herramientas/tomar_contexto.md`) | 2.1 | 2026-01-05 |

---

## 🚀 Historial de Versiones

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
