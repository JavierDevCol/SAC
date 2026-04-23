# SAC — Sistema Agéntico COCHAS

> Sistema de agentes IA especializados para GitHub Copilot  
> **Versión:** 7.3.0

SAC instala en tu proyecto un conjunto de **agentes Copilot** con roles especializados (Arquitecto, Desarrollador, DevOps, Analista de Requisitos, Cronista de Cambios) y **12 herramientas** ejecutables para el ciclo completo de desarrollo.

---

## Instalación rápida

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/JavierDevCol/SAC/main/INSTALACION/bootstrap/install.ps1 | iex
```

**Linux/Mac:**
```bash
curl -fsSL https://raw.githubusercontent.com/JavierDevCol/SAC/main/INSTALACION/bootstrap/install.sh | bash
```

Después de reiniciar la terminal:
```bash
sac "C:/mi-proyecto"
```

Guía completa: [INSTALACION/README.md](INSTALACION/README.md)

---

## Uso

Invoca un agente desde Copilot Chat y ejecuta herramientas:

```
@arquitecto
>tomar_contexto

@analista_historias
>refinar_hu HU-001

@arquitecto
>validar_hu HU-001
>planificar_hu HU-001

@desarrollador
>ejecutar_plan HU-001

@narrador_commit
>generar_commit
```

---

## Documentación

| Recurso | Descripción |
|---------|-------------|
| [docs/INSTALACION.md](docs/INSTALACION.md) | Guía de instalación detallada |
| [docs/ROLES.md](docs/ROLES.md) | Agentes disponibles |
| [docs/HERRAMIENTAS.md](docs/HERRAMIENTAS.md) | Herramientas disponibles |
| [docs/guias/guia_comandos.md](docs/guias/guia_comandos.md) | Referencia de comandos |
| [docs/guias/guia_ciclo_vida_tareas.md](docs/guias/guia_ciclo_vida_tareas.md) | Ciclo de vida de HUs |
| [docs/guias/guia_creacion_roles.md](docs/guias/guia_creacion_roles.md) | Crear roles personalizados |
| [docs/guias/guia_subagents_vscode.md](docs/guias/guia_subagents_vscode.md) | Subagentes en VS Code Copilot |
| [CHANGELOG.md](CHANGELOG.md) | Historial de versiones |

---

## Estructura del proyecto instalado

```
tu-proyecto/
├── .SAC/
│   ├── agentes/        ← 6 roles SAC (*.rol.md)
│   ├── herramientas/   ← 12 herramientas (*.tool.md)
│   ├── plantillas/
│   ├── config/
│   └── reglas/
├── artifacts/          ← HUs, ADRs, planes generados
└── .github/
    └── agents/         ← Activadores para Copilot Chat
        ├── arquitecto.agent.md
        ├── desarrollador.agent.md
        ├── devops.agent.md
        ├── analista_historias.agent.md
        └── narrador_commit.agent.md
```

