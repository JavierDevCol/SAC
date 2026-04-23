# 📦 Instalación de SAC v5.0

> **SAC - Sistema Agéntico COCHAS**
> Sistema de Orquestación de Agentes IA para GitHub Copilot

---

## 🚀 Instalación Rápida

### Opción 1: Bootstrap (Primera Instalación) ⭐ Recomendado

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/JavierDevCol/SAC/main/INSTALACION/bootstrap/install.ps1 | iex
```

**Linux/Mac (Bash):**
```bash
curl -fsSL https://raw.githubusercontent.com/JavierDevCol/SAC/main/INSTALACION/bootstrap/install.sh | bash
```

Esto:
1. Clona el repositorio en caché del sistema
2. Instala el comando global `sac`
3. Agrega `sac` al PATH

Después de reiniciar la terminal, puedes usar:
```bash
sac --help                    # Ver ayuda
sac "C:/mi-proyecto"          # Instalar en un proyecto
sac --update                  # Actualizar SAC
sac --upgrade-all             # Actualizar todas las instalaciones
```

### Opción 2: Usando el Script Directamente

```bash
python instalar.py
```

El script te pedirá la ruta del proyecto donde instalar SAC.

También puedes pasar la ruta como argumento:

```bash
python instalar.py "C:/mi/proyecto"
python instalar.py "/home/usuario/mi-proyecto"
```

### Opción 3: Instalación Manual

1. **Copia las siguientes carpetas** desde la raíz de `ia_prompts/` a `[tu-proyecto]/.SAC/`:
   - `agentes/`
   - `herramientas/`
   - `plantillas/`
   - `ejemplos/`
   - `config/`
   - `reglas/`

2. **Copia la carpeta `.github/agents/`** de esta instalación a `[tu-proyecto]/.github/agents/`

---

## 🌐 Instalación Sin Tener el Repositorio Local

El script puede **descargar automáticamente** los archivos desde GitHub si no tienes el repositorio `ia_prompts` en tu equipo.

### Requisitos

- **Python 3.8+**
- **Git** instalado y disponible en el PATH

### ¿Cómo funciona?

1. El script detecta si está dentro del proyecto `ia_prompts` completo
2. Si **SÍ** → Usa los archivos locales
3. Si **NO** → Clona automáticamente desde GitHub a una ubicación permanente:
   - **Windows:** `%LOCALAPPDATA%\SAC\repo\`
   - **Linux/Mac:** `~/.local/share/SAC/repo/`

### Descargar solo el script

Puedes descargar **solo el archivo `instalar.py`** y ejecutarlo en cualquier equipo:

```bash
# El script clonará el repositorio automáticamente
python instalar.py "C:/mi/proyecto"
```

---

## 🔄 Actualizar el Sistema

Para obtener la última versión de SAC desde GitHub:

**Con comando global:**
```bash
sac --update
```

**O con el script directamente:**
```bash
python instalar.py --update
```

Esto actualiza el repositorio en caché (`git pull`). Luego puedes reinstalar en tu proyecto:

```bash
sac "C:/mi/proyecto"
```

---

## 🔄 Actualizar Todas las Instalaciones

Si tienes SAC instalado en múltiples proyectos:

```bash
sac --upgrade-all
```

Esto actualiza el repositorio y reinstala en todos los proyectos donde SAC ya está instalado.

---

## 📋 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `sac` | Modo interactivo (pide la ruta) |
| `sac "RUTA"` | Instala en la ruta especificada |
| `sac --update` | Actualiza el repositorio desde GitHub |
| `sac --upgrade-all` | Actualiza todas las instalaciones |
| `sac --help` | Muestra la ayuda |

> **Nota:** Si no tienes el comando `sac` instalado, puedes usar `python instalar.py` en su lugar.

---

## 📋 Contenido de esta Carpeta

```
INSTALACION/
├── README.md              ← Este archivo
├── instalar.py            ← Script de instalación automática
├── bootstrap/             ← Scripts de instalación global
│   ├── install.ps1        ← Bootstrap para Windows
│   ├── install.sh         ← Bootstrap para Linux/Mac
│   ├── sac.bat            ← Comando global Windows
│   └── sac.sh             ← Comando global Linux/Mac
└── .github/
    └── agents/            ← Activadores para GitHub Copilot
        ├── arquitecto_onad.agent.md
        ├── archdev_pro.agent.md
        ├── arquitecto_devops.agent.md
        ├── refinador_hu.agent.md
        └── artesano_de_commits.agent.md
