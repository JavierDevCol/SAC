---
nombre: "Registrar Hallazgo"
comando: ">registrar_hallazgo"
alias: [">hallazgo"]
version: "1.0"
---

```yaml
# ============================================
# REGISTRAR HALLAZGO - Dispatcher de Clasificación
# ============================================
# Archivo: registrar_hallazgo.tool.md
# Versión: 1.0
# Disponible para: Arquitecto y Desarrollador
# ============================================
# NOTA: Esta herramienta NO tiene proceso propio de registro.
# Es un dispatcher que recopila información, clasifica el
# hallazgo y redirige a >registrar_bug o >registrar_pendiente
# transfiriendo todo el contexto recopilado.
# ============================================

# ============================================
# MANDATORY - INSTRUCCIONES INVIOLABLES
# ============================================
mandatory:
  # === BASE ESTÁNDAR (NO MODIFICAR) ===
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
  # === ESPECÍFICAS DE LA HERRAMIENTA ===
  - instruccion: "NUNCA registrar directamente — siempre redirigir a >registrar_bug o >registrar_pendiente"
  - instruccion: "SIEMPRE confirmar la clasificación con el usuario antes de redirigir"
  - instruccion: "Transferir TODO el contexto recopilado a la herramienta destino (la herramienta destino salta su Paso 1)"
  - instruccion: "SI el agente activo es Desarrollador y clasifica como pendiente → Informar que >registrar_pendiente es exclusivo del Arquitecto y registrar como bug o anotar para que el Arquitecto lo registre después"

# ============================================
# PARÁMETROS
# ============================================
parametros:
  requeridos:
    - nombre: descripcion
      tipo: string
      descripcion: "Descripción libre del hallazgo tal como el usuario lo percibe"
  opcionales:
    - nombre: proyecto
      tipo: string
      descripcion: "Proyecto afectado (si se omite, se detecta del contexto activo)"
      defecto: null
    - nombre: logs
      tipo: string
      descripcion: "Logs, mensajes de consola, stack traces o evidencia"
      defecto: null

# ============================================
# INDICADORES DE CLASIFICACIÓN
# ============================================
indicadores_clasificacion:
  bug_probable:
    keywords_error:
      - "Error:", "error:", "ERROR"
      - "blocked", "failed", "rejected", "refused"
      - "not allowed", "forbidden", "unauthorized"
      - "crash", "exception", "throw", "unhandled"
      - "Cannot read", "undefined is not", "null reference"
      - "status 4xx", "status 5xx", "500", "404", "403"
    comportamiento:
      - "Funcionalidad que antes funcionaba ya no funciona"
      - "Operación bloqueada o imposible de completar"
      - "Datos incorrectos, perdidos o corruptos"
      - "Redirección inesperada o loop infinito"
    severidad_implicita: "Media o superior"

  pendiente_probable:
    keywords_warning:
      - "Warning:", "warning:", "WARN"
      - "deprecated", "deprecation"
      - "aria-", "accessibility", "a11y"
      - "performance", "slow", "optimization"
      - "TODO", "FIXME", "HACK"
    comportamiento:
      - "Funciona correctamente pero muestra warning"
      - "Mejora visual o de UX sin impacto funcional"
      - "Deuda técnica identificada"
      - "Revisar o verificar algo para más adelante"
      - "Analizar flujo o comportamiento"
    severidad_implicita: "Baja"

  indeterminado:
    condicion: "No se detectan keywords claros Y el comportamiento es ambiguo"
    accion: "Preguntar al usuario con opción [I] Investigar"

# ============================================
# PROCESO
# ============================================
proceso:
  - paso: "Recepción Universal"
    obligatorio: true
    acciones:
      - "Recopilar descripción del hallazgo tal como el usuario la proporciona"
      - "Detectar proyecto del contexto activo (SI no se proporcionó explícitamente)"
      - "Preguntar por evidencia:"
      - "  > 🤷 ¿Tienes logs, mensajes de error o evidencia para adjuntar?"
      - "  > - 📎 [S] Sí, los pego a continuación"
      - "  > - ➡️ [N] No, continuar con lo que tengo"
      - "SI [S] → Recopilar logs y almacenar como contexto"

  - paso: "Clasificación Automática"
    obligatorio: true
    acciones:
      - "Analizar descripción y logs contra indicadores_clasificacion:"
      - "  1. Buscar keywords de error → Sumar puntos hacia 'bug'"
      - "  2. Buscar keywords de warning → Sumar puntos hacia 'pendiente'"
      - "  3. Evaluar comportamiento descrito → ¿Bloquea funcionalidad?"
      - "  4. SI hay error de runtime o funcionalidad rota → Bug probable"
      - "  5. SI hay warning sin impacto funcional → Pendiente probable"
      - "  6. SI no es claro → Indeterminado"
      - "Mostrar evaluación al usuario:"
      - ""
      - "  🔍 Analizando hallazgo..."
      - "  Indicadores detectados:"
      - "    [✅/⚠️/❓] [indicador 1]"
      - "    [✅/⚠️/❓] [indicador 2]"
      - "  📊 Evaluación: [AFECTA FUNCIONALIDAD → Bug / NO AFECTA → Pendiente / INDETERMINADO]"

  - paso: "Confirmación del Usuario"
    obligatorio: true
    acciones:
      - "SI clasificación = Bug probable:"
      - "  > 🤷 Este hallazgo parece un **bug** que afecta funcionalidad. ¿Confirmas?"
      - "  > - 🐛 [B] Sí, es un bug → continuar con registro de bug"
      - "  > - 📋 [P] No, es solo un pendiente para después"
      - "SI clasificación = Pendiente probable:"
      - "  > 🤷 Este hallazgo parece un **pendiente** (no afecta funcionalidad). ¿Confirmas?"
      - "  > - 📋 [P] Sí, registrar como pendiente para después"
      - "  > - 🐛 [B] No, realmente es un bug que afecta algo"
      - "SI clasificación = Indeterminado:"
      - "  > 🤷 No puedo determinar si esto afecta funcionalidad. ¿Qué tipo de hallazgo es?"
      - "  > - 🐛 [B] Es un bug — algo no funciona correctamente"
      - "  > - 📋 [P] Es un pendiente — funciona pero podría mejorar"
      - "  > - 🔍 [I] No sé — necesito investigar primero"

  - paso: "Redirección con Contexto"
    obligatorio: true
    acciones:
      - "Preparar paquete de contexto recopilado:"
      - "  contexto_transferido:"
      - "    descripcion: [descripción del usuario]"
      - "    proyecto: [proyecto detectado o proporcionado]"
      - "    logs: [logs/evidencia si se adjuntaron]"
      - "    clasificacion_sugerida: [bug/pendiente/investigacion]"
      - "SI respuesta = [B]:"
      - "  Ejecutar >registrar_bug con contexto_transferido"
      - "  La herramienta destino SALTA su Paso 1 (Recepción) y continúa desde Paso 2 (Clasificación de Severidad)"
      - "SI respuesta = [P]:"
      - "  SI agente activo = Desarrollador:"
      - "    Informar: '📋 Los pendientes son responsabilidad del Arquitecto.'"
      - "    > 🤷 ¿Cómo proceder?"
      - "    > - 🐛 [B] Registrar como bug en su lugar (Desarrollador puede)"
      - "    > - 📝 [N] Anotar para que el Arquitecto lo registre después"
      - "    SI [N] → Mostrar resumen formateado para copiar al Arquitecto y TERMINAR"
      - "  SI agente activo = Arquitecto:"
      - "    Ejecutar >registrar_pendiente con contexto_transferido"
      - "    La herramienta destino SALTA su Paso 1 (Recepción) y continúa desde Paso 2 (Evaluación de Severidad)"
      - "SI respuesta = [I]:"
      - "  SI agente activo = Arquitecto:"
      - "    Ejecutar >registrar_pendiente con contexto_transferido + categoria='investigacion'"
      - "  SI agente activo = Desarrollador:"
      - "    Informar y anotar para el Arquitecto (mismo flujo que [P] + [N])"

salida:
  nota: "Esta herramienta no genera archivos propios. La salida es la de la herramienta destino."
  mensaje_redireccion: |
    ↪️ Redirigiendo a >[herramienta_destino]...
       Contexto transferido: descripción ✅ | proyecto ✅ | logs [✅/—]
       Continuando desde Paso [N] de >[herramienta_destino]

errores:
  sin_descripcion: {msg: "❌ Se requiere al menos una descripción del hallazgo", accion: "Solicitar descripción al usuario"}
```
