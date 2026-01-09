```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Ejecutar tareas del plan en ORDEN ESTRICTO"
    nunca_saltar: true
  - instruccion: "DETENERSE INMEDIATAMENTE ante cualquier error"
    nunca_saltar: true
  - instruccion: "Solicitar CONFIRMACIÓN antes de comandos Git"
    nunca_saltar: true
  - instruccion: "NO improvisar ni saltar tareas del plan"
    nunca_saltar: true
  - instruccion: "Generar documentación en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true
  - instruccion: "ACTUALIZAR el plan de implementación EN TIEMPO REAL según {{plantillas.plan_implementacion}}"
    nunca_saltar: true
  - instruccion: "Marcar pasos completados [ ] → [X] inmediatamente después de ejecutar"
    nunca_saltar: true
  - instruccion: "Cambiar estados de tareas: [PENDIENTE] → [EN_PROGRESO] → [EJECUTADA]"
    nunca_saltar: true

identificacion:
  nombre: "Ejecutar Plan de Implementación"
  comando: ">ejecutar_plan"
  alias: [">ejecutar", ">implementar"]
  version: "4.0"

prerequisitos:
  archivos_requeridos:
    - descripcion: "Plan de implementación generado por ONAD"
      ubicacion: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      estado_requerido: "[P] Planificada"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"
    - "{{archivos.reglas_arquitectonicas}}"

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
      - "Buscar plan en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      - "Verificar que sigue estructura de {{plantillas.plan_implementacion}}"
      - "Parsear fases, tareas y pasos"
      - "Verificar estado [P] Planificada en {{archivos.backlog}}"
      - "Cambiar estado HU a [E] En Ejecución en {{archivos.backlog}}"
      - "Actualizar campo 'Estado' en Metadata del plan a 'EN_PROGRESO'"
      - "Actualizar campo 'Última actualización' en Metadata"
    si_error:
      no_encontrado: "❌ Plan no encontrado para [ID-HU]"
      estado_invalido: "⚠️ HU debe estar en estado [P] Planificada"
    plantilla_referencia: "{{plantillas.plan_implementacion}}"

  paso_2:
    nombre: "Ejecutar Fases Secuencialmente"
    obligatorio: true
    acciones:
      - "Para cada fase del plan:"
      - "  1. Anunciar inicio de fase"
      - "  2. Actualizar estado de fase en tabla 'Progreso General'"
      - "  3. Para cada tarea de la fase:"
      - "     a. Cambiar estado tarea: [PENDIENTE] → [EN_PROGRESO]"
      - "     b. Ejecutar cada paso de la tarea"
      - "     c. Al completar paso: marcar [ ] → [X]"
      - "     d. Al completar tarea: cambiar a [EJECUTADA]"
      - "     e. Agregar entrada en 'Historial de Ejecución'"
      - "  4. Si error: DETENER, marcar tarea como [ERROR], reportar"
    actualizacion_plan:
      cuando: "Después de CADA paso completado"
      campos:
        - "Checkbox del paso: [ ] → [X]"
        - "Estado de tarea si aplica"
        - "Tabla 'Progreso General'"
        - "'Última actualización' en Metadata"
    comportamiento_error:
      accion: "DETENER ejecución inmediatamente"
      actualizar_plan:
        - "Marcar tarea como [ERROR]"
        - "Agregar detalle en 'Historial de Ejecución'"
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
    nombre: "Validar Criterios de Aceptación"
    obligatorio: true
    acciones:
      - "Revisar sección 'Fase Final: Validar Criterios de Aceptación' del plan"
      - "Para cada criterio de aceptación:"
      - "  1. Verificar que se cumple"
      - "  2. Marcar [ ] → [X] en el plan"
      - "  3. Marcar [ ] → [X] en la HU original"
      - "Si algún criterio NO se cumple: DETENER y reportar"

  paso_6:
    nombre: "Solicitar Confirmación de Commit"
    obligatorio: true
    condicion: "si auto_commit=false"
    acciones:
      - "Mostrar resumen de cambios"
      - "Preguntar: ¿Proceder con commit?"
      - "Si NO: pausar para revisión"
      - "Si SÍ: sugerir >generar_commit"

  paso_7:
    nombre: "Finalización"
    obligatorio: true
    acciones:
      - "Actualizar estado del plan a 'COMPLETADO' en Metadata"
      - "Actualizar 'Última actualización' en Metadata"
      - "Cambiar estado HU a [X] Completada en {{archivos.backlog}}"
      - "Agregar entrada final en 'Historial de Ejecución'"

salida:
  archivos_actualizados:
    - ruta: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      descripcion: "Plan actualizado con progreso en tiempo real"
    - ruta: "{{archivos.backlog}}"
      descripcion: "Estado de HU actualizado"
    - descripcion: "Archivos de código según plan"
  
  estado_hu_final: "[X] Completada"
  
  mensaje_exito: |
    ✅ IMPLEMENTACIÓN COMPLETADA: [ID-HU]
    
    📊 Resumen:
    - Fases ejecutadas: [N/N]
    - Tareas completadas: [M/M]
    - Criterios de Aceptación: [Y/Y] ✅
    - Tests: ✅ Pasando
    
    📄 Plan actualizado: {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
    
    💡 Siguiente: >generar_commit para documentar cambios

  mensaje_error: |
    ❌ EJECUCIÓN DETENIDA: [ID-HU]
    
    🔴 Error en: Fase [X], Tarea [Y]
    📋 Detalle: [descripción del error]
    
    📄 Plan actualizado con estado de error
    
    💡 Acciones sugeridas:
    - Revisar el plan para ver progreso actual
    - [corrección específica]
    - O escalar a +ONAD para rediseño

actualizacion_plan_tiempo_real:
  descripcion: "El plan de implementación se actualiza conforme se ejecuta"
  plantilla_referencia: "{{plantillas.plan_implementacion}}"
  campos_a_actualizar:
    al_iniciar_tarea:
      - "Estado de tarea: [PENDIENTE] → [EN_PROGRESO]"
    al_completar_paso:
      - "Checkbox: [ ] → [X]"
      - "'Última actualización' en Metadata"
    al_completar_tarea:
      - "Estado de tarea: [EN_PROGRESO] → [EJECUTADA]"
      - "Entrada en 'Historial de Ejecución'"
      - "Progreso en tabla 'Progreso General'"
    al_error:
      - "Estado de tarea: → [ERROR]"
      - "Detalle en 'Historial de Ejecución'"
    al_finalizar:
      - "Estado en Metadata: 'COMPLETADO'"
      - "Todos los criterios de aceptación marcados"
  beneficio: |
    Si el usuario cierra el chat, puede retomar la ejecución
    leyendo el plan y continuando desde la última tarea completada.

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
  agente: "Artesano de Commits"
  descripcion: "Documentar los cambios realizados"
  accion_usuario: |
    Para continuar:
    1. Abre un nuevo chat con el agente **Artesano de Commits**
    2. Ejecuta: `>generar_commit`
```
