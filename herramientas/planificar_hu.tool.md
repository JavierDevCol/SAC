---
nombre: "Planificar Historia de Usuario"
comando: ">planificar_hu"
alias: [">planificar", ">plan_hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Generar plan alineado con arquitectura del proyecto"
  - instruccion: "Incluir tareas de testing en el plan"
  - instruccion: "Especificar orden de ejecución y dependencias"
  - instruccion: "Usar plantilla {{plantillas.plan_implementacion}}"
  - instruccion: "Incluir TODOS los criterios de aceptación de la HU en Fase Final"
  - instruccion: "SI campo Tipo no existe en la HU → asumir Tipo=Funcional"
  - instruccion: "SI Tipo=Bug → Cargar archivo de bug referenciado y usar estructura_fases.bugfix"

reglas_arquitectonicas_requeridas:
  descripcion: "Si hay reglas arquitectónicas cargadas, aplicar:"
  secciones:
    - seccion: "arquitectura.estructura"
      aplicar: "Planificar creación de archivos en carpetas según estructura definida"
    - seccion: "nomenclatura.*"
      aplicar: "Usar convenciones de nombres en tareas del plan"
    - seccion: "testing.metodologia"
      aplicar: "Si TDD, incluir tarea de tests ANTES de implementación"
    - seccion: "documentacion.adr_obligatorio"
      aplicar: "Si aplica, incluir tarea de ADR en el plan"
  si_no_existe: "Planificar con mejores prácticas estándar del stack"

condiciones_entrada:
  - condicion: "HU en estado [A] Aprobada"
    si_no_cumple: "Ejecutar >validar_hu primero"
  - condicion_alternativa: "HU con Tipo=Bug y severidad Crítica en estado [R] Refinada"
    si_cumple: "Permitir planificación directa (bypass de validación para bugs críticos)"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a planificar"
  opcionales:
    - nombre: proyecto
      tipo: string
      descripcion: "Proyecto específico (auto-detectado desde campo Proyecto de la HU)"
      defecto: null
    - nombre: incluir_migraciones
      tipo: boolean
      defecto: true
    - nombre: incluir_rollback
      tipo: boolean
      defecto: true

estructura_fases:
  # Fases dinámicas según arquitectura detectada en contexto_proyecto.md
  hexagonal:
    fase_1: "Infraestructura (migraciones, configuración)"
    fase_2: "Dominio (entidades, value objects, puertos)"
    fase_3: "Aplicación (casos de uso, DTOs)"
    fase_4: "Adaptadores (controllers, repositorios)"
    fase_5: "Testing (unitarios, integración)"
  mvc:
    fase_1: "Infraestructura (migraciones, configuración)"
    fase_2: "Modelos (entidades, validaciones)"
    fase_3: "Controladores (rutas, lógica)"
    fase_4: "Vistas (templates, respuestas)"
    fase_5: "Testing (unitarios, integración)"
  capas:
    fase_1: "Infraestructura (migraciones, configuración)"
    fase_2: "Datos (entidades, repositorios)"
    fase_3: "Negocio (servicios, lógica)"
    fase_4: "Presentación (API, UI)"
    fase_5: "Testing (unitarios, integración)"
  script:
    fase_1: "Setup (dependencias, configuración)"
    fase_2: "Lógica Principal (funciones core)"
    fase_3: "Testing (unitarios)"
  frontend:
    fase_1: "Setup (dependencias, estructura)"
    fase_2: "Componentes (UI, props/state)"
    fase_3: "Hooks/Services (lógica, API)"
    fase_4: "Integración (rutas, estado global)"
    fase_5: "Testing (unitarios, e2e)"
  default:
    fase_1: "Preparación (setup, configuración)"
    fase_2: "Implementación (lógica principal)"
    fase_3: "Testing (validación)"
  bugfix:
    fase_1: "Reproducción y Diagnóstico (validar bug, confirmar causa raíz desde BUG-NNN)"
    fase_2: "Corrección (implementar fix en archivos identificados)"
    fase_3: "Testing de Regresión (test del caso específico + regresión en módulo afectado)"

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones:
      - "Establecer valores por defecto para parámetros opcionales no especificados: incluir_migraciones=true, incluir_rollback=true"
      - "Mostrar resumen compacto de configuración activa:"
      - "  ⚙️ Configuración: migraciones=[sí/no] | rollback=[sí/no]"
      - "  Personaliza con: >planificar_hu [ID-HU] --incluir_migraciones false"
    nota: "Garantiza evaluación correcta de condiciones y visibilidad de la configuración activa"

  - paso: "Cargar HU y Contexto"
    obligatorio: true
    acciones: 
      - "Buscar HU en backlog"
      - "Extraer campo '- **Tipo:**' de la HU (SI no existe → asumir Funcional)"
      - "SI Tipo = Bug:"
      - "  1. Verificar estado mínimo [R] Refinada O [A] Aprobada"
      - "  2. SI severidad es 🔴 Crítica y estado [R] → Permitir planificación directa (bypass validación)"
      - "  3. Extraer campo 'Ref_Bug' → Cargar archivo de bug desde {{artifacts.bugs_folder}}/[BUG-NNN]*.md"
      - "  4. Extraer del archivo bug: Causa Raíz, Archivos Afectados, Corrección (si existe)"
      - "  5. SI existe sección '🐛 Ajustes por Bug' en refinamiento → Incorporar instrucciones"
      - "  6. Guardar tipo_hu='Bug' para usar estructura_fases.bugfix"
      - "SI Tipo != Bug:"
      - "  Verificar estado [A] Aprobada (flujo estándar)"
      - "  Guardar tipo_hu='Funcional'"
      - "Extraer campo '- **Proyecto:**' de la HU"
      - "SI Proyecto = 'compartida':"
      - "  1. Leer sección '**Proyectos afectados:**' de la HU (lista de proyectos)"
      - "  2. Para cada proyecto listado → Cargar contexto desde {{artifacts.contextos_folder}}/[proyecto]_contexto.md"
      - "  3. Planificar tareas agrupadas por proyecto cuando corresponda"
      - "SI Proyecto = [nombre] → Cargar contexto desde {{artifacts.contextos_folder}}/[proyecto]_contexto.md"
      - "Cargar refinamiento de la HU (contiene decisiones técnicas del ADR si aplica)"
      - "Identificar HUs relacionadas en backlog (misma épica, feature o dominio)"
      - "Detectar componentes reutilizables de HUs ya implementadas [X]"
      - "Registrar dependencias o conflictos potenciales con HUs en progreso [E]"
    si_error:
      no_aprobada: " HU debe estar aprobada. Ejecutar >validar_hu primero"
      contexto_no_encontrado: " Contexto del proyecto '[proyecto]' no encontrado"

  - paso: "Detección de Ambigüedades"
    obligatorio: true
    descripcion: "NUNCA asumir. Ante cualquier duda técnica, preguntar al usuario."
    acciones:
      - "Analizar HU, CA y ADR buscando: tecnologías no especificadas, rutas ambiguas, decisiones técnicas faltantes"
      - "SI se detectan ambigüedades → Listar preguntas claras y específicas"
      - "PAUSAR y esperar respuestas del usuario antes de continuar"
      - "Incorporar respuestas al contexto de planificación"
    comportamiento:
      si_hay_dudas: "PREGUNTAR y ESPERAR respuesta"
      si_no_hay_dudas: "Continuar al siguiente paso"
    ejemplo_preguntas:
      - "¿El nuevo servicio debe ir en app/Services/ o en app/Domain/Services/?"
      - "¿Qué librería usar para validaciones: nativa o externa?"
      - "¿La migración debe ser reversible o irreversible?"

  - paso: "Detectar Arquitectura y Validar Estructura"
    obligatorio: true
    acciones:
      - "SI tipo_hu = 'Bug' → Usar estructura_fases.bugfix directamente (no depende de arquitectura)"
      - "SI tipo_hu != 'Bug':"
      - "  Leer sección '## 4. Arquitectura' en contexto_proyecto"
      - "  Extraer campo 'Estilo' para determinar tipo de fases"
      - "  Validar que '### Estructura del Proyecto' esté documentada y sea coherente"
      - "  SI estructura es ambigua o incompleta → PREGUNTAR al usuario"
      - "  Mapear estilo a estructura_fases:"
      - "  SI estilo CONTIENE 'Hexagonal' → usar estructura_fases.hexagonal"
      - "  SI estilo CONTIENE 'MVC' → usar estructura_fases.mvc"
      - "  SI estilo CONTIENE 'Capas' → usar estructura_fases.capas"
      - "  SI estilo CONTIENE 'Script' OR tipo='CLI' → usar estructura_fases.script"
      - "  SI estilo CONTIENE 'Frontend' OR framework IN [React, Vue, Angular] → usar estructura_fases.frontend"
      - "  DEFAULT → usar estructura_fases.default"
      - "Guardar fases seleccionadas en variable 'fases_plan'"
      - "Aplicar convenciones de reglas_arquitectonicas si están disponibles"
    si_no_existe_contexto: "Usar estructura_fases.default y PREGUNTAR rutas al usuario"
    si_inconsistencia: "PAUSAR y confirmar con usuario antes de continuar"

  - paso: "Diseño de Componentes"
    obligatorio: true
    acciones: 
      - "Identificar componentes a crear/modificar según HU y refinamiento"
      - "Definir interfaces y contratos según reglas_arquitectonicas"
      - "Consultar sección '## 4. Arquitectura' > '### Estructura del Proyecto' en contexto_proyecto"
      - "Usar rutas REALES documentadas (NO genéricas)"
    si_ruta_no_existe:
      - "SI no existe ruta clara para un componente → PREGUNTAR al usuario:"
      - "  1. ¿Crear carpeta nueva? Sugerir ruta siguiendo convención de la arquitectura detectada"
      - "     Ejemplo Hexagonal: 'Sugiero src/Application/UseCases/[NuevoUseCase]/ ¿Es correcto?'"
      - "     Ejemplo MVC: 'Sugiero app/Services/[NuevoServicio]/ ¿Es correcto?'"
      - "  2. ¿Ubicar en carpeta existente? ¿Cuál de las documentadas?"
      - "ESPERAR respuesta antes de continuar"

  - paso: "Planificación de Migraciones"
    obligatorio: false
    condicion: "incluir_migraciones=true y hay cambios en BD"
    acciones: ["Diseñar scripts de migración", "Definir nomenclatura (Flyway/Liquibase)", "Incluir plan de rollback si incluir_rollback=true"]

  - paso: "Secuenciación de Tareas"
    obligatorio: true
    acciones: 
      - "Ordenar tareas por dependencias"
      - "Agrupar en fases según 'fases_plan' detectado"
      - "Asignar rutas consultando '## 4. Arquitectura' > '### Estructura del Proyecto'"
      - "Asignar estimación por tarea"

  - paso: "Generación del Plan"
    obligatorio: true
    acciones: 
      - "Leer plantilla desde {{plantillas.plan_implementacion}}"
      - "Rellenar metadata (ID-HU, título, fecha, estimación)"
      - "Rellenar campo 'Arquitectura' con estilo de '## 4. Arquitectura'"
      - "Generar tabla 'Progreso General' con fases de 'fases_plan'"
      - "Generar secciones de fase según 'fases_plan'"
      - "En cada tarea, usar rutas de '### Estructura del Proyecto' (NO genéricas)"
      - "Ejemplo correcto: 'Crear User.php en app/Models/' (ruta real)"
      - "Ejemplo incorrecto: 'Crear User en models/' (ruta genérica)"
      - "Copiar criterios de aceptación de la HU a Fase Final"
      - "Guardar en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"

  - paso: "Actualización de Estado"
    obligatorio: true
    acciones: ["Cambiar estado HU a [P] Planificada en {{archivos.backlog}}", "Agregar referencia al plan en la HU"]

salida:
  archivos_generados:
    ruta: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
    plantilla: "{{plantillas.plan_implementacion}}"
  archivos_actualizados: ["{{archivos.backlog}}"]
  estado_hu_final: "[P] Planificada"
  mensaje_exito: |
     PLAN GENERADO: [ID-HU]
     Artefacto: {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
     Fases: [N] | Tareas: [M] | Estimación: [X]h | Criterios: [Y]
     Siguiente: >ejecutar_plan [ID-HU]

errores:
  hu_no_aprobada: {msg: " HU no está en estado [A] Aprobada", accion: "Ejecutar >validar_hu primero"}
  sin_contexto: {msg: "ℹ Sin contexto de proyecto", accion: "Ejecutar >tomar_contexto para mejor planificación"}

siguiente:
  - {comando: ">ejecutar_plan [ID-HU]", desc: "Ejecutar el plan generado", chat_agente: "ArchDev Pro"}
```
