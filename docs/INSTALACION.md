# 📦 Guía de Instalación - SAC v7.14.0

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

### Opción 1: Bootstrap desde GitHub (Un solo comando) ⭐ Recomendado

No necesitas clonar nada. Ejecuta un solo comando y SAC se instala globalmente:

=== "Windows (PowerShell)"

    ```powershell
    irm https://github.com/JavierDevCol/SAC/releases/latest/download/install.ps1 | iex
    ```

=== "Linux / Mac (Bash)"

    ```bash
    curl -fsSL https://github.com/JavierDevCol/SAC/releases/latest/download/install.sh | bash
    ```

Esto realiza automáticamente:

1. Clona el repositorio en la caché del sistema
2. Instala el comando global `sac`
3. Agrega `sac` al PATH

Después de **reiniciar la terminal**, puedes usar:

```bash
sac --help                    # Ver ayuda
sac "C:/mi-proyecto"          # Instalar en un proyecto
sac --update                  # Actualizar SAC
sac --upgrade-all             # Actualizar todas las instalaciones
```

### Opción 2: Instalación Segura desde Release (Descargar → Revisar → Ejecutar)

!!! tip "Recomendado para entornos corporativos"
    Descarga el script, revisa su contenido y luego ejecútalo.

=== "Windows (PowerShell)"

    ```powershell
    # 1. Descargar desde el último release
    Invoke-WebRequest -Uri "https://github.com/JavierDevCol/SAC/releases/latest/download/install.ps1" -OutFile install.ps1

    # 2. Revisar el contenido antes de ejecutar
    Get-Content install.ps1

    # 3. Ejecutar
    .\install.ps1
    ```

=== "Linux / Mac (Bash)"

    ```bash
    # 1. Descargar desde el último release
    curl -fsSL -o install.sh https://github.com/JavierDevCol/SAC/releases/latest/download/install.sh

    # 2. Revisar el contenido antes de ejecutar
    cat install.sh

    # 3. Ejecutar
    chmod +x install.sh
    ./install.sh
    ```

!!! info "Instalación con versión fija (pinning)"
    Puedes apuntar a una versión específica en lugar de `latest`:

    ```
    https://github.com/JavierDevCol/SAC/releases/download/v7.14.0/install.ps1
    https://github.com/JavierDevCol/SAC/releases/download/v7.14.0/install.sh
    ```

### Opción 3: Script Automático (Si tienes el repositorio local)

```bash
cd INSTALACION
python instalar.py
```

El script te pedirá la ruta del proyecto donde instalar SAC.

También puedes pasar la ruta directamente:

```bash
python instalar.py "C:\mi\proyecto"
```

### Opción 4: Instalación Manual

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
        └── cronista_de_cambios.agent.md
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

---

## 🎭 Agentes Disponibles

| Invocación en Copilot | Agente | Especialidad |
|-----------------------|--------|--------------|
| `@arquitecto` | Arquitecto (Onad) | Arquitectura, DDD, decisiones técnicas, ADRs |
| `@desarrollador` | Desarrollador (ArchDev Pro) | Implementación, TDD, refactoring |
| `@devops` | DevOps | CI/CD, infraestructura, DevSecOps |
| `@analista_historias` | Analista de Requisitos | Refinamiento de HUs |
| `@cronista_de_cambios` | Cronista de Cambios | Conventional Commits |

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

### 🌐 Instalación desde GitHub (Sin repositorio local)

El script `instalar.py` puede **descargar automáticamente** los archivos desde GitHub si no tienes el repositorio clonado:

```bash
# Descarga solo el script y ejecútalo — clonará el repo automáticamente
python instalar.py "C:/mi/proyecto"
```

El script detecta si está dentro del proyecto `ia_prompts` completo:

- **SÍ** → Usa los archivos locales
- **NO** → Clona automáticamente desde GitHub a una ubicación permanente:

| Sistema | Ubicación del caché |
|---------|-------------------|
| Windows | `%LOCALAPPDATA%\SAC\repo\` |
| Linux/Mac | `~/.local/share/SAC/repo/` |

### 🔄 Actualizar SAC

Para obtener la última versión desde GitHub:

=== "Con comando global"

    ```bash
    sac --update
    ```

=== "Con script directo"

    ```bash
    python instalar.py --update
    ```

Luego reinstala en tu proyecto:

```bash
sac "C:/mi-proyecto"
```

### 🔄 Actualizar Todas las Instalaciones

Si tienes SAC instalado en múltiples proyectos:

```bash
sac --upgrade-all
```

Esto actualiza el repositorio en caché y reinstala en todos los proyectos registrados.

### 🏷️ Releases y Versionado

SAC utiliza **GitHub Releases** con tags versionados siguiendo [SemVer](https://semver.org/lang/es/):

| Concepto | Ejemplo | Descripción |
|----------|---------|-------------|
| **Latest** | `releases/latest/download/` | Siempre apunta a la última versión estable |
| **Tag fijo** | `releases/download/v7.14.0/` | Versión específica, inmutable |

!!! warning "¿Por qué usar releases en vez de `raw.githubusercontent.com/main`?"
    - Los **releases** apuntan a un **tag inmutable** — no cambian si alguien pushea a `main`
    - `raw.githubusercontent.com` tiene **caching agresivo** y puede servir versiones desactualizadas
    - Los releases permiten adjuntar **checksums y notas de versión**

### 🔒 Consideraciones de Seguridad

| Riesgo | Mitigación |
|--------|-----------|
| Script descargado no verificado | Usa la [Opción 2](#opcion-2-instalacion-segura-desde-release-descargar-revisar-ejecutar) para revisar antes de ejecutar |
| Versión inestable | Pinea a un tag específico (e.g., `v7.14.0`) en lugar de `latest` |
| Ejecución con privilegios elevados | Los scripts **NO** requieren permisos de administrador |
| `ExecutionPolicy` en PowerShell | Si está bloqueado, usa: `Set-ExecutionPolicy Bypass -Scope Process` |

### 📖 Recursos

| Recurso | Ubicación |
|---------|-----------|
| Instrucciones detalladas | `INSTALACION/README.md` |
| Documentación del sistema | `README.md` |
| Índice de roles | [Agentes](ROLES.md) |
| Índice de herramientas | [Herramientas](HERRAMIENTAS.md) |
| Repositorio en GitHub | [JavierDevCol/SAC](https://github.com/JavierDevCol/SAC) |
| Releases | [Todas las versiones](https://github.com/JavierDevCol/SAC/releases) |

---

**¿Problemas?** Abre un [issue en GitHub](https://github.com/JavierDevCol/SAC/issues) o verifica que Python y Git estén instalados correctamente.