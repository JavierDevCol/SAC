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
  - instruccion: "Ejecutar tareas del plan en ORDEN ESTRICTO"
    nunca_saltar: true
  - instruccion: "DETENERSE INMEDIATAMENTE ante cualquier error"
    nunca_saltar: true
  - instruccion: "Solicitar CONFIRMACIÓN antes de comandos Git"
    nunca_saltar: true
  - instruccion: "NO improvisar ni saltar tareas del plan"
    nunca_saltar: true

identificacion:
  nombre: "Ejecutar Plan de Implementación"
  comando: ">ejecutar_plan"
  alias: [">ejecutar", ">implementar"]
  version: "4.0"

roles_autorizados:
  - ARCHDEV

prerequisitos:
  archivos_requeridos:
    - descripcion: "Plan de implementación generado por ONAD"
      ubicacion: "{{planes_location}}/[ID-HU]_plan_implementacion.md"
      estado_requerido: "[P] Planificada"
  archivos_opcionales:
    - "{{contexto_proyecto_location}}"
    - "{{reglas_arquitectonicas_location}}"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a implementar"
  opcionales:
    - nombre: modo_ejecucion
      tipo: string
      valores: [completo, fase_por_fase, tarea_por_tarea]
      defecto: fase_por_fase
    - nombre: auto_commit
      tipo: boolean
      defecto: false
      descripcion: "Solicitar confirmación antes de cada commit"

proceso:
  paso_1:
    nombre: "Cargar Plan de Implementación"
    obligatorio: true
    acciones:
      - "Buscar plan en {{planes_location}}"
      - "Parsear fases y tareas"
      - "Verificar estado [P] Planificada"
      - "Cambiar estado a [E] En Ejecución"
    si_error:
      no_encontrado: "❌ Plan no encontrado para [ID-HU]"
      estado_invalido: "⚠️ HU debe estar en estado [P] Planificada"

  paso_2:
    nombre: "Ejecutar Fases Secuencialmente"
    obligatorio: true
    acciones:
      - "Para cada fase del plan:"
      - "  1. Anunciar inicio de fase"
      - "  2. Ejecutar cada tarea en orden"
      - "  3. Validar resultado de cada tarea"
      - "  4. Marcar tarea como completada"
      - "  5. Si error: DETENER y reportar"
    comportamiento_error:
      accion: "DETENER ejecución inmediatamente"
      reportar: "Fase, tarea y error específico"
      sugerir: "Corrección o escalamiento"

  paso_3:
    nombre: "Crear/Modificar Archivos"
    obligatorio: true
    acciones:
      - "Crear archivos nuevos según especificación"
      - "Modificar archivos existentes"
      - "Aplicar convenciones del proyecto"
    validaciones:
      - "Código compila correctamente"
      - "Sigue estándares del proyecto"
      - "Imports correctos"

  paso_4:
    nombre: "Ejecutar Tests"
    obligatorio: true
    acciones:
      - "Ejecutar tests unitarios: mvn test"
      - "Verificar que todos pasen"
      - "Si fallan: DETENER y reportar"

  paso_5:
    nombre: "Solicitar Confirmación de Commit"
    obligatorio: true
    condicion: "si auto_commit=false"
    acciones:
      - "Mostrar resumen de cambios"
      - "Preguntar: ¿Proceder con commit?"
      - "Si NO: pausar para revisión"
      - "Si SÍ: sugerir >generar_commit"

  paso_6:
    nombre: "Finalización"
    obligatorio: true
    acciones:
      - "Cambiar estado HU a [X] Completada"
      - "Generar resumen de implementación"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Abrir/crear {{session_state_location}}"
      - "Registrar herramienta ejecutada: ejecutar_plan"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Actualizar estado de la HU ejecutada"
      - "Guardar cambios en session_state.json"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "ejecutar_plan"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"

salida:
  archivos_generados:
    - tipo: "registro_ejecucion"
      ruta: "{{ejecuciones_location}}/[ID-HU]_ejecucion_[timestamp].md"
  
  archivos_actualizados:
    - "{{backlog_location}}"
    - "{{session_state_location}}"
    - "Archivos de código según plan"
  
  estado_hu_final: "[X] Completada"
  
  mensaje_exito: |
    ✅ IMPLEMENTACIÓN COMPLETADA: [ID-HU]
    
    📊 Resumen:
    - Fases ejecutadas: [N/N]
    - Tareas completadas: [M/M]
    - Tests: ✅ Pasando
    
    💡 Siguiente: >generar_commit para documentar cambios

  mensaje_error: |
    ❌ EJECUCIÓN DETENIDA: [ID-HU]
    
    🔴 Error en: Fase [X], Tarea [Y]
    📋 Detalle: [descripción del error]
    
    💡 Acciones sugeridas:
    - [corrección específica]
    - O escalar a +ONAD para rediseño

manejo_errores:
  compilacion:
    accion: "DETENER"
    mensaje: "❌ Error de compilación"
    sugerir: "Revisar código generado"
  tests_fallidos:
    accion: "DETENER"
    mensaje: "❌ Tests fallando"
    sugerir: "Revisar lógica o actualizar tests"
  archivo_existente:
    accion: "PREGUNTAR"
    mensaje: "⚠️ Archivo ya existe"
    opciones: ["Sobrescribir", "Fusionar", "Omitir"]

errores:
  plan_no_encontrado:
    mensaje: "❌ Plan de implementación no encontrado"
    accion: "Ejecutar >planificar_hu [ID-HU] primero"
  estado_incorrecto:
    mensaje: "⚠️ HU no está en estado [P] Planificada"
    accion: "Verificar flujo: Refinada → Aprobada → Planificada"

siguiente:
  herramienta: "generar_commit"
  comando: ">generar_commit"
  rol_requerido: "ARTESANO"
  descripcion: "Documentar los cambios realizados"
```
