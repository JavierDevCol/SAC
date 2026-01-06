```yaml
mandatory:
  - instruccion: "Seguir el proceso paso a paso en orden secuencial"
    nunca_saltar: true
  - instruccion: "Validar prerequisitos antes de ejecutar"
    nunca_saltar: true
  - instruccion: "Los pasos marcados como obligatorio:true NO se pueden omitir"
    nunca_saltar: true
  - instruccion: "Actualizar session_state.json al finalizar"
    nunca_saltar: true
  - instruccion: "Generar plan alineado con arquitectura del proyecto"
    nunca_saltar: true
  - instruccion: "Incluir tareas de testing en el plan"
    nunca_saltar: true
  - instruccion: "Especificar orden de ejecución y dependencias"
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
      ubicacion: "{{backlog_location}}"
      estado_requerido: "[A] Aprobada"
  archivos_opcionales:
    - "{{contexto_proyecto_location}}"
    - "{{reglas_arquitectonicas_location}}"

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
      - "Buscar HU en {{backlog_location}}"
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
      - "Crear archivo de plan de implementación"
      - "Incluir código esqueleto cuando sea útil"
      - "Guardar en {{planes_location}}"

  paso_6:
    nombre: "Actualización de Estado"
    obligatorio: true
    acciones:
      - "Cambiar estado HU a [P] Planificada"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Abrir/crear {{session_state_location}}"
      - "Registrar herramienta ejecutada: planificar_hu"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Actualizar estado de la HU planificada"
      - "Guardar cambios en session_state.json"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "planificar_hu"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"

salida:
  archivos_generados:
    - tipo: "plan_implementacion"
      ruta: "{{planes_location}}/[ID-HU]_plan_implementacion.md"
  
  archivos_actualizados:
    - "{{backlog_location}}"
    - "{{session_state_location}}"
  
  estado_hu_final: "[P] Planificada"
  
  mensaje_exito: |
    ✅ PLAN DE IMPLEMENTACIÓN GENERADO: [ID-HU]
    
    📄 Artefacto: {{planes_location}}/[ID-HU]_plan_implementacion.md
    
    📊 Resumen:
    - Fases: [N]
    - Tareas totales: [M]
    - Estimación: [X] horas
    
    💡 Siguiente: +ARCHDEV >ejecutar_plan [ID-HU]

formato_plan: |
  📋 Plan de Implementación: [ID-HU] - [Título]
  
  ## Metadata
  - **Generado por:** ONAD
  - **Fecha:** [timestamp]
  - **Estimación total:** [X] horas
  
  ## Fase 1: Infraestructura
  ### Migraciones
  - [ ] `V[XXX]__[descripcion].sql`
    ```sql
    -- Contenido de la migración
    ```
  
  ## Fase 2: Dominio
  ### Entidades
  - [ ] Crear `[Entidad].java` en `domain/model/`
  
  ## Fase 3: Aplicación
  ### Casos de Uso
  - [ ] Crear `[CasoDeUso]UseCase.java`
  
  ## Fase 4: Adaptadores
  ### Controllers
  - [ ] Crear/Modificar `[Controller].java`
  
  ## Fase 5: Testing
  - [ ] Tests unitarios para dominio
  - [ ] Tests de integración para adaptadores
  
  ## Notas de Implementación
  [Consideraciones especiales]

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
  rol_requerido: "ARCHDEV"
  descripcion: "Ejecutar el plan de implementación generado"
```
