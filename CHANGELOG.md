# 📝 CHANGELOG - SAC

> **Sistema:** SAC - Sistema Agéntico COCHAS  
> **Archivo:** Índice centralizado de versiones de todos los componentes

---

## 📊 Estado Actual de Componentes

| Componente | Versión Actual | Última Actualización |
|------------|----------------|----------------------|
| **Sistema SAC** | 7.21.0 | 2026-04-28 |
| **Configuración Sistema** (`config/CONFIG_SYSTEM.yaml`) | 7.21.0 | 2026-04-28 |
| **Configuración Usuario** (`config/CONFIG_USER.template.yaml`) | 7.9.0 | 2026-04-24 |
| **Roles SAC** (`agentes/*.rol.md`) | 7.17.0 | 2026-04-28 |
| **Herramientas** (`herramientas/*.tool.yaml`) | 7.21.0 | 2026-04-28 |
| **Plantillas** (`plantillas/`) | 7.21.0 | 2026-04-28 |
| **Guía de Comandos** (`guias/guia_comandos.md`) | 7.15.0 | 2026-04-28 |
| **Guía de Roles** (`guias/guia_roles_activos.md`) | 3.0 | 2026-01-05 |
| **Guía Ciclo de Vida** (`guias/guia_ciclo_vida_tareas.md`) | 7.15.0 | 2026-04-28 |

---

## 🚀 Historial de Versiones

### [7.21.0] - 2026-04-28

#### 📦 Refactor: Nomenclatura jerárquica TASK-N / TASK-N-EJEC-NN + propagación [~] candidato

**Objetivo:** Unificar nomenclatura de tasks funcionales y tareas técnicas con IDs compuestos auto-documentados. Eliminar marcas `⟵T[N]` (redundantes con IDs compuestos). Formalizar cadena de satisfacción ascendente con estado intermedio `[~]` candidato.

**Nomenclatura nueva:**
| Antes | Ahora | Contexto |
|-------|-------|----------|
| `[ID-HU]-T1` | `[ID-HU]-TASK-1` | Task funcional |
| `T01`, `T02` | `TASK-1-EJEC-01`, `TASK-1-EJEC-02` | Tarea técnica (compuesta, por task) |
| `CA-T1-01` | `CA-TASK1-01` | CA granular |
| `T03 ⟵T1` | `TASK-1-EJEC-03` | Dependencia cross-task (auto-documentada) |

**Propagación ascendente:**
| Estado | Símbolo | Significado |
|--------|---------|-------------|
| Pendiente | `[ ]` | No validado aún |
| Candidato | `[~]` | CAs granulares pasan, pendiente integración |
| Cumplido | `[X]` | Validado contra código + integración |
| Fallido | `[!]` | Validación falló |

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|--------|
| `refinar_hu.tool.yaml` | Nomenclatura: `T1`→`TASK-1`, `CA-T1-01`→`CA-TASK1-01`, `[ID-HU]-T[N]-API-01`→`[ID-HU]-TASK-N-API-01` |
| `refinar_hu.tool.yaml` | Cadena satisfacción: incluye estado `[~]` candidato antes de `[X]` |
| `validar_hu.tool.yaml` | Nomenclatura: `T[N]`→`TASK-N` en cadena de satisfacción |
| `planificar_hu.tool.yaml` | Nomenclatura: `T01`→`TASK-N-EJEC-NN` (IDs compuestos por task) |
| `planificar_hu.tool.yaml` | Eliminadas marcas `⟵T[N]` — IDs compuestos son auto-documentados |
| `ejecutar_plan.tool.yaml` | Nomenclatura: IDs compuestos en actualización en tiempo real, reanudación, mensajes |
| `ejecutar_plan.tool.yaml` | Nuevo: CAs granulares pasan a `[~]` candidato (no `[X]` directo) |
| `validar_ca.tool.yaml` | Nuevo: lógica de propagación ascendente `[ ]→[~]→[X]` con estados formalizados |
| `validar_ca.tool.yaml` | Nuevo: `--scope integracion` confirma `[~]→[X]` o `[~]→[!]` |

#### ✅ Cambios en Plantillas

| Cambio | Detalle |
|--------|--------|
| `refinamiento_hu_plantilla.md` | Tasks: `[ID-HU]-T1`→`[ID-HU]-TASK-1`, CAs: `CA-T1-01`→`CA-TASK1-01` |
| `refinamiento_hu_plantilla.md` | Desglose: `[ID-HU]-T1-API-01`→`[ID-HU]-TASK-1-API-01` |
| `refinamiento_hu_plantilla.md` | Cadena satisfacción: incluye `[~]` candidato |
| `plan_implementacion_plantilla.md` | Tareas técnicas: `T01`→`TASK-1-EJEC-01` (IDs compuestos) |
| `plan_implementacion_plantilla.md` | Eliminada notación `⟵T[N]` y nota explicativa — reemplazada por nota sobre prefijos |
| `plan_implementacion_plantilla.md` | CAs: `CA-T1-01`→`CA-TASK1-01` en tablas de verificación |
| `backlog_desarrollo_plantilla.md` | Índice Rápido: `T1,T2`→`TASK-1,TASK-2` |
| `backlog_desarrollo_plantilla.md` | Estados [R], [A], [P]: `[ID-HU]-T1`→`[ID-HU]-TASK-1` |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|--------|
| `CONFIG_SYSTEM.yaml` | version 7.20.0 → 7.21.0 |

### [7.20.0] - 2026-04-28

#### 📦 Feat: Plan lean + herramienta >validar_ca — eliminación de redundancia refinamiento↔plan

**Objetivo:** Eliminar la duplicación de CAs entre refinamiento y plan de implementación. El refinamiento es la fuente de verdad de QUÉ se necesita (CAs, tasks, criterios). El plan define CÓMO se implementa (pasos precisos de código, archivos, rutas) y trackea ESTADO de verificación. Nueva herramienta `>validar_ca` valida código implementado contra CAs del refinamiento.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|---------|
| `validar_ca.tool.yaml` v1.0 (NUEVA) | Herramienta del Desarrollador para validar CAs contra código real y tests |
| `validar_ca.tool.yaml` | Parámetros: `id_hu`, `task_id` (opcional), `scope` (granulares/integracion/todos) |
| `validar_ca.tool.yaml` | Lee CAs del refinamiento (fuente de verdad), verifica contra filesystem y tests, marca checkboxes en plan |
| `validar_ca.tool.yaml` | Soporta validación parcial por task (granulares) y validación completa (integración) |
| `ejecutar_plan.tool.yaml` | Paso "Validar CAs" refactorizado: delega a `>validar_ca` en vez de validar inline |
| `ejecutar_plan.tool.yaml` | Nuevo en sección `siguiente`: referencia a `>validar_ca` |
| `planificar_hu.tool.yaml` | Generación del Plan: NO copia CAs al plan. Genera tabla de estado (ID + resumen) con referencia al refinamiento |
| `planificar_hu.tool.yaml` | Nuevo campo 'Refinamiento' en Metadata del plan (link al archivo fuente) |
| `planificar_hu.tool.yaml` | Instrucción explícita: pasos de implementación PRECISOS (archivos, código, rutas exactas) |

#### ✅ Cambios en Plantillas

| Cambio | Detalle |
|--------|---------|
| `plan_implementacion_plantilla.md` v3.0 → v4.0 | Metadata: nuevo campo `Refinamiento` (ruta al archivo fuente de verdad) |
| `plan_implementacion_plantilla.md` | Fase Final: CAs como tabla de estado (ID + resumen + checkbox) en vez de texto completo copiado |
| `plan_implementacion_plantilla.md` | Sección Particionada: Validar CAs por task como tabla de estado + referencia a `>validar_ca` |
| `plan_implementacion_plantilla.md` | Notas: eliminada sección Riesgos (ya vive en refinamiento). Solo Decisiones Técnicas |
| `plan_implementacion_plantilla.md` | Frontmatter: nuevo campo `validado_por: >validar_ca` |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|---------|
| `CONFIG_SYSTEM.yaml` | version 7.19.0 → 7.20.0 |

