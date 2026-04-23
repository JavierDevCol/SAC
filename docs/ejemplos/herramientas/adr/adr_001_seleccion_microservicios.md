# ADR 001: Migración de Monolito a Arquitectura de Microservicios

**Estado:** Aceptado  
**Fecha:** 2025-03-15  
**Autores:** Equipo de Arquitectura, CTO, Tech Leads

---

## Contexto

Nuestra plataforma de e-commerce ha crecido significativamente en los últimos 18 meses desde su lanzamiento inicial como monolito modular. Actualmente enfrentamos los siguientes desafíos:

### Situación Actual

- **Usuarios concurrentes:** 8,000+ en horarios pico (16x crecimiento desde lanzamiento)
- **Tamaño del monolito:** 450,000 líneas de código, tiempo de build 25 minutos
- **Equipo:** Crecimiento de 3 a 15 desarrolladores organizados en 4 equipos
- **Deployment:** Cada deployment (1-2 por semana) requiere coordinar múltiples equipos y tiene riesgo de afectar toda la plataforma
- **Dominios de negocio:** 6 dominios (Catálogo, Carrito, Órdenes, Pagos, Marketplace, Suscripciones)

### Problemas Identificados

1. **Escalabilidad:** El módulo de Catálogo requiere 4x más recursos que otros módulos, pero escalar el monolito completo es costoso ($800/mes → $3,200/mes para 4 instancias)
2. **Velocidad de desarrollo:** Equipos bloqueados esperando merges y resolución de conflictos. Ciclo de feedback aumentó de 2 días a 7 días
3. **Deployment acoplado:** Un bug en el módulo de Marketplace retrasó release crítico de Pagos 3 días
4. **Tecnología:** Módulo de Búsqueda requiere Elasticsearch pero agregar dependencia al monolito afecta startup time de toda la app
5. **Organización:** Equipos autónomos (Catálogo, Marketplace, Subscripciones) no pueden avanzar independientemente

### Umbrales de Pivot Alcanzados

En el ADR original (ADR-000) definimos condiciones para revisar la arquitectura:

- ✅ Usuarios concurrentes > 2,000 (alcanzado: 8,000+)
- ✅ Equipo > 8 desarrolladores (alcanzado: 15)
- ✅ Dominios de negocio > 3 (alcanzado: 6)
- ✅ Deployment frecuente bloqueado por acoplamiento

---

## Decisión

**Migraremos gradualmente del monolito modular a una arquitectura de microservicios** siguiendo el patrón Strangler Fig, comenzando con los módulos de mayor beneficio/riesgo.

### Estrategia de Migración (24 meses)

#### **Fase 1: Fundaciones (Meses 1-3)**
- Implementar API Gateway (Kong o AWS API Gateway)
- Setup de Service Mesh (Istio)
- Infraestructura de observabilidad centralizada (ELK + Prometheus + Jaeger)
- CI/CD pipeline para microservicios (Jenkins + ArgoCD)
- Service template (Spring Boot + Docker + Helm charts)

#### **Fase 2: Primer Microservicio Piloto (Meses 4-6)**
- **Servicio Catálogo** (primer candidato por alta demanda de recursos)
- Extraer usando Strangler Fig: nuevo tráfico → microservicio, legacy → monolito
- Validar patrón de comunicación (REST + eventos asíncronos con Kafka)
- Aprendizajes para siguientes extracciones

#### **Fase 3: Servicios de Negocio Core (Meses 7-12)**
- **Servicio Marketplace** (equipo autónomo, deploy independiente)
- **Servicio Suscripciones** (lógica de negocio compleja, evolución rápida)
- **Servicio Búsqueda** (requiere stack especializado: Elasticsearch)

#### **Fase 4: Servicios Transaccionales (Meses 13-18)**
- **Servicio Órdenes** (orquestación con Saga Pattern)
- **Servicio Pagos** (alta criticidad, requiere aislamiento)
- **Servicio Carrito** (sesiones, alta escritura)

