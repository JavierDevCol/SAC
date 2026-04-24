---
nombre: "Registrar Pendiente"
comando: ">registrar_pendiente"
alias: [">pendiente", ">hallazgo"]
version: "1.0"
---

```yaml
# ============================================
# REGISTRAR PENDIENTE - Herramienta de IA
# ============================================
# Archivo: registrar_pendiente.tool.md
# Versión: 1.0
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
  - instruccion: "El ID del pendiente sigue el patrón PND-NNN (autoincremental basado en entradas existentes en {{artifacts.pendientes}})"
  - instruccion: "Pendientes son hallazgos de pruebas funcionales para atacar más adelante, NO bugs activos"

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
      descripcion: "Descripción del hallazgo detectado en pruebas funcionales"
  opcionales:
    - nombre: categoria
      tipo: string
      valores: [deuda_tecnica, mejora_ux, optimizacion, otro]
      defecto: null
      descripcion: "Categoría del hallazgo. Si se omite, se determina durante el proceso."
    - nombre: hu_relacionada
      tipo: string
      descripcion: "ID de HU relacionada (ej: HU-003)"
      defecto: null
    - nombre: contexto_prueba
      tipo: string
      descripcion: "Contexto o prueba funcional donde se detectó el hallazgo"
      defecto: null

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Recepción del Hallazgo"
    obligatorio: true
    acciones:
      - "Recopilar información: descripción del hallazgo, contexto de prueba donde se detectó"
      - "SI falta la descripción → Solicitar al usuario"
      - "Asignar ID autoincremental: leer {{artifacts.pendientes}} para obtener último PND-NNN y sumar 1"

  - paso: "Evaluación de Severidad"
    obligatorio: true
    acciones:
      - "Evaluar si el hallazgo es realmente un pendiente o debería ser un bug:"
      - "  SI afecta funcionalidad del sistema → Informar al usuario:"
      - "  > ⚠️ Este hallazgo parece afectar funcionalidad directamente."
      - "  > 🤷 ¿Reclasificar como bug?"
      - "  > - 🐛 [B] Sí, registrar como bug vía >registrar_bug"
      - "  > - 📋 [P] No, mantener como pendiente"
      - "SI se confirma como pendiente → Continuar"
      - "SI se reclasifica → Detener y redirigir a >registrar_bug"

  - paso: "Categorización"
    obligatorio: true
    acciones:
      - "SI el usuario proporcionó categoría → Usar la indicada"
      - "SI NO → Determinar según contexto:"
      - "  🔧 Deuda Técnica: Código funcional pero mejorable (refactoring, patrones)"
      - "  🎨 Mejora UX: Experiencia de usuario mejorable pero funcional"
      - "  ⚡ Optimización: Rendimiento mejorable pero aceptable"
      - "  📌 Otro: No encaja en las anteriores"
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

salida:
  archivos_generados:
    ruta: "{{artifacts.pendientes}} (creado si no existía)"
  archivos_actualizados:
    - "{{artifacts.pendientes}} (nueva entrada agregada)"
  mensaje_exito: |
    📋 PENDIENTE REGISTRADO
    
    🆔 ID: PND-[NNN]
    📂 Categoría: [categoría]
    🔢 Prioridad: [prioridad]
    🔗 HU Relacionada: [HU-XXX / —]
    
    📄 Archivo: {{artifacts.pendientes}}
  siguiente:
    - { accion: "Continuar con la tarea actual", desc: "El pendiente queda registrado para abordar después" }
    - { comando: ">registrar_bug", desc: "Si se detecta otro hallazgo que SÍ afecte funcionalidad" }

errores:
  no_es_arquitecto: {msg: "❌ Solo el Arquitecto puede registrar pendientes", accion: "Usar >registrar_bug si eres Desarrollador"}
  hallazgo_es_bug: {msg: "⚠️ Este hallazgo afecta funcionalidad — debe ser bug", accion: "Redirigir a >registrar_bug"}
```
