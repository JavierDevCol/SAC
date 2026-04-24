---
nombre: "Registrar Bug"
comando: ">registrar_bug"
alias: [">bug", ">reportar_bug"]
version: "1.0"
---

```yaml
# ============================================
# REGISTRAR BUG - Herramienta de IA
# ============================================
# Archivo: registrar_bug.tool.md
# Versión: 1.0
# Disponible para: Arquitecto y Desarrollador
# ============================================

# ============================================
# MANDATORY - INSTRUCCIONES INVIOLABLES
# ============================================
mandatory:
  # === BASE ESTÁNDAR (NO MODIFICAR) ===
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
  - instruccion: "Nunca saltar proceso.paso_final"
  # === CONFIGURACIÓN DE IDIOMA ===
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
  # === ESPECÍFICAS DE LA HERRAMIENTA ===
  - instruccion: "Todo bug DEBE tener triage antes de considerarse procesado"
  - instruccion: "SIEMPRE buscar HUs existentes en el backlog antes de crear una nueva"
  - instruccion: "Los bugs afectan funcionalidad del sistema — priorizar resolución"
  - instruccion: "El ID del bug sigue el patrón BUG-NNN (autoincremental basado en archivos existentes en {{artifacts.bugs_folder}})"
  - instruccion: "Al registrar un bug ya corregido, completar TODAS las secciones incluyendo Corrección y Lección Aprendida"

# ============================================
# PREREQUISITOS
# ============================================
condiciones_entrada:
  - condicion: "Existe {{archivos.backlog}}"
    si_no_cumple: "No hay backlog disponible. Ejecutar >refinar_hu para crear el backlog primero."

# ============================================
# PARÁMETROS
# ============================================
parametros:
  requeridos:
    - nombre: descripcion
      tipo: string
      descripcion: "Descripción del bug detectado"
  opcionales:
    - nombre: proyecto
      tipo: string
      descripcion: "Nombre del proyecto afectado"
      defecto: null
    - nombre: detectado_en
      tipo: string
      descripcion: "Contexto de detección (ej: HU-010, pruebas funcionales, producción)"
      defecto: null
    - nombre: severidad
      tipo: string
      valores: [critica, alta, media]
      defecto: null
      descripcion: "Severidad del bug. Si se omite, se evalúa durante el proceso."
    - nombre: ya_corregido
      tipo: flag
      descripcion: "Indica que el bug ya fue corregido y se registra post-mortem"

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Recepción del Bug"
    obligatorio: true
    acciones:
      - "Recopilar información del bug: descripción, proyecto, contexto de detección"
      - "SI faltan datos críticos (descripción o síntoma) → Solicitar al usuario"
      - "Asignar ID autoincremental: escanear {{artifacts.bugs_folder}} para obtener último BUG-NNN y sumar 1"
      - "SI flag --ya_corregido → Recopilar también: commit fix, archivos afectados, código antes/después, lección aprendida"

  - paso: "Clasificación de Severidad"
    obligatorio: true
    acciones:
      - "SI el usuario proporcionó severidad → Usar la indicada"
      - "SI NO → Evaluar según criterios:"
      - "  🔴 Crítica: Bloquea funcionalidad core, pérdida de datos, crash del sistema"
      - "  🟠 Alta: Funcionalidad degradada, workaround difícil, afecta a múltiples usuarios"
      - "  🟡 Media: Funcionalidad menor afectada, workaround disponible"
      - "Mostrar clasificación propuesta y confirmar con usuario"

  - paso: "Análisis de Causa Raíz"
    obligatorio: true
    acciones:
      - "Documentar el síntoma observable (qué ve el usuario o el sistema)"
      - "Identificar la causa raíz técnica (por qué ocurre)"
      - "SI hay inconsistencia entre capas/componentes → Documentar con tabla comparativa"
      - "Listar archivos afectados con descripción del problema en cada uno"

  - paso: "Triage — Búsqueda de HU Existente"
    obligatorio: true
    condicion: "SI NO es --ya_corregido (bugs ya corregidos no necesitan triage)"
    acciones:
      - "Leer {{archivos.backlog}}"
      - "Buscar HUs cuyo alcance funcional cubra el módulo/componente afectado por el bug"
      - "Buscar HUs con estado [E] En Ejecución o [P] Planificada en el mismo módulo"
      - "SI encuentra HU(s) candidata(s):"
      - "  Mostrar al usuario las HUs encontradas con su estado actual"
      - "  Preguntar:"
      - "  > 🤷 ¿Cómo proceder con este bug?"
      - "  > - 🔗 [V] Vincular a HU-XXX (se resolverá cuando se complete esa HU)"
      - "  > - 📝 [A] Agregar ajuste a HU-XXX (instrucciones de corrección en la HU existente)"
      - "  > - 🆕 [N] Crear nueva HU tipo Bug (es un problema independiente)"
      - "SI NO encuentra HUs relacionadas:"
      - "  Informar: 'No se encontraron HUs que cubran este módulo. Se creará nueva HU tipo Bug.'"

  - paso: "Acción según Triage"
    obligatorio: true
    condicion: "SI NO es --ya_corregido"
    acciones:
      - "SI [V] Vincular a HU existente:"
      - "  1. Registrar en el archivo bug la referencia: 'Detectado en HU-XXX'"
      - "  2. Estado del bug: '🔗 Vinculado a HU'"
      - "  3. NO crear nueva HU en backlog"
      - "SI [A] Agregar ajuste a HU existente:"
      - "  1. Leer refinamiento de la HU desde {{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md"
      - "  2. SI el refinamiento NO tiene sección '## 🐛 Ajustes por Bug' → Crearla al final antes de la firma"
      - "  3. Agregar bloque de ajuste en esa sección:"
      - "     ### BUG-NNN: [Título del bug]"
      - "     - **Severidad:** [severidad]"
      - "     - **Causa raíz:** [resumen de causa raíz del paso anterior]"
      - "     - **Archivos a modificar:** [lista de archivos afectados]"
      - "     - **Corrección sugerida:** [instrucciones concretas de qué cambiar]"
      - "  4. Registrar en el archivo bug: 'Ajuste agregado a HU-XXX'"
      - "  5. Estado del bug: '📝 Ajuste en HU'"
      - "SI [N] Crear nueva HU tipo Bug:"
      - "  1. Agregar nueva entrada en {{archivos.backlog}} con formato:"
      - "     ### HU-[siguiente_ID]: 🐛 [Título del bug]"
      - "     Con campos: Tipo=Bug, Prioridad según severidad, Ref_Bug=BUG-NNN"
      - "  2. Estado del bug: '🔗 Vinculado a HU' con la nueva HU creada"

  - paso: "Documentar Corrección"
    obligatorio: false
    condicion: "SI el bug ya fue corregido (--ya_corregido o el usuario indica que ya lo arregló)"
    acciones:
      - "Registrar el commit fix con su mensaje"
      - "Documentar la corrección con fragmentos de código Antes/Después"
      - "Estado del bug: '✅ Corregido'"
      - "Incluir fecha de corrección"

  - paso: "Lección Aprendida"
    obligatorio: false
    condicion: "SI el bug ya fue corregido"
    acciones:
      - "Documentar qué se puede hacer para prevenir este tipo de bug en el futuro"
      - "Las recomendaciones deben ser concretas y accionables"

  - paso: "Generación de Archivo Bug"
    obligatorio: true
    acciones:
      - "Cargar plantilla desde {{plantillas_folder}}/bug_plantilla.md"
      - "Completar TODAS las secciones aplicables con la información recopilada"
      - "Secciones obligatorias: Metadata, Descripción, Síntoma, Causa Raíz, Archivos Afectados"
      - "Secciones condicionales (si corregido): Corrección, Lección Aprendida"
      - "Guardar en {{artifacts.bugs_folder}}/BUG-[ID]_[descripcion_kebab_case].md"

salida:
  archivos_generados:
    ruta: "{{artifacts.bugs_folder}}/BUG-[ID]_[descripcion].md"
  archivos_actualizados:
    - "{{archivos.backlog}} (si se creó nueva HU tipo Bug)"
    - "{{artifacts.hu_refinamientos}}/[ID-HU]_refinamiento*.md (si se agregó ajuste a HU existente)"
  mensaje_exito: |
    🐛 BUG REGISTRADO
    
    📋 ID: BUG-[ID]
    🔴 Severidad: [severidad]
    📌 Estado: [🆕 Nuevo / 🔗 Vinculado a HU-XXX / 📝 Ajuste en HU-XXX / ✅ Corregido]
    
    📄 Archivo: {{artifacts.bugs_folder}}/BUG-[ID]_[descripcion].md
  siguiente:
    - { comando: ">planificar_hu", desc: "Planificar resolución del bug (si se creó HU nueva)", chat_agente: "Arquitecto" }
    - { comando: ">ejecutar_plan", desc: "Ejecutar corrección directamente (si ya hay plan)", chat_agente: "Desarrollador" }

errores:
  backlog_no_encontrado: {msg: "❌ No se encontró {{archivos.backlog}}", accion: "Ejecutar >refinar_hu para crear el backlog primero"}
  bugs_folder_no_existe: {msg: "⚠️ La carpeta {{artifacts.bugs_folder}} no existe", accion: "Crear la carpeta automáticamente antes de guardar"}
```
