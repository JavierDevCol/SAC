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
  - instruccion: "Nunca saltar proceso.paso_final"
    nunca_saltar: true
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
    nunca_saltar: true
  - instruccion: "Validar que el formato de ADR seleccionado sea uno de los soportados (nygard, madr, y-statement, custom)"
    nunca_saltar: true
  - instruccion: "Asegurar que el título del ADR sea único y no exista duplicado en la carpeta de ADRs"
    nunca_saltar: true
  - instruccion: "Los ADRs son inmutables - nunca modificar ADRs existentes, crear nuevos que superseden"
    nunca_saltar: true
  - instruccion: "Mantener numeración secuencial sin saltos (001, 002, 003...)"
    nunca_saltar: true
  - instruccion: "Leer y almacenar parámetros desde {{reglas.mermaid}}"
    nunca_saltar: true
  - instruccion: "Si se decide crear diagramas mermaid en el ADR, seguir el proceso paso a paso en orden secuencial del paso_5"
    nunca_saltar: true

identificacion:
  nombre: "Generar Architecture Decision Record (ADR)"
  comando: ">generar_adr"
  alias: [">crear_adr", ">nuevo_adr", ">adr"]
  version: "2.2"

objetivo: |
  Generar documentación formal de decisiones arquitectónicas siguiendo estándares 
  de Architecture Decision Records (ADR), soportando múltiples formatos y plantillas, 
  para mantener trazabilidad y contexto de decisiones técnicas críticas a lo largo 
  del ciclo de vida del proyecto.

roles_autorizados:
  - "ArchDev Pro"
  - "Arquitecto Onad"
  - "Arquitecto DevOps"

integracion:
  herramientas_que_invocan:
    - nombre: "define_arquitectura"
      cuando: "Al finalizar análisis arquitectónico y obtener aprobación del usuario"
      proposito: "Documentar formalmente la decisión arquitectónica en un ADR"
    - nombre: "planificar_hu"
      cuando: "Cuando una HU implica decisiones arquitectónicas significativas"
      proposito: "Registrar decisiones técnicas antes de la implementación"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Archivo de estado de sesión"
      ubicacion: "{{session_state_location}}"
    - descripcion: "Archivo de configuración del proyecto"
      ubicacion: "{{project_root}}/.SAC/CONFIG_INIT.yaml"
  archivos_opcionales:
    - descripcion: "Directorio de ADRs existentes (para auto-numeración)"
      ubicacion: "{{adr_location}}"
    - descripcion: "Archivo de contexto del proyecto"
      ubicacion: "{{contexto_proyecto_location}}"
    - descripcion: "Índice de ADRs existentes"
      ubicacion: "{{adr_location}}/README.md"

parametros:
  requeridos:
    - nombre: "titulo"
      tipo: string
      descripcion: "Título descriptivo de la decisión arquitectónica"
    - nombre: "contexto"
      tipo: string
      descripcion: "Descripción del problema o necesidad que motivó la decisión"
    - nombre: "decision"
      tipo: string
      descripcion: "Opción arquitectónica seleccionada con justificación"
    - nombre: "consecuencias"
      tipo: string
      descripcion: "Trade-offs, beneficios y riesgos aceptados"
  opcionales:
    - nombre: "formato"
      tipo: string
      valores: ["nygard", "madr", "y-statement", "custom"]
      defecto: "nygard"
      descripcion: "Formato de ADR a usar"
    - nombre: "estado"
      tipo: string
      valores: ["propuesto", "aceptado", "rechazado", "deprecado", "supersedido"]
      defecto: "aceptado"
      descripcion: "Estado de la decisión"
    - nombre: "opciones_consideradas"
      tipo: string
      descripcion: "Alternativas evaluadas y razones de descarte"
    - nombre: "fecha"
      tipo: string
      defecto: "{{fecha_actual}}"
      descripcion: "Fecha de la decisión (YYYY-MM-DD)"
    - nombre: "autores"
      tipo: string
      defecto: "{{usuario.nombre}}"
      descripcion: "Equipo o personas involucradas en la decisión"
    - nombre: "referencias"
      tipo: string
      descripcion: "Links a documentos relacionados (análisis, benchmarks, RFCs)"
    - nombre: "adr_relacionados"
      tipo: string
      descripcion: "ADRs que supersede o complementa"
    - nombre: "incluir_diagrama"
      tipo: boolean
      defecto: true
      descripcion: "Generar diagrama Mermaid visual de la decisión"
    - nombre: "archivo_salida"
      tipo: string
      defecto: "{{adr_location}}/NNN-titulo-slug.md"
      descripcion: "Ruta donde guardar el ADR"
    - nombre: "numero_adr"
      tipo: number
      defecto: "auto"
      descripcion: "Número secuencial del ADR (auto-detecta siguiente disponible)"

