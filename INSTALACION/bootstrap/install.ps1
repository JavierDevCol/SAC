#Requires -Version 5.1
<#
.SYNOPSIS
    Instalador bootstrap de SAC (Sistema Agéntico COCHAS) para Windows

.DESCRIPTION
    Este script descarga e instala SAC en el sistema, configurando el comando
    global 'sac' para que esté disponible desde cualquier terminal.

.EXAMPLE
    irm https://raw.githubusercontent.com/JavierDevCol/SAC/feature/instalacion/INSTALACION/bootstrap/install.ps1 | iex

.NOTES
    Autor: SAC Team
    Versión: 1.0
    Requiere: PowerShell 5.1+, Python 3.8+, Git
#>

$ErrorActionPreference = "Stop"

# ============================================
# CONFIGURACIÓN
# ============================================
$SAC_HOME = "$env:LOCALAPPDATA\SAC"
$REPO_URL = "https://github.com/JavierDevCol/SAC.git"
$REPO_BRANCH = "feature/instalacion"

# ============================================
# FUNCIONES DE UTILIDAD
# ============================================
function Write-Banner {
    Write-Host ""
    Write-Host "╔═══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                                                               ║" -ForegroundColor Cyan
    Write-Host "║   🤖 SAC - Sistema Agéntico COCHAS                            ║" -ForegroundColor Cyan
    Write-Host "║   Instalador Bootstrap para Windows                           ║" -ForegroundColor Cyan
    Write-Host "║                                                               ║" -ForegroundColor Cyan
    Write-Host "╚═══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "  ✅ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "  ❌ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "  ℹ️  $Message" -ForegroundColor Yellow
}

function Write-Warning {
    param([string]$Message)
    Write-Host "  ⚠️  $Message" -ForegroundColor Yellow
}

# ============================================
# VALIDACIONES
# ============================================
function Test-Prerequisites {
    Write-Host "🔍 Verificando requisitos previos..." -ForegroundColor White
    Write-Host ""
    
    # Verificar Python
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Error "Python no está instalado o no está en el PATH"
        Write-Info "Descarga Python desde: https://www.python.org/downloads/"
        return $false
    }
    
    $pythonVersion = & python --version 2>&1
    Write-Success "Python encontrado: $pythonVersion"
    
    # Verificar Git
    $git = Get-Command git -ErrorAction SilentlyContinue
    if (-not $git) {
        Write-Error "Git no está instalado o no está en el PATH"
        Write-Info "Descarga Git desde: https://git-scm.com/downloads"
        return $false
    }
    
    $gitVersion = & git --version 2>&1
    Write-Success "Git encontrado: $gitVersion"
    
    Write-Host ""
    return $true
}

