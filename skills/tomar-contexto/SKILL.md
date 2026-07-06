---
name: tomar-contexto
description: Analiza un proyecto software y genera archivos de contexto. Detecta workspace, stack, arquitectura, DevOps y genera diagramas. Ejecuta esta skill cuando el usuario pida analizar un proyecto, configurar el workspace, o cuando se necesite contexto para otras operaciones del sistema SAC.
---

## Parámetros

| Parámetro | Tipo | Default | Valores posibles | Descripción |
|-----------|------|---------|------------------|-------------|
| `--profundidad_analisis` | option | `exhaustivo` | `basico`, `completo`, `exhaustivo` | Cuánto analizar del proyecto |
| `--nombre_proyecto` | string | — | Ej: `mi-app`, `backend` | Proyecto específico (multi-proyecto) |
| `--all` | flag | false | `--all` (activar) | Analizar todos los proyectos |
| `--force` | flag | false | `--force` (activar) | Regenerar aunque exista contexto |

## Instrucciones

### 1. Inicialización y Confirmación

- **Cargar configuración del sistema** antes de cualquier operación:
  1. Leer `.SAC/config/CONFIG_SYSTEM.yaml` → obtener rutas: `artifacts_folder`, `hu_folder`, `contextos_folder`, `adr_folder`, `backlog`, `workspace`, `plantillas.*`
  2. Leer `.SAC/config/CONFIG_USER.yaml` (si existe) → obtener: idioma, nombre proyecto, `rutas_override.artifacts_folder` (si existe)
  3. Si CONFIG_USER tiene `rutas_override.artifacts_folder`, usar esa ruta en lugar de la de CONFIG_SYSTEM
  4. Si no existe `.SAC/config/` → Informar: "No hay instalación previa. Ejecuta el instalador o crea la configuración manualmente"
- Establecer valores por defecto: `profundidad_analisis='exhaustivo'`
- Detectar tipo de workspace (ver paso 2)
- **SI ya existe contexto** y no se usó `--force` → Informar y preguntar:
  > ℹ️ Ya existe contexto del proyecto. ¿Qué deseas hacer?
  > - [U] Usar el existente
  > - [R] Regenerar (sobrescribir)
- **Mostrar configuración propuesta al usuario y ESPERAR confirmación antes de continuar:**
  > ⚙️ Configuración:
  > - Profundidad: [valor]
  > - Tipo workspace: [Mono/Multi]
  > - Proyectos detectados: [lista]
  > - Ruta artifacts: [ruta obtenida de config]
  >
  > ¿Confirmas esta configuración? [Sí/No/Editar]

### 2. Detectar Tipo de Workspace

- Buscar marcadores de proyecto en la raíz según:
  - Java: `pom.xml`, `build.gradle`, `build.gradle.kts`
  - JavaScript: `package.json`
  - Python: `pyproject.toml`, `setup.py`, `requirements.txt`
  - .NET: `*.csproj`, `*.sln`
  - Rust: `Cargo.toml`
  - Go: `go.mod`
- Si 1+ marcador en raíz → **MODO_UNICO**
- Si 0 en raíz + 2+ subcarpetas con marcadores → **MODO_MULTI**
- Si no hay marcadores → Informar: "No se detectó ningún proyecto en esta ruta"

### 3. Listar Proyectos (solo MODO_MULTI)

- Escanear subcarpetas con marcadores de proyecto
- Mostrar tabla: `# | Proyecto | Stack | Ruta`
- Si se especificó `--nombre_proyecto` → Filtrar solo ese proyecto
- Si se usó `--all` → Analizar todos
- Si no se especificó nada → Preguntar al usuario qué proyecto analizar

### 4. Detectar Stack Tecnológico

- Identificar lenguaje principal y versión
- Detectar framework y versión
- Identificar herramientas de build, testing, linting
- Generar lista detallada de componentes con versiones exactas

### 5. Analizar Arquitectura

- Identificar estilo arquitectónico (Hexagonal, MVC, Capas, Event-Driven, Microservicios, Script, Monolito)
- Mapear estructura de carpetas y su propósito
- Detectar componentes principales y sus responsabilidades
- En multi-proyecto: identificar relaciones de dependencia entre proyectos (quién consume a quién, tipo de comunicación)

### 6. Evaluar DevOps

- Buscar Dockerfile, docker-compose
- Detectar CI/CD (GitHub Actions, GitLab CI, Azure Pipelines)
- Identificar IaC (Terraform, Bicep, Pulumi)
- Identificar puertos expuestos y profiles/entornos

### 7. Generar Scorecard

- Evaluar y puntuar (1-10):
  - Arquitectura: claridad, separación de responsabilidades, documentación
  - Stack: idoneidad para el tipo de proyecto, versiones actualizadas
  - Testing: cobertura, tipos de tests, herramientas
  - DevOps: automatización, containers, CI/CD
  - Documentación: README, ADRs, comentarios relevantes
- Identificar puntos de atención por categoría (críticos, importantes, sugerencias)

### 8. Generar Diagramas con Sub-Agente

