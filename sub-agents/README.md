# Sub-Agents Generator

Sistema para generar sub-agentes compatibles con **Claude Code** y **OpenCode** desde una fuente de verdad común.

## Estructura

```
sub-agents/
├── source/                     # Fuente de verdad (YAML)
│   ├── validador-calidad.yaml
│   └── validador-compilacion.yaml
├── generate.py                 # Script generador
├── output/                     # Generados automáticamente
│   ├── claude/                 # .md para Claude Code
│   │   ├── validador-calidad.md
│   │   └── validador-compilacion.md
│   └── opencode/               # .json para OpenCode
│       ├── opencode-agents.json
│       └── prompts/            # Prompts separados
│           ├── validador-calidad.md
│           └── validador-compilacion.md
└── README.md
```

## Uso

### Prerrequisitos

```bash
pip install pyyaml
```

### Generar sub-agentes

```bash
# Desde el directorio sub-agents/
python generate.py

# Especificar directorios personalizados
python generate.py --source ./mi-source --output ./mi-output

# Modo dry-run (sin escribir archivos)
python generate.py --dry-run
```

### Instalar sub-agentes

#### Claude Code

Copiar los archivos `.md` generados a `.claude/agents/`:

```bash
cp output/claude/*.md ~/.claude/agents/          # Global
cp output/claude/*.md .claude/agents/             # Proyecto
```

#### OpenCode

Copiar el archivo JSON y los prompts a la configuración de OpenCode:

```bash
# Copiar JSON y prompts al directorio del proyecto
cp output/opencode/opencode-agents.json .
cp -r output/opencode/prompts/ .
```

**Nota:** Los prompts se referencian con `{file:./prompts/nombre.md}`, por lo que deben estar en la misma ubicación que el JSON.

## Formato Fuente de Verdad (YAML)

Cada archivo YAML en `source/` define un sub-agente:

```yaml
name: mi-agente
description: "Descripción del agente"

model:
  claude: haiku              # sonnet, opus, haiku
  opencode: opencode/deepseek-v4-flash-free

color:
  claude: green              # Nombre para Claude Code
  opencode: "#4CAF50"        # Hex para OpenCode

tools:
  read: true
  search: true
  glob: true
  grep: true
  write: false
  edit: false
  bash: false
  webfetch: false

permissions:
  edit: deny
  bash: deny
  webfetch: deny
  task: deny

hidden: true
temperature: 0.1

prompt: |
  Instrucciones del agente en markdown...
```

## Mapeo de Campos

| Campo YAML | Claude Code | OpenCode |
|------------|-------------|----------|
| `name` | `name` (frontmatter) | Clave en `agent` |
| `description` | `description` (frontmatter) | `description` |
| `model.claude` | `model` | - |
| `model.opencode` | - | `model` |
| `color.claude` | `color` (nombre) | - |
| `color.opencode` | - | `color` (hex) |
| `tools` | `tools` (string CSV) | `tools` (objeto) |
| `permissions` | - | `permission` |
| `hidden` | - | `hidden` |
| `temperature` | - | `temperature` |
| `prompt` | Cuerpo del markdown | - |

## Agregar Nuevo Sub-Agente

1. Crear archivo YAML en `source/`:
   ```bash
   cp source/validador-calidad.yaml source/nuevo-agente.yaml
   ```

2. Editar el archivo con los datos del nuevo agente

3. Regenerar:
   ```bash
   python generate.py
   ```

4. Instalar en las plataformas deseadas

## Notas

- Los colores de Claude Code usan nombres (`green`, `orange`), no hex
- Los colores de OpenCode usan hex (`#4CAF50`)
- El campo `tools` en Claude Code es una cadena separada por comas
- El campo `tools` en OpenCode es un objeto con booleanos
- Los permisos (`permissions`) solo aplican para OpenCode