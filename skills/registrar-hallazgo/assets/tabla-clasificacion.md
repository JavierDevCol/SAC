# Prompt: Clasificación de Hallazgos

> Archivo de referencia para que la skill clasifique hallazgos.

## Tabla de Clasificación

| Criterio | BUG | PENDIENTE |
|----------|-----|-----------|
| **Estado actual** | ROTO — no funciona | FUNCIONA — pero mejorable |
| **Impacto** | Bloquea funcionalidad | No bloquea, es mejora |
| **Urgencia** | Requiere corrección ahora | Puede esperar |
| **Error visible** | Sí (crash, error, exception) | No (warning, lento, código) |

## Indicadores de BUG

- Keywords: Error, failed, rejected, crash, exception, status 4xx/5xx
- Comportamiento: Funcionalidad que antes funcionaba ya no funciona
- Operación bloqueada o imposible de completar
- Datos incorrectos, perdidos o corruptos
- Redirección inesperada o loop infinito

## Indicadores de PENDIENTE

- Keywords: Warning, deprecated, TODO, FIXME, performance, slow
- Funciona correctamente pero muestra warning
- Mejora visual o de UX sin impacto funcional
- Deuda técnica identificada
- Revisar o verificar algo para más adelante

## Matriz de Decisión

| Usuario dice | Código confirma | Clasificación | Confianza |
|--------------|-----------------|---------------|-----------|
| "No funciona" | Código roto | BUG | Alta |
| "No funciona" | Código OK | PENDIENTE | Media |
| "Podría mejorar" | Código roto | BUG | Alta |
| "Podría mejorar" | Mejora confirmada | PENDIENTE | Alta |
| No está seguro | Código roto | BUG | Media |
| No está seguro | Mejora | PENDIENTE | Media |
| Conflicto | — | Priorizar código | — |

## Reglas de Clasificación

1. **Priorizar evidencia del código** sobre opinión del usuario
2. **Si hay conflicto** → El código manda
3. **Si no hay evidencia** → Clasificar como INCIERTO y pedir más detalles
4. **Si el usuario dice "ya corregido"** → Registrar como post-mortem
