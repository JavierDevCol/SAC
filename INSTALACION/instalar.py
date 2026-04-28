#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║           INSTALADOR DE COCHAS v6.0                           ║
║   Sistema de Orquestación de Agentes IA para GitHub Copilot   ║
╚═══════════════════════════════════════════════════════════════╝

Este script instala el sistema COCHAS en cualquier proyecto.

Uso:
    python instalar.py                       # Modo interactivo
    python instalar.py "C:/mi/proyecto"      # Ruta como argumento
    python instalar.py --update              # Actualizar repo desde GitHub
    python instalar.py --upgrade-all         # Actualizar todas las instalaciones
    python instalar.py --help                # Mostrar ayuda
"""

import os
import sys
import shutil
import subprocess
import platform
import tempfile
import json
import hashlib
from pathlib import Path
from datetime import datetime

# ============================================
# CONFIGURACIÓN DE CODIFICACIÓN (Windows)
# ============================================
# Forzar UTF-8 en la salida estándar para Windows
if platform.system() == "Windows":
    # Configurar la consola de Windows para UTF-8
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            # Python < 3.7
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        try:
            sys.stderr.reconfigure(encoding='utf-8')
        except AttributeError:
            import io
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# ============================================
# CONFIGURACIÓN
# ============================================

# URL del repositorio de COCHAS
REPO_URL = "https://github.com/JavierDevCol/SAC.git"
REPO_NAME = "SAC"
REPO_BRANCH = "main"  # Rama principal para instalación

# Carpetas a copiar desde la raíz de ia_prompts
CARPETAS_COCHAS = [
    "agentes",
    "herramientas", 
    "plantillas",
    "config",
    "reglas"
]

# Carpeta de agentes de GitHub (relativa a INSTALACION/)
GITHUB_AGENTS_SOURCE = ".github/agents"

# Flag interno para evitar bucles de reinicio
RELAUNCH_FLAG = "--_relaunched"


# ============================================
# FUNCIONES DE AUTO-REINICIO
# ============================================

def get_file_hash(file_path):
    """
    Calcula el hash MD5 de un archivo.
    Retorna None si el archivo no existe.
    """
    try:
        with open(file_path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return None


def relaunch_script(new_script_path, original_args):
    """
    Relanza el script con la nueva versión.
    Agrega flag para evitar bucles infinitos.
    """
    print()
    print("─" * 55)
    print_info("🔄 El instalador se actualizó. Reiniciando con la nueva versión...")
    print("─" * 55)
    print()
    
    # Filtrar argumentos internos y agregar flag de relanzamiento
    clean_args = [arg for arg in original_args if arg != RELAUNCH_FLAG]
    
    # Construir comando
    cmd = [sys.executable, str(new_script_path)] + clean_args + [RELAUNCH_FLAG]
    
    try:
        # Ejecutar el nuevo script y esperar a que termine
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except Exception as e:
        print_error(f"Error al relanzar el script: {e}")
        print_info("Ejecuta 'sac --update' nuevamente para usar la nueva versión")
        return False


# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def get_system_version():
    """Obtiene la versión del sistema desde CONFIG_SYSTEM.yaml del repositorio."""
    # Intentar obtener desde el repo local primero
    script_dir = Path(__file__).parent.absolute()
    root_dir = script_dir.parent
    config_path = root_dir / "config" / "CONFIG_SYSTEM.yaml"
    
    if not config_path.exists():
        # Intentar desde el repo en caché
        if platform.system() == "Windows":
            local_app_data = os.environ.get("LOCALAPPDATA")
            if local_app_data:
                config_path = Path(local_app_data) / "SAC" / "repo" / "config" / "CONFIG_SYSTEM.yaml"
        else:
            config_path = Path.home() / ".local" / "share" / "SAC" / "repo" / "config" / "CONFIG_SYSTEM.yaml"
    
    if config_path.exists():
        try:
            content = config_path.read_text(encoding="utf-8")
            for line in content.split("\n"):
                if line.strip().startswith("version:"):
                    return line.split(":", 1)[1].strip().strip('"').strip("'")
        except Exception:
            pass
    
    return "not_fount"


def print_banner():
    """Muestra el banner de bienvenida."""
    version = get_system_version()
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🤖 SAC - Sistema Agéntico COCHAS v{version}                      ║
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
    Obtiene la ruta donde se clonará/almacenará el repositorio.
    Usa ubicaciones permanentes según el sistema operativo:
    - Windows: %LOCALAPPDATA%/SAC/repo/
    - Linux/Mac: ~/.local/share/SAC/repo/
    """
    if platform.system() == "Windows":
        # Usar %LOCALAPPDATA% (ej: C:\Users\Usuario\AppData\Local)
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            base_path = Path(local_app_data) / "SAC" / "repo"
        else:
            # Fallback si no existe la variable
            base_path = Path.home() / "AppData" / "Local" / "SAC" / "repo"
    else:
        # Linux/Mac: ~/.local/share/SAC/repo/
        base_path = Path.home() / ".local" / "share" / "SAC" / "repo"
    
    return base_path


def get_installations_cache_path():
    """
    Obtiene la ruta del archivo de caché de instalaciones.
    - Windows: %LOCALAPPDATA%/SAC/installations.json
    - Linux/Mac: ~/.local/share/SAC/installations.json
    """
    if platform.system() == "Windows":
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            base_path = Path(local_app_data) / "SAC"
        else:
            base_path = Path.home() / "AppData" / "Local" / "SAC"
    else:
        base_path = Path.home() / ".local" / "share" / "SAC"
    
    return base_path / "installations.json"


def load_installations_cache():
    """Carga el archivo de caché de instalaciones."""
    cache_path = get_installations_cache_path()
    
    if not cache_path.exists():
        return {"version": "1.0", "installations": []}
    
    try:
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception):
        return {"version": "1.0", "installations": []}


def save_installations_cache(cache_data):
    """Guarda el archivo de caché de instalaciones."""
    cache_path = get_installations_cache_path()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print_warning(f"No se pudo guardar caché de instalaciones: {e}")
        return False


