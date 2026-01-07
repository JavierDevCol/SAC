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
  - instruccion: "Verificar alineación con reglas arquitectónicas del proyecto"
    nunca_saltar: true
  - instruccion: "NO aprobar HU que violen principios arquitectónicos"
    nunca_saltar: true
  - instruccion: "Documentar razones de rechazo o ajustes requeridos"
    nunca_saltar: true
  - instruccion: "Generar documentación en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Validar Historia de Usuario"
  comando: ">validar_hu"
  alias: [">validar", ">aprobar_hu"]
  version: "4.0"

roles_autorizados:
  - ONAD

prerequisitos:
  archivos_requeridos:
    - descripcion: "HU refinada"
      ubicacion: "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento.md"
      estado_requerido: "[R] Refinada"
  archivos_opcionales:
    - "{{archivos.reglas_arquitectonicas}}"
    - "{{archivos.contexto_proyecto}}"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a validar"
  opcionales:
    - nombre: nivel_validacion
      tipo: string
      valores: [basico, completo, exhaustivo]
      defecto: completo

proceso:
  paso_1:
    nombre: "Cargar HU y Contexto"
    obligatorio: true
    acciones:
      - "Buscar HU en {{archivos.backlog}}"
      - "Verificar estado [R] Refinada"
      - "Cargar archivo de refinamiento"
      - "Cargar reglas arquitectónicas si existen"
    si_error:
      no_encontrada: "❌ HU [id_hu] no encontrada en backlog"
      estado_invalido: "⚠️ HU debe estar en estado [R] Refinada"

  paso_2:
    nombre: "Validación de Criterios de Aceptación"
    obligatorio: true
    acciones:
      - "Verificar que todos los CA sean medibles (SMART)"
      - "Detectar ambigüedades residuales"
      - "Validar cobertura de casos de error"
    checklist:
      - "CA específicos y verificables"
      - "Casos de error contemplados"
      - "Performance considerado si aplica"

  paso_3:
    nombre: "Validación Arquitectónica"
    obligatorio: true
    acciones:
      - "Verificar alineación con patrones del proyecto"
      - "Detectar violaciones a reglas arquitectónicas"
      - "Evaluar impacto en componentes existentes"
    validaciones:
      - "Respeta separación de capas"
      - "No introduce acoplamiento indebido"
      - "Sigue convenciones del proyecto"

  paso_4:
    nombre: "Análisis de Viabilidad Técnica"
    obligatorio: true
    acciones:
      - "Evaluar complejidad de implementación"
      - "Identificar riesgos técnicos"
      - "Validar estimación propuesta"

  paso_5:
    nombre: "Emisión de Veredicto"
    obligatorio: true
    acciones:
      - "Determinar resultado: APROBADA | AJUSTES | RECHAZADA"
      - "Documentar razones detalladas"
      - "Actualizar estado de HU"
    resultados:
      aprobada:
        estado_nuevo: "[A] Aprobada"
        siguiente: ">planificar_hu [id_hu]"
      ajustes:
        estado_nuevo: "[R] Refinada (con observaciones)"
        siguiente: "Devolver a REFINADOR con observaciones"
      rechazada:
        estado_nuevo: "[B] Bloqueada"
        siguiente: "Requiere rediseño significativo"

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
      - "Registrar herramienta ejecutada: validar_hu"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Actualizar estado de la HU validada"
      - "Guardar cambios en {{archivos.session_state}}"
    plantilla_referencia: "{{plantillas.session_state}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "validar_hu"
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
  archivos_actualizados:
    - "{{archivos.backlog}}"
    - "{{archivos.session_state}}"
  
  estado_hu_aprobada: "[A] Aprobada"
  estado_hu_ajustes: "[R] Refinada"
  estado_hu_rechazada: "[B] Bloqueada"
  
  mensaje_exito_aprobada: |
    ✅ HU APROBADA: [ID-HU]
    
    📋 Validaciones Pasadas:
    - ✅ Criterios de Aceptación
    - ✅ Alineación Arquitectónica
    - ✅ Viabilidad Técnica
    
    💡 Siguiente: >planificar_hu [ID-HU]

  mensaje_ajustes: |
    ⚠️ HU REQUIERE AJUSTES: [ID-HU]
    
    📋 Observaciones:
    - [lista de ajustes requeridos]
    
    💡 Acción: Devolver a +REFINADOR para ajustes

errores:
  hu_no_encontrada:
    mensaje: "❌ HU [id_hu] no encontrada"
    accion: "Verificar ID y ejecutar *HU para listar"
  estado_incorrecto:
    mensaje: "⚠️ HU no está en estado [R] Refinada"
    accion: "Ejecutar >refinar_hu primero"
  sin_reglas:
    mensaje: "ℹ️ No hay reglas arquitectónicas definidas"
    accion: "Validación basada en mejores prácticas generales"

siguiente:
  si_aprobada:
    herramienta: "planificar_hu"
    comando: ">planificar_hu [ID-HU]"
    rol_requerido: "ONAD"
  si_ajustes:
    herramienta: "refinar_hu"
    comando: ">refinar_hu [ID-HU]"
    rol_requerido: "REFINADOR"
```
