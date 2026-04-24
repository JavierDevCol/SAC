---
nombre: "Registrar Pendiente"
comando: ">registrar_pendiente"
alias: [">pendiente", ">hallazgo"]
version: "2.0"
---

```yaml
# ============================================
# REGISTRAR PENDIENTE - Herramienta de IA
# ============================================
# Archivo: registrar_pendiente.tool.md
# Versión: 2.0
# Disponible para: Arquitecto (exclusivo)
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
  - instruccion: "Solo el Arquitecto puede ejecutar esta herramienta"
  - instruccion: "Hallazgos de prioridad Alta deben reclasificarse como bug vía >registrar_bug"
  - instruccion: "El ID del pendiente sigue el patrón PND-NNN (autoincremental)"
  - instruccion: "Si el usuario adjunta logs o evidencia extensa, SIEMPRE crear archivo individual de detalle"
  - instruccion: "Un pendiente puede evolucionar a HU funcional O a bug — no asumir que solo evoluciona a bug"

# ============================================
# PREREQUISITOS
# ============================================
condiciones_entrada:
  - condicion: "El agente activo es Arquitecto"
    si_no_cumple: "Esta herramienta es exclusiva del Arquitecto. El Desarrollador puede reportar bugs con >registrar_bug."

# ============================================
# PARÁMETROS
# ============================================
parametros:
  requeridos:
    - nombre: descripcion
      tipo: string
      descripcion: "Qué se debe revisar, verificar, analizar o mejorar"
  opcionales:
    - nombre: categoria
      tipo: string
      valores: [deuda_tecnica, mejora_ux, optimizacion, verificacion, investigacion, con_evidencia]
      defecto: null
      descripcion: "Categoría del pendiente. Si se omite, se determina durante el proceso."
    - nombre: hu_relacionada
      tipo: string
      descripcion: "ID de HU relacionada (ej: HU-003)"
      defecto: null
    - nombre: contexto
      tipo: string
      descripcion: "Contexto donde se originó el pendiente (prueba, revisión, HU específica)"
      defecto: null
    - nombre: logs
      tipo: string
      descripcion: "Logs, stack traces o evidencia para análisis posterior. Activa creación de archivo individual."
      defecto: null

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Recepción del Pendiente"
    obligatorio: true
    acciones:
      - "Recopilar información: descripción de lo que se debe hacer/revisar/analizar"
      - "SI falta la descripción → Solicitar al usuario"
      - "Asignar ID autoincremental: leer {{artifacts.pendientes}} para obtener último PND-NNN y sumar 1"
      - "Determinar nivel de detalle:"
      - "  SI el usuario adjunta logs/evidencia → Nivel DETALLADO (archivo individual)"
      - "  SI el usuario proporciona descripción extensa (>3 líneas) → Nivel DETALLADO"
      - "  SI NO → Nivel RÁPIDO (solo fila en tabla)"

  - paso: "Evaluación de Severidad"
    obligatorio: true
    acciones:
      - "Evaluar si el pendiente debería ser un bug:"
      - "  SI afecta funcionalidad del sistema ACTUALMENTE → Informar al usuario:"
      - "  > ⚠️ Esto parece afectar funcionalidad activa del sistema."
      - "  > 🤷 ¿Reclasificar como bug?"
      - "  > - 🐛 [B] Sí, registrar como bug vía >registrar_bug"
      - "  > - 📋 [P] No, mantener como pendiente (para revisar después)"
      - "SI se confirma como pendiente → Continuar"
      - "SI se reclasifica → Detener y redirigir a >registrar_bug"

  - paso: "Categorización"
    obligatorio: true
    acciones:
      - "SI el usuario proporcionó categoría → Usar la indicada"
      - "SI NO → Determinar según la naturaleza del pendiente:"
      - "  🔧 Deuda Técnica: Código funcional pero mejorable (refactoring, patrones)"
      - "  🎨 Mejora UX: Experiencia de usuario mejorable pero funcional"
      - "  ⚡ Optimización: Rendimiento mejorable pero aceptable"
      - "  🔍 Verificación: Revisar correcto funcionamiento de algo (testing pendiente)"
      - "  🧪 Investigación: Analizar flujo, comportamiento o viabilidad de algo"
      - "  📎 Con Evidencia: Incluye logs/datos que requieren análisis posterior"
      - "NOTA: 📎 Con Evidencia puede combinarse con otra categoría. En ese caso, usar la categoría funcional y marcar que tiene evidencia adjunta."
      - "Asignar prioridad:"
      - "  🟡 Baja: Puede esperar varias iteraciones"
      - "  🟠 Media: Debería abordarse en próximas iteraciones"
      - "  NOTA: Si la prioridad es Alta → Reclasificar como bug"

  - paso: "Vinculación Opcional"
    obligatorio: false
    acciones:
      - "SI el usuario proporcionó hu_relacionada → Registrar la referencia"
      - "SI NO → Buscar brevemente en {{archivos.backlog}} HUs del mismo módulo"
      - "  SI encuentra candidata → Preguntar si desea vincular"
      - "  SI NO encuentra → Dejar campo como '—'"

  - paso: "Registro en Archivo de Pendientes"
    obligatorio: true
    acciones:
      - "SI NO existe {{artifacts.pendientes}} → Crear archivo usando plantilla {{plantillas_folder}}/pendientes_plantilla.md"
      - "SI existe → Leer archivo actual"
      - "Agregar nueva fila en la tabla de Registro con todos los campos completados"
      - "Guardar {{artifacts.pendientes}}"

  - paso: "Generación de Archivo Individual (Condicional)"
    obligatorio: false
    condicion: "SI nivel es DETALLADO (logs adjuntos, descripción extensa, o categoría 📎 Con Evidencia)"
    acciones:
      - "Cargar plantilla desde {{plantillas_folder}}/pendiente_detalle_plantilla.md"
      - "Completar secciones aplicables: Metadata, Descripción, Evidencia/Logs, Análisis Previo"
      - "Dejar sección Resolución vacía (se completa al promover/reclasificar/descartar)"
      - "Guardar en {{artifacts.pendientes_folder}}/PND-[ID]_[descripcion_kebab_case].md"

salida:
  archivos_generados:
    ruta_tabla: "{{artifacts.pendientes}} (creado si no existía)"
    ruta_detalle: "{{artifacts.pendientes_folder}}/PND-[ID]_[descripcion].md (solo si nivel DETALLADO)"
  archivos_actualizados:
    - "{{artifacts.pendientes}} (nueva entrada agregada)"
  mensaje_exito: |
    📋 PENDIENTE REGISTRADO
    
    🆔 ID: PND-[NNN]
    📂 Categoría: [categoría]
    🔢 Prioridad: [prioridad]
    🔗 HU Relacionada: [HU-XXX / —]
    📎 Detalle: [Sí — archivo individual creado / No — solo en tabla]
    
    📄 Archivo: {{artifacts.pendientes}}
  siguiente:
    - { accion: "Continuar con la tarea actual", desc: "El pendiente queda registrado para abordar después" }
    - { comando: ">registrar_bug", desc: "Si se detecta un hallazgo que SÍ afecte funcionalidad activa" }

errores:
  no_es_arquitecto: {msg: "❌ Solo el Arquitecto puede registrar pendientes", accion: "Usar >registrar_bug si eres Desarrollador"}
  hallazgo_es_bug: {msg: "⚠️ Este hallazgo afecta funcionalidad activa — debe ser bug", accion: "Redirigir a >registrar_bug"}
  pendientes_folder_no_existe: {msg: "⚠️ La carpeta {{artifacts.pendientes_folder}} no existe", accion: "Crear la carpeta automáticamente antes de guardar"}
```
