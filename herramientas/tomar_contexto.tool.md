---
nombre: "Tomar Contexto"
comando: ">tomar_contexto"
alias: [">contexto", ">tc"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Pasos obligatorios NO se pueden omitir"
  - instruccion: "Detectar tipo de workspace (unico/multi) ANTES de analizar"
  - instruccion: "En multi-proyecto: workspace.md + contextos individuales"
  - instruccion: "NUNCA mezclar contextos de diferentes proyectos"
  - instruccion: "Generar en idioma: {{preferencias.idioma_documentacion}}"
  - instruccion: "Si {{usuario.incluir_firma_en_documentos}}=true, agregar pie: '---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---'"

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
    - {nombre: profundidad_analisis, tipo: string, valores: [basico, completo, exhaustivo], defecto: completo}
    - {nombre: incluir_dependencias, tipo: boolean, defecto: true}
    - {nombre: incluir_devops, tipo: boolean, defecto: true}
    - {nombre: detectar_patrones, tipo: boolean, defecto: true}
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
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: profundidad_analisis='completo', incluir_dependencias=true, incluir_devops=true, detectar_patrones=true"]
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
    acciones: ["Identificar lenguaje principal", "Detectar framework y versión", "Listar dependencias principales"]

  - paso: "Analizar Arquitectura"
    obligatorio: true
    acciones: ["Identificar estilo arquitectónico", "Mapear estructura de carpetas", "Detectar componentes principales"]

  - paso: "Evaluar DevOps"
    obligatorio: true
    condicion: "incluir_devops=true"
    acciones: ["Buscar Dockerfile, docker-compose", "Detectar CI/CD (GitHub Actions, GitLab CI)", "Identificar IaC"]

  - paso: "Generar Scorecard"
    obligatorio: true
    acciones: ["Evaluar: Arquitectura, Stack, Testing, DevOps (1-10)", "Identificar puntos de atención"]

  - paso: "Crear Archivos de Contexto"
    obligatorio: true
    acciones_unico:
      - "Crear {{rutas.artifacts_folder}} si no existe"
      - "Generar {{archivos.contexto_proyecto}} desde {{plantillas.contexto}}"
      - "Generar {{archivos.stack_proyecto}} desde {{plantillas.stack_proyecto}}"
    acciones_multi:
      - "Crear estructura: {{artifacts.contextos_folder}}, {{artifacts.hu_compartidas}}, {{artifacts.hu_folder}}/[proyecto]"
      - "Por cada proyecto: contexto_proyecto_[nombre].md + stack_proyecto_[nombre].md"
      - "Detectar relaciones entre proyectos"
      - "Generar {{archivos.workspace_index}} desde {{plantillas.workspace}}"

salida:
  archivos_unico:
    - "{{archivos.contexto_proyecto}}"
    - "{{archivos.stack_proyecto}}"
  archivos_multi:
    - "{{archivos.workspace_index}}"
    - "{{artifacts.contextos_folder}}/contexto_proyecto_[nombre].md"
    - "{{artifacts.contextos_folder}}/stack_proyecto_[nombre].md"
  carpetas_multi:
    - "{{artifacts.contextos_folder}}"
    - "{{artifacts.hu_compartidas}}"
    - "{{artifacts.hu_folder}}/[proyecto]"
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
  mensaje_unico: |
     CONTEXTO GENERADO
     {{archivos.contexto_proyecto}} + {{archivos.stack_proyecto}}
     Scorecard: Arq [X]/10 | Stack [X]/10 | Test [X]/10 | DevOps [X]/10
  mensaje_multi: |
     WORKSPACE MULTI-PROYECTO CONFIGURADO
     workspace.md + [N] contextos generados
     Comandos: *HU --compartidas | *HU --proyecto=[nombre]

errores:
  sin_permisos: {msg: " Sin permisos de lectura", accion: "Solicitar acceso"}
  proyecto_vacio: {msg: " Sin archivos detectables", accion: "Generar contexto básico"}
  sin_marcadores: {msg: " No se detectó ningún proyecto", accion: "Verificar carpeta correcta"}
  proyecto_no_encontrado: {msg: " Proyecto '[nombre]' no encontrado", accion: "Ejecutar sin parámetros para listar"}
  workspace_existente: {msg: "ℹ Ya existe contexto", accion: "Usar --force para regenerar"}

siguiente:
  - {comando: "*HU", desc: "Ver historias de usuario en backlog"}
  - {comando: ">refinar_hu [ID]", desc: "Refinar una HU", chat_agente: "Refinador HU"}
  - {comando: "*HU --compartidas", desc: "Ver HUs cross-proyecto (multi)"}
```
