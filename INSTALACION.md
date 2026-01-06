# 📦 Guía de Instalación - Sistema COCHAS v4.0

> **Sistema de Orquestación de Agentes IA para GitHub Copilot**

---

## 🎯 ¿Qué es COCHAS?

COCHAS es un sistema de agentes de IA especializados que se integra con **GitHub Copilot** para proporcionar asistentes expertos en diferentes áreas del desarrollo de software.

---

## 📋 Requisitos Previos

- **Python 3.6+** (para el script de instalación)
- **VS Code** con la extensión **GitHub Copilot** instalada
- **GitHub Copilot Chat** habilitado

---

## 🚀 Instalación

### Opción 1: Script Automático (Recomendado)

```bash
cd INSTALACION
python instalar.py
```

El script te pedirá la ruta del proyecto donde instalar COCHAS.

También puedes pasar la ruta directamente:

```bash
python instalar.py "C:\mi\proyecto"
```

### Opción 2: Instalación Manual

1. **Copia las carpetas** desde la raíz de `ia_prompts/` a `[tu-proyecto]/.cochas/`:
   - `agentes/`
   - `herramientas/`
   - `plantillas/`
   - `ejemplos/`
   - `config/`

2. **Copia `.github/agents/`** desde `INSTALACION/` a `[tu-proyecto]/.github/agents/`

---

## 📁 Contenido de INSTALACION/

```
INSTALACION/
├── README.md              ← Instrucciones detalladas
├── instalar.py            ← Script de instalación automática
└── .github/
    └── agents/            ← Activadores para Copilot (5 archivos)
        ├── arquitecto.agent.md
        ├── desarrollador.agent.md
        ├── devops.agent.md
        ├── analista_historias.agent.md
        └── narrador_commit.agent.md
```

**Nota:** Las carpetas del sistema (`agentes/`, `herramientas/`, etc.) se copian directamente desde la raíz de `ia_prompts/`, evitando duplicación.

---

## 📁 Estructura Final en tu Proyecto

```
tu-proyecto/
├── .cochas/
│   ├── agentes/          ← 5 agentes especializados
│   ├── herramientas/     ← 9 herramientas ejecutables
│   ├── plantillas/       ← Plantillas para personalización
│   ├── ejemplos/         ← Ejemplos de uso
│   ├── config/           ← Configuración
│   ├── session/          ← Estado de sesión
│   └── artifacts/        ← Artefactos generados
│       └── HU/
├── .github/
│   └── agents/           ← Activadores Copilot
└── ... (tu código)
```

---

## 🎭 Agentes Disponibles

| Invocación en Copilot | Agente | Especialidad |
|-----------------------|--------|--------------|
| `@arquitecto` | Arquitecto Onad | Arquitectura, DDD, decisiones técnicas |
| `@desarrollador` | ArchDev Pro | Java/Spring Boot, TDD, refactoring |
| `@devops` | Arquitecto DevOps | CI/CD, infraestructura, DevSecOps |
| `@analista_historias` | Analista de Historias | Refinamiento de HUs |
| `@narrador_commit` | Narrador de Cambios | Conventional Commits |

---

## 🔧 Uso Básico

1. Abre **Copilot Chat** en VS Code (`Ctrl+Shift+I`)
2. Escribe `@` y selecciona un agente
3. El agente cargará su personalidad
4. Usa herramientas con `>`:

```
>tomar_contexto
>crear_pruebas
>generar_commit
```

---

## ⚠️ Notas Importantes

1. **Rutas fijas**: No renombres archivos en `.cochas/agentes/`
2. **Gitignore**: Agrega a `.gitignore`:
   ```
   .cochas/session/
   .cochas/artifacts/
   ```

---

## 📚 Más Información

| Recurso | Ubicación |
|---------|-----------|
| Instrucciones detalladas | `INSTALACION/README.md` |
| Documentación del sistema | `README.md` |
| Índice de roles | `ROLES.md` |
| Índice de herramientas | `HERRAMIENTAS.md` |

---

**¿Problemas?** Verifica que Python esté instalado y que las rutas sean correctas.