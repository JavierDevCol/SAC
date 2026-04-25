---
nombre: "Ejecutar Plan de Implementación"
comando: ">ejecutar_plan"
alias: [">ejecutar", ">implementar"]
version: "4.2"
---

```yaml
mandatory:
  - instruccion: "Ejecutar tareas del plan en ORDEN ESTRICTO"
  - instruccion: "DETENERSE INMEDIATAMENTE ante cualquier error"
  - instruccion: "Solicitar CONFIRMACIÓN antes de comandos Git"
  - instruccion: "NO improvisar ni saltar tareas del plan"
  - instruccion: "ACTUALIZAR plan EN TIEMPO REAL: [ ]  [X], estados de tareas"
  - instruccion: "Estados de tareas: [PENDIENTE]  [EN_PROGRESO]  [EJECUTADA]"

reglas_arquitectonicas_requeridas:
  descripcion: "Si hay reglas arquitectónicas cargadas, aplicar:"
  secciones:
    - seccion: "nomenclatura.*"
      aplicar: "Nombrar clases, métodos, variables según convenciones definidas"
    - seccion: "arquitectura.estructura"
      aplicar: "Crear archivos en carpetas según estructura definida (domain/, application/, infrastructure/)"
    - seccion: "patrones.obligatorios"
      aplicar: "Usar patrones requeridos (Repository, Factory, Builder, etc.)"
    - seccion: "patrones.prohibidos"
      aplicar: "NUNCA usar patrones prohibidos (Singleton, Service Locator, etc.)"
    - seccion: "principios.inmutabilidad"
      aplicar: "Usar final/readonly/const según política"
    - seccion: "principios.null_policy"
      aplicar: "Manejar nulls según política (Optional, Null Object, etc.)"
    - seccion: "calidad.max_*"
      aplicar: "Respetar límites de líneas por método/clase/parámetros"
  si_no_existe: "Usar mejores prácticas estándar del stack detectado"

condiciones_entrada:
  - condicion: "HU en estado [P] Planificada con plan generado"
    si_no_cumple: "Ejecutar >planificar_hu primero"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a implementar"
  opcionales:
    - nombre: proyecto
      tipo: string
      descripcion: "Proyecto específico (auto-detectado desde campo Proyecto de la HU)"
      defecto: null
    - nombre: modo_ejecucion
      tipo: string
      valores: [completo, fase_por_fase, tarea_por_tarea]
      defecto: fase_por_fase
    - nombre: auto_commit
      tipo: boolean
      defecto: false

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones:
      - "Establecer valores por defecto para parámetros opcionales no especificados: modo_ejecucion='fase_por_fase', auto_commit=false"
      - "Mostrar resumen compacto de configuración activa:"
      - "  ⚙️ Configuración: modo_ejecucion=[valor] | auto_commit=[valor]"
      - "  Personaliza con: >ejecutar_plan [ID-HU] --modo_ejecucion completo --auto_commit true"
    nota: "Garantiza evaluación correcta de condiciones y visibilidad de la configuración activa"
    validaciones_combinacion:
      - si: "modo_ejecucion=completo AND auto_commit=true"
        accion: "⛔ Combinación prohibida. Usar fase_por_fase con auto_commit, o completo sin auto_commit"
        razon: "Ejecutar todo sin pausas Y con commit automático elimina toda supervisión humana"

  - paso: "Cargar Plan de Implementación"
    obligatorio: true
    acciones:
      - "Buscar plan en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      - "Verificar estructura según {{plantillas.plan_implementacion}}"
      - "Verificar estado [P] Planificada en {{archivos.backlog}}"
      - "Extraer campo '- **Proyecto:**' de la HU"
      - "SI Proyecto = 'compartida':"
      - "  1. Leer sección '**Proyectos afectados:**' de la HU (lista de proyectos)"
      - "  2. Ejecutar tareas en el directorio de cada proyecto según corresponda"
      - "SI Multi-Proyecto → Establecer directorio base del proyecto como CWD"
      - "Cambiar estado HU a [E] En Ejecución"
      - "Actualizar Metadata del plan: Estado  EN_PROGRESO"
    si_error:
      no_encontrado: " Plan no encontrado. Ejecutar >planificar_hu primero"
      estado_invalido: " HU debe estar en estado [P] Planificada"

  - paso: "Validar Entorno de Ejecución"
    obligatorio: true
    acciones:
      - "Verificar rama Git activa coincide con rama esperada para la HU"
      - "Verificar directorio del proyecto existe y es accesible"
      - "Detectar framework de tests disponible (mvn/npm/pytest/vitest/jest/dotnet test/etc.)"
      - "Verificar dependencias instaladas (node_modules, venv, .m2, etc.)"
      - "Crear punto de restauración: git stash push -m 'backup/[ID-HU]_pre_ejecucion' (si hay cambios sin commit)"
    si_error:
      entorno_invalido: "⛔ Entorno no preparado. Detallar requisitos faltantes antes de continuar"
      sin_framework_tests: "⚠️ No se detectó framework de tests. Confirmar con usuario antes de continuar"

  - paso: "Ejecutar Fases Secuencialmente"
    obligatorio: true
    acciones: ["Para cada fase del plan: 1. Anunciar inicio de fase", "2. Para cada tarea: [PENDIENTE]  [EN_PROGRESO]", "3. Ejecutar pasos, marcar [ ]  [X] al completar", "4. Al completar tarea: [EN_PROGRESO]  [EJECUTADA]", "5. Agregar entrada en Historial de Ejecución"]
    reanudacion:
      descripcion: "Si el plan tiene tareas [EJECUTADA], saltar a la primera tarea [PENDIENTE]"
      acciones:
        - "Verificar que los archivos generados por tareas [EJECUTADA] existen en el filesystem"
        - "Si algún archivo falta, marcar la tarea como [PENDIENTE] y re-ejecutarla"
        - "Informar al usuario: 'Reanudando desde tarea T[N] — [X] tareas ya completadas'"
    max_reintentos_por_tarea: 2
    si_max_reintentos:
      accion: "DETENER. La tarea T[N] falló [max_reintentos] veces consecutivas"
      sugerencia: "Revisar manualmente y ejecutar >ejecutar_plan [ID-HU] --modo_ejecucion tarea_por_tarea"
    si_error:
      cualquier_error:
        accion: "DETENER inmediatamente"
        actualizar: "Marcar tarea como [ERROR], agregar detalle en Historial"

  - paso: "Crear/Modificar Archivos"
    obligatorio: true
    acciones: [Crear archivos nuevos, Modificar existentes, Aplicar convenciones]
    validaciones:
      - condicion: "Código compila correctamente"
        si_no_cumple: "DETENER y reportar error de compilación"

  - paso: "Ejecutar Tests"
    obligatorio: true
    acciones: ["Ejecutar tests: mvn test / npm test / pytest", "Verificar todos pasan"]
    si_error:
      tests_fallidos: " DETENER. Revisar lógica o actualizar tests"

  - paso: "Validar Criterios de Aceptación"
    obligatorio: true
    acciones: ["Para cada criterio de aceptación: 1. Verificar cumplimiento", "2. Marcar [ ]  [X] en plan Y en HU original"]
    si_error:
      criterio_no_cumplido: " DETENER. Criterio [X] no cumplido"

  - paso: "Confirmación de Commit"
    obligatorio: true
    condicion: "si auto_commit=false"
    acciones: ["Mostrar resumen de cambios", "Preguntar: ¿Proceder con commit?", "Si NO: pausar para revisión", "Si SÍ: sugerir >generar_commit"]

  - paso: "Finalización"
    obligatorio: true
    acciones:
      - "Actualizar Metadata del plan: Estado  COMPLETADO"
      - "Cambiar estado HU a [X] Completada en {{archivos.backlog}}"
      - "SI Multi-Proyecto → Actualizar contadores en sección 'Resumen por Proyecto'"
      - "Agregar entrada final en Historial de Ejecución (incluir columna Proyecto)"

actualizacion_tiempo_real:
  descripcion: "Plan se actualiza conforme se ejecuta para permitir retomar si se interrumpe"
  al_iniciar_tarea: "[PENDIENTE]  [EN_PROGRESO]"
  al_completar_paso: "[ ]  [X]"
  al_completar_tarea: "[EN_PROGRESO]  [EJECUTADA] + entrada en Historial"
  al_error: " [ERROR] + detalle en Historial"
  al_finalizar: "Metadata Estado  COMPLETADO"

salida:
  archivos_actualizados:
    - ruta: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
    - ruta: "{{archivos.backlog}}"
    - descripcion: "Archivos de código según plan"
  estado_hu_final: "[C] Completada"
  mensaje_exito: |
     IMPLEMENTACIÓN COMPLETADA: [ID-HU]
    
     Resumen:
    - Fases: [N/N] 
    - Tareas: [M/M] 
    - Criterios de Aceptación: [Y/Y] 
    - Tests:  Pasando

errores:
  plan_no_encontrado: {msg: " Plan no encontrado", accion: "Ejecutar >planificar_hu primero"}
  estado_incorrecto: {msg: " HU no está en [P] Planificada", accion: "Verificar flujo de estados"}
  compilacion: {msg: " Error de compilación", accion: "Revisar código generado"}
  tests_fallidos: {msg: " Tests fallando", accion: "Revisar lógica o tests"}
  archivo_existente: {msg: " Archivo ya existe", opciones: [Sobrescribir, Fusionar, Omitir]}

siguiente:
  - {comando: ">generar_commit", desc: "Documentar cambios realizados", chat_agente: "Cronista de Cambios"}
```
