---
name: planificar-hu
description: Genera planes de implementación para HUs aprobadas. Soporta modo plano y particionado con tasks. Selecciona fases según arquitectura del proyecto. Ejecuta esta skill cuando una HU esté en estado [A] Aprobada y necesite un plan de implementación.
---

## Parámetros

| Parámetro | Tipo | Default | Valores posibles | Descripción |
|-----------|------|---------|------------------|-------------|
| `id_hu` | string | — | Ej: `HU-001`, `HU-012` | Identificador de la HU a planificar |
| `--proyecto` | string | null | Ej: `mi-app`, `backend` | Proyecto específico (auto-detectado) |
| `--incluir_migraciones` | flag | true | `--incluir_migraciones` (activar) | Incluir plan de migraciones BD |
| `--incluir_rollback` | flag | true | `--incluir_rollback` (activar) | Incluir plan de rollback |

## Fases según Arquitectura

| Arquitectura | Fases |
|--------------|-------|
| **Hexagonal** | 1. Infraestructura → 2. Dominio → 3. Aplicación → 4. Adaptadores → 5. Testing |
| **MVC** | 1. Infraestructura → 2. Modelos → 3. Controladores → 4. Vistas → 5. Testing |
| **Capas** | 1. Infraestructura → 2. Datos → 3. Negocio → 4. Presentación → 5. Testing |
| **Script/CLI** | 1. Setup → 2. Lógica Principal → 3. Testing |
| **Frontend** | 1. Setup → 2. Componentes → 3. Hooks/Services → 4. Integración → 5. Testing |
| **Default** | 1. Preparación → 2. Implementación → 3. Testing |
| **Bugfix** | 1. Reproducción → 2. Corrección → 3. Testing Regresión |

## Instrucciones

### 1. Cargar Configuración

- Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener `archivos.backlog`, `artifacts.hu_folder`, `artifacts.contextos_folder`, `plantillas.hu.plan`
- Leer `.SAC/config/CONFIG_USER.yaml` (si existe) → obtener idioma

### 2. Cargar HU y Contexto

- Verificar que existe `{hu_folder}/[ID-HU]/`
- Leer `{hu_folder}/[ID-HU]/HU.md`
- Extraer campo 'Tipo' (si no existe → asumir Funcional)
- **SI Tipo = Bug:**
  1. Leer `{hu_folder}/[ID-HU]/RefinamientoBug.md`
  2. Extraer: Causa Raíz, Archivos Afectados, Corrección Sugerida
  3. Usar `estructura_fases.bugfix`
- **SI Tipo != Bug:**
  1. Leer `{hu_folder}/[ID-HU]/Refinamiento.md`
  2. Verificar que tiene '## Aprobación' con '**Estado** | ✅ Aprobada'
  3. Si existe '### Directrices de Planificación' → Incorporar como contexto prioritario
- Cargar contexto del proyecto
- Identificar HUs relacionadas en backlog
- Detectar componentes reutilizables de HUs [X]

### 3. Detección de Ambigüedades

- Analizar HU, CA y ADR buscando: tecnologías no especificadas, rutas ambiguas, decisiones técnicas faltantes
- Si hay ambigüedades → Listar preguntas claras
- **PAUSAR** y esperar respuestas del usuario

### 4. Detectar Arquitectura y Seleccionar Fases

- **SI tipo_hu = 'Bug'** → Usar `estructura_fases.bugfix` directamente
- **SI tipo_hu != 'Bug':**
  - Leer '## 4. Arquitectura' en contexto_proyecto
  - Extraer campo 'Estilo'
  - Mapear a `estructura_fases`:

| Estilo contiene | Fases a usar |
|-----------------|--------------|
| Hexagonal | hexagonal |
| MVC | mvc |
| Capas | capas |
| Script o CLI | script |
| Frontend o React/Vue/Angular | frontend |
| Default | default |

- Si estructura ambigua → PREGUNTAR al usuario

### 5. Diseño de Componentes

