---
nombre: "Tomar Contexto"
comando: ">tomar_contexto"
alias: [">contexto", ">tc"]
version: "4.1"
---

```yaml
mandatory_base: "Cargar y aplicar TODAS las instrucciones de _base.tool.md ANTES de ejecutar esta herramienta. CRUCIAL - NO SALTAR."

mandatory_especifico:
  - instruccion: "Detectar tipo de workspace (unico/multi) ANTES de analizar"
  - instruccion: "En multi-proyecto: workspace.md + contextos individuales"
  - instruccion: "NUNCA mezclar contextos de diferentes proyectos"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Acceso a raíz del proyecto"
      validacion: "Permisos de lectura"
  archivos_opcionales:
    - "README.md"
    - "pom.xml | build.gradle | package.json"
    - "Dockerfile | docker-compose.yml"

parametros:
  opcionales:
    - {nombre: profundidad_analisis, tipo: string, valores: [basico, completo, exhaustivo], defecto: exhaustivo}
    - {nombre: nombre_proyecto, tipo: string, descripcion: "Proyecto específico en multi-proyecto"}
    - {nombre: all, tipo: flag, descripcion: "Analizar todos los proyectos"}
    - {nombre: force, tipo: flag, descripcion: "Regenerar aunque exista"}

marcadores_proyecto:
  java: ["pom.xml", "build.gradle", "build.gradle.kts"]
  javascript: ["package.json"]
  python: ["pyproject.toml", "setup.py", "requirements.txt"]
  dotnet: ["*.csproj", "*.sln"]
  rust: ["Cargo.toml"]
  go: ["go.mod"]

deteccion_tipo:
  unico: "1 marcador en raíz"
  multi: "0 marcadores en raíz + 2+ subcarpetas con marcadores"

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: profundidad_analisis='exhaustivo'"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Detectar Tipo de Workspace"
    obligatorio: true
    acciones: ["Buscar marcadores en raíz según marcadores_proyecto", "Si 1+ en raíz  MODO_UNICO", "Si 0 en raíz  buscar en subcarpetas  MODO_MULTI si 2+"]

  - paso: "Listar Proyectos (MODO_MULTI)"
    obligatorio: true
    condicion: "MODO_MULTI"
    acciones: ["Escanear subcarpetas con marcadores", "Mostrar tabla: # | Proyecto | Stack | Ruta", "Solicitar selección o confirmar --all"]

  - paso: "Detectar Stack Tecnológico"
    obligatorio: true
    acciones: ["Identificar lenguaje principal", "Detectar framework y versión"]

  - paso: "Analizar Arquitectura"
    obligatorio: true
    acciones: ["Identificar estilo arquitectónico", "Mapear estructura de carpetas", "Detectar componentes principales", "Si es multirepo/proyecto identificar relaciones entre proyectos/repos como se comunican, etc."]

  - paso: "Evaluar DevOps"
    obligatorio: true
    condicion: "incluir_devops=true"
    acciones: ["Buscar Dockerfile, docker-compose", "Detectar CI/CD (GitHub Actions, GitLab CI)", "Identificar IaC"]

  - paso: "Detectar Patrones"
    obligatorio: true
    regla_referencia: "{{reglas.patrones_diseno}}"
    herramientas: ["file_search", "grep_search", "list_dir", "read_file"]
    acciones:
      - "Ejecutar {{reglas.patrones_diseno}}.indicadores_deteccion.algoritmo_deteccion"
      - "Paso 1: file_search para archivos con nombres de patrones (Factory, Builder, Repository...)"
      - "Paso 2: list_dir + file_search para detectar patrones arquitectónicos por estructura"
      - "Paso 3: grep_search + read_file para validar implementación real en código"
      - "Paso 4: Asignar confianza según coincidencias (nombre + estructura + código = alta)"
      - "SI detecta code smell → consultar {{reglas.patrones_diseno}}.mapeo_smells para sugerir patrón"
      - "Obtener URL de ejemplo según stack: {{reglas.patrones_diseno}}.urls_por_patron[patron][lenguaje]"
    output:
      usar: "{{reglas.patrones_diseno}}.indicadores_deteccion.output_deteccion"
    validacion:
      - "Verificar consistencia patrones ↔ stack del proyecto"
      - "SI confianza = baja → marcar para revisión manual"
      - "SI no encuentra patrones → reportar 'Sin patrones identificables'"
      - "SI encuentra anti-patrones → agregar warning con sugerencia de {{reglas.patrones_diseno}}"

  - paso: "Generar Scorecard"
    obligatorio: true
    acciones: ["Evaluar: Arquitectura, Stack, Testing, DevOps (1-10)", "Identificar puntos de atención"]
  
  - paso: "Generar Diagramas de Estructura, clases, secuencia"
    obligatorio: true
    acciones: ["Generar diagramas mermaid", "Seguir estrcitamente los pasos  de creacion de diagramas {{reglas.mermaid}} "]

  - paso: "Crear Archivos de Contexto"
    obligatorio: true
    dependencias: ["Detectar Stack Tecnológico"] 
    acciones_unico:
      - "Generar Listas detallada de cada componente identificado en el analisis especificando la version de cada uno"
      - "Crear {{rutas.artifacts_folder}} si no existe"
      - "Generar {{archivos.contexto_proyecto}} desde {{plantillas.contexto}}"
      - "Incluir resumen básico del stack en contexto_proyecto (datos de 'Detectar Stack Tecnológico')"
    acciones_multi:
      - "Generar Listas detallada de cada componente identificado en el analisis especificando la version de cada uno"
      - "Crear estructura: {{artifacts.contextos_folder}}, {{artifacts.hu_compartidas}}, {{artifacts.hu_folder}}/[proyecto]"
      - "Por cada proyecto: contexto_proyecto_[nombre].md (incluye resumen básico del stack)"
      - "Detectar relaciones entre proyectos"
      - "Generar {{archivos.workspace_index}} desde {{plantillas.workspace}}"

salida:
  descripcion: "Archivos y carpetas generados. Paths definidos en CONFIG_SYSTEM.yaml"
  
  modo_unico:
    carpetas_a_crear:
      - "{{rutas.artifacts_folder}}"         
    archivos_a_generar:
      - path: "{{archivos.contexto_proyecto}}"
        plantilla: "{{plantillas.contexto}}"
        datos_requeridos: [arquitectura, componentes, patrones, scorecard, diagramas, stack_basico]
    mensaje_exito: |
      ✅ CONTEXTO GENERADO
      📁 {{archivos.contexto_proyecto}}
      📊 Scorecard: Arq ${scorecard.arquitectura}/10 | Stack ${scorecard.stack}/10 | Test ${scorecard.testing}/10 | DevOps ${scorecard.devops}/10
      
      💡 Para análisis detallado del stack: >tomar_stack
  
  modo_multi:
    carpetas_a_crear:
      - "{{rutas.artifacts_folder}}"          
      - "{{artifacts.contextos_folder}}"    
      - "{{artifacts.hu_compartidas}}"         
      - "{{artifacts.hu_folder}}/${proyecto.nombre}" 
         ↑ Iterar: PARA CADA proyecto en proyectos[]
    archivos_a_generar:
      - path: "{{archivos.workspace_index}}"   
        plantilla: "{{plantillas.workspace}}"
        datos_requeridos: [lista_proyectos, relaciones, stack_consolidado, scorecard_global]
      - path: "{{artifacts.contextos_folder}}/contexto_proyecto_${proyecto.nombre}.md"
        plantilla: "{{plantillas.contexto}}"
        iterar: "PARA CADA proyecto en proyectos[]"
        datos_requeridos: [proyecto.arquitectura, proyecto.componentes, proyecto.patrones, proyecto.stack_basico]
    mensaje_exito: |
      ✅ WORKSPACE MULTI-PROYECTO CONFIGURADO
      📁 {{archivos.workspace_index}}
      📁 {{artifacts.contextos_folder}}/ (${proyectos.length} contextos)
      📊 Scorecard Global: ${scorecard.promedio}/10
      
      🔧 Comandos disponibles:
        >planificar_hu --compartidas
        >planificar_hu --proyecto=${proyectos[0].nombre}

validar: 
  obligatorio: true
  acciones: ["Siempre verificar que los documentos contengan la informacion correcta del analsiis realizado.", "Preguntar al uisuario si el contexto lo ve correcto [OK] o si tiene alguna sugerencia sobre el contexto y editarlo [EDITAR]", "Especificar el flag con el cual se realizo el analisis [basico, completo, exhaustivo]"]

errores:
  si_proyecto_vacio: {msg: " Sin archivos detectables", accion: "Generar contexto básico"}
  sin_marcadores: {msg: " No se detectó ningún proyecto", accion: "Verificar carpeta correcta"}
  si_proyecto_no_encontrado: {msg: " Proyecto '[nombre]' no encontrado", accion: "Ejecutar sin parámetros para listar"}
  workspace_existente: {msg: "ℹ Ya existe contexto", accion: "Preguntar al usuario si Usar --force para regenerar"}
```
