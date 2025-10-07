# 🛒 Ejemplo Completo: Definición de Arquitectura para E-Commerce MVP

> **Herramienta utilizada:** `define_arquitectura`  
> **Fecha:** 7 de octubre de 2025  
> **Caso de uso:** Startup de e-commerce para tienda de ropa con MVP en 3 meses

---

## 📋 Contexto Inicial del Proyecto

### Solicitud del Usuario

```
Estoy iniciando un proyecto de e-commerce para una tienda de ropa que actualmente vende solo físicamente. Queremos validar el canal online con un MVP.

**Requisitos Funcionales Iniciales:**
- Catálogo de productos (300 productos iniciales)
- Carrito de compras
- Checkout con integración a pasarela de pagos (Stripe)
- Gestión básica de órdenes
- Panel administrativo simple

**Requisitos No Funcionales:**
- Esperamos ~500 usuarios concurrentes en picos (fin de semana)
- Uptime deseable: 99% (no crítico para MVP)
- Tiempo de respuesta: < 2 segundos está bien inicialmente

**Equipo:**
- 2 desarrolladores backend (1 mid-level Java, 1 junior)
- 1 desarrollador frontend (React)
- Sin DevOps dedicado

**Restricciones:**
- Presupuesto limitado: ~$300/mes para infraestructura
- Time-to-market crítico: MVP en 2.5 meses
- Crecimiento futuro incierto (depende de validación del canal)
```

---

## 🔄 Proceso de Análisis

### **Paso 1: Clarificación de Requisitos**

**Preguntas realizadas por la herramienta:**

#### Requisitos Funcionales
> ¿Cuántos dominios de negocio diferentes abarcará el sistema inicialmente?

**Respuesta:**
- 3 dominios principales: Catálogo, Carrito/Checkout, Gestión de Órdenes
- Todos están claramente separados
- No se espera crecimiento de dominios en los primeros 6 meses

#### Requisitos No Funcionales
> ¿Cuáles son los requisitos no funcionales más críticos?

**Respuesta:**
- **Alta disponibilidad:** 99% es suficiente (no 99.9%)
- **Latencia:** < 2 segundos es aceptable para MVP
- **Escalabilidad:** 500 usuarios concurrentes, máx. 1,000 en Black Friday
- **Seguridad:** PCI-DSS compliance delegado a Stripe
- **Observabilidad:** Logs básicos suficientes inicialmente

#### Equipo y Organización
> ¿Cuál es la experiencia del equipo con arquitecturas distribuidas?

**Respuesta:**
- 1 dev mid-level: Experiencia con Spring Boot monolítico, sin microservicios
- 1 dev junior: Sin experiencia profesional previa
- Frontend dev: Experiencia con React, consume APIs REST
- Sin experiencia en Kubernetes, Docker básico

#### Restricciones de Negocio
> ¿Cuál es el presupuesto y presión de time-to-market?

**Respuesta:**
- Presupuesto infraestructura: $300/mes máximo
- Time-to-market: 2.5 meses CRÍTICO (lanzamiento antes de temporada alta)
- Inversión inicial limitada, depende de validación para recaudar más fondos

#### Evolución y Escalado
> ¿Existe previsión de escalado por dominios?

**Respuesta:**
- Si el MVP es exitoso (> 5,000 usuarios sostenidos), se planea:
  - Marketplace (vendedores externos)
  - Suscripciones/membresías
  - App móvil nativa
- Horizonte: 12-18 meses después del lanzamiento

---

### **Paso 2: Análisis de Opciones Arquitectónicas**

#### Opciones Seleccionadas para Evaluación

1. **Monolito Modular** con Arquitectura Hexagonal
2. **Microservicios Básico** (3 servicios: Catálogo, Carrito, Órdenes)
3. **Serverless** (AWS Lambda + API Gateway)

#### Opciones Descartadas

❌ **Arquitectura Orientada a Eventos (EDA):**
- **Razón:** Complejidad innecesaria para MVP
- **Justificación:** No hay integraciones complejas que requieran desacoplamiento temporal

