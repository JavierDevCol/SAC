# Herramienta: refinar_hu

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

Herramienta: refinar_hu
Objetivo
Analizar una Historia de Usuario (HU) y producir: preguntas de clarificación, criterios de aceptación mejorados, desglose técnico vertical, estrategia y estimación justificadas.
Entradas Requeridas (Contexto)
Principal: Texto completo de la HU y criterios de aceptación actuales.
Secundario (Opcional): Contexto arquitectónico, restricciones no funcionales, dependencias conocidas.
Parámetros del Usuario: Formato de estimación (Story Points / Horas), nivel de detalle (alto|medio|bajo).
Roles Autorizados:
- ArchDev Pro
- Refinador HU
- Arquitecto DevOps (solo para impacto infra)
Proceso Paso a Paso
Análisis Inicial:
- Detectar ambigüedades, lagunas, criterios no medibles.
- Clasificar tipo de HU (feature, refactor, deuda, spike).
Refinamiento:
- Generar lista de Preguntas de Clarificación priorizadas.
- Proponer Criterios de Aceptación SMART adicionales o mejoras.
Desglose Técnico (Vertical Slicing):
- Identificar slices end-to-end (API -> Servicio -> Persistencia -> Tests).
- Para cada slice: definir tareas con identificador sugerido (TAG-PREFIJO).
Estrategia y Estimación:
- Recomendar enfoque (ej: TDD, incremental, feature toggle).
- Estimar esfuerzo justificando complejidad, incertidumbre y riesgo.
Riesgos y Dependencias:
- Listar bloqueadores potenciales y mitigaciones.
Finalización y Entrega:
- Emitir output estructurado con secciones numeradas.
Manejo de Errores y Casos Borde
- Si faltan criterios de aceptación: marcar severidad alta y priorizar preguntas.
- Si la HU es demasiado amplia: sugerir partición en HUs hijas.
Formato de Salida Esperado
1. Preguntas de Clarificación
2. Criterios de Aceptación Refinados
3. Desglose Técnico (checklist)
4. Estrategia y Estimación
5. Riesgos y Mitigaciones
6. Observaciones Adicionales