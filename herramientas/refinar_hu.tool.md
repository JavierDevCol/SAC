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
  - instruccion: "Generar archivo de refinamiento ANTES de actualizar estado"
    nunca_saltar: true
  - instruccion: "NUNCA aceptar criterios de aceptación no medibles"
    nunca_saltar: true
  - instruccion: "Usar desglose VERTICAL (end-to-end), nunca horizontal"
    nunca_saltar: true
  - instruccion: "Generar documentación en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Refinar Historia de Usuario"
  comando: ">refinar_hu"
  alias: [">refinar", ">hu"]
  version: "4.0"

roles_autorizados:
  - REFINADOR
  - ARCHDEV
  - DEVOPS

prerequisitos:
  archivos_requeridos:
    - descripcion: "Texto de la Historia de Usuario"
      formato: "Como [rol], quiero [funcionalidad], para [beneficio]"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"
    - "{{archivos.backlog}}"
    - "Criterios de aceptación existentes"

parametros:
  opcionales:
    - nombre: formato_estimacion
      tipo: string
      valores: [story_points, horas, ambos]
      defecto: story_points
    - nombre: nivel_detalle
      tipo: string
      valores: [alto, medio, bajo]
      defecto: medio
    - nombre: incluir_riesgos
      tipo: boolean
      defecto: true
    - nombre: generar_tareas
      tipo: boolean
      defecto: true
    - nombre: incluir_testing
      tipo: boolean
      defecto: true

