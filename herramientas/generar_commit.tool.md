---
nombre: "Generar Commit"
comando: ">generar_commit"
alias: [">commit", ">gc"]
version: "4.1"
---

```yaml
mandatory_base: "Cargar y aplicar TODAS las instrucciones de _base.tool.md ANTES de ejecutar esta herramienta. CRUCIAL - NO SALTAR."

mandatory_especifico:
  - instruccion: "Seguir especificación Conventional Commits estrictamente"
  - instruccion: "Usar modo imperativo (Añadir, no Añadido)"
  - instruccion: "Limitar título a 50 caracteres, máximo 72"
  - instruccion: "NUNCA terminar título con punto"
  - instruccion: "Primera letra mayúscula en descripción"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Git diff de cambios"
      obtencion: "git diff > {{rutas.artifacts_folder}}/diff.txt"
  archivos_opcionales:
    - "Nombre de branch actual"
    - "Número de issue/ticket"

parametros:
  opcionales:
    - nombre: tipo_commit
      tipo: string
      valores: [auto, feat, fix, docs, style, refactor, perf, test, build, ci, chore]
      defecto: auto
    - nombre: incluir_body
      tipo: boolean
      defecto: true
    - nombre: formato_alcance
      tipo: string
      valores: [auto, archivo, modulo, componente]
      defecto: auto
    - nombre: breaking_change
      tipo: boolean
      defecto: false

tipos_commit:
  feat: {desc: "Nueva funcionalidad", semver: MINOR}
  fix: {desc: "Corrección de bug", semver: PATCH}
  refactor: {desc: "Mejora estructura sin cambiar comportamiento", semver: none}
  perf: {desc: "Mejora de rendimiento", semver: PATCH}
  test: {desc: "Añadir o corregir pruebas", semver: none}
  docs: {desc: "Cambios en documentación", semver: none}
  style: {desc: "Cambios de formato", semver: none}
  ci: {desc: "Cambios en CI/CD", semver: none}
  build: {desc: "Cambios en sistema de build", semver: none}
  chore: {desc: "Tareas de mantenimiento", semver: none}

reglas_deteccion:
  feat: "Nuevos archivos de funcionalidad, nuevos métodos públicos"
  fix: "Cambios en try-catch, correcciones de bugs"
  refactor: "Renombrado, extracción de código"
  test: "Archivos en carpetas de test"
  docs: "Archivos .md, comentarios de documentación"
  style: "Cambios de formato, espacios"
  ci: "Archivos de CI/CD, Docker, pipelines"

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: tipo_commit='auto', incluir_body=true, formato_alcance='auto', breaking_change=false"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Captura Automática del Git Diff"
    obligatorio: true
    acciones: ["Crear {{rutas.artifacts_folder}} si no existe", "Ejecutar git diff > {{rutas.artifacts_folder}}/diff.txt", "Validar que el archivo no esté vacío"]
    si_error:
      sin_repositorio: " No es un repositorio git válido"
      sin_cambios: "ℹ No hay cambios para documentar"

  - paso: "Análisis del Contexto"
    obligatorio: true
    acciones: ["Parsear {{rutas.artifacts_folder}}/diff.txt", "Identificar archivos modificados", "Extraer información del branch name"]

  - paso: "Clasificación del Tipo de Commit"
    obligatorio: true
    acciones: ["Aplicar reglas_deteccion al diff", "Si tipo_commit=auto, inferir del contexto", "Validar tipo contra tipos_commit"]

  - paso: "Determinación del Alcance"
    obligatorio: true
    acciones: ["Aplicar estrategia según formato_alcance", "auto: inferir del contexto", "archivo/modulo/componente: detectar según patrón"]

  - paso: "Construcción del Título"
    obligatorio: true
    acciones: ["Formato: tipo(alcance): descripción", "Validar modo imperativo", "Validar longitud 50-72 chars", "Sin punto final"]

  - paso: "Generación del Cuerpo"
    obligatorio: false
    condicion: "incluir_body=true"
    acciones: ["Párrafo explicando el 'porqué'", "Lista de cambios con viñetas (-)", "Referencias a issues si disponibles", "BREAKING CHANGE si breaking_change=true"]

  - paso: "Entrega del Mensaje"
    obligatorio: true
    acciones: ["Validar formato Conventional Commits", "Presentar mensaje listo para usar"]

salida:
  archivos_generados:
    ruta: "{{rutas.artifacts_folder}}/diff.txt"
    temporal: true
  mensaje_exito: |
     Mensaje de Commit Generado
    ```
    [tipo](alcance): descripción
    
    [cuerpo opcional]
    ```
     Ejecutar: git commit -m "[mensaje]"

errores:
  sin_repositorio: {msg: " No se encuentra repositorio git", accion: "Verificar git init"}
  diff_vacio: {msg: "ℹ No hay cambios pendientes", accion: "Verificar git status"}
  titulo_muy_largo: {msg: " Título excede 72 chars", accion: "Acortar manteniendo palabras clave"}

siguiente:
  - {accion: "git commit -m '[mensaje]'", desc: "Aplicar el commit generado"}
  - {accion: "git add . && git commit -m '[mensaje]'", desc: "Agregar cambios y commitear"}
```
