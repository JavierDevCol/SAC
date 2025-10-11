# 🛠️ Herramienta: Diagnosticar DevOps

> **Versión:** 2.0  
> **Fecha de Actualización:** 10 de octubre de 2025  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `diagnosticar_devops`

---

## 🎯 Objetivo

Realizar un diagnóstico integral y estructurado de pipelines CI/CD, infraestructura cloud y prácticas DevSecOps para identificar gaps críticos, evaluar madurez organizacional y generar un plan priorizado de mejoras que optimice la entrega de software, seguridad y eficiencia operacional.

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Descripción del entorno actual (proveedor cloud, orquestador, arquitectura general)
- Archivos de configuración de infraestructura (Dockerfile, docker-compose.yml, kubernetes manifests)
- Definiciones de pipelines CI/CD (GitHub Actions, GitLab CI, Jenkins, Azure DevOps)
- Configuración de Infrastructure as Code (Terraform, ARM templates, CloudFormation, Helm charts)

**Secundario (Opcional):**
- Requisitos no funcionales y SLOs (RTO, RPO, disponibilidad, performance targets)
- Restricciones de presupuesto y costos operacionales
- Políticas de seguridad y compliance requeridos (GDPR, SOC2, ISO27001)
- Métricas actuales de observabilidad (logs, métricas, trazas)
- Inventario de herramientas DevOps existentes y licencias
- Contexto del equipo (tamaño, experiencia, estructura organizacional)

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `profundidad_analisis` | string | rapido\|completo\|exhaustivo | completo | Nivel de detalle del diagnóstico y recomendaciones |
| `foco_principal` | string | seguridad\|rendimiento\|costo\|escalabilidad\|equilibrado | equilibrado | Área de énfasis para priorizar recomendaciones |
| `incluir_costos` | boolean | true\|false | true | Analizar optimización de costos y ROI de mejoras |
| `generar_roadmap` | boolean | true\|false | true | Crear plan de implementación incremental por fases |
| `nivel_madurez_actual` | string | auto\|adhoc\|repetible\|gestionado\|optimizado | auto | Forzar nivel de madurez o detectar automáticamente |
| `incluir_compliance` | boolean | true\|false | false | Evaluar cumplimiento de estándares de seguridad y regulaciones |
| `formato_salida` | string | markdown\|json\|pdf | markdown | Formato del reporte de diagnóstico |

---

## 👥 Roles Autorizados

- ✅ **Arquitecto DevOps** (uso principal - especialista en infraestructura y pipelines)
- ✅ **ArchDev Pro** (integración con flujos de desarrollo y decisiones arquitectónicas)
- ✅ **Arquitecto Onad** *(para decisiones estratégicas y transformación organizacional)*

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Configuración Inicial y Análisis de Contexto

- **Selección de modo de operación:**
  - **Presentar opciones al usuario:**
    - **Modo Automático**: Ejecutar diagnóstico con parámetros por defecto (análisis completo y equilibrado)
    - **Modo Personalizado**: Configurar parámetros específicos según necesidades del proyecto
  
- **Si elige Modo Personalizado, mostrar configuración disponible:**
  ```
  🔧 Configuración del Diagnóstico DevOps:
  
  📊 Profundidad del análisis:
  • completo (análisis estándar - 2h) ← por defecto
  • rapido (overview - 30min), exhaustivo (análisis profundo - medio día)
  
  🎯 Foco principal:
  • equilibrado (todas las áreas por igual) ← por defecto
  • seguridad, rendimiento, costo, escalabilidad
  
  💰 Incluir análisis de costos: true ← por defecto
  🗺️ Generar roadmap de implementación: true ← por defecto
  📋 Incluir evaluación de compliance: false ← por defecto
  📄 Formato de salida: markdown ← por defecto
  ```

