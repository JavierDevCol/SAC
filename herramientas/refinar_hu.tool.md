---
nombre: "Refinar Historia de Usuario"
comando: ">refinar_hu"
alias: [">refinar", ">hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Generar archivo de refinamiento ANTES de actualizar estado"
  - instruccion: "NUNCA aceptar criterios de aceptación no medibles"
  - instruccion: "Usar desglose VERTICAL (end-to-end), nunca horizontal"

reglas_arquitectonicas_requeridas:
  descripcion: "Si hay reglas arquitectónicas cargadas, considerar:"
  secciones:
    - seccion: "arquitectura.estilo"
      aplicar: "Alinear desglose técnico con arquitectura definida (Hexagonal, MVC, Capas)"
    - seccion: "testing.metodologia"
      aplicar: "Incluir criterios de aceptación alineados con metodología (TDD, BDD)"
    - seccion: "testing.cobertura_global"
      aplicar: "Mencionar cobertura esperada en estimación"
  si_no_existe: "Refinar sin restricciones arquitectónicas específicas"

condiciones_entrada:
  - condicion: "Usuario proporciona texto de HU"
    formato: "Como [rol], quiero [funcionalidad], para [beneficio]"
    si_no_cumple: "Solicitar HU en formato correcto"

parametros:
  opcionales:
    - nombre: proyecto
      tipo: string
      descripcion: "Proyecto destino (requerido en multi-proyecto, ignorado en mono)"
      defecto: null
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
    acciones:
      - "Establecer valores por defecto para parámetros opcionales no especificados: formato_estimacion='ambos', nivel_detalle='medio', incluir_riesgos=true, generar_tareas=true, incluir_testing=true"
      - "Mostrar resumen compacto de configuración activa:"
      - "  ⚙️ Configuración: nivel_detalle=[valor] | estimación=[valor] | riesgos=[sí/no] | tareas=[sí/no] | testing=[sí/no]"
      - "  Personaliza con: >refinar_hu --nivel_detalle alto --incluir_riesgos false"
    nota: "Garantiza evaluación correcta de condiciones y visibilidad de la configuración activa"

  - paso: "Detectar Tipo de Workspace"
    obligatorio: true
    acciones:
      - "Leer {{archivos.workspace}} y extraer campo 'Tipo'"
      - "SI Tipo='Multi-Proyecto':"
      - "  - SI parámetro 'proyecto' no especificado → PREGUNTAR proyecto destino"
      - "  - Validar proyecto existe en tabla de workspace.md"
      - "  - Cargar contexto desde {{artifacts.contextos_folder}}/[proyecto]_contexto.md"
      - "SI Tipo='Mono-Proyecto':"
      - "  - Ignorar parámetro 'proyecto', usar proyecto único"
      - "  - Cargar contexto desde {{artifacts.contextos_folder}}/[nombre]_contexto.md"
    si_error:
      proyecto_no_existe: "Proyecto '[proyecto]' no encontrado en workspace"

  - paso: "Detectar Modo de Operación"
    obligatorio: true
    acciones:
      - "Buscar refinamiento existente en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md"
      - "Si existe con feedback pendiente → MODO_AJUSTE"
      - "Si no existe → MODO_NUEVO"
      - "Extraer campo '- **Tipo:**' de la HU (SI no existe → asumir Funcional)"
      - "SI Tipo = Bug:"
      - "  1. Extraer campo 'Ref_Bug' de la HU → Cargar archivo de bug desde {{artifacts.bugs_folder}}/[BUG-NNN]*.md"
      - "  2. Pre-poblar desglose técnico con archivos afectados del bug"
      - "  3. Pre-poblar CA con: 'El bug BUG-NNN no se reproduce tras la corrección'"
      - "  4. SI el bug tiene sección 'Causa Raíz' → Incorporar como contexto técnico"
      - "  5. SI el bug tiene sección 'Corrección' → Incorporar como guía de implementación"
      - "  6. Reducir preguntas de clarificación (causa raíz ya documentada en el bug)"
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
      - "Generar {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md desde {{plantillas.refinamiento_hu}}"
      - "Rellenar Iteración: 1"
      - "Actualizar estado HU a [R] Refinada"
      - "Determinar proyecto de la HU:"
      - "  SI parámetro 'proyecto' especificado → usar ese valor"
      - "  SI Mono-Proyecto → usar nombre del proyecto único"
      - "  SI Multi-Proyecto sin parámetro → PREGUNTAR al usuario:"
      - "    '¿A qué proyecto(s) pertenece esta HU?'"
      - "    Proyectos disponibles:"
      - "      [1] backend_users"
      - "      [2] backend_orders"
      - "      [3] backend_payments"
      - "      [4] frontend_web"
      - "      [5] frontend_mobile"
      - "    Opciones de respuesta:"
      - "      • Número único: '2' → proyecto específico"
      - "      • Números separados por coma: '1,3' → proyectos seleccionados manualmente"
      - "      • 'AP' → analizar impacto en TODOS los proyectos"
      - "      • Números + AP: '1,2,3 AP' → analizar impacto solo entre los proyectos indicados"
      - "  Interpretación de respuestas:"
      - "    '2'       → Proyecto: backend_orders (directo, sin análisis)"
      - "    '1,3'     → Proyectos: backend_users, backend_payments (directo, compartida)"
      - "    'AP'      → Ejecutar análisis de impacto en los 5 proyectos"
      - "    '1,2,3 AP'→ Ejecutar análisis de impacto SOLO en backend_users, backend_orders, backend_payments"
      - "  SI respuesta contiene 'AP':"
      - "    1. Determinar scope de análisis:"
      - "       - Si solo 'AP' → todos los proyectos del workspace"
      - "       - Si 'N,M,... AP' → solo los proyectos indicados por números"
      - "    2. Leer contextos de proyectos en scope desde {{artifacts.contextos_folder}}/"
      - "    3. Analizar sección '## 6. Dependencias de Proyecto' de cada contexto"
      - "    4. Evaluar la HU contra:"
      - "       - Dominio/bounded context de cada proyecto"
      - "       - Stack tecnológico (¿la HU requiere tecnologías de qué proyecto?)"
      - "       - APIs/interfaces expuestas entre proyectos"
      - "       - Dependencias declaradas entre proyectos"
      - "    5. Presentar análisis al usuario:"
      - "       '📊 Análisis de Impacto para [ID-HU] (scope: [N proyectos]):'"
      - "       '- [proyecto_1]: ✅ AFECTADO - [razón]'"
      - "       '- [proyecto_2]: ❌ NO afectado'"
      - "       '- [proyecto_3]: ⚠️ POSIBLE - [razón de incertidumbre]'"
      - "    6. PREGUNTAR: '¿Confirmas estos proyectos? (S/N/Editar lista)'"
      - "  SI respuesta son solo números (sin AP):"
      - "    - Asignar directamente sin análisis"
      - "Poblar campo '- **Proyecto:**' con nombre del proyecto o 'compartida'"
      - "SI es compartida → Agregar sección '**Proyectos afectados:**' con lista de proyectos"
      - "SI Multi-Proyecto → Actualizar sección 'Resumen por Proyecto' en backlog"
    acciones_modo_ajuste:
      - "Actualizar refinamiento existente"
      - "Incrementar campo Iteración en Metadata"
      - "Marcar observaciones resueltas: [ ] → [x]"
      - "Agregar entrada en sección '## 7. Ajustes Aplicados'"

salida:
  archivos_generados:
    ruta: "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento_[concepto].md"
    plantilla: "{{plantillas.refinamiento_hu}}"
  archivos_actualizados: ["{{archivos.backlog}}"]
  estado_hu_final: "[R] Refinada"
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
