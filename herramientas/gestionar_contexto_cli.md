# Herramienta: gestionar_contexto_cli

## Objetivo
(Ver descripción en Contenido Original.)

## Entradas Requeridas (Contexto)
(Ver Contenido Original.)

## Parámetros del Usuario
(Ver Contenido Original.)

## Roles Autorizados
(Ver Contenido Original.)

## Proceso Paso a Paso
(Descrito en Contenido Original.)

## Manejo de Errores y Casos Borde
(Descrito en Contenido Original.)

## Formato de Salida Esperado
(Descrito en Contenido Original.)

---

## Contenido Original

Herramienta: gestionar_contexto_cli
Objetivo
Automatizar la ingesta inicial, actualización y persistencia de un archivo de contexto arquitectónico del proyecto operando desde la raíz (CLI).
Entradas Requeridas (Contexto)
Principal: Estructura de directorios, archivos de build (pom.xml / build.gradle), código fuente.
Secundario (Opcional): Archivo de contexto previo existente, metadatos de versión.
Parámetros del Usuario: forzar_reconstruccion (bool), incluir_detalle_dependencias (bool).
Roles Autorizados:
- ArchDev Pro
- Arquitecto DevOps (modo lectura + validación)
Proceso Paso a Paso
Análisis Inicial:
- Verificar existencia de archivo de contexto objetivo (archdev_pro_context.md o nombre custom).
- Si existe y no se fuerza reconstrucción: cargar, validar integridad mínima (secciones clave presentes).
Ingesta (si no existe o se fuerza):
- Escanear estructura (módulos, capas, paquetes dominantes).
- Parsear archivo build extrayendo: lenguaje, versión Java, framework principal, dependencias core, plugins.
- Inferir estilo arquitectónico (capas vs hexagonal vs microservicios módulo único) por patrones de paquetes.
Consolidación:
- Generar secciones: Resumen, Stack, Arquitectura, Componentes Clave, Endpoints (si detecta *Controller.java), Dependencias Externas, Notas Técnicas.
Persistencia:
- Escribir/actualizar archivo contexto.
Actualización Incremental:
- Detectar cambios estructurales (nuevos módulos / eliminación) y fusionar preservando historial de cambios.
Manejo de Errores y Casos Borde
- Si no se detecta archivo de build: marcar advertencia y continuar con análisis parcial.
- Si parsing falla: registrar sección de errores y sugerir acción manual.
Formato de Salida Esperado
Archivo markdown consolidado listo para reutilización en futuras sesiones.
Finalización y Entrega
- Confirmar ruta del archivo creado/actualizado.
- Resumir dif principal (nuevas secciones o cambios).