- **Análisis automático del contexto del proyecto:**
  - **Verificar si existe `artefactos/contexto_proyecto.md` en la raíz del proyecto**
  - **Si existe, extraer información relevante para DevOps:**
    - **Stack Tecnológico:** Framework principal, base de datos, servicios cloud utilizados
    - **Gestión y Comandos:** Sistema de build, scripts de deployment existentes
    - **Arquitectura detectada:** Monolito, microservicios, patrones arquitectónicos
    - **Dependencias externas:** APIs consumidas, servicios de terceros, integraciones
    - **Componentes clave:** Servicios principales, puntos de entrada, módulos críticos
  
  - **Con el contexto obtenido, enfocar el diagnóstico:**
    - Adaptar preguntas específicas al stack detectado (ej: Kubernetes si es microservicios)
    - Priorizar áreas según la arquitectura (ej: service mesh para microservicios distribuidos)
    - Identificar gaps específicos del stack (ej: falta Redis para cache si usa Spring Boot)

- **Si no existe contexto_proyecto.md, solicitar información básica:**
  - **Tipo de aplicación:** "¿Es una aplicación monolítica, microservicios, o serverless?"
  - **Stack principal:** "¿Qué tecnologías principales usa? (Java/Spring, Node.js, Python, .NET)"
  - **Proveedor cloud:** "¿Usan algún proveedor cloud? (AWS, Azure, GCP, on-premise, híbrido)"
  - **Nivel de containerización:** "¿Usan Docker, Kubernetes, o deployment tradicional?"

- **Inventariar recursos de infraestructura disponibles:**
  - Analizar archivos de configuración proporcionados (Dockerfile, K8s manifests, Terraform)
  - Identificar proveedores cloud y servicios utilizados detectados en el contexto
  - Mapear arquitectura de deployment basada en información del proyecto
  - Catalogar herramientas DevOps mencionadas en dependencias o configuraciones

- **Evaluar pipelines CI/CD existentes:**
  - Buscar archivos de workflow (.github/workflows, .gitlab-ci.yml, Jenkinsfile)
  - Revisar scripts de build mencionados en el contexto del proyecto
  - Identificar etapas implementadas vs ausentes
  - Detectar puntos de fricción específicos del stack tecnológico

### 2️⃣ Evaluación de Madurez DevOps

- **Clasificar nivel de madurez según dimensiones:**
  - **Ad-hoc (Nivel 1):** Procesos manuales, deployments esporádicos, sin automation
  - **Repetible (Nivel 2):** Scripts básicos, CI implementado, deployments semi-automáticos  
  - **Gestionado (Nivel 3):** Pipelines completos, IaC básico, monitoring implementado
  - **Optimizado (Nivel 4):** Full automation, self-healing, continuous optimization

- **Evaluar capacidades por área contextualizada:**
  - **Automatización:** Específica al stack detectado (Maven/Gradle vs npm vs pip)
  - **Observabilidad:** Apropiada para la arquitectura (APM para microservicios, logs para monolitos)
  - **Seguridad:** Relevante al ecosistema (OWASP para web, container security para K8s)
  - **Colaboración:** Alineada con el tamaño y estructura del equipo detectado

### 3️⃣ Análisis de Seguridad (DevSecOps)

- **Auditar controles de seguridad implementados:**
  - **Shift-left security:** SAST específico al lenguaje detectado, pre-commit hooks relevantes
  - **Pipeline security:** Dependency scanning apropiado (npm audit, OWASP, Snyk según stack)
  - **Infrastructure security:** Network policies, RBAC, encryption basado en la arquitectura
  - **Compliance:** Evaluar solo si `incluir_compliance=true` en configuración

- **Identificar vulnerabilidades específicas del contexto:**
  - Secretos hardcodeados en configuraciones del stack detectado
  - Vulnerabilidades específicas del framework principal (Spring Security, Express.js security)
  - Gaps de seguridad según la arquitectura (service-to-service auth en microservicios)
  - Configuraciones inseguras por defecto del stack tecnológico

### 4️⃣ Evaluación de Infraestructura y Escalabilidad

- **Analizar arquitectura contextualizada:**
  - **Infrastructure as Code:** Específico al proveedor cloud detectado o sugerido
  - **Container orchestration:** Apropiado para la escala y complejidad del proyecto
  - **Networking:** Basado en la arquitectura (load balancers para microservicios, CDN para frontends)
  - **Data persistence:** Consistente con las bases de datos detectadas en el contexto

- **Revisar capacidades de escalabilidad según arquitectura:**
  - Estrategias específicas al tipo de aplicación detectada
  - Patrones de escalabilidad apropiados (horizontal para stateless, vertical para databases)
  - Performance testing integrado y específico al stack
  - Resource optimization basada en las características del workload

