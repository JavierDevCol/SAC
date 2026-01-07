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
  - instruccion: "Evaluar TODAS las áreas DevOps antes de emitir diagnóstico"
    nunca_saltar: true
  - instruccion: "Priorizar backlog por impacto/esfuerzo"
    nunca_saltar: true
  - instruccion: "Incluir consideraciones de seguridad en cada área"
    nunca_saltar: true
  - instruccion: "Generar diagnósticos en el idioma configurado en {{preferencias.idioma_documentacion}}"
    nunca_saltar: true

identificacion:
  nombre: "Diagnosticar DevOps"
  comando: ">diagnosticar_devops"
  alias: [">diagnostico", ">madurez_devops"]
  version: "4.0"

roles_autorizados:
  - DEVOPS

prerequisitos:
  archivos_requeridos:
    - descripcion: "Acceso al repositorio del proyecto"
  archivos_opcionales:
    - "{{archivos.contexto_proyecto}}"
    - ".github/workflows/ | .gitlab-ci.yml | Jenkinsfile"
    - "Dockerfile | docker-compose.yml"
    - "terraform/ | bicep/ | cloudformation/"

parametros:
  opcionales:
    - nombre: areas
      tipo: array
      valores: [cicd, iac, observabilidad, seguridad, cultura]
      defecto: [cicd, iac, observabilidad, seguridad, cultura]
    - nombre: nivel_detalle
      tipo: string
      valores: [resumen, completo, exhaustivo]
      defecto: completo

areas_evaluacion:
  cicd:
    nombre: "CI/CD"
    criterios:
      - "Pipelines automatizados"
      - "Tests en pipeline"
      - "Deployment automatizado"
      - "Rollback capability"
    niveles:
      1: "Manual o inexistente"
      2: "CI básico (build + test)"
      3: "CI/CD con staging"
      4: "CI/CD con canary/blue-green"
      5: "GitOps completo"
  
  iac:
    nombre: "Infrastructure as Code"
    criterios:
      - "Infra definida en código"
      - "Versionado en Git"
      - "Idempotencia"
      - "Módulos reutilizables"
    niveles:
      1: "Manual/clickops"
      2: "Scripts ad-hoc"
      3: "IaC básico (Terraform/Bicep)"
      4: "Módulos + state management"
      5: "GitOps + policy as code"
  
  observabilidad:
    nombre: "Observabilidad"
    criterios:
      - "Logs centralizados"
      - "Métricas de aplicación"
      - "Tracing distribuido"
      - "Alertas configuradas"
    niveles:
      1: "Sin observabilidad"
      2: "Logs básicos"
      3: "Métricas + dashboards"
      4: "Tracing + correlación"
      5: "AIOps / auto-remediation"
  
  seguridad:
    nombre: "Seguridad (DevSecOps)"
    criterios:
      - "SAST en pipeline"
      - "Dependency scanning"
      - "Secret management"
      - "Container scanning"
    niveles:
      1: "Sin controles"
      2: "Scanning manual"
      3: "SAST/DAST en CI"
      4: "Secret management + policies"
      5: "Zero-trust + compliance automatizado"
  
  cultura:
    nombre: "Cultura DevOps"
    criterios:
      - "Colaboración Dev-Ops"
      - "Ownership de código"
      - "Blameless postmortems"
      - "Mejora continua"
    niveles:
      1: "Silos tradicionales"
      2: "Colaboración reactiva"
      3: "Ownership compartido"
      4: "Equipos autónomos"
      5: "Cultura de excelencia"

