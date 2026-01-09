```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Detectar si es proyecto único o multi-proyecto ANTES de analizar"
    nunca_saltar: true
  - instruccion: "En multi-proyecto, generar workspace.md + contextos individuales"
    nunca_saltar: true
  - instruccion: "NUNCA mezclar contextos de diferentes proyectos en un solo archivo"
    nunca_saltar: true
  - instruccion: "Generar documentación en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Tomar Contexto"
  comando: ">tomar_contexto"
  alias: [">contexto", ">tc"]
  version: "4.0"

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
      - "Verificar si existe {{rutas.artifacts_folder}}"
      - "Si NO existe, crear estructura de carpetas"
      - "Leer plantilla desde {{plantillas.contexto}}"
      - "Rellenar plantilla con datos analizados del proyecto"
      - "Guardar resultado en {{archivos.contexto_proyecto}}"
    plantilla_referencia: "{{plantillas.contexto}}"

  paso_6:
    nombre: "Generar Stack del Proyecto"
    obligatorio: true
    descripcion: "Genera archivo con especificaciones técnicas del stack detectado"
    acciones:
      - "Leer plantilla desde {{plantillas.stack_proyecto}}"
      - "Rellenar con datos detectados en pasos anteriores:"
      - "  - Lenguajes y versiones (de archivos de configuración)"
      - "  - Frameworks principales (de dependencias)"
      - "  - Librerías relevantes (de dependencias)"
      - "  - Herramientas de build (de archivos de proyecto)"
      - "  - Frameworks de testing (de dependencias de test)"
      - "  - Comandos de ejecución (inferidos del build tool)"
      - "  - Patrones sugeridos (según framework detectado)"
      - "  - Convenciones del ecosistema (según lenguaje)"
      - "Guardar resultado en {{archivos.stack_proyecto}}"
    plantilla_referencia: "{{plantillas.stack_proyecto}}"
    nota: "Este archivo permite que los agentes se adapten al stack específico del proyecto"

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
      - "Crear {{rutas.artifacts_folder}} si no existe"
      - "Crear {{artifacts.contextos_folder}} si no existe"
      - "Crear {{artifacts.hu_compartidas}} si no existe"
      - "Crear {{artifacts.hu_folder}}/[nombre_proyecto]/ por cada proyecto"

  paso_4:
    nombre: "Analizar Proyecto(s) Seleccionado(s)"
    obligatorio: true
    acciones:
      - "Para cada proyecto seleccionado:"
      - "  - Ejecutar proceso_proyecto_unico pasos 1-4"
      - "  - Guardar contexto en: {{artifacts.contextos_folder}}/contexto_proyecto_[nombre].md"
      - "  - Guardar stack en: {{artifacts.contextos_folder}}/stack_proyecto_[nombre].md"

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
      - "Verificar si existe {{rutas.artifacts_folder}}"
      - "Si NO existe, crear estructura de carpetas"
      - "Leer plantilla desde {{plantillas.workspace}}"
      - "Rellenar plantilla con:"
      - "  - Tabla de proyectos detectados"
      - "  - Relaciones entre proyectos"
      - "  - Stack tecnológico de cada uno"
      - "Guardar resultado en {{archivos.workspace_index}}"
    plantilla_referencia: "{{plantillas.workspace}}"

salida_proyecto_unico:
  archivos_generados:
    - tipo: "contexto"
      ruta: "{{archivos.contexto_proyecto}}"
    - tipo: "stack"
      ruta: "{{archivos.stack_proyecto}}"
  
  mensaje_exito: |
    ✅ CONTEXTO GENERADO
    
    📄 Archivos generados:
       - {{archivos.contexto_proyecto}}
       - {{archivos.stack_proyecto}}
    
    📊 Confianza: [Alto|Medio|Bajo]
    
    🎯 Scorecard:
    | Aspecto | Puntuación |
    |---------|------------|
    | Arquitectura | [X]/10 |
    | Stack | [X]/10 |
    | Testing | [X]/10 |
    | DevOps | [X]/10 |
    
    💡 El archivo stack_proyecto.md contiene las especificaciones
       técnicas detectadas. Puedes editarlo si necesitas ajustes.

salida_multi_proyecto:
  archivos_generados:
    - tipo: "workspace"
      ruta: "{{archivos.workspace_index}}"
    - tipo: "contextos"
      ruta: "{{artifacts.contextos_folder}}/contexto_proyecto_[nombre].md"
    - tipo: "stacks"
      ruta: "{{artifacts.contextos_folder}}/stack_proyecto_[nombre].md"
  
  carpetas_creadas:
    - "{{artifacts.contextos_folder}}"
    - "{{artifacts.hu_compartidas}}"
    - "{{artifacts.hu_folder}}/[nombre_proyecto]"
  
  mensaje_exito: |
    ✅ WORKSPACE MULTI-PROYECTO CONFIGURADO
    
    📁 Estructura creada:
    {{rutas.artifacts_folder}}/
    ├── workspace.md
    ├── contextos/
    │   ├── contexto_proyecto_[proyecto_1].md
    │   ├── stack_proyecto_[proyecto_1].md
    │   ├── contexto_proyecto_[proyecto_2].md
    │   └── stack_proyecto_[proyecto_2].md
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
  descripcion: "Flujos recomendados según el tipo de proyecto"
  proyecto_unico:
    - comando: "*HU"
      descripcion: "Ver historias de usuario en el backlog"
    - herramienta: "refinar_hu"
      comando: ">refinar_hu [ID]"
      agente: "Refinador HU"
      descripcion: "Refinar una historia de usuario"
      accion_usuario: |
        1. Abre un nuevo chat con el agente **Refinador HU**
        2. Ejecuta: `>refinar_hu [ID-HU]`
  multi_proyecto:
    - comando: "*HU --compartidas"
      descripcion: "Ver HUs que afectan múltiples proyectos"
    - herramienta: "tomar_contexto"
      comando: ">tomar_contexto [proyecto]"
      descripcion: "Actualizar contexto de un proyecto específico"
```