#### 📊 Principio de diseño: Separación de responsabilidades

| Artefacto | Responsabilidad | NO contiene |
|---|---|---|
| **Refinamiento** | QUÉ (CAs, tasks, aceptación, riesgos) | Código, pasos de implementación |
| **Plan** | CÓMO (pasos precisos, archivos, código, estado) | Texto completo de CAs, riesgos |
| **>validar_ca** | VERIFICAR (código vs CAs del refinamiento) | Implementación de código |

---

### [7.19.0] - 2026-04-28

#### 📦 Feat: Soporte de ejecución por tasks funcionales en pipeline planificar→ejecutar

**Objetivo:** Completar el soporte end-to-end de HUs particionadas en tasks funcionales. El refinador ya soportaba partición (v7.18.0), pero el planificador y ejecutor no sabían generar ni iterar planes organizados por tasks. Esta versión cierra la brecha: planes conscientes de tasks con dependencias explícitas, ejecución granular por task (completa, task_por_task, task_especifica), y retrocompatibilidad total con HUs planas.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|---------|
| `ejecutar_plan.tool.yaml` v4.3 → v5.0 | Nuevos `modo_ejecucion`: `task_por_task` (pausa entre tasks) y `task_especifica` (ejecuta solo una task) |
| `ejecutar_plan.tool.yaml` | Nuevo parámetro `task_id`: ID de task funcional para modo `task_especifica` |
| `ejecutar_plan.tool.yaml` | Nuevo paso "Resolver Modo de Ejecución": detecta campo Modo del plan, degrada modos incompatibles con aviso (nunca rompe), valida dependencias entre tasks |
| `ejecutar_plan.tool.yaml` | Paso "Ejecutar Fases" transformado a "Ejecutar Plan según Modo Resuelto": doble estrategia (acciones_modo_plano = comportamiento actual, acciones_modo_particionada = iteración por tasks → fases internas) |
| `ejecutar_plan.tool.yaml` | Paso "Validar CAs" evolucionado: CAs granulares por task + CAs de integración al final |
| `ejecutar_plan.tool.yaml` | Paso "Finalización" evolucionado: soporta finalización parcial (task_especifica con tasks pendientes mantiene HU en [E]) |
| `ejecutar_plan.tool.yaml` | Salida diferenciada: `mensaje_exito_completo` vs `mensaje_exito_task` |
| `planificar_hu.tool.yaml` v4.1 → v5.0 | Nuevas mandatory: organizar plan por tasks si Modo=Particionada, numeración global de tareas técnicas |
| `planificar_hu.tool.yaml` | Paso "Secuenciación de Tareas" bifurcado: Modo Plano (sin cambios) vs Modo Particionada (tasks → fases internas, tabla dependencias, numeración global, marca cross-task ⟵T[N]) |
| `planificar_hu.tool.yaml` | Paso "Generación del Plan" bifurcado: genera campos Modo/Tasks en Metadata, sección Dependencias entre Tasks, progreso por task, sub-fases por task, CAs granulares por task + CAs integración |

#### ✅ Cambios en Plantillas

| Cambio | Detalle |
|--------|---------|
| `plan_implementacion_plantilla.md` v2.0 → v3.0 | Metadata: nuevos campos `Modo` (Plano/Particionada) y `Tasks` |
| `plan_implementacion_plantilla.md` | Progreso General: opción tabla por fases (plano) o por tasks (particionada) |
| `plan_implementacion_plantilla.md` | Nueva sección condicional "Dependencias entre Tasks" con tabla Task/Depende de/Razón/Ejecutable |
| `plan_implementacion_plantilla.md` | Estructura dual: Opción A (modo plano, sin cambios) vs Opción B (modo particionada: Task > Fases internas > Tareas técnicas con dependencias cross-task ⟵T[N]) |
| `plan_implementacion_plantilla.md` | Fase Final: CAs de integración (padre) con nota sobre CAs granulares validados por task |
| `plan_implementacion_plantilla.md` | Historial de Ejecución: columna Task agregada para modo particionada |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|---------|
| `CONFIG_SYSTEM.yaml` | version 7.18.0 → 7.19.0 |

#### 📊 Tabla de compatibilidad modo_ejecucion

| `modo_ejecucion` | HU Plana | HU Particionada |
|---|---|---|
| `completo` | ✅ Igual que antes | ✅ T1→T2→T3 sin pausas |
| `fase_por_fase` | ✅ Igual que antes | ⚠️→ `task_por_task` con aviso |
| `tarea_por_tarea` | ✅ Igual que antes | ✅ Pausa en cada tarea técnica |
| `task_por_task` (nuevo) | ⚠️→ `fase_por_fase` con aviso | ✅ Pausa entre tasks funcionales |
| `task_especifica` (nuevo) | ⛔ Error claro | ✅ Solo task indicada en task_id |

---

### [7.18.0] - 2026-04-28

#### 📦 Feat: Descomposición jerárquica de HUs en Tasks funcionales con CAs granulares

**Objetivo:** Permitir que HUs de complejidad media-alta se descompongan en Tasks funcionales (work items lógicos) con sus propios Criterios de Aceptación granulares y desglose técnico, manteniendo trazabilidad CA padre ↔ CA hijas. Las Tasks viven dentro del refinamiento (sin explosión de archivos) y se referencian como texto plano en el backlog.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|---------||
| `refinar_hu.tool.yaml` | Nueva regla mandatory: evaluar partición en tasks para complejidad ≥ MEDIO |
| `refinar_hu.tool.yaml` | Nuevo paso "Evaluación de Partición en Tasks": detecta HUs con múltiples objetivos funcionales independientes, propone partición al usuario (nunca forzada) |
| `refinar_hu.tool.yaml` | Paso "Desglose Técnico Vertical" transformado: soporta modo plano (actual) y modo particionada (tasks funcionales con CAs granulares + desglose técnico por task) |
| `refinar_hu.tool.yaml` | Persistencia: agrega campo `Tasks` a la HU en backlog cuando hay partición |
| `validar_hu.tool.yaml` | Paso "Validación de CAs": verifica trazabilidad CA padre ↔ Tasks si modo particionada; sugiere partición si HU plana con ≥6 CAs y complejidad ≥ MEDIO |

#### ✅ Cambios en Plantillas

| Cambio | Detalle |
|--------|---------||
| `refinamiento_hu_plantilla.md` | Metadata: nuevos campos `Modo` (Plano/Particionada) y `Tasks` |
| `refinamiento_hu_plantilla.md` | Sección 2 (CAs): comentarios de traza a tasks |
| `refinamiento_hu_plantilla.md` | Sección 4: dos opciones (4A modo plano, 4B modo particionada con Tasks que incluyen CAs granulares + desglose técnico por task) |
| `backlog_desarrollo_plantilla.md` | Campo `Tasks` agregado a plantillas de estado [R], [A], [P] |
| `backlog_desarrollo_plantilla.md` | Índice Rápido: nueva columna `Tasks` |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|---------||
| `CONFIG_SYSTEM.yaml` | version 7.17.0 → 7.18.0 |

---

### [7.17.0] - 2026-04-28

#### 📦 Feat: Resumen de backlog en inicialización del Analista y flag `--resumen` en `>sincronizar_backlog`

**Objetivo:** Dar visibilidad inmediata del estado del backlog al usuario cuando inicia conversación con el Analista de Requisitos, y ofrecer un comando ligero para consultar el estado sin ejecutar la sincronización completa.

