# Estructura del Directorio `ia_prompts`

> **Versión:** 7.3.0  
> **Última actualización:** 23 de abril de 2026

## Árbol de Directorios

```
ia_prompts/
├── 📄 CHANGELOG.md                    # Historial de cambios del sistema
├── 📄 LICENSE
├── 📄 README.md                       # Vestíbulo: qué es, instalación rápida, links
│
├── 📁 docs/                           # Documentación de autor/usuario (NO se instala)
│   ├── estructura_directorio.md       # Este archivo
│   ├── HERRAMIENTAS.md                # Índice de herramientas disponibles
│   ├── INSTALACION.md                 # Guía rápida de instalación
│   ├── ROLES.md                       # Índice de roles/agentes disponibles
│   ├── README_PLANTILLA.md            # Plantilla para README de proyectos
│   ├── 📁 guias/                      # Guías para usuarios
│   │   ├── guia_ciclo_vida_tareas.md  # Ciclo de vida de tareas/HU
│   │   ├── guia_comandos.md           # Referencia de comandos
│   │   ├── guia_creacion_agentes_vscode.md
│   │   ├── guia_creacion_roles.md     # Cómo crear nuevos roles SAC
│   │   ├── guia_roles_activos.md      # Roles disponibles
│   │   └── guia_subagents_vscode.md   # Subagentes en VS Code Copilot
│   └── 📁 ejemplos/                   # Ejemplos de uso de herramientas
│       ├── README.md
│       └── 📁 herramientas/
│           ├── analizar_code_smells_ejemplo.md
│           ├── crear_pruebas_ejemplo.md
│           ├── diagnosticar_devops_ejemplo.md
│           ├── ecommerce_mvp_completo.md
│           ├── generar_commit_ejemplo.md
│           ├── refinar_hu_ejemplo.md
│           ├── solucionar_smells_ejemplo.md
│           ├── tomar_contexto_ejemplo.md
│           ├── verifica_pruebas_ejemplo.md
│           └── 📁 adr/
│
├── 📁 agentes/                        # Roles SAC — instrucciones de personalidad para IA
│   ├── _base.rol.md                   # Comportamiento base compartido (MANDATORY)
│   ├── archdev_pro.rol.md             # Rol: Desarrollador
│   ├── arquitecto_devops.rol.md       # Rol: DevOps
│   ├── arquitecto_onad.rol.md         # Rol: Arquitecto
│   ├── cronista_de_cambios.rol.md     # Rol: Cronista de Cambios
│   └── refinador_hu.rol.md            # Rol: Analista de Requisitos
│
├── 📁 config/                         # Configuración del sistema
│   ├── CONFIG_SYSTEM.yaml             # Rutas y estructura del sistema (NO modificar)
│   └── CONFIG_USER.template.yaml      # Plantilla de configuración de usuario
│
├── 📁 herramientas/                   # Instrucciones de herramientas para IA
│   ├── analizar_code_smells.tool.yaml   # >analizar_code_smells
│   ├── analizar_stack.tool.yaml         # >analizar_stack
│   ├── crear_pruebas.tool.yaml          # >crear_pruebas
│   ├── diagnosticar_devops.tool.yaml    # >diagnosticar_devops
│   ├── ejecutar_plan.tool.yaml          # >ejecutar_plan
│   ├── generar_adr.tool.yaml            # >generar_adr
│   ├── generar_commit.tool.yaml         # >generar_commit
│   ├── init_reglas_arquitectonicas.tool.yaml # >init_reglas_arquitectonicas
│   ├── planificar_hu.tool.yaml          # >planificar_hu
│   ├── refinar_hu.tool.yaml             # >refinar_hu
│   ├── tomar_contexto.tool.yaml         # >tomar_contexto
│   └── validar_hu.tool.yaml             # >validar_hu
│
├── 📁 INSTALACION/                    # Instalador del sistema
│   ├── instalar.py                    # Script principal de instalación
│   ├── README.md                      # Instrucciones detalladas
│   ├── bootstrap/                     # Scripts de instalación global (sac)
│   │   ├── install.ps1
│   │   ├── install.sh
│   │   ├── sac.bat
│   │   └── sac.sh
│   └── .github/
│       └── agents/                    # Agentes VS Code Copilot (activadores)
│           ├── analista_historias.agent.md
│           ├── arquitecto.agent.md
│           ├── desarrollador.agent.md
│           ├── devops.agent.md
│           └── cronista_de_cambios.agent.md
│
├── 📁 legacy/                         # Archivos de versiones anteriores (referencia)
│   ├── cochas.agent.md
│   ├── CONFIG_INIT.yaml               # Configuración unificada antigua
│   ├── 📁 herramientas_antiguas/      # Herramientas formato .md antiguo
│   │   └── ...
│   └── 📁 personas_antiguas/          # Personas formato .md antiguo
│       └── ...
│
├── 📁 personas/                       # Instrucciones de roles para IA
│   ├── archdev_pro.agent.md
│   ├── arquitecto_devops.agent.md
│   ├── arquitecto_onad.agent.md
│   ├── cronista_de_cambios.agent.md
│   ├── refinador_hu.agent.md
│   └── roles-activos.md               # Índice de roles activos
│
└── 📁 plantillas/                     # Plantillas para generar artefactos
    ├── adr_madr.plantilla.md
    ├── adr_nygard.plantilla.md
    ├── adr_y_statement.plantilla.md
    ├── agente_plantilla.agent.md
    ├── backlog_desarrollo_plantilla.md
    ├── contexto_proyecto_plantilla.md
    ├── herramienta_plantilla.tool.yaml
    ├── plan_implementacion_plantilla.md
    ├── refinamiento_hu_plantilla.md
    ├── reglas_arquitectonicas_plantilla.md
    └── workspace_plantilla.md
```

