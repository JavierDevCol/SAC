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
REPO_BRANCH = "feature/instalacion"  # Rama principal para instalación

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
    Obtiene la ruta donde se clonará/almacenará el repositorio.
    Usa ubicaciones permanentes según el sistema operativo:
    - Windows: %LOCALAPPDATA%/cochas/repo/
    - Linux/Mac: ~/.local/share/cochas/repo/
    """
    if platform.system() == "Windows":
        # Usar %LOCALAPPDATA% (ej: C:\Users\Usuario\AppData\Local)
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            base_path = Path(local_app_data) / "cochas" / "repo"
        else:
            # Fallback si no existe la variable
            base_path = Path.home() / "AppData" / "Local" / "cochas" / "repo"
    else:
        # Linux/Mac: ~/.local/share/cochas/repo/
        base_path = Path.home() / ".local" / "share" / "cochas" / "repo"
    
    return base_path


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

    # 2.1 Reemplazar {project-root} en la configuración instalada
    config_system_path = cochas_dest / "config" / "CONFIG_SYSTEM.yaml"
    replace_project_root_placeholder(config_system_path, dest)
    
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


def configure_user_settings(dest_path):
    """
    Solicita configuración personalizada al usuario y genera CONFIG_USER.yaml.
    Retorna True si se completó correctamente, False si se omitió.
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
    
    # === GENERAR ARCHIVO CONFIG_USER.yaml ===
    config_content = f"""# ============================================
# CONFIGURACIÓN DEL USUARIO/PROYECTO
# ============================================
# ✅ Editable por el usuario
# Generado automáticamente por el instalador de COCHAS
# Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# ============================================

# === INFORMACIÓN DEL USUARIO ===
usuario:
  nombre: "{nombre_usuario}"                  # Tu nombre para personalización

# === PREFERENCIAS DE IDIOMA ===
idiomas:
  documentacion: "{idioma_doc}"                 # Idioma para documentos generados (es|en|pt)
  comunicacion: "{idioma_com}"                  # Idioma para interacción con el sistema

# === INFORMACIÓN DEL PROYECTO ===
proyecto:
  nombre: "{nombre_proyecto}"                          # Nombre del proyecto
"""
    
    # Guardar archivo
    config_path = Path(dest_path) / ".cochas" / "config" / "CONFIG_USER.yaml"
    
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            f.write(config_content)
        print_success(f"Configuración guardada en: .cochas/config/CONFIG_USER.yaml")
        return True
    except Exception as e:
        print_error(f"Error al guardar configuración: {e}")
        return False


def ask_for_configuration(dest_path):
    """
    Pregunta al usuario si desea configurar COCHAS ahora.
    Retorna True si se configuró o se omitió correctamente.
    """
    print("\n" + "─" * 55)
    print("\n   ¿Deseas configurar COCHAS para tu proyecto ahora?")
    print("   (Puedes hacerlo después editando .cochas/config/CONFIG_USER.yaml)\n")
    
    response = input("   Configurar ahora (S/n): ").strip().lower()
    
    if response == 'n':
        print_info("Configuración omitida. Puedes editar CONFIG_USER.yaml más tarde.")
        return True
    
    return configure_user_settings(dest_path)


def print_help():
    """Muestra la ayuda del comando."""
    print("""
📖 USO:
    python instalar.py [RUTA]              Instala COCHAS en la ruta especificada
    python instalar.py                     Modo interactivo (pide la ruta)
    python instalar.py --update            Actualiza el repositorio en caché
    python instalar.py --help              Muestra este mensaje de ayuda

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
    - Windows: %LOCALAPPDATA%\\cochas\\repo\\
    - Linux/Mac: ~/.local/share/cochas/repo/
""".format(repo_url=REPO_URL))


def do_update():
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
        
        # Ejecutar instalación
        install_success = install_cochas(dest_path, temp_repo_path)
        
        if install_success:
            print_final_summary(dest_path)
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
        ask_for_configuration(dest_path)
    else:
        print_error("La instalación falló")
        sys.exit(1)


if __name__ == "__main__":
    main()