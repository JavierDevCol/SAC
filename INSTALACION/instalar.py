#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║           INSTALADOR DE COCHAS v4.0                           ║
║   Sistema de Orquestación de Agentes IA para GitHub Copilot   ║
╚═══════════════════════════════════════════════════════════════╝

Este script instala el sistema COCHAS en cualquier proyecto.

Uso:
    python instalar.py                       # Modo interactivo
    python instalar.py "C:/mi/proyecto"      # Ruta como argumento
    python instalar.py --update              # Actualizar repo desde GitHub
    python instalar.py --help                # Mostrar ayuda
"""

import os
import sys
import shutil
import subprocess
import platform
import tempfile
from pathlib import Path
from datetime import datetime


# ============================================
# CONFIGURACIÓN
# ============================================

# URL del repositorio de COCHAS
REPO_URL = "https://github.com/JavierDevCol/SAC.git"
REPO_NAME = "SAC"
REPO_BRANCH = "feature/instalacion"  # Rama a clonar

# Carpetas a copiar desde la raíz de ia_prompts
CARPETAS_COCHAS = [
    "agentes",
    "herramientas", 
    "plantillas",
    "ejemplos",
    "config"
]

# Carpeta de agentes de GitHub (relativa a INSTALACION/)
GITHUB_AGENTS_SOURCE = ".github/agents"


# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def print_banner():
    """Muestra el banner de bienvenida."""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🤖 INSTALADOR DE COCHAS v4.0                                ║
║   Sistema de Orquestación de Agentes IA                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)


def print_success(message):
    """Imprime mensaje de éxito."""
    print(f"  ✅ {message}")


def print_error(message):
    """Imprime mensaje de error."""
    print(f"  ❌ {message}")


def print_info(message):
    """Imprime mensaje informativo."""
    print(f"  ℹ️  {message}")


def print_warning(message):
    """Imprime mensaje de advertencia."""
    print(f"  ⚠️  {message}")


def get_script_directory():
    """Obtiene el directorio donde está el script."""
    return Path(__file__).parent.absolute()


def get_root_directory():
    """Obtiene el directorio raíz de ia_prompts (padre de INSTALACION)."""
    return get_script_directory().parent


def get_temp_repo_path():
    """
    Obtiene la ruta temporal donde se clonará el repositorio.
    - Windows: %TEMP%/cochas_repo/
    - Linux/Mac: /tmp/cochas_repo/
    """
    if platform.system() == "Windows":
        temp_base = Path(tempfile.gettempdir())
    else:
        temp_base = Path("/tmp")
    
    return temp_base / "cochas_repo"


def is_git_available():
    """Verifica si Git está disponible en el sistema."""
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def is_local_install():
    """
    Verifica si el script se está ejecutando desde una instalación local
    (dentro del proyecto ia_prompts completo).
    """
    root_dir = get_root_directory()
    
    # Verificar si existen las carpetas necesarias en el padre
    for folder in CARPETAS_COCHAS:
        if not (root_dir / folder).exists():
            return False
    
    return True


def clone_repository(dest_path):
    """Clona el repositorio desde GitHub."""
    print_info(f"Clonando repositorio desde {REPO_URL}...")
    
    try:
        # Eliminar carpeta si existe
        if dest_path.exists():
            shutil.rmtree(dest_path)
        
        # Crear carpeta padre si no existe
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Clonar repositorio
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, str(dest_path)],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print_success("Repositorio clonado correctamente")
            return True
        else:
            print_error(f"Error al clonar: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print_error("Tiempo de espera agotado al clonar el repositorio")
        return False
    except Exception as e:
        print_error(f"Error inesperado: {e}")
        return False


def update_repository(repo_path):
    """Actualiza el repositorio con git pull."""
    print_info("Actualizando repositorio...")
    
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path), "pull", "--ff-only"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            if "Already up to date" in result.stdout or "Ya está actualizado" in result.stdout:
                print_success("El repositorio ya está actualizado")
            else:
                print_success("Repositorio actualizado correctamente")
            return True
        else:
            print_error(f"Error al actualizar: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print_error("Tiempo de espera agotado al actualizar")
        return False
    except Exception as e:
        print_error(f"Error inesperado: {e}")
        return False


def ensure_repo_available():
    """
    Asegura que el repositorio esté disponible.
    Retorna la ruta al directorio raíz de ia_prompts.
    """
    # Primero verificar si estamos en una instalación local
    if is_local_install():
        print_info("Usando instalación local")
        return get_root_directory()
    
    # Si no, necesitamos clonar/actualizar desde GitHub
    print_info("No se encontró instalación local, usando repositorio remoto...")
    
    if not is_git_available():
        print_error("Git no está instalado o no está disponible en el PATH")
        print_info("Instala Git desde: https://git-scm.com/downloads")
        print_info("O usa Chocolatey: choco install git")
        return None
    
    temp_repo_path = get_temp_repo_path()
    
    # Si ya existe el repo en temp, actualizarlo
    if temp_repo_path.exists() and (temp_repo_path / ".git").exists():
        print_info(f"Repositorio encontrado en {temp_repo_path}")
        if update_repository(temp_repo_path):
            return temp_repo_path
        else:
            # Si falla el update, intentar clonar de nuevo
            print_warning("Fallo la actualización, re-clonando...")
            if clone_repository(temp_repo_path):
                return temp_repo_path
            return None
    else:
        # Clonar el repositorio
        if clone_repository(temp_repo_path):
            return temp_repo_path
        return None


def validate_source_folders(root_dir):
    """Valida que existan las carpetas fuente necesarias."""
    missing = []
    for folder in CARPETAS_COCHAS:
        if not (root_dir / folder).exists():
            missing.append(folder)
    return missing


def validate_destination(dest_path):
    """Valida el directorio destino."""
    path = Path(dest_path)
    
    if not path.exists():
        return False, f"La ruta no existe: {dest_path}"
    
    if not path.is_dir():
        return False, f"La ruta no es un directorio: {dest_path}"
    
    return True, None


def check_existing_installation(dest_path):
    """Verifica si ya existe una instalación de COCHAS."""
    cochas_path = Path(dest_path) / ".cochas"
    github_agents_path = Path(dest_path) / ".github" / "agents"
    
    existing = []
    if cochas_path.exists():
        existing.append(".cochas/")
    if github_agents_path.exists():
        existing.append(".github/agents/")
    
    return existing


def copy_folder(source, destination, folder_name):
    """Copia una carpeta completa."""
    src = source / folder_name
    dst = destination / folder_name
    
    if dst.exists():
        shutil.rmtree(dst)
    
    shutil.copytree(src, dst)
    return True


def get_github_agents_source(root_dir):
    """
    Obtiene la ruta a los archivos de .github/agents.
    Puede estar en INSTALACION/.github/agents o directamente en el repo.
    """
    # Primero intentar en INSTALACION/
    instalacion_path = root_dir / "INSTALACION" / ".github" / "agents"
    if instalacion_path.exists():
        return instalacion_path
    
    # Si no, buscar en la raíz del repo
    root_github_path = root_dir / ".github" / "agents"
    if root_github_path.exists():
        return root_github_path
    
    return None


def install_cochas(dest_path, root_dir):
    """Ejecuta la instalación de COCHAS."""
    dest = Path(dest_path)
    
    print("\n📦 Iniciando instalación...\n")
    
    # 1. Crear carpeta .cochas
    cochas_dest = dest / ".cochas"
    cochas_dest.mkdir(exist_ok=True)
    print_info(f"Creando {cochas_dest}")
    
    # 2. Copiar carpetas desde la raíz
    print("\n📂 Copiando carpetas del sistema:\n")
    for folder in CARPETAS_COCHAS:
        try:
            copy_folder(root_dir, cochas_dest, folder)
            print_success(f"{folder}/")
        except Exception as e:
            print_error(f"{folder}/ - Error: {e}")
            return False
    
    # 3. Crear carpeta .github/agents
    github_dest = dest / ".github" / "agents"
    github_dest.mkdir(parents=True, exist_ok=True)
    
    # 4. Copiar archivos de activación de agentes
    print("\n📂 Copiando activadores de Copilot:\n")
    github_source = get_github_agents_source(root_dir)
    
    if github_source and github_source.exists():
        for agent_file in github_source.glob("*.agent.md"):
            try:
                shutil.copy2(agent_file, github_dest / agent_file.name)
                print_success(f".github/agents/{agent_file.name}")
            except Exception as e:
                print_error(f"{agent_file.name} - Error: {e}")
                return False
    else:
        print_warning("No se encontró la carpeta de activadores .github/agents")
        print_info("Puedes copiarlos manualmente desde INSTALACION/.github/agents/")
    
    # 5. Crear carpetas de artefactos (vacías)
    print("\n📂 Creando estructura de artefactos:\n")
    
    session_dir = cochas_dest / "session"
    artifacts_dir = cochas_dest / "artifacts"
    hu_dir = artifacts_dir / "HU"
    
    session_dir.mkdir(exist_ok=True)
    print_success(".cochas/session/")
    
    artifacts_dir.mkdir(exist_ok=True)
    print_success(".cochas/artifacts/")
    
    hu_dir.mkdir(exist_ok=True)
    print_success(".cochas/artifacts/HU/")
    
    return True


def print_final_summary(dest_path):
    """Muestra el resumen final de la instalación."""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                  ✅ INSTALACIÓN COMPLETADA                    ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print(f"📍 Ubicación: {dest_path}\n")
    
    print("📁 Estructura creada:\n")
    print(f"""    {dest_path}/
    ├── .cochas/
    │   ├── agentes/          (5 agentes)
    │   ├── herramientas/     (9 herramientas)
    │   ├── plantillas/       (6 plantillas)
    │   ├── ejemplos/         (ejemplos de uso)
    │   ├── config/           (configuración)
    │   ├── session/          (estado de sesión)
    │   └── artifacts/        (artefactos generados)
    │       └── HU/           (historias de usuario)
    └── .github/
        └── agents/           (5 activadores Copilot)
    """)
    
    print("🚀 Cómo usar:\n")
    print("    1. Abre VS Code en tu proyecto")
    print("    2. Abre Copilot Chat (Ctrl+Shift+I)")
    print("    3. Escribe @ y selecciona un agente:")
    print("       • @arquitecto")
    print("       • @desarrollador") 
    print("       • @devops")
    print("       • @analista_historias")
    print("       • @narrador_commit")
    print()


def print_help():
    """Muestra la ayuda del comando."""
    print("""