- Identificar componentes a crear/modificar
- Definir interfaces y contratos según reglas arquitectónicas
- Usar rutas REALES documentadas (NO genéricas)
- Si ruta no existe → PREGUNTAR al usuario

### 6. Planificación de Migraciones (opcional)

**Condición:** `--incluir_migraciones=true` y hay cambios en BD

- Diseñar scripts de migración
- Definir nomenclatura (Flyway/Liquibase)
- Incluir rollback si `--incluir_rollback=true`

### 7. Secuenciación de Tareas

**Modo Plano:**
- Ordenar tareas por dependencias
- Agrupar en fases según `fases_plan`
- Numerar: EJEC-01, EJEC-02, EJEC-03...
- Asignar rutas de '### Estructura del Proyecto'
- Asignar estimación por tarea

**Modo Particionada:**
1. Extraer tasks del refinamiento
2. Construir tabla 'Dependencias entre Tasks'
3. Para CADA task:
   - Leer CAs granulares y desglose técnico
   - Seleccionar fases según stack de la task
   - Numerar con IDs compuestos: TASK-N-EJEC-NN
4. Generar tabla 'Progreso General' por task
5. Agregar 'Fase Final: Validar CAs de Integración'

### 8. Generación del Plan

**SIEMPRE:**
- Crear `{hu_folder}/[ID-HU]/Plan.md` desde plantilla
- Rellenar metadata (ID-HU, título, fecha, estimación, modo)

**Modo Plano:**
- Generar tabla de progreso + secciones de fase
- Fase Final: tabla de CAs (ID + resumen)

**Modo Particionada:**
- En Plan.md del padre: generar resumen de tasks + dependencias + progreso general
- **Crear Plan.md en CADA task hija:**
  - `{hu_folder}/[ID-HU]-TASK-1/Plan.md` → fases internas de la task
  - `{hu_folder}/[ID-HU]-TASK-2/Plan.md` → fases internas de la task
  - `{hu_folder}/[ID-HU]-TASK-N/Plan.md` → fases internas de la task
- Cada Plan.md de task contiene:
  - Metadata de la task (ID, traza CA padre, estimación, dependencias)
  - Sub-fases internas con tareas técnicas (IDs: TASK-N-EJEC-NN)
  - Sección 'Validar CAs de TASK-N' con checkboxes
- Actualizar backbone índice: [A] → [P]

## Restricciones

- Generar plan alineado con arquitectura del proyecto
- Incluir tareas de testing en el plan
- Especificar orden de ejecución y dependencias
- Usar plantilla `plantillas.hu.plan`
- Incluir TODOS los CAs en Fase Final
- **SI Tipo=Bug** → Usar estructura bugfix
- **SI Modo=Particionada** → Organizar por tasks con fases internas
- Numerar tareas técnicas con IDs compuestos: TASK-N-EJEC-NN

## Formato de salida

**Modo Plano:**
```
✅ PLAN GENERADO: [ID-HU]
📁 Archivo: {hu_folder}/[ID-HU]/Plan.md
📊 Modo: Plano | Fases: [N] | Tareas: [M] | Estimación: [X]h
Siguiente: >ejecutar_plan [ID-HU]
```

**Modo Particionada:**
```
✅ PLAN GENERADO: [ID-HU]
📁 Plan padre: {hu_folder}/[ID-HU]/Plan.md
📊 Modo: Particionada | Tasks: [N]
   ├── {hu_folder}/[ID-HU]-TASK-1/Plan.md  (SP: [X])
   ├── {hu_folder}/[ID-HU]-TASK-2/Plan.md  (SP: [Y])
   └── {hu_folder}/[ID-HU]-TASK-N/Plan.md  (SP: [Z])
Siguiente: >ejecutar_plan [ID-HU]
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| HU no está aprobada | No tiene [A] | Ejecutar >validar_hu primero |
| Sin contexto de proyecto | No configurado | Ejecutar >tomar_contexto |

## Después de ejecutar

- `>ejecutar_plan [ID-HU]` — Ejecutar el plan generado