### 5️⃣ Análisis de Costos y Eficiencia

- **Evaluar optimización contextualizada (solo si `incluir_costos=true`):**
  - Right-sizing específico al tipo de workload detectado
  - Estrategias de ahorro apropiadas para el stack (serverless vs containers vs VMs)
  - Optimizaciones específicas del proveedor cloud identificado
  - Identificación de anti-patrones costosos del stack tecnológico

- **Calcular TCO adaptado al contexto:**
  - Costos específicos del stack tecnológico detectado
  - Licensing costs relevantes (Oracle, Microsoft, enterprise tools)
  - Operational overhead específico de la arquitectura
  - ROI estimado basado en el tamaño y complejidad real del proyecto

### 6️⃣ Generación de Recomendaciones Priorizadas

- **Clasificar mejoras contextualizadas por impacto y esfuerzo:**
  - **Quick wins específicos:** Basados en gaps detectados del stack (ej: enable JaCoCo para Java)
  - **Proyectos estratégicos:** Alineados con la arquitectura objetivo detectada
  - **Mejoras incrementales:** Específicas al nivel de madurez y contexto actual
  - **Investigación contextual:** Tecnologías emergentes relevantes al stack

- **Crear matriz de priorización adaptada:**
  - Criticidad específica al dominio y compliance requirements detectados
  - Impacto en developer experience del stack tecnológico específico
  - ROI calculation basado en métricas reales del contexto del proyecto
  - Alineación con el roadmap arquitectónico inferido del contexto

### 7️⃣ Elaboración de Roadmap de Implementación

- **Definir fases contextualizadas (solo si `generar_roadmap=true`):**
  - **Fase 0 - Estabilizar:** Gaps críticos específicos del stack y arquitectura detectados
  - **Fase 1 - Visibilidad:** Observability stack apropiado para la arquitectura
  - **Fase 2 - Automatización:** CI/CD optimizado para el ecosistema tecnológico específico
  - **Fase 3 - Optimización:** Advanced practices relevantes al contexto organizacional

- **Generar plan de acción específico:**
  - Tasks técnicas específicas al stack y herramientas detectadas
  - Métricas de éxito apropiadas para el tipo de aplicación y arquitectura
  - Risk mitigation basado en los riesgos específicos del contexto
  - Budget estimates realistas basados en el tamaño y complejidad detectados

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Archivo `contexto_proyecto.md` corrupto o incompleto | Advertir al usuario sobre datos faltantes y solicitar información manual específica para completar el diagnóstico |
| No hay archivos de configuración DevOps disponibles | Generar diagnóstico básico enfocado en gaps fundamentales y sugerir implementación desde cero |
| Stack tecnológico no reconocido o muy específico | Aplicar mejores prácticas genéricas de DevOps y solicitar al usuario contexto adicional del ecosistema |
| Múltiples proveedores cloud detectados (multi-cloud) | Analizar cada proveedor por separado y generar recomendaciones de consolidación o estrategia multi-cloud |
| Configuraciones de seguridad altamente restrictivas | Informar limitaciones del análisis y enfocar en mejoras compatibles con políticas existentes |
| Proyecto legacy sin containerización | Evaluar feasibilidad de modernización vs optimización in-place y generar roadmap apropiado |
| Infraestructura completamente on-premise | Adaptar recomendaciones a entornos on-premise y evaluar oportunidades de cloud híbrido |
| Equipo muy pequeño o recursos limitados | Priorizar quick wins y soluciones de bajo mantenimiento, evitar over-engineering |
| Compliance requirements extremos (sector financiero/salud) | Enfocar en security-first approach y incluir consideraciones regulatorias específicas |
| Arquitectura monolítica con alta complejidad | Evaluar estrategias de strangler pattern vs big bang migration para modernización |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Diagnóstico estructurado en formato Markdown con evaluación de madurez, hallazgos críticos y roadmap priorizado
- Matriz de recomendaciones con impacto, esfuerzo y ROI estimado