- **Delegar a sub-agente** la generación de diagramas Mermaid:
  > "Genera diagramas Mermaid del proyecto analizado. Usa la skill `mermaid-diagram` para aplicar estándares de colores y formato.
  >
  > Diagramas a generar:
  > 1. **Diagrama de estructura** (flowchart TD): mostrar organización de carpetas y componentes
  > 2. **Diagrama de clases** (class diagram): mostrar entidades principales y relaciones
  > 3. **Diagrama de secuencia** (sequence diagram): mostrar flujo principal del sistema (request → controller → service → repository → DB)
  >
  > Contexto del proyecto: [información del análisis previo]
  > Stack detectado: [stack]"
- El sub-agente retorna los 3 diagramas en formato ` ```mermaid ` listo para insertar

### 9. Crear Archivos de Contexto

Usar las rutas cargadas del paso 1 (CONFIG_SYSTEM / CONFIG_USER):

```
Estructura de artifacts (usar rutas de config):
{artifacts_folder}/
├── HU/
│   └── [ID-HU]/
│       ├── HU.md              (desde plantillas.hu.hu)
│       ├── Refinamiento.md    (desde plantillas.hu.refinamiento)
│       ├── RefinamientoBug.md (solo bugs, desde plantillas.hu.refinamiento_bug)
│       ├── Plan.md            (desde plantillas.hu.plan)
│       └── Tracking.md        (desde plantillas.hu.tracking)
├── {adr_folder relative}/
├── {code_smells_folder relative}/
├── {contextos_folder relative}/
├── {deuda_tecnica_folder relative}/
├── {pendientes_folder relative}/
├── backlog_desarrollo.md      (desde plantillas.backlog)
├── lecciones_aprendidas.md    (desde plantillas.lecciones_aprendidas)
├── pendientes.md              (desde plantillas.pendientes)
└── workspace.md               (desde plantillas.workspace)
```

**Crear carpetas del sistema** (usar rutas de CONFIG_SYSTEM):
- Crear `{artifacts_folder}/` y subcarpetas: `HU/`, `ADR/`, `code_smells/`, `{contextos_folder}/`, `deuda_tecnica/`, `pendientes/`
- Crear `.SAC/config/`, `.SAC/plantillas/`, `.SAC/reglas/` si no existen

**Generar archivos de contexto:**
- **Mono-Proyecto:**
  - Generar `{contextos_folder}/contexto_proyecto.md` desde `{plantillas.contexto}`
  - Generar `{archivos.workspace}` desde `{plantillas.workspace}` con Tipo: Mono-Proyecto
- **Multi-Proyecto:**
  - Por cada proyecto: generar `{contextos_folder}/contexto_proyecto_{nombre}.md`
  - Detectar y documentar relaciones entre proyectos (sección "Dependencias de Proyecto")
  - Generar `{archivos.workspace}` con Tipo: Multi-Proyecto

### 10. Validación Final

- Verificar que los documentos generados contengan la información correcta del análisis
- Preguntar al usuario:
  > ¿El contexto generado es correcto?
  > - [OK] Correcto, guardar
  > - [EDITAR] Necesito hacer correcciones
- Si el usuario elige EDITAR → Mostrar el documento y permitir ediciones específicas
- Especificar con qué profundidad se realizó el análisis (`--profundidad_analisis`)

## Restricciones

- **SIEMPRE** esperar confirmación del usuario en el paso 1 ANTES de ejecutar análisis
- **SIEMPRE** detectar tipo de workspace ANTES de analizar contenido
- En multi-proyecto: generar workspace.md + contextos individuales por proyecto
- **NUNCA** mezclar contextos de diferentes proyectos
- Si el proyecto está vacío → generar contexto básico con la información disponible
- Si no se detectan marcadores → informar y sugerir verificar la ruta

## Formato de salida

**Mono-Proyecto:**
```
✅ WORKSPACE CONFIGURADO (Mono-Proyecto)
📁 .SAC/workspace.md
📁 .SAC/artifacts/contextos/contexto_proyecto.md
📊 Scorecard: Arq X/10 | Stack X/10 | Test X/10 | DevOps X/10 | Docs X/10
```

**Multi-Proyecto:**
```
✅ WORKSPACE CONFIGURADO (Multi-Proyecto)
📁 .SAC/workspace.md
📁 .SAC/artifacts/contextos/ (N contextos generados)
📊 Scorecard Global: X/10
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Sin archivos detectables | Proyecto vacío o ruta incorrecta | Verificar ruta, generar contexto básico |
| No se detectó ningún proyecto | Sin marcadores en raíz ni subcarpetas | Verificar que estés en la raíz del proyecto |
| Proyecto '[nombre]' no encontrado | Nombre incorrecto en multi-proyecto | Ejecutar sin `--nombre_proyecto` para listar |
| Ya existe contexto | Contexto previo sin `--force` | Responder [R] para regenerar o [U] para usar existente |

## Después de ejecutar

- `>init_reglas_arquitectonicas` — Configurar reglas arquitectónicas del proyecto
- `>refinar_hu [ID-HU]` — Refinar una HU con el contexto disponible
- `>diagnosticar_devops` — Evaluar madurez DevOps más a fondo
