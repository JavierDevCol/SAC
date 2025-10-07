# Herramienta: diagnosticar_devops

## Objetivo
Realizar diagnóstico estructurado de pipeline, infraestructura y prácticas DevSecOps para proponer mejoras priorizadas.

## Entradas Requeridas (Contexto)
Principal: Descripción del entorno actual (cloud, orquestador, pipeline), fragmentos de config (Dockerfile, workflow CI, terraform, helm charts).
Secundario (Opcional): Requisitos no funcionales (SLOs, RTO/RPO), límites de costos.

## Parámetros del Usuario
parámetros del Usuario: profundidad (rápido|completo), foco (seguridad|rendimiento|costo|equilibrado).

## Roles Autorizados:
- Arquitecto DevOps
- ArchDev Pro (modo lectura / asesoría)

## Proceso Paso a Paso

### Análisis Inicial:
- Clasificar madurez (Ad-hoc, Repeatable, Managed, Optimized) basado en insumos.
- Detectar gaps críticos (ausencia de tests, falta de escaneo de vulnerabilidades, deployments manuales).

### Sección Pipelines CI/CD:
- Revisar etapas (build, test, security scan, deploy) y cobertura.

### Seguridad (DevSecOps):
- Verificar presencia de SAST, DAST, dependencia scanning, secret scanning.

### Infraestructura:
- Evaluar IaC (Terraform/Bicep/CloudFormation) vs provisión manual.
- Revisar observabilidad (logs, métricas, trazas) y alertas.

### Costos y Escalabilidad:
- Identificar posibles sobreaprovisionamientos o ausencia de autoescalado.

### Recomendaciones Priorizadas:
- Generar tabla conceptual: Prioridad (Alta/Media/Baja), Impacto, Esfuerzo estimado.

### Plan de Implementación Incremental:
- Fases (0-Estabilizar, 1-Visibilidad, 2-Automación, 3-Optimización).

## Manejo de Errores y Casos Borde
- Si faltan datos críticos, emitir lista de datos requeridos y detener recomendaciones profundas.

## Formato de Salida Esperado
1. Resumen Ejecutivo
2. Estado Actual (Matriz de Madurez)
3. Hallazgos Clave
4. Recomendaciones Priorizadas
5. Plan Incremental
6. Riesgos y Mitigaciones

## Finalización y Entrega
- Confirmar si generar versión exportable (documento_estandar).