📖 USO:
    python instalar.py [RUTA]              Instala COCHAS en la ruta especificada
    python instalar.py                     Modo interactivo (pide la ruta)
    python instalar.py --update            Actualiza el repositorio en caché
    python instalar.py --help              Muestra esta ayuda

📍 EJEMPLOS:
    python instalar.py "C:/proyectos/mi-app"
    python instalar.py "/home/user/mi-proyecto"
    python instalar.py --update

🔧 OPCIONES:
    --update    Actualiza el repositorio COCHAS desde GitHub sin instalar.
                Útil para obtener la última versión antes de instalar.
    
    --help      Muestra este mensaje de ayuda.

📦 FUENTES:
    El script primero busca los archivos localmente.
    Si no los encuentra, clona automáticamente desde:
    {repo_url}
    
    El repositorio se guarda en:
    - Windows: %TEMP%/cochas_repo/
    - Linux/Mac: /tmp/cochas_repo/
""".format(repo_url=REPO_URL))


def do_update():
    """Ejecuta solo la actualización del repositorio."""
    print_banner()
    print("🔄 Modo actualización\n")
    
    if not is_git_available():
        print_error("Git no está instalado o no está disponible en el PATH")
        return False
    
    temp_repo_path = get_temp_repo_path()
    
    if temp_repo_path.exists() and (temp_repo_path / ".git").exists():
        print_info(f"Repositorio en: {temp_repo_path}")
        return update_repository(temp_repo_path)
    else:
        print_info("No existe repositorio en caché, clonando...")
        return clone_repository(temp_repo_path)


def main():
    """Función principal."""
    
    # Procesar argumentos
    args = sys.argv[1:]
    
    # --help
    if "--help" in args or "-h" in args:
        print_banner()
        print_help()
        sys.exit(0)
    
    # --update
    if "--update" in args:
        success = do_update()
        sys.exit(0 if success else 1)
    
    print_banner()
    
    # Obtener la raíz del proyecto (local o remoto)
    root_dir = ensure_repo_available()
    if root_dir is None:
        print_error("No se pudo obtener el repositorio de COCHAS")
        sys.exit(1)
    
    # Validar carpetas fuente
    missing = validate_source_folders(root_dir)
    if missing:
        print_error(f"Faltan carpetas fuente: {', '.join(missing)}")
        print_info(f"Directorio raíz: {root_dir}")
        sys.exit(1)
    
    # Obtener ruta destino
    if args and not args[0].startswith("--"):
        dest_path = args[0]
    else:
        print("📍 Ingresa la ruta donde instalar COCHAS:\n")
        print("   (La carpeta debe existir)\n")
        dest_path = input("   Ruta: ").strip()
        
        if not dest_path:
            print_error("No se proporcionó una ruta")
            sys.exit(1)
    
    # Expandir ~ y variables de entorno
    dest_path = os.path.expanduser(dest_path)
    dest_path = os.path.expandvars(dest_path)
    dest_path = os.path.abspath(dest_path)
    
    # Validar destino
    valid, error = validate_destination(dest_path)
    if not valid:
        print_error(error)
        sys.exit(1)
    
    print(f"\n📍 Destino: {dest_path}")
    print(f"📦 Fuente: {root_dir}\n")
    
    # Verificar instalación existente
    existing = check_existing_installation(dest_path)
    if existing:
        print_warning(f"Ya existe una instalación: {', '.join(existing)}")
        response = input("\n   ¿Sobrescribir? (s/N): ").strip().lower()
        if response != 's':
            print_info("Instalación cancelada")
            sys.exit(0)
    
    # Ejecutar instalación
    success = install_cochas(dest_path, root_dir)
    
    if success:
        print_final_summary(dest_path)
    else:
        print_error("La instalación falló")
        sys.exit(1)


if __name__ == "__main__":
    main()