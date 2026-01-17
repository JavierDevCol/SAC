---
nombre: "Analizar Stack Tecnológico"
comando: ">tomar_stack"
alias: [">stack", ">ts"]
version: "1.0"
---

```yaml
# ============================================
# ANALIZAR STACK TECNOLÓGICO - Herramienta de IA
# ============================================
# Archivo: analizar_stack.tool.md
# Versión: 1.0
# ============================================

# ============================================
# MANDATORY - INSTRUCCIONES INVIOLABLES
# ============================================
mandatory:
  # === BASE ESTÁNDAR (NO MODIFICAR) ===
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
  - instruccion: "Actualizar session_state.json al finalizar"
  - instruccion: "Nunca saltar proceso.paso_final"
  # === CONFIGURACIÓN DE IDIOMA ===
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
  # === ESPECÍFICAS DE LA HERRAMIENTA ===
  - instruccion: "SIEMPRE solicitar ruta_proyecto si no se proporciona"
  - instruccion: "Ejecutar algoritmo completo de {{reglas.deteccion_stack}}"
  - instruccion: "Calcular confidence score para cada detección"
  - instruccion: "SI confidence < 0.6: agregar warning y solicitar confirmación al usuario"
  - instruccion: "Generar archivo {{archivos.stack_proyecto}} al finalizar"

# ============================================
# PREREQUISITOS
# ============================================
prerequisitos:
  archivos_requeridos: none
  archivos_opcionales: none

# ============================================
# PARÁMETROS
# ============================================
parametros:
  requeridos:
    - nombre: "ruta_proyecto"
      tipo: string
      descripcion: "Ruta absoluta al proyecto a analizar"
  opcionales:
    - nombre: "profundidad"
      tipo: string
      valores: [basico, completo, exhaustivo]
      defecto: exhaustivo
      descripcion: "Nivel de profundidad del análisis"
    - nombre: "force"
      tipo: flag
      descripcion: "Regenerar archivo de stack aunque ya exista"
    - nombre: "incluir_dependencias"
      tipo: boolean
      defecto: true
      descripcion: "Incluir análisis detallado de dependencias"
reglas_delegadas:
  deteccion: "{{reglas.deteccion_stack}}"
  secciones_usadas:
    - "ecosistemas"       
    - "tipo_proyecto"         
    - "infraestructura"     
    - "proceso"            
    - "desambiguacion"       
    - "fallback"              
    - "output"               
proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones:
      - "Verificar que ruta_proyecto fue proporcionado"
      - "SI ruta_proyecto vacío → PREGUNTAR al usuario la ruta"
      - "Establecer valores por defecto: profundidad='exhaustivo', incluir_dependencias=true"
    si_error:
      ruta_no_proporcionada: "Solicitar ruta del proyecto al usuario antes de continuar"

  - paso: "Validar Acceso al Proyecto"
    obligatorio: true
    acciones:
      - "Verificar que {{ruta_proyecto}} existe y es accesible"
      - "Verificar permisos de lectura"
      - "Detectar si existe {{archivos.stack_proyecto}} previo"
    validaciones:
      - condicion: "Existe archivo stack previo AND force=false"
        si_cumple: "Preguntar: ¿Usar existente o regenerar?"
        si_no_cumple: "Continuar con análisis"
    si_error:
      ruta_invalida: "❌ La ruta especificada no existe o no es accesible"

  - paso: "Ejecutar Algoritmo de Detección de Stack"
    obligatorio: true
    delegar_a: "{{reglas.deteccion_stack}}.proceso"
    descripcion: "Ejecutar el algoritmo completo definido en las rules"
    acciones:
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_1: Detectar Monorepo"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_2: Buscar Marcadores de Ecosistema"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_3: Calcular Score por Ecosistema"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_4: Desambiguar por Extensiones (si empate)"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_5: Extraer Versiones"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_6: Detectar Tipo de Proyecto"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_7: Detectar Infraestructura"
      - "EJECUTAR {{reglas.deteccion_stack}}.proceso.paso_8: Calcular Confianza y Generar Output"
    usar_de_rules:
      ecosistemas: "{{reglas.deteccion_stack}}.ecosistemas"
      tipo_proyecto: "{{reglas.deteccion_stack}}.tipo_proyecto"
      infraestructura: "{{reglas.deteccion_stack}}.infraestructura"
      desambiguacion: "{{reglas.deteccion_stack}}.desambiguacion"
      fallback: "{{reglas.deteccion_stack}}.fallback"
    output: "Almacenar resultado en variable 'stack_detectado'"

  - paso: "Analizar Dependencias Detalladas"
    obligatorio: false
    condicion: "incluir_dependencias=true AND profundidad IN [completo, exhaustivo]"
    acciones:
      - "Leer archivo de dependencias según ecosistema detectado"
      - "Categorizar: producción vs desarrollo"
      - "Detectar dependencias de seguridad (auth, crypto)"
      - "Identificar dependencias de testing"
      - "SI profundidad='exhaustivo': detectar dependencias obsoletas"
    output:
      dependencias:
        produccion: ["dep@version"]
        desarrollo: ["dep@version"]
        seguridad: ["dep@version"]
        testing: ["dep@version"]
      warnings: ["Lista de dependencias potencialmente problemáticas"]

  - paso: "Validar Confidence y Confirmar"
    obligatorio: true
    acciones:
      - "Obtener confidence de stack_detectado.metadata.confidence"
      - "SI confidence < 0.6: Mostrar WARNING con top 3 ecosistemas"
      - "SI confidence < 0.6: Solicitar confirmación al usuario"
      - "SI usuario rechaza: permitir especificar ecosistema manualmente"
    usar_de_rules:
      threshold: "{{reglas.deteccion_stack}}.proceso.paso_8.accion"

  - paso: "Generar Archivo de Stack"
    obligatorio: true
    descripcion: "Genera 1 archivo MD con documentación legible del stack"
    acciones:
      - "Determinar ruta base según contexto existente:"
      - "  SI existe contexto_proyecto.md → usar {{rutas.artifacts_folder}}"
      - "  SI existe contexto_proyecto_{nombre}.md → usar {{artifacts.contextos_folder}}"
      - "Crear carpeta destino si no existe"
      - "Generar archivo MD:"
      - "  Ruta modo_unico: {{archivos.stack_proyecto}}"
      - "  Ruta modo_multi: {{artifacts.contextos_folder}}/{{multi_proyecto.patron_stack}}"
      - "  Formato: {{reglas.deteccion_stack}}.output.formato_legible"
      - "Agregar timestamp de generación"
      - "Agregar warnings de {{reglas.deteccion_stack}}.output si existen"
    rutas:
      modo_unico: "{{archivos.stack_proyecto}}"
      modo_multi: "{{artifacts.contextos_folder}}/{{multi_proyecto.patron_stack}}"

  - paso: "Actualizar Sección Stack en Contexto"
    obligatorio: true
    acciones:
      - "SI existe archivo contexto_proyecto*.md:"
      - "  Agregar/actualizar referencia al archivo stack generado"
      - "  Formato: '📊 Stack detallado: [stack_proyecto.md](./stack_proyecto.md)'"
      - "SI NO existe contexto: omitir este paso"

  - paso: "Actualizar Estado de Sesión"
    obligatorio: true
    acciones:
      - "Registrar ejecución en session_state.json"
      - "Actualizar última_herramienta_ejecutada: 'tomar_stack'"
      - "Guardar ruta del archivo generado"

# ============================================
# SALIDA
# ============================================
salida:
  descripcion: "Genera 1 archivo MD en la misma ubicación que contexto_proyecto"
  
  archivos_generados:
    nombre: "Stack MD (documentación)"
    ruta_unico: "{{archivos.stack_proyecto}}"
    ruta_multi: "{{artifacts.contextos_folder}}/stack_proyecto_{nombre}.md"
    formato: "{{reglas.deteccion_stack}}.output.formato_legible"
    proposito: "Documentación legible del stack tecnológico"
  
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
  
  mensaje_exito: |
    ✅ ANÁLISIS DE STACK COMPLETADO
    
    📊 Resumen:
    - Ecosistema: {{stack.ecosistema}} {{stack.version}}
    - Framework: {{stack.framework}} {{stack.framework_version}}
    - Tipo: {{stack.tipo_proyecto}}
    - Confidence: {{stack.confidence}}%
    
    📄 Artefacto generado:
    - 📝 {{archivos.stack_proyecto}}
    
    ⚠️ Warnings: {{stack.metadata.warnings | default: "Ninguno"}}
    
    💡 Siguiente paso sugerido:
    - >tomar_contexto (si no existe contexto)
    - >planificar_hu (si ya existe contexto)

# ============================================
# ERRORES
# ============================================
errores:
  ruta_no_proporcionada: {msg: "❌ Parámetro ruta_proyecto es obligatorio", accion: "Proporcionar ruta del proyecto a analizar"}
  ruta_invalida: {msg: "❌ La ruta especificada no existe", accion: "Verificar que la ruta es correcta y accesible"}
  sin_marcadores: 
    msg: "❌ No se detectaron archivos de configuración de proyecto"
    accion: "Aplicar {{reglas.deteccion_stack}}.fallback.sin_marcadores"
  error_lectura:
    msg: "⚠️ No se pudo leer archivo marcador"
    accion: "Aplicar {{reglas.deteccion_stack}}.fallback.error_lectura"
  confidence_baja: 
    msg: "⚠️ Confidence score bajo (<0.6)"
    accion: "Mostrar top 3 ecosistemas y solicitar confirmación manual"
  archivo_existente: {msg: "ℹ️ Ya existe archivo de stack", accion: "Usar --force para regenerar"}

siguiente:
  - { comando: ">tomar_contexto", desc: "Generar contexto completo del proyecto", chat_agente: "archdev_pro" }
  - { comando: ">planificar_hu", desc: "Planificar historias de usuario", chat_agente: "refinador_hu" }
  - { comando: ">analizar_code_smells", desc: "Detectar problemas de código", chat_agente: "archdev_pro" }
```
