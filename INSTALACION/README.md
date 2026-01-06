# 📦 Instalación de COCHAS v4.0

> **Sistema de Orquestación de Agentes IA para GitHub Copilot**

---

## 🚀 Instalación Rápida

### Opción 1: Usando el Script (Recomendado)

```bash
python instalar.py
```

El script te pedirá la ruta del proyecto donde instalar COCHAS.

También puedes pasar la ruta como argumento:

```bash
python instalar.py "C:\mi\proyecto"
python instalar.py "/home/usuario/mi-proyecto"
```

### Opción 2: Instalación Manual

1. **Copia las siguientes carpetas** desde la raíz de `ia_prompts/` a `[tu-proyecto]/.cochas/`:
   - `agentes/`
   - `herramientas/`
   - `plantillas/`
   - `ejemplos/`
   - `config/`

2. **Copia la carpeta `.github/agents/`** de esta instalación a `[tu-proyecto]/.github/agents/`

---

## 📋 Contenido de esta Carpeta

```
INSTALACION/
├── README.md              ← Este archivo
├── instalar.py            ← Script de instalación automática
└── .github/
    └── agents/            ← Activadores para GitHub Copilot
        ├── arquitecto.agent.md
        ├── desarrollador.agent.md
        ├── devops.agent.md
        ├── analista_historias.agent.md
        └── narrador_commit.agent.md
```

### `.github/agents/` - Activadores para Copilot

| Archivo | Agente que Activa | Descripción |
|---------|-------------------|-------------|
| `arquitecto.agent.md` | Arquitecto Onad | Arquitectura estratégica y DDD |
| `desarrollador.agent.md` | ArchDev Pro | Implementación, TDD, refactoring |
| `devops.agent.md` | Arquitecto DevOps | CI/CD, infraestructura, DevSecOps |
| `analista_historias.agent.md` | Analista de Historias | Refinamiento de HUs |
| `narrador_commit.agent.md` | Narrador de Cambios | Conventional Commits |

---

## 📁 Estructura Final en tu Proyecto

Después de la instalación, tu proyecto tendrá:

```
tu-proyecto/
├── .cochas/                          ← Sistema COCHAS
│   ├── agentes/                      ← 5 agentes especializados
│   ├── herramientas/                 ← 9 herramientas ejecutables
│   ├── plantillas/                   ← Plantillas para personalización
│   ├── ejemplos/                     ← Ejemplos de uso
│   ├── config/                       ← Configuración del sistema
│   ├── session/                      ← Estado de sesión (auto-creado)
│   └── artifacts/                    ← Artefactos generados
│       └── HU/                       ← Historias de usuario
├── .github/
│   └── agents/                       ← Activadores Copilot
│       ├── arquitecto.agent.md
│       ├── desarrollador.agent.md
│       ├── devops.agent.md
│       ├── analista_historias.agent.md
│       └── narrador_commit.agent.md
└── ... (tu código)
```

---

## 🎯 Cómo Usar los Agentes

### En GitHub Copilot Chat (VS Code)

1. Abre **Copilot Chat** (`Ctrl+Shift+I` o `Cmd+Shift+I`)
2. Escribe `@` para ver los agentes disponibles
3. Selecciona el agente que necesitas
4. El agente se activará con su personalidad completa

### Agentes Disponibles

| Invocación | Agente | Cuándo Usar |
|------------|--------|-------------|
| `@arquitecto` | Arquitecto Onad | Decisiones de arquitectura, validar HUs |
| `@desarrollador` | ArchDev Pro | Implementar código, tests, refactoring |
| `@devops` | Arquitecto DevOps | CI/CD, infraestructura, pipelines |
| `@analista_historias` | Analista de Historias | Refinar historias de usuario |
| `@narrador_commit` | Narrador de Cambios | Crear mensajes de commit |

---

## 🔧 Herramientas Disponibles

Una vez activado un agente, puedes usar sus herramientas con el prefijo `>`:

| Herramienta | Comando | Agentes |
|-------------|---------|---------|
| Tomar Contexto | `>tomar_contexto` | Todos |
| Refinar HU | `>refinar_hu` | Analista |
| Validar HU | `>validar_hu` | Arquitecto |
| Planificar HU | `>planificar_hu` | Arquitecto |
| Ejecutar Plan | `>ejecutar_plan` | Desarrollador |
| Crear Pruebas | `>crear_pruebas` | Desarrollador |
| Analizar Code Smells | `>analizar_code_smells` | Desarrollador |
| Diagnosticar DevOps | `>diagnosticar_devops` | DevOps |
| Generar Commit | `>generar_commit` | Todos |

---

## ⚠️ Notas Importantes

1. **Python requerido**: El script necesita Python 3.6 o superior
2. **Rutas fijas**: No renombres los archivos en `.cochas/agentes/`
3. **Gitignore**: Considera agregar a tu `.gitignore`:
   ```
   .cochas/session/
   .cochas/artifacts/
   ```

---

## 📚 Más Información

- Documentación completa: `ia_prompts/README.md`
- Crear nuevos agentes: `.cochas/plantillas/agente_plantilla.agent.md`
- Crear nuevas herramientas: `.cochas/plantillas/herramienta_plantilla.tool.md`

---

**¡Listo!** Ejecuta `python instalar.py` para comenzar. 🚀