# 🛠️ Herramientas Potenciales para Arquitecto DevOps

> Documento de análisis y especificación de herramientas potenciales identificadas durante la refactorización del rol **Arquitecto DevOps**. Este documento sirve como referencia para futuras implementaciones o refactorizaciones de herramientas existentes.

---

## 📋 Índice

1. [Herramienta 1: `identificar_entorno_devops`](#1-identificar_entorno_devops)
2. [Herramienta 2: `recopilar_contexto_operativo`](#2-recopilar_contexto_operativo)
3. [Herramienta 3: `generar_plan_incremental_devops`](#3-generar_plan_incremental_devops)
4. [Herramienta 4: `analizar_superficie_seguridad`](#4-analizar_superficie_seguridad)
5. [Mejora a herramienta existente: `diagnosticar_devops`](#5-mejora-diagnosticar_devops)

---

## 1. `identificar_entorno_devops`

### 🎯 Propósito

Detectar automáticamente el entorno tecnológico del proyecto (cloud provider, orquestación, IaC, CI/CD) analizando archivos de configuración, código de infraestructura y estructura del proyecto.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es el "Paso Crítico" que el Arquitecto DevOps SIEMPRE debe ejecutar antes de dar recomendaciones.

### 🔍 Problema que Resuelve

- **Antes:** El arquitecto debe preguntar manualmente al usuario sobre su entorno, lo que consume tiempo y puede llevar a respuestas incompletas.
- **Después:** La herramienta escanea el proyecto y presenta un resumen automático del stack detectado, permitiendo al usuario solo confirmar o corregir.

### 📥 Input Esperado

**Parámetros:**
- `ruta_proyecto` (string, requerido): Path al directorio raíz del proyecto
- `profundidad_escaneo` (enum, opcional): `basico` | `completo` (default: `basico`)
  - `basico`: Solo archivos de configuración principales
  - `completo`: Incluye análisis de dependencias, versiones, configuraciones anidadas

**Archivos que debe buscar:**
- **Cloud Provider:**
  - AWS: `terraform.tf` con provider aws, `cloudformation.yaml`, `.aws/`, `cdk.json`
  - Azure: `*.bicep`, `*.json` (ARM templates), `azure-pipelines.yml`
  - GCP: `terraform.tf` con provider google, `cloudbuild.yaml`, `app.yaml`
  
- **Contenedores:**
  - Docker: `Dockerfile`, `docker-compose.yml`, `.dockerignore`
  - Kubernetes: `*.yaml` en carpetas `k8s/`, `kubernetes/`, archivos con `kind: Deployment`
  - Helm: `Chart.yaml`, `values.yaml`, `templates/`

- **CI/CD:**
  - GitHub Actions: `.github/workflows/*.yml`
  - GitLab CI: `.gitlab-ci.yml`
  - Jenkins: `Jenkinsfile`
  - Azure DevOps: `azure-pipelines.yml`
  - CircleCI: `.circleci/config.yml`

- **IaC:**
  - Terraform: `*.tf`, `terraform.tfvars`, `.terraform/`
  - Bicep: `*.bicep`
  - Pulumi: `Pulumi.yaml`, archivos en lenguajes de programación con imports de Pulumi
  - Ansible: `playbook.yml`, `inventory/`, `roles/`

- **Observabilidad:**
  - Prometheus: `prometheus.yml`
  - Grafana: `grafana.ini`, dashboards JSON
  - ELK: `elasticsearch.yml`, `logstash.conf`, `kibana.yml`
  - Datadog: `datadog.yaml`

### 📤 Output Esperado

**Formato: JSON estructurado + Resumen markdown**

```json
{
  "deteccion_completada": true,
  "timestamp": "2025-10-05T17:45:00Z",
  "entorno": {
    "cloud_provider": {
      "principal": "AWS",
      "confianza": 95,
      "evidencias": [
        "terraform.tf con provider 'aws'",
        "Dockerfile con imágenes de ECR",
        ".github/workflows/deploy.yml menciona AWS credentials"
      ]
    },
    "contenedores": {
      "tecnologias": ["Docker", "Kubernetes"],
      "orquestador": "Kubernetes",
      "confianza": 90,
      "evidencias": [
        "Dockerfile en raíz",
        "k8s/deployment.yaml encontrado",
        "helm/Chart.yaml encontrado"
      ]
    },
    "iac": {
      "herramientas": ["Terraform"],
      "version": "1.5.0",
      "modulos_detectados": 3,
      "confianza": 100,
      "evidencias": [
        "main.tf, variables.tf, outputs.tf",
        ".terraform.lock.hcl presente"
      ]
    },
    "ci_cd": {
      "herramientas": ["GitHub Actions"],
      "pipelines_detectados": 2,
      "confianza": 100,
      "evidencias": [
        ".github/workflows/ci.yml",
        ".github/workflows/deploy.yml"
      ]
    },
    "observabilidad": {
      "herramientas": ["Prometheus"],
      "confianza": 70,
      "evidencias": [
        "k8s/prometheus-config.yaml"
      ]
    },
    "seguridad": {
      "herramientas_detectadas": [],
      "secretos_expuestos": false,
      "analisis_pendiente": true
    }
  },
  "recomendaciones_iniciales": [
    "Se detectó uso de Terraform sin tfstate remoto. Considerar S3 + DynamoDB para lock.",
    "No se detectaron herramientas de escaneo de seguridad en pipelines CI/CD.",
    "Helm charts detectados sin values para múltiples ambientes (dev/staging/prod)."
  ]
}
```

**Resumen markdown para el usuario:**

```markdown
## 🔍 Entorno Detectado

### Cloud Provider
- **Principal:** AWS (95% confianza)
- **Evidencias:** terraform.tf con provider 'aws', imágenes ECR en Dockerfile

### Contenedores y Orquestación
- **Tecnologías:** Docker, Kubernetes
- **Orquestador:** Kubernetes (90% confianza)
- **Evidencias:** Dockerfile, k8s/deployment.yaml, helm/Chart.yaml

### Infraestructura como Código
- **Herramienta:** Terraform v1.5.0 (100% confianza)
- **Módulos detectados:** 3

### CI/CD
- **Herramienta:** GitHub Actions (100% confianza)
- **Pipelines:** ci.yml, deploy.yml

### Observabilidad
- **Herramienta:** Prometheus (70% confianza)

### 💡 Recomendaciones Iniciales
1. ⚠️ Terraform sin tfstate remoto detectado → Considerar S3 + DynamoDB
2. ⚠️ No se detectaron herramientas de seguridad en CI/CD
3. ⚠️ Helm charts sin values para múltiples ambientes

¿Es correcto este análisis o hay algo que deba ajustar?
```

### 🔧 Lógica Interna Sugerida

1. **Fase 1: Escaneo de archivos**
   - Recorrer directorios hasta profundidad N (configurable)
   - Buscar patrones de archivos conocidos
   - Leer contenido de archivos clave (primeras 100 líneas)

2. **Fase 2: Análisis de contenido**
   - Parsear archivos YAML/JSON/HCL cuando sea posible
   - Buscar palabras clave (providers, services, resources)
   - Extraer versiones de herramientas

3. **Fase 3: Correlación y confianza**
   - Asignar score de confianza basado en cantidad y calidad de evidencias
   - Detectar conflictos (ej: múltiples cloud providers)

4. **Fase 4: Generación de recomendaciones**
   - Identificar gaps comunes (sin seguridad, sin observabilidad)
   - Sugerir mejoras basadas en best practices

### 🎭 Comportamiento Esperado del Rol

Cuando el Arquitecto DevOps usa esta herramienta:

```markdown
> "Permíteme analizar tu entorno para entender mejor tu infraestructura..."

[Ejecuta herramienta]

> "He detectado que estás trabajando en **AWS con Kubernetes** (EKS probablemente), 
> usando **Terraform** para IaC y **GitHub Actions** para CI/CD. 
> 
> También veo que tienes configurado **Prometheus** para métricas.
> 
> ¿Es correcto este análisis? Si hay algo que deba ajustar, házmelo saber."
```

### 🔗 Integración con Otras Herramientas

- **Complementa a:** `diagnosticar_devops` (le proporciona contexto inicial)
- **Se ejecuta antes de:** Cualquier recomendación o diseño
- **Puede disparar:** `analizar_superficie_seguridad` si detecta riesgos

### 📈 Criterios de Éxito

- ✅ Detecta correctamente el cloud provider en 90%+ de casos
- ✅ Identifica contenedores y orquestadores en 85%+ de casos
- ✅ Reduce de 5-10 preguntas manuales a 1-2 preguntas de confirmación
- ✅ Completa análisis básico en < 10 segundos
- ✅ Completa análisis completo en < 60 segundos

### 🚧 Limitaciones Conocidas

- No puede detectar configuraciones en servicios cloud externos (solo archivos locales)
- Puede confundirse con proyectos multi-cloud
- Necesita acceso de lectura a todos los directorios del proyecto

---

## 2. `recopilar_contexto_operativo`

### 🎯 Propósito

Hacer preguntas estructuradas y dinámicas al usuario sobre su contexto operativo, ajustando el cuestionario según el entorno detectado y el tipo de problema.

### 📊 Nivel de Prioridad

**🟡 MEDIA** - Mejora la experiencia, pero el arquitecto puede hacer preguntas manualmente.

### 🔍 Problema que Resuelve

- **Antes:** El arquitecto debe recordar todas las preguntas contextuales relevantes para cada tipo de problema y entorno.
- **Después:** La herramienta genera un cuestionario dinámico optimizado, garantizando que no se omiten preguntas críticas.

### 📥 Input Esperado

**Parámetros:**
- `entorno_detectado` (object, requerido): Output de `identificar_entorno_devops`
- `tipo_problema` (enum, requerido): 
  - `diseño_infraestructura`
  - `migracion_arquitectonica`
  - `problema_produccion`
  - `optimizacion_pipelines`
  - `implementacion_observabilidad`
  - `mejora_seguridad`
- `nivel_complejidad` (enum, requerido): `BAJO` | `MEDIO` | `ALTO`

### 📤 Output Esperado

**Formato: Cuestionario estructurado en markdown**

**Ejemplo para tipo_problema="diseño_infraestructura" + nivel="ALTO" + cloud="AWS":**

```markdown
## 📋 Cuestionario de Contexto Operativo

Para diseñar la mejor infraestructura en AWS, necesito conocer:

### 1. Requisitos No Funcionales (Crítico)
- ¿Cuál es el RTO (Recovery Time Objective) aceptable? (ej: < 5 minutos, < 1 hora)
- ¿Cuál es el RPO (Recovery Point Objective) aceptable? (ej: 0 pérdida de datos, < 15 minutos)
- ¿Qué SLA necesitas garantizar? (ej: 99.9%, 99.99%)
- ¿Cuántos usuarios concurrentes esperas? (ej: 100, 10K, 1M)
- ¿Cuál es el throughput esperado? (ej: 100 req/s, 10K req/s)

### 2. Restricciones (Crítico)
- ¿Cuál es el presupuesto mensual disponible? (ej: $100, $1000, $10K)
- ¿Hay restricciones de compliance? (HIPAA, PCI-DSS, SOC 2, GDPR)
- ¿Hay restricciones geográficas? (regiones AWS específicas)
- ¿Cuántas personas conforman el equipo técnico?
- ¿El equipo tiene experiencia con AWS/Kubernetes/Terraform?

### 3. Estado Actual
- ¿Es un proyecto greenfield (desde cero) o brownfield (migración)?
- Si es migración, ¿cuál es la arquitectura actual?
- ¿Existen dependencias con sistemas legacy?

### 4. Preferencias Técnicas (Opcional)
- ¿Preferencia entre ECS vs EKS vs EC2 directo?
- ¿Preferencia entre RDS vs Aurora vs bases de datos auto-administradas?
- ¿Hay alguna herramienta/servicio que NO quieras usar?

### 5. Prioridades de Negocio
- ¿Qué es más importante? (ordena del 1 al 5)
  - [ ] Time-to-market (velocidad de lanzamiento)
  - [ ] Costo operativo bajo
  - [ ] Alta disponibilidad
  - [ ] Seguridad máxima
  - [ ] Escalabilidad futura

---

Por favor, responde las preguntas de las secciones **Críticas** primero. Las opcionales nos ayudarán a afinar la recomendación.
```

**Para nivel="MEDIO" el cuestionario sería más corto:**

```markdown
## 📋 Cuestionario de Contexto (Versión Rápida)

Para resolver tu problema de integración, necesito saber:

1. ¿Qué versión de Kubernetes usas? (ej: 1.28)
2. ¿El problema ocurre en qué ambiente? (dev, staging, prod)
3. ¿Hay logs de error que puedas compartir?
4. ¿Cuándo comenzó el problema? (fecha/hora)
5. ¿Qué cambios recientes se hicieron? (deploys, configs)

Responde estas 5 preguntas y podré darte una solución precisa.
```

### 🔧 Lógica Interna Sugerida

1. **Cargar plantilla de preguntas** según `tipo_problema`
2. **Filtrar preguntas** según `entorno_detectado`:
   - Si cloud=AWS → preguntar sobre regiones, VPC, IAM
   - Si cloud=Azure → preguntar sobre Resource Groups, RBAC
   - Si orquestador=K8s → preguntar sobre namespaces, ingress
3. **Ajustar cantidad de preguntas** según `nivel_complejidad`:
   - BAJO: 1-2 preguntas
   - MEDIO: 3-5 preguntas
   - ALTO: 6-10+ preguntas
4. **Priorizar preguntas** marcando "Crítico" vs "Opcional"
5. **Generar markdown** formateado para presentar al usuario

### 🎭 Comportamiento Esperado del Rol

```markdown
> "He identificado que necesitas diseñar infraestructura completa en AWS (complejidad ALTA).
> Voy a generarte un cuestionario estructurado para capturar todos los aspectos clave..."

[Ejecuta herramienta]

> [Presenta cuestionario al usuario]
```

### 🔗 Integración con Otras Herramientas

- **Usa output de:** `identificar_entorno_devops`
- **Su output alimenta a:** `generar_plan_incremental_devops`

### 📈 Criterios de Éxito

- ✅ Genera cuestionarios en < 2 segundos
- ✅ Preguntas relevantes al 95% (sin preguntas irrelevantes)
- ✅ Cubre el 100% de información crítica necesaria
- ✅ Reduce tiempo de recopilación de contexto en 50%

---

## 3. `generar_plan_incremental_devops`

### 🎯 Propósito

Estructurar automáticamente soluciones DevOps en fases incrementales priorizadas por impacto/esfuerzo, incluyendo análisis de riesgos, costos, seguridad y rollback.

### 📊 Nivel de Prioridad

**🔴 ALTA** - Es el formato estándar que TODA respuesta del Arquitecto DevOps debe seguir.

### 🔍 Problema que Resuelve

- **Antes:** El arquitecto debe estructurar manualmente cada solución en el formato de 7 secciones.
- **Después:** La herramienta genera automáticamente la estructura completa, el arquitecto solo llena el contenido.

### 📥 Input Esperado

**Parámetros:**
- `problema_identificado` (string, requerido): Descripción del problema a resolver
- `contexto_operativo` (object, requerido): Output de `recopilar_contexto_operativo`
- `opciones_tecnicas` (array, requerido): Lista de opciones técnicas con pros/contras
  ```json
  [
    {
      "nombre": "Opción A: ECS Fargate",
      "pros": ["Serverless", "Fácil scaling"],
      "contras": ["Costo mayor", "Menos control"],
      "costo_estimado": "$180-220/mes",
      "complejidad": "media"
    }
  ]
  ```
- `opcion_recomendada` (string, requerido): Nombre de la opción recomendada
- `justificacion_recomendacion` (string, requerido): Por qué es la mejor opción

### 📤 Output Esperado

**Formato: Documento markdown estructurado completo**

```markdown
## 🎯 Contexto Resumido
[Generado automáticamente desde problema_identificado + contexto_operativo]

## ⚠️ Hallazgos / Riesgos Identificados
[Lista de riesgos detectados automáticamente]

## 🔀 Opciones Disponibles
[Tabla comparativa de opciones_tecnicas con pros/contras/costos]

## 💡 Recomendación
[opcion_recomendada + justificacion_recomendacion]

## 🚀 Plan Incremental
[Fases generadas automáticamente con timeboxing]

### Fase 1: [Nombre] (Semana 1)
**Objetivo:** [Meta clara]
**Pasos:**
1. [Paso con bajo riesgo]
2. [Paso con bajo riesgo]
**Por qué:** [Justificación]

### Fase 2: [Nombre] (Semana 2-3)
...

## 🔒 Consideraciones de Seguridad (DevSecOps)
[Checklist de seguridad generado automáticamente según entorno]

## 💰 Desglose de Costos
[Tabla de costos si aplica]

## ❓ Preguntas de Validación Final
[Preguntas generadas para confirmar supuestos]
```

### 🔧 Lógica Interna Sugerida

1. **Análisis de riesgos automático:**
   - Si no hay rollback plan → agregar riesgo
   - Si no hay health checks → agregar riesgo
   - Si no hay backup strategy → agregar riesgo

2. **Generación de fases incrementales:**
   - Ordenar pasos por riesgo (menor a mayor)
   - Agrupar en fases de 1-2 semanas
   - Asignar objetivos SMART a cada fase

3. **Generación de checklist de seguridad:**
   - Según cloud provider (AWS → IAM, Security Groups, etc.)
   - Según tecnología (K8s → RBAC, Network Policies, etc.)

4. **Estimación de costos:**
   - Calcular costos de cada componente
   - Sumar total mensual
   - Sugerir optimizaciones

### 🎭 Comportamiento Esperado del Rol

```markdown
> "Perfecto, con toda esta información voy a estructurar un plan incremental completo..."

[Ejecuta herramienta]

> [Presenta plan estructurado completo]
```

### 📈 Criterios de Éxito

- ✅ Genera plan completo en < 5 segundos
- ✅ Plan sigue el 100% de la estructura estándar
- ✅ Fases son incrementales (cada una entrega valor)
- ✅ Riesgos identificados cubren 90% de casos comunes

---

## 4. `analizar_superficie_seguridad`

### 🎯 Propósito

Identificar automáticamente vectores de ataque, secretos expuestos, configuraciones inseguras y vulnerabilidades en infraestructura, pipelines y código de despliegue.

### 📊 Nivel de Prioridad

**🔴 ALTA** - El principio cardinal "Seguridad es No Negociable" requiere análisis sistemático.

### 🔍 Problema que Resuelve

- **Antes:** El arquitecto debe revisar manualmente cada archivo buscando problemas de seguridad.
- **Después:** La herramienta escanea automáticamente y genera reporte priorizado de vulnerabilidades.

### 📥 Input Esperado

**Parámetros:**
- `ruta_proyecto` (string, requerido): Path al proyecto
- `entorno_detectado` (object, opcional): Output de `identificar_entorno_devops`
- `alcance` (enum, opcional): `codigo_iac` | `pipelines_ci_cd` | `configuraciones` | `todos` (default: `todos`)

### 📤 Output Esperado

**Formato: Reporte de seguridad estructurado**

```json
{
  "analisis_completado": true,
  "timestamp": "2025-10-05T18:00:00Z",
  "score_seguridad": 65,
  "nivel_riesgo": "MEDIO",
  "hallazgos": {
    "criticos": [
      {
        "id": "SEC-001",
        "categoria": "Secretos Expuestos",
        "severidad": "CRITICA",
        "descripcion": "Credenciales hardcodeadas encontradas en terraform.tfvars",
        "archivo": "terraform.tfvars",
        "linea": 15,
        "contenido": "db_password = 'superSecret123'",
        "impacto": "Acceso no autorizado a base de datos de producción",
        "recomendacion": "Usar AWS Secrets Manager o HashiCorp Vault",
        "referencias": ["CWE-798", "OWASP-A02:2021"]
      }
    ],
    "altos": [
      {
        "id": "SEC-002",
        "categoria": "Exposición de Red",
        "severidad": "ALTA",
        "descripcion": "Security Group permite tráfico SSH (22) desde 0.0.0.0/0",
        "archivo": "infra/security_groups.tf",
        "linea": 23,
        "impacto": "Posible acceso no autorizado a instancias EC2",
        "recomendacion": "Restringir acceso SSH solo a IPs de oficina o VPN"
      }
    ],
    "medios": [...],
    "bajos": [...]
  },
  "metricas": {
    "total_archivos_analizados": 45,
    "archivos_con_problemas": 12,
    "secretos_detectados": 3,
    "configuraciones_inseguras": 8,
    "vulnerabilidades_dependencias": 5
  },
  "checklist_cumplimiento": {
    "secretos_en_vault": false,
    "ssl_tls_habilitado": true,
    "mfa_habilitado": false,
    "logs_auditoria": true,
    "network_segmentation": false,
    "least_privilege": false,
    "backup_encryption": true
  }
}
```

**Resumen markdown:**

```markdown
## 🔒 Reporte de Análisis de Seguridad

**Score Global:** 65/100 (⚠️ RIESGO MEDIO)
**Fecha:** 2025-10-05 18:00:00

---

### 🔴 Hallazgos CRÍTICOS (Acción Inmediata Requerida)

#### SEC-001: Secretos Expuestos
- **Archivo:** `terraform.tfvars:15`
- **Problema:** Credenciales hardcodeadas de base de datos
- **Impacto:** Acceso no autorizado a BD de producción
- **Recomendación:** Migrar a AWS Secrets Manager
- **Referencias:** CWE-798, OWASP-A02:2021

---

### 🟠 Hallazgos ALTOS (Priorizar en Sprint Actual)

#### SEC-002: Exposición de Red
- **Archivo:** `infra/security_groups.tf:23`
- **Problema:** SSH abierto a internet (0.0.0.0/0)
- **Impacto:** Posible acceso no autorizado a EC2
- **Recomendación:** Restringir a IPs de oficina/VPN

---

### 📊 Métricas de Análisis
- Archivos analizados: 45
- Archivos con problemas: 12 (26.7%)
- Secretos detectados: 3
- Configuraciones inseguras: 8

---

### ✅ Checklist de Cumplimiento

| Control de Seguridad | Estado |
|---------------------|--------|
| Secretos en Vault | ❌ No |
| SSL/TLS habilitado | ✅ Sí |
| MFA habilitado | ❌ No |
| Logs de auditoría | ✅ Sí |
| Segmentación de red | ❌ No |
| Least privilege | ❌ No |
| Backup encryption | ✅ Sí |

**Score:** 4/7 (57%)

---

### 🎯 Plan de Remediación Priorizado

**Fase 1 (Esta semana):**
1. Migrar secretos a AWS Secrets Manager (SEC-001)
2. Restringir Security Groups SSH (SEC-002)

**Fase 2 (Próxima semana):**
3. Implementar MFA en cuentas AWS
4. Configurar Network Policies en K8s

**Fase 3 (Mes 1):**
5. Implementar RBAC con least privilege
6. Escaneo automático de secretos en CI/CD
```

### 🔧 Lógica Interna Sugerida

1. **Escaneo de secretos:**
   - Regex para API keys, passwords, tokens
   - Integración con herramientas: gitleaks, truffleHog

2. **Análisis de configuraciones:**
   - Security Groups con 0.0.0.0/0
   - Buckets S3 públicos
   - IAM con permisos * (wildcard)
   - RDS sin encryption
   - SSL/TLS deshabilitado

3. **Escaneo de dependencias:**
   - Integración con: Snyk, Trivy, OWASP Dependency Check

4. **Priorización:**
   - CVSS score para vulnerabilidades
   - Impacto en producción
   - Facilidad de explotación

### 🎭 Comportamiento Esperado del Rol

```markdown
> "Antes de continuar, voy a realizar un análisis de superficie de seguridad en tu infraestructura..."

[Ejecuta herramienta]

> "⚠️ He detectado 1 hallazgo CRÍTICO y 2 ALTOS que debemos abordar inmediatamente.
> 
> El más crítico es que tienes credenciales de base de datos hardcodeadas en `terraform.tfvars`.
> Esto es un riesgo de seguridad severo.
> 
> Te recomiendo que antes de desplegar, migremos estos secretos a AWS Secrets Manager.
> ¿Quieres que te guíe en cómo hacerlo?"
```

### 📈 Criterios de Éxito

- ✅ Detecta 95%+ de secretos hardcodeados
- ✅ Identifica configuraciones inseguras comunes (Security Groups, IAM, etc.)
- ✅ Completa análisis en < 30 segundos
- ✅ Genera plan de remediación priorizado
- ✅ Reduce falsos positivos a < 10%

---

## 5. Mejora: `diagnosticar_devops`

### 🎯 Propósito de la Mejora

Enriquecer la herramienta existente `diagnosticar_devops` con:
1. **Integración con `identificar_entorno_devops`** (contexto automático)
2. **Sistema de niveles** (análisis básico vs profundo según complejidad)
3. **Análisis de seguridad integrado** (llamar a `analizar_superficie_seguridad`)

### 📊 Nivel de Prioridad

**🟡 MEDIA** - Mejora herramienta existente, no crea una nueva.

### 🔍 Cambios Propuestos

#### Cambio 1: Auto-detección de entorno al inicio

**Antes:**
```markdown
Usuario ejecuta: `> diagnosticar_devops`
Herramienta pregunta: "¿Qué tecnologías usas?"
```

**Después:**
```markdown
Usuario ejecuta: `> diagnosticar_devops`
Herramienta ejecuta automáticamente: `identificar_entorno_devops`
Herramienta dice: "He detectado AWS + K8s + Terraform. Procedo con el diagnóstico..."
```

#### Cambio 2: Niveles de profundidad

**Nueva opción de parámetro:**
```
> diagnosticar_devops --profundidad=basico|completo
```

- **básico (default):** Análisis rápido (5-10 min) de CI/CD, IaC, observabilidad
- **completo:** Análisis profundo (15-30 min) que incluye seguridad, cultura, métricas históricas

#### Cambio 3: Integración con análisis de seguridad

**Si profundidad=completo:**
- Llamar automáticamente a `analizar_superficie_seguridad`
- Incluir sección de "Hallazgos de Seguridad" en matriz de madurez
- Priorizar items de backlog que tengan impacto en seguridad

### 📤 Output Mejorado

**Matriz de madurez ampliada:**

```markdown
## 📊 Matriz de Madurez DevOps

| Dimensión | Nivel Actual | Nivel Objetivo | Gap | Prioridad |
|-----------|--------------|----------------|-----|-----------|
| CI/CD | 3 - Automatizado | 4 - Medido | 1 | 🔴 Alta |
| IaC | 2 - Repetible | 4 - Medido | 2 | 🔴 Alta |
| Observabilidad | 2 - Repetible | 3 - Automatizado | 1 | 🟡 Media |
| Seguridad | 1 - Inicial | 4 - Medido | 3 | 🔴 **CRÍTICA** |
| Cultura | 2 - Repetible | 3 - Automatizado | 1 | 🟢 Baja |

**Score Global:** 2.0/5.0 (40%)
```

### 📈 Criterios de Éxito de la Mejora

- ✅ Reduce tiempo de setup inicial (no hay que responder preguntas de entorno)
- ✅ Análisis básico completa en < 10 minutos
- ✅ Análisis completo incluye seguridad automáticamente
- ✅ Backlog priorizado incluye items de seguridad

---

## 📝 Notas Finales

### Priorización Recomendada para Implementación

1. **🥇 Primera iteración:**
   - `identificar_entorno_devops` (base para todas las demás)
   - Mejora a `diagnosticar_devops` (integración con identificador)

2. **🥈 Segunda iteración:**
   - `analizar_superficie_seguridad` (principio cardinal requiere esto)

3. **🥉 Tercera iteración:**
   - `generar_plan_incremental_devops` (automatiza formato estándar)
   - `recopilar_contexto_operativo` (nice-to-have)

### Impacto Estimado

| Herramienta | Ahorro de Tiempo | Mejora de Calidad | Complejidad Implementación |
|-------------|------------------|-------------------|---------------------------|
| `identificar_entorno_devops` | 🔥🔥🔥 (70%) | 🔥🔥 (30%) | 🟡 Media |
| `recopilar_contexto_operativo` | 🔥🔥 (50%) | 🔥 (20%) | 🟢 Baja |
| `generar_plan_incremental_devops` | 🔥🔥🔥 (80%) | 🔥🔥🔥 (60%) | 🔴 Alta |
| `analizar_superficie_seguridad` | 🔥🔥 (60%) | 🔥🔥🔥🔥 (90%) | 🔴 Alta |
| Mejora `diagnosticar_devops` | 🔥🔥 (40%) | 🔥🔥 (40%) | 🟡 Media |

---

## 📅 Última Actualización

**Fecha:** 5 de octubre de 2025  
**Autor:** Análisis durante refactorización de Arquitecto DevOps v2.0  
**Estado:** Propuesta de herramientas pendientes de implementación
