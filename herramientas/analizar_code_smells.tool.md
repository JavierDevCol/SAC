---
nombre: "Analizar Code Smells"
comando: ">analizar_code_smells"
alias: [">smells", ">code_review"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Clasificar smells por severidad (Alta/Media/Baja)"
  - instruccion: "Proponer solución específica para cada smell"
  - instruccion: "Priorizar por impacto en mantenibilidad"

reglas_arquitectonicas_requeridas:
  descripcion: "Si hay reglas arquitectónicas cargadas, aplicar:"
  secciones:
    - seccion: "calidad.max_lineas_metodo"
      aplicar: "Usar límite personalizado en lugar de 20 líneas por defecto"
    - seccion: "calidad.max_lineas_clase"
      aplicar: "Usar límite personalizado en lugar de 300 líneas por defecto"
    - seccion: "calidad.max_parametros"
      aplicar: "Usar límite personalizado en lugar de 3 parámetros por defecto"
    - seccion: "patrones.prohibidos"
      aplicar: "Agregar patrones prohibidos del proyecto a detección de smells"
    - seccion: "principios.nivel_solid"
      aplicar: "Ajustar severidad de violaciones SOLID según nivel (estricto/flexible)"
  si_no_existe: "Usar valores por defecto del catálogo de smells"

catalogo_smells:
  bloaters:
    - {smell: "Long Method", indicador: ">20 líneas", solucion: "Extract Method"}
    - {smell: "Large Class/God Object", indicador: ">300 líneas o >10 métodos", solucion: "Extract Class, SRP"}
    - {smell: "Long Parameter List", indicador: ">3 parámetros", solucion: "Parameter Object"}
    - {smell: "Data Clumps", indicador: "Datos que aparecen juntos", solucion: "Extract Class"}
  oo_abusers:
    - {smell: "Feature Envy", indicador: "Usa más datos de otra clase", solucion: "Move Method"}
    - {smell: "Inappropriate Intimacy", indicador: "Accede a internals de otras", solucion: "Move Method/Field"}
    - {smell: "Refused Bequest", indicador: "Subclase no usa herencia", solucion: "Replace Inheritance with Delegation"}
  change_preventers:
    - {smell: "Divergent Change", indicador: "Clase cambia por múltiples razones", solucion: "Extract Class (SRP)"}
    - {smell: "Shotgun Surgery", indicador: "Un cambio afecta múltiples clases", solucion: "Move Method/Field"}
    - {smell: "Parallel Inheritance", indicador: "Crear subclase requiere otra", solucion: "Move Method/Field"}
  dispensables:
    - {smell: "Dead Code", indicador: "Código no ejecutado", solucion: "Remove Dead Code"}
    - {smell: "Speculative Generality", indicador: "Abstracciones no usadas", solucion: "Collapse Hierarchy"}
    - {smell: "Duplicate Code", indicador: "Código repetido", solucion: "Extract Method, Pull Up"}
  couplers:
    - {smell: "Message Chains", indicador: "a.getB().getC().getD()", solucion: "Hide Delegate"}
    - {smell: "Middle Man", indicador: "Clase solo delega", solucion: "Remove Middle Man"}

severidad:
  alta: ["Afecta múltiples clases", "Bloquea testing", "Viola SOLID críticos"]
  media: ["Afecta mantenibilidad", "Dificulta comprensión"]
  baja: ["Mejora cosmética", "Convenciones de estilo"]

proceso:
  - paso: "Recepción de Código"
    obligatorio: true
    acciones: ["Recibir código a analizar", "Identificar lenguaje y contexto"]

  - paso: "Detección de Smells"
    obligatorio: true
    acciones: ["Escanear por cada categoría del catalogo_smells", "Aplicar indicadores", "Registrar ubicación exacta (clase:línea)"]

  - paso: "Clasificación por Severidad"
    obligatorio: true
    acciones: ["Evaluar cada smell contra criterios de severidad", "Asignar  Alta |  Media |  Baja", "Ordenar por impacto"]

  - paso: "Generación de Reporte"
    obligatorio: true
    acciones: ["Consolidar hallazgos ordenados por severidad", "Incluir solución del catálogo para cada smell", "Guardar en {{artifacts.code_smells_folder}}/code_smells_[timestamp].md"]

salida:
  archivos_generados:
    ruta: "{{artifacts.code_smells_folder}}/code_smells_[timestamp].md"
  mensaje_exito: |
     ANÁLISIS COMPLETADO
      Alta: [N] |  Media: [N] |  Baja: [N]
     Top 3: 1.[smellsolución] 2.[smellsolución] 3.[smellsolución]
     Siguiente: >solucionar_smells

errores:
  sin_codigo: {msg: " No se proporcionó código", accion: "Solicitar código o archivo específico"}
  no_java: {msg: " Código no es Java", accion: "Aplicar análisis genérico de smells"}

siguiente:
  - {comando: ">solucionar_smells", desc: "Aplicar refactorings para resolver smells detectados", chat_agente: "ArchDev Pro"}
```
