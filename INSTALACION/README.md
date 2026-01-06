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
python instalar.py "C:/mi/proyecto"
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

## 🌐 Instalación Sin Tener el Repositorio Local

El script puede **descargar automáticamente** los archivos desde GitHub si no tienes el repositorio `ia_prompts` en tu equipo.

### Requisitos

- **Python 3.6+**
- **Git** instalado y disponible en el PATH

### ¿Cómo funciona?

1. El script detecta si está dentro del proyecto `ia_prompts` completo
2. Si **SÍ** → Usa los archivos locales
3. Si **NO** → Clona automáticamente desde GitHub a una carpeta temporal:
   - **Windows:** `%TEMP%\cochas_repo\`
   - **Linux/Mac:** `/tmp/cochas_repo/`

### Descargar solo el script

Puedes descargar **solo el archivo `instalar.py`** y ejecutarlo en cualquier equipo:

```bash
# El script clonará el repositorio automáticamente
python instalar.py "C:/mi/proyecto"
```

---

## 🔄 Actualizar el Sistema

Para obtener la última versión de COCHAS desde GitHub:

```bash
python instalar.py --update
```

Esto actualiza el repositorio en caché (`git pull`). Luego puedes reinstalar en tu proyecto:

```bash
python instalar.py "C:/mi/proyecto"
```

---

## 📋 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `python instalar.py` | Modo interactivo (pide la ruta) |
| `python instalar.py "RUTA"` | Instala en la ruta especificada |
| `python instalar.py --update` | Actualiza el repositorio desde GitHub |
| `python instalar.py --help` | Muestra la ayuda |

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
2. **Git requerido**: Para descargar desde GitHub (si no tienes el repo local)
3. **Rutas fijas**: No renombres los archivos en `.cochas/agentes/`
4. **Gitignore**: Considera agregar a tu `.gitignore`:
   ```
   .cochas/session/
   .cochas/artifacts/
   ```

---

## 🐛 Solución de Problemas

### "Git no está instalado"

```bash
# Windows (Chocolatey)
choco install git

# Windows (winget)
winget install Git.Git

# Linux (Ubuntu/Debian)
sudo apt install git

# Mac
brew install git
```

### "Python no encontrado"

```bash
# Windows (Chocolatey)
choco install python

# Windows (winget)
winget install Python.Python.3.11
```

### "La ruta no existe"

Asegúrate de que la carpeta destino exista antes de ejecutar el instalador.

---

## 📚 Más Información

- Documentación completa: `ia_prompts/README.md`
- Crear nuevos agentes: `.cochas/plantillas/agente_plantilla.agent.md`
- Crear nuevas herramientas: `.cochas/plantillas/herramienta_plantilla.tool.md`
- Repositorio: https://github.com/JavierDevCol/SAC

---

**¡Listo!** Ejecuta `python instalar.py` para comenzar. 🚀