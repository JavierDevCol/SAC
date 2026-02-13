# Instrucciones Obligatorias (Mandatory)

1. Seguir el proceso paso a paso en orden secuencial
2. Validar prerequisitos antes de ejecutar
3. Pasos obligatorios **NO** se pueden omitir
4. Generar en idioma: `{{preferencias.idioma_documentacion}}`
5. Si `{{usuario.incluir_firma_en_documentos}}` = true, agregar pie de documento:

---
✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}

---

## Estructura Estándar de Proceso

Toda herramienta debe seguir esta estructura:

1. **Inicialización de Parámetros** - Establecer valores por defecto
2. **Validación de Prerequisitos** - Verificar archivos y condiciones requeridas
3. **Ejecución del Proceso** - Pasos específicos de la herramienta
4. **Generación de Salida** - Crear/actualizar archivos
5. **Actualización de Estado** - Modificar backlog u otros registros

---

## Manejo de Errores

| Situación | Acción |
|-----------|--------|
| Prerequisito faltante | Informar y detener ejecución |
| Parámetro requerido ausente | Solicitar al usuario |
| Error en paso obligatorio | Detener y reportar |
| Error en paso opcional | Detener y reportar |

---

## Formato de Salida

Toda herramienta debe definir:

- **archivos_generados:** Ruta y nombre del archivo creado
- **archivos_actualizados:** Lista de archivos modificados
- **mensaje_exito:** Confirmación al usuario
- **siguiente:** Comando sugerido para continuar flujo

