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
  - instruccion: "El ID del bug sigue el patrón BUG_NNN (autoincremental basado en archivos existentes en {{artifacts.bugs_folder}})"

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
    - nombre: modulo
      tipo: string
      descripcion: "Módulo o componente afectado"
      defecto: null
    - nombre: archivo
      tipo: string
      descripcion: "Ruta del archivo donde se detectó el bug"
      defecto: null
    - nombre: severidad
      tipo: string
      valores: [critica, alta, media]
      defecto: null
      descripcion: "Severidad del bug. Si se omite, se evalúa durante el proceso."

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Recepción del Bug"
    obligatorio: true
    acciones:
      - "Recopilar información del bug: descripción, módulo afectado, archivo(s), pasos para reproducir"
      - "SI faltan datos críticos (descripción o cómo reproducir) → Solicitar al usuario"
      - "Asignar ID autoincremental: escanear {{artifacts.bugs_folder}} para obtener último BUG_NNN y sumar 1"

  - paso: "Clasificación de Severidad"
    obligatorio: true
    acciones:
      - "SI el usuario proporcionó severidad → Usar la indicada"
      - "SI NO → Evaluar según criterios:"
      - "  🔴 Crítica: Bloquea funcionalidad core, pérdida de datos, crash del sistema"
      - "  🟠 Alta: Funcionalidad degradada, workaround difícil, afecta a múltiples usuarios"
      - "  🟡 Media: Funcionalidad menor afectada, workaround disponible"
      - "Mostrar clasificación propuesta y confirmar con usuario"

  - paso: "Triage — Búsqueda de HU Existente"
    obligatorio: true
    acciones:
      - "Leer {{archivos.backlog}}"
      - "Buscar HUs cuyo alcance funcional cubra el módulo/componente afectado por el bug"
      - "Buscar HUs con estado [E] En Ejecución o [P] Planificada en el mismo módulo"
      - "SI encuentra HU(s) candidata(s):"
      - "  Mostrar al usuario las HUs encontradas con su estado actual"
      - "  Preguntar:"
      - "  > 🤷 ¿Este bug se resuelve con una HU existente?"
      - "  > - 🔗 [V] Vincular a HU-XXX (el bug se resolverá cuando se complete esa HU)"
      - "  > - 🆕 [N] Crear nueva HU tipo Bug (es un problema independiente)"
      - "SI NO encuentra HUs relacionadas:"
      - "  Informar: 'No se encontraron HUs que cubran este módulo. Se creará nueva HU tipo Bug.'"

  - paso: "Acción según Triage"
    obligatorio: true
    acciones:
      - "SI [V] Vincular a HU existente:"
      - "  1. Registrar en el archivo bug la referencia: 'Vinculado a HU-XXX'"
      - "  2. Estado del bug: '🔗 Vinculado a HU'"
      - "  3. NO crear nueva HU en backlog"
      - "SI [N] Crear nueva HU tipo Bug:"
      - "  1. Agregar nueva entrada en {{archivos.backlog}} con formato:"
      - "     ### HU-[siguiente_ID]: 🐛 [Título del bug]"
      - "     Con campos: Tipo=Bug, Prioridad según severidad, Ref_Bug=BUG_NNN"
      - "  2. Estado del bug: '🔗 Vinculado a HU' con la nueva HU creada"

  - paso: "Generación de Archivo Bug"
    obligatorio: true
    acciones:
      - "Cargar plantilla desde {{plantillas_folder}}/bug_plantilla.md"
      - "Completar todos los campos con la información recopilada"
      - "Guardar en {{artifacts.bugs_folder}}/BUG_[ID]_[descripcion_snake_case].md"

salida:
  archivos_generados:
    ruta: "{{artifacts.bugs_folder}}/BUG_[ID]_[descripcion].md"
  archivos_actualizados:
    - "{{archivos.backlog}} (si se creó nueva HU tipo Bug)"
  mensaje_exito: |
    🐛 BUG REGISTRADO
    
    📋 ID: BUG_[ID]
    🔴 Severidad: [severidad]
    🔗 Acción: [Vinculado a HU-XXX / Nueva HU-XXX creada]
    
    📄 Archivo: {{artifacts.bugs_folder}}/BUG_[ID]_[descripcion].md
  siguiente:
    - { comando: ">planificar_hu", desc: "Planificar resolución del bug (si se creó HU nueva)", chat_agente: "Arquitecto" }
    - { comando: ">ejecutar_plan", desc: "Ejecutar corrección directamente (si ya hay plan)", chat_agente: "Desarrollador" }

errores:
  backlog_no_encontrado: {msg: "❌ No se encontró {{archivos.backlog}}", accion: "Ejecutar >refinar_hu para crear el backlog primero"}
  bugs_folder_no_existe: {msg: "⚠️ La carpeta {{artifacts.bugs_folder}} no existe", accion: "Crear la carpeta automáticamente antes de guardar"}
```