❌ **CQRS:**
- **Razón:** Over-engineering para volumen esperado
- **Justificación:** Separación lectura/escritura no aporta beneficio con 500 usuarios concurrentes

---

### **Paso 3: Comparación Detallada de Opciones**

#### Tabla Comparativa Consolidada

| Criterio | Monolito Modular | Microservicios | Serverless |
|----------|------------------|----------------|------------|
| **Complejidad Inicial** | 🟢 Baja | 🔴 Alta | 🟡 Media |
| **Complejidad Operativa** | 🟢 Baja | 🔴 Alta | 🟡 Media |
| **Velocidad Desarrollo Inicial** | 🟢 8-10 sem | 🔴 14-16 sem | 🟡 10-12 sem |
| **Escalabilidad Horizontal** | 🟡 Media | 🟢 Alta | 🟢 Alta |
| **Coste Mensual (inicial)** | 🟢 $100-150 | 🔴 $400-600 | 🟢 $50-100 |
| **Adecuación Equipo** | 🟢 Excelente | 🔴 Inadecuado | 🟡 Aceptable |
| **Observabilidad/Debugging** | 🟢 Simple | 🔴 Complejo | 🟡 Medio |
| **Vendor Lock-in** | 🟢 Ninguno | 🟢 Ninguno | 🔴 Alto (AWS) |
| **Tiempo Hasta Producción** | 🟢 2-3 meses | 🔴 4-5 meses | 🟡 3-4 meses |

---

#### Detalle por Opción

##### **Opción A: Monolito Modular con Arquitectura Hexagonal**

**✅ Ventajas:**
- Complejidad inicial y operativa muy baja
- Velocidad de desarrollo alta (sin overhead de comunicación entre servicios)
- Debugging y testing simplificados (todo en un proceso)
- Coste de infraestructura mínimo ($100-150/mes)
- Ideal para equipo pequeño (2-4 desarrolladores)
- Transacciones ACID simples (sin distributed transactions)
- Sin vendor lock-in

**❌ Desventajas:**
- Escalabilidad horizontal limitada (escala todo o nada)
- Acoplamiento de deployment (un bug en un módulo puede afectar todo)
- Riesgo de degradación a "Big Ball of Mud" sin disciplina arquitectónica
- Tiempo de build y startup puede crecer con el tamaño

**🎯 Cuándo Elegir:**
- MVP o validación de producto ✅
- Equipo pequeño sin experiencia en sistemas distribuidos ✅
- Requisitos de escalabilidad moderados (miles de usuarios, no millones) ✅
- Presión alta de time-to-market ✅

**⚙️ Requisitos de Equipo:**
- 2-4 desarrolladores backend
- Nivel: Junior-Mid ✅
- DevOps básico (deployment de un artefacto) ✅

**⚠️ Riesgos:**
- Sin límites de módulo claros, puede convertirse en monolito acoplado
- **Mitigación:** Aplicar Arquitectura Hexagonal desde el inicio, ArchUnit tests

**🛠️ Stack Sugerido:**
- Spring Boot 3.x (modular con subproyectos Gradle)
- PostgreSQL
- Docker + AWS Elastic Beanstalk (o equivalente)
- Redis (caché opcional)

---

##### **Opción B: Microservicios Básico**

**✅ Ventajas:**
- Escalabilidad independiente por servicio
- Aislamiento de fallos (un servicio caído no tumba todo)
- Equipos autónomos (cada equipo puede trabajar en un servicio)
- Deployment independiente

**❌ Desventajas:**
- Complejidad operativa alta (múltiples deployments, networking, service mesh)
- Observabilidad compleja (tracing distribuido, correlación de logs)
- Debugging difícil (problemas pueden cruzar múltiples servicios)
- Latencia de red entre servicios
- Distributed transactions complejas (eventual consistency, sagas)
- Coste de infraestructura alto ($400-600/mes inicial)
- Requiere experiencia que el equipo NO tiene ❌

**🎯 Cuándo Elegir:**
- Equipo grande (8+ desarrolladores) con experiencia
- Requisitos de escalabilidad muy alta
- Deployment frecuente e independiente por módulo

