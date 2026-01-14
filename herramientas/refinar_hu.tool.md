---
nombre: "Refinar Historia de Usuario"
comando: ">refinar_hu"
alias: [">refinar", ">hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Pasos obligatorios NO se pueden omitir"
  - instruccion: "Generar archivo de refinamiento ANTES de actualizar estado"
  - instruccion: "NUNCA aceptar criterios de aceptación no medibles"
  - instruccion: "Usar desglose VERTICAL (end-to-end), nunca horizontal"
  - instruccion: "Generar en idioma: {{preferencias.idioma_documentacion}}"
  - instruccion: "Si {{usuario.incluir_firma_en_documentos}}=true, agregar pie: '---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---'"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Texto de la HU"
      formato: "Como [rol], quiero [funcionalidad], para [beneficio]"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"
    - "{{archivos.backlog}}"

parametros:
  opcionales:
    - {nombre: formato_estimacion, tipo: string, valores: [story_points, horas, ambos], defecto: ambos}
    - {nombre: nivel_detalle, tipo: string, valores: [alto, medio, bajo], defecto: medio}
    - {nombre: incluir_riesgos, tipo: boolean, defecto: true}
    - {nombre: generar_tareas, tipo: boolean, defecto: true}
    - {nombre: incluir_testing, tipo: boolean, defecto: true}

matriz_complejidad:
  bajo: {indicadores: "CRUD básico, sin integraciones", preguntas: "1-2", tareas: "3-5", sp: "2-3"}
  medio: {indicadores: "Lógica moderada, 1-2 integraciones", preguntas: "3-5", tareas: "5-10", sp: "5-8"}
  alto: {indicadores: "Múltiples integraciones, impacto arquitectónico", preguntas: "6-10+", tareas: "10-20", sp: "13+"}

criterios_smart:
  S: "Específico - qué debe ocurrir exactamente"
  M: "Medible - métricas verificables"
  A: "Alcanzable - realista en el sprint"
  R: "Relevante - relacionado con objetivo"
  T: "Temporal - condiciones de tiempo"

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: formato_estimacion='ambos', nivel_detalle='medio', incluir_riesgos=true, generar_tareas=true, incluir_testing=true"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Detectar Modo de Operación"
    obligatorio: true
    acciones: ["Buscar refinamiento existente en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md", "Si existe con feedback pendiente  MODO_AJUSTE", "Si no existe  MODO_NUEVO"]
    modo_ajuste: "Re-refinamiento enfocado en resolver observaciones de validación previa"
    modo_nuevo: "Refinamiento inicial de HU nueva"

  - paso: "Evaluación de Complejidad"
    obligatorio: true
    acciones: ["Analizar indicadores según matriz_complejidad", "Clasificar:  BAJO |  MEDIO |  ALTO", "Anunciar nivel al usuario"]

  - paso: "Preguntas de Clarificación"
    obligatorio: true
    acciones: ["Identificar ambigüedades en narrativa", "Generar preguntas priorizadas (Alta/Media/Baja)", "Alta: afectan estimación | Media: mejoran UX | Baja: detalles impl"]

  - paso: "Refinamiento de Criterios de Aceptación"
    obligatorio: true
    acciones: ["Aplicar criterios_smart a cada CA", "Reformular CA ambiguos", "Agregar CA faltantes (error, validación, performance)"]

  - paso: "Desglose Técnico Vertical"
    obligatorio: true
    condicion: "generar_tareas=true"
    acciones: ["Identificar slices end-to-end mínimos", "Generar tareas por slice (frontendapiserviciopersistenciatesting)", "Asignar IDs: HU-XXX-UI-01, HU-XXX-API-01"]

  - paso: "Estrategia y Estimación"
    obligatorio: true
    acciones: ["Recomendar enfoque (TDD, incremental, feature toggle)", "Calcular Story Points con justificación", "Desglosar: complejidad + incertidumbre + riesgo"]

  - paso: "Análisis de Riesgos"
    obligatorio: true
    condicion: "incluir_riesgos=true"
    acciones: ["Identificar bloqueadores potenciales", "Proponer mitigaciones", "Detectar dependencias de otras HUs"]

  - paso: "Persistencia del Refinamiento"
    obligatorio: true
    acciones_modo_nuevo:
      - "Crear {{archivos.backlog}} desde {{plantillas.backlog}} si no existe"
      - "Generar {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md"
      - "Actualizar estado HU a [R] Refinada"
    acciones_modo_ajuste:
      - "Actualizar refinamiento existente"
      - "Marcar observaciones resueltas: [ ]  [x]"
      - "Agregar sección '##  Ajustes Aplicados (Iteración N)'"

salida:
  archivos_generados:
    ruta: "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md"
  archivos_actualizados: ["{{archivos.backlog}}"]
  estado_hu_final: "[R] Refinada"
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
  mensaje_exito: |
     REFINAMIENTO COMPLETADO: [ID-HU]
     Artefacto: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md
     CA: [X] mejorados + [Y] nuevos | SP: [Z] | Riesgos: [N]
     Siguiente: >validar_hu [ID-HU]

errores:
  hu_mal_formateada: {msg: " HU incompleta o mal formateada", accion: "Solicitar formato: Como [rol], quiero [func], para [beneficio]"}
  sin_criterios: {msg: "ℹ HU sin criterios de aceptación", accion: "Generar CA básicos inferidos, solicitar validación"}
  hu_muy_grande: {msg: " HU tamaño épica detectada", accion: "Sugerir partición en HUs más pequeñas"}

siguiente:
  - {comando: ">validar_hu [ID-HU]", desc: "Validación arquitectónica de la HU refinada", chat_agente: "Arquitecto Onad"}
```
