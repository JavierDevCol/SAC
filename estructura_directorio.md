# Estructura del Directorio `ia_prompts`

> **Versión:** 4.0  
> **Última actualización:** 6 de enero de 2026

## Árbol de Directorios

```
ia_prompts/
├── 📄 CHANGELOG.md                    # Historial de cambios del sistema
├── 📄 estructura_directorio.md        # Este archivo
├── 📄 PLAN_REESTRUCTURACION_V4.md     # Plan de reestructuración v4.0
├── 📄 README.md                       # Documentación principal
├── 📄 README_PLANTILLA.md             # Plantilla para README de proyectos
│
├── 📁 config/                         # Configuración del sistema
│   ├── CONFIG_SYSTEM.yaml             # Rutas y estructura del sistema (NO modificar)
│   └── CONFIG_USER.template.yaml      # Plantilla de configuración de usuario
│
├── 📁 definiciones/                   # Definiciones YAML (fuente de verdad)
│   ├── 📁 herramientas/               # Definiciones de herramientas
│   │   ├── analizar_code_smells.yaml
│   │   ├── asignar_responsable.yaml
│   │   ├── crear_pruebas.yaml
│   │   ├── define_arquitectura.yaml
│   │   ├── diagnosticar_devops.yaml
│   │   ├── ejecutar_plan.yaml
│   │   ├── generar_adr.yaml
│   │   ├── generar_commit.yaml
│   │   ├── planificar_hu.yaml
│   │   ├── refactorizar.yaml
│   │   ├── refinar_hu.yaml
│   │   ├── solucionar_smells.yaml
│   │   ├── tomar_contexto.yaml
│   │   ├── validar_hu.yaml
│   │   └── verifica_pruebas.yaml
│   │
│   └── 📁 personas/                   # Definiciones de roles/personas
│       ├── archdev_pro.yaml
│       ├── arquitecto_devops.yaml
│       ├── arquitecto_onad.yaml
│       ├── artesano_de_commits.yaml
│       └── refinador_hu.yaml
│
├── 📁 ejemplos/                       # Ejemplos de uso
│   ├── README.md
│   ├── 📁 herramientas/               # Ejemplos por herramienta
│   │   ├── analizar_code_smells_ejemplo.md
│   │   ├── crear_pruebas_ejemplo.md
│   │   ├── diagnosticar_devops_ejemplo.md
│   │   ├── ecommerce_mvp_completo.md
│   │   ├── generar_commit_ejemplo.md
│   │   ├── refinar_hu_ejemplo.md
│   │   ├── solucionar_smells_ejemplo.md
│   │   ├── tomar_contexto_ejemplo.md
│   │   ├── verifica_pruebas_ejemplo.md
│   │   └── 📁 adr/                    # Ejemplos de ADR
│   │       └── ...
│   └── ...
│
├── 📁 guias/                          # Guías de uso del sistema
│   ├── guia_ciclo_vida_tareas.md      # Ciclo de vida de tareas/HU
│   ├── guia_comandos.md               # Referencia de comandos
│   ├── guia_creacion_roles.md         # Cómo crear nuevos roles
│   └── guia_roles_activos.md          # Roles disponibles
│
├── 📁 herramientas/                   # Instrucciones de herramientas para IA
│   ├── analizar_code_smells.tool.md
│   ├── crear_pruebas.tool.md
│   ├── diagnosticar_devops.tool.md
│   ├── ejecutar_plan.tool.md
│   ├── generar_commit.tool.md
│   ├── herramientas-activas.md        # Índice de herramientas activas
│   ├── planificar_hu.tool.md
│   ├── refinar_hu.tool.md
│   ├── tomar_contexto.tool.md
│   └── validar_hu.tool.md
│
├── 📁 legacy/                         # Archivos de versiones anteriores
│   ├── cochas.agent.md                # Orquestador original (referencia)
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
│   ├── artesano_de_commits.agent.md
│   ├── refinador_hu.agent.md
│   └── roles-activos.md               # Índice de roles activos
│
└── 📁 plantillas/                     # Plantillas para generar artefactos
    ├── backlog_desarrollo_plantilla.md
    ├── contexto_proyecto_plantilla.md
    └── estructura_session_state.md
```

---

## Descripción de Carpetas

| Carpeta | Propósito |
|---------|-----------|
| `config/` | Archivos de configuración del sistema COCHAS |
| `definiciones/` | Fuente de verdad en formato YAML para roles y herramientas |
| `ejemplos/` | Ejemplos prácticos de uso de herramientas |
| `guias/` | Documentación para usuarios humanos |
| `herramientas/` | Archivos `.tool.md` con instrucciones para IA |
| `legacy/` | Archivos de versiones anteriores (referencia histórica) |
| `personas/` | Archivos `.agent.md` con instrucciones de roles para IA |
| `plantillas/` | Plantillas para generar artefactos del proyecto |

---

## Convenciones de Nomenclatura

| Tipo de Archivo | Extensión | Audiencia | Ejemplo |
|-----------------|-----------|-----------|---------|
| Rol/Agente | `.agent.md` | IA | `arquitecto_onad.agent.md` |
| Herramienta | `.tool.md` | IA | `refinar_hu.tool.md` |
| Definición | `.yaml` | Sistema | `arquitecto_onad.yaml` |
| Documentación | `.md` | Humanos | `guia_comandos.md` |

---

## Roles Disponibles

| Rol | Comando | Archivo |
|-----|---------|---------|
| Arquitecto Onad | `+ONAD` | `personas/arquitecto_onad.agent.md` |
| ArchDev Pro | `+ARCHDEV` | `personas/archdev_pro.agent.md` |
| Refinador HU | `+REFINADOR` | `personas/refinador_hu.agent.md` |
| Artesano de Commits | `+ARTESANO` | `personas/artesano_de_commits.agent.md` |
| Arquitecto DevOps | `+DEVOPS` | `personas/arquitecto_devops.agent.md` |

---

## Herramientas Disponibles

| Herramienta | Comando | Roles Autorizados |
|-------------|---------|-------------------|
| Tomar Contexto | `>tomar_contexto` | Todos |
| Refinar HU | `>refinar_hu` | REFINADOR |
| Validar HU | `>validar_hu` | ONAD |
| Planificar HU | `>planificar_hu` | ONAD |
| Ejecutar Plan | `>ejecutar_plan` | ARCHDEV |
| Crear Pruebas | `>crear_pruebas` | ARCHDEV |
| Generar Commit | `>generar_commit` | ARTESANO, ARCHDEV |
| Analizar Code Smells | `>analizar_code_smells` | ARCHDEV |
| Diagnosticar DevOps | `>diagnosticar_devops` | DEVOPS |