proceso:
  paso_1:
    nombre: "Recolección de Contexto"
    obligatorio: true
    acciones:
      - "Escanear estructura del repositorio"
      - "Identificar archivos de CI/CD"
      - "Detectar IaC y configuración"
      - "Analizar documentación existente"

  paso_2:
    nombre: "Evaluación por Área"
    obligatorio: true
    acciones:
      - "Para cada área seleccionada:"
      - "  - Evaluar criterios específicos"
      - "  - Asignar nivel de madurez (1-5)"
      - "  - Documentar evidencia"
      - "  - Identificar gaps"

  paso_3:
    nombre: "Generación de Matriz de Madurez"
    obligatorio: true
    acciones:
      - "Consolidar evaluaciones"
      - "Calcular promedio ponderado"
      - "Generar visualización de matriz"

  paso_4:
    nombre: "Creación de Backlog Priorizado"
    obligatorio: true
    acciones:
      - "Identificar mejoras por área"
      - "Evaluar impacto vs esfuerzo"
      - "Priorizar por Quick Wins primero"
      - "Generar roadmap sugerido"

  paso_5:
    nombre: "Generación de Reporte"
    obligatorio: true
    acciones:
      - "Crear reporte completo"
      - "Incluir recomendaciones específicas"
      - "Guardar en artifacts"

  paso_final:
    nombre: "Actualizar Estado de Sesión"
    obligatorio: true
    importante: "⚠️ ESTE PASO ES OBLIGATORIO EN TODA HERRAMIENTA"
    acciones:
      - "Verificar si existe {{archivos.session_state}}"
      - "Si NO existe:"
      - "  1. Crear estructura de carpetas {{rutas.session_folder}} si no existe"
      - "  2. Copiar plantilla desde {{plantillas.session_state}}"
      - "  3. Inicializar con valores por defecto"
      - "Si existe:"
      - "  1. Leer estado actual"
      - "  2. Actualizar campos correspondientes"
      - "Registrar herramienta ejecutada: diagnosticar_devops"
      - "Actualizar timestamp de ultima_actividad"
      - "Registrar artefactos generados en la sesión"
      - "Si hay HU activa, actualizar su estado"
      - "Guardar cambios en {{archivos.session_state}}"
    plantilla_referencia: "{{plantillas.session_state}}"
    campos_a_actualizar:
      - campo: "ultima_herramienta"
        valor: "diagnosticar_devops"
      - campo: "ultima_actividad"
        valor: "[timestamp ISO 8601]"
      - campo: "artefactos_generados"
        valor: "[lista de archivos creados/modificados]"
      - campo: "resultado_ejecucion"
        valor: "[exito|error|parcial]"
    validacion_post:
      - "Confirmar que {{archivos.session_state}} existe y es válido"
      - "Confirmar que el JSON es parseable"

salida:
  archivos_generados:
    - tipo: "diagnostico"
      ruta: "{{rutas.artifacts_folder}}/diagnostico_devops_[timestamp].md"
  
  archivos_actualizados:
    - "{{archivos.session_state}}"
  
  mensaje_exito: |
    ✅ DIAGNÓSTICO DEVOPS COMPLETADO
    
    📊 Matriz de Madurez:
    | Área | Nivel | Estado |
    |------|-------|--------|
    | CI/CD | [N]/5 | [emoji] |
    | IaC | [N]/5 | [emoji] |
    | Observabilidad | [N]/5 | [emoji] |
    | Seguridad | [N]/5 | [emoji] |
    | Cultura | [N]/5 | [emoji] |
    
    📈 Madurez Promedio: [X.X]/5
    
    🎯 Top 3 Quick Wins:
    1. [mejora 1]
    2. [mejora 2]
    3. [mejora 3]

formato_matriz:
  niveles_emoji:
    1: "🔴"
    2: "🟠"
    3: "🟡"
    4: "🟢"
    5: "⭐"

errores:
  sin_contexto:
    mensaje: "ℹ️ Sin archivos de infraestructura detectados"
    accion: "Evaluar basándose en entrevista con usuario"
  acceso_limitado:
    mensaje: "⚠️ Acceso limitado a algunos recursos"
    accion: "Marcar áreas como 'No evaluable'"

siguiente:
  opciones:
    - comando: "Implementar Quick Win #1"
      descripcion: "Comenzar con mejora de mayor impacto/menor esfuerzo"
    - herramienta: "tomar_contexto"
      comando: ">tomar_contexto"
      descripcion: "Generar contexto completo del proyecto"
```