---

## Descripción de Carpetas

| Carpeta | Propósito | ¿Se instala? |
|---------|-----------|:------------:|
| `docs/` | Documentación de autor y usuario (guías, índices, ejemplos) | ❌ |
| `agentes/` | Roles SAC — archivos `.rol.md` con personalidad e instrucciones para IA | ✅ |
| `config/` | Configuración del sistema SAC (`CONFIG_SYSTEM.yaml`, `CONFIG_USER`) | ✅ |
| `herramientas/` | Archivos `.tool.yaml` con instrucciones de herramientas para IA | ✅ |
| `plantillas/` | Plantillas para generar artefactos del proyecto | ✅ |
| `reglas/` | Reglas especializadas por tecnología (Mermaid, etc.) | ✅ |
| `INSTALACION/` | Script de instalación, bootstrap global y activadores VS Code | ❌ |

---

## Convenciones de Nomenclatura

| Tipo de Archivo | Extensión | Audiencia | Ejemplo |
|-----------------|-----------|-----------|---------|
| Rol SAC | `.rol.md` | IA | `arquitecto_onad.rol.md` |
| Agente VS Code | `.agent.md` | VS Code + IA | `arquitecto.agent.md` |
| Herramienta | `.tool.yaml` | IA | `refinar_hu.tool.yaml` |
| Configuración | `.yaml` | Sistema | `CONFIG_SYSTEM.yaml` |
| Documentación | `.md` | Humanos | `guia_comandos.md` |

---

## Agentes Disponibles

| Nombre en Copilot | Rol SAC | Archivo de rol |
|-------------------|---------|----------------|
| `@arquitecto` | Arquitecto (Onad) | `agentes/arquitecto_onad.rol.md` |
| `@desarrollador` | Desarrollador (ArchDev Pro) | `agentes/archdev_pro.rol.md` |
| `@devops` | DevOps | `agentes/arquitecto_devops.rol.md` |
| `@analista_historias` | Analista de Requisitos | `agentes/refinador_hu.rol.md` |
| `@cronista_de_cambios` | Cronista de Cambios | `agentes/cronista_de_cambios.rol.md` |

---

## Herramientas Disponibles

| Herramienta | Comando | Agente principal |
|-------------|---------|-----------------|
| Tomar Contexto | `>tomar_contexto` | Todos |
| Analizar Stack | `>analizar_stack` | Arquitecto, Desarrollador |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` | Arquitecto |
| Refinar HU | `>refinar_hu` | Analista de Requisitos |
| Validar HU | `>validar_hu` | Arquitecto |
| Planificar HU | `>planificar_hu` | Arquitecto |
| Ejecutar Plan | `>ejecutar_plan` | Desarrollador |
| Crear Pruebas | `>crear_pruebas` | Desarrollador |
| Analizar Code Smells | `>analizar_code_smells` | Desarrollador |
| Generar ADR | `>generar_adr` | Arquitecto, Desarrollador, DevOps |
| Diagnosticar DevOps | `>diagnosticar_devops` | DevOps |
| Generar Commit | `>generar_commit` | Cronista de Cambios |