def register_installation(dest_path, system_version):
    """Registra una nueva instalación en la caché."""
    cache = load_installations_cache()
    normalized_path = Path(dest_path).resolve().as_posix()
    now = datetime.now().isoformat()
    
    # Buscar si ya existe
    existing_idx = None
    for idx, inst in enumerate(cache["installations"]):
        if inst["path"] == normalized_path:
            existing_idx = idx
            break
    
    installation_entry = {
        "path": normalized_path,
        "installed_at": now if existing_idx is None else cache["installations"][existing_idx].get("installed_at", now),
        "last_updated": now,
        "system_version": system_version
    }
    
    if existing_idx is not None:
        cache["installations"][existing_idx] = installation_entry
    else:
        cache["installations"].append(installation_entry)
    
    save_installations_cache(cache)


def get_installed_version(dest_path):
    """Obtiene la versión instalada en una ruta desde CONFIG_SYSTEM.yaml."""
    # Buscar primero en .SAC, luego en .cochas (migración)
    config_path = Path(dest_path) / ".SAC" / "config" / "CONFIG_SYSTEM.yaml"
    if not config_path.exists():
        config_path = Path(dest_path) / ".cochas" / "config" / "CONFIG_SYSTEM.yaml"
    
    if not config_path.exists():
        return None
    
    try:
        content = config_path.read_text(encoding="utf-8")
        for line in content.split("\n"):
            if line.strip().startswith("version:"):
                # Extraer versión: version: "4.0" -> 4.0
                version = line.split(":", 1)[1].strip().strip('"').strip("'")
                return version
        return None
    except Exception:
        return None


def get_repo_version(root_dir):
    """Obtiene la versión del repositorio desde CONFIG_SYSTEM.yaml."""
    config_path = Path(root_dir) / "config" / "CONFIG_SYSTEM.yaml"
    
    if not config_path.exists():
        return None
    
    try:
        content = config_path.read_text(encoding="utf-8")
        for line in content.split("\n"):
            if line.strip().startswith("version:"):
                version = line.split(":", 1)[1].strip().strip('"').strip("'")
                return version
        return None
    except Exception:
        return None


