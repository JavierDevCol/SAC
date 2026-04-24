---
nombre: "Sincronizar Backlog"
comando: ">sincronizar_backlog"
alias: [">sync_backlog", ">sync"]
version: "1.0"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
  - instruccion: "Nunca saltar proceso.paso_final"
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
  - instruccion: "NUNCA modificar estados sin evidencia en artefactos"
  - instruccion: "Mostrar reporte de discrepancias ANTES de aplicar cambios"
  - instruccion: "Solicitar confirmación del usuario antes de sobrescribir estados en el backlog"

condiciones_entrada:
  - condicion: "Existe {{archivos.backlog}}"
    si_no_cumple: "No hay backlog que sincronizar. Ejecutar >refinar_hu para crear la primera HU."

parametros:
  opcionales:
    - nombre: id_hu
      tipo: string
      descripcion: "Sincronizar solo una HU específica. Si se omite, sincroniza todas."
      defecto: null
    - nombre: proyecto
      tipo: string
      descripcion: "Filtrar HUs de un proyecto específico (solo multi-proyecto)"
      defecto: null
    - nombre: auto
      tipo: flag
      descripcion: "Aplicar correcciones sin pedir confirmación (usar con precaución)"
    - nombre: dry_run
      tipo: flag
      descripcion: "Solo mostrar reporte sin aplicar cambios"

