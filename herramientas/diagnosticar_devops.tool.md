---
nombre: "Diagnosticar DevOps"
comando: ">diagnosticar_devops"
alias: [">diagnostico", ">madurez_devops"]
---

```yaml
mandatory_base: "Cargar y aplicar TODAS las instrucciones de _base.tool.md ANTES de ejecutar esta herramienta. CRUCIAL - NO SALTAR."

mandatory_especifico:
  - instruccion: "Evaluar TODAS las áreas antes del diagnóstico"
  - instruccion: "Priorizar backlog por impacto/esfuerzo"
  - instruccion: "Incluir seguridad en cada área"

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
    criterios: [Pipelines automatizados, Tests en pipeline, Deploy automatizado, Rollback]
    niveles: {1: Manual/inexistente, 2: CI básico, 3: CI/CD+staging, 4: Canary/blue-green, 5: GitOps completo}
  
  iac:
    nombre: "Infrastructure as Code"
    criterios: [Infra en código, Versionado Git, Idempotencia, Módulos reutilizables]
    niveles: {1: Clickops, 2: Scripts ad-hoc, 3: Terraform/Bicep básico, 4: Módulos+state, 5: GitOps+policy-as-code}
  
  observabilidad:
    nombre: "Observabilidad"
    criterios: [Logs centralizados, Métricas app, Tracing distribuido, Alertas]
    niveles: {1: Sin observabilidad, 2: Logs básicos, 3: Métricas+dashboards, 4: Tracing+correlación, 5: AIOps/auto-remediation}
  
  seguridad:
    nombre: "DevSecOps"
    criterios: [SAST en pipeline, Dependency scanning, Secret management, Container scanning]
    niveles: {1: Sin controles, 2: Scanning manual, 3: SAST/DAST en CI, 4: Secrets+policies, 5: Zero-trust+compliance}
  
  cultura:
    nombre: "Cultura DevOps"
    criterios: [Colaboración Dev-Ops, Ownership código, Blameless postmortems, Mejora continua]
    niveles: {1: Silos, 2: Colaboración reactiva, 3: Ownership compartido, 4: Equipos autónomos, 5: Excelencia}

proceso:
  - paso: "Inicialización de Parámetros"
    obligatorio: true
    acciones: ["Establecer valores por defecto para parámetros opcionales no especificados: areas=[cicd, iac, observabilidad, seguridad, cultura], nivel_detalle='completo'"]
    nota: "Garantiza evaluación correcta de condiciones en pasos posteriores"

  - paso: "Recolección de Contexto"
    obligatorio: true
    acciones: [Escanear repo, Identificar CI/CD, Detectar IaC, Analizar docs]

  - paso: "Evaluación por Área"
    obligatorio: true
    acciones: [Evaluar criterios, Asignar nivel 1-5, Documentar evidencia, Identificar gaps]

  - paso: "Matriz de Madurez"
    obligatorio: true
    acciones: [Consolidar evaluaciones, Calcular promedio, Generar visualización]

  - paso: "Backlog Priorizado"
    obligatorio: true
    acciones: [Identificar mejoras, Evaluar impacto/esfuerzo, Quick Wins primero, Roadmap]

  - paso: "Reporte"
    obligatorio: true
    acciones: [Crear reporte, Recomendaciones, Guardar en artifacts, Referenciar en {{contexto_proyecto}}]

salida:
  archivos_generados:
    ruta: "{{rutas.artifacts_folder}}/diagnostico_devops_[timestamp].md"
    template: |
      📊 Matriz: [Área | Nivel/5 | Emoji] por cada área
      📈 Madurez Promedio: [X.X]/5
      🎯 Top 3 Quick Wins: [lista priorizada]
  formato_matriz:
    emojis: {1: 🔴, 2: 🟠, 3: 🟡, 4: 🟢, 5: ⭐}
  pie_documento:
    condicion: "{{usuario.incluir_firma_en_documentos}} = true AND {{usuario.nombre}} no vacío"
    formato: "---\n✅ Revisado por **{{usuario.nombre}}** | 📅 {{fecha}}\n---"
  mensaje_exito: |
    ✅ DIAGNÓSTICO DEVOPS COMPLETADO
    
    📊 Resumen:
    - Áreas evaluadas: [N]
    - Madurez promedio: [X.X]/5
    
    📄 Artefactos:
    - diagnostico_devops_[timestamp].md
  

errores:
  sin_contexto: {msg: "ℹ️ Sin infra detectada", accion: "Evaluar vía entrevista"}
  acceso_limitado: {msg: "⚠️ Acceso limitado", accion: "Marcar 'No evaluable'"}

siguiente:
  - {accion: "Implementar Quick Win #1", desc: "Mayor impacto/menor esfuerzo"}
  - {comando: ">tomar_contexto", desc: "Generar contexto completo"}
```
