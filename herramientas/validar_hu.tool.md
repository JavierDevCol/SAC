---
nombre: "Validar Historia de Usuario"
comando: ">validar_hu"
alias: [">validar", ">aprobar_hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Pasos obligatorios NO se pueden omitir"
  - instruccion: "Verificar alineación con reglas arquitectónicas del proyecto"
  - instruccion: "NO aprobar HU que violen principios arquitectónicos"
  - instruccion: "Documentar razones de rechazo o ajustes requeridos"
  - instruccion: "Generar en idioma: {{preferencias.idioma_documentacion}}"

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
    - {nombre: nivel_validacion, tipo: string, valores: [basico, completo, exhaustivo], defecto: completo}

veredictos:
  aprobada: {estado: "[A] Aprobada", siguiente: ">planificar_hu [ID-HU]"}
  ajustes: {estado: "[R] Refinada + observaciones", siguiente: ">refinar_hu [ID-HU]"}
  rechazada: {estado: "[B] Bloqueada", siguiente: "Requiere rediseño significativo"}

proceso:
  - paso: "Cargar HU y Contexto"
    obligatorio: true
    acciones: ["Buscar HU en {{archivos.backlog}}", "Verificar estado [R] Refinada", "Cargar refinamiento y reglas arquitectónicas"]
    si_error:
      no_encontrada: "HU [id_hu] no encontrada en backlog"
      estado_invalido: "HU debe estar en estado [R] Refinada"

  - paso: "Validación de Criterios de Aceptación"
    obligatorio: true
    acciones: ["Verificar CA medibles (SMART)", "Detectar ambigüedades residuales", "Validar cobertura de casos de error"]
    checklist: ["CA específicos y verificables", "Casos de error contemplados", "Performance considerado si aplica"]

  - paso: "Validación Arquitectónica"
    obligatorio: true
    acciones: ["Verificar alineación con patrones del proyecto", "Detectar violaciones a reglas arquitectónicas", "Evaluar impacto en componentes existentes"]
    checklist: ["Respeta separación de capas", "No introduce acoplamiento indebido", "Sigue convenciones del proyecto"]

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