#### **Fase 5: Consolidación (Meses 19-24)**
- Deprecación gradual del monolito legacy
- Migración de datos históricos si es necesario
- Optimización de costos y performance
- Runbooks y documentación completa

### Principios de Diseño

1. **Domain-Driven Design:** Cada microservicio representa un bounded context
2. **Base de datos por servicio:** Cada servicio tiene su propia BD (excepto datos compartidos read-only)
3. **Comunicación asíncrona preferida:** Eventos via Kafka para desacoplamiento
4. **API REST para lectura:** Queries síncronos cuando sea necesario
5. **Saga Pattern:** Para transacciones distribuidas (ej: checkout)
6. **Backward compatibility:** Versioning de APIs para evitar breaking changes

---

## Consecuencias

### Positivas ✅

**Corto Plazo (6 meses):**
- ✅ Escalabilidad independiente del módulo Catálogo reduce costos 40% ($3,200 → $1,900/mes)
- ✅ Equipos de Marketplace y Suscripciones pueden deployar independientemente (2-3x por semana)
- ✅ Tiempo de build del monolito reducido 30% (de 25 min a 17 min)

**Medio Plazo (12 meses):**
- ✅ Velocidad de desarrollo aumentada: ciclo de feedback 7 días → 2-3 días
- ✅ Reducción de incidentes críticos por deployment acoplado (-70%)
- ✅ Stack tecnológico especializado por servicio (Elasticsearch en Búsqueda, Redis en Carrito)