proceso:
  paso_0:
    nombre: "Carga de Configuración Crítica"
    obligatorio: true
    acciones:
      - "Cargar y leer {{session_state_location}}"
      - "Cargar y leer {{project_root}}/.SAC/CONFIG_INIT.yaml"
      - "Extraer variables de configuración necesarias (idioma, rutas, etc.)"
    si_error:
      "archivo_no_encontrado": "Notificar al usuario y solicitar ejecutar >tomar_contexto primero"

  paso_1:
    nombre: "Validación de Entradas"
    obligatorio: true
    acciones:
      - "Verificar que todos los parámetros requeridos estén presentes (titulo, contexto, decision, consecuencias)"
      - "Validar que el formato seleccionado sea soportado"
      - "Verificar que el título no exceda 100 caracteres"
      - "Si falta información crítica, solicitar al usuario antes de continuar"
    validaciones:
      - "titulo no vacío y no duplicado"
      - "contexto mínimo 50 caracteres"
      - "decision mínimo 30 caracteres"
      - "consecuencias mínimo 30 caracteres"
    si_error:
      "parametros_faltantes": "Solicitar explícitamente cada dato faltante antes de generar"
      "formato_invalido": "Listar formatos disponibles: nygard, madr, y-statement, custom"
      "titulo_duplicado": "Advertir y sugerir título alternativo"

  paso_2:
    nombre: "Determinación de Número ADR"
    obligatorio: true
    acciones:
      - "Escanear carpeta {{adr_location}} para listar ADRs existentes"
      - "Determinar el siguiente número secuencial disponible"
      - "Formato de número: 001, 002, 003, etc. (3 dígitos con padding)"
      - "Si la carpeta no existe, crearla y comenzar con 001"
    si_error:
      "error_lectura": "Crear carpeta {{adr_location}} y comenzar con número 001"

  paso_3:
    nombre: "Selección de Plantilla"
    obligatorio: true
    acciones:
      - "Seleccionar plantilla según parámetro 'formato'"
      - "Cargar estructura base de la plantilla correspondiente"
    plantillas_disponibles:
      nygard:
        descripcion: "Formato clásico de Michael Nygard - Simple y directo"
        ubicacion: "{{plantillas_location}}/adr_nygard.plantilla.md"
      madr:
        descripcion: "Markdown Any Decision Records - Más estructurado"
        ubicacion: "{{plantillas_location}}/adr_madr.plantilla.md"
      y-statement:
        descripcion: "Formato ultra-conciso - Una sola frase estructurada"
        ubicacion: "{{plantillas_location}}/adr_y_statement.plantilla.md"
      custom:
        descripcion: "Estructura personalizada definida por el usuario"
        ubicacion: "Definida por el usuario en tiempo de ejecución"
    si_error:
      "plantilla_no_encontrada": "Usar formato nygard por defecto"

  paso_4:
    nombre: "Generación del Contenido ADR"
    obligatorio: true
    acciones:
      - "Rellenar la plantilla seleccionada con los datos proporcionados"
      - "Aplicar formato Markdown correcto (títulos, listas, tablas, énfasis)"
      - "Asegurar que las secciones obligatorias estén completas"
      - "Agregar metadatos: fecha, versión, autores, estado"
      - "Generar slug del título para nombre de archivo (máximo 50 caracteres, kebab-case)"
    formato_archivo: "[numero_adr]-[titulo-slug].md"
    si_error:
      "error_formato": "Notificar sección con error y solicitar corrección"

  paso_5:
    nombre: "Generación de Diagrama Mermaid"
    obligatorio: false
    condicion: "Si incluir_diagrama es true O la decisión involucra flujos/componentes/estados"
    reglas_mermaid:
      obligatorio: true
      referencia: "{{reglas.mermaid}}"
    acciones:
      - "Cargar las reglas_mermaid"
      - "Analizar el contexto y la decisión para determinar el tipo de diagrama más adecuado"
      - "Generar diagrama Mermaid siguiendo las reglas de reglas_mermaid"
      - "Insertar el diagrama en la sección correspondiente del ADR"
    si_error:
      "diagrama_invalido": "Omitir diagrama y notificar al usuario"

  paso_6:
    nombre: "Creación del Archivo"
    obligatorio: true
    acciones:
      - "Generar nombre del archivo: [numero_adr]-[titulo-slug].md"
      - "Crear estructura de carpetas {{adr_location}} si no existe"
      - "Guardar el archivo en la ruta especificada"
      - "Actualizar índice de ADRs si existe ({{adr_location}}/README.md)"
    actualizacion_indice:
      - "Agregar entrada al índice con número, título, estado y fecha"
      - "Mantener orden cronológico/numérico"
    si_error:
      "error_escritura": "Verificar permisos y notificar al usuario"
      "archivo_existe": "Preguntar si sobrescribir o crear nueva versión"

  paso_7:
    nombre: "Confirmación y Entrega"
    obligatorio: true
    acciones:
      - "Mostrar resumen del ADR generado"
      - "Mostrar vista previa de las primeras líneas"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    acciones:
      - "Verificar si existe {{session_state_location}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas si no existe"
      - "  2. Copiar plantilla desde {{plantillas.session_state}}"
      - "  3. Inicializar con valores por defecto"
      - "Si existe:"
      - "  1. Leer estado actual"
      - "  2. Actualizar campos correspondientes"
      - "Registrar herramienta ejecutada: generar_adr"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Actualizar registro de ADRs (ultimo_numero, total, lista)"
      - "Guardar cambios en {{session_state_location}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "generar_adr"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[ruta del ADR generado]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"
      - campo: "adrs.ultimo_numero"
        valor: "[NNN]"
      - campo: "adrs.total"
        valor: "[incrementar en 1]"
    registro_evento:
      timestamp: "[timestamp_actual]"
      rol: "[rol_actual]"
      herramienta: "generar_adr"
      tipo: "adr_generado"
      detalle: "ADR [NNN]: [titulo] - Formato: [formato] - Estado: [estado]"
    validacion_post:
      - "Confirmar que {{session_state_location}} existe y es válido"
      - "Confirmar que el JSON es parseable"