def validate_and_clean_cache():
    """
    Valida las instalaciones en caché y elimina las rutas huérfanas.
    Retorna lista de instalaciones válidas con su estado.
    """
    cache = load_installations_cache()
    valid_installations = []
    removed_paths = []
    
    for inst in cache["installations"]:
        path = inst["path"]
        # Verificar tanto .SAC como .cochas (para migración)
        sac_path = Path(path) / ".SAC"
        cochas_path = Path(path) / ".cochas"
        
        if sac_path.exists() or cochas_path.exists():
            installed_version = get_installed_version(path)
            valid_installations.append({
                **inst,
                "current_version": installed_version,
                "exists": True
            })
        else:
            removed_paths.append(path)
    
    # Actualizar caché eliminando rutas huérfanas
    if removed_paths:
        cache["installations"] = [
            inst for inst in cache["installations"]
            if inst["path"] not in removed_paths
        ]
        save_installations_cache(cache)
    
    return valid_installations, removed_paths


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
    """Clona el repositorio desde GitHub y cambia a la rama correcta."""
    print_info(f"Clonando repositorio desde {REPO_URL}...")
    print_info(f"Rama objetivo: {REPO_BRANCH}")
    
    try:
        # Eliminar carpeta si existe
        if dest_path.exists():
            shutil.rmtree(dest_path)
        
        # Crear carpeta padre si no existe
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Intentar clonar directamente la rama específica
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, str(dest_path)],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print_success(f"Repositorio clonado correctamente (rama: {REPO_BRANCH})")
            # Configurar safe.directory INMEDIATAMENTE para evitar errores de ownership en Windows
            configure_git_safe_directory(dest_path)
            return True
        else:
            # Si falla el clone de la rama específica, intentar clone normal + checkout
            print_warning(f"No se pudo clonar la rama '{REPO_BRANCH}' directamente")
            print_info("Intentando clone completo y checkout...")
            
            # Clone sin especificar rama
            result_full = subprocess.run(
                ["git", "clone", REPO_URL, str(dest_path)],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result_full.returncode != 0:
                print_error(f"Error al clonar: {result_full.stderr}")
                return False
            
            # Configurar safe.directory antes de hacer checkout
            configure_git_safe_directory(dest_path)
            
            # Hacer checkout de la rama
            result_checkout = subprocess.run(
                ["git", "-C", str(dest_path), "checkout", REPO_BRANCH],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result_checkout.returncode == 0:
                print_success(f"Repositorio clonado y cambiado a rama: {REPO_BRANCH}")
                return True
            else:
                # Si la rama no existe, intentar crearla desde origin
                result_fetch = subprocess.run(
                    ["git", "-C", str(dest_path), "fetch", "origin", REPO_BRANCH],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result_fetch.returncode == 0:
                    result_checkout2 = subprocess.run(
                        ["git", "-C", str(dest_path), "checkout", "-b", REPO_BRANCH, f"origin/{REPO_BRANCH}"],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result_checkout2.returncode == 0:
                        print_success(f"Repositorio clonado y cambiado a rama: {REPO_BRANCH}")
                        return True
                
                print_error(f"La rama '{REPO_BRANCH}' no existe en el repositorio remoto")
                print_info("Verifica que la rama exista en GitHub")
                return False
            
    except subprocess.TimeoutExpired:
        print_error("Tiempo de espera agotado al clonar el repositorio")
        return False
    except Exception as e:
        print_error(f"Error inesperado: {e}")
        return False


def configure_git_safe_directory(repo_path):
    """
    Configura el directorio como safe.directory en Git.
    Necesario en Windows cuando el repo está en carpeta temporal.
    """
    try:
        # Normalizar la ruta para Git (usar forward slashes)
        safe_path = str(repo_path).replace("\\", "/")
        
        result = subprocess.run(
            ["git", "config", "--global", "--add", "safe.directory", safe_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print_info(f"Configurado safe.directory: {safe_path}")
        return result.returncode == 0
    except Exception:
        return False


def update_repository(repo_path):
    """Actualiza el repositorio con git pull, asegurando que la rama sea la correcta."""
    print_info("Actualizando repositorio...")

    try:
        # Asegurar que estamos en la rama principal y que su upstream es origin/REPO_BRANCH
        current_branch = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()

        if current_branch != REPO_BRANCH:
            # Verificar si la rama principal ya existe localmente
            branches = subprocess.run(
                ["git", "-C", str(repo_path), "branch", "--list", REPO_BRANCH],
                capture_output=True, text=True, timeout=10
            ).stdout.strip()

            if branches:
                subprocess.run(
                    ["git", "-C", str(repo_path), "checkout", REPO_BRANCH],
                    capture_output=True, text=True, timeout=10
                )
            else:
                subprocess.run(
                    ["git", "-C", str(repo_path), "checkout", "-b", REPO_BRANCH,
                     "--track", f"origin/{REPO_BRANCH}"],
                    capture_output=True, text=True, timeout=10
                )
        else:
            # Asegurar que el upstream apunta a origin/REPO_BRANCH
            subprocess.run(
                ["git", "-C", str(repo_path), "branch",
                 "--set-upstream-to", f"origin/{REPO_BRANCH}", REPO_BRANCH],
                capture_output=True, text=True, timeout=10
            )

        # Hacer fetch explícito de la rama correcta
        fetch_result = subprocess.run(
            ["git", "-C", str(repo_path), "fetch", "origin", REPO_BRANCH],
            capture_output=True, text=True, timeout=60
        )
        if fetch_result.returncode != 0:
            print_error(f"Error al hacer fetch: {fetch_result.stderr}")
            return False

        # Pull --ff-only con rama explícita
        result = subprocess.run(
            ["git", "-C", str(repo_path), "pull", "--ff-only", "origin", REPO_BRANCH],
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


def find_cochas_root(base_path):
    """
    Busca el directorio raíz de COCHAS dentro de una ruta.
    El repositorio puede tener las carpetas en la raíz o dentro de una subcarpeta.
    """
    base = Path(base_path)
    
    # Primero verificar si las carpetas están directamente en base_path
    if all((base / folder).exists() for folder in CARPETAS_COCHAS):
        return base
    
    # Buscar en subcarpetas de primer nivel (ej: SAC/ia_prompts/, ia_prompts/)
    for subdir in base.iterdir():
        if subdir.is_dir() and not subdir.name.startswith('.'):
            if all((subdir / folder).exists() for folder in CARPETAS_COCHAS):
                return subdir
            # Buscar un nivel más profundo
            for subsubdir in subdir.iterdir():
                if subsubdir.is_dir() and not subsubdir.name.startswith('.'):
                    if all((subsubdir / folder).exists() for folder in CARPETAS_COCHAS):
                        return subsubdir
                    # Buscar un tercer nivel (por si acaso)
                    for subsubsubdir in subsubdir.iterdir():
                        if subsubsubdir.is_dir() and not subsubsubdir.name.startswith('.'):
                            if all((subsubsubdir / folder).exists() for folder in CARPETAS_COCHAS):
                                return subsubsubdir
    
    # Intentar buscar por nombre específico "ia_prompts"
    ia_prompts_candidates = list(base.rglob("ia_prompts"))
    for candidate in ia_prompts_candidates:
        if candidate.is_dir():
            if all((candidate / folder).exists() for folder in CARPETAS_COCHAS):
                return candidate
    
    # Depuración: mostrar qué carpetas hay en la raíz
    print_warning(f"No se encontró la estructura de COCHAS en {base}")
    print_info("Contenido del repositorio:")
    try:
        for item in base.iterdir():
            print_info(f"  - {item.name}{'/' if item.is_dir() else ''}")
    except Exception as e:
        print_error(f"  Error listando contenido: {e}")
    
    return None


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
        configure_git_safe_directory(temp_repo_path)
        if update_repository(temp_repo_path):
            return find_cochas_root(temp_repo_path)
        else:
            # Si falla el update, intentar clonar de nuevo
            print_warning("Fallo la actualización, re-clonando...")
            if clone_repository(temp_repo_path):
                configure_git_safe_directory(temp_repo_path)
                return find_cochas_root(temp_repo_path)
            return None
    else:
        # Clonar el repositorio
        if clone_repository(temp_repo_path):
            configure_git_safe_directory(temp_repo_path)
            return find_cochas_root(temp_repo_path)
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
    """Verifica si ya existe una instalación de SAC (o COCHAS legacy)."""
    sac_path = Path(dest_path) / ".SAC"
    cochas_path = Path(dest_path) / ".cochas"  # Legacy
    github_agents_path = Path(dest_path) / ".github" / "agents"
    
    existing = []
    if sac_path.exists():
        existing.append(".SAC/")
    if cochas_path.exists():
        existing.append(".cochas/ (legacy)")
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


def replace_project_root_placeholder(config_path, project_root):
    """Reemplaza {project-root} en CONFIG_SYSTEM.yaml por la ruta real."""
    try:
        if not config_path.exists():
            print_warning("No se encontró CONFIG_SYSTEM.yaml en la instalación")
            return

        content = config_path.read_text(encoding="utf-8")
        normalized_root = Path(project_root).resolve().as_posix()
        updated = content.replace("{project-root}", normalized_root)

        if updated != content:
            config_path.write_text(updated, encoding="utf-8")
            print_success("CONFIG_SYSTEM.yaml actualizado con la ruta del proyecto")
        else:
            print_info("CONFIG_SYSTEM.yaml no requería reemplazos")
    except Exception as e:
        print_warning(f"No se pudo actualizar CONFIG_SYSTEM.yaml: {e}")


def replace_artifacts_path(config_path, project_root, artifacts_rel):
    """
    Reemplaza la ruta por defecto de artifacts en CONFIG_SYSTEM.yaml
    por la ruta personalizada elegida por el usuario.
    Solo actúa si artifacts_rel es distinto de 'artifacts'.
    """
    if artifacts_rel == "artifacts":
        return

    try:
        if not config_path.exists():
            return

        content = config_path.read_text(encoding="utf-8")
        normalized_root = Path(project_root).resolve().as_posix()
        # Defensa: si artifacts_rel contiene la raíz del proyecto, extraer solo la parte relativa
        if artifacts_rel.startswith(normalized_root):
            artifacts_rel = artifacts_rel[len(normalized_root):].strip("/")
        elif artifacts_rel.startswith(normalized_root.lstrip("/")):
            artifacts_rel = artifacts_rel[len(normalized_root.lstrip("/")):].strip("/")
        default_artifacts = f"{normalized_root}/artifacts"
        custom_artifacts = f"{normalized_root}/{artifacts_rel}"
        updated = content.replace(default_artifacts, custom_artifacts)

        if updated != content:
            config_path.write_text(updated, encoding="utf-8")
            print_success(f"Rutas de artifacts actualizadas a: {artifacts_rel}/")
    except Exception as e:
        print_warning(f"No se pudo actualizar rutas de artifacts: {e}")


def replace_ruta_proyecto_in_agents(agents_folder, project_root):
    """Reemplaza {ruta_proyecto} en los archivos .agent.md por la ruta real."""
    try:
        normalized_root = Path(project_root).resolve().as_posix()
        replaced_count = 0
        
        for agent_file in agents_folder.glob("*.agent.md"):
            content = agent_file.read_text(encoding="utf-8")
            updated = content.replace("{ruta_proyecto}", normalized_root)
            
            if updated != content:
                agent_file.write_text(updated, encoding="utf-8")
                replaced_count += 1
        
        if replaced_count > 0:
            print_success(f"Rutas actualizadas en {replaced_count} archivo(s) de agentes")
    except Exception as e:
        print_warning(f"No se pudo actualizar rutas en archivos de agentes: {e}")


def migrate_cochas_to_sac(dest_path):
    """
    Migra una instalación existente de .cochas a .SAC.
    Preserva CONFIG_USER.yaml y session_state.json.
    Retorna True si se realizó migración, False si no había nada que migrar.
    """
    dest = Path(dest_path)
    cochas_path = dest / ".cochas"
    sac_path = dest / ".SAC"
    
    if not cochas_path.exists():
        return False
    
    if sac_path.exists():
        print_warning("Ya existe .SAC/, no se puede migrar automáticamente")
        return False
    
    print_info("Detectada instalación legacy .cochas/, migrando a .SAC/...")
    
    try:
        # Renombrar carpeta
        cochas_path.rename(sac_path)
        print_success("Carpeta .cochas/ renombrada a .SAC/")
        
        # Actualizar rutas en CONFIG_SYSTEM.yaml
        config_system = sac_path / "config" / "CONFIG_SYSTEM.yaml"
        if config_system.exists():
            content = config_system.read_text(encoding="utf-8")
            updated = content.replace(".cochas", ".SAC")
            config_system.write_text(updated, encoding="utf-8")
            print_success("CONFIG_SYSTEM.yaml actualizado con nuevas rutas")
        
        # Actualizar .gitignore si existe
        gitignore = dest / ".gitignore"
        if gitignore.exists():
            content = gitignore.read_text(encoding="utf-8")
            if ".cochas" in content and ".SAC" not in content:
                updated = content.replace(".cochas", ".SAC")
                gitignore.write_text(updated, encoding="utf-8")
                print_success(".gitignore actualizado")
        
        return True
    except Exception as e:
        print_error(f"Error durante la migración: {e}")
        return False


def migrate_artifacts_to_root(dest_path):
    """
    Migra artifacts de .SAC/artifacts/ a artifacts/ en la raíz del proyecto.
    Necesario al actualizar desde versiones anteriores a 7.2.0 donde
    artifacts_folder apuntaba a {project-root}/.SAC/artifacts.
    Retorna True si se realizó migración, False si no había nada que migrar.
    """
    dest = Path(dest_path)
    old_artifacts = dest / ".SAC" / "artifacts"
    new_artifacts = dest / "artifacts"

    if not old_artifacts.exists():
        return False

    if new_artifacts.exists():
        print_warning("Ya existe artifacts/ en la raíz, no se puede migrar automáticamente")
        print_info("Mueve manualmente el contenido de .SAC/artifacts/ a artifacts/")
        return False

    print_info("Detectados artifacts en .SAC/artifacts/, migrando a artifacts/ (raíz)...")

    try:
        shutil.move(str(old_artifacts), str(new_artifacts))
        print_success("artifacts/ movido a la raíz del proyecto")
        return True
    except Exception as e:
        print_error(f"Error durante la migración de artifacts: {e}")
        return False


def install_sac(dest_path, root_dir, artifacts_rel="artifacts"):
    """Ejecuta la instalación de SAC."""
    dest = Path(dest_path)
    
    print("\n📦 Iniciando instalación...\n")
    
    # 0. Verificar si hay instalación legacy y migrar
    cochas_legacy = dest / ".cochas"
    if cochas_legacy.exists():
        migrate_cochas_to_sac(dest_path)

    # 0.1 Migrar artifacts de .SAC/artifacts/ a artifacts/ (raíz) si viene de <7.2.0
    migrate_artifacts_to_root(dest_path)

    # 1. Crear carpeta .SAC
    sac_dest = dest / ".SAC"
    sac_dest.mkdir(exist_ok=True)
    print_info(f"Creando {sac_dest}")
    
    # 2. Copiar carpetas desde la raíz
    print("\n📂 Copiando carpetas del sistema:\n")
    for folder in CARPETAS_COCHAS:
        try:
            copy_folder(root_dir, sac_dest, folder)
            print_success(f"{folder}/")
        except Exception as e:
            print_error(f"{folder}/ - Error: {e}")
            return False

    # 2.1 Reemplazar {project-root} en la configuración instalada
    config_system_path = sac_dest / "config" / "CONFIG_SYSTEM.yaml"
    replace_project_root_placeholder(config_system_path, dest)

    # 2.2 Reemplazar ruta de artifacts si el usuario eligió una ruta personalizada
    replace_artifacts_path(config_system_path, dest, artifacts_rel)
    
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
        
        # 4.1 Reemplazar {ruta_proyecto} en los archivos de agentes copiados
        replace_ruta_proyecto_in_agents(github_dest, dest)
    else:
        print_warning("No se encontró la carpeta de activadores .github/agents")
        print_info("Puedes copiarlos manualmente desde INSTALACION/.github/agents/")
    
    # 5. Crear carpetas de artefactos (vacías)
    print("\n📂 Creando estructura de artefactos:\n")
    
    session_dir = sac_dest / "session"
    artifacts_dir = dest / artifacts_rel
    hu_dir = artifacts_dir / "HU"
    
    session_dir.mkdir(exist_ok=True)
    print_success(".SAC/session/")
    
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    print_success(f"{artifacts_rel}/")
    
    hu_dir.mkdir(exist_ok=True)
    print_success(f"{artifacts_rel}/HU/")
    
    # 6. Registrar instalación en caché
    system_version = get_installed_version(dest) or "unknown"
    register_installation(dest, system_version)
    
    return True


def print_final_summary(dest_path, artifacts_rel="artifacts"):
    """Muestra el resumen final de la instalación."""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                  ✅ INSTALACIÓN COMPLETADA                    ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print(f"📍 Ubicación: {dest_path}\n")
    
    print("📁 Estructura creada:\n")
    print(f"""    {dest_path}/
    ├── .SAC/
    │   ├── agentes/          (5 agentes)
    │   ├── herramientas/     (9 herramientas)
    │   ├── plantillas/       (6 plantillas)
    │   ├── ejemplos/         (ejemplos de uso)
    │   ├── config/           (configuración)
    │   ├── reglas/           (reglas por tecnología)
    │   └── session/          (estado de sesión)
    ├── {artifacts_rel}/            (artefactos generados)
    │   └── HU/               (historias de usuario)
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
    print("       • @cronista_de_cambios")
    print()


def collect_user_settings(dest_path):
    """
    Solicita configuración personalizada al usuario.
    Retorna un diccionario con los valores recolectados, o None si se omite.
    """
    print("""
╔═══════════════════════════════════════════════════════════════╗
║              ⚙️  CONFIGURACIÓN PERSONALIZADA                   ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print("   Vamos a personalizar COCHAS para tu proyecto.\n")
    print("   (Presiona Enter para usar el valor por defecto)\n")
    print("─" * 55 + "\n")
    
    # === INFORMACIÓN DEL USUARIO ===
    print("👤 INFORMACIÓN DEL USUARIO\n")
    nombre_usuario = input("   Tu nombre: ").strip()
    if not nombre_usuario:
        nombre_usuario = ""
        print_info("Sin nombre configurado")
    else:
        print_success(f"Nombre: {nombre_usuario}")
    
    print()
    
    # === PREFERENCIAS DE IDIOMA ===
    print("🌐 PREFERENCIAS DE IDIOMA\n")
    print("   Opciones: es (Español), en (English), pt (Português)\n")
    
    idioma_doc = input("   Idioma para documentación [es]: ").strip().lower()
    if idioma_doc not in ["es", "en", "pt"]:
        idioma_doc = "es"
    print_success(f"Documentación: {idioma_doc}")
    
    idioma_com = input("   Idioma para comunicación [es]: ").strip().lower()
    if idioma_com not in ["es", "en", "pt"]:
        idioma_com = "es"
    print_success(f"Comunicación: {idioma_com}")
    
    print()
    
    # === INFORMACIÓN DEL PROYECTO ===
    print("📁 INFORMACIÓN DEL PROYECTO\n")
    
    # Sugerir nombre basado en carpeta destino
    nombre_proyecto_default = Path(dest_path).name
    nombre_proyecto = input(f"   Nombre del proyecto [{nombre_proyecto_default}]: ").strip()
    if not nombre_proyecto:
        nombre_proyecto = nombre_proyecto_default
    print_success(f"Proyecto: {nombre_proyecto}")
    
    print()
    
    # === RUTA DE ARTIFACTS ===
    print("📂 RUTA DE ARTIFACTS\n")
    print("   Los artifacts (HU, ADR, planes, bugs) se guardan en una carpeta del proyecto.")
    print("   Ruta relativa a la raíz del proyecto.\n")
    
    artifacts_rel = input("   Ruta para artifacts [artifacts]: ").strip()
    if not artifacts_rel:
        artifacts_rel = "artifacts"
    else:
        raw_input = artifacts_rel
        # Normalizar: reemplazar backslashes
        artifacts_rel = artifacts_rel.replace("\\", "/")
        # Detectar ruta absoluta: empieza con / (Unix) o X: (Windows)
        is_absolute = artifacts_rel.startswith("/") or (len(artifacts_rel) >= 2 and artifacts_rel[1] == ":")
        artifacts_rel = artifacts_rel.strip("/")
        if is_absolute:
            dest_posix = Path(dest_path).resolve().as_posix()
            dest_stripped = dest_posix.lstrip("/")
            if artifacts_rel.startswith(dest_stripped):
                # Extraer solo la parte relativa después del project root
                artifacts_rel = artifacts_rel[len(dest_stripped):].strip("/")
                print_warning(f"Se detectó una ruta absoluta. Se extrajo la parte relativa: {artifacts_rel}/")
            else:
                # Ruta absoluta que no pertenece al proyecto destino
                print_warning(f"'{raw_input}' es una ruta absoluta que no pertenece al proyecto destino.")
                print_info(f"Debe ser relativa a: {dest_path}")
                print_info(f"Ejemplo: 'docs/artifacts' o 'documentacion/artifacts'")
                artifacts_rel = input("   Ruta relativa para artifacts [artifacts]: ").strip()
                if not artifacts_rel:
                    artifacts_rel = "artifacts"
                artifacts_rel = artifacts_rel.replace("\\", "/").strip("/")
    print_success(f"Artifacts: {artifacts_rel}/")
    
    print()
    
    return {
        "nombre_usuario": nombre_usuario,
        "idioma_doc": idioma_doc,
        "idioma_com": idioma_com,
        "nombre_proyecto": nombre_proyecto,
        "artifacts_rel": artifacts_rel,
    }


def write_user_config(dest_path, settings):
    """
    Escribe CONFIG_USER.yaml con los valores recolectados.
    Retorna True si se guardó correctamente.
    """
    artifacts_section = ""
    if settings["artifacts_rel"] != "artifacts":
        artifacts_section = f"""
# === OVERRIDE DE RUTAS (Opcional) ===
# Ruta personalizada de artifacts (relativa a la raíz del proyecto)
rutas_override:
  artifacts_folder: "{settings['artifacts_rel']}"
"""

    config_content = f"""# ============================================
# CONFIGURACIÓN DEL USUARIO/PROYECTO
# ============================================
# ✅ Editable por el usuario
# Generado automáticamente por el instalador de COCHAS
# Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# ============================================

# === INFORMACIÓN DEL USUARIO ===
usuario:
  nombre: "{settings['nombre_usuario']}"                  # Tu nombre para personalización

# === PREFERENCIAS DE IDIOMA ===
idiomas:
  documentacion: "{settings['idioma_doc']}"                 # Idioma para documentos generados (es|en|pt)
  comunicacion: "{settings['idioma_com']}"                  # Idioma para interacción con el sistema

# === INFORMACIÓN DEL PROYECTO ===
proyecto:
  nombre: "{settings['nombre_proyecto']}"                          # Nombre del proyecto
{artifacts_section}"""
    
    # Guardar archivo
    config_path = Path(dest_path) / ".SAC" / "config" / "CONFIG_USER.yaml"
    
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(config_content)
        print_success(f"Configuración guardada en: .SAC/config/CONFIG_USER.yaml")
        return True
    except Exception as e:
        print_error(f"Error al guardar configuración: {e}")
        return False


def ask_for_configuration(dest_path):
    """
    Pregunta al usuario si desea configurar SAC ahora.
    Retorna dict con settings (incluye artifacts_rel) o None si omitió.
    """
    print("\n" + "─" * 55)
    print("\n   ¿Deseas configurar SAC para tu proyecto ahora?")
    print("   (Puedes hacerlo después editando .SAC/config/CONFIG_USER.yaml)\n")
    
    response = input("   Configurar ahora (S/n): ").strip().lower()
    
    if response == 'n':
        print_info("Configuración omitida. Puedes editar CONFIG_USER.yaml más tarde.")
        return None
    
    return collect_user_settings(dest_path)


def print_help():
    """Muestra la ayuda del comando."""
    print("""
📖 USO:
    sac [RUTA]                 Instala SAC en la ruta especificada
    sac                        Modo interactivo (pide la ruta)
    sac --update               Actualiza el repositorio en caché
    sac --upgrade-all          Actualiza todas las instalaciones registradas
    sac --help                 Muestra este mensaje de ayuda

📍 EJEMPLOS:
    sac "C:/proyectos/mi-app"
    sac "/home/user/mi-proyecto"
    sac --update
    sac --upgrade-all

🔧 OPCIONES:
    --update       Actualiza el repositorio SAC desde GitHub.
                   Luego muestra las instalaciones registradas y permite
                   seleccionar cuáles actualizar.
    
    --upgrade-all  Actualiza automáticamente todas las instalaciones
                   registradas sin preguntar (útil para CI/CD).
    
    --help         Muestra este mensaje de ayuda.

📦 FUENTES:
    El script primero busca los archivos localmente.
    Si no los encuentra, clona automáticamente desde:
    {repo_url}
    
    El repositorio se guarda en:
    - Windows: %LOCALAPPDATA%\\SAC\\repo\\
    - Linux/Mac: ~/.local/share/SAC/repo/
    
    Las instalaciones se registran en:
    - Windows: %LOCALAPPDATA%\\SAC\\installations.json
    - Linux/Mac: ~/.local/share/SAC/installations.json
""".format(repo_url=REPO_URL))


def get_artifacts_rel_from_config_user(config_user_content):
    """
    Extrae el valor de rutas_override.artifacts_folder del contenido de CONFIG_USER.yaml.
    Retorna 'artifacts' si no se encuentra o está vacío.
    """
    if not config_user_content:
        return "artifacts"
    
    # Buscar artifacts_folder en rutas_override
    in_override_section = False
    for line in config_user_content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("rutas_override:"):
            in_override_section = True
            continue
        if in_override_section and stripped.startswith("artifacts_folder:"):
            value = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
            break
        # Si encontramos otra sección de nivel superior, dejamos de buscar
        if in_override_section and not stripped.startswith("#") and stripped and not stripped.startswith("-") and ":" in stripped and not stripped.startswith(" ") and not stripped.startswith("\t"):
            break
    
    return "artifacts"


def upgrade_installation(dest_path, root_dir, preserve_user_config=True):
    """
    Actualiza una instalación existente preservando CONFIG_USER.yaml.
    Retorna True si la actualización fue exitosa.
    """
    dest = Path(dest_path)
    sac_dest = dest / ".SAC"
    
    # Si existe .cochas legacy, migrar primero
    cochas_legacy = dest / ".cochas"
    if cochas_legacy.exists() and not sac_dest.exists():
        migrate_cochas_to_sac(dest_path)
        sac_dest = dest / ".SAC"
    
    # Guardar CONFIG_USER.yaml si existe
    config_user_path = sac_dest / "config" / "CONFIG_USER.yaml"
    config_user_backup = None
    artifacts_rel = "artifacts"
    
    if preserve_user_config and config_user_path.exists():
        try:
            config_user_backup = config_user_path.read_text(encoding="utf-8")
            # Leer la ruta de artifacts personalizada si existe
            artifacts_rel = get_artifacts_rel_from_config_user(config_user_backup)
        except Exception:
            pass
    
    # Ejecutar instalación normal con la ruta de artifacts preservada
    success = install_sac(dest_path, root_dir, artifacts_rel)
    
    # Restaurar CONFIG_USER.yaml
    if success and config_user_backup and preserve_user_config:
        try:
            config_user_path.write_text(config_user_backup, encoding="utf-8")
            print_success("CONFIG_USER.yaml preservado")
        except Exception as e:
            print_warning(f"No se pudo restaurar CONFIG_USER.yaml: {e}")
    
    return success


def do_update(upgrade_all=False):
    """Ejecuta la actualización del repositorio y opcionalmente actualiza instalaciones."""
    print_banner()
    print("🔄 Modo actualización\n")
    
    # Verificar si ya fue relanzado (evitar bucle infinito)
    is_relaunched = RELAUNCH_FLAG in sys.argv
    
    if not is_git_available():
        print_error("Git no está instalado o no está disponible en el PATH")
        return False
    
    temp_repo_path = get_temp_repo_path()
    
    # Calcular hash del script ANTES del update (solo si no fue relanzado)
    new_script_path = None
    old_hash = None
    if not is_relaunched:
        new_script_path = temp_repo_path / "INSTALACION" / "instalar.py"
        old_hash = get_file_hash(new_script_path) if new_script_path.exists() else None
    
    if temp_repo_path.exists() and (temp_repo_path / ".git").exists():
        print_info(f"Repositorio en: {temp_repo_path}")
        configure_git_safe_directory(temp_repo_path)
        success = update_repository(temp_repo_path)
    else:
        print_info("No existe repositorio en caché, clonando...")
        success = clone_repository(temp_repo_path)
        if success:
            configure_git_safe_directory(temp_repo_path)
    
    if not success:
        return False
    
    # Verificar si el script cambió y necesita relanzarse
    if not is_relaunched and new_script_path and new_script_path.exists():
        new_hash = get_file_hash(new_script_path)
        if old_hash and new_hash and old_hash != new_hash:
            print_success("Se detectó una nueva versión del instalador")
            # Relanzar con la nueva versión
            original_args = [arg for arg in sys.argv[1:] if arg != RELAUNCH_FLAG]
            relaunch_script(new_script_path, original_args)
            return True  # No debería llegar aquí, pero por si acaso
        elif old_hash is None and new_hash:
            # Primera vez que se clona, verificar si es diferente al actual
            current_script = Path(__file__).resolve()
            current_hash = get_file_hash(current_script)
            if current_hash and new_hash != current_hash:
                print_success("Se detectó una nueva versión del instalador")
                original_args = [arg for arg in sys.argv[1:] if arg != RELAUNCH_FLAG]
                relaunch_script(new_script_path, original_args)
                return True
    
    # Obtener versión del repositorio
    root_dir = find_cochas_root(temp_repo_path)
    if not root_dir:
        print_error("No se encontró la estructura de COCHAS en el repositorio")
        return False
    
    repo_version = get_repo_version(root_dir) or "unknown"
    print_info(f"Versión disponible: {repo_version}")
    
    # Validar y limpiar caché de instalaciones
    print("\n📋 Verificando instalaciones registradas...\n")
    valid_installations, removed_paths = validate_and_clean_cache()
    
    # Mostrar rutas eliminadas
    if removed_paths:
        print_warning(f"Se eliminaron {len(removed_paths)} ruta(s) huérfana(s) de la caché:")
        for path in removed_paths:
            print(f"      └─ {path}")
        print()
    
    if not valid_installations:
        print_info("No hay instalaciones registradas.")
        print("\n" + "─" * 50)
        response = input("\n   ¿Deseas instalar COCHAS en un proyecto nuevo? (s/N): ").strip().lower()
        
        if response == 's':
            return do_new_installation(root_dir)
        else:
            print_info("Puedes instalar más tarde con: python instalar.py \"RUTA\"")
        return True
    
    # Identificar instalaciones desactualizadas
    outdated = []
    up_to_date = []
    
    for inst in valid_installations:
        if inst["current_version"] != repo_version:
            outdated.append(inst)
        else:
            up_to_date.append(inst)
    
    # Mostrar estado de instalaciones
    print(f"   Instalaciones registradas ({len(valid_installations)}):\n")
    
    for idx, inst in enumerate(valid_installations, 1):
        path = inst["path"]
        current = inst["current_version"] or "?"
        
        if inst in outdated:
            print(f"   {idx}. {path}")
            print(f"      └─ v{current} → v{repo_version} (desactualizada)")
        else:
            print(f"   {idx}. {path}")
            print(f"      └─ v{current} ✅ Actualizada")
        print()
    
    if not outdated:
        print_success("Todas las instalaciones están actualizadas")
        return True
    
    # Modo --upgrade-all: actualizar sin preguntar
    if upgrade_all:
        print_info(f"Actualizando {len(outdated)} instalación(es)...\n")
        return do_bulk_upgrade(outdated, root_dir)
    
    # Modo interactivo: permitir selección
    print("─" * 50)
    print(f"\n   {len(outdated)} instalación(es) desactualizada(s).\n")
    print("   Opciones:")
    print("     [A] Actualizar todas las desactualizadas")
    print("     [S] Seleccionar cuáles actualizar")
    print("     [N] Nueva instalación en otro proyecto")
    print("     [X] Salir\n")
    
    response = input("   Selecciona una opción: ").strip().upper()
    
    if response == 'A':
        return do_bulk_upgrade(outdated, root_dir)
    elif response == 'S':
        return do_selective_upgrade(outdated, root_dir)
    elif response == 'N':
        return do_new_installation(root_dir)
    else:
        print_info("Operación cancelada")
        return True


def do_bulk_upgrade(installations, root_dir):
    """Actualiza múltiples instalaciones."""
    success_count = 0
    fail_count = 0
    
    for inst in installations:
        path = inst["path"]
        print(f"\n   Actualizando: {path}")
        
        if upgrade_installation(path, root_dir, preserve_user_config=True):
            success_count += 1
        else:
            fail_count += 1
    
    print("\n" + "─" * 50)
    print(f"\n   ✅ Actualizadas: {success_count}")
    if fail_count > 0:
        print(f"   ❌ Fallidas: {fail_count}")
    
    return fail_count == 0


def do_selective_upgrade(outdated, root_dir):
    """Permite al usuario seleccionar qué instalaciones actualizar."""
    print("\n   Ingresa los números de las instalaciones a actualizar")
    print("   (separados por coma, ej: 1,3,4):\n")
    
    # Mostrar lista numerada
    for idx, inst in enumerate(outdated, 1):
        print(f"     {idx}. {inst['path']}")
    
    selection = input("\n   Selección: ").strip()
    
    if not selection:
        print_info("No se seleccionó ninguna instalación")
        return True
    
    try:
        indices = [int(x.strip()) - 1 for x in selection.split(",")]
        selected = [outdated[i] for i in indices if 0 <= i < len(outdated)]
    except (ValueError, IndexError):
        print_error("Selección inválida")
        return False
    
    if not selected:
        print_info("No se seleccionó ninguna instalación válida")
        return True
    
    return do_bulk_upgrade(selected, root_dir)


def do_new_installation(root_dir):
    """Ejecuta una nueva instalación interactiva."""
    print("\n📍 Ingresa la ruta donde instalar COCHAS:\n")
    print("   (La carpeta debe existir)\n")
    dest_path = input("   Ruta: ").strip()
    
    if not dest_path:
        print_error("No se proporcionó una ruta")
        return False
    
    # Expandir ~ y variables de entorno
    dest_path = os.path.expanduser(dest_path)
    dest_path = os.path.expandvars(dest_path)
    dest_path = os.path.abspath(dest_path)
    
    # Validar destino
    valid, error = validate_destination(dest_path)
    if not valid:
        print_error(error)
        return False
    
    print(f"\n📍 Destino: {dest_path}")
    print(f"📦 Fuente: {root_dir}\n")
    
    # Verificar instalación existente
    existing = check_existing_installation(dest_path)
    if existing:
        print_warning(f"Ya existe una instalación: {', '.join(existing)}")
        overwrite = input("\n   ¿Sobrescribir? (s/N): ").strip().lower()
        if overwrite != 's':
            print_info("Instalación cancelada")
            return True
    
    # Ejecutar configuración ANTES de instalar (para obtener ruta de artifacts)
    settings = ask_for_configuration(dest_path)
    artifacts_rel = settings["artifacts_rel"] if settings else "artifacts"

    # Ejecutar instalación
    install_success = install_sac(dest_path, root_dir, artifacts_rel)
    
    if install_success:
        print_final_summary(dest_path, artifacts_rel)
        # Escribir CONFIG_USER.yaml si el usuario configuró
        if settings:
            write_user_config(dest_path, settings)
    else:
        print_error("La instalación falló")
        return False
    
    return True


def do_update_legacy():
    """Ejecuta la actualización del repositorio y opcionalmente instala."""
    print_banner()
    print("🔄 Modo actualización\n")
    
    if not is_git_available():
        print_error("Git no está instalado o no está disponible en el PATH")
        return False
    
    temp_repo_path = get_temp_repo_path()
    
    if temp_repo_path.exists() and (temp_repo_path / ".git").exists():
        print_info(f"Repositorio en: {temp_repo_path}")
        configure_git_safe_directory(temp_repo_path)
        success = update_repository(temp_repo_path)
    else:
        print_info("No existe repositorio en caché, clonando...")
        success = clone_repository(temp_repo_path)
        if success:
            configure_git_safe_directory(temp_repo_path)
    
    if not success:
        return False
    
    # Preguntar si desea instalar
    print("\n" + "─" * 50)
    response = input("\n   ¿Deseas instalar COCHAS en un proyecto ahora? (s/N): ").strip().lower()
    
    if response == 's':
        print("\n📍 Ingresa la ruta donde instalar COCHAS:\n")
        print("   (La carpeta debe existir)\n")
        dest_path = input("   Ruta: ").strip()
        
        if not dest_path:
            print_error("No se proporcionó una ruta")
            return False
        
        # Expandir ~ y variables de entorno
        dest_path = os.path.expanduser(dest_path)
        dest_path = os.path.expandvars(dest_path)
        dest_path = os.path.abspath(dest_path)
        
        # Validar destino
        valid, error = validate_destination(dest_path)
        if not valid:
            print_error(error)
            return False
        
        print(f"\n📍 Destino: {dest_path}")
        print(f"📦 Fuente: {temp_repo_path}\n")
        
        # Verificar instalación existente
        existing = check_existing_installation(dest_path)
        if existing:
            print_warning(f"Ya existe una instalación: {', '.join(existing)}")
            overwrite = input("\n   ¿Sobrescribir? (s/N): ").strip().lower()
            if overwrite != 's':
                print_info("Instalación cancelada")
                return True  # El update fue exitoso
        
        # Ejecutar configuración ANTES de instalar
        settings = ask_for_configuration(dest_path)
        artifacts_rel = settings["artifacts_rel"] if settings else "artifacts"

        # Ejecutar instalación
        install_success = install_sac(dest_path, temp_repo_path, artifacts_rel)
        
        if install_success:
            print_final_summary(dest_path, artifacts_rel)
            if settings:
                write_user_config(dest_path, settings)
        else:
            print_error("La instalación falló")
            return False
    else:
        print_info("Puedes instalar más tarde con: python instalar.py \"RUTA\"")
    
    return True


def main():
    """Función principal."""
    
    # Procesar argumentos
    args = sys.argv[1:]
    
    # --help
    if "--help" in args or "-h" in args:
        print_banner()
        print_help()
        sys.exit(0)
    
    # --upgrade-all
    if "--upgrade-all" in args:
        success = do_update(upgrade_all=True)
        sys.exit(0 if success else 1)
    
    # --update
    if "--update" in args:
        success = do_update(upgrade_all=False)
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
    
    # Ejecutar configuración ANTES de instalar (para obtener ruta de artifacts)
    settings = ask_for_configuration(dest_path)
    artifacts_rel = settings["artifacts_rel"] if settings else "artifacts"

    # Ejecutar instalación
    success = install_sac(dest_path, root_dir, artifacts_rel)
    
    if success:
        print_final_summary(dest_path, artifacts_rel)
        # Escribir CONFIG_USER.yaml si el usuario configuró
        if settings:
            write_user_config(dest_path, settings)
    else:
        print_error("La instalación falló")
        sys.exit(1)


if __name__ == "__main__":
    main()