proceso:
  paso_1:
    nombre: "Evaluación de Nivel de Complejidad"
    obligatorio: true
    acciones:
      - "Analizar indicadores de la HU"
      - "Clasificar como 🟢 BAJO | 🟡 MEDIO | 🔴 ALTO"
      - "Anunciar nivel al usuario"
    matriz_decision:
      bajo:
        indicadores: ["CRUD básico", "Sin integraciones", "CA claros"]
        preguntas: "1-2"
        tareas: "3-5"
        sp_tipico: "2-3"
      medio:
        indicadores: ["Lógica moderada", "1-2 integraciones internas"]
        preguntas: "3-5"
        tareas: "5-10"
        sp_tipico: "5-8"
      alto:
        indicadores: ["Múltiples integraciones", "Impacto arquitectónico"]
        preguntas: "6-10+"
        tareas: "10-20"
        sp_tipico: "13+"

  paso_2:
    nombre: "Análisis y Preguntas de Clarificación"
    obligatorio: true
    acciones:
      - "Identificar ambigüedades en la narrativa"
      - "Detectar lagunas de información"
      - "Generar preguntas priorizadas (Alta/Media/Baja)"
    categorias_preguntas:
      alta_prioridad: "Afectan estimación o implementación"
      media_prioridad: "Mejoran experiencia de usuario"
      baja_prioridad: "Detalles de implementación"

  paso_3:
    nombre: "Refinamiento de Criterios de Aceptación"
    obligatorio: true
    acciones:
      - "Aplicar criterios SMART a cada CA"
      - "Reformular CA ambiguos"
      - "Agregar CA faltantes (error, validación, performance)"
    formato_smart:
      S: "Específico - qué debe ocurrir exactamente"
      M: "Medible - métricas verificables"
      A: "Alcanzable - realista en el sprint"
      R: "Relevante - relacionado con objetivo"
      T: "Temporal - condiciones de tiempo"

  paso_4:
    nombre: "Desglose Técnico Vertical"
    obligatorio: true
    condicion: "si generar_tareas=true"
    acciones:
      - "Identificar slices end-to-end mínimos"
      - "Generar tareas por slice"
      - "Asignar identificadores (HU-XXX-UI-01)"
      - "Incluir tareas de testing"
    estructura_slice:
      frontend: "Componentes UI, validaciones"
      api: "Endpoints REST, validación entrada"
      servicio: "Lógica de negocio"
      persistencia: "Modelos, queries, migrations"
      testing: "Unit, integration, acceptance"

  paso_5:
    nombre: "Estrategia y Estimación"
    obligatorio: true
    acciones:
      - "Recomendar enfoque (TDD, incremental, feature toggle)"
      - "Calcular Story Points con justificación"
      - "Desglosar factores: complejidad, incertidumbre, riesgo"

  paso_6:
    nombre: "Análisis de Riesgos"
    obligatorio: false
    condicion: "si incluir_riesgos=true"
    acciones:
      - "Identificar bloqueadores potenciales"
      - "Proponer estrategias de mitigación"
      - "Detectar dependencias de otras HU"

  paso_7:
    nombre: "Persistencia del Refinamiento"
    obligatorio: true
    acciones:
      - "Generar archivo [ID-HU]_refinamiento_[concepto].md"
      - "Guardar en {{artifacts.hu_refinamientos}}"
      - "Verificar si existe {{archivos.backlog}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas {{rutas.artifacts_folder}} si no existe"
      - "  2. Copiar plantilla desde {{plantillas.backlog}}"
      - "  3. Inicializar backlog vacío con estructura correcta"
      - "Actualizar {{archivos.backlog}} con estado [R] para la HU"
    plantilla_referencia: "{{plantillas.backlog}}"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Verificar si existe {{archivos.session_state}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas {{rutas.session_folder}} si no existe"
      - "  2. Copiar plantilla desde {{plantillas.session_state}}"
      - "  3. Inicializar con valores por defecto"
      - "Si existe:"
      - "  1. Leer estado actual"
      - "  2. Actualizar campos correspondientes"
      - "Registrar herramienta ejecutada: refinar_hu"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Actualizar estado de la HU refinada"
      - "Guardar cambios en {{archivos.session_state}}"
    plantilla_referencia: "{{plantillas.session_state}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "refinar_hu"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"
    validacion_post:
      - "Confirmar que {{archivos.session_state}} existe y es válido"
      - "Confirmar que el JSON es parseable"

salida:
  archivos_generados:
    - tipo: "refinamiento"
      ruta: "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md"
  
  archivos_actualizados:
    - "{{archivos.backlog}}"
    - "{{archivos.session_state}}"
  
  estado_hu_final: "[R] Refinada"
  
  mensaje_exito: |
    ✅ REFINAMIENTO COMPLETADO: [ID-HU]
    
    📄 Artefacto: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md
    
    📊 Resumen:
    - Criterios de Aceptación: [X] mejorados + [Y] nuevos
    - Estimación: [Z] SP / [W] horas
    - Riesgos: [N] identificados
    
    💡 Siguiente: >validar_hu [ID-HU]

formato_salida:
  estructura: |
    📋 Refinamiento: [Título de la HU]
    
    ## 1️⃣ Preguntas de Clarificación
    ### Alta Prioridad
    - [pregunta]
    ### Media Prioridad
    - [pregunta]
    
    ## 2️⃣ Criterios de Aceptación Refinados
    ### Mejorados
    - ✅ [original] → [SMART]
    ### Nuevos
    - [nuevo CA]
    
    ## 3️⃣ Desglose Técnico
    ### Slice 1: [Funcionalidad]
    - [ ] [ID-TAREA]: [descripción] ([Xh])
    
    ## 4️⃣ Estrategia y Estimación
    - Enfoque: [TDD/incremental/etc.]
    - Total: [X] SP ([Y] horas)
    
    ## 5️⃣ Riesgos
    - 🔴 Alto: [descripción] → Mitigación: [acción]

errores:
  hu_mal_formateada:
    mensaje: "⚠️ HU incompleta o mal formateada"
    accion: "Solicitar formato: Como [rol], quiero [func], para [beneficio]"
  sin_criterios:
    mensaje: "ℹ️ HU sin criterios de aceptación"
    accion: "Generar CA básicos inferidos, solicitar validación"
  hu_muy_grande:
    mensaje: "⚠️ HU de tamaño épica detectada"
    accion: "Sugerir partición en HUs más pequeñas"

siguiente:
  herramienta: "validar_hu"
  comando: ">validar_hu [ID-HU]"
  rol_requerido: "ONAD"
  descripcion: "Validación arquitectónica de la HU refinada"
```
