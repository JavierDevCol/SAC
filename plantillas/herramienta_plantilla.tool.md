# 📝 Guía de Uso de Esta Plantilla

## Pasos para Crear una Nueva Herramienta

1. **Copiar este archivo** a `herramientas/[nombre].tool.md`
2. **Reemplazar todos los `[placeholders]`** con valores reales
3. **Personalizar las instrucciones mandatory** específicas
4. **Definir el proceso** con los pasos necesarios
5. **Recomendación**: No dejar comentarios YAML en la herramienta final. Los comentarios (`# ...`) son solo guía para esta plantilla.

## Secciones Obligatorias

| Sección | Obligatoria | Notas |
|---------|-------------|-------|
| `mandatory` | ✅ | Incluir las 4 instrucciones base |
| `identificacion` | ✅ | Nombre, comando, alias |
| `prerequisitos` | ✅ | Puede estar vacío |
| `proceso` | ✅ | Mínimo paso_1 + paso_final |
| `salida` | ✅ | Incluir session_state en actualizados |
| `errores` | ✅ | Al menos un error común |
| `siguiente` | ⚠️ Recomendado | Guía el flujo de trabajo |

---

## 🔧 Esqueleto: Herramienta (`.tool.md`)
---
nombre: [NOMBRE_HERRAMIENTA]
comando: [COMANDO_ACTIVACION]
alias: [COMANDOS SINONIMOS QUE ACTIVANLA HERRRAMIENTA]
---
Cuerpo prompt de la herramienta en formato yaml: 
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
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
  - instruccion: "Actualizar session_state.json al finalizar"
  - instruccion: "Nunca saltar proceso.paso_final"
  # === CONFIGURACIÓN DE IDIOMA ===
  - instruccion: "Generar TODOS los artefactos/documentos en el idioma definido en 'idiomas.documentacion'"
  # === ESPECÍFICAS DE LA HERRAMIENTA (PERSONALIZAR) ===
  - instruccion: "[Instrucción específica 1]"
  - instruccion: "[Instrucción específica 2]"

# ============================================
# PREREQUISITOS
# ============================================
prerequisitos:
  archivos_requeridos:
    - descripcion: "[Descripción del archivo requerido]"
      ubicacion: "[ruta o variable de ubicación]"
  archivos_opcionales:
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
  - paso: "[Nombre del Paso 1]"
    obligatorio: true  # true | false - Si el paso se puede omitir
    acciones: ["Acción 1", "Acción 2", "Acción 3"]
    validaciones:  # Opcional
      - condicion: "[Condición a validar]"
        si_cumple: "[Acción cuando cumple]"
        si_no_cumple: "[Acción cuando NO cumple]"
    si_error:
      "[tipo_error]": "[Mensaje y acción]"
  
  - paso: "[Nombre del Paso 2]"
    obligatorio: false
    acciones: ["Acción 1", "Acción 2"]
  
  # ... más pasos según necesidad ...

# ============================================
# SALIDA
# ============================================
salida:
  archivos_generados:
      ruta: "[ruta del archivo generado]"
      template: "Template corto de como se visualiza el archivo generado"
 # mensaje_exito es opcional 
  mensaje_exito: |    
    ✅ [NOMBRE HERRAMIENTA] COMPLETADO
    
    📊 Resumen:
    - [Métrica 1]: [valor]
    - [Métrica 2]: [valor]
    
    📄 Artefactos:
    - [archivo generado]
    


# ============================================
# ERRORES
# ============================================
errores:
  "[codigo_error]": {msg: "❌ [Mensaje de error descriptivo]", accion: "[Acción sugerida para resolver]"}

# ============================================
# SIGUIENTE
# ============================================
siguiente:
  - { accion: "[Acción sugerida para resolver]", desc: "Mayor impacto/menor esfuerzo" }
  - { comando: "[nombre herramienta]", desc: "Mayor impacto/menor esfuerzo", chat_agente: "[Agente que debe tener activo en el nuevo chat]" }

```
