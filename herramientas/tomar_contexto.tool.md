```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Actualizar session_state.json al finalizar"
    nunca_saltar: true
  - instruccion: "Detectar si es proyecto único o multi-proyecto ANTES de analizar"
    nunca_saltar: true
  - instruccion: "En multi-proyecto, generar workspace.md + contextos individuales"
    nunca_saltar: true
  - instruccion: "NUNCA mezclar contextos de diferentes proyectos en un solo archivo"
    nunca_saltar: true

identificacion:
  nombre: "Tomar Contexto"
  comando: ">tomar_contexto"
  alias: [">contexto", ">tc"]
  version: "4.0"

roles_autorizados:
  - ONAD
  - ARCHDEV
  - DEVOPS
  - REFINADOR

prerequisitos:
  archivos_requeridos:
    - descripcion: "Acceso a la raíz del proyecto"
      validacion: "Permisos de lectura en directorios"
  archivos_opcionales:
    - "README.md"
    - "pom.xml | build.gradle | package.json"
    - "Dockerfile | docker-compose.yml"
    - ".github/workflows/ | .gitlab-ci.yml"

parametros:
  opcionales:
    - nombre: profundidad_analisis
      tipo: string
      valores: [basico, completo, exhaustivo]
      defecto: completo
    - nombre: incluir_dependencias
      tipo: boolean
      defecto: true
    - nombre: generar_readme
      tipo: string
      valores: [auto, siempre, nunca]
      defecto: auto
    - nombre: incluir_devops
      tipo: boolean
      defecto: true
    - nombre: detectar_patrones
      tipo: boolean
      defecto: true
    - nombre: nombre_proyecto
      tipo: string
      descripcion: "Nombre del proyecto específico a analizar (en multi-proyecto)"
      defecto: null
    - nombre: all
      tipo: flag
      descripcion: "Analizar todos los proyectos del workspace"
      defecto: false
    - nombre: force
      tipo: flag
      descripcion: "Forzar regeneración aunque exista contexto"
      defecto: false

deteccion_workspace:
  marcadores_proyecto:
    java: ["pom.xml", "build.gradle", "build.gradle.kts"]
    javascript: ["package.json"]
    python: ["pyproject.toml", "setup.py", "requirements.txt"]
    dotnet: ["*.csproj", "*.sln"]
    rust: ["Cargo.toml"]
    go: ["go.mod"]
  
  logica_deteccion:
    - "Buscar marcadores en carpeta actual"
    - "Si encuentra 1 marcador en raíz → Proyecto Único"
    - "Si encuentra 0 marcadores en raíz → Buscar en subcarpetas"
    - "Si encuentra 2+ subcarpetas con marcadores → Multi-Proyecto"

proceso_proyecto_unico:
  paso_1:
    nombre: "Detectar Stack Tecnológico"
    obligatorio: true
    acciones:
      - "Identificar lenguaje principal"
      - "Detectar framework y versión"
      - "Listar dependencias principales"

  paso_2:
    nombre: "Analizar Arquitectura"
    obligatorio: true
    acciones:
      - "Identificar estilo arquitectónico"
      - "Mapear estructura de carpetas"
      - "Detectar componentes principales"

  paso_3:
    nombre: "Evaluar DevOps"
    obligatorio: true
    acciones:
      - "Buscar Dockerfile, docker-compose"
      - "Detectar CI/CD (GitHub Actions, GitLab CI, etc.)"
      - "Identificar IaC si existe"

  paso_4:
    nombre: "Generar Scorecard"
    obligatorio: true
    acciones:
      - "Evaluar cada aspecto (1-10)"
      - "Identificar puntos de atención"

  paso_5:
    nombre: "Crear Archivo de Contexto"
    obligatorio: true
    acciones:
      - "Usar plantilla: contexto_proyecto_plantilla.md"
      - "Guardar en: {{artifacts_folder}}/contexto_proyecto.md"

proceso_multi_proyecto:
  paso_1:
    nombre: "Detectar Proyectos"
    obligatorio: true
    acciones:
      - "Escanear subcarpetas buscando marcadores"
      - "Listar proyectos encontrados con su stack"
      - "Mostrar lista al usuario"
    output: |
      📁 Workspace Multi-Proyecto Detectado
      
      Proyectos encontrados:
      | # | Proyecto | Stack | Ruta |
      |---|----------|-------|------|
      | 1 | [nombre] | [stack] | ./[ruta] |
      | 2 | [nombre] | [stack] | ./[ruta] |

  paso_2:
    nombre: "Solicitar Selección o Confirmar --all"
    obligatorio: true
    condicion: "si NO se pasó parámetro"
    acciones:
      - "Preguntar: ¿Analizar proyecto específico o todos?"
      - "Opciones: [número], --all, cancelar"

  paso_3:
    nombre: "Crear Estructura de Carpetas"
    obligatorio: true
    acciones:
      - "Crear {{artifacts_folder}}/contextos/ si no existe"
      - "Crear {{hu_folder}}/compartidas/ si no existe"
      - "Crear {{hu_folder}}/[nombre_proyecto]/ por cada proyecto"

  paso_4:
    nombre: "Analizar Proyecto(s) Seleccionado(s)"
    obligatorio: true
    acciones:
      - "Para cada proyecto seleccionado:"
      - "  - Ejecutar proceso_proyecto_unico pasos 1-4"
      - "  - Guardar en: {{contextos_folder}}/contexto_proyecto_[nombre].md"

  paso_5:
    nombre: "Detectar Relaciones entre Proyectos"
    obligatorio: true
    condicion: "si --all o múltiples proyectos"
    acciones:
      - "Buscar referencias cruzadas en código"
      - "Detectar dependencias compartidas"
      - "Identificar integraciones (APIs, BD compartida, etc.)"

  paso_6:
    nombre: "Generar workspace.md"
    obligatorio: true
    condicion: "si es multi-proyecto"
    acciones:
      - "Usar plantilla: workspace_plantilla.md"
      - "Incluir tabla de proyectos"
      - "Incluir relaciones detectadas"
      - "Guardar en: {{artifacts_folder}}/workspace.md"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Abrir/crear {{session_state_location}}"
      - "Registrar herramienta ejecutada: tomar_contexto"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Si hay HU activa, actualizar su estado"
      - "Guardar cambios en session_state.json"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "tomar_contexto"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"

salida_proyecto_unico:
  archivos_generados:
    - tipo: "contexto"
      ruta: "{{artifacts_folder}}/contexto_proyecto.md"
  
  mensaje_exito: |
    ✅ CONTEXTO GENERADO
    
    📄 Archivo: .cochas/artifacts/contexto_proyecto.md
    📊 Confianza: [Alto|Medio|Bajo]
    
    🎯 Scorecard:
    | Aspecto | Puntuación |
    |---------|------------|
    | Arquitectura | [X]/10 |
    | Stack | [X]/10 |
    | Testing | [X]/10 |
    | DevOps | [X]/10 |

salida_multi_proyecto:
  archivos_generados:
    - tipo: "workspace"
      ruta: "{{artifacts_folder}}/workspace.md"
    - tipo: "contextos"
      ruta: "{{contextos_folder}}/contexto_proyecto_[nombre].md"
  
  carpetas_creadas:
    - "{{contextos_folder}}"
    - "{{hu_folder}}/compartidas"
    - "{{hu_folder}}/[nombre_proyecto]"
  
  mensaje_exito: |
    ✅ WORKSPACE MULTI-PROYECTO CONFIGURADO
    
    📁 Estructura creada:
    .cochas/artifacts/
    ├── workspace.md
    ├── contextos/
    │   ├── contexto_proyecto_[proyecto_1].md
    │   └── contexto_proyecto_[proyecto_2].md
    └── HU/
        ├── compartidas/
        ├── [proyecto_1]/
        └── [proyecto_2]/
    
    📊 Proyectos analizados: [N]
    
    💡 Comandos disponibles:
    - *HU --compartidas
    - *HU --proyecto=[nombre]
    - >tomar_contexto [nombre] (actualizar uno)

errores:
  sin_permisos:
    mensaje: "❌ Sin permisos de lectura en el directorio"
    accion: "Solicitar acceso o cambiar directorio"
  proyecto_vacio:
    mensaje: "⚠️ Proyecto sin archivos de código detectables"
    accion: "Generar contexto básico y sugerir inicialización"
  multiple_gestores:
    mensaje: "ℹ️ Detectados múltiples gestores de dependencias"
    accion: "Analizar ambos, marcar como proyecto polyglot"
  sin_marcadores:
    mensaje: "❌ No se detectó ningún proyecto en esta ubicación"
    accion: "Verificar que estás en la carpeta correcta"
  proyecto_no_encontrado:
    mensaje: "❌ Proyecto '[nombre]' no encontrado en el workspace"
    accion: "Ejecutar >tomar_contexto sin parámetros para ver proyectos disponibles"
  workspace_existente:
    mensaje: "ℹ️ Ya existe contexto para este workspace"
    accion: "Usar --force para regenerar"

siguiente:
  proyecto_unico:
    - comando: "*HU"
      descripcion: "Ver historias de usuario"
    - comando: ">refinar_hu [ID]"
      descripcion: "Refinar una historia de usuario"
  multi_proyecto:
    - comando: "*HU --compartidas"
      descripcion: "Ver HUs que afectan múltiples proyectos"
    - comando: ">tomar_contexto [proyecto]"
      descripcion: "Actualizar contexto de un proyecto específico"
```
