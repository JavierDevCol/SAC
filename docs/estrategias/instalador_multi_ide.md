# Estrategia: Instalador Multi-IDE para SAC

> **Versión:** 1.0
> **Fecha:** 2026-07-04
> **Propósito:** Documentar la estrategia para extender el instalador de SAC con soporte multi-IDE

---

## Tabla de Contenidos

1. [Objetivo](#1-objetivo)
2. [Estado Actual](#2-estado-actual)
3. [Alcance](#3-alcance)
4. [Selección de IDE](#4-selección-de-ide)
5. [Estructura por IDE](#5-estructura-por-ide)
6. [Funciones del Instalador](#6-funciones-del-instalador)
7. [Flujo de Instalación](#7-flujo-de-instalación)
8. [Templates por IDE](#8-templates-por-ide)
9. [Skills a Crear](#9-skills-a-crear)
10. [Archivos a Modificar/Crear](#10-archivos-a-modificarcrear)
11. [Ejemplos de Uso](#11-ejemplos-de-uso)
12. [Preguntas Pendientes](#12-preguntas-pendientes)

---

## 1. Objetivo

Extender el instalador de SAC (`instalar.py`) para soportar múltiples IDEs de desarrollo:

- **GitHub Copilot** (actual)
- **Claude Code** (nuevo)
- **OpenCode** (nuevo)

El usuario podrá seleccionar qué IDE(s) usar durante la instalación.

---

## 2. Estado Actual

### Instalador Actual

| Característica | Estado |
|----------------|--------|
| IDE soportado | Solo GitHub Copilot |
| Selección de IDE | No existe |
| Agentes | Solo `.github/agents/*.agent.md` |
| Skills | No aplica |
| Configuración | No genera `CLAUDE.md` ni `opencode.json` |

### Limitaciones

1. No se pueden crear agentes para Claude Code o OpenCode
2. No se generan skills para herramientas SAC
3. No se crea configuración específica por IDE

---

## 3. Alcance

### Qué se va a implementar

| Componente | Copilot | Claude Code | OpenCode |
|------------|---------|-------------|----------|
| Agentes | ✅ Ya existe | ✅ Nuevo | ✅ Nuevo |
| Skills | ❌ No aplica | ✅ Nuevo | ✅ Nuevo |
| Configuración | ❌ No aplica | ✅ `CLAUDE.md` | ✅ `opencode.json` |

### Qué NO se va a implementar

- Hooks de Claude Code (complejidad innecesaria por ahora)
- Workflows de Claude Code
- MCP servers
- Agent teams

---

## 4. Selección de IDE

### Interfaz de selección

```
🖥️ SELECCIONA EL IDE DONDE USARÁS SAC

   Los agentes y skills se crearán en el formato
   correspondiente al IDE seleccionado.

   - [C] GitHub Copilot
   - [L] Claude Code  
   - [O] OpenCode
   - [T] Todos los anteriores

   Selección [C/l/o/t]:
```

### Opciones

| Opción | Descripción | Resultado |
|--------|-------------|-----------|
| `C` | Solo Copilot | Solo crea `.github/agents/` |
| `L` | Solo Claude Code | Crea `.claude/agents/` + `.claude/skills/` + `CLAUDE.md` |
| `O` | Solo OpenCode | Crea `.opencode/agents/` + `opencode.json` |
| `T` | Todos | Crea estructura para los 3 IDEs |

### Implementación

```python
def select_ide():
    """
    Pregunta al usuario qué IDE(s) quiere instalar.
    Retorna lista de IDEs seleccionados.
    """
    print("\n🖥️  SELECCIONA EL IDE DONDE USARÁS SAC\n")
    print("   Los agentes y skills se crearán en el formato")
    print("   correspondiente al IDE seleccionado.\n")
    print("   - [C] GitHub Copilot")
    print("   - [L] Claude Code")
    print("   - [O] OpenCode")
    print("   - [T] Todos los anteriores\n")
    
    selection = input("   Selección [C]: ").strip().lower()
    
    if selection == "t":
        return ["copilot", "claude", "opencode"]
    elif selection == "l":
        return ["claude"]
    elif selection == "o":
        return ["opencode"]
    else:
        return ["copilot"]  # Default
```

---

## 5. Estructura por IDE

### GitHub Copilot

```
tu-proyecto/
└── .github/
    └── agents/
        ├── arquitecto.agent.md
        ├── desarrollador.agent.md
        ├── devops.agent.md
        ├── analista_historias.agent.md
        └── cronista_de_cambios.agent.md
```

### Claude Code

```
tu-proyecto/
├── .claude/
│   ├── agents/
│   │   ├── arquitecto.md
│   │   ├── desarrollador.md
│   │   ├── devops.md
│   │   ├── analista_historias.md
│   │   └── cronista_de_cambios.md
│   └── skills/
│       ├── tomar-contexto/
│       │   └── SKILL.md
│       ├── generar-adr/
│       │   └── SKILL.md
│       ├── validar-hu/
│       │   └── SKILL.md
│       └── ... (12 skills total)
└── CLAUDE.md
```

### OpenCode

```
tu-proyecto/
├── .opencode/
│   └── agents/
│       ├── arquitecto.md
│       ├── desarrollador.md
│       ├── devops.md
│       ├── analista_historias.md
│       └── cronista_de_cambios.md
└── opencode.json
```

### Multi-IDE (Todos)

```
tu-proyecto/
├── .SAC/                          ← Fuente de verdad
├── .github/agents/                ← Copilot
├── .claude/                       ← Claude Code
│   ├── agents/
│   └── skills/
├── .opencode/                     ← OpenCode
│   └── agents/
├── CLAUDE.md                      ← Config Claude Code
└── opencode.json                  ← Config OpenCode
```

---

## 6. Funciones del Instalador

### Funciones Nuevas

| Función | Propósito | Parámetros |
|---------|-----------|------------|
| `select_ide()` | Seleccionar IDE(s) | Ninguno |
| `install_copilot_agents()` | Crear `.github/agents/` | `dest, root_dir` |
| `install_claude()` | Instalar para Claude Code | `dest, root_dir, agentes` |
| `install_opencode()` | Instalar para OpenCode | `dest, root_dir, agentes` |
| `generate_claude_agent()` | Generar wrapper Claude | `agent_name, rol_file` |
| `generate_opencode_agent()` | Generar agente OpenCode | `agent_name, rol_file` |
| `generate_skill()` | Generar SKILL.md | `skill_name, tool_file` |
| `generate_claude_md()` | Generar CLAUDE.md | `dest, agentes, skills` |
| `generate_opencode_json()` | Generar opencode.json | `dest, agentes` |

### Funciones Existentes (sin cambios)

| Función | Estado |
|---------|--------|
| `install_sac()` | Modificar (agregar parámetro `selected_ides`) |
| `collect_user_settings()` | Modificar (agregar selección IDE) |
| `copy_folder()` | Sin cambios |
| `replace_project_root_placeholder()` | Sin cambios |

### Detalle de Funciones

#### `select_ide()`

```python
def select_ide():
    """
    Pregunta al usuario qué IDE(s) quiere instalar.
    Retorna lista de IDEs seleccionados.
    """
    print("\n🖥️  SELECCIONA EL IDE DONDE USARÁS SAC\n")
    print("   - [C] GitHub Copilot")
    print("   - [L] Claude Code")
    print("   - [O] OpenCode")
    print("   - [T] Todos los anteriores\n")
    
    selection = input("   Selección [C]: ").strip().lower()
    
    if selection == "t":
        return ["copilot", "claude", "opencode"]
    elif selection == "l":
        return ["claude"]
    elif selection == "o":
        return ["opencode"]
    else:
        return ["copilot"]
```

#### `install_claude()`

```python
def install_claude(dest, root_dir, agentes):
    """
    Instala agentes y skills para Claude Code.
    Crea .claude/agents/ y .claude/skills/
    """
    claude_dest = dest / ".claude"
    
    # Crear directorio de agentes
    agents_dest = claude_dest / "agents"
    agents_dest.mkdir(parents=True, exist_ok=True)
    
    # Generar agentes
    agent_mapping = {
        "arquitecto": "arquitecto_onad.rol.md",
        "desarrollador": "archdev_pro.rol.md",
        "devops": "arquitecto_devops.rol.md",
        "analista_historias": "refinador_hu.rol.md",
        "cronista_de_cambios": None  # inline
    }
    
    for agent_name, rol_file in agent_mapping.items():
        if rol_file:
            content = generate_claude_agent(agent_name, rol_file)
            agent_path = agents_dest / f"{agent_name}.md"
            agent_path.write_text(content, encoding="utf-8")
    
    # Crear directorio de skills
    skills_dest = claude_dest / "skills"
    skills_dest.mkdir(parents=True, exist_ok=True)
    
    # Generar skills
    for skill_name, tool_file in SKILLS_MAPPING.items():
        skill_dir = skills_dest / skill_name
        skill_dir.mkdir(exist_ok=True)
        content = generate_skill(skill_name, tool_file)
        skill_path = skill_dir / "SKILL.md"
        skill_path.write_text(content, encoding="utf-8")
    
    # Generar CLAUDE.md
    generate_claude_md(dest, agentes, SKILLS_MAPPING.keys())
    
    return True
```

#### `generate_claude_agent()`

```python
def generate_claude_agent(agent_name, rol_file):
    """
    Genera el contenido de un agente para Claude Code.
    """
    agent_descriptions = {
        "arquitecto": {
            "description": "Consultor técnico de élite y arquitecto estratégico especializado en arquitectura de software.",
            "color": "blue"
        },
        "desarrollador": {
            "description": "Ingeniero Constructor experto en implementación pragmática de arquitecturas de software.",
            "color": "green"
        },
        "devops": {
            "description": "Mentor experto en DevOps que eleva la madurez operativa mediante pipelines reproducibles.",
            "color": "orange"
        },
        "analista_historias": {
            "description": "Experto en transformar Historias de Usuario ambiguas en paquetes tácticos de ejecución.",
            "color": "purple"
        },
        "cronista_de_cambios": {
            "description": "Genera mensajes de commit Conventional Commits a partir de diffs.",
            "color": "cyan"
        }
    }
    
    info = agent_descriptions[agent_name]
    
    return f"""---
name: {agent_name}
description: {info['description']}
model: sonnet
tools: Read, Grep, Glob, Bash, Agent
color: {info['color']}
memory: project
---

# Agente {agent_name.title()}

## Inicialización (Obligatorio)

Al iniciar sesión, ejecuta estos pasos en orden:

1. **Carga el archivo base:**
   ```
   Read .SAC/agentes/_base.rol.md
   ```

2. **Carga tu personalidad:**
   ```
   Read .SAC/agentes/{rol_file}
   ```

3. **Carga contexto del proyecto:**
   - Si existe `CLAUDE.md`, léelo
   - Si existe `.SAC/config/CONFIG_SYSTEM.yaml`, cargo
   - Si existe `artifacts/backlog_desarrollo.md`, lee solo el índice rápido

4. **Saluda en personaje** y presenta las herramientas disponibles.

---

## Herramientas SAC

Cuando el usuario solicite una herramienta SAC (con prefijo `>`), carga el archivo correspondiente desde `.SAC/herramientas/`:

| Comando | Archivo a cargar |
|---------|------------------|
| `>tomar_contexto` | `.SAC/herramientas/tomar_contexto.tool.yaml` |
| `>generar_adr` | `.SAC/herramientas/generar_adr.tool.yaml` |
| `>validar_hu` | `.SAC/herramientas/validar_hu.tool.yaml` |

---

## Delegación

Cuando detectes que otra parte del trabajo requiere otro agente, informa al usuario:

> 🔄 Esta subtarea se beneficiaría del agente **[Nombre]** (`@[activador]`).

| Agente | Activador |
|--------|-----------|
| Desarrollador | `@desarrollador` |
| DevOps | `@devops` |
| Analista de Requisitos | `@analista_historias` |
| Cronista de Cambios | `@cronista_de_cambios` |
"""
```

#### `generate_skill()`

```python
def generate_skill(skill_name, tool_file):
    """
    Genera el contenido de un SKILL.md para una herramienta SAC.
    """
    skill_descriptions = {
        "tomar-contexto": {
            "description": "Analiza la estructura del proyecto y crea un workspace.",
            "what": "Analizo la estructura del proyecto (stack, frameworks, arquitectura)",
            "when": "Al iniciar un proyecto nuevo o cuando se necesita contexto arquitectónico"
        },
        "generar-adr": {
            "description": "Genera Architecture Decision Records para decisiones técnicas.",
            "what": "Genero ADRs estructurados para documentar decisiones arquitectónicas",
            "when": "Cuando se toma una decisión técnica significativa"
        },
        "validar-hu": {
            "description": "Valida historias de usuario contra criterios arquitectónicos.",
            "what": "Valido HUs contra principios SOLID, patrones y reglas del proyecto",
            "when": "Antes de implementar una HU o al revisar refinement"
        },
        "refinar-hu": {
            "description": "Refina historias de usuario con criterios de aceptación medibles.",
            "what": "Transformo HUs ambiguas en paquetes tácticos de ejecución",
            "when": "Cuando una HU necesita más detalle antes de ser implementada"
        },
        "planificar-hu": {
            "description": "Planifica la implementación de una historia de usuario.",
            "what": "Creo un plan detallado de implementación con tareas técnicas",
            "when": "Antes de implementar una HU compleja"
        },
        "ejecutar-plan": {
            "description": "Ejecuta un plan de implementación paso a paso.",
            "what": "Ejecuto las tareas definidas en un plan de implementación",
            "when": "Cuando se tiene un plan aprobado y se desea ejecutar"
        },
        "crear-pruebas": {
            "description": "Genera tests unitarios y de integración.",
            "what": "Genero tests basados en criterios de aceptación y código existente",
            "when": "Al implementar nueva funcionalidad o al mejorar cobertura"
        },
        "analizar-code-smells": {
            "description": "Detecta problemas de diseño y código.",
            "what": "Identifico code smells, deuda técnica y oportunidades de refactorización",
            "when": "Al revisar código o antes de un refactoring"
        },
        "sincronizar-backlog": {
            "description": "Sincroniza estados del backlog con artefactos reales.",
            "what": "Verifico y actualizo el estado de las HUs en el backlog",
            "when": "periódicamente o al cambiar estados de HUs"
        },
        "registrar-bug": {
            "description": "Registra y clasifica bugs detectados.",
            "what": "Creo bugs estructurados con información para reproducción",
            "when": "Al encontrar un defecto en el código"
        },
        "registrar-pendiente": {
            "description": "Registra hallazgos de pruebas funcionales.",
            "what": "Documento hallazgos que no son bugs pero requieren atención",
            "when": "Al encontrar mejoras o issues menores"
        },
        "init-reglas-arquitectonicas": {
            "description": "Configura estándares y reglas del proyecto.",
            "what": "Inicializo el archivo de reglas arquitectónicas del proyecto",
            "when": "Al inicio del proyecto o al cambiar estándares"
        }
    }
    
    info = skill_descriptions.get(skill_name, {
        "description": f"Herramienta SAC: {skill_name}",
        "what": f"Ejecuta la herramienta {skill_name}",
        "when": f"Cuando se necesita {skill_name.replace('-', ' ')}"
    })
    
    return f"""---
name: {skill_name}
description: {info['description']}
---

## Qué hago
- {info['what']}

## Cuándo usar
- {info['when']}

## Instrucciones
1. Lee el archivo de herramienta: `.SAC/herramientas/{tool_file}`
2. Sigue las instrucciones del archivo
3. Genera la salida esperada

## Archivo de herramienta
Si el usuario necesita ejecutar la herramienta SAC completa, carga:
```
Read .SAC/herramientas/{tool_file}
```
"""
```

#### `generate_claude_md()`

```python
def generate_claude_md(dest, agentes, skills):
    """
    Genera el archivo CLAUDE.md para Claude Code.
    """
    agentes_table = """
| Agente | Invocación | Uso |
|--------|------------|-----|
| Arquitecto | `@arquitecto` | Decisiones de arquitectura, ADRs |
| Desarrollador | `@desarrollador` | Implementación, tests |
| DevOps | `@devops` | CI/CD, infraestructura |
| Analista | `@analista_historias` | Refinamiento de HU |
| Cronista | `@cronista_de_cambios` | Commits |
"""
    
    skills_table = """
| Skill | Invocación | Uso |
|-------|------------|-----|
| Tomar Contexto | `/tomar-contexto` | Analizar proyecto |
| Generar ADR | `/generar-adr` | Documentar decisiones |
| Validar HU | `/validar-hu` | Validar historias |
| Refinar HU | `/refinar-hu` | Refinar historias |
| Planificar HU | `/planificar-hu` | Planificar implementación |
| Ejecutar Plan | `/ejecutar-plan` | Ejecutar planes |
| Crear Pruebas | `/crear-pruebas` | Generar tests |
| Analizar Code Smells | `/analizar-code-smells` | Detectar problemas |
| Sincronizar Backlog | `/sincronizar-backlog` | Sincronizar estados |
| Registrar Bug | `/registrar-bug` | Registrar bugs |
| Registrar Pendiente | `/registrar-pendiente` | Registrar hallazgos |
| Init Reglas | `/init-reglas-arquitectonicas` | Configurar reglas |
"""
    
    content = f"""# Configuración del Proyecto SAC

## Agentes SAC Disponibles
{agentes_table}

## Skills Disponibles
{skills_table}

## Convenciones
- Usar Conventional Commits para commits
- Seguir principios SOLID
- Escribir tests antes del código (TDD)

## Rutas del Sistema
- Agentes: `.SAC/agentes/`
- Herramientas: `.SAC/herramientas/`
- Plantillas: `.SAC/plantillas/`
- Config: `.SAC/config/`
- Artifacts: `artifacts/`
"""
    
    claude_md_path = dest / "CLAUDE.md"
    claude_md_path.write_text(content, encoding="utf-8")
```

#### `generate_opencode_json()`

```python
def generate_opencode_json(dest, agentes):
    """
    Genera el archivo opencode.json para OpenCode.
    """
    agents_config = {}
    
    agent_mapping = {
        "arquitecto": {
            "description": "Consultor técnico de élite y arquitecto estratégico",
            "temperature": 0.1
        },
        "desarrollador": {
            "description": "Ingeniero Constructor experto en implementación pragmática",
            "temperature": 0.3
        },
        "devops": {
            "description": "Mentor experto en DevOps y automatización",
            "temperature": 0.2
        },
        "analista_historias": {
            "description": "Experto en transformar HUs en paquetes tácticos",
            "temperature": 0.2
        },
        "cronista_de_cambios": {
            "description": "Genera mensajes de commit Conventional Commits",
            "temperature": 0.1
        }
    }
    
    for agent_name, config in agent_mapping.items():
        agents_config[agent_name] = {
            "description": config["description"],
            "mode": "subagent",
            "model": "anthropic/claude-sonnet-4-20250514",
            "temperature": config["temperature"],
            "permission": {
                "edit": "ask",
                "bash": "ask"
            }
        }
    
    opencode_config = {
        "$schema": "https://opencode.ai/config.json",
        "agent": agents_config
    }
    
    opencode_json_path = dest / "opencode.json"
    opencode_json_path.write_text(
        json.dumps(opencode_config, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
```

---

## 7. Flujo de Instalación

### Diagrama de Flujo

```
install_sac(dest_path, root_dir, artifacts_rel, selected_ides)
│
├── 1. Migraciones existentes
│   ├── migrate_cochas_to_sac()
│   └── migrate_artifacts_to_root()
│
├── 2. Crear .SAC/
│   └── Copiar carpetas del sistema
│
├── 3. SELECCIONAR IDE(s)
│   └── selected_ides = select_ide()
│
├── 4. Para CADA IDE seleccionado:
│   │
│   ├── [copilot] install_copilot_agents()
│   │   └── Copiar .github/agents/*.agent.md
│   │
│   ├── [claude] install_claude()
│   │   ├── .claude/agents/*.md
│   │   ├── .claude/skills/*/SKILL.md
│   │   └── CLAUDE.md
│   │
│   └── [opencode] install_opencode()
│       ├── .opencode/agents/*.md
│       └── opencode.json
│
├── 5. Crear artifacts/
│
└── 6. Registrar instalación
```

### Código del Flujo

```python
def install_sac(dest_path, root_dir, artifacts_rel="artifacts", selected_ides=None):
    """
    Ejecuta la instalación de SAC con soporte multi-IDE.
    """
    if selected_ides is None:
        selected_ides = ["copilot"]  # Default
    
    dest = Path(dest_path)
    
    print("\n📦 Iniciando instalación...\n")
    
    # 0. Migraciones existentes
    cochas_legacy = dest / ".cochas"
    if cochas_legacy.exists():
        migrate_cochas_to_sac(dest_path)
    migrate_artifacts_to_root(dest_path)

    # 1. Crear carpeta .SAC
    sac_dest = dest / ".SAC"
    sac_dest.mkdir(exist_ok=True)
    
    # 2. Copiar carpetas desde la raíz
    for folder in CARPETAS_COCHAS:
        copy_folder(root_dir, sac_dest, folder)

    # 3. Reemplazar placeholders
    config_system_path = sac_dest / "config" / "CONFIG_SYSTEM.yaml"
    replace_project_root_placeholder(config_system_path, dest)
    replace_artifacts_path(config_system_path, dest, artifacts_rel)
    
    # 4. Instalar para cada IDE seleccionado
    print("\n🖥️  Instalando para IDE(s) seleccionado(s):\n")
    
    if "copilot" in selected_ides:
        print_info("Instalando para GitHub Copilot...")
        install_copilot_agents(dest, root_dir)
    
    if "claude" in selected_ides:
        print_info("Instalando para Claude Code...")
        install_claude(dest, root_dir, selected_ides)
    
    if "opencode" in selected_ides:
        print_info("Instalando para OpenCode...")
        install_opencode(dest, root_dir, selected_ides)
    
    # 5. Crear carpetas de artefactos
    session_dir = sac_dest / "session"
    artifacts_dir = dest / artifacts_rel
    hu_dir = artifacts_dir / "HU"
    
    session_dir.mkdir(exist_ok=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    hu_dir.mkdir(exist_ok=True)
    
    # 6. Registrar instalación
    system_version = get_installed_version(dest) or "unknown"
    register_installation(dest, system_version)
    
    return True
```

---

## 8. Templates por IDE

### Directorio de Templates

```
INSTALACION/
├── templates/
│   ├── copilot/
│   │   └── agents/
│   │       ├── arquitecto.agent.md
│   │       ├── desarrollador.agent.md
│   │       ├── devops.agent.md
│   │       ├── analista_historias.agent.md
│   │       └── cronista_de_cambios.agent.md
│   ├── claude/
│   │   ├── CLAUDE.md
│   │   └── agents/
│   │       ├── arquitecto.md
│   │       ├── desarrollador.md
│   │       ├── devops.md
│   │       ├── analista_historias.md
│   │       └── cronista_de_cambios.md
│   └── opencode/
│       ├── opencode.json
│       └── agents/
│           ├── arquitecto.md
│           ├── desarrollador.md
│           ├── devops.md
│           ├── analista_historias.md
│           └── cronista_de_cambios.md
└── instalar.py
```

### Ventajas de usar Templates

1. **Mantenimiento centralizado**: Actualizar un template actualiza todas las instalaciones
2. **Consistencia**: Asegura formato uniforme
3. **Personalización**: Fácil de modificar sin cambiar código Python
4. **Documentación**: Los templates sirven como referencia

---

## 9. Skills a Crear

### Lista Completa de Skills

| # | Skill | Herramienta SAC | Descripción |
|---|-------|-----------------|-------------|
| 1 | `tomar-contexto` | `tomar_contexto.tool.yaml` | Análisis de contexto del proyecto |
| 2 | `generar-adr` | `generar_adr.tool.yaml` | Generación de ADRs |
| 3 | `validar-hu` | `validar_hu.tool.yaml` | Validación arquitectónica de HU |
| 4 | `refinar-hu` | `refinador_hu.tool.yaml` | Refinamiento de historias |
| 5 | `planificar-hu` | `planificar_hu.tool.yaml` | Planificación de implementación |
| 6 | `ejecutar-plan` | `ejecutar_plan.tool.yaml` | Ejecución de planes |
| 7 | `crear-pruebas` | `crear_pruebas.tool.yaml` | Generación de tests |
| 8 | `analizar-code-smells` | `analizar_code_smells.tool.yaml` | Detección de problemas |
| 9 | `sincronizar-backlog` | `sincronizar_backlog.tool.yaml` | Sincronizar backlog |
| 10 | `registrar-bug` | `registrar_bug.tool.yaml` | Registro de bugs |
| 11 | `registrar-pendiente` | `registrar_pendiente.tool.yaml` | Registro de hallazgos |
| 12 | `init-reglas-arquitectonicas` | `init_reglas_arquitectonicas.tool.yaml` | Configurar reglas |

### Notas

- Los skills se crean en `.claude/skills/`
- OpenCode lee `.claude/skills/` automáticamente (no duplicar)
- Cada skill tiene su propio directorio con `SKILL.md`

---

## 10. Archivos a Modificar/Crear

### Archivos Existentes (Modificar)

| Archivo | Cambios |
|---------|---------|
| `INSTALACION/instalar.py` | Agregar funciones multi-IDE |
| `INSTALACION/README.md` | Actualizar documentación |

### Archivos Nuevos (Crear)

| Archivo | Propósito |
|---------|-----------|
| `INSTALACION/templates/copilot/agents/*.agent.md` | Templates Copilot |
| `INSTALACION/templates/claude/CLAUDE.md` | Template Claude Code |
| `INSTALACION/templates/claude/agents/*.md` | Templates Claude Code |
| `INSTALACION/templates/opencode/opencode.json` | Template OpenCode |
| `INSTALACION/templates/opencode/agents/*.md` | Templates OpenCode |

### Estructura Final

```
INSTALACION/
├── .github/agents/            ← Agentes Copilot (existente)
├── bootstrap/                 ← Scripts de instalación (existente)
├── templates/                 ← Templates por IDE (NUEVO)
│   ├── copilot/
│   ├── claude/
│   └── opencode/
├── instalar.py                ← Instalador (modificar)
└── README.md                  ← Documentación (modificar)
```

---

## 11. Ejemplos de Uso

### Instalación Interactiva

```bash
python instalar.py

# Prompt: Ruta del proyecto
   Ruta del proyecto [/home/usuario/mi-proyecto]: 

# Prompt: Configuración
   ¿Deseas configurar SAC para tu proyecto ahora? (S/n): S

# Prompt: Selección IDE
   🖥️  SELECCIONA EL IDE DONDE USARÁS SAC

   - [C] GitHub Copilot
   - [L] Claude Code
   - [O] OpenCode
   - [T] Todos los anteriores

   Selección [C]: T

# Resultado: Se crean estructuras para los 3 IDEs
```

### Instalación con Argumentos

```bash
# Solo Claude Code
python instalar.py --ide claude "/home/usuario/mi-proyecto"

# Solo OpenCode
python instalar.py --ide opencode "/home/usuario/mi-proyecto"

# Todos
python instalar.py --ide all "/home/usuario/mi-proyecto"
```

### Resultado de Instalación

```
tu-proyecto/
├── .SAC/
│   ├── agentes/
│   ├── herramientas/
│   ├── plantillas/
│   └── config/
├── .github/agents/            ← Copilot
│   ├── arquitecto.agent.md
│   └── ...
├── .claude/                   ← Claude Code
│   ├── agents/
│   │   └── *.md
│   └── skills/
│       ├── tomar-contexto/
│       │   └── SKILL.md
│       └── ...
├── .opencode/                 ← OpenCode
│   └── agents/
│       └── *.md
├── artifacts/
├── CLAUDE.md
└── opencode.json
```

---

## 12. Preguntas Pendientes

1. **¿Soporte para `--ide` como argumento CLI?** ¿O solo interactivo?
2. **¿Actualizar instalaciones existentes?** Si ya tiene `.github/agents/`, ¿agregar Claude/OpenCode?
3. **¿Migración automática?** Si detecta `.github/agents/` sin `.claude/`, ¿ofrecer agregar?
4. **¿Configuración personalizada por IDE?** ¿Preguntar modelo, temperatura, etc.?

---

**Última actualización:** 2026-07-04
**Estado:** Documentación lista para implementación
