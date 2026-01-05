# 👥 Guía de Roles Activos del Sistema

> **Sistema:** Cochas - Orquestación de Agentes IA  
> **Versión:** 2.0  
> **Última Actualización:** 16 de octubre de 2025

---

## 📖 Índice

- [Introducción](#introducción)
- [Roles Disponibles](#roles-disponibles)
- [Matriz de Capacidades](#matriz-de-capacidades)
- [Cuándo Usar Cada Rol](#cuándo-usar-cada-rol)
- [Flujos de Trabajo Comunes](#flujos-de-trabajo-comunes)

---

## Introducción

Los roles (o personas) son agentes especializados con personalidades únicas, áreas de expertise específicas y herramientas dedicadas. Cada rol está diseñado para un tipo de tarea y momento del desarrollo.

**Principio clave:** No todos los roles hacen todo. Cada uno tiene un propósito específico.

---

## Roles Disponibles

### 🏛️ Arquitecto Onad (ONAD)

**Comando de activación:** `@ONAD` o `@switch ONAD`

**Especialidad:** Arquitectura estratégica y decisiones de alto nivel

**Personalidad:**
- 🎯 **Estilo:** Consultor técnico de élite, mentor arquitectónico
- 💬 **Comunicación:** Socrática (pregunta antes de responder)
- ⏱️ **Horizonte temporal:** Largo plazo (6-12 meses)
- 📊 **Enfoque:** Análisis de trade-offs y validación de supuestos

**Herramientas:**
- `tomar_contexto` - Analiza el proyecto completo
- `define_arquitectura` - Diseña arquitecturas con visión estratégica
- `generar_adr` - Documenta decisiones arquitectónicas importantes

**Cuándo usarlo:**
- ✅ Diseñar la arquitectura de un nuevo proyecto
- ✅ Evaluar propuestas técnicas complejas
- ✅ Analizar trade-offs de decisiones arquitectónicas
- ✅ Validar viabilidad técnica de alto nivel
- ✅ Documentar decisiones estratégicas (ADRs)
- ✅ Resolver deuda técnica arquitectónica

**Cuándo NO usarlo:**
- ❌ Implementar código específico (usa **ArchDev Pro**)
- ❌ Configurar infraestructura (usa **DevOps**)
- ❌ Refinar historias de usuario (usa **Refinador HU**)
- ❌ Crear mensajes de commit (usa **Artesano**)

**Principio Cardinal: "No Comer Entero"**
- Nunca acepta propuestas sin análisis crítico previo
- Siempre valida supuestos y evalúa alternativas
- Expone trade-offs antes de recomendar soluciones

**Ejemplo de interacción:**
```
Usuario: Propongo usar Redis como caché

ONAD:
Interesante. Antes de diseñar la implementación, validemos:

**Supuestos a validar:**
1. ¿Las consultas son realmente un cuello de botella medible?
2. ¿Cuál es el patrón de acceso?
3. ¿Qué TTL sería aceptable?

**Alternativas:**
1. Optimizar queries de BD primero
2. Caché HTTP con ETag
3. Redis con invalidación event-driven

¿Tienes métricas que justifiquen la complejidad añadida?
```

---

### 💻 ArchDev Pro (ARCHDEV)

**Comando de activación:** `@ARCHDEV` o `@switch ARCHDEV`

**Especialidad:** Implementación de código y refactoring

**Personalidad:**
- 🎯 **Estilo:** Desarrollador pragmático y experto en código
- 💬 **Comunicación:** Directa, con código y ejemplos concretos
- ⏱️ **Horizonte temporal:** Sprint actual (1-2 semanas)
- 🛠️ **Enfoque:** Código limpio, tests y mejores prácticas

**Herramientas:**
- `tomar_contexto` - Analiza el proyecto completo
- `refactorizar` - Mejora código existente aplicando patrones
- `analizar_code_smells` - Detecta problemas de calidad en el código
- `solucionar_smells` - Aplica soluciones a code smells detectados
- `crear_pruebas` - Genera tests unitarios y de integración
- `verifica_pruebas` - Valida calidad y cobertura de tests
- `generar_adr` - Documenta decisiones técnicas de implementación

**Cuándo usarlo:**
- ✅ Implementar código basado en diseños arquitectónicos
- ✅ Refactorizar código existente
- ✅ Crear tests unitarios y de integración
- ✅ Aplicar patrones de diseño ya decididos
- ✅ Resolver code smells y problemas de calidad
- ✅ Mejorar legibilidad y mantenibilidad del código

**Cuándo NO usarlo:**
- ❌ Tomar decisiones arquitectónicas estratégicas (usa **ONAD**)
- ❌ Configurar pipelines CI/CD (usa **DevOps**)
- ❌ Refinar historias de usuario (usa **Refinador HU**)
- ❌ Crear mensajes de commit profesionales (usa **Artesano**)

**Flujo típico con ONAD:**
```
1. ONAD diseña arquitectura → 2. ARCHDEV implementa código
```

**Ejemplo de interacción:**
```
Usuario: Necesito refactorizar el módulo de autenticación

ARCHDEV:
Perfecto. Voy a analizar el código y aplicar mejoras.

> analizar_code_smells

**Code Smells Detectados:**
1. Long Method en AuthService.authenticate()
2. Feature Envy en TokenValidator
3. Duplicación en métodos de validación

> solucionar_smells

**Refactorings Aplicados:**
1. Extract Method para reducir complejidad
2. Move Method para cohesión
3. Extract Common para DRY

> crear_pruebas

**Tests Generados:**
✅ 12 tests unitarios
✅ 4 tests de integración
✅ Cobertura: 95%
```

---

### 🚀 Arquitecto DevOps (DEVOPS)

**Comando de activación:** `@DEVOPS` o `@switch DEVOPS`

**Especialidad:** Infraestructura, pipelines y deployment

**Personalidad:**
- 🎯 **Estilo:** Especialista en operaciones y automatización
- 💬 **Comunicación:** Técnica, con foco en observabilidad y resiliencia
- ⏱️ **Horizonte temporal:** Inmediato a mediano plazo
- 🔧 **Enfoque:** Automatización, monitoreo y confiabilidad

**Herramientas:**
- `tomar_contexto` - Analiza el proyecto completo
- `diagnosticar_devops` - Analiza infraestructura, pipelines y deployment

**Cuándo usarlo:**
- ✅ Configurar pipelines CI/CD
- ✅ Optimizar infraestructura cloud
- ✅ Implementar estrategias de deployment
- ✅ Configurar contenedores y orquestación (Docker/K8s)
- ✅ Establecer monitoreo y observabilidad
- ✅ Resolver problemas de despliegue
- ✅ Diseñar estrategias de backup y recuperación

**Cuándo NO usarlo:**
- ❌ Diseñar arquitectura de aplicación (usa **ONAD**)
- ❌ Implementar código de negocio (usa **ArchDev Pro**)
- ❌ Refinar historias de usuario (usa **Refinador HU**)

**Ejemplo de interacción:**
```
Usuario: Necesito configurar CI/CD con GitHub Actions

DEVOPS:
Perfecto. Voy a diagnosticar tu proyecto y proponer un pipeline.

> diagnosticar_devops

**Diagnóstico Completo:**

📦 **Build & Test:**
- Maven/Gradle detectado
- Sugerencia: Pipeline multi-stage
- Tests: Separar unit/integration

🚀 **Deployment:**
- Opción 1: Docker + AWS ECS
- Opción 2: Kubernetes
- Opción 3: Serverless (Lambda)

📊 **Monitoreo:**
- Prometheus + Grafana
- CloudWatch Logs
- Health checks necesarios

¿Qué opción de deployment prefieres?
```

---

### 📝 Refinador HU (REFINADOR)

**Comando de activación:** `@REFINADOR` o `@switch REFINADOR`

**Especialidad:** Refinamiento de historias de usuario

**Personalidad:**
- 🎯 **Estilo:** Analista de negocio técnico
- 💬 **Comunicación:** Estructurada, con foco en criterios de aceptación
- ⏱️ **Horizonte temporal:** Sprint planning
- 📋 **Enfoque:** Claridad, completitud y estimabilidad

**Herramientas:**
- `tomar_contexto` - Analiza el proyecto completo
- `refinar_hu` - Refina historias de usuario con criterios claros

**Cuándo usarlo:**
- ✅ Refinar historias de usuario antes del sprint
- ✅ Clarificar requisitos ambiguos
- ✅ Definir criterios de aceptación precisos
- ✅ Identificar dependencias técnicas
- ✅ Estimar complejidad de historias
- ✅ Detectar historias que requieren splitting

**Cuándo NO usarlo:**
- ❌ Implementar código (usa **ArchDev Pro**)
- ❌ Diseñar arquitectura (usa **ONAD**)
- ❌ Configurar infraestructura (usa **DevOps**)

**Ejemplo de interacción:**
```
Usuario: HU: Como usuario quiero buscar productos

REFINADOR:
Veo que esta historia necesita refinamiento. Vamos a clarificarla.

> refinar_hu

**Historia Refinada:**

**Título:** Como usuario quiero buscar productos por nombre y categoría

**Descripción:**
Como usuario del e-commerce
Quiero buscar productos usando filtros
Para encontrar rápidamente lo que necesito

**Criterios de Aceptación:**
✅ Búsqueda por nombre (mínimo 3 caracteres)
✅ Filtro por categoría (dropdown)
✅ Resultados paginados (10 por página)
✅ Tiempo de respuesta < 500ms
✅ Sin resultados: mensaje claro

**Dependencias Técnicas:**
- API de búsqueda existente
- Índice de productos en BD

**Estimación:** 5 puntos (1 sprint)

**Notas Técnicas:**
- Considerar caché para queries frecuentes
- Validar input del usuario (SQL injection)
```

---

### 🎨 Artesano de Commits (ARTESANO)

**Comando de activación:** `@ARTESANO` o `@switch ARTESANO`

**Especialidad:** Creación de mensajes de commit profesionales

**Personalidad:**
- 🎯 **Estilo:** Perfeccionista de la documentación de cambios
- 💬 **Comunicación:** Concisa pero completa
- ⏱️ **Horizonte temporal:** Inmediato (por commit)
- 📝 **Enfoque:** Conventional Commits y trazabilidad

**Herramientas:**
- `generar_commit` - Crea mensajes de commit siguiendo mejores prácticas

**Cuándo usarlo:**
- ✅ Crear mensajes de commit profesionales
- ✅ Documentar cambios complejos en el código
- ✅ Seguir Conventional Commits
- ✅ Mejorar trazabilidad del historial de Git
- ✅ Vincular commits con issues/tasks

**Cuándo NO usarlo:**
- ❌ Implementar código (usa **ArchDev Pro**)
- ❌ Diseñar arquitectura (usa **ONAD**)
- ❌ Cualquier cosa que no sea crear commits

**Ejemplo de interacción:**
```
Usuario: Necesito un commit para los cambios de autenticación

ARTESANO:
Perfecto. Voy a generar un mensaje de commit profesional.

> generar_commit

**Mensaje de Commit Generado:**

feat(auth): implement JWT-based authentication

Implement JWT token generation and validation for user authentication.

**Changes:**
- Add JwtTokenProvider with RS256 signing
- Implement TokenAuthenticationFilter
- Add SecurityConfig with JWT integration
- Include token refresh mechanism

**Technical Details:**
- Tokens expire after 1 hour
- Refresh tokens valid for 7 days
- Public/private key pair for signing

**Tests:**
- Unit tests for JwtTokenProvider
- Integration tests for auth endpoints
- Security tests for unauthorized access

**Breaking Changes:** None

**Related:** AUTH-123, AUTH-124

---

**Comando para ejecutar:**
git commit -m "feat(auth): implement JWT-based authentication" -m "..."
```

---

## Matriz de Capacidades

| Capacidad / Rol | ONAD | ARCHDEV | DEVOPS | REFINADOR | ARTESANO |
|-----------------|------|---------|--------|-----------|----------|
| **Diseñar arquitectura** | ✅ Experto | ⚠️ Básico | ⚠️ Infra | ❌ No | ❌ No |
| **Implementar código** | ❌ No | ✅ Experto | ⚠️ Scripts | ❌ No | ❌ No |
| **Refactorizar** | ⚠️ Estratégico | ✅ Experto | ❌ No | ❌ No | ❌ No |
| **Crear tests** | ❌ No | ✅ Experto | ⚠️ Básico | ❌ No | ❌ No |
| **Configurar CI/CD** | ❌ No | ❌ No | ✅ Experto | ❌ No | ❌ No |
| **Infraestructura cloud** | ⚠️ Consulta | ❌ No | ✅ Experto | ❌ No | ❌ No |
| **Refinar HU** | ⚠️ Validar | ❌ No | ❌ No | ✅ Experto | ❌ No |
| **Crear commits** | ❌ No | ⚠️ Básico | ❌ No | ❌ No | ✅ Experto |
| **Analizar trade-offs** | ✅ Experto | ⚠️ Técnico | ⚠️ Infra | ❌ No | ❌ No |
| **Documentar decisiones (ADR)** | ✅ Experto | ⚠️ Técnico | ⚠️ Infra | ❌ No | ❌ No |

**Leyenda:**
- ✅ **Experto** - Capacidad principal del rol
- ⚠️ **Básico/Limitado** - Puede hacerlo pero no es su fuerte
- ❌ **No** - No es responsabilidad de este rol

---

## Cuándo Usar Cada Rol

### Preguntas Guía

**¿Necesitas tomar una decisión arquitectónica importante?**
→ Usa **ONAD** para analizar trade-offs y alternativas

**¿Ya tienes el diseño y necesitas implementarlo?**
→ Usa **ArchDev Pro** para escribir código limpio

**¿Necesitas configurar infraestructura o deployment?**
→ Usa **DevOps** para automatizar y optimizar

**¿Tienes historias de usuario ambiguas?**
→ Usa **Refinador HU** para clarificarlas

**¿Necesitas commitear cambios profesionalmente?**
→ Usa **Artesano** para documentar correctamente

---

### Matriz de Decisión por Escenario

| Escenario | Rol Recomendado | Justificación |
|-----------|----------------|---------------|
| Diseñar sistema desde cero | **ONAD** | Requiere visión estratégica y análisis de trade-offs |
| Evaluar propuesta técnica | **ONAD** | Necesita validación crítica y alternativas |
| Implementar feature | **ArchDev Pro** | Código concreto con tests |
| Mejorar código existente | **ArchDev Pro** | Refactoring táctico |
| Configurar pipeline | **DevOps** | Automatización y deployment |
| Optimizar infraestructura | **DevOps** | Conocimiento de cloud y ops |
| Clarificar requisitos | **Refinador HU** | Análisis de negocio técnico |
| Documentar cambios en Git | **Artesano** | Conventional Commits |
| Resolver deuda técnica arquitectónica | **ONAD** | Análisis estratégico |
| Resolver code smells | **ArchDev Pro** | Refactoring de código |
| Investigar problema de producción | **DevOps** | Troubleshooting y logs |
| Estimar complejidad de HU | **Refinador HU** | Análisis técnico de historias |

---

## Flujos de Trabajo Comunes

### Flujo 1: Nuevo Proyecto

```
1. @ONAD
   > tomar_contexto              # Analizar proyecto
   > define_arquitectura          # Diseñar arquitectura
   > generar_adr                  # Documentar decisiones

2. @DEVOPS
   > diagnosticar_devops          # Configurar infraestructura

3. @ARCHDEV
   > refactorizar                 # Implementar código
   > crear_pruebas                # Agregar tests

4. @ARTESANO
   > generar_commit               # Documentar cambios
```

---

### Flujo 2: Refactoring Mayor

```
1. @ONAD
   > tomar_contexto              # Analizar situación actual
   Validar propuesta de refactoring

2. @ARCHDEV
   > analizar_code_smells         # Detectar problemas
   > solucionar_smells            # Aplicar mejoras
   > verifica_pruebas             # Validar tests

3. @ARTESANO
   > generar_commit               # Documentar refactoring
```

---

### Flujo 3: Sprint Planning

```
1. @REFINADOR
   > refinar_hu                   # Clarificar historias

2. @ONAD
   Validar viabilidad técnica de historias

3. @ARCHDEV
   Estimar esfuerzo de implementación
```

---

### Flujo 4: Deployment de Feature

```
1. @ARCHDEV
   > crear_pruebas                # Asegurar cobertura
   > verifica_pruebas             # Validar calidad

2. @DEVOPS
   > diagnosticar_devops          # Preparar deployment

3. @ARTESANO
   > generar_commit               # Documentar release
```

---

### Flujo 5: Resolución de Propuesta Técnica

```
1. @ONAD
   Analizar propuesta con "No Comer Entero"
   - Validar supuestos
   - Evaluar trade-offs
   - Proponer alternativas

2. Si se aprueba → @ARCHDEV
   Implementar la solución validada

3. Si requiere infra → @DEVOPS
   Configurar recursos necesarios
```

---

## 💡 Tips para Elegir el Rol Correcto

### Tip 1: Usa `@assign` Cuando Tengas Dudas
```bash
@assign "Tu descripción de la tarea"
```
El sistema analizará tu necesidad y recomendará el rol más adecuado.

### Tip 2: Horizonte Temporal
- **Largo plazo (6-12 meses)** → **ONAD**
- **Sprint actual (1-2 semanas)** → **ArchDev Pro**
- **Inmediato (operaciones)** → **DevOps**
- **Planning** → **Refinador HU**
- **Por commit** → **Artesano**

### Tip 3: Naturaleza de la Tarea
- **¿Qué hacer?** → **ONAD** (estrategia)
- **¿Cómo implementar?** → **ArchDev Pro** (código)
- **¿Cómo desplegar?** → **DevOps** (infraestructura)
- **¿Qué construir exactamente?** → **Refinador HU** (requisitos)
- **¿Cómo documentar?** → **Artesano** (commits)

### Tip 4: Nivel de Abstracción
- **Alto nivel (arquitectura)** → **ONAD**
- **Medio nivel (código)** → **ArchDev Pro**
- **Operaciones (infra)** → **DevOps**
- **Negocio (requisitos)** → **Refinador HU**
- **Documentación (Git)** → **Artesano**

---

## 🔄 Cambio Entre Roles

Es común necesitar múltiples roles en una sesión. El sistema mantiene el contexto entre cambios:

```bash
# Analizar arquitectura
@ONAD
> define_arquitectura

# Implementar código
@ARCHDEV
> refactorizar

# Configurar deployment
@DEVOPS
> diagnosticar_devops

# Crear commit
@ARTESANO
> generar_commit

# Ver historial de cambios
@history
```

**El sistema recuerda:**
- ✅ Contexto del proyecto analizado
- ✅ Tareas completadas por cada rol
- ✅ Decisiones tomadas
- ✅ Estado del backlog

---

## 📚 Documentación Relacionada

- **[README Principal](README.md)** - Visión general del sistema
- **[Guía de Comandos](guia_comandos.md)** - Comandos detallados
- **[Guía de Ciclo de Vida](guia_ciclo_vida_tareas.md)** - Flujo de tareas
- **[Crear Roles Personalizados](guia_creacion_roles.md)** - Extender el sistema

---

**¿No estás seguro qué rol usar?**

Ejecuta: `@assign "descripción de tu tarea"`

El orquestador te recomendará el rol más adecuado con justificación.
