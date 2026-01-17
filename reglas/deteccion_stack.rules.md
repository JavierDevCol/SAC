Seguir estrictamente la confdiguracion yml
```yaml
descripcion: "Algoritmo ejecutable para identificar el ecosistema tecnológico de un proyecto"
version: "2.0.0"
fecha_actualizacion: "2026-01-16"

# =============================================================================
# ECOSISTEMAS POR ARCHIVO FIRMA
# =============================================================================
ecosistemas:
  java:
    marcadores: 
      - archivo: "pom.xml"
        peso: 10
        version_en: "//project/version | //project/parent/version"  # XPath
      - archivo: "build.gradle"
        peso: 10
        version_en: "sourceCompatibility|targetCompatibility"
      - archivo: "build.gradle.kts"
        peso: 10
        version_en: "jvmToolchain|JavaVersion"
    extensiones: [".java"]
    lockfiles: ["pom.xml.lock", "gradle.lockfile"]
    reglas: "java.rules.md"
  
  kotlin:
    marcadores:
      - archivo: "build.gradle.kts"
        peso: 12  # Mayor peso que Java si hay .kt
        version_en: "kotlin(\"jvm\") version"
      - archivo: "settings.gradle.kts"
        peso: 8
    extensiones: [".kt", ".kts"]
    reglas: "java.rules.md"  # Comparte ecosistema JVM
  
  javascript:
    marcadores:
      - archivo: "package.json"
        peso: 8
        version_en: "$.engines.node"  # JSONPath
    extensiones: [".js", ".jsx", ".mjs", ".cjs"]
    lockfiles: ["package-lock.json", "yarn.lock", "pnpm-lock.yaml", "bun.lockb"]
    reglas: "javascript.rules.md"
  
  typescript:
    marcadores:
      - archivo: "tsconfig.json"
        peso: 12  # Mayor peso que JS puro
        version_en: "$.compilerOptions.target"
      - archivo: "package.json"
        peso: 5
        condicion: "dependencies|devDependencies contiene 'typescript'"
    extensiones: [".ts", ".tsx", ".mts", ".cts"]
    lockfiles: ["package-lock.json", "yarn.lock", "pnpm-lock.yaml", "bun.lockb"]
    reglas: "javascript.rules.md"
  
  python:
    marcadores:
      - archivo: "pyproject.toml"
        peso: 10
        version_en: "[tool.poetry.dependencies.python] | [project.requires-python]"
      - archivo: "requirements.txt"
        peso: 6
        version_en: null  # No contiene versión de Python
      - archivo: "Pipfile"
        peso: 8
        version_en: "[requires.python_version]"
      - archivo: "setup.py"
        peso: 5
        version_en: "python_requires"
    extensiones: [".py", ".pyi"]
    lockfiles: ["poetry.lock", "Pipfile.lock", "requirements.lock"]
    reglas: "python.rules.md"
  
  rust:
    marcadores:
      - archivo: "Cargo.toml"
        peso: 10
        version_en: "[package.rust-version] | [package.edition]"
    extensiones: [".rs"]
    lockfiles: ["Cargo.lock"]
    reglas: null  # TODO: crear rust.rules.md
  
  go:
    marcadores:
      - archivo: "go.mod"
        peso: 10
        version_en: "^go \\d+\\.\\d+"  # Regex en primera línea
    extensiones: [".go"]
    lockfiles: ["go.sum"]
    reglas: "go.rules.md"
  
  dotnet:
    marcadores:
      - archivo: "*.csproj"
        peso: 10
        version_en: "//TargetFramework"  # XPath
      - archivo: "*.fsproj"
        peso: 10
      - archivo: "*.sln"
        peso: 8
      - archivo: "global.json"
        peso: 6
        version_en: "$.sdk.version"
    extensiones: [".cs", ".fs", ".vb"]
    reglas: "dotnet.rules.md"
  
  php:
    marcadores:
      - archivo: "composer.json"
        peso: 10
        version_en: "$.require.php"
    extensiones: [".php"]
    lockfiles: ["composer.lock"]
  
  ruby:
    marcadores:
      - archivo: "Gemfile"
        peso: 10
        version_en: "ruby '[version]'"
      - archivo: ".ruby-version"
        peso: 8
        version_en: "contenido completo del archivo"
    extensiones: [".rb", ".rake"]
    lockfiles: ["Gemfile.lock"]
  
  cpp:
    marcadores:
      - archivo: "CMakeLists.txt"
        peso: 10
        version_en: "CMAKE_CXX_STANDARD"
      - archivo: "Makefile"
        peso: 6
      - archivo: "*.vcxproj"
        peso: 8
      - archivo: "conanfile.txt"
        peso: 7
    extensiones: [".cpp", ".cc", ".cxx", ".hpp", ".h", ".c"]
    lockfiles: ["conan.lock"]
  
  elixir:
    marcadores:
      - archivo: "mix.exs"
        peso: 10
        version_en: "elixir: \"~> X.X\""
    extensiones: [".ex", ".exs"]
    lockfiles: ["mix.lock"]

# =============================================================================
# TIPO DE PROYECTO
# =============================================================================
tipo_proyecto:
  frontend:
    marcadores:
      - archivo: "vite.config.*"
        framework: "vite"
      - archivo: "next.config.*"
        framework: "nextjs"
        tipo_override: "fullstack"
      - archivo: "nuxt.config.*"
        framework: "nuxt"
        tipo_override: "fullstack"
      - archivo: "svelte.config.*"
        framework: "sveltekit"
      - archivo: "angular.json"
        framework: "angular"
      - archivo: "astro.config.*"
        framework: "astro"
    indicadores_carpeta: ["src/components/", "src/pages/", "public/", "static/"]
    indicadores_dependencia:
      - nombre: "react"
        framework: "react"
      - nombre: "vue"
        framework: "vue"
      - nombre: "@angular/core"
        framework: "angular"
      - nombre: "svelte"
        framework: "svelte"
  
  backend:
    marcadores:
      - archivo: "main.go"
        condicion: "contiene http.ListenAndServe|gin|echo|fiber"
      - archivo: "manage.py"
        framework: "django"
      - archivo: "app.py"
        framework: "flask|fastapi"
    indicadores_carpeta: ["routes/", "controllers/", "handlers/", "api/"]
    indicadores_dependencia:
      - nombre: "express"
        framework: "express"
      - nombre: "fastify"
        framework: "fastify"
      - nombre: "@nestjs/core"
        framework: "nestjs"
      - nombre: "fastapi"
        framework: "fastapi"
      - nombre: "django"
        framework: "django"
      - nombre: "flask"
        framework: "flask"
      - nombre: "gin-gonic/gin"
        framework: "gin"
      - nombre: "spring-boot"
        framework: "spring-boot"
  
  api:
    marcadores:
      - archivo: "openapi.yaml"
      - archivo: "openapi.json"
      - archivo: "swagger.json"
      - archivo: "*.graphql"
      - archivo: "schema.graphql"
      - archivo: "*.proto"
  
  cli:
    indicadores_dependencia:
      - nombre: "commander"
        ecosistema: "javascript"
      - nombre: "yargs"
        ecosistema: "javascript"
      - nombre: "click"
        ecosistema: "python"
      - nombre: "typer"
        ecosistema: "python"
      - nombre: "cobra"
        ecosistema: "go"
      - nombre: "clap"
        ecosistema: "rust"
    indicadores_carpeta: ["cmd/"]
  
  library:
    indicadores:
      - "package.json sin 'main' ni 'bin' pero con 'exports'"
      - "setup.py con solo 'packages'"
      - "Cargo.toml con [lib] sin [[bin]]"
  
  monorepo:
    marcadores:
      - archivo: "pnpm-workspace.yaml"
        tipo: "pnpm"
      - archivo: "turbo.json"
        tipo: "turborepo"
      - archivo: "nx.json"
        tipo: "nx"
      - archivo: "lerna.json"
        tipo: "lerna"
      - archivo: "rush.json"
        tipo: "rush"

# =============================================================================
# INFRAESTRUCTURA
# =============================================================================
infraestructura:
  contenedores:
    marcadores: ["Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml", "Containerfile"]
    version_en: "FROM imagen:VERSION"
  
  kubernetes:
    marcadores: ["Chart.yaml", "kustomization.yaml", "skaffold.yaml"]
    indicadores_carpeta: ["k8s/", "kubernetes/", "helm/", "charts/"]
  
  iac:
    terraform:
      marcadores: ["*.tf", "terraform.tfvars"]
      version_en: "required_version"
    pulumi:
      marcadores: ["Pulumi.yaml"]
    cdk:
      marcadores: ["cdk.json"]
    ansible:
      marcadores: ["ansible.cfg", "playbook.yml"]
      indicadores_carpeta: ["roles/", "playbooks/"]
  
  ci_cd:
    github_actions:
      marcadores: [".github/workflows/*.yml", ".github/workflows/*.yaml"]
    gitlab_ci:
      marcadores: [".gitlab-ci.yml"]
    azure_devops:
      marcadores: ["azure-pipelines.yml"]
    jenkins:
      marcadores: ["Jenkinsfile"]
    circleci:
      marcadores: [".circleci/config.yml"]
    travis:
      marcadores: [".travis.yml"]

# =============================================================================
# proceso DE DETECCIÓN (EJECUTABLE)
# =============================================================================
proceso:
  descripcion: "Secuencia de pasos que el agente DEBE ejecutar en orden"
  
  paso_1:
    nombre: "Detectar Monorepo"
    herramienta: "file_search"
    query: "**/pnpm-workspace.yaml,**/turbo.json,**/nx.json,**/lerna.json,**/rush.json"
    accion: |
      SI encuentra alguno:
        - Marcar proyecto como MONOREPO
        - Identificar carpetas de proyectos (packages/, apps/, libs/)
        - PARA CADA subcarpeta: ejecutar paso_2 a paso_6 recursivamente
        - Agregar resultados como array de stacks
      SI NO:
        - Continuar con paso_2
  
  paso_2:
    nombre: "Buscar Marcadores de Ecosistema"
    herramienta: "file_search"
    query: |
      **/{pom.xml,build.gradle,build.gradle.kts,package.json,tsconfig.json,
      pyproject.toml,requirements.txt,Pipfile,Cargo.toml,go.mod,*.csproj,
      *.sln,composer.json,Gemfile,CMakeLists.txt,mix.exs}
    accion: |
      PARA CADA marcador encontrado:
        - Obtener profundidad (0 = raíz, 1 = subcarpeta, etc.)
        - Calcular peso_ajustado = peso_base - (profundidad * 2)
        - Agregar a lista_marcadores[]
  
  paso_3:
    nombre: "Calcular Score por Ecosistema"
    herramienta: null  # Procesamiento interno
    accion: |
      PARA CADA ecosistema en lista_marcadores:
        - Sumar todos los peso_ajustado de sus marcadores
        - SI existe lockfile del ecosistema: score += 3
        - Guardar en ranking[ecosistema] = score_total
  
  paso_4:
    nombre: "Desambiguar por Extensiones (si empate)"
    herramienta: "file_search"
    condicion: "SI dos o más ecosistemas tienen score dentro de ±2 puntos"
    accion: |
      PARA CADA ecosistema empatado:
        - Contar archivos con extensiones del ecosistema
        - Agregar 0.1 puntos por archivo (máximo +5 puntos)
      Reordenar ranking
  
  paso_5:
    nombre: "Extraer Versiones"
    herramienta: "read_file"
    accion: |
      PARA el ecosistema ganador (y secundarios si score > threshold):
        - Leer archivo marcador principal
        - Extraer versión usando el campo 'version_en' definido arriba
        - SI version_en es XPath: parsear XML
        - SI version_en es JSONPath: parsear JSON
        - SI version_en es Regex: aplicar regex
        - SI version_en es null: reportar "version: no especificada"
  
  paso_6:
    nombre: "Detectar Tipo de Proyecto"
    herramienta: "file_search + read_file"
    accion: |
      1. Buscar marcadores de tipo_proyecto (vite.config.*, next.config.*, etc.)
      2. SI encuentra framework con tipo_override: usar ese tipo
      3. SI NO: buscar indicadores_carpeta
      4. SI encuentra routes/|controllers/|handlers/: tipo = "backend"
      5. SI encuentra components/|pages/: tipo = "frontend"
      6. SI encuentra ambos: tipo = "fullstack"
      7. Leer package.json/pyproject.toml para detectar framework por dependencia
  
  paso_7:
    nombre: "Detectar Infraestructura"
    herramienta: "file_search"
    accion: |
      Buscar en paralelo:
        - Dockerfile|compose.yml → infra.contenedores = true
        - Chart.yaml|k8s/ → infra.kubernetes = true
        - *.tf|Pulumi.yaml → infra.iac = [tipo]
        - .github/workflows/*.yml → infra.ci_cd = "github_actions"
  
  paso_8:
    nombre: "Calcular Confianza y Generar Output"
    herramienta: null
    accion: |
      confidence = score_ganador / (score_ganador + score_segundo + 1)
      
      SI confidence < config.confidence_threshold:
        - Agregar warning: "Detección ambigua, múltiples stacks posibles"
        - Listar top 3 ecosistemas con sus scores
      
      RETURN output estructurado

# =============================================================================
# REGLAS DE DESAMBIGUACIÓN
# =============================================================================
desambiguacion:
  reglas_explicitas:
    - condicion: "tsconfig.json + package.json"
      resultado: "TypeScript (no JavaScript)"
      razon: "tsconfig.json indica proyecto TypeScript explícitamente"
    
    - condicion: "build.gradle.kts + archivos .kt"
      resultado: "Kotlin (no Java)"
      razon: "Extensión .kt tiene prioridad sobre .java en proyectos Gradle Kotlin DSL"
    
    - condicion: "package.json + go.mod en raíz"
      resultado: "Multi-stack (frontend JS + backend Go)"
      razon: "Combinación común, reportar ambos"
    
    - condicion: "Dockerfile sin otros marcadores"
      resultado: "stack_desconocido"
      razon: "Dockerfile solo indica containerización, no lenguaje"
    
    - condicion: "Solo archivos .h y .c"
      resultado: "C (no C++)"
      razon: "Ausencia de .cpp/.cc indica C puro"

# =============================================================================
# FALLBACKS Y ERRORES
# =============================================================================
fallback:
  sin_marcadores:
    accion: |
      1. Buscar cualquier archivo de código fuente
      2. Contar por extensión
      3. SI encuentra archivos:
         - Reportar ecosistema con más archivos
         - Agregar warning: "Detección por extensión únicamente, sin archivo de proyecto"
      4. SI NO encuentra archivos de código:
         - Reportar: "stack_desconocido"
         - Sugerir: "Proyecto vacío o no es un proyecto de software"
  
  error_lectura:
    accion: |
      SI falla read_file en un marcador:
        - Continuar con siguiente marcador
        - Agregar warning: "No se pudo leer [archivo]"
        - Reducir confidence en 0.1

# =============================================================================
# OUTPUT ESTRUCTURADO
# =============================================================================
output:
  formato_yaml: |
    stack:
      ecosistema_principal: "[nombre]"
      version: "[X.X.X | no especificada]"
      ecosistemas_secundarios:  # Solo si confidence > 0.3
        - nombre: "[nombre]"
          version: "[X.X.X]"
          ubicacion: "[path relativo]"
      
      framework:
        nombre: "[nombre | null]"
        version: "[X.X.X | null]"
      
      tipo: "[frontend|backend|fullstack|api|cli|library|monorepo]"
      
      infraestructura:
        contenedores: [true|false]
        kubernetes: [true|false]
        ci_cd: "[github_actions|gitlab_ci|azure_devops|jenkins|null]"
        iac: "[terraform|pulumi|cdk|ansible|null]"
      
      metadata:
        confidence: [0.0-1.0]
        warnings: []
        reglas_aplicar: ["[ecosistema].rules.md"]
        detectado_en: "[timestamp ISO]"
  
  formato_legible: |
    ## 🔍 Stack Detectado
    
    | Campo | Valor |
    |-------|-------|
    | **Ecosistema** | [nombre] [version] |
    | **Framework** | [nombre] [version] |
    | **Tipo** | [tipo] |
    | **Confianza** | [X]% |
    
    ### Infraestructura
    - 🐳 Contenedores: [Sí/No]
    - ☸️ Kubernetes: [Sí/No]
    - 🔄 CI/CD: [proveedor]
    
    ### ⚠️ Advertencias
    [lista de warnings si existen]
```