**Estructura del output:**
```
# 🔍 Diagnóstico DevOps: [Nombre del Proyecto]

## 📊 Resumen Ejecutivo
- **Nivel de madurez actual:** Gestionado (Nivel 3/4)
- **Score general:** 7.2/10
- **Gaps críticos:** 3 identificados
- **ROI estimado de mejoras:** $45K anuales
- **Tiempo de implementación:** 8-12 meses

## 🎯 Estado Actual (Matriz de Madurez)
| Área | Nivel Actual | Nivel Objetivo | Gap | Prioridad |
|------|--------------|----------------|-----|-----------|
| CI/CD Pipeline | 3 - Gestionado | 4 - Optimizado | 🟡 Medio | Alta |
| Seguridad | 2 - Repetible | 4 - Optimizado | 🔴 Alto | Crítica |
| Infraestructura | 3 - Gestionado | 3 - Gestionado | ✅ None | Media |
| Observabilidad | 2 - Repetible | 3 - Gestionado | 🟠 Alto | Alta |

## 🚨 Hallazgos Críticos
1. **Ausencia de security scanning** - Sin SAST/DAST en pipeline
2. **Monitoring limitado** - Solo logs básicos, sin métricas APM
3. **IaC parcial** - 60% infraestructura aún manual

## 💡 Recomendaciones Priorizadas
### Quick Wins (0-1 mes)
- Implementar SonarQube en pipeline CI/CD
- Configurar alertas básicas de Prometheus
- Automatizar backup de base de datos

### Proyectos Estratégicos (3-6 meses)
- Migración completa a Infrastructure as Code
- Implementación de service mesh (Istio)
- Setup de observabilidad distribuida (Jaeger + Grafana)

## 🗺️ Roadmap de Implementación
### Fase 1: Estabilización (Meses 1-3)
- **Objetivo:** Resolver gaps críticos de seguridad
- **Entregables:** SAST/DAST, secret scanning, vulnerability management
- **Inversión:** $15K, 2 FTE

### Fase 2: Visibilidad (Meses 4-6)
- **Objetivo:** Observabilidad completa del sistema
- **Entregables:** APM, distributed tracing, centralized logging
- **Inversión:** $25K, 1.5 FTE

## 💰 Análisis de ROI
- **Inversión total:** $65K en herramientas + $120K en tiempo de equipo
- **Ahorros anuales:** $45K (reducción downtime + eficiencia operacional)
- **Payback period:** 14 meses
- **Beneficios intangibles:** Faster time-to-market, mejor developer experience
```

**Formatos alternativos disponibles:**
- **JSON:** Para integración con herramientas de automation y dashboards
- **PDF:** Para presentaciones ejecutivas y documentación formal
- **Checklist interactivo:** Para tracking de implementación paso a paso

