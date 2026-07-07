#!/usr/bin/env python3
"""
Generador de sub-agentes para Claude Code y OpenCode.

Lee archivos YAML de source/ y genera:
- output/claude/*.md (formato Claude Code)
- output/opencode/opencode-agents.json (formato OpenCode)

Uso:
    python generate.py [--source DIR] [--output DIR] [--dry-run]
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml


# Mapeo de colores Claude Code (hex -> nombre)
COLOR_MAP_CLAUDE = {
    "#4CAF50": "green",
    "#FF9800": "orange",
    "#F44336": "red",
    "#2196F3": "blue",
    "#FFEB3B": "yellow",
    "#9C27B0": "purple",
    "#E91E63": "pink",
    "#00BCD4": "cyan",
}

# Mapeo de colores OpenCode (nombre -> hex)
COLOR_MAP_OPENCODE = {v: k for k, v in COLOR_MAP_CLAUDE.items()}


def load_yaml_source(source_path: Path) -> dict[str, Any]:
    """Carga un archivo YAML y retorna su contenido."""
    with open(source_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def tools_to_claude_string(tools: dict[str, bool]) -> str:
    """Convierte diccionario de tools a string separado por comas para Claude Code."""
    # Mapeo de nombres internos a nombres Claude Code
    tool_map = {
        "read": "Read",
        "search": "Search",
        "glob": "Glob",
        "grep": "Grep",
        "write": "Write",
        "edit": "Edit",
        "bash": "Bash",
        "webfetch": "WebFetch",
    }
    enabled = []
    for tool, enabled_val in tools.items():
        if enabled_val and tool in tool_map:
            enabled.append(tool_map[tool])
    return ", ".join(enabled)


def tools_to_opencode(tools: dict[str, bool]) -> dict[str, bool]:
    """Convierte tools a formato OpenCode (mantiene formato original)."""
    return tools


def permissions_to_opencode(permissions: dict[str, Any]) -> dict[str, Any]:
    """Convierte permisos a formato OpenCode."""
    result = {}
    for key, value in permissions.items():
        if key == "task" and value == "deny":
            result["task"] = {"*": "deny"}
        else:
            result[key] = value
    return result


def generate_claude_md(agent: dict[str, Any]) -> str:
    """Genera contenido markdown con frontmatter para Claude Code."""
    name = agent["name"]
    description = agent["description"]
    model = agent.get("model", {}).get("claude", "haiku")
    color_hex = agent.get("color", {}).get("claude", "green")
    tools = agent.get("tools", {})
    prompt = agent.get("prompt", "")

    # Convertir color hex a nombre si es necesario
    color_name = COLOR_MAP_CLAUDE.get(color_hex, color_hex)

    # Generar string de tools
    tools_str = tools_to_claude_string(tools)

    # Construir frontmatter
    frontmatter_lines = [
        "---",
        f"name: {name}",
        f'description: "{description}"',
        f"tools: {tools_str}",
        f"model: {model}",
        f"color: {color_name}",
        "---",
    ]
    frontmatter = "\n".join(frontmatter_lines)

    # Construir contenido completo
    content = f"{frontmatter}\n\n{prompt.strip()}\n"
    return content


def generate_opencode_json(agents: list[dict[str, Any]], prompts_dir: Path) -> dict[str, Any]:
    """Genera estructura JSON para OpenCode con referencias a archivos de prompt."""
    opencode_agents = {}

    for agent in agents:
        name = agent["name"]
        description = agent["description"]
        model = agent.get("model", {}).get("opencode", "opencode/deepseek-v4-flash-free")
        color_hex = agent.get("color", {}).get("opencode", "#4CAF50")
        tools = agent.get("tools", {})
        permissions = agent.get("permissions", {})
        hidden = agent.get("hidden", True)
        temperature = agent.get("temperature", 0.1)
        prompt = agent.get("prompt", "")

        # Generar archivo de prompt separado
        prompt_file = prompts_dir / f"{name}.md"
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt.strip() + "\n")

        opencode_agents[name] = {
            "description": description,
            "mode": "subagent",
            "hidden": hidden,
            "model": model,
            "temperature": temperature,
            "color": color_hex,
            "tools": tools_to_opencode(tools),
            "permission": permissions_to_opencode(permissions),
            "prompt": "{file:./prompts/" + name + ".md}",
        }

    return {
        "$schema": "https://opencode.ai/config.json",
        "agent": opencode_agents,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Genera sub-agentes para Claude Code y OpenCode desde archivos YAML"
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("source"),
        help="Directorio con archivos YAML fuente (default: source/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Directorio de salida (default: output/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra lo que se generaría sin escribir archivos",
    )
    args = parser.parse_args()

    # Verificar directorio fuente
    if not args.source.exists():
        print(f"Error: Directorio fuente no existe: {args.source}")
        sys.exit(1)

    # Buscar archivos YAML
    yaml_files = list(args.source.glob("*.yaml")) + list(args.source.glob("*.yml"))
    if not yaml_files:
        print(f"Error: No se encontraron archivos YAML en {args.source}")
        sys.exit(1)

    print(f"Encontrados {len(yaml_files)} archivos YAML en {args.source}")

    # Cargar todos los agentes
    agents = []
    for yaml_file in sorted(yaml_files):
        try:
            agent = load_yaml_source(yaml_file)
            agents.append(agent)
            print(f"  Cargado: {yaml_file.name} -> {agent['name']}")
        except Exception as e:
            print(f"  Error cargando {yaml_file.name}: {e}")
            sys.exit(1)

    # Crear directorios de salida
    claude_dir = args.output / "claude"
    opencode_dir = args.output / "opencode"
    prompts_dir = opencode_dir / "prompts"

    if not args.dry_run:
        claude_dir.mkdir(parents=True, exist_ok=True)
        opencode_dir.mkdir(parents=True, exist_ok=True)
        prompts_dir.mkdir(parents=True, exist_ok=True)

    # Generar archivos Claude Code
    print(f"\nGenerando archivos Claude Code en {claude_dir}:")
    for agent in agents:
        name = agent["name"]
        output_file = claude_dir / f"{name}.md"
        content = generate_claude_md(agent)

        if args.dry_run:
            print(f"  [DRY-RUN] Se generaría: {output_file}")
            print(f"    Contenido (primeras 5 líneas):")
            for line in content.split("\n")[:5]:
                print(f"      {line}")
        else:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Generado: {output_file}")

    # Generar archivo OpenCode
    opencode_output = opencode_dir / "opencode-agents.json"
    opencode_json = generate_opencode_json(agents, prompts_dir)

    print(f"\nGenerando archivo OpenCode en {opencode_output}:")
    if args.dry_run:
        print(f"  [DRY-RUN] Se generaría: {opencode_output}")
        print(f"    Agentes: {list(opencode_json['agent'].keys())}")
        print(f"    Prompts se generarían en: {prompts_dir}")
    else:
        with open(opencode_output, "w", encoding="utf-8") as f:
            json.dump(opencode_json, f, indent=2, ensure_ascii=False)
        print(f"  Generado: {opencode_output}")
        print(f"  Prompts generados en: {prompts_dir}")

    # Resumen
    print(f"\nResumen:")
    print(f"  Agentes procesados: {len(agents)}")
    print(f"  Archivos Claude Code: {len(agents)} (.md)")
    print(f"  Archivos OpenCode: 1 (opencode-agents.json)")
    print(f"  Archivos prompts: {len(agents)} (.md)")

    if args.dry_run:
        print("\n[DRY-RUN] No se escribieron archivos.")


if __name__ == "__main__":
    main()