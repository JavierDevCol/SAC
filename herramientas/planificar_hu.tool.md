---
nombre: "Planificar Historia de Usuario"
comando: ">planificar_hu"
alias: [">planificar", ">plan_hu"]
version: "4.1"
---

```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
  - instruccion: "Validar prerequisitos antes de ejecutar"
  - instruccion: "Pasos obligatorios NO se pueden omitir"
  - instruccion: "Generar plan alineado con arquitectura del proyecto"
  - instruccion: "Incluir tareas de testing en el plan"
  - instruccion: "Especificar orden de ejecución y dependencias"
  - instruccion: "Generar en idioma: {{preferencias.idioma_documentacion}}"
  - instruccion: "Usar plantilla {{plantillas.plan_implementacion}}"
  - instruccion: "Incluir TODOS los criterios de aceptación de la HU en Fase Final"
  - instruccion: "Si {{usuario.incluir_firma_en_documentos}}=true, agregar pie: '---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---'"

prerequisitos:
  archivos_requeridos:
    - descripcion: "HU aprobada arquitectónicamente"
      ubicacion: "{{archivos.backlog}}"
      estado_requerido: "[A] Aprobada"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"
    - "{{archivos.reglas_arquitectonicas}}"

parametros:
  requeridos:
    - nombre: id_hu
      tipo: string
      descripcion: "Identificador de la HU a planificar"
  opcionales:
    - nombre: incluir_migraciones
      tipo: boolean
      defecto: true
    - nombre: incluir_rollback
      tipo: boolean
      defecto: true

estructura_fases:
  fase_1: "Infraestructura (migraciones, configuración)"
  fase_2: "Dominio (entidades, value objects)"
  fase_3: "Aplicación (casos de uso, servicios)"
  fase_4: "Adaptadores (controllers, repositorios)"
  fase_5: "Testing (unitarios, integración)"

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: incluir_migraciones=true, incluir_rollback=true"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Cargar HU y Contexto"
    obligatorio: true
    acciones: ["Buscar HU en {{archivos.backlog}}", "Verificar estado [A] Aprobada", "Cargar refinamiento y {{archivos.contexto_proyecto}}"]
    si_error:
      no_aprobada: " HU debe estar aprobada. Ejecutar >validar_hu primero"

  - paso: "Diseño de Componentes"
    obligatorio: true
    acciones: ["Identificar componentes a crear/modificar", "Definir interfaces y contratos", "Especificar ubicación de archivos"]

  - paso: "Planificación de Migraciones"
    obligatorio: false
    condicion: "incluir_migraciones=true y hay cambios en BD"
    acciones: ["Diseñar scripts de migración", "Definir nomenclatura (Flyway/Liquibase)", "Incluir plan de rollback si incluir_rollback=true"]

  - paso: "Secuenciación de Tareas"
    obligatorio: true
    acciones: ["Ordenar tareas por dependencias", "Agrupar en fases según estructura_fases", "Asignar estimación por tarea"]

  - paso: "Generación del Plan"
    obligatorio: true
    acciones: ["Leer plantilla desde {{plantillas.plan_implementacion}}", "Rellenar metadata (ID-HU, título, fecha, estimación)", "Incluir tareas organizadas por fases", "Copiar criterios de aceptación de la HU", "Guardar en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"]

  - paso: "Actualización de Estado"
    obligatorio: true
    acciones: ["Cambiar estado HU a [P] Planificada en {{archivos.backlog}}", "Agregar referencia al plan en la HU"]

salida:
  archivos_generados:
    ruta: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
    plantilla: "{{plantillas.plan_implementacion}}"
  archivos_actualizados: ["{{archivos.backlog}}"]
  estado_hu_final: "[P] Planificada"
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
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
