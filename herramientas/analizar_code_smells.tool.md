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
  - instruccion: "Clasificar smells por severidad (Alta/Media/Baja)"
    nunca_saltar: true
  - instruccion: "Proponer solución específica para cada smell"
    nunca_saltar: true
  - instruccion: "Priorizar por impacto en mantenibilidad"
    nunca_saltar: true
  - instruccion: "Generar reportes en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Analizar Code Smells"
  comando: ">analizar_code_smells"
  alias: [">smells", ">code_review"]
  version: "4.0"

roles_autorizados:
  - ARCHDEV

catalogo_smells:
  bloaters:
    - nombre: "Long Method"
      indicador: "Método > 20 líneas"
      solucion: "Extract Method"
    - nombre: "Large Class / God Object"
      indicador: "Clase > 300 líneas o > 10 métodos públicos"
      solucion: "Extract Class, Single Responsibility"
    - nombre: "Long Parameter List"
      indicador: "> 3 parámetros"
      solucion: "Introduce Parameter Object"
    - nombre: "Data Clumps"
      indicador: "Grupos de datos que aparecen juntos"
      solucion: "Extract Class"
  
  oo_abusers:
    - nombre: "Feature Envy"
      indicador: "Método usa más datos de otra clase"
      solucion: "Move Method"
    - nombre: "Inappropriate Intimacy"
      indicador: "Clases acceden a internals de otras"
      solucion: "Move Method/Field, Extract Class"
    - nombre: "Refused Bequest"
      indicador: "Subclase no usa herencia del padre"
      solucion: "Replace Inheritance with Delegation"
  
  change_preventers:
    - nombre: "Divergent Change"
      indicador: "Clase cambia por múltiples razones"
      solucion: "Extract Class (SRP)"
    - nombre: "Shotgun Surgery"
      indicador: "Un cambio afecta múltiples clases"
      solucion: "Move Method/Field, Inline Class"
    - nombre: "Parallel Inheritance"
      indicador: "Crear subclase en una requiere otra"
      solucion: "Move Method/Field"
  
  dispensables:
    - nombre: "Dead Code"
      indicador: "Código no ejecutado"
      solucion: "Remove Dead Code"
    - nombre: "Speculative Generality"
      indicador: "Abstracciones no usadas"
      solucion: "Collapse Hierarchy, Inline Class"
    - nombre: "Duplicate Code"
      indicador: "Código repetido"
      solucion: "Extract Method, Pull Up Method"
  
  couplers:
    - nombre: "Message Chains"
      indicador: "a.getB().getC().getD()"
      solucion: "Hide Delegate"
    - nombre: "Middle Man"
      indicador: "Clase solo delega"
      solucion: "Remove Middle Man"

proceso:
  paso_1:
    nombre: "Recepción de Código"
    obligatorio: true
    acciones:
      - "Recibir código a analizar"
      - "Identificar lenguaje y contexto"
      - "Cargar reglas arquitectónicas si existen"

  paso_2:
    nombre: "Detección de Smells"
    obligatorio: true
    acciones:
      - "Escanear código por categoría de smell"
      - "Aplicar indicadores del catálogo"
      - "Registrar ubicación exacta (línea, método)"

  paso_3:
    nombre: "Clasificación por Severidad"
    obligatorio: true
    criterios:
      alta:
        - "Afecta múltiples clases"
        - "Bloquea testing"
        - "Viola principios SOLID críticos"
      media:
        - "Afecta mantenibilidad"
        - "Dificulta comprensión"
      baja:
        - "Mejora cosmética"
        - "Convenciones de estilo"

  paso_4:
    nombre: "Generación de Reporte"
    obligatorio: true
    acciones:
      - "Consolidar hallazgos"
      - "Ordenar por severidad"
      - "Incluir solución para cada smell"
      - "Guardar en {{artifacts.code_smells_folder}}"

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
      - "Registrar herramienta ejecutada: analizar_code_smells"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Si hay HU activa, actualizar su estado"
      - "Guardar cambios en {{archivos.session_state}}"
    plantilla_referencia: "{{plantillas.session_state}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "analizar_code_smells"
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
  archivos_generados:
    - tipo: "reporte_smells"
      ruta: "{{artifacts.code_smells_folder}}/code_smells_[timestamp].md"
  
  archivos_actualizados:
    - "{{archivos.session_state}}"
  
  mensaje_exito: |
    ✅ ANÁLISIS DE CODE SMELLS COMPLETADO
    
    📊 Resumen:
    - 🔴 Alta severidad: [N]
    - 🟡 Media severidad: [N]
    - 🟢 Baja severidad: [N]
    
    🎯 Top 3 Prioridades:
    1. [smell] en [ubicación] → [solución]
    2. [smell] en [ubicación] → [solución]
    3. [smell] en [ubicación] → [solución]
    
    💡 Siguiente: >solucionar_smells

formato_reporte: |
  # 🔍 Reporte de Code Smells
  
  ## Resumen Ejecutivo
  - Total smells: [N]
  - Severidad promedio: [Alta|Media|Baja]
  
  ## Hallazgos por Severidad
  
  ### 🔴 Alta Severidad
  | Smell | Ubicación | Solución |
  |-------|-----------|----------|
  | [nombre] | [clase:línea] | [refactoring] |
  
  ### 🟡 Media Severidad
  ...
  
  ### 🟢 Baja Severidad
  ...
  
  ## Plan de Acción Sugerido
  1. [acción prioritaria]

errores:
  sin_codigo:
    mensaje: "❌ No se proporcionó código para analizar"
    accion: "Solicitar código o archivo específico"
  codigo_no_java:
    mensaje: "⚠️ Código no es Java"
    accion: "Aplicar análisis genérico de smells"

siguiente:
  herramienta: "solucionar_smells"
  comando: ">solucionar_smells"
  descripcion: "Aplicar refactorings para resolver smells detectados"
```