**Artefactos complementarios generados:**
- Lista de herramientas recomendadas con comparativas y pricing
- Scripts de automatización para quick wins identificados
- Templates de configuración específicos del stack detectado
- Métricas baseline y KPIs sugeridos para medir progreso

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/diagnosticar_devops_ejemplo.md`

---

## 📚 Referencias y Notas

### Frameworks y Metodologías de Referencia

**Modelos de Madurez DevOps:**
- **DORA State of DevOps Report:** Métricas estándar (deployment frequency, lead time, MTTR, change failure rate)
- **DevOps Maturity Model (Scaled Agile):** Framework de 5 niveles para evaluación organizacional
- **CALMS Framework:** Culture, Automation, Lean, Measurement, Sharing

**Seguridad y Compliance:**
- **NIST Cybersecurity Framework:** Guidelines para gestión de riesgos de seguridad
- **OWASP DevSecOps Guideline:** Integración de seguridad en pipelines DevOps
- **CIS Controls:** 20 controles críticos de seguridad para organizaciones

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `define_arquitectura` - Para evolución arquitectónica basada en gaps identificados
- `tomar_contexto` - Proporciona el archivo `contexto_proyecto.md` base para el análisis
- `generar_adr` - Documenta decisiones arquitectónicas derivadas del diagnóstico
- `refactorizar` - Implementa mejoras de código identificadas en el análisis

**Herramientas de diagnóstico externas:**
- **AWS Well-Architected Tool:** Assessment específico para arquitecturas AWS
- **Azure Advisor:** Recomendaciones de optimización para Azure
- **GCP Recommender:** Insights de performance y costos para Google Cloud
- **Chaos Engineering Tools:** Gremlin, Chaos Monkey para testing de resiliencia

### Proveedores Cloud y Servicios Evaluados

**Amazon Web Services (AWS):**
- CodePipeline, CodeBuild, CodeDeploy para CI/CD
- EKS, Fargate para container orchestration
- CloudWatch, X-Ray para observabilidad
- Security Hub, GuardDuty para seguridad

**Microsoft Azure:**
- Azure DevOps, GitHub Actions para CI/CD
- AKS, Container Instances para containers
- Application Insights, Monitor para observabilidad
- Security Center, Sentinel para seguridad

**Google Cloud Platform (GCP):**
- Cloud Build, Cloud Deploy para CI/CD
- GKE, Cloud Run para containers
- Operations Suite (Stackdriver) para observabilidad
- Security Command Center para seguridad

### Limitaciones Conocidas

- **Acceso limitado:** Diagnóstico basado en información proporcionada, no acceso directo a sistemas
- **Contexto organizacional:** No evalúa aspectos culturales o resistencia al cambio
- **Costos dinámicos:** Estimaciones basadas en pricing público, no considera descuentos enterprise
- **Tecnologías emergentes:** Limitado a stack mainstream, puede no cubrir tecnologías muy nuevas
- **Multi-región:** Análisis enfocado en single-region, limitaciones para architecturas globales

### Consideraciones de Implementación

**Factores de éxito críticos:**
- **Executive sponsorship:** Soporte de liderazgo para inversión y cambio organizacional
- **Team skills:** Capacidad técnica del equipo para implementar recomendaciones
- **Change management:** Estrategia para adoption de nuevas herramientas y procesos
- **Incremental approach:** Implementación por fases vs big bang transformation

**Riesgos comunes de implementación:**
- **Over-engineering:** Implementar soluciones demasiado complejas para el contexto actual
- **Tool sprawl:** Adoptar demasiadas herramientas sin integración apropiada
- **Skills gap:** Subestimar la curva de aprendizaje de nuevas tecnologías
- **Budget creep:** Costos que exceden estimaciones iniciales

### Métricas de Evaluación Recomendadas

**Technical Metrics (DORA):**
- **Deployment Frequency:** Frecuencia de deployments a producción
- **Lead Time for Changes:** Tiempo desde commit hasta producción
- **Change Failure Rate:** Porcentaje de deployments que causan issues
- **Time to Restore Service:** Tiempo promedio para recuperarse de incidentes

**Business Metrics:**
- **System Availability:** Uptime y SLA compliance
- **Cost Efficiency:** Cost per transaction, infrastructure cost trends
- **Developer Productivity:** Cycle time, code review time, feature delivery rate
- **Security Posture:** Vulnerability detection time, patch deployment rate

### Futuras Mejoras de la Herramienta

- **AI-driven analysis:** Machine learning para pattern recognition en configuraciones
- **Real-time monitoring integration:** Conexión directa con herramientas de observabilidad
- **Cost optimization engine:** Análisis continuo de costos con recomendaciones automáticas
- **Compliance automation:** Verificación automática de frameworks regulatorios
- **Multi-cloud optimization:** Strategies para arquitecturas multi-cloud complejas

### Casos de Uso por Industria

**Startups/Scale-ups:**
- Enfoque en cost optimization y developer velocity
- Priorización de automation sobre governance complejo
- Quick wins para maximizar ROI temprano

**Enterprise/Fortune 500:**
- Compliance y security como prioridades principales  
- Governance frameworks y audit trails
- Multi-team coordination y standardización

**Regulated Industries (Finance/Healthcare):**
- Security-first approach con compliance frameworks
- Audit logging y immutable infrastructure
- Zero-trust architecture y data encryption

### Recursos de Aprendizaje Recomendados

**Certificaciones relevantes:**
- **AWS:** Solutions Architect, DevOps Engineer Professional
- **Azure:** DevOps Engineer Expert, Solutions Architect Expert
- **Kubernetes:** CKA (Certified Kubernetes Administrator), CKAD
- **Security:** CISSP, CEH, Security+ para DevSecOps

**Libros de referencia:**
- "The Phoenix Project" - Gene Kim (DevOps fundamentals)
- "Site Reliability Engineering" - Google (SRE practices)
- "Building Secure & Reliable Systems" - Google (Security + Reliability)
- "Accelerate" - Forsgren, Humble, Kim (DevOps research)