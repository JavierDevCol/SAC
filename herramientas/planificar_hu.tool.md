```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Generar plan alineado con arquitectura del proyecto"
    nunca_saltar: true
  - instruccion: "Incluir tareas de testing en el plan"
    nunca_saltar: true
  - instruccion: "Especificar orden de ejecución y dependencias"
    nunca_saltar: true
  - instruccion: "Generar documentación en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true
  - instruccion: "Usar plantilla {{plantillas.plan_implementacion}} para generar el plan"
    nunca_saltar: true
  - instruccion: "Incluir TODOS los criterios de aceptación de la HU en Fase Final"
    nunca_saltar: true

identificacion:
  nombre: "Planificar Historia de Usuario"
  comando: ">planificar_hu"
  alias: [">planificar", ">plan_hu"]
  version: "4.0"

roles_autorizados:
  - ONAD

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

proceso:
  paso_1:
    nombre: "Cargar HU y Contexto"
    obligatorio: true
    acciones:
      - "Buscar HU en {{archivos.backlog}}"
      - "Verificar estado [A] Aprobada"
      - "Cargar refinamiento y contexto del proyecto"
    si_error:
      no_aprobada: "⚠️ HU debe estar aprobada. Ejecutar >validar_hu primero"

  paso_2:
    nombre: "Diseño de Componentes"
    obligatorio: true
    acciones:
      - "Identificar componentes a crear/modificar"
      - "Definir interfaces y contratos"
      - "Especificar ubicación de archivos"
    output:
      - "Lista de clases/archivos nuevos"
      - "Modificaciones a archivos existentes"
      - "Interfaces y DTOs requeridos"

  paso_3:
    nombre: "Planificación de Migraciones"
    obligatorio: false
    condicion: "si incluir_migraciones=true y hay cambios en BD"
    acciones:
      - "Diseñar scripts de migración"
      - "Definir nomenclatura según gestor (Flyway/Liquibase)"
      - "Incluir plan de rollback"

  paso_4:
    nombre: "Secuenciación de Tareas"
    obligatorio: true
    acciones:
      - "Ordenar tareas por dependencias"
      - "Agrupar en fases lógicas"
      - "Asignar estimación por tarea"
    estructura_fases:
      fase_1: "Infraestructura (migraciones, configuración)"
      fase_2: "Dominio (entidades, value objects)"
      fase_3: "Aplicación (casos de uso, servicios)"
      fase_4: "Adaptadores (controllers, repositorios)"
      fase_5: "Testing (unitarios, integración)"

  paso_5:
    nombre: "Generación del Plan"
    obligatorio: true
    acciones:
      - "Leer plantilla desde {{plantillas.plan_implementacion}}"
      - "Rellenar plantilla con:"
      - "  - Metadata (ID-HU, título, fecha, estimación)"
      - "  - Tareas organizadas por fases"
      - "  - Código esqueleto cuando sea útil"
      - "  - Criterios de aceptación copiados de la HU"
      - "Guardar en {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
    plantilla_referencia: "{{plantillas.plan_implementacion}}"

  paso_6:
    nombre: "Actualización de Estado"
    obligatorio: true
    acciones:
      - "Cambiar estado HU a [P] Planificada en {{archivos.backlog}}"
      - "Agregar referencia al plan en la HU"

salida:
  archivos_generados:
    - tipo: "plan_implementacion"
      ruta: "{{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md"
      plantilla: "{{plantillas.plan_implementacion}}"
  
  archivos_actualizados:
    - "{{archivos.backlog}}"
  
  estado_hu_final: "[P] Planificada"
  
  mensaje_exito: |
    ✅ PLAN DE IMPLEMENTACIÓN GENERADO: [ID-HU]
    
    📄 Artefacto: {{artifacts.planes_folder}}/[ID-HU]_plan_implementacion.md
    
    📊 Resumen:
    - Fases: [N]
    - Tareas totales: [M]
    - Estimación: [X] horas
    - Criterios de Aceptación: [Y]
    
    💡 Siguiente: +ARCHDEV >ejecutar_plan [ID-HU]

errores:
  hu_no_aprobada:
    mensaje: "⚠️ HU no está en estado [A] Aprobada"
    accion: "Ejecutar >validar_hu [ID-HU] primero"
  sin_contexto:
    mensaje: "ℹ️ Sin contexto de proyecto"
    accion: "Ejecutar >tomar_contexto para mejor planificación"

siguiente:
  herramienta: "ejecutar_plan"
  comando: ">ejecutar_plan [ID-HU]"
  agente: "ArchDev Pro"
  descripcion: "Ejecutar el plan de implementación generado"
  accion_usuario: |
    Para continuar:
    1. Abre un nuevo chat con el agente **ArchDev Pro**
    2. Ejecuta: `>ejecutar_plan [ID-HU]`
```
