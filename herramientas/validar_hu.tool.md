---
nombre: "Validar Historia de Usuario"
comando: ">validar_hu"
alias: [">validar", ">aprobar_hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Verificar alineación con reglas arquitectónicas del proyecto"
  - instruccion: "NO aprobar HU que violen principios arquitectónicos"
  - instruccion: "Documentar razones de rechazo o ajustes requeridos"

condiciones_entrada:
  - condicion: "HU en estado [R] Refinada"
    si_no_cumple: "Ejecutar >refinar_hu primero"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a validar"
  opcionales:
    - {nombre: nivel_validacion, tipo: string, valores: [basico, completo, exhaustivo], defecto: completo}

veredictos:
  aprobada: {estado: "[A] Aprobada", siguiente: ">planificar_hu [ID-HU]"}
  ajustes: {estado: "[R] Refinada + observaciones", siguiente: ">refinar_hu [ID-HU]"}
  rechazada: {estado: "[B] Bloqueada", siguiente: "Requiere rediseño significativo"}

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: nivel_validacion='completo'"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Cargar HU y Contexto"
    obligatorio: true
    acciones: 
      - "Buscar HU en backlog"
      - "Verificar estado [R] Refinada"
      - "Cargar refinamiento desde {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md"
      - "SI HU tiene campo ADR_Ref → Cargar ADR referenciado desde {{artifacts.adr_folder}}"
    si_error:
      no_encontrada: "HU [id_hu] no encontrada en backlog"
      estado_invalido: "HU debe estar en estado [R] Refinada"

  - paso: "Detección de Ambigüedades"
    obligatorio: true
    descripcion: "NUNCA asumir. Ante cualquier duda, preguntar al usuario."
    acciones:
      - "Analizar HU y CA buscando: términos vagos, información faltante, contradicciones, casos no cubiertos"
      - "SI se detectan ambigüedades → Listar preguntas claras y específicas"
      - "PAUSAR y esperar respuestas del usuario antes de continuar"
      - "Incorporar respuestas al contexto de validación"
    comportamiento:
      si_hay_dudas: "PREGUNTAR y ESPERAR respuesta"
      si_no_hay_dudas: "Continuar al siguiente paso"
    ejemplo_preguntas:
      - "El CA dice 'respuesta rápida' — ¿Cuál es el tiempo máximo aceptable en ms?"
      - "¿El usuario debe estar autenticado para esta funcionalidad?"
      - "¿Qué debe ocurrir si [caso X] falla?"

  - paso: "Validación contra ADR"
    obligatorio: false
    condicion: "HU tiene ADR_Ref definido (no 'ninguno')"
    acciones:
      - "Leer sección '## Decisión' del ADR referenciado"
      - "Verificar que la HU implementa la decisión correctamente"
      - "Detectar contradicciones entre HU y ADR"
      - "SI hay contradicción → Agregar a observaciones de validación"
    checklist: ["HU alineada con decisión del ADR", "No contradice consecuencias documentadas"]

  - paso: "Validación de Criterios de Aceptación"
    obligatorio: true
    acciones: ["Verificar CA medibles (SMART)", "Detectar ambigüedades residuales", "Validar cobertura de casos de error"]
    checklist: ["CA específicos y verificables", "Casos de error contemplados", "Performance considerado si aplica"]

  - paso: "Validación Arquitectónica"
    obligatorio: true
    nota: "Valida la HU como REQUISITO, no define implementación (eso es planificar_hu)"
    acciones:
      - "Verificar que la funcionalidad propuesta encaja en arquitectura existente"
      - "Detectar si los CA fuerzan implementaciones que violarían patrones"
      - "Evaluar si la HU introduce responsabilidades que no corresponden a su dominio"
      - "Aplicar reglas_arquitectonicas si están disponibles"
    checklist:
      - "La funcionalidad respeta la separación de responsabilidades del proyecto"
      - "Los CA no imponen decisiones técnicas que violen la arquitectura"
      - "No cruza boundaries entre módulos/capas indebidamente"
      - "Es coherente con el contexto técnico documentado"
      - "No contradice decisiones arquitectónicas previas (ADRs)"

  - paso: "Análisis de Viabilidad Técnica"
    obligatorio: true
    acciones: ["Evaluar complejidad de implementación", "Identificar riesgos técnicos", "Validar estimación propuesta"]

  - paso: "Emisión de Veredicto"
    obligatorio: true
    acciones: ["Determinar resultado: APROBADA | AJUSTES | RECHAZADA", "Documentar razones detalladas", "Actualizar estado según veredictos"]

  - paso: "Persistir Feedback"
    obligatorio: true
    condicion: "resultado == AJUSTES"
    acciones: ["Agregar sección '## Feedback de Validación' en refinamiento", "Incluir fecha, iteración, observaciones pendientes", "Marcar como [ ] pendientes de resolver"]

salida:
  archivos_actualizados: ["{{archivos.backlog}}", "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md (si AJUSTES)"]
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
  mensaje_aprobada: |
     HU APROBADA: [ID-HU]
     Validaciones:  CA |  Arquitectura |  Viabilidad
     Siguiente: >planificar_hu [ID-HU]
  mensaje_ajustes: |
     HU REQUIERE AJUSTES: [ID-HU]
     Feedback en: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md
     Siguiente: >refinar_hu [ID-HU] (Refinador HU)

errores:
  hu_no_encontrada: {msg: " HU [id_hu] no encontrada", accion: "Verificar ID y ejecutar *HU para listar"}
  estado_incorrecto: {msg: " HU no está en estado [R] Refinada", accion: "Ejecutar >refinar_hu primero"}
  sin_reglas: {msg: "ℹ Sin reglas arquitectónicas", accion: "Validación basada en mejores prácticas generales"}

siguiente:
  - {comando: ">planificar_hu [ID-HU]", desc: "Si APROBADA - crear plan de implementación", chat_agente: "Arquitecto Onad"}
  - {comando: ">refinar_hu [ID-HU]", desc: "Si AJUSTES - aplicar observaciones", chat_agente: "Refinador HU"}
```
