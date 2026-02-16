---
nombre: "Analizar Stack Tecnológico"
comando: ">tomar_stack"
alias: [">stack", ">ts"]
version: "1.0"
---

```yaml
mandatory:
  - instruccion: "SIEMPRE solicitar ruta_proyecto si no se proporciona"
  - instruccion: "Ejecutar algoritmo completo de {{reglas.deteccion_stack}}"
  - instruccion: "Calcular confidence score para cada detección"
  - instruccion: "SI confidence < 0.6: agregar warning y solicitar confirmación al usuario"
  - instruccion: "Actualizar sección '## 2. Stack Tecnológico' en el contexto del proyecto activo (ver {{archivos.workspace}})"

# ============================================
# CONDICIONES DE ENTRADA
# ============================================
condiciones_entrada:
  - condicion: "Ruta del proyecto a analizar"

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
      - "Detectar si existe {{archivos.workspace}}"
      - "SI existe workspace: identificar contexto del proyecto activo desde {{artifacts.contextos_folder}}"
    validaciones:
      - condicion: "NO existe {{archivos.workspace}}"
        si_cumple: "Informar: 'No existe workspace. Ejecutar >tomar_contexto primero'"
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

  - paso: "Actualizar Sección Stack en Contexto"
    obligatorio: true
    descripcion: "Actualiza la sección '## 2. Stack Tecnológico' en el contexto del proyecto"
    acciones:
      - "Obtener ruta del contexto activo desde {{archivos.workspace}}:"
      - "  - Mono-proyecto: {{artifacts.contextos_folder}}/contexto_proyecto.md"
      - "  - Multi-proyecto: {{artifacts.contextos_folder}}/contexto_proyecto_[nombre].md"
      - "SI existe el contexto:"
      - "  Buscar sección '## 2. Stack Tecnológico'"
      - "  Reemplazar contenido completo de la sección (hasta siguiente ##) con:"
      - "    ### Resumen"
      - "    | Categoría | Tecnología | Versión |"
      - "    | Lenguaje | {{stack.ecosistema}} | {{stack.version}} |"
      - "    | Framework | {{stack.framework}} | {{stack.framework_version}} |"
      - "    | Base de Datos | {{stack.database}} | {{stack.db_version}} |"
      - "    | Testing | {{stack.testing}} | - |"
      - "    | Build | {{stack.build_tool}} | {{stack.build_version}} |"
      - "    ### Dependencias Core"
      - "    [tabla de dependencias principales]"
      - "    ### Herramientas de Desarrollo"
      - "    [tabla de linters/formatters detectados]"
      - "  Actualizar timestamp en Historial"
      - "SI NO existe workspace:"
      - "  Mostrar resultado en consola"
      - "  Sugerir: '>tomar_contexto para crear workspace'"

# ============================================
# SALIDA
# ============================================
salida:
  descripcion: "Actualiza sección Stack en el contexto del proyecto activo"
  
  archivos_actualizados:
    - archivo: "{{artifacts.contextos_folder}}/contexto_proyecto[_nombre].md"
      seccion: "## 2. Stack Tecnológico"
      accion: "Reemplazar contenido de la sección"
  
  mensaje_exito: |
    ✅ ANÁLISIS DE STACK COMPLETADO
    
    📊 Resumen:
    - Ecosistema: {{stack.ecosistema}} {{stack.version}}
    - Framework: {{stack.framework}} {{stack.framework_version}}
    - Tipo: {{stack.tipo_proyecto}}
    - Confidence: {{stack.confidence}}%
    
    📄 Actualizado:
    - Contexto del proyecto → Sección "## 2. Stack Tecnológico"
    
    ⚠️ Warnings: {{stack.metadata.warnings | default: "Ninguno"}}
    
    💡 Siguiente paso sugerido:
    - >planificar_hu (si hay HUs pendientes)
    - >analizar_code_smells (análisis de calidad)

# ============================================
# ERRORES
# ============================================
errores:
  ruta_no_proporcionada: {msg: "❌ Parámetro ruta_proyecto es obligatorio", accion: "Proporcionar ruta del proyecto a analizar"}
  ruta_invalida: {msg: "❌ La ruta especificada no existe", accion: "Verificar que la ruta es correcta y accesible"}
  sin_contexto: {msg: "⚠️ No existe workspace", accion: "Ejecutar >tomar_contexto primero para crear el workspace"}
  sin_marcadores: 
    msg: "❌ No se detectaron archivos de configuración de proyecto"
    accion: "Aplicar {{reglas.deteccion_stack}}.fallback.sin_marcadores"
  error_lectura:
    msg: "⚠️ No se pudo leer archivo marcador"
    accion: "Aplicar {{reglas.deteccion_stack}}.fallback.error_lectura"
  confidence_baja: 
    msg: "⚠️ Confidence score bajo (<0.6)"
    accion: "Mostrar top 3 ecosistemas y solicitar confirmación manual"

siguiente:
  - { comando: ">tomar_contexto", desc: "Generar contexto completo del proyecto", chat_agente: "archdev_pro" }
  - { comando: ">planificar_hu", desc: "Planificar historias de usuario", chat_agente: "refinador_hu" }
  - { comando: ">analizar_code_smells", desc: "Detectar problemas de código", chat_agente: "archdev_pro" }
```