#### ✅ Cambios en Roles

| Cambio | Detalle |
|--------|---------|
| `refinador_hu.rol.md` | Nuevo Paso 2 "Mostrar Estado del Backlog" en Inicialización: lee Resumen de Estados e Índice Rápido, muestra bloque compacto con contadores y próxima acción sugerida (prioridad: Bloqueadas → Pendientes → Refinadas → Aprobadas → Completadas) |
| `refinador_hu.rol.md` | Paso "Detectar Tipo de Solicitud" renumerado de Paso 2 a Paso 3 |

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|---------|
| `sincronizar_backlog.tool.yaml` | Nuevo parámetro `--resumen` (alias `--status`): lectura rápida del backlog sin escanear artefactos en disco |
| `sincronizar_backlog.tool.yaml` | Nuevo paso "Atajo Resumen Rápido" con condición `resumen=true`: extrae contadores, índice rápido y próxima acción sugerida, luego termina sin continuar el flujo de sincronización |
| `sincronizar_backlog.tool.yaml` | Nuevo alias `>resumen_backlog` agregado al comando |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|---------|
| `CONFIG_SYSTEM.yaml` | version 7.16.1 → 7.17.0 |

---

### [7.16.1] - 2026-04-28

#### 🐛 Fix: Contexto mínimo en HUs tipo Bug creadas desde `>registrar_bug`

**Objetivo:** Al crear una nueva HU tipo Bug en el backlog (flujo [N]), se transferían solo título, tipo y Ref_Bug — sin origen, descripción ni dependencias. Esto dejaba la HU sin contexto útil, obligando a cargar el archivo BUG por separado.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|---------|
| `registrar_bug.tool.yaml` | Paso "Crear nueva HU tipo Bug" ahora incluye campos: Origen, Descripción (1-2 líneas técnicas) y Dependencias |

#### ✅ Cambios en Plantillas

| Cambio | Detalle |
|--------|---------|
| `backlog_desarrollo_plantilla.md` | Comentario HTML indicando usar descripción técnica breve (no user story) cuando Tipo=Bug, con referencia al archivo Ref_Bug como fuente de verdad |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|---------|
| `CONFIG_SYSTEM.yaml` | version 7.16.0 → 7.16.1 |

---

### [7.16.0] - 2026-04-28

#### 📦 Feat: Workflow de GitHub Actions para release automático al mergear PR

**Objetivo:** Automatizar la creación de tags y GitHub Releases cuando un PR mergeado a `main` contiene un bump de versión en `CONFIG_SYSTEM.yaml`. Incluye extracción automática de notas del CHANGELOG y adjunta los scripts de bootstrap como assets descargables.

#### ✅ Cambios en CI/CD

| Cambio | Detalle |
|--------|--------|
| Nuevo `.github/workflows/release.yml` | Trigger: PR merged a main. Detecta versión en CONFIG_SYSTEM.yaml, compara con tags existentes, crea Release si es nueva |
| Extracción de CHANGELOG | Parsea automáticamente la sección `### [X.Y.Z]` del CHANGELOG como notas del Release |
| Assets de bootstrap | Adjunta `install.ps1` e `install.sh` al Release para que los enlaces `releases/latest/download/` funcionen |
| Idempotencia | Si el tag ya existe, skip silencioso (soporta re-merge y múltiples PRs sin bump) |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|--------|
| `CONFIG_SYSTEM.yaml` | version 7.15.0 → 7.16.0 |

---

### [7.15.0] - 2026-04-28

#### 🔄 Refactor: Migrar `>planificar_hu` del Arquitecto al Desarrollador con Directrices de Planificación

**Objetivo:** Resolver la violación de SRP en el rol Arquitecto (que declaraba "NO implementación" pero planificaba a nivel táctico) y eliminar el cuello de botella que impedía flujo continuo. El Arquitecto ahora deja directrices estratégicas al aprobar la HU; el Desarrollador las consume al planificar.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|--------|
| `validar_hu` — Nueva subsección "Directrices de Planificación" | Se agrega al paso "Persistir Aprobación": campos Fases sugeridas, Componentes clave, Dependencias entre HUs, Riesgos a mitigar, Notas adicionales |
| `validar_hu` — `siguiente` actualizado | `>planificar_hu` ahora apunta a `chat_agente: "ArchDev Pro"` en vez de `"Arquitecto Onad"` |
| `planificar_hu` — Consumo de directrices | Nuevo bloque en paso "Cargar HU y Contexto": lee `### Directrices de Planificación` del refinamiento como recomendaciones (no mandatos); graceful degradation si no existen |
| `registrar_bug` — `siguiente` actualizado | `>planificar_hu` apunta a `chat_agente: "ArchDev Pro"` |
| `sincronizar_backlog` — `siguiente` actualizado | `>planificar_hu` apunta a `chat_agente: "ArchDev Pro"` |
| `analizar_stack` — `siguiente` actualizado | `>planificar_hu` apunta a `chat_agente: "archdev_pro"` |

#### ✅ Cambios en Roles

| Cambio | Detalle |
|--------|--------|
| `arquitecto_onad.rol.md` | Removido `>planificar_hu` de tabla de herramientas |
| `archdev_pro.rol.md` | Agregado `>planificar_hu` a tabla de herramientas |

#### ✅ Cambios en Documentación

| Cambio | Detalle |
|--------|--------|
| `docs/ROLES.md` | Arquitecto pierde `>planificar_hu`; Desarrollador lo gana |
| `docs/guias/guia_comandos.md` | Tabla de agentes actualizada |
| `docs/guias/guia_ciclo_vida_tareas.md` | Transición `[A]→[P]` ahora asignada a ArchDev Pro |
| `docs/estructura_directorio.md` | Agente principal de `>planificar_hu` → Desarrollador |
| `INSTALACION/README.md` | Tabla de herramientas actualizada |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|--------|
| `CONFIG_SYSTEM.yaml` | version 7.14.0 → 7.15.0 |

---

### [7.14.0] - 2026-04-27

#### 📦 Feat: Instalación vía GitHub Releases con sistema de tags versionados

**Objetivo:** Migrar los enlaces de instalación bootstrap de `raw.githubusercontent.com/main` (mutable, con caching agresivo) a **GitHub Releases** con tags inmutables, e incorporar documentación completa de instalación remota, actualización y seguridad en la página pública de MkDocs.

#### ✅ Cambios en Documentación

| Cambio | Detalle |
|--------|--------|
| `docs/INSTALACION.md` — Opción 1: Bootstrap desde GitHub | Nuevo; un solo comando vía `releases/latest/download/` |
| `docs/INSTALACION.md` — Opción 2: Instalación Segura | Nuevo; flujo descargar → revisar → ejecutar para entornos corporativos |
| `docs/INSTALACION.md` — Sección Releases y Versionado | Nuevo; explica `latest` vs tag fijo con tabla comparativa |
| `docs/INSTALACION.md` — Consideraciones de Seguridad | Nuevo; tabla de riesgos y mitigaciones |
| `docs/INSTALACION.md` — Actualización y upgrade-all | Nuevo; comandos `sac --update` y `sac --upgrade-all` |
| `docs/INSTALACION.md` — Más Información expandida | Tabla de recursos con links a GitHub, issues y releases |
| `INSTALACION/README.md` — URLs bootstrap | Migradas de `raw.githubusercontent.com/main` a `releases/latest/download/` |
| `INSTALACION/README.md` — Instalación segura | Nuevo bloque con flujo descargar-revisar-ejecutar |
| `INSTALACION/README.md` — Versión fija | Nuevo; ejemplo de pinning a tag específico |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|--------|
| `CONFIG_SYSTEM.yaml` | version 7.13.0 → 7.14.0 |

