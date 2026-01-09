```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Seguir especificación Conventional Commits estrictamente"
    nunca_saltar: true
  - instruccion: "Usar modo imperativo (Añadir, no Añadido)"
    nunca_saltar: true
  - instruccion: "Limitar título a 50 caracteres, máximo 72"
    nunca_saltar: true
  - instruccion: "NUNCA terminar título con punto"
    nunca_saltar: true
  - instruccion: "Generar mensajes de commit en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Generar Commit"
  comando: ">generar_commit"
  alias: [">commit", ">gc"]
  version: "4.0"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Git diff de cambios"
      obtencion: "git diff > cochas/artifacts/diff.txt"
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

proceso:
  paso_0:
    nombre: "Captura Automática del Git Diff"
    obligatorio: true
    acciones:
      - "Crear directorio {{rutas.artifacts_folder}} si no existe"
      - "Ejecutar: git diff > {{rutas.artifacts_folder}}/diff.txt"
      - "Validar que el archivo no esté vacío"
    si_error:
      sin_repositorio: "❌ No es un repositorio git válido"
      sin_cambios: "ℹ️ No hay cambios para documentar"

  paso_1:
    nombre: "Análisis del Contexto"
    obligatorio: true
    acciones:
      - "Parsear {{rutas.artifacts_folder}}/diff.txt para identificar archivos modificados"
      - "Extraer información del branch name"
      - "Identificar si hay cambios en archivos críticos"

  paso_2:
    nombre: "Clasificación del Tipo de Commit"
    obligatorio: true
    reglas_deteccion:
      feat: "Nuevos archivos de funcionalidad, nuevos métodos públicos"
      fix: "Cambios en try-catch, correcciones de bugs"
      refactor: "Renombrado, extracción de código"
      test: "Archivos en carpetas de test"
      docs: "Archivos .md, comentarios de documentación"
      style: "Cambios de formato, espacios"
      ci: "Archivos de CI/CD, Docker"

  paso_3:
    nombre: "Determinación del Alcance"
    obligatorio: true
    estrategias:
      auto: "Inferir del contexto del proyecto"
      archivo: "Nombre del archivo principal"
      modulo: "Detectar módulo/paquete afectado"
      componente: "Identificar componente arquitectónico"

  paso_4:
    nombre: "Construcción del Título"
    obligatorio: true
    formato: "tipo(alcance): descripción"
    reglas:
      - "Modo imperativo y tiempo presente"
      - "Primera letra mayúscula"
      - "Sin punto final"
      - "Máximo 50-72 caracteres"

  paso_5:
    nombre: "Generación del Cuerpo"
    obligatorio: false
    condicion: "si incluir_body=true"
    estructura:
      - "Párrafo explicando el 'porqué'"
      - "Lista de cambios con viñetas (-)"
      - "Referencias a issues si disponibles"
      - "BREAKING CHANGE si aplica"

  paso_6:
    nombre: "Entrega del Mensaje"
    obligatorio: true
    acciones:
      - "Validar formato Conventional Commits"
      - "Presentar mensaje listo para usar"

salida:
  archivos_generados:
    - tipo: "diff temporal"
      ruta: "{{rutas.artifacts_folder}}/diff.txt"
      temporal: true
  
  mensaje_exito: |
    ✅ Mensaje de Commit Generado
    
    ```
    [mensaje completo]
    ```
    
    🚀 Ejecutar: git commit -m "[mensaje]"

tipos_commit:
  feat:
    descripcion: "Nueva funcionalidad para el usuario"
    semver: "MINOR"
  fix:
    descripcion: "Corrección de bug"
    semver: "PATCH"
  refactor:
    descripcion: "Mejora de estructura sin cambiar comportamiento"
    semver: "ninguno"
  perf:
    descripcion: "Mejora de rendimiento"
    semver: "PATCH"
  test:
    descripcion: "Añadir o corregir pruebas"
    semver: "ninguno"
  docs:
    descripcion: "Cambios en documentación"
    semver: "ninguno"
  style:
    descripcion: "Cambios de formato sin afectar significado"
    semver: "ninguno"
  ci:
    descripcion: "Cambios en integración continua"
    semver: "ninguno"
  build:
    descripcion: "Cambios en sistema de compilación"
    semver: "ninguno"
  chore:
    descripcion: "Otras tareas de mantenimiento"
    semver: "ninguno"

errores:
  sin_repositorio:
    mensaje: "❌ No se encuentra repositorio git"
    accion: "Verificar que está en directorio con git init"
  diff_vacio:
    mensaje: "ℹ️ No hay cambios pendientes"
    accion: "Verificar con git status"
  titulo_muy_largo:
    mensaje: "⚠️ Título excede 72 caracteres"
    accion: "Acortar automáticamente manteniendo palabras clave"

siguiente:
  descripcion: "Acciones disponibles tras generar el mensaje de commit"
  opciones:
    - comando: "git commit -m '[mensaje]'"
      descripcion: "Aplicar el commit generado"
      accion_usuario: "Copia el mensaje generado y ejecuta el comando en terminal"
    - comando: "git add . && git commit -m '[mensaje]'"
      descripcion: "Agregar cambios y commitear"
      accion_usuario: "Usa este comando si tienes cambios sin agregar al staging"
```
````