# ============================================
# INSTALACIÓN
# ============================================
function Install-SAC {
    Write-Host "📦 Instalando SAC..." -ForegroundColor White
    Write-Host ""
    
    # 1. Crear estructura de carpetas
    Write-Info "Creando estructura de carpetas..."
    
    $repoPath = Join-Path $SAC_HOME "repo"
    $binPath = Join-Path $SAC_HOME "bin"
    
    if (-not (Test-Path $SAC_HOME)) {
        New-Item -ItemType Directory -Force -Path $SAC_HOME | Out-Null
    }
    
    if (-not (Test-Path $binPath)) {
        New-Item -ItemType Directory -Force -Path $binPath | Out-Null
    }
    
    Write-Success "Carpeta SAC creada: $SAC_HOME"
    
    # 2. Clonar o actualizar repositorio
    if (Test-Path (Join-Path $repoPath ".git")) {
        Write-Info "Repositorio existente, actualizando..."
        Push-Location $repoPath
        try {
            Start-Process -FilePath "git" -ArgumentList "fetch", "origin" -NoNewWindow -Wait
            Start-Process -FilePath "git" -ArgumentList "checkout", $REPO_BRANCH -NoNewWindow -Wait
            Start-Process -FilePath "git" -ArgumentList "pull", "origin", $REPO_BRANCH -NoNewWindow -Wait
            Write-Success "Repositorio actualizado"
        }
        catch {
            Write-Warning "No se pudo actualizar, usando versión existente"
        }
        finally {
            Pop-Location
        }
    }
    else {
        Write-Info "Clonando repositorio desde GitHub..."
        
        if (Test-Path $repoPath) {
            Remove-Item -Recurse -Force $repoPath
        }
        
        # Ejecutar git clone suprimiendo stderr (git escribe progreso a stderr)
        $env:GIT_TERMINAL_PROMPT = "0"
        Start-Process -FilePath "git" -ArgumentList "clone", "--branch", $REPO_BRANCH, $REPO_URL, $repoPath -NoNewWindow -Wait -RedirectStandardError "$env:TEMP\git_clone_err.txt"
        
        if (-not (Test-Path (Join-Path $repoPath ".git"))) {
            Write-Error "Error al clonar el repositorio"
            if (Test-Path "$env:TEMP\git_clone_err.txt") {
                $errContent = Get-Content "$env:TEMP\git_clone_err.txt" -Raw
                Write-Host "  Detalles: $errContent" -ForegroundColor Yellow
            }
            return $false
        }
        
        Write-Success "Repositorio clonado"
    }
    
    # 3. Crear comando global sac.bat
    Write-Info "Creando comando global 'sac'..."
    
    $sacBatPath = Join-Path $binPath "sac.bat"
    $sacBatContent = @"
@echo off
python "%LOCALAPPDATA%\SAC\repo\INSTALACION\instalar.py" %*
"@
    
    Set-Content -Path $sacBatPath -Value $sacBatContent -Encoding ASCII
    Write-Success "Comando 'sac.bat' creado"
    
    # 4. Crear comando sac.ps1 para PowerShell
    $sacPs1Path = Join-Path $binPath "sac.ps1"
    $sacPs1Content = @'
# SAC - Sistema Agéntico COCHAS
# Wrapper para PowerShell

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

$installerPath = "$env:LOCALAPPDATA\SAC\repo\INSTALACION\instalar.py"

if ($Arguments) {
    & python $installerPath @Arguments
} else {
    & python $installerPath
}
'@
    
    Set-Content -Path $sacPs1Path -Value $sacPs1Content -Encoding UTF8
    Write-Success "Comando 'sac.ps1' creado"
    
    # 5. Agregar al PATH si no está
    Write-Info "Configurando PATH del sistema..."
    
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    
    if ($userPath -notlike "*$binPath*") {
        $newPath = "$userPath;$binPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Success "Carpeta agregada al PATH del usuario"
        
        # Actualizar PATH de la sesión actual
        $env:Path = "$env:Path;$binPath"
    }
    else {
        Write-Info "PATH ya contiene la carpeta de SAC"
    }
    
    Write-Host ""
    return $true
}

# ============================================
# OBTENER VERSIÓN
# ============================================
function Get-SACVersion {
    $configPath = Join-Path $SAC_HOME "repo\config\CONFIG_SYSTEM.yaml"
    
    if (Test-Path $configPath) {
        $content = Get-Content $configPath -Raw
        if ($content -match 'version:\s*"?([^"\s]+)"?') {
            return $matches[1]
        }
    }
    
    return "desconocida"
}

# ============================================
# RESUMEN FINAL
# ============================================
function Write-Summary {
    $version = Get-SACVersion
    
    Write-Host ""
    Write-Host "╔═══════════════════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║                                                               ║" -ForegroundColor Green
    Write-Host "║   ✅ SAC INSTALADO CORRECTAMENTE                              ║" -ForegroundColor Green
    Write-Host "║                                                               ║" -ForegroundColor Green
    Write-Host "╚═══════════════════════════════════════════════════════════════╝" -ForegroundColor Green
    Write-Host ""
    Write-Host "   📍 Ubicación:  $SAC_HOME" -ForegroundColor White
    Write-Host "   📦 Versión:    $version" -ForegroundColor White
    Write-Host ""
    Write-Host "   🚀 Comandos disponibles:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "      sac --help              Ver ayuda" -ForegroundColor Gray
    Write-Host "      sac `"C:\mi-proyecto`"    Instalar en un proyecto" -ForegroundColor Gray
    Write-Host "      sac --update            Actualizar SAC" -ForegroundColor Gray
    Write-Host "      sac --upgrade-all       Actualizar todas las instalaciones" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   ⚠️  IMPORTANTE: Reinicia la terminal para que el comando 'sac'" -ForegroundColor Yellow
    Write-Host "      esté disponible globalmente." -ForegroundColor Yellow
    Write-Host ""
}

# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================
Write-Banner

if (-not (Test-Prerequisites)) {
    Write-Host ""
    Write-Error "No se cumplen los requisitos previos. Instalación cancelada."
    exit 1
}

if (-not (Install-SAC)) {
    Write-Host ""
    Write-Error "La instalación falló."
    exit 1
}

Write-Summary