---

### [7.13.0] - 2026-04-27

#### 🛡️ Feat: Veredicto `bloqueada` y verificación de dependencias en `validar_hu`

**Objetivo:** Formalizar el manejo de dependencias no resueltas (HUs, APIs externas, decisiones pendientes) durante la validación de HU, alineando la herramienta con la taxonomía de bloqueos definida en `guia_ciclo_vida_tareas.md`.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|--------|
| Nuevo veredicto `bloqueada` en `validar_hu` | Separado de `rechazada` — para dependencias no resueltas sin rediseño |
| 4 tipos de bloqueo embebidos | `DEPENDENCIA_HU`, `DEPENDENCIA_EXTERNA`, `DECISION_PENDIENTE`, `RECURSO_NO_DISPONIBLE` — autosuficientes, sin referencia externa |
| Nuevo paso "Verificación de Dependencias" | Entre Validación Arquitectónica y Análisis de Viabilidad Técnica |
| Nuevo paso "Persistir Bloqueo" | Documenta bloqueo en refinamiento con tabla estructurada (tipo, motivo, acción requerida) |
| Mensaje de salida `mensaje_bloqueada` | Incluye tipo, motivo y acción requerida |
| Mandatory actualizado | Nueva instrucción: verificar dependencias antes de aprobar |
| Versión herramienta | 4.1 → 4.2 |

#### ✅ Cambios en Configuración

| Cambio | Detalle |
|--------|--------|
| `CONFIG_SYSTEM.yaml` | version 7.12.0 → 7.13.0 |

---

### [7.12.0] - 2026-04-25

#### 🔄 Refactor: Migrar herramientas de `.tool.md` a `.tool.yaml`

**Objetivo:** Eliminar las 3 capas redundantes (frontmatter YAML + code block markdown + YAML body) en cada herramienta, pasando a YAML puro. El LLM consume el contenido idénticamente; la extensión ahora refleja el formato real del archivo.

#### ✅ Cambios en Herramientas

