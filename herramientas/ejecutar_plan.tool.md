---
nombre: "Ejecutar Plan de Implementación"
comando: ">ejecutar_plan"
alias: [">ejecutar", ">implementar"]
version: "4.3"
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
    acciones:
      - "Para cada fase del plan:"
      - "  1. Anunciar inicio de fase"
      - "  2. Para cada tarea de la fase:"
      - "     a. EDITAR ARCHIVO del plan: cambiar [PENDIENTE] → [EN_PROGRESO] en la línea de la tarea"
      - "     b. Ejecutar los pasos de la tarea (crear/modificar código)"
      - "     c. Por cada paso completado: EDITAR ARCHIVO del plan cambiando '- [ ]' → '- [X]' en ese paso específico"
      - "     d. Al completar TODOS los pasos de la tarea: EDITAR ARCHIVO del plan cambiando [EN_PROGRESO] → [EJECUTADA]"
      - "     e. EDITAR ARCHIVO del plan: agregar fila en tabla 'Historial de Ejecución' con fecha, tarea y resultado"
      - "     f. Actualizar fila de la fase en tabla 'Progreso General': incrementar progreso [X/Y]"
    critico: "Los pasos c, d, e y f son BLOQUEANTES — NO avanzar a la siguiente tarea sin haber EDITADO el archivo del plan. Si el archivo no refleja el estado actual, la ejecución es inválida."
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
        actualizar: "EDITAR ARCHIVO del plan: cambiar estado de la tarea a [ERROR], agregar detalle en Historial"

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
      - "VERIFICAR: Leer archivo del plan y confirmar que TODAS las tareas están en [EJECUTADA] y TODOS los pasos en [X]"
      - "SI hay discrepancias: EDITAR ARCHIVO del plan para corregir estados pendientes ANTES de continuar"
      - "EDITAR ARCHIVO del plan: cambiar campo Estado en tabla Metadata → 'COMPLETADO'"
      - "Cambiar estado HU a [X] Completada en {{archivos.backlog}}"
      - "SI Multi-Proyecto → Actualizar contadores en sección 'Resumen por Proyecto'"
      - "Agregar entrada final en Historial de Ejecución (incluir columna Proyecto)"

actualizacion_tiempo_real:
  descripcion: "El archivo .md del plan DEBE ser editado (escritura en disco) en cada transición. NO es una anotación mental — es una operación de edición de archivo."
  instrucciones_imperativas:
    - "EDITAR ARCHIVO del plan al iniciar tarea: reemplazar texto '[PENDIENTE]' → '[EN_PROGRESO]' en la línea #### T[N]"
    - "EDITAR ARCHIVO del plan al completar paso: reemplazar texto '- [ ]' → '- [X]' en la línea del paso"
    - "EDITAR ARCHIVO del plan al completar tarea: reemplazar texto '[EN_PROGRESO]' → '[EJECUTADA]' en la línea #### T[N]"
    - "EDITAR ARCHIVO del plan al error: reemplazar estado actual → '[ERROR]' en la línea #### T[N]"
    - "EDITAR ARCHIVO del plan al finalizar: cambiar campo Estado en tabla Metadata a 'COMPLETADO'"
  frecuencia: "Después de CADA tarea, NO al final de todas las fases"
  verificacion: "Si al leer el plan las marcas no coinciden con lo ejecutado, DETENER y corregir antes de continuar"

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
