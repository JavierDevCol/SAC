# Reglas de Detección Automática de Stack

```yaml
descripcion: "Identificación rápida del ecosistema tecnológico de un proyecto"

# =============================================================================
# ECOSISTEMAS POR ARCHIVO FIRMA
# =============================================================================
ecosistemas:
  java:
    marcadores: ["pom.xml", "build.gradle", "build.gradle.kts"]
    extensiones: [".java"]
    reglas: "java.rules.md"
  
  javascript:
    marcadores: ["package.json"]
    extensiones: [".js", ".jsx", ".mjs"]
    reglas: "javascript.rules.md"
  
  typescript:
    marcadores: ["tsconfig.json", "package.json"]
    extensiones: [".ts", ".tsx"]
    reglas: "javascript.rules.md"
  
  python:
    marcadores: ["pyproject.toml", "requirements.txt", "Pipfile"]
    extensiones: [".py"]
    reglas: "python.rules.md"
  
  dotnet:
    marcadores: ["*.csproj", "*.sln"]
    extensiones: [".cs"]
    reglas: "dotnet.rules.md"
  
  go:
    marcadores: ["go.mod"]
    extensiones: [".go"]
    reglas: "go.rules.md"
  
  php:
    marcadores: ["composer.json"]
    extensiones: [".php"]
  
  ruby:
    marcadores: ["Gemfile"]
    extensiones: [".rb"]

# =============================================================================
# TIPO DE PROYECTO
# =============================================================================
tipo_proyecto:
  frontend: 
    indicadores: ["index.html", "public/", "static/", "React/Vue/Angular/Svelte"]
  backend: 
    indicadores: ["routes/", "controllers/", "Dockerfile", "framework backend"]
  fullstack: 
    indicadores: ["next", "nuxt", "sveltekit", "remix", "rails", "django"]
  api: 
    indicadores: ["openapi.yaml", "swagger.json", "*.graphql", "*.proto"]
  cli: 
    indicadores: ["cmd/", "sin servidor HTTP", "cobra/commander/click/clap"]
  library: 
    indicadores: ["sin entry point", "múltiples exports"]
  monorepo: 
    indicadores: ["pnpm-workspace.yaml", "turbo.json", "nx.json", "lerna.json"]

# =============================================================================
# INFRAESTRUCTURA
# =============================================================================
infraestructura:
  contenedores: ["Dockerfile", "docker-compose.yml", "Containerfile"]
  kubernetes: ["k8s/", "Chart.yaml", "kustomization.yaml"]
  iac: ["*.tf", "Pulumi.yaml", "cdk.json", "ansible.cfg"]
  ci_cd:
    github: ".github/workflows/*.yml"
    gitlab: ".gitlab-ci.yml"
    azure: "azure-pipelines.yml"
    jenkins: "Jenkinsfile"

# =============================================================================
# ALGORITMO
# =============================================================================
deteccion:
  pasos:
    1: "Buscar archivos marcadores en raíz"
    2: "Identificar ecosistema por marcador"
    3: "Si múltiples → contar extensiones para determinar principal"
    4: "Cargar reglas específicas del ecosistema"
    5: "Detectar tipo de proyecto e infraestructura"
  
  ambiguedad:
    - "tsconfig.json + package.json → TypeScript"
    - "build.gradle.kts + *.kt → Kotlin"
    - "Múltiples marcadores en subcarpetas → Multi-proyecto"

# =============================================================================
# OUTPUT
# =============================================================================
output:
  formato: |
    **Ecosistema:** [nombre]
    **Framework:** [nombre] [version]
    **Tipo:** [frontend|backend|fullstack|api|cli|library]
    **Infra:** [docker|k8s|ci_cd]
```