```

---

## 📁 Estructura Final en tu Proyecto

Después de la instalación, tu proyecto tendrá:

```
tu-proyecto/
├── .SAC/                          ← Sistema SAC
│   ├── agentes/                      ← 5 agentes especializados
│   ├── herramientas/                 ← 12 herramientas ejecutables
│   ├── plantillas/                   ← Plantillas para personalización
│   ├── ejemplos/                     ← Ejemplos de uso
│   ├── config/                       ← Configuración del sistema
│   ├── reglas/                       ← Reglas por tecnología
│   ├── session/                      ← Estado de sesión (auto-creado)
│   └── artifacts/                    ← Artefactos generados
│       └── HU/                       ← Historias de usuario
├── .github/
│   └── agents/                       ← Activadores Copilot
│       ├── arquitecto_onad.agent.md
│       ├── archdev_pro.agent.md
│       ├── arquitecto_devops.agent.md
│       ├── refinador_hu.agent.md
│       └── artesano_de_commits.agent.md
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
| `@arquitecto_onad` | Arquitecto Onad | Decisiones de arquitectura, ADRs, validar HUs |
| `@archdev_pro` | ArchDev Pro | Implementar código, tests, refactoring |
| `@arquitecto_devops` | Arquitecto DevOps | CI/CD, infraestructura, pipelines |
| `@refinador_hu` | Refinador de HU | Refinar historias de usuario |
| `@artesano_de_commits` | Artesano de Commits | Crear mensajes de commit semánticos |

---

## 🔧 Herramientas Disponibles

Una vez activado un agente, puedes usar sus herramientas con el prefijo `>`:

| Herramienta | Comando | Agentes |
|-------------|---------|---------|
| Tomar Contexto | `>tomar_contexto` | Todos |
| Refinar HU | `>refinar_hu` | Refinador |
| Validar HU | `>validar_hu` | Arquitecto |
| Planificar HU | `>planificar_hu` | Arquitecto |
| Ejecutar Plan | `>ejecutar_plan` | ArchDev Pro |
| Crear Pruebas | `>crear_pruebas` | ArchDev Pro |
| Analizar Code Smells | `>analizar_code_smells` | ArchDev Pro |
| Analizar Stack | `>analizar_stack` | Todos |
| Generar ADR | `>generar_adr` | Arquitecto |
| Init Reglas Arquitectónicas | `>init_reglas_arquitectonicas` | Arquitecto |
| Diagnosticar DevOps | `>diagnosticar_devops` | DevOps |
| Generar Commit | `>generar_commit` | Artesano de Commits |

---

## ⚠️ Notas Importantes

1. **Python requerido**: El script necesita Python 3.8 o superior
2. **Git requerido**: Para descargar desde GitHub (si no tienes el repo local)
3. **Rutas fijas**: No renombres los archivos en `.SAC/agentes/`
4. **Migración automática**: Si tienes una instalación anterior con `.cochas/`, el instalador la migrará automáticamente a `.SAC/`
5. **Gitignore**: Considera agregar a tu `.gitignore`:
   ```
   .SAC/session/
   .SAC/artifacts/
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
- Crear nuevos agentes: `.SAC/plantillas/agente_plantilla.agent.md`
- Crear nuevas herramientas: `.SAC/plantillas/herramienta_plantilla.tool.md`
- Repositorio: https://github.com/JavierDevCol/SAC

---

**¡Listo!** Ejecuta `python instalar.py` para comenzar. 🚀