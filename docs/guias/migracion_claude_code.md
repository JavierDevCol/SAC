# Guía de Migración: SAC para Claude Code

> **Versión:** 7.25.0
> **Fecha:** 2026-07-04
> **Propósito:** Documentar cómo instalar y usar SAC en Claude Code

---

## Tabla de Contenidos

1. [Visión General](#1-visión-general)
2. [Diferencias con GitHub Copilot](#2-diferencias-con-github-copilot)
3. [Estructura de Directorios](#3-estructura-de-directorios)
4. [Crear Agentes](#4-crear-agentes)
5. [Crear Skills](#5-crear-skills)
6. [Configurar CLAUDE.md](#6-configurar-claudemd)
7. [Uso](#7-uso)
8. [Solución de Problemas](#8-solución-de-problemas)

---

## 1. Visión General

### ¿Qué es SAC?

SAC (Sistema Agéntico COCHAS) es un sistema de orquestación de agentes IA que incluye:

- **5 agentes especializados** con personalidades definidas
- **Herramientas** para tareas específicas (refinamiento, ADRs, bugs, etc.)
- **Plantillas** para documentos estructurados
- **Configuración** centralizada del sistema

### Compatible con

| IDE | Estado | Agentes | Skills |
|-----|--------|---------|--------|
| GitHub Copilot | ✅ Nativo | `.github/agents/*.agent.md` | No aplica |
| Claude Code | ✅ Adaptado | `.claude/agents/*.md` | `.claude/skills/*/SKILL.md` |
| OpenCode | ✅ Compatível | `.opencode/agents/*.md` | `.claude/skills/` + `.opencode/skills/` |

### Compatibilidad entre herramientas

| Componente | OpenCode | Claude Code | Copilot |
|------------|----------|-------------|---------|
| **Skills** | `.claude/skills/` ✅ | `.claude/skills/` ✅ | No aplica |
| **Agents** | `.opencode/agents/` (solo nativo) | `.claude/agents/` (solo nativo) | `.github/agents/` (solo nativo) |

> **Nota:** OpenCode SÍ lee skills de `.claude/skills/`, pero NO lee agentes de `.claude/agents/`.

---

## 2. Diferencias entre Herramientas

| Concepto | GitHub Copilot | Claude Code | OpenCode |
|----------|----------------|-------------|----------|
| **Agentes** | `.github/agents/*.agent.md` | `.claude/agents/*.md` | `.opencode/agents/*.md` |
| **Skills** | No aplica | `.claude/skills/*/SKILL.md` | `.opencode/skills/*/SKILL.md` + `.claude/skills/` |
| **Herramientas** | Prefijo `>` en chat | Skills con `/nombre` | Skills con `/nombre` |
| **Config** | `.SAC/config/CONFIG_SYSTEM.yaml` | `CLAUDE.md` | `opencode.json` |
| **Invocación** | `@nombre_agente` | `@nombre_agente` | `@nombre_agente` o `Tab` |
| **Modelo** | `Claude Opus 4.5 (copilot)` | `sonnet`, `opus`, `haiku` | `provider/model-id` |

### Formatos de Archivos

| Elemento | Copilot | Claude Code | OpenCode |
|----------|---------|-------------|----------|
| Agente | `.agent.md` | `.md` | `.md` |
| Rol | `.rol.md` (referencia) | `.rol.md` (referencia) | `.rol.md` (nativo) |
| Skill | No aplica | `SKILL.md` | `SKILL.md` |

---

## 3. Estructura de Directorios

### Estructura multi-herramienta recomendada

```
tu-proyecto/
├── .SAC/                              ← Fuente de verdad (compartida)
│   ├── agentes/
│   │   ├── _base.rol.md               ← Reglas base (compartido)
│   │   ├── arquitecto_onad.rol.md     ← Personalidad Arquitecto
│   │   ├── archdev_pro.rol.md         ← Personalidad Desarrollador
│   │   ├── arquitecto_devops.rol.md   ← Personalidad DevOps
│   │   └── refinador_hu.rol.md        ← Personalidad Analista
│   ├── herramientas/                  ← Herramientas YAML
│   ├── plantillas/                    ← Plantillas de documentos
│   ├── config/                        ← Configuración del sistema
│   └── reglas/                        ← Reglas por tecnología
│
├── .claude/                           ← Nativo Claude Code
│   ├── agents/                        ← Agentes (thin wrappers)
│   │   ├── arquitecto.md
│   │   ├── desarrollador.md
│   │   ├── devops.md
│   │   ├── analista_historias.md
│   │   └── cronista_de_cambios.md
│   └── skills/                        ← Skills (Claude + OpenCode leen)
│       ├── tomar-contexto/
│       │   └── SKILL.md
│       ├── generar-adr/
│       │   └── SKILL.md
│       ├── validar-hu/
│       │   └── SKILL.md
│       ├── refinar-hu/
│       │   └── SKILL.md
│       └── planificar-hu/
│           └── SKILL.md
│
├── .opencode/                         ← Nativo OpenCode
│   └── agents/                        ← Agentes OpenCode (NO lee .claude/)
│       ├── arquitecto.md
│       ├── desarrollador.md
│       ├── devops.md
│       ├── analista_historias.md
│       └── cronista_de_cambios.md
│
├── .github/agents/                    ← Copilot (thin wrappers)
│   ├── arquitecto.agent.md
│   ├── desarrollador.agent.md
│   ├── devops.agent.md
│   ├── analista_historias.agent.md
│   └── cronista_de_cambios.agent.md
│
├── CLAUDE.md                          ← Config Claude Code
└── opencode.json                      ← Config OpenCode
```

### Nota sobre compatibilidad

- **Skills en `.claude/skills/`**: OpenCode y Claude Code los leen ✅
- **Agents en `.claude/agents/`:** Solo Claude Code los lee ❌ OpenCode
- **Agents en `.opencode/agents/`:** Solo OpenCode los lee ❌ Claude Code
- **Agents en `.github/agents/`:** Solo Copilot los lee ❌ otros

---

## 4. Crear Agentes

### 4.1 Plantilla de agente (thin wrapper)

Cada agente en `.claude/agents/` es un wrapper delgado que referencia los `.rol.md`:

```markdown
---
name: nombre-agente
description: Descripción del agente para Claude Code
model: sonnet
tools: Read, Grep, Glob, Bash, Agent
color: blue
memory: project
---

# Agente Nombre

## Inicialización (Obligatorio)

Al iniciar sesión, ejecuta estos pasos en orden:

1. **Carga el archivo base:**
   ```
   Read .SAC/agentes/_base.rol.md
   ```
   Contiene reglas de configuración y comportamiento base.

2. **Carga tu personalidad:**
   ```
   Read .SAC/agentes/nombre_rol.rol.md
   ```
   Contiene tu personalidad, reglas y especialización.

3. **Carga contexto del proyecto:**
   - Si existe `CLAUDE.md`, léelo
   - Si existe `.SAC/config/CONFIG_SYSTEM.yaml`, cargo
   - Si existe `artifacts/backlog_desarrollo.md`, lee solo el índice rápido
   - Si existen `artifacts/reglas_arquitectonicas.md`, cargo

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
```

### 4.2 Agentes a crear

| Archivo | Rol referencia | Modelo | Color |
|---------|---------------|--------|-------|
| `arquitecto.md` | `arquitecto_onad.rol.md` | sonnet | blue |
| `desarrollador.md` | `archdev_pro.rol.md` | sonnet | green |
| `devops.md` | `arquitecto_devops.rol.md` | sonnet | orange |
| `analista_historias.md` | `refinador_hu.rol.md` | sonnet | purple |
| `cronista_de_cambios.md` | (inline) | haiku | cyan |

---

## 5. Crear Skills

### 5.1 Plantilla de skill

```markdown
---
name: nombre-skill
description: Qué hace el skill y cuándo usarlo
---

## Qué hago
- [Capacidad 1]
- [Capacidad 2]

## Cuándo usar
- [Caso de uso 1]
- [Caso de uso 2]

## Instrucciones
1. [Paso 1]
2. [Paso 2]

## Archivo de herramienta
Si el usuario necesita ejecutar la herramienta SAC completa, carga:
```
Read .SAC/herramientas/nombre_herramienta.tool.yaml
```
```

### 5.2 Skills a crear

| Skill | Herramienta SAC | Descripción |
|-------|-----------------|-------------|
| `tomar-contexto` | `tomar_contexto.tool.yaml` | Análisis de contexto del proyecto |
| `generar-adr` | `generar_adr.tool.yaml` | Generación de Architecture Decision Records |
| `validar-hu` | `validar_hu.tool.yaml` | Validación arquitectónica de HU |
| `refinar-hu` | `refinador_hu.tool.yaml` | Refinamiento de historias de usuario |
| `planificar-hu` | `planificar_hu.tool.yaml` | Planificación de implementación |

### 5.3 Ejemplo: Skill tomar-contexto

**Archivo:** `.claude/skills/tomar-contexto/SKILL.md`

```markdown
---
name: tomar-contexto
description: Analiza la estructura del proyecto y crea un workspace. Ejecuta >tomar_contexto del sistema SAC.
---

## Qué hago
- Analizo la estructura del proyecto (stack, frameworks, arquitectura)
- Creo un workspace.md con el contexto del proyecto
- Identifico tecnologías y patrones utilizados

## Cuándo usar
- Al iniciar un proyecto nuevo
- Cuando se necesita contexto arquitectónico
- Antes de tomar decisiones de diseño

## Instrucciones
1. Lee el archivo de herramienta: `.SAC/herramientas/tomar_contexto.tool.yaml`
2. Sigue las instrucciones del archivo
3. Genera el workspace en `artifacts/workspace.md`

## Salida esperada
- Archivo `artifacts/workspace.md` creado
- Resumen de tecnologías detectadas
- Recomendaciones de siguientes pasos
```

---

## 6. Configurar CLAUDE.md

### 6.1 Plantilla de CLAUDE.md

**Archivo:** `CLAUDE.md` (raíz del proyecto)

```markdown
# Configuración del Proyecto

## Información del Proyecto
- Nombre: [Nombre del proyecto]
- Stack: [Tecnologías principales]
- Arquitectura: [Tipo de arquitectura]

## Agentes SAC Disponibles
| Agente | Invocación | Uso |
|--------|------------|-----|
| Arquitecto | `@arquitecto` | Decisiones de arquitectura, ADRs |
| Desarrollador | `@desarrollador` | Implementación, tests |
| DevOps | `@devops` | CI/CD, infraestructura |
| Analista | `@analista_historias` | Refinamiento de HU |
| Cronista | `@cronista_de_cambios` | Commits |

## Skills Disponibles
| Skill | Invocación | Uso |
|-------|------------|-----|
| Tomar Contexto | `/tomar-contexto` | Analizar proyecto |
| Generar ADR | `/generar-adr` | Documentar decisiones |
| Validar HU | `/validar-hu` | Validar historias |

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
```

---

## 7. Uso

### 7.1 Invocar agentes

```
@arquitecto Analiza la arquitectura de este proyecto
@desarrollador Implementa el módulo de autenticación
@devops Configura el pipeline de CI/CD
@analista_historias Refina esta historia de usuario
```

### 7.2 Invocar skills

```
/tomar-contexto
/generar-adr
/validar-hu SAC-001
```

### 7.3 Usar herramientas SAC desde agentes

Dentro de un agente, puedes usar el prefijo `>`:

```
@arquitecto >tomar_contexto
@arquitecto >generar_adr
```

---

## 8. Solución de Problemas

### 8.1 El agente no carga los .rol.md

**Verificar:**
1. Que la ruta en el `.md` del agente sea correcta
2. Que los archivos `.rol.md` existan en `.SAC/agentes/`
3. Que el agente tenga permiso de lectura (`tools: Read`)

### 8.2 Los skills no aparecen

**Verificar:**
1. Que la estructura sea `.claude/skills/nombre-skill/SKILL.md`
2. Que el frontmatter tenga `name` y `description`
3. Que el nombre del directorio coincida con `name`

### 8.3 CLAUDE.md no se carga

**Verificar:**
1. Que el archivo esté en la raíz del proyecto
2. Que se llame exactamente `CLAUDE.md` (mayúsculas)
3. Reiniciar Claude Code después de crearlo

### 8.4 OpenCode no lee agentes de .claude/

**Verificar:**
1. Los agentes OpenCode deben estar en `.opencode/agents/*.md`
2. OpenCode NO lee `.claude/agents/` para agentes
3. Los skills SÍ se comparten entre `.claude/skills/` y `.opencode/skills/`

**Solución:** Crear agentes en `.opencode/agents/` que referencien los `.rol.md` de `.SAC/agentes/`

---

## 9. Configurar OpenCode

### 9.1 Estructura de agentes OpenCode

Los agentes OpenCode van en `.opencode/agents/` con formato `.md`:

**Archivo:** `.opencode/agents/arquitecto.md`

```markdown
---
description: Consultor técnico de élite y arquitecto estratégico
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
permission:
  edit: deny
  bash: deny
---

Eres un consultor técnico de élite y arquitecto estratégico.
Enfócate en:
- Análisis de trade-offs
- Decisiones arquitectónicas
- Architecture Decision Records (ADR)
- Validación de supuestos

NO implementes código directamente.
```

### 9.2 Skills compartidos

Los skills en `.claude/skills/` son leídos por OpenCode automáticamente. No duplicar.

### 9.3 Configuración en opencode.json

**Archivo:** `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "arquitecto": {
      "description": "Consultor técnico y arquitecto estratégico",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "temperature": 0.1,
      "permission": {
        "edit": "deny",
        "bash": "deny"
      }
    }
  }
}
```

---

## Referencia Rápida

### Comandos por Herramienta

| Herramienta | Comando | Descripción |
|-------------|---------|-------------|
| Claude Code | `/agents` | Gestionar agentes |
| Claude Code | `/skills` | Gestionar skills |
| Claude Code | `@nombre` | Invocar agente |
| Claude Code | `/nombre-skill` | Invocar skill |
| OpenCode | `Tab` | Cambiar entre agentes primarios |
| OpenCode | `@nombre` | Invocar subagente |
| OpenCode | `/nombre-skill` | Invocar skill |
| Copilot | `@nombre` | Invocar agente |

### Frontmatter de Agentes

| Campo | Claude Code | OpenCode | Copilot |
|-------|-------------|----------|---------|
| `name` | requerido | (nombre del archivo) | requerido |
| `description` | requerido | requerido | requerido |
| `model` | `sonnet`, `opus`, `haiku` | `provider/model-id` | `Claude Opus 4.5 (copilot)` |
| `tools` | `Read, Grep, Glob, Bash` | `write: true/false` | JSON array |
| `mode` | No aplica | `primary`, `subagent`, `all` | No aplica |
| `temperature` | No aplica | 0.0 - 1.0 | No aplica |

### Frontmatter de Skills

| Campo | Tipo | Default | Descripción |
|-------|------|---------|-------------|
| `name` | string | requerido | Nombre del skill |
| `description` | string | requerido | Descripción |
| `disable-model-invocation` | boolean | `false` | Solo invocación manual |
| `allowed-tools` | string | - | Herramientas auto-aprobadas |

### Ubicaciones por Herramienta

| Componente | Claude Code | OpenCode | Copilot |
|------------|-------------|----------|---------|
| Agentes | `.claude/agents/` | `.opencode/agents/` | `.github/agents/` |
| Skills | `.claude/skills/` | `.claude/skills/` + `.opencode/skills/` | No aplica |
| Config | `CLAUDE.md` | `opencode.json` | No aplica |

---

**Última actualización:** 2026-07-04
**Versión SAC:** 7.25.0
**Verificado con:** Documentación oficial OpenCode (2026-07-04)
