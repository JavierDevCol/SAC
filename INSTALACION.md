# 📦 Guía de Instalación - SAC v7.2.0

> **Sistema Agéntico COCHAS para GitHub Copilot**

---

## 🎯 ¿Qué es SAC?

SAC (Sistema Agéntico COCHAS) es un sistema de agentes de IA especializados que se integra con **GitHub Copilot** para proporcionar asistentes expertos en diferentes áreas del desarrollo de software.

---

## 📋 Requisitos Previos

- **Python 3.8+** (para el script de instalación)
- **VS Code** con la extensión **GitHub Copilot** instalada
- **GitHub Copilot Chat** habilitado
- **Git** (para descarga automática)

---

## 🚀 Instalación

### Opción 1: Script Automático (Recomendado)

```bash
cd INSTALACION
python instalar.py
```

El script te pedirá la ruta del proyecto donde instalar SAC.

También puedes pasar la ruta directamente:

```bash
python instalar.py "C:\mi\proyecto"
```

### Opción 2: Instalación Manual

1. **Copia las carpetas** desde la raíz de `ia_prompts/` a `[tu-proyecto]/.SAC/`:
   - `agentes/`
   - `herramientas/`
   - `plantillas/`
   - `ejemplos/`
   - `config/`
   - `reglas/`

2. **Crea la carpeta** `[tu-proyecto]/artifacts/` (artefactos generados)

3. **Copia `.github/agents/`** desde `INSTALACION/` a `[tu-proyecto]/.github/agents/`

---

## 📁 Contenido de INSTALACION/

```
INSTALACION/
├── README.md              ← Instrucciones detalladas
├── instalar.py            ← Script de instalación automática
├── bootstrap/             ← Scripts de instalación global
│   ├── install.ps1
│   ├── install.sh
│   ├── sac.bat
│   └── sac.sh
└── .github/
    └── agents/            ← Activadores para Copilot (5 archivos)
        ├── arquitecto.agent.md
        ├── desarrollador.agent.md
        ├── devops.agent.md
        ├── analista_historias.agent.md
        └── narrador_commit.agent.md
```
```

**Nota:** Las carpetas del sistema (`agentes/`, `herramientas/`, etc.) se copian directamente desde la raíz de `ia_prompts/`, evitando duplicación.

---

## 📁 Estructura Final en tu Proyecto

```
tu-proyecto/
├── .SAC/
│   ├── agentes/          ← 6 roles SAC (archivos .rol.md)
│   ├── herramientas/     ← 12 herramientas ejecutables
│   ├── plantillas/       ← Plantillas para personalización
│   ├── ejemplos/         ← Ejemplos de uso
│   ├── config/           ← Configuración
│   ├── reglas/           ← Reglas por tecnología
│   └── session/          ← Estado de sesión
├── artifacts/            ← Artefactos generados (HUs, ADRs, planes)
│   └── HU/
├── .github/
│   └── agents/           ← Activadores Copilot
└── ... (tu código)
```
```

---

## 🎭 Agentes Disponibles

| Invocación en Copilot | Agente | Especialidad |
|-----------------------|--------|--------------|
| `@arquitecto` | Arquitecto (Onad) | Arquitectura, DDD, decisiones técnicas, ADRs |
| `@desarrollador` | Desarrollador (ArchDev Pro) | Implementación, TDD, refactoring |
| `@devops` | DevOps | CI/CD, infraestructura, DevSecOps |
| `@analista_historias` | Analista de Requisitos | Refinamiento de HUs |
| `@narrador_commit` | Cronista de Cambios | Conventional Commits |

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

1. **Rutas fijas**: No renombres archivos en `.SAC/agentes/`
2. **Gitignore**: Agrega a `.gitignore`:
   ```
   .SAC/session/
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