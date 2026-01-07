# 📝 Guía de Uso de Esta Plantilla

## Pasos para Crear una Nueva Herramienta

1. **Copiar este archivo** a `herramientas/[nombre].tool.md`
2. **Reemplazar todos los `[placeholders]`** con valores reales
3. **Personalizar las instrucciones mandatory** específicas
4. **Definir el proceso** con los pasos necesarios
5. **⚠️ MANTENER el paso_final** de actualización de sesión
6. **Registrar** en `herramientas/herramientas-activas.md`

## Secciones Obligatorias

| Sección | Obligatoria | Notas |
|---------|-------------|-------|
| `mandatory` | ✅ | Incluir las 4 instrucciones base |
| `identificacion` | ✅ | Nombre, comando, alias |
| `roles_autorizados` | ✅ | Al menos un rol |
| `prerequisitos` | ✅ | Puede estar vacío |
| `proceso` | ✅ | Mínimo paso_1 + paso_final |
| `salida` | ✅ | Incluir session_state en actualizados |
| `errores` | ✅ | Al menos un error común |
| `siguiente` | ⚠️ Recomendado | Guía el flujo de trabajo |

## ⚠️ Recordatorio Crítico

**El paso de "Actualizar Estado de Sesión" es OBLIGATORIO.**

Sin este paso:
- ❌ No hay trazabilidad de ejecución
- ❌ El sistema pierde contexto entre sesiones
- ❌ No se puede auditar qué herramientas se ejecutaron
- ❌ Las HUs no actualizan su estado correctamente

## Ejemplo de session_state.json Actualizado

```json
{
  "sesion_actual": {
    "ultima_herramienta": "nombre_herramienta",
    "ultima_actividad": "2026-01-06T10:30:00Z",
    "resultado_ejecucion": "exito"
  },
  "historial_herramientas": [
    {
      "herramienta": "nombre_herramienta",
      "timestamp": "2026-01-06T10:30:00Z",
      "artefactos": ["archivo1.md", "archivo2.md"],
      "resultado": "exito"
    }
  ]
}
```

---

## 🔧 Esqueleto: Herramienta (`.tool.md`)

```yaml
# ============================================
# [NOMBRE HERRAMIENTA] - Herramienta de IA
# ============================================
# Archivo: [nombre_herramienta].tool.md
# Versión: 1.0
# ============================================

# ============================================
# MANDATORY - INSTRUCCIONES INVIOLABLES
# ============================================
mandatory:
  # === BASE ESTÁNDAR (NO MODIFICAR) ===
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Actualizar session_state.json al finalizar"
    nunca_saltar: true
  # === CONFIGURACIÓN DE IDIOMA ===
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
    nunca_saltar: true
  # === ESPECÍFICAS DE LA HERRAMIENTA (PERSONALIZAR) ===
  - instruccion: "[Instrucción específica 1]"
    nunca_saltar: true
  - instruccion: "[Instrucción específica 2]"
    nunca_saltar: true

# ============================================
# IDENTIFICACIÓN
# ============================================
identificacion:
  nombre: "[Nombre Descriptivo de la Herramienta]"
  comando: ">[nombre_herramienta]"
  alias: [">[alias1]", ">[alias2]"]
  version: "1.0"

# ============================================
# ROLES AUTORIZADOS
# ============================================
roles_autorizados:
  - "[ROL1]"
  - "[ROL2]"

# ============================================
# PREREQUISITOS
# ============================================
prerequisitos:
  archivos_requeridos:
    - descripcion: "[Descripción del archivo requerido]"
      ubicacion: "[ruta o variable de ubicación]"
  archivos_opcionales:
    - "{{session_state_location}}"
    - "{{contexto_proyecto_location}}"

# ============================================
# PARÁMETROS
# ============================================
parametros:
  requeridos:
    - nombre: "[param_requerido]"
      tipo: string
      descripcion: "[Descripción del parámetro]"
  opcionales:
    - nombre: "[param_opcional]"
      tipo: string
      valores: [valor1, valor2, valor3]
      defecto: valor1
      descripcion: "[Descripción del parámetro]"

# ============================================
# PROCESO
# ============================================
# NOTA IMPORTANTE: El último paso siempre debe ser 
# "Actualizar Estado de Sesión" - Este paso es OBLIGATORIO
# para mantener la trazabilidad del sistema.
# ============================================
proceso:
  paso_1:
    nombre: "[Nombre del Paso 1]"
    obligatorio: true
    acciones:
      - "[Acción 1]"
      - "[Acción 2]"
      - "[Acción 3]"
    validaciones:
      - "[Validación si aplica]"
    si_error:
      "[tipo_error]": "[Mensaje y acción]"

  paso_2:
    nombre: "[Nombre del Paso 2]"
    obligatorio: true
    acciones:
      - "[Acción 1]"
      - "[Acción 2]"

  # ... más pasos según necesidad ...

  # ============================================
  # ⚠️ PASO OBLIGATORIO - NO ELIMINAR
  # ============================================
  # Este paso DEBE ser el último de toda herramienta.
  # Garantiza la trazabilidad y persistencia del estado.
  # ============================================
  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Abrir/crear {{session_state_location}}"
      - "Registrar herramienta ejecutada: [nombre_herramienta]"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Si hay HU activa, actualizar su estado"
      - "Guardar cambios en session_state.json"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "[nombre_herramienta]"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"

# ============================================
# SALIDA
# ============================================
salida:
  archivos_generados:
    - tipo: "[tipo_artefacto]"
      ruta: "[ruta del archivo generado]"
      condicion: "[si aplica condición]"
  
  archivos_actualizados:
    # ⚠️ session_state SIEMPRE debe estar en esta lista
    - "{{session_state_location}}"
  
  mensaje_exito: |
    ✅ [NOMBRE HERRAMIENTA] COMPLETADO
    
    📊 Resumen:
    - [Métrica 1]: [valor]
    - [Métrica 2]: [valor]
    
    📄 Artefactos:
    - [archivo generado]
    
    💡 Siguiente: >[herramienta_sugerida]

# ============================================
# ERRORES
# ============================================
errores:
  "[codigo_error]":
    mensaje: "❌ [Mensaje de error descriptivo]"
    accion: "[Acción sugerida para resolver]"
  "[otro_error]":
    mensaje: "⚠️ [Mensaje de advertencia]"
    accion: "[Acción alternativa]"

# ============================================
# SIGUIENTE
# ============================================
siguiente:
  herramienta: "[nombre_herramienta_siguiente]"
  comando: ">[comando]"
  descripcion: "[Descripción de por qué seguir con esta herramienta]"
  opciones:
    - comando: "[opción alternativa 1]"
      descripcion: "[cuándo usar esta opción]"
```