# ============================================
# LÓGICA DE DEDUCCIÓN DE ESTADOS
# ============================================
# La fuente de verdad son los ARTEFACTOS en disco,
# no el estado registrado en el backlog.
# ============================================
reglas_deduccion:
  descripcion: "Cada HU del backlog se evalúa contra la existencia y contenido de sus artefactos"
  estados:
    pendiente:
      condicion: "NO existe archivo en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md"
      estado_deducido: "[ ] Pendiente"

    refinada:
      condicion: >
        EXISTE archivo en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md
        AND NO contiene sección '## Aprobación' con campo '**Estado** | ✅ Aprobada'
        AND NO existe archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
      estado_deducido: "[R] Refinada"

    aprobada:
      condicion: >
        EXISTE archivo en {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md
        AND CONTIENE sección '## Aprobación' con campo '**Estado** | ✅ Aprobada'
        AND NO existe archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
      estado_deducido: "[A] Aprobada"

    planificada:
      condicion: >
        EXISTE archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
        AND campo Metadata 'Estado' == 'PENDIENTE'
      estado_deducido: "[P] Planificada"

    en_ejecucion:
      condicion: >
        EXISTE archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
        AND campo Metadata 'Estado' == 'EN_PROGRESO'
      estado_deducido: "[E] En Ejecución"

    completada:
      condicion: >
        EXISTE archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
        AND campo Metadata 'Estado' == 'COMPLETADO'
      estado_deducido: "[X] Completada"

    bloqueada:
      condicion: >
        EXISTE archivo en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
        AND campo Metadata 'Estado' == 'BLOQUEADO'
      estado_deducido: "[B] Bloqueada"

  prioridad_evaluacion: >
    Las reglas se evalúan en orden: completada → bloqueada → en_ejecucion → planificada → aprobada → refinada → pendiente.
    La primera regla que coincida determina el estado deducido.

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones:
      - "Establecer valores por defecto: id_hu=null, proyecto=null, auto=false, dry_run=false"
      - "Mostrar resumen compacto de configuración activa:"
      - "  ⚙️ Configuración: hu=[todas] | proyecto=[todos] | auto=[no] | dry_run=[no]"
      - "  Personaliza con: >sincronizar_backlog --id_hu HU-001 --dry_run"
    nota: "Garantiza evaluación correcta de condiciones y visibilidad de la configuración activa"

  - paso: "Cargar Backlog"
    obligatorio: true
    acciones:
      - "Leer {{archivos.backlog}}"
      - "Extraer todas las HUs registradas (buscar patrón: ### [ID-HU]: [Título])"
      - "Para cada HU extraer: ID, Título, Tipo (SI no existe → asumir Funcional), Estado actual, Proyecto, Ref_Bug (si Tipo=Bug)"
      - "SI parámetro id_hu → Filtrar solo esa HU"
      - "SI parámetro proyecto → Filtrar HUs de ese proyecto"
    si_error:
      backlog_no_encontrado: "❌ No se encontró {{archivos.backlog}}"
      backlog_vacio: "ℹ️ Backlog sin HUs registradas. Nada que sincronizar."

  - paso: "Escanear Artefactos por HU"
    obligatorio: true
    acciones:
      - "Para cada HU del paso anterior:"
      - "  1. Buscar refinamiento: {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md"
      - "  2. SI existe refinamiento → Buscar sección '## Aprobación' con '**Estado** | ✅ Aprobada'"
      - "  3. Buscar plan: {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      - "  4. SI existe plan → Leer campo '| **Estado** |' de la tabla Metadata"
      - "  5. Aplicar reglas_deduccion según prioridad_evaluacion"
      - "  6. Registrar: {id, estado_backlog, estado_deducido, artefactos_encontrados}"

  - paso: "Generar Reporte de Discrepancias"
    obligatorio: true
    acciones:
      - "Comparar estado_backlog vs estado_deducido para cada HU"
      - "Clasificar cada HU en:"
      - "  ✅ SINCRONIZADA — estado_backlog == estado_deducido"
      - "  ⚠️ DESINCRONIZADA — estado_backlog != estado_deducido"
      - "  ❓ HUÉRFANA — HU en backlog sin ningún artefacto (y no es Pendiente)"
      - "Mostrar reporte al usuario:"
      - ""
      - "  📊 Reporte de Sincronización"
      - "  ════════════════════════════"
      - "  Total HUs escaneadas: [N]"
      - "  ✅ Sincronizadas: [X]"
      - "  ⚠️ Desincronizadas: [Y]"
      - "  ❓ Huérfanas: [Z]"
      - ""
      - "  ⚠️ Discrepancias Encontradas:"
      - "  | HU | Estado Backlog | Estado Real | Artefacto Evidencia |"
      - "  |----|---------------|-------------|---------------------|"
      - "  | [ID] | [estado actual] | [estado deducido] | [ruta artefacto] |"
      - ""
      - "SI dry_run=true → Mostrar reporte y TERMINAR (no aplicar cambios)"

  - paso: "Solicitar Confirmación"
    obligatorio: true
    condicion: "auto=false AND dry_run=false AND hay discrepancias"
    acciones:
      - "Preguntar al usuario:"
      - "  🤷 ¿Aplicar las correcciones?"
      - "  ✅ [S] Sí, aplicar todas"
      - "  🔍 [P] Seleccionar cuáles aplicar"
      - "  ❌ [N] No aplicar cambios"
      - "SI respuesta = 'P' → Mostrar lista numerada y solicitar selección"

  - paso: "Aplicar Correcciones al Backlog"
    obligatorio: true
    condicion: "dry_run=false AND (auto=true OR usuario confirmó)"
    acciones:
      - "Para cada HU a corregir:"
      - "  1. Buscar la sección ### [ID-HU] en el backlog"
      - "  2. Actualizar campo '- **Estado:**' al estado deducido"
      - "  3. Actualizar campos adicionales según plantilla del estado destino:"
      - "     - [R] Refinada: agregar Refinamiento, Fecha refinamiento, Estimación"
      - "     - [A] Aprobada: agregar Fecha aprobación, Aprobado por (de sección Aprobación del refinamiento)"
      - "     - [P] Planificada: agregar Plan, Fecha planificación"
      - "     - [E] En Ejecución: agregar Inicio ejecución, Progreso, Sección actual"
      - "     - [X] Completada: agregar Completado, Duración"
      - "  4. SI Multi-Proyecto → Recalcular contadores en 'Resumen por Proyecto'"
      - "  5. Recalcular contadores en 'Resumen de Estados'"

  - paso: "Reporte Final"
    obligatorio: true
    acciones:
      - "Mostrar resumen de cambios aplicados"
      - "Actualizar campo 'Última Actualización' del backlog con timestamp actual"

# ============================================
# SALIDA
# ============================================
salida:
  archivos_actualizados:
    - ruta: "{{archivos.backlog}}"
  mensaje_exito: |
    ✅ SINCRONIZACIÓN COMPLETADA

    📊 Resumen:
    - HUs escaneadas: [N]
    - Correcciones aplicadas: [X]
    - Sin cambios: [Y]

    📄 Backlog actualizado: {{archivos.backlog}}

# ============================================
# ERRORES
# ============================================
errores:
  backlog_no_encontrado: {msg: "❌ Backlog no encontrado", accion: "Ejecutar >refinar_hu para crear la primera HU y generar el backlog"}
  hu_no_encontrada: {msg: "❌ HU [id_hu] no encontrada en backlog", accion: "Verificar ID con la lista de HUs del backlog"}
  artefacto_corrupto: {msg: "⚠️ Artefacto de [ID-HU] no tiene estructura esperada", accion: "Revisar manualmente el archivo indicado"}
  estado_ambiguo: {msg: "⚠️ No se pudo deducir estado de [ID-HU]", accion: "Los artefactos no coinciden con ninguna regla. Revisar manualmente."}

# ============================================
# SIGUIENTE
# ============================================
siguiente:
  - {comando: ">refinar_hu [ID-HU]", desc: "Refinar HUs que estén en estado Pendiente", chat_agente: "Refinador HU"}
  - {comando: ">validar_hu [ID-HU]", desc: "Validar HUs Refinadas pendientes de aprobación", chat_agente: "Arquitecto Onad"}
  - {comando: ">planificar_hu [ID-HU]", desc: "Planificar HUs Aprobadas", chat_agente: "Arquitecto Onad"}
```
