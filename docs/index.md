# SAC — Sistema Agéntico COCHAS

> Sistema de agentes IA especializados para GitHub Copilot

SAC instala en tu proyecto un conjunto de **agentes Copilot** con roles especializados y **12 herramientas** ejecutables para el ciclo completo de desarrollo.

---

## ¿Qué hace SAC?

| Agente | Invocación | Especialidad |
|--------|-----------|--------------|
| Arquitecto | `@arquitecto` | Arquitectura, DDD, ADRs, validación de HUs |
| Desarrollador | `@desarrollador` | Implementación, TDD, refactoring |
| DevOps | `@devops` | CI/CD, infraestructura, DevSecOps |
| Analista de Requisitos | `@analista_historias` | Refinamiento de HUs |
| Cronista de Cambios | `@narrador_commit` | Conventional Commits |

---

## Inicio rápido

**1. Instalar SAC en tu proyecto:**

=== "Windows"
    ```powershell
    irm https://raw.githubusercontent.com/JavierDevCol/SAC/feature/instalacion/INSTALACION/bootstrap/install.ps1 | iex
    # Reiniciar terminal, luego:
    sac "C:/mi-proyecto"
    ```

=== "Linux/Mac"
    ```bash
    curl -fsSL https://raw.githubusercontent.com/JavierDevCol/SAC/feature/instalacion/INSTALACION/bootstrap/install.sh | bash
    # Reiniciar terminal, luego:
    sac /ruta/mi-proyecto
    ```

**2. Usar un agente en Copilot Chat:**

```
@arquitecto
>tomar_contexto

@analista_historias
>refinar_hu HU-001

@desarrollador
>ejecutar_plan HU-001

@narrador_commit
>generar_commit
```

---

## Documentación

- [Instalación detallada](INSTALACION.md)
- [Agentes disponibles](ROLES.md)
- [Herramientas disponibles](HERRAMIENTAS.md)
- [Guía de comandos](guias/guia_comandos.md)
- [Ciclo de vida de HUs](guias/guia_ciclo_vida_tareas.md)