| Cambio | Detalle |
|--------|--------|
| 16 archivos `.tool.md` → `.tool.yaml` | Eliminados frontmatter (`---`) y code blocks (` ```yaml `) — YAML puro con campos `nombre`, `comando`, `alias`, `version` al nivel raíz |
| `_base.tool.md` eliminado | Archivo deprecado desde v5.0, ya no necesario |
| Plantilla `herramienta_plantilla.tool.md` → `.tool.yaml` | Instrucciones actualizadas para nuevo formato |

#### ✅ Cambios en Roles

| Archivo | Cambio |
|---------|--------|
| `_base.rol.md` | Línea de resolución: `.tool.md` → `.tool.yaml` |

#### ✅ Cambios en Documentación

| Archivo | Cambio |
|---------|--------|
| `docs/HERRAMIENTAS.md` | Todas las rutas de archivo actualizadas |
| `docs/README_PLANTILLA.md` | Referencias a plantilla y extensión actualizadas |
| `docs/estructura_directorio.md` | Árbol de directorio actualizado, `_base.tool` eliminado |
| `docs/guias/guia_creacion_roles.md` | Instrucciones de creación actualizadas |
| `INSTALACION/README.md` | Referencia a plantilla actualizada |
| `README.md` | Contador de herramientas corregido (12→16) y extensión actualizada |

#### 📊 Impacto

| Métrica | Antes | Después |
|---------|-------|---------|
| Líneas redundantes por herramienta | ~8 (frontmatter + code blocks) | 0 |
| Capas de estructura | 3 (frontmatter + md + yaml) | 1 (yaml puro) |
| Archivos en `herramientas/` | 17 (.md) | 16 (.yaml) |
| Mecanismo de carga (tokens) | Sin cambio | Sin cambio |

---

### [7.11.3] - 2026-04-25

#### 🐛 Fix: ejecutar_plan no actualizaba estados en archivo del plan

**Causa raíz:** Las instrucciones de actualización usaban formato declarativo (diccionario YAML pasivo) que el LLM interpretaba como metadata, no como acción de edición de archivo. El verbo "marcar" era ambiguo — no implicaba escritura en disco.

#### ✅ Cambios en Herramientas

| Herramienta | Cambio |
|-------------|--------|
| `ejecutar_plan.tool.md` | Paso "Ejecutar Fases": acciones expandidas de array compacto a sub-pasos explícitos con verbo "EDITAR ARCHIVO" |
| `ejecutar_plan.tool.md` | Campo `critico` añadido: pasos de edición del plan son BLOQUEANTES (no avanzar sin escribir) |
| `ejecutar_plan.tool.md` | Sección `actualizacion_tiempo_real`: convertida de diccionario pasivo a `instrucciones_imperativas` con verbos explícitos |
| `ejecutar_plan.tool.md` | Paso "Finalización": nueva verificación de coherencia — leer plan y confirmar que TODOS los estados coinciden antes de cerrar |
| `ejecutar_plan.tool.md` | Versión 4.2 → 4.3 |

---

### [7.11.2] - 2026-04-25

#### 🛡️ Mejora: Robustez de ejecutar_plan.tool.md

**Objetivo:** Corregir tres riesgos críticos detectados: ausencia de validación de entorno, imposibilidad de reanudación segura tras interrupciones, y combinación peligrosa de modo completo con auto-commit.

#### ✅ Cambios en Herramientas

| Herramienta | Cambio |
|-------------|--------|
| `ejecutar_plan.tool.md` | Nuevo paso obligatorio "Validar Entorno de Ejecución" (rama Git, directorio, framework tests, punto de restauración) |
| `ejecutar_plan.tool.md` | Cláusula `reanudacion` en "Ejecutar Fases": salta tareas [EJECUTADA], verifica archivos, informa progreso |
| `ejecutar_plan.tool.md` | Límite `max_reintentos_por_tarea: 2` para evitar bucles infinitos de error-corrección |
| `ejecutar_plan.tool.md` | Validación: `modo_ejecucion=completo + auto_commit=true` prohibida (⛔) |
| `ejecutar_plan.tool.md` | Versión 4.1 → 4.2 |

#### 📊 Impacto

| Métrica | Antes | Después |
|---------|-------|---------|
| Validación de entorno pre-ejecución | No | Sí (rama, deps, framework tests) |
| Reanudación tras interrupción | Implícita (frágil) | Explícita con verificación de archivos |
| Protección contra ejecución sin supervisión | Parcial | Completa (completo+auto_commit bloqueado) |
| Límite de reintentos por tarea | Infinito | 2 |

---

### [7.11.1] - 2026-04-24

#### 🐛 Fix: Instalador - Rutas absolutas en artifacts

| Tipo | Cambio |
|------|--------|
| **Fix** | Validar rutas absolutas en input de `artifacts_rel` del instalador |
| **Fix** | Detectar automáticamente cuando el usuario pega una ruta absoluta que contiene el `project_root` y extraer la parte relativa |
| **Fix** | Defensa adicional en `replace_artifacts_path()` para sanitizar `artifacts_rel` antes de concatenar |

---

### [7.11.0] - 2026-04-24

#### 🎯 Simplificación del Protocolo de Subagentes

**Objetivo:** Reemplazar el protocolo de subagentes (238 líneas, prompts no funcionales, paralelismo ficticio) por un modelo liviano de recomendación de delegación donde el usuario decide si cambia de agente.

#### ✅ Cambios en Roles

| Archivo | Cambio |
|---------|--------|
| `_base.rol.md` | Sección "Protocolo de Subagentes" (~55 líneas) → "Delegación entre Agentes" (~20 líneas) |
| `archdev_pro.rol.md` | Sección de subagentes (~50 líneas) → tabla "Recomendaciones de Delegación" (~10 líneas) |
| `arquitecto_devops.rol.md` | Sección de subagentes (~50 líneas) → tabla "Recomendaciones de Delegación" (~10 líneas) |
| `arquitecto_onad.rol.md` | Sección de subagentes (~40 líneas) → tabla "Recomendaciones de Delegación" (~10 líneas) |
| `refinador_hu.rol.md` | Sección de subagentes (~43 líneas) → tabla "Recomendaciones de Delegación" (~10 líneas) |

#### 📊 Impacto

| Métrica | Antes | Después |
|---------|-------|--------|
| Líneas de instrucciones de subagentes | 238 | 60 |
| Tokens por sesión (subagentes) | ~700 | ~200 |
| Prompts de invocación no funcionales | 4 | 0 |
| Delegaciones automáticas opacas | Sí | No (usuario decide) |

---

### [7.10.1] - 2026-04-24

#### 🎯 Carga de Reglas de Dominio Bajo Demanda

**Objetivo:** Reducir ~1000 tokens/sesión al no cargar reglas (mermaid, etc.) en la inicialización, sino solo cuando la tarea lo requiera.

#### ✅ Cambios en Roles

| Archivo | Cambio |
|---------|--------|
| `_base.rol.md` | Paso "Cargar Reglas de Dominio" cambiado de obligatorio a bajo demanda |
| `_base.rol.md` | Tabla "Resumen de Contexto" actualizada: reglas ya no aparecen como cargadas |

---

### [7.10.0] - 2026-04-24

#### 🎯 Optimización de Carga del Backlog (Ahorro de Tokens)

**Objetivo:** Reducir el consumo de tokens al cargar el backlog, pasando de lectura completa (~5000 tokens para 50+ HUs) a carga parcial (~200 tokens) con búsqueda dirigida bajo demanda.

#### ✅ Cambios en Plantillas

| Plantilla | Cambio |
|-----------|--------|
| `backlog_desarrollo_plantilla.md` | Nueva sección `## 📇 Índice Rápido` — tabla compacta (1 fila por HU: ID, Título, Estado, Prioridad, Tipo) |

#### ✅ Cambios en Roles

| Archivo | Cambio |
|---------|--------|
| `_base.rol.md` | Carga obligatoria cambiada: leer solo hasta `## 🎯 Historias de Usuario` (índice + metadatos) |
| `_base.rol.md` | Nueva instrucción de búsqueda dirigida: grep heading `### [ID-HU]` + read_file por rango |
| `_base.rol.md` | Instrucción explícita: NUNCA leer backlog completo para consultar una sola HU |

#### ✅ Cambios en Herramientas

| Herramienta | Cambio |
|-------------|--------|
| `sincronizar_backlog.tool.md` | Nuevo paso obligatorio `Regenerar Índice Rápido` — reconstruye tabla compacta tras sincronización |

---

### [7.9.0] - 2026-04-24

#### 🎯 Ruta de Artifacts Personalizable en Instalación

**Objetivo:** Permitir al usuario elegir la ruta relativa donde se generan los artifacts durante la instalación de SAC, en lugar de usar siempre `artifacts/`.

#### ✅ Cambios en Instalador

| Componente | Cambio |
|------------|--------|
| `instalar.py` | Nueva pregunta en configuración: ruta de artifacts (default: `artifacts/`) |
| `instalar.py` | Reordenamiento del flujo: configuración se pregunta ANTES de instalar |
| `instalar.py` | Nueva función `replace_artifacts_path()` para inyectar ruta custom en CONFIG_SYSTEM |
| `instalar.py` | Nueva función `collect_user_settings()` (recolección) separada de `write_user_config()` (escritura) |
| `instalar.py` | `upgrade_installation()` lee `artifacts_rel` del CONFIG_USER existente para preservar ruta custom |

#### ✅ Cambios en Configuración

| Archivo | Cambio |
|---------|--------|
| `CONFIG_USER.template.yaml` | Nueva sección `rutas_override.artifacts_folder` (opcional, comentada por defecto) |
| `CONFIG_SYSTEM.yaml` | Bump versión a 7.9.0 (sin cambios estructurales) |

---

### [7.8.0] - 2026-04-24

#### 🎯 Cambio Mayor: Sistema de Gestión de Bugs y Pendientes con Dispatcher Unificado

**Objetivo:** Implementar un sistema completo para registrar, clasificar y gestionar bugs y pendientes dentro del SAC, con soporte a lo largo de todo el ciclo de vida de HUs.

#### ✅ Nuevas Herramientas

| Herramienta | Descripción |
|-------------|-------------|
| **`>registrar_bug`** | Registro estructurado de bugs con triage: vincular a HU, agregar ajuste, o crear HU tipo Bug |
| **`>registrar_pendiente`** v2 | Registro dual (rápido en tabla / detallado con archivo individual), 6 categorías |
| **`>registrar_hallazgo`** | Dispatcher unificado que clasifica automáticamente y redirige a bug o pendiente |

#### ✅ Nuevas Plantillas

| Plantilla | Descripción |
|-----------|-------------|
| `bug_plantilla.md` | Formato post-mortem: Síntoma, Causa Raíz, Corrección, Lección Aprendida |
| `pendientes_plantilla.md` | Índice con 6 categorías y 4 estados de ciclo de vida |
| `pendiente_detalle_plantilla.md` | Archivo individual para pendientes con logs y evidencia |

#### ✅ Herramientas Adaptadas para HU tipo Bug

| Herramienta | Cambios |
|-------------|--------|
| `planificar_hu.tool.md` | Fases bugfix (Reproducción → Corrección → Testing Regresión), bypass para bugs críticos |
| `refinar_hu.tool.md` | Pre-población automática desde archivo BUG-NNN, auto-generación de CA |
| `validar_hu.tool.md` | Validación acelerada para Bug+Crítica |
| `sincronizar_backlog.tool.md` | Lectura de campos Tipo y Ref_Bug por HU |

#### ✅ Cambios en Configuración y Roles

| Archivo | Cambio |
|---------|--------|
| `CONFIG_SYSTEM.yaml` | Nuevas rutas: `bugs_folder`, `pendientes`, `pendientes_folder` |
| `backlog_desarrollo_plantilla.md` | Campos Tipo y Ref_Bug en todos los estados de HU |
| `_base.rol.md` | Carga bajo demanda de bugs y pendientes |
| `arquitecto_onad.rol.md` | +3 herramientas: `>registrar_bug`, `>registrar_pendiente`, `>registrar_hallazgo` |
| `archdev_pro.rol.md` | +2 herramientas: `>registrar_bug`, `>registrar_hallazgo` |

#### 📋 Flujo de Uso

```
Usuario reporta hallazgo
    └─ >registrar_hallazgo (dispatcher)
        ├─ [B] → >registrar_bug → Triage → HU tipo Bug
        └─ [P] → >registrar_pendiente → Tabla + archivo detalle
```

#### ⚙️ Retrocompatibilidad

Todos los cambios son retrocompatibles: si el campo `Tipo` no existe en una HU, se asume `Funcional`.

---

### [7.3.0] - 2026-04-23

#### 🎯 Cambio Mayor: Mejora de Sistema de Agentes, Roles y Guía de Subagentes

#### ✅ Mejoras

| Funcionalidad | Descripción |
|---------------|-------------|
| **Sistema de Agentes** | Mejoras en la configuración y comportamiento de agentes |
| **Roles** | Actualización de definiciones de roles del sistema |
| **Guía de Subagentes** | Mejoras en la guía de subagentes de VS Code |

---

### [7.2.0] - 2026-04-23

#### 🎯 Cambio Mayor: Subagentes, Extensiones y Limpieza Arquitectónica

#### ✅ Nuevas Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| **Protocolo de Delegación** | `_base.rol.md` incluye protocolo activo de escalamiento con `runSubagent` |
| **Soporte Subagentes VS Code** | Activadores con propiedad `agents:` para orchestrar subagentes natively |
| **Guía de Subagentes** | Nueva `guias/guia_subagents_vscode.md` con patrones y recomendaciones |

#### ✅ Cambios en Nombres y Rutas

| Elemento | Antes | Ahora |
|----------|-------|-------|
| Extensión roles SAC | `.agent.md` | `.rol.md` |
| Carpeta roles | `personas/` | `agentes/` |
| `artifacts/` | dentro de `.SAC/` | en raíz del proyecto |
| Activadores Copilot | `arquitecto_onad.agent.md` | `arquitecto.agent.md` |
| Invocaciones | `@arquitecto_onad` | `@arquitecto` |

#### ✅ Correcciones en Configuración

| Elemento | Cambio |
|----------|--------|
| `CONFIG_SYSTEM.yaml` | Eliminadas variables anidadas `{artifacts_folder}/...` |
| `instalar.py` | `artifacts_dir` apunta a raíz del proyecto; nueva función `migrate_artifacts_to_root()` |

#### ✅ Documentación P1 Corregida

| Archivo | Cambio |
|---------|--------|
| `estructura_directorio.md` | Reescrito completo para reflejar estructura real v7.2.0 |
| `INSTALACION.md` | Corregidos nombres de agentes, rutas de artifacts, invocaciones |
| `guias/guia_creacion_roles.md` | Actualizado a v3.0: rutas, extensiones, eliminados pasos legacy |

---

### [7.1.0] - 2026-02-16

#### 🎯 Cambio Mayor: Soporte Completo Multi-Proyecto

**Objetivo:** Unificar el manejo de workspaces mono y multi-proyecto, adaptar backlog y herramientas para soportar HUs compartidas entre proyectos, e implementar análisis automático de impacto.

#### ✅ Nuevas Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| **Workspace Unificado** | `workspace.md` como índice único para mono y multi-proyecto |
| **Campo Proyecto en HUs** | Cada HU indica a qué proyecto pertenece o si es `compartida` |
| **Análisis de Impacto `[AP]`** | Opción en `>refinar_hu` para que el agente analice qué proyectos afecta una HU |
| **Resumen por Proyecto** | Nueva sección en backlog con contadores de HUs por proyecto |
| **Proyectos afectados** | Sección en HUs compartidas listando proyectos involucrados |

#### ✅ Cambios en Plantillas

| Plantilla | Cambio |
|-----------|--------|
| `workspace_plantilla.md` | Simplificada a índice mínimo (tipo, tabla de proyectos, historial) |
| `contexto_proyecto_plantilla.md` | Nueva sección "6. Dependencias de Proyecto" |
| `backlog_desarrollo_plantilla.md` | Campo Workspace/Tipo, Resumen por Proyecto, campo Proyecto en HUs, columna Proyecto en tablas |

#### ✅ Cambios en Herramientas

| Herramienta | Cambios |
|-------------|---------|
| `refinar_hu.tool.md` | Parámetro `--proyecto`, detección de workspace, opción `[AP]` análisis de impacto, soporte respuestas combinadas (`1,2,3 AP`) |
| `validar_hu.tool.md` | Parámetro `--proyecto`, carga contextos de proyectos afectados, validación cross-proyecto |
| `planificar_hu.tool.md` | Parámetro `--proyecto`, carga contextos según campo Proyecto de HU |
| `ejecutar_plan.tool.md` | Parámetro `--proyecto`, CWD por proyecto, actualización Resumen por Proyecto |
| `tomar_contexto.tool.md` | Genera `workspace.md` en ambos modos (mono/multi) |

#### ✅ Cambios en Agentes

| Agente | Cambio |
|--------|--------|
| `_base.agent.md` | Carga unificada desde `{{archivos.workspace}}`, contextos on-demand |

#### ✅ Cambios en Configuración

| Archivo | Cambio |
|---------|--------|
| `CONFIG_SYSTEM.yaml` | Unificado a `archivos.workspace` (eliminados `contexto_proyecto` y `workspace_index`) |

#### 📋 Flujo Multi-Proyecto

```
>refinar_hu "nueva funcionalidad"
   ↓
¿A qué proyecto(s) pertenece?
  [1] backend_users
  [2] backend_orders
  [AP] Analizar impacto
   ↓
Usuario: "1,2 AP" → Analiza impacto solo en proyectos 1 y 2
   ↓
📊 Análisis de Impacto:
  - backend_users: ✅ AFECTADO
  - backend_orders: ❌ NO afectado
   ↓
HU creada como Proyecto: backend_users (o compartida si múltiples)
```

---

### [7.0] - 2026-02-13

#### 🎯 Cambio Mayor: Sistema Mandatory Base, Limpieza de Reglas y Mejoras en Herramientas

**Objetivo:** Centralizar instrucciones mandatory comunes en `_base.tool.md` y `_base.agent.md`, eliminar reglas de stack que son conocimiento implícito del LLM, mejorar herramientas de validación y refinamiento, y unificar plantillas.

#### ⚠️ Breaking Changes

| Cambio | Impacto | Migración |
|--------|---------|----------|
| Bloque `mandatory` en herramientas reemplazado por `mandatory_base` + `mandatory_especifico` | Herramientas heredan instrucciones comunes de `_base.tool.md` | Actualizar herramientas personalizadas |
| Reglas de stack eliminadas (`java.rules.md`, `go.rules.md`, etc.) | Movidas a legacy / conocimiento implícito del LLM | No se requiere acción |
| `stack_proyecto_plantilla.md` eliminada | Unificada con `contexto_proyecto_plantilla.md` | Usar plantilla de contexto |
| `session_state_plantilla.md` movida a legacy | Ya deprecada en v6.0 | Sin impacto |

#### ✅ Nuevos Archivos

| Archivo | Propósito |
|---------|----------|
| `agentes/_base.agent.md` | Instrucciones base compartidas por todos los agentes |
| `herramientas/_base.tool.md` | Instrucciones mandatory compartidas por todas las herramientas |
| `plantillas/refinamiento_hu_plantilla.md` | Plantilla estándar para refinamientos de HU |

#### ✅ Cambios en Herramientas

**Todas las herramientas (`herramientas/*.tool.md`):**
- Bloque `mandatory` reemplazado por `mandatory_base` (referencia a `_base.tool.md`) + `mandatory_especifico`
- Eliminadas instrucciones repetidas de idioma y firma (ahora en `_base.tool.md`)

**`validar_hu.tool.md`:**
- Nuevo paso "Detección de Ambigüedades" — NUNCA asumir, preguntar al usuario
- Nuevo paso "Validación contra ADR" — Verificar coherencia con decisiones arquitectónicas
- Validación Arquitectónica mejorada con checklist ampliado
- Acciones desglosadas en formato lista para mayor claridad

**`refinar_hu.tool.md`:**
- Referencia a `{{plantillas.refinamiento_hu}}` para generación de archivo
- Nuevo campo "Iteración" en acciones de modo nuevo y ajuste
- Acciones de modo ajuste mejoradas con sección de ajustes aplicados

**`tomar_contexto.tool.md`:**
- Mandatory reestructurado con mandatory_base + mandatory_especifico

#### ✅ Cambios en Plantillas

**`backlog_desarrollo_plantilla.md`:**
- Nuevo campo `ADR_Ref` en todas las secciones de HU
- Rutas unificadas a `{{artifacts.*}}` en lugar de variables legacy
- Nueva sección "Deuda Técnica" para tracking de tech debt
- Estado `[X]` Completada renombrado a `[C]` Completada

**`contexto_proyecto_plantilla.md`:**
- Estructura mejorada con subsecciones de Dependencias Core y Herramientas de Desarrollo
- Sección de arquitectura generalizada (no solo "capas")
- Convenciones reorganizadas en Código y Proyecto

**`plan_implementacion_plantilla.md`:**
- Versión actualizada a 2.0
- Fases dinámicas según arquitectura del proyecto (Hexagonal, MVC, Capas, Script, Frontend)
- Comentarios instructivos para `>planificar_hu`
- Eliminados ejemplos hardcodeados Java/Spring

#### ✅ Archivos Eliminados (movidos a legacy o eliminados)

| Archivo | Razón |
|---------|-------|
| `reglas/arquitectura.rules.md` | Conocimiento implícito del LLM |
| `reglas/deteccion_stack.rules.md` | Conocimiento implícito del LLM |
| `reglas/java.rules.md` | Conocimiento implícito del LLM |
| `reglas/javascript.rules.md` | Conocimiento implícito del LLM |
| `reglas/python.rules.md` | Conocimiento implícito del LLM |
| `reglas/dotnet.rules.md` | Conocimiento implícito del LLM |
| `reglas/go.rules.md` | Conocimiento implícito del LLM |
| `reglas/patrones_diseno.rules.md` | Conocimiento implícito del LLM |
| `plantillas/session_state_plantilla.md` | Movida a legacy (deprecada desde v6.0) |
| `plantillas/stack_proyecto_plantilla.md` | Unificada con contexto_proyecto_plantilla.md |

#### ✅ Cambios en Configuración

**`config/CONFIG_SYSTEM.yaml`:**
- Versión actualizada a 7.0
- Eliminado: `archivos.stack_proyecto` (unificado en contexto)
- Agregado: `plantillas.refinamiento_hu`
- Reglas simplificadas: solo `mermaid.rules.md` permanece

---

### [6.0] - 2026-01-09

#### 🎯 Cambio Mayor: Agentes Technology-Agnostic y Deprecación de Session State

**Objetivo:** Hacer el sistema SAC independiente de tecnología específica y simplificar la gestión de estado usando el backlog como única fuente de verdad.

#### ⚠️ Breaking Changes

| Cambio | Impacto | Migración |
|--------|---------|----------|
| `session_state.json` **DEPRECADO** | Proyectos existentes deben migrar | El backlog es ahora la única fuente de verdad |
| Agentes ya no son Java/Spring específicos | Comportamiento genérico por defecto | Ejecutar `>tomar_contexto` para generar `stack_proyecto.md` |
| Nuevo artefacto `stack_proyecto.md` requerido | `>tomar_contexto` tiene nuevo paso obligatorio | Se genera automáticamente |

#### ✅ Nuevos Artefactos y Plantillas

| Archivo | Propósito |
|---------|-----------|
| `plantillas/stack_proyecto_plantilla.md` | Plantilla para información del stack tecnológico |
| `plantillas/plan_implementacion_plantilla.md` | Plantilla para planes de implementación de HUs |
| `.SAC/artifacts/stack_proyecto.md` | Auto-generado con stack detectado del proyecto |

#### ✅ Cambios en Agentes

**Todos los agentes (`agentes/*.agent.md`):**
- Eliminada inicialización de `session_state.json`
- Nueva referencia dinámica: `referencia_stack: "{{archivos.stack_proyecto}}"`
- Principios universales en lugar de prácticas Java-específicas
- `actualizacion_estado` ahora referencia archivos de artefactos

#### ✅ Cambios en Herramientas

**`tomar_contexto.tool.md`:**
- Nuevo `paso_6`: Generación automática de `stack_proyecto.md`
- Detección de lenguajes, frameworks, herramientas de testing, convenciones

**`validar_hu.tool.md`:**
- Nuevo `paso_6`: Persistir feedback de validación en archivo de refinamiento
- Cuando veredicto es AJUSTES, agrega sección `## 📝 Feedback de Validación`

**`refinar_hu.tool.md`:**
- Nuevo `paso_0`: Detectar feedback de validación previa
- **MODO AJUSTE**: Re-refinamiento enfocado en resolver observaciones
- Marca observaciones como resueltas `[x]` al completar

**`planificar_hu.tool.md`:**
- Referencia a `{{plantillas.plan_implementacion}}`

**`ejecutar_plan.tool.md`:**
- Nueva sección `actualizacion_plan_tiempo_real` con estados y reglas

**Todas las herramientas:**
- Eliminado `paso_final` que actualizaba `session_state.json`
- Secciones `siguiente` sincronizadas con nombres de agentes correctos
- Nuevo campo `accion_usuario` con instrucciones para flujo cross-chat

#### ✅ Cambios en Configuración

**`config/CONFIG_SYSTEM.yaml`:**
- Eliminado: `rutas.session_folder`
- Eliminado: `archivos.session_state`
- Eliminado: `plantillas.session_state`
- Agregado: `archivos.stack_proyecto`
- Agregado: `plantillas.stack_proyecto`
- Agregado: `plantillas.plan_implementacion`

#### ✅ Archivos Deprecados/Eliminados

| Archivo | Razón |
|---------|-------|
| `plantillas/session_state_plantilla.md` | Backlog es única fuente de verdad |
| `.SAC/session/session_state.json` | Ya no se genera ni utiliza |

#### ✅ Flujo de Feedback Validación ↔ Refinamiento

```
>refinar_hu → [R] Refinada → >validar_hu 
                                   ↓
                        ┌─────────────────────┐
                        │   ¿Veredicto?       │
                        └─────────────────────┘
                           ↓           ↓
                      APROBADA     AJUSTES
                           ↓           ↓
                    >planificar   Persiste feedback
                                  en refinamiento.md
                                          ↓
                                    >refinar_hu
                                    (MODO AJUSTE)
                                          ↓
                                    Resuelve [x]
                                          ↓
                                    >validar_hu
```

---

### [4.0] - 2026-01-05

#### 🎯 Cambio Mayor: Reestructuración Completa del Repositorio

**Objetivo:** Separar configuración del sistema (no editable) de configuración del usuario (editable), crear capa de definiciones compactas y organizar archivos legacy.

#### ✅ Nueva Estructura de Carpetas

```
ia_prompts/
├── config/                          # ⚠️ NUEVO - Configuración separada
│   ├── CONFIG_SYSTEM.yaml           # NO EDITABLE - Rutas del sistema
│   └── CONFIG_USER.template.yaml    # EDITABLE - Preferencias del usuario
├── definiciones/                    # ⚠️ NUEVO - Definiciones compactas
│   ├── personas/                    # 5 archivos YAML de roles
│   │   ├── archdev_pro.yaml
│   │   ├── arquitecto_onad.yaml
│   │   ├── refinador_hu.yaml
│   │   ├── artesano_de_commits.yaml
│   │   └── arquitecto_devops.yaml
│   └── herramientas/                # 15 archivos YAML de herramientas
│       ├── tomar_contexto.yaml
│       ├── refinar_hu.yaml
│       ├── crear_pruebas.yaml
│       └── ... (12 más)
├── guias/                           # ⚠️ NUEVO - Carpeta para guías
├── legacy/                          # ⚠️ NUEVO - Archivos deprecados
│   ├── CONFIG_INIT.yaml             # Configuración antigua
│   ├── cochas.agent.md              # Orquestador anterior
│   ├── personas_antiguas/           # Backup de personas
│   └── herramientas_antiguas/       # Backup de herramientas
├── personas/                        # Archivos completos de personalidad
├── herramientas/                    # Archivos completos de herramientas
├── plantillas/                      # Sin cambios
└── ejemplos/                        # Sin cambios
```

#### ✅ Nuevos Archivos de Configuración

| Archivo | Propósito | Editable |
|---------|-----------|----------|
| `config/CONFIG_SYSTEM.yaml` | Rutas internas del sistema COCHAS | ❌ NO |
| `config/CONFIG_USER.template.yaml` | Preferencias del usuario/proyecto | ✅ SÍ |

#### ✅ Nueva Capa de Definiciones

**Propósito:** Archivos YAML compactos que sirven como índice rápido de roles y herramientas.

**Personas (5 definiciones):**
- `archdev_pro.yaml` - Ingeniero Constructor Java/Spring Boot
- `arquitecto_onad.yaml` - Arquitecto Estratégico
- `refinador_hu.yaml` - Experto en Historias de Usuario
- `artesano_de_commits.yaml` - Experto en Conventional Commits
- `arquitecto_devops.yaml` - Mentor DevOps

**Herramientas (15 definiciones):**
- `tomar_contexto.yaml`, `refinar_hu.yaml`, `crear_pruebas.yaml`
- `generar_commit.yaml`, `diagnosticar_devops.yaml`, `define_arquitectura.yaml`
- `generar_adr.yaml`, `analizar_code_smells.yaml`, `solucionar_smells.yaml`
- `refactorizar.yaml`, `verifica_pruebas.yaml`, `ejecutar_plan.yaml`
- `validar_hu.yaml`, `planificar_hu.yaml`, `asignar_responsable.yaml`

#### ✅ Archivos Migrados a Legacy

| Archivo Original | Nueva Ubicación |
|------------------|-----------------|
| `CONFIG_INIT.yaml` | `legacy/CONFIG_INIT.yaml` |
| `cochas.agent.md` | `legacy/cochas.agent.md` |
| `personas/*.md` | `legacy/personas_antiguas/` (backup) |
| `herramientas/*.md` | `legacy/herramientas_antiguas/` (backup) |

#### ✅ Beneficios de la Reestructuración

1. **Separación clara** entre configuración del sistema y del usuario
2. **Definiciones compactas** para referencia rápida sin leer archivos extensos
3. **Preservación de legacy** para rollback si es necesario
4. **Estructura escalable** para agregar nuevos roles/herramientas

---

### [3.2] - 2026-01-05

#### ✅ Correcciones Críticas
- **README.md**: Corregida referencia `core-cochas.md` → `cochas.agent.md`
- **README.md**: Agregado diagrama visual del sistema
- **herramientas-activas.md**: Eliminada herramienta `asignar_responsable` (ORQUESTADOR no es un rol activable)
- **guia_roles_activos.md**: Actualizada a v3.0, sincronizada sintaxis `+ROL`
- **Sincronización**: Herramientas ahora coinciden entre `roles-activos.md` y `herramientas-activas.md`

#### ✅ Nuevas Características
- **CHANGELOG.md** centralizado (este archivo)
- **Documentación de manejo de errores** en `cochas.agent.md`:
  - Session_state.json corrupto → recreación automática desde plantilla
  - Rol no encontrado → sugerencia de roles disponibles
  - Herramienta sin rol activo → indicación de roles compatibles
  - CONFIG_INIT.yaml inválido → mensaje de error claro
- **Sección "Herramientas por Rol"** en herramientas-activas.md

#### ✅ Clarificaciones de Ambigüedades Resueltas
| Ambigüedad | Resolución | Documento |
|------------|------------|-----------|
| Estado [B] Bloqueada: ¿Quién puede marcar? | **Cualquier rol** puede marcar si detecta impedimento | `guia_ciclo_vida_tareas.md` |
| Reglas Arquitectónicas: ¿Borrador o final? | Se genera como **BORRADOR**, requiere confirmación del usuario | `tomar_contexto.md` |
| Session State corrupto | Se **recrea automáticamente** desde plantilla base | `cochas.agent.md` |
| Confirmación de reglas: ¿Y si no responde? | **Siempre esperar** respuesta del usuario (A/B/C/D) | `tomar_contexto.md` |

---

### [3.1] - 2026-01-05

#### ✅ Cambios en Orquestador
- Nuevo sistema de prefijos (`*`, `+`, `>`)
- Eliminada tabla de roles duplicada (ver `roles-activos.md`)

---

### [3.0] - 2026-01-05

#### 🎯 Cambio Mayor: Nuevo Sistema de Prefijos

| Antes (v2.x) | Ahora (v3.0) | Propósito |
|--------------|--------------|-----------|
| `/cochas list` | `*roles` | Listar roles |
| `/cochas switch ONAD` | `+ONAD` | Activar rol |
| `/cochas status` | `*status` | Ver estado |
| `-> herramienta` | `>herramienta` | Ejecutar herramienta |

#### ✅ Componentes Actualizados
- `cochas.agent.md` - Orquestador simplificado con 5 responsabilidades
- `guia_comandos.md` - Nueva documentación de prefijos
- `roles-activos.md` - Actualizada tabla de roles
- `herramientas-activas.md` - Nuevo formato de comandos

#### ✅ Nuevos Comandos del Orquestador
- `*roles` - Lista roles disponibles
- `*status` - Muestra estado de sesión
- `*HU` - Lista historias de usuario
- `*help` - Ayuda de comandos
- `*actualizar_config` - Recarga configuración

#### ✅ Validación de Estructura (Paso 3.5)
- Nuevo paso obligatorio en protocolo de inicio
- Detecta archivos mal ubicados en artifacts/
- Sugiere correcciones automáticas

---

### [2.1] - 2026-01-04

#### ✅ Mejoras en Roles
- `arquitecto_onad.md` - Integración con placeholders y session_state
- Paso 0 crítico con `{{session_state_location}}`
- Secciones formales de Restricciones y Métricas

#### ✅ Nuevas Herramientas
- `validar_hu` - Validación arquitectónica de HUs
- `planificar_hu` - Planificación de implementación
- `ejecutar_plan` - Ejecución de planes de desarrollo

---

### [2.0] - 2025-10-16

#### 🎯 Cambio Mayor: Sistema de Estado Persistente

- **session_state.json** - Memoria de sesión entre cambios de rol
- **Validación secuencial** - Tareas pasan por estados obligatorios
- **Backlog automatizado** - Tracking de HUs con estados

#### ✅ Nuevos Componentes
- `plantillas/estructura_session_state.md` - Schema del estado
- `plantillas/backlog_desarrollo_plantilla.md` - Plantilla de backlog
- `guia_ciclo_vida_tareas.md` - Documentación de estados

#### ✅ Ciclo de Vida de Tareas
```
[ ] Pendiente → [R] Refinada → [A] Aprobada → [P] Planificada → [E] En Ejecución → [X] Completada
                                                                          ↓
                                                                    [B] Bloqueada
```

---

### [1.0] - 2025-10-01

#### 🎯 Versión Inicial

- **Orquestador básico** con cambio de roles
- **5 roles iniciales**: ONAD, ARCHDEV, DEVOPS, REFINADOR, ARTESANO
- **Sistema de herramientas** modular
- **Herramienta `tomar_contexto`** para análisis de proyectos

---

## 📋 Guía de Versionado

### Convención de Versiones

| Tipo | Cuándo | Ejemplo |
|------|--------|---------|
| **Major (X.0)** | Cambios que rompen compatibilidad | Nuevo sistema de comandos |
| **Minor (X.Y)** | Nuevas funcionalidades compatibles | Nueva herramienta |
| **Patch (X.Y.Z)** | Correcciones de bugs | Fix de documentación |

### Al Actualizar un Componente

1. **Incrementar versión** en el header del archivo
2. **Actualizar fecha** de última actualización
3. **Agregar entrada** en este CHANGELOG
4. **Actualizar tabla** de Estado Actual de Componentes

---

## 🔗 Referencias

- **README Principal**: `README.md`
- **Orquestador**: `cochas.agent.md`
- **Configuración**: `CONFIG_INIT.yaml`
