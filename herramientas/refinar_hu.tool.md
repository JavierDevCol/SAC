```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
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
  paso_0:
    nombre: "Detectar Feedback de Validación Previa"
    obligatorio: true
    acciones:
      - "Buscar archivo existente en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md"
      - "Si existe, buscar sección '## 📝 Feedback de Validación'"
      - "Si hay feedback pendiente, cambiar a MODO AJUSTE"
    modo_ajuste:
      descripcion: "Re-refinamiento enfocado en resolver observaciones"
      comportamiento:
        - "Mostrar observaciones pendientes al usuario"
        - "Enfocar preguntas de clarificación en las observaciones"
        - "Priorizar resolución de feedback sobre nuevo refinamiento"
        - "Marcar observaciones como resueltas al abordarlas"
      mensaje_inicio: |
        🔄 MODO AJUSTE ACTIVADO
        
        Se detectó feedback de validación previa (Iteración [N]):
        
        📝 Observaciones pendientes:
        - [ ] [observación_1]
        - [ ] [observación_2]
        
        Este refinamiento se enfocará en resolver estas observaciones.
    modo_nuevo:
      descripcion: "Refinamiento inicial de HU nueva"
      comportamiento: "Flujo normal de refinamiento"

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
      - "Verificar si existe {{archivos.backlog}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas {{rutas.artifacts_folder}} si no existe"
      - "  2. Copiar plantilla desde {{plantillas.backlog}}"
      - "  3. Inicializar backlog vacío con estructura correcta"
      - "Actualizar {{archivos.backlog}} con estado [R] para la HU"
    acciones_modo_nuevo:
      - "Generar archivo [ID-HU]_refinamiento_[concepto].md"
      - "Guardar en {{artifacts.hu_refinamientos}}"
    acciones_modo_ajuste:
      - "Actualizar archivo existente [ID-HU]_refinamiento.md"
      - "Marcar observaciones resueltas: [ ] → [x]"
      - "Agregar sección '## ✅ Ajustes Aplicados (Iteración N)'"
      - "Documentar qué cambió para resolver cada observación"
    formato_ajustes_aplicados: |
      ## ✅ Ajustes Aplicados (Iteración [N])
      
      **Fecha:** [fecha_actual]
      
      ### Observaciones Resueltas
      - [x] [observación_1]: [cómo se resolvió]
      - [x] [observación_2]: [cómo se resolvió]
      
      ### Cambios Realizados
      - [descripción del cambio 1]
      - [descripción del cambio 2]
    plantilla_referencia: "{{plantillas.backlog}}"

salida:
  archivos_generados:
    - tipo: "refinamiento"
      ruta: "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md"
      nota: "Solo en modo nuevo"
  
  archivos_actualizados:
    - "{{archivos.backlog}}"
    - "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md (en modo ajuste)"
  
  estado_hu_final: "[R] Refinada"
  
  mensaje_exito_modo_nuevo: |
    ✅ REFINAMIENTO COMPLETADO: [ID-HU]
    
    📄 Artefacto: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md
    
    📊 Resumen:
    - Criterios de Aceptación: [X] mejorados + [Y] nuevos
    - Estimación: [Z] SP / [W] horas
    - Riesgos: [N] identificados
    
    💡 Siguiente: >validar_hu [ID-HU]

  mensaje_exito_modo_ajuste: |
    ✅ AJUSTES COMPLETADOS: [ID-HU] (Iteración [N])
    
    📄 Artefacto actualizado: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md
    
    📊 Observaciones Resueltas:
    - [x] [observación_1]
    - [x] [observación_2]
    
    💡 Siguiente: >validar_hu [ID-HU] (re-validación)

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
  agente: "Arquitecto Onad"
  descripcion: "Validación arquitectónica de la HU refinada"
  accion_usuario: |
    Para continuar:
    1. Abre un nuevo chat con el agente **Arquitecto Onad**
    2. Ejecuta: `>validar_hu [ID-HU]`
```