# ============================================
# RESTRICCIONES
# ============================================
restricciones:
  - "Solo genera archivos Markdown (.md)"
  - "Requiere parámetros mínimos: titulo, contexto, decision, consecuencias"
  - "No modifica ADRs existentes - Son inmutables, se crean nuevos que superseden"
  - "Numeración secuencial obligatoria - No permite saltos"
  - "Un ADR por decisión - No mezcla múltiples decisiones"
  - "Slug máximo 50 caracteres - Nombres truncados automáticamente"
  - "Diagramas Mermaid sin HTML - Solo sintaxis estándar"

salida:
  archivos_generados:
    - tipo: "Archivo ADR"
      ruta: "{{adr_location}}/[numero]-[titulo-slug].md"
      descripcion: "Architecture Decision Record en formato Markdown"
  archivos_actualizados:
    - "{{session_state_location}}"
    - "{{adr_location}}/README.md (si existe)"
  mensaje_exito: |
    ✅ **GENERACIÓN DE ADR COMPLETADA**
    
    📄 **Archivo generado:** {{adr_location}}/[numero]-[slug].md
    
    📊 **Resumen:**
    - Formato: [formato]
    - Estado: [estado]
    - Fecha: [fecha]
    - Diagrama incluido: [sí/no]

errores:
  "parametros_faltantes":
    mensaje: "❌ Faltan parámetros requeridos para generar el ADR"
    accion: "Solicitar al usuario: titulo, contexto, decision, consecuencias"
  "formato_invalido":
    mensaje: "❌ El formato especificado no es válido"
    accion: "Formatos disponibles: nygard, madr, y-statement, custom"
  "titulo_duplicado":
    mensaje: "⚠️ Ya existe un ADR con título similar"
    accion: "Sugerir título alternativo o confirmar creación"
  "error_lectura":
    mensaje: "❌ Error al leer la carpeta de ADRs"
    accion: "Verificar permisos y existencia de {{adr_location}}"
  "error_escritura":
    mensaje: "❌ Error al guardar el archivo ADR"
    accion: "Verificar permisos de escritura en la carpeta destino"
  "diagrama_invalido":
    mensaje: "⚠️ No se pudo generar el diagrama Mermaid"
    accion: "ADR generado sin diagrama - revisar manualmente"
  "session_state_error":
    mensaje: "⚠️ Error al actualizar session_state"
    accion: "ADR generado correctamente pero sin registro en sesión"

metricas:
  trackear_en_session_state:
    - nombre: "adrs_generados_total"
      descripcion: "Total de ADRs generados"
    - nombre: "adrs_por_formato"
      descripcion: "Distribución por formato (Nygard, MADR, Y-Statement)"
    - nombre: "adrs_por_estado"
      descripcion: "Distribución por estado (Aceptado, Propuesto, etc.)"
    - nombre: "adrs_con_diagrama"
      descripcion: "Total de ADRs que incluyen diagrama Mermaid"

siguiente:  "Esta herramienta no tiene flujo siguiente obligatorio, El ADR generado es un artefacto final independiente"
```