**Largo Plazo (24 meses):**
- ✅ Escalabilidad horizontal ilimitada por servicio
- ✅ Autonomía completa de equipos (Conway's Law aplicado correctamente)
- ✅ Resiliencia mejorada (fault isolation)
- ✅ Time-to-market reducido para nuevas features

### Negativas / Trade-offs ⚠️

**Complejidad Operativa:**
- ⚠️ Incremento de 1 deployment → 10+ deployments coordinados
- ⚠️ Debugging distribuido más complejo (requiere tracing correlacionado)
- ⚠️ Necesidad de contratar 2 SRE/DevOps dedicados ($180K/año adicional)

**Costos de Infraestructura:**
- ⚠️ Costo inicial de infraestructura aumenta 50% por overhead de networking, service mesh, observabilidad
- ⚠️ Proyección: $1,900/mes actual → $2,800/mes con 6 microservicios (aún menor que 4x instancias monolito)

**Transacciones Distribuidas:**
- ⚠️ Eventual consistency introduce complejidad en flujos transaccionales (checkout)
- ⚠️ Requiere Saga Pattern (orquestación o coreografía)
- ⚠️ Debugging de fallos distribuidos más difícil

**Migración Gradual:**
- ⚠️ Período de transición con dual-write/read (18-24 meses)
- ⚠️ Mantenimiento paralelo de monolito y microservicios

**Data Consistency:**
- ⚠️ Queries cross-service requieren API composition o CQRS views
- ⚠️ Reportes que cruzan múltiples servicios son más complejos

### Riesgos Mitigados

| Riesgo | Probabilidad | Mitigación |
|--------|--------------|------------|
| Fallo en primer microservicio paraliza migración | 🟡 MEDIA | Piloto con Catálogo (no transaccional, fácil rollback) |
| Overhead operativo paraliza equipo | 🟡 MEDIA | Contratar 2 SRE dedicados antes de Fase 1 |
| Data inconsistency en flujos críticos | 🔴 ALTA | Saga Pattern + tests exhaustivos + feature flags |
| Costos se disparan fuera de control | 🟡 MEDIA | Monitoring de costos por servicio + rightsizing mensual |
| Debugging imposible en producción | 🟡 MEDIA | Distributed tracing (Jaeger) + logging estructurado + APM |

---

## Opciones Consideradas

### Opción 1: Mantener Monolito Modular (Descartada) ❌

**Pros:**
- Sin complejidad adicional
- Sin costos de migración
- Equipo ya familiarizado

**Contras:**
- Escalabilidad sigue siendo problema crítico (costos crecientes)
- Velocidad de desarrollo continuará degradándose
- Equipos bloqueados (no resuelve problema organizacional)
- **Razón de descarte:** No resuelve problemas críticos actuales

### Opción 2: "Big Bang" - Reescribir todo a Microservicios (Descartada) ❌

**Pros:**
- Arquitectura final limpia desde día 1
- Sin dual-write/read

**Contras:**
- Riesgo extremadamente alto (6-9 meses sin features nuevas)
- "Second System Syndrome"
- No genera valor de negocio durante migración
- **Razón de descarte:** Riesgo inaceptable, viola principio de entrega continua

### Opción 3: Migración Gradual con Strangler Fig (Seleccionada) ✅

**Pros:**
- Riesgo controlado (microservicio por microservicio)
- Valor de negocio continuo
- Aprendizajes aplicados a siguientes migraciones
- Rollback fácil por fase

**Contras:**
- Período de transición largo (24 meses)
- Complejidad temporal de mantener dos sistemas

**Razón de selección:** Balance óptimo entre riesgo y beneficio

---

## Validación

### Métricas de Éxito

| Métrica | Baseline | Objetivo 6m | Objetivo 12m | Objetivo 24m |
|---------|----------|-------------|--------------|--------------|
| **Deployment Frequency** | 1-2/semana | 3-5/semana | 10+/semana | 20+/semana |
| **Lead Time for Changes** | 7 días | 4 días | 2 días | 1 día |
| **MTTR (Mean Time to Recovery)** | 4 horas | 2 horas | 1 hora | 30 min |
| **Change Failure Rate** | 15% | 10% | 5% | 3% |
| **Costo Infraestructura** | $1,900/mes | $2,200/mes | $2,500/mes | $2,800/mes |
| **P95 Latency** | 800ms | 600ms | 400ms | 300ms |
| **Uptime** | 99.5% | 99.7% | 99.9% | 99.95% |

### Condiciones de Re-evaluación

**Pausar migración si:**
- Change Failure Rate > 25% durante 2 meses consecutivos
- Costos superan $4,000/mes sin justificación de valor
- MTTR aumenta > 6 horas sostenido
- 3+ incidentes críticos relacionados con arquitectura distribuida en 1 mes

**Acelerar migración si:**
- Éxito del piloto (Catálogo) supera expectativas en 50%+
- Equipos solicitan independencia antes de lo planificado
- Problemas de escalabilidad se intensifican

---

## Referencias

- **ADR Supersedido:** ADR-000: Selección de Monolito Modular Inicial
- **Análisis de Viabilidad:** `docs/analisis-migracion-microservicios-2025-02.pdf`
- **Spike Técnico:** `docs/poc-strangler-fig-catalog-service.md`
- **Benchmarks de Costos:** `docs/cost-analysis-microservices-vs-monolith.xlsx`
- **Referencias Externas:**
  - [Strangler Fig Pattern - Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html)
  - [Building Microservices - Sam Newman](https://samnewman.io/books/building_microservices_2nd_edition/)
  - [Saga Pattern](https://microservices.io/patterns/data/saga.html)

---

## Aprobaciones

| Rol | Nombre | Fecha | Firma |
|-----|--------|-------|-------|
| CTO | [Nombre] | 2025-03-15 | ✅ Aprobado |
| VP Engineering | [Nombre] | 2025-03-15 | ✅ Aprobado |
| Tech Lead (Catálogo) | [Nombre] | 2025-03-14 | ✅ Aprobado |
| Tech Lead (Marketplace) | [Nombre] | 2025-03-14 | ✅ Aprobado |
| Head of SRE | [Nombre] | 2025-03-15 | ✅ Aprobado con observaciones* |

**Observaciones SRE:** Requiere contratar 2 SRE adicionales antes de Fase 1 para garantizar soporte operativo.

---

## Historial de Cambios

| Fecha | Versión | Cambios | Autor |
|-------|---------|---------|-------|
| 2025-03-15 | 1.0 | Creación inicial | Equipo de Arquitectura |
| 2025-03-20 | 1.1 | Agregadas observaciones de SRE sobre contratación | Head of SRE |
