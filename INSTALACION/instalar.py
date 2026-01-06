#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║           INSTALADOR DE COCHAS v4.0                           ║
║   Sistema de Orquestación de Agentes IA para GitHub Copilot   ║
╚═══════════════════════════════════════════════════════════════╝

Este script instala el sistema COCHAS en cualquier proyecto.

Uso:
    python instalar.py                    # Modo interactivo
    python instalar.py "C:\mi\proyecto"   # Ruta como argumento
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime


# ============================================
# CONFIGURACIÓN
# ============================================

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


def install_cochas(dest_path):
    """Ejecuta la instalación de COCHAS."""
    dest = Path(dest_path)
    root_dir = get_root_directory()
    script_dir = get_script_directory()
    
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
    github_source = script_dir / GITHUB_AGENTS_SOURCE
    
    if github_source.exists():
        for agent_file in github_source.glob("*.agent.md"):
            try:
                shutil.copy2(agent_file, github_dest / agent_file.name)
                print_success(f".github/agents/{agent_file.name}")
            except Exception as e:
                print_error(f"{agent_file.name} - Error: {e}")
                return False
    else:
        print_error(f"No se encontró la carpeta de agentes: {github_source}")
        return False
    
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


def main():
    """Función principal."""
    print_banner()
    
    # Obtener directorios
    root_dir = get_root_directory()
    script_dir = get_script_directory()
    
    # Validar carpetas fuente
    missing = validate_source_folders(root_dir)
    if missing:
        print_error(f"Faltan carpetas fuente: {', '.join(missing)}")
        print_info(f"Directorio raíz esperado: {root_dir}")
        sys.exit(1)
    
    # Obtener ruta destino
    if len(sys.argv) > 1:
        dest_path = sys.argv[1]
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
    
    print(f"\n📍 Destino: {dest_path}\n")
    
    # Verificar instalación existente
    existing = check_existing_installation(dest_path)
    if existing:
        print_warning(f"Ya existe una instalación: {', '.join(existing)}")
        response = input("\n   ¿Sobrescribir? (s/N): ").strip().lower()
        if response != 's':
            print_info("Instalación cancelada")
            sys.exit(0)
    
    # Ejecutar instalación
    success = install_cochas(dest_path)
    
    if success:
        print_final_summary(dest_path)
    else:
        print_error("La instalación falló")
        sys.exit(1)


if __name__ == "__main__":
    main()