**⚙️ Requisitos de Equipo:**
- 8+ desarrolladores backend
- 2+ DevOps/SRE dedicados ❌
- Nivel: Senior (experiencia con Kubernetes, observabilidad) ❌

**⚠️ Riesgos:**
- Sobrecarga operativa puede paralizar equipo pequeño ⚠️
- **Conclusión:** NO RECOMENDADO para este proyecto

---

##### **Opción C: Serverless (AWS Lambda)**

**✅ Ventajas:**
- Coste optimizado (pay-per-use, ~$50-100/mes inicial)
- Escalabilidad automática sin configuración
- No requiere gestión de servidores
- Despliegues independientes por función

**❌ Desventajas:**
- Vendor lock-in fuerte con AWS ⚠️
- Cold starts (latencia inicial 1-3 segundos)
- Debugging complejo (logs distribuidos en CloudWatch)
- Límites de ejecución (15 min timeout Lambda)
- Curva de aprendizaje nueva para el equipo
- Dificultad para desarrollo local

**🎯 Cuándo Elegir:**
- Cargas de trabajo irregulares (picos esporádicos)
- Presupuesto muy limitado
- Equipo con experiencia en cloud-native

**⚙️ Requisitos de Equipo:**
- 2-3 desarrolladores backend
- Nivel: Mid (experiencia con AWS) ⚠️
- Familiaridad con arquitectura event-driven

**⚠️ Riesgos:**
- Vendor lock-in dificulta migración futura
- Cold starts pueden afectar experiencia de usuario
- **Conclusión:** POSIBLE pero con trade-offs significativos

---

### **Paso 4: Recomendación Fundamentada**

## ✅ Recomendación Arquitectónica

### Opción Seleccionada: **Monolito Modular con Arquitectura Hexagonal**

**Recomiendo Monolito Modular porque:**

1. ✅ **Maximiza velocidad de desarrollo:** Permite entregar MVP en 2.5 meses (vs 4-5 meses con microservicios)
2. ✅ **Alineado con capacidades del equipo:** Complejidad manejable para equipo junior-mid sin DevOps dedicado
3. ✅ **Optimiza presupuesto:** Coste de infraestructura ~$120/mes vs $500+ de microservicios o lock-in de serverless
4. ✅ **Evolutividad preservada:** Límites de módulo claros (Arquitectura Hexagonal) permiten extracción futura a microservicios si e-commerce es exitoso
5. ✅ **Reduce riesgos:** Tecnologías conocidas por el equipo (Spring Boot), sin aprendizaje de paradigmas nuevos

**A pesar de aceptar los siguientes trade-offs:**

- ⚠️ **Escalabilidad horizontal limitada inicialmente** (aceptable para 500-1,000 usuarios concurrentes)
- ⚠️ **Deployment acoplado** (mitigado con tests automatizados + feature flags + releases controladas)
- ⚠️ **Requiere disciplina arquitectónica** para mantener límites de módulo (mitigado con ArchUnit tests automáticos)

---

#### Alineación con Requisitos

| Requisito | Prioridad Usuario | Soporte de Arquitectura | Justificación |
|-----------|-------------------|------------------------|---------------|
| Time-to-market (2.5 meses) | 🔴 CRÍTICO | 🟢 EXCELENTE | Desarrollo lineal sin overhead de coordinación |
| Presupuesto ($300/mes) | 🔴 CRÍTICO | 🟢 EXCELENTE | $120/mes infraestructura, 60% bajo presupuesto |
| Escalabilidad (500 users) | 🟡 MEDIO | 🟢 SUFICIENTE | Monolito escala vertical hasta 2-3K usuarios |
| Equipo sin DevOps | 🔴 CRÍTICO | 🟢 EXCELENTE | Deployment simple (un artefacto .jar) |
| Evolución futura | 🟡 MEDIO | 🟢 BUENA | Límites de módulo claros facilitan extracción |

---

### **Paso 5: Riesgos y Mitigaciones**

| # | Riesgo | Probabilidad | Impacto | Mitigación Propuesta |
|---|--------|--------------|---------|---------------------|
| R1 | Monolito se degrada a "Big Ball of Mud" por falta de disciplina | 🟡 MEDIA | 🔴 ALTO | - Aplicar Arquitectura Hexagonal desde inicio<br>- Code reviews enfocados en límites de módulo<br>- ArchUnit tests automáticos en CI<br>- Ejecutar `analizar_code_smells` mensualmente |
| R2 | Escalabilidad insuficiente si crecimiento es más rápido de lo esperado | 🟡 MEDIA | 🟡 MEDIO | - Diseñar con límites de módulo claros desde inicio<br>- Plan de extracción de primer microservicio preparado<br>- Monitoreo de métricas de carga desde día 1<br>- Umbral de pivot: 2,000 usuarios concurrentes |
| R3 | Equipo junior no adopta patrones arquitectónicos correctamente | 🟡 MEDIA | 🟡 MEDIO | - Sesiones de pair programming iniciales<br>- Documentar patrones en `artefactos/arquitectura_patrones.md`<br>- Usar `refactorizar` proactivamente<br>- Code reviews obligatorios |
| R4 | Integración con Stripe falla o cambia API | 🟢 BAJA | 🟡 MEDIO | - Usar SDK oficial de Stripe<br>- Testing exhaustivo en sandbox<br>- Capa anticorrupción para aislamiento |
| R5 | Falta de observabilidad dificulta debugging | 🟡 MEDIA | 🟢 BAJO | - Implementar logs estructurados (JSON)<br>- APM básico (New Relic free tier o Elastic APM)<br>- Healthchecks y métricas básicas |

---

### **Paso 6: Roadmap Técnico Inicial**

## 🛠️ Roadmap de Implementación (Primeros 3 Meses)

### **Sprint 0: Fundaciones (Semana 1-2)**
- [ ] Definir límites de módulos/dominios con equipo (sesión de Event Storming)
- [ ] Crear estructura de proyecto con submódulos Gradle:
  - `catalog-module`
  - `cart-checkout-module`
  - `order-management-module`
  - `shared-domain`
- [ ] Establecer convenciones de capas (domain, application, infrastructure)
- [ ] Configurar ArchUnit para validar reglas arquitectónicas
- [ ] Documentar patrones en `artefactos/arquitectura_patrones.md`
- [ ] Setup de infraestructura base (AWS Elastic Beanstalk + PostgreSQL RDS)

### **Sprint 1-2: Implementación Core (Semana 3-6)**
- [ ] **Catálogo:**
  - Modelo de dominio (Product, Category)
  - API REST para listado y búsqueda
  - Integración con PostgreSQL
- [ ] **Carrito:**
  - Gestión de sesión (Redis)
  - Agregar/remover productos
- [ ] **Autenticación básica** (Spring Security + JWT)
- [ ] **Frontend:** Integración React con APIs

### **Sprint 3-4: Checkout y Pagos (Semana 7-10)**
- [ ] **Checkout:**
  - Validación de inventario
  - Integración con Stripe (SDK oficial)
  - Webhook para confirmación de pago
- [ ] **Órdenes:**
  - Creación de orden post-pago
  - Estados de orden (pending, paid, shipped, delivered)
- [ ] **Panel Admin básico:** Gestión de productos y órdenes
- [ ] **Testing:** Cobertura mínima 70%

### **Sprint 5-6: Refinamiento Pre-MVP (Semana 11-12)**
- [ ] Ejecutar `analizar_code_smells` y aplicar `refactorizar` si necesario
- [ ] Documentación de APIs (Swagger/OpenAPI)
- [ ] Hardening de seguridad básico (OWASP Top 10)
- [ ] Pruebas de carga (Apache JMeter) - validar 500 usuarios concurrentes
- [ ] Observabilidad: Logs estructurados + healthchecks
- [ ] Preparación para Go-Live (runbooks, rollback plan)

---

### **Paso 7: Condiciones de Re-evaluación**

## 🔄 Condiciones de Re-evaluación Arquitectónica

**Debes considerar revisar esta decisión si:**

1. **Crecimiento de usuarios:** Se superan 2,000 usuarios concurrentes sostenidos (4x objetivo inicial)
2. **Ventas mensuales:** > $50K sostenidas (indicador de éxito comercial)
3. **Crecimiento de dominios:** Se añaden > 3 dominios de negocio nuevos (marketplace, subscripciones, B2B)
4. **Problemas de deployment:** Frecuencia de deployment deseable > 5 veces/día pero bloqueada por acoplamiento
5. **Crecimiento de equipo:** El equipo crece a 8+ desarrolladores con múltiples equipos autónomos
6. **Requisitos de latencia:** Tiempos de respuesta sostenidos > 1 segundo (p95)

**Revisión programada:** Junio 2026 (8 meses post-lanzamiento) o al alcanzar $50K ventas mensuales

**Plan de migración preparado:**
- Primer microservicio candidato: **Catálogo** (si se supera 10K productos o se requiere escalabilidad independiente)
- Estrategia: Strangler Fig Pattern (migración incremental)

---

### **Paso 8: Invocación de `generar_adr`**

## 📝 Generación de ADR Formal

**Confirmación del usuario:** ✅ Aprobado

**Comando ejecutado:**
```bash
> generar_adr
    titulo="Selección de Arquitectura Monolito Modular para E-Commerce MVP"
    contexto="Startup de e-commerce con equipo pequeño (2 devs backend, 1 frontend), presupuesto limitado ($300/mes), time-to-market crítico (2.5 meses). Volumen esperado: 500 usuarios concurrentes."
    decision="Monolito Modular con Arquitectura Hexagonal. Maximiza velocidad de desarrollo, alinea con capacidades del equipo, optimiza presupuesto, preserva evolutividad futura."
    consecuencias="Positivas: Time-to-market reducido (2.5 meses vs 4-5), coste optimizado ($120/mes vs $500+), tecnologías conocidas. Negativas: Escalabilidad horizontal limitada (aceptable para 500-1K usuarios), deployment acoplado (mitigado con tests + feature flags)."
    opciones_consideradas="1. Microservicios (descartado por sobrecarga operativa excesiva). 2. Serverless (descartado por vendor lock-in y cold starts). 3. Monolito Modular (seleccionado)."
    formato=nygard
    autores="ArchDev Pro, Tech Lead, Product Owner"
    estado=aceptado
```

**Resultado:**
✅ ADR generado exitosamente en `artefactos/adr/001-seleccion-arquitectura-monolito-modular-ecommerce-mvp.md`

---

## 📊 Métricas de Éxito del Proyecto

### Objetivos a Validar en los Primeros 6 Meses

| Métrica | Objetivo | Medición |
|---------|----------|----------|
| **Time-to-Market** | ≤ 2.5 meses | ✅ Arquitectura permite cumplir objetivo |
| **Coste Infraestructura** | ≤ $300/mes | ✅ Estimado $120-150/mes (50% bajo presupuesto) |
| **Usuarios Concurrentes** | 500 (picos 1,000) | Monitoreo continuo en producción |
| **Tiempo Respuesta (p95)** | < 2 segundos | APM + tests de carga validarán |
| **Uptime** | 99%+ | Monitoreo con healthchecks |
| **Cobertura Tests** | 70%+ | JaCoCo en pipeline CI |
| **Deuda Técnica** | Controlada | `analizar_code_smells` mensual |

---

## 🎓 Lecciones Aprendidas (Para Actualizar Post-Lanzamiento)

_Esta sección se actualizará después del lanzamiento del MVP con learnings reales:_

- ¿La arquitectura seleccionada permitió cumplir el time-to-market?
- ¿Surgieron problemas de escalabilidad no anticipados?
- ¿Fue necesario refactorizar antes de lo esperado?
- ¿El equipo adoptó correctamente los patrones arquitectónicos?

---

## 📚 Referencias

- **Análisis completo:** Este documento
- **ADR generado:** `artefactos/adr/001-seleccion-arquitectura-monolito-modular-ecommerce-mvp.md`
- **Herramienta utilizada:** `define_arquitectura` v2.0
- **Patrones aplicados:** 
  - [Arquitectura Hexagonal](https://alistair.cockburn.us/hexagonal-architecture/)
  - [Monolith First](https://martinfowler.com/bliki/MonolithFirst.html)
  - [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) (para migración futura)
