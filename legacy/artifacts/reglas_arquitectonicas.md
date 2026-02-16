# 📐 Reglas Arquitectónicas del Proyecto

> **Proyecto:** ms-banca-conversacion  
> **Stack:** Java 21 + Spring Boot 3.x  
> **Generado:** 2026-02-15  
> **Versión:** 1.0  
> **Aprobado por:** Usuario

---

## 📋 Índice

1. [Nomenclatura](#1-nomenclatura)
2. [Arquitectura](#2-arquitectura)
3. [Patrones de Diseño](#3-patrones-de-diseño)
4. [Principios y Paradigmas](#4-principios-y-paradigmas)
5. [Dependencias](#5-dependencias)
6. [Testing](#6-testing)
7. [Documentación](#7-documentación)
8. [Seguridad y Calidad](#8-seguridad-y-calidad)
9. [Checklist de Validación](#9-checklist-de-validación)

---

## 1. Nomenclatura

### 1.1 Convenciones Generales

| Elemento | Convención | Ejemplo | Anti-patrón |
|----------|------------|---------|-------------|
| Clases/Tipos | PascalCase | `MotorDeInteraccion`, `EstrategiaBase` | `motorDeInteraccion`, `estrategia_base` |
| Métodos/Funciones | camelCase | `procesarEtapa()`, `obtenerEstrategia()` | `ProcesarEtapa()`, `obtener_estrategia()` |
| Variables | camelCase | `interaccionDTO`, `mensajeRespuesta` | `InteraccionDTO`, `mensaje_respuesta` |
| Constantes | UPPER_SNAKE_CASE | `ERROR_ENVIANDO_RESPUESTA`, `MAX_REINTENTOS` | `errorEnviandoRespuesta` |
| Interfaces (Puertos) | Sin prefijo, nombre descriptivo | `PuertoGuardarInteraccion`, `EstrategiaDeInteraccionPorEtapa` | `IPuertoGuardarInteraccion` |
| Implementaciones | Prefijo/Sufijo descriptivo tecnología | `RepositorioEventoWebhookRabbitMQ`, `InteraccionJdbcRepository` | `RepositorioEventoWebhookImpl` |

### 1.2 Patrones de Nombres por Tipo

| Tipo de Clase | Patrón | Ejemplo |
|---------------|--------|---------|
| Entidad | `{Sustantivo}` | `Interaccion`, `Usuario`, `Mensaje` |
| Value Object | `{Concepto}` | `TelefonoUsuario`, `EtapaInteraccion` |
| Servicio de Dominio | `Servicio{Dominio}` | `ServicioCacheRetiro`, `ServicioContextoConversacion` |
| Caso de Uso | `{Accion}{Entidad}UseCase` | `IniciarInteraccionUseCase` |
| Puerto (Interface) | `Puerto{Accion}{Entidad}` | `PuertoGuardarInteraccion`, `PuertoObtenerInteraccion` |
| Repositorio | `{Entidad}Repository` o `Repositorio{Entidad}{Tecnologia}` | `InteraccionJdbcRepository`, `RepositorioEventoWebhookRabbitMQ` |
| Controlador | `{Recurso}Controller` | `ComandoWebhookEventController`, `AutenticacionController` |
| DTO Request | `{Accion}{Entidad}Request` | `SolicitudEnviarMensajeWhatsAppDTO` |
| DTO Response | `{Entidad}Response` o `{Entidad}DTO` | `InteraccionDTO`, `ResultadoEstrategia` |
| Excepción | `Excepcion{Dominio}` | `ExcepcionEnviarRespuestaBot` |
| Evento | `{Entidad}{Accion}Event` | `MensajeRecibidoEvent` |
| Estrategia | `Estrategia{Descripcion}` o `{Descripcion}Estrategia` | `EstrategiaBase`, `EstrategiaDeInteraccionPorEtapa` |
| Manejador | `Manejador{Evento}` | `ManejadorRecibirEventoServicioBmm` |

### 1.3 Prefijos y Sufijos

| Uso | Prefijo/Sufijo | Ejemplo | Cuándo Usar |
|-----|----------------|---------|-------------|
| Interfaces | Sin prefijo | `PuertoGuardarInteraccion` | Siempre en dominio |
| Implementaciones | Sufijo tecnología | `InteraccionJdbcRepository`, `RepositorioRabbitMQ` | Cuando hay múltiples implementaciones |
| Test classes | `Test` sufijo | `MotorDeInteraccionTest` | Siempre para tests |
| Integration tests | `IntegrationTest` sufijo | `FlowEndpointControllerIntegrationTest` | Tests de integración |
| Mocks | `Mock` prefijo | `MockPuertoGuardarInteraccion` | En tests |

---

## 2. Arquitectura

### 2.1 Estilo Arquitectónico

**Patrón Principal:** Arquitectura Hexagonal (Puertos y Adaptadores)

La arquitectura separa claramente las responsabilidades en tres capas principales, donde el dominio es el núcleo independiente de frameworks y tecnologías externas. Los puertos definen las interfaces que el dominio necesita, y los adaptadores (en infraestructura) proporcionan las implementaciones concretas.

### 2.2 Estructura de Carpetas/Paquetes

```
microservicio/
├── dominio/                          # Capa de Dominio (núcleo)
│   └── src/main/java/co/com/bmm/
│       ├── modelo/                   # Entidades, Value Objects, Enums
│       ├── puerto/                   # Interfaces (puertos de salida)
│       ├── servicio/                 # Servicios de dominio
│       ├── maquina_estados/          # Motor FSM y estrategias
│       │   └── estrategias/          # Implementaciones de estrategias
│       ├── dto/                      # DTOs del dominio
│       └── excepciones/              # Excepciones de dominio
│
├── aplicacion/                       # Capa de Aplicación (casos de uso)
│   └── src/main/java/co/com/bmm/
│       ├── casosdeuso/               # Casos de uso / Application Services
│       └── manejador/                # Manejadores de eventos
│
└── infraestructura/                  # Capa de Infraestructura (adaptadores)
    └── src/main/java/co/com/bmm/
        ├── webhook/                  # Adaptadores REST (controllers)
        ├── jdbc/                     # Adaptadores de persistencia
        ├── mensaje/                  # Adaptadores de mensajería (RabbitMQ)
        ├── servicio/                 # Implementaciones de servicios externos
        ├── configuracion/            # Configuración Spring
        └── util/                     # Utilidades de infraestructura
```

### 2.3 Reglas de Dependencia

```
┌─────────────────────────────────────────────────────────────┐
│                    INFRAESTRUCTURA                          │
│  (Controllers, Repositories, Adapters, Config)              │
│                         │                                   │
│                         ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   APLICACIÓN                          │  │
│  │  (Use Cases, Application Services, Handlers)          │  │
│  │                         │                             │  │
│  │                         ▼                             │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │                   DOMINIO                       │  │  │
│  │  │  (Entities, Value Objects, Ports, Services)     │  │  │
│  │  │  ⚠️ SIN dependencias externas                   │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Regla:** Estricta - Las dependencias solo fluyen hacia adentro (infraestructura → aplicación → dominio). **NUNCA** al revés.

| Capa | Puede Importar | NO Puede Importar |
|------|----------------|-------------------|
| Dominio | Solo Java estándar, sin frameworks | Aplicación, Infraestructura, Spring, JPA |
| Aplicación | Dominio | Infraestructura |
| Infraestructura | Dominio, Aplicación | - |

### 2.4 Domain-Driven Design

**Nivel de DDD:** DDD Táctico parcial

| Táctica DDD | Uso | Descripción |
|-------------|-----|-------------|
| Entities | ✅ Sí | Objetos con identidad (`Interaccion`, `Usuario`) |
| Value Objects | ✅ Sí | Objetos inmutables por valor (`EtapaInteraccion`, `DisparadorDeEstrategia`) |
| Domain Events | ✅ Sí | Eventos de dominio via RabbitMQ (`MensajeParaServicio`) |
| Repositories | ✅ Sí | Puertos en dominio, implementaciones en infraestructura |
| Domain Services | ✅ Sí | Lógica de dominio que no pertenece a una entidad (`ServicioCacheRetiro`) |
| Aggregates | ⚠️ Parcial | Agrupación lógica, no estricta |

---

## 3. Patrones de Diseño

### 3.1 Patrones Obligatorios

| Patrón | Cuándo Usar | Ejemplo de Aplicación |
|--------|-------------|----------------------|
| Repository | Acceso a datos externos | `PuertoGuardarInteraccion` (puerto) → `InteraccionJdbcRepository` (impl) |
| Strategy | Lógica intercambiable por etapa/disparador | `EstrategiaDeInteraccionPorEtapa`, `EstrategiaBase` |
| Factory/Builder | Objetos con >3 parámetros o creación compleja | `ResultadoEstrategia.builder()` |
| Adapter | Integración con sistemas externos | `RepositorioEventoWebhookRabbitMQ`, `ServicioDeMensajeriaWhatsApp` |
| Template Method | Lógica común con pasos variables | `EstrategiaBase.ejecutar()` con `logicaEspecificaDeEtapa()` |
| State Machine | Flujo de conversación con estados definidos | `MotorDeInteraccion` con `EtapaInteraccion` |
| Dependency Injection | Inyección de dependencias | Constructor injection en todas las clases |

### 3.2 Patrones Prohibidos

| Patrón | Razón | Alternativa |
|--------|-------|-------------|
| Singleton | Estado global dificulta testing y paralelismo | Inyección de dependencias (Spring beans) |
| Service Locator | Anti-pattern, oculta dependencias reales | Constructor injection explícito |
| God Object | Viola SRP, difícil de mantener y testear | Descomponer en clases cohesivas con responsabilidad única |
| Anemic Domain Model | Lógica fuera del dominio | Encapsular comportamiento en entidades/servicios de dominio |

### 3.3 Guía de Selección de Patrones

| Situación | Patrón Recomendado | Justificación |
|-----------|-------------------|---------------|
| Creación de objetos complejos (>3 params) | Builder | Legibilidad, inmutabilidad, validación en construcción |
| Múltiples algoritmos intercambiables | Strategy | Open/Closed principle, extensibilidad |
| Acceso a datos externos | Repository | Abstracción de persistencia, testabilidad |
| Llamadas a servicios externos | Adapter | Aislamiento de dependencias, facilita mocking |
| Operaciones que pueden fallar (servicios externos) | Circuit Breaker | Resiliencia, fail-fast |
| Notificación de cambios entre módulos | Observer/Events | Desacoplamiento, comunicación asíncrona |
| Flujo con estados definidos | State Machine | Control explícito de transiciones |

---

## 4. Principios y Paradigmas

### 4.1 Principios SOLID

**Nivel de aplicación:** Estricto (todos obligatorios)

| Principio | Obligatorio | Guía de Aplicación |
|-----------|-------------|-------------------|
| **S**ingle Responsibility | ✅ Sí | Una clase = una razón para cambiar. Ej: `EstrategiaBase` solo orquesta, delega lógica específica |
| **O**pen/Closed | ✅ Sí | Abierto a extensión, cerrado a modificación. Ej: Nuevas estrategias sin modificar `MotorDeInteraccion` |
| **L**iskov Substitution | ✅ Sí | Subtipos intercambiables. Ej: Cualquier `EstrategiaDeInteraccionPorEtapa` funciona en el motor |
| **I**nterface Segregation | ✅ Sí | Interfaces pequeñas y específicas. Ej: Puertos separados por operación |
| **D**ependency Inversion | ✅ Sí | Depender de abstracciones. Ej: Dominio define `Puerto*`, infraestructura implementa |

### 4.2 Principios Adicionales

| Principio | Aplicación |
|-----------|------------|
| DRY | Extraer código duplicado a métodos/clases comunes. No duplicar lógica de negocio |
| KISS | Preferir soluciones simples. Evitar sobre-ingeniería |
| YAGNI | No implementar funcionalidad "por si acaso". Solo lo necesario ahora |

### 4.3 Inmutabilidad

**Política:** Inmutabilidad por defecto

- [x] Usar `final` en campos siempre que sea posible
- [x] Preferir Records para DTOs (`ResultadoEstrategia`, `ContextoEstrategia`)
- [x] Value Objects siempre inmutables
- [x] Colecciones inmutables: `Collections.unmodifiableMap()`, `List.of()`
- [x] Usar `Objects.requireNonNull()` en constructores

### 4.4 Manejo de Null

**Política:** Prohibir null - usar `Optional` y validación explícita

| Situación | Manejo Requerido |
|-----------|------------------|
| Retorno de métodos | `Optional<T>` para valores que pueden no existir |
| Parámetros obligatorios | `Objects.requireNonNull(param, "mensaje")` en constructor |
| Parámetros opcionales | Sobrecarga de métodos o `Optional<T>` |
| Campos opcionales | `Optional<T>` o valor por defecto |

### 4.5 Paradigma

**Paradigma predominante:** Híbrido (OOP estructura, Funcional lógica)

| Aspecto | Enfoque |
|---------|---------|
| Estructura | OOP - Clases, interfaces, herencia controlada |
| Lógica de negocio | OOP - Encapsulada en dominio |
| Transformaciones de datos | Funcional - Streams, lambdas, métodos funcionales |
| DTOs | Records (inmutables, funcionales) |

### 4.6 Composición vs Herencia

**Política:** Composición preferida (herencia permitida solo si framework lo requiere o es-un verdadero)

- ✅ **Usar herencia cuando:** Framework lo requiere (Spring), es-un verdadero (`EstrategiaBase` → estrategias concretas)
- ❌ **Evitar herencia cuando:** Solo para reutilizar código, más de 2 niveles de profundidad
- ✅ **Preferir composición:** `DependenciasEstrategiaBase` inyectado en estrategias

---

## 5. Dependencias

### 5.1 Dependencias Aprobadas

#### Testing
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
| JUnit Jupiter | 5.x | Framework de testing principal |
| Mockito | 5.x | Mocking de dependencias |
| AssertJ | 3.x | Aserciones fluidas |
| ArchUnit | 1.x | Validación de arquitectura |
| Testcontainers | 1.x | Tests de integración con contenedores |

#### Logging
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
| SLF4J | 2.x | API de logging |
| java.util.logging | JDK 21 | Implementación nativa |

#### Frameworks
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
| Spring Boot | 3.x | Framework principal |
| Spring AMQP | 3.x | Integración RabbitMQ |
| Spring JDBC | 3.x | Acceso a datos |
| MapStruct | 1.x | Mapeo de objetos |
| Jackson | 2.x | Serialización JSON |

### 5.2 Dependencias Prohibidas

| Librería | Razón | Alternativa |
|----------|-------|-------------|
| Lombok `@Data` | Genera código mutable, dificulta debugging | Records de Java 21 |
| Apache Commons Lang (obsoleto) | APIs nativas suficientes | `java.util.Objects`, `String` methods |
| JUnit 4 | Obsoleto | JUnit 5 Jupiter |
| Dependencias con CVEs conocidas | Seguridad | Versiones parcheadas |

### 5.3 Política de Actualizaciones

**Estrategia:** Versiones LTS preferidas

- Actualizar dependencias con CVEs críticas inmediatamente
- Evaluar actualizaciones mayores cada trimestre
- Mantener compatibilidad con Java LTS (21)
- Usar `resolutionStrategy.force` para fijar versiones seguras

---

## 6. Testing

### 6.1 Metodología

**Enfoque principal:** TDD flexible (test junto al código)

- Escribir tests antes o junto con la implementación
- Cada nueva funcionalidad debe incluir tests
- Refactoring siempre con tests pasando

### 6.2 Cobertura

| Capa | Cobertura Mínima | Tipo de Tests |
|------|------------------|---------------|
| Dominio | 90% | Unitarios puros (sin mocks de framework) |
| Aplicación | 85% | Unitarios + Integración |
| Infraestructura | 75% | Integración con Testcontainers |
| **Global** | **80%** | Todos |

### 6.3 Convención de Nombres

**Patrón:** `should_{resultado}_when_{condicion}`

**Ejemplos:**
```java
@Test
void should_return_estrategia_when_etapa_y_disparador_validos() { }

@Test
void should_throw_exception_when_interaccion_es_null() { }

@Test
void should_persist_interaccion_when_datos_validos() { }
```

### 6.4 Estructura de Tests

**Patrón:** Given-When-Then (Arrange-Act-Assert)

```java
@Test
void should_procesar_etapa_when_estrategia_existe() {
    // Given (Arrange)
    var interaccion = crearInteraccionValida();
    var disparador = DisparadorDeEstrategia.EVENTO_MENSAJE_WHATSAPP;
    
    // When (Act)
    motor.procesarEtapa(interaccion, disparador, "mensaje");
    
    // Then (Assert)
    assertThat(interaccion.getEtapa()).isEqualTo(EtapaInteraccion.SIGUIENTE);
}
```

### 6.5 Tests de Integración

**Herramienta:** Testcontainers

**Configuración:**
- PostgreSQL en contenedor para tests de repositorio
- RabbitMQ en contenedor para tests de mensajería
- Redis en contenedor para tests de caché
- Usar `@Testcontainers` y `@Container` annotations

---

## 7. Documentación

### 7.1 Documentación de Código

**Obligatoria en:**
- [x] Clases/Interfaces públicas
- [x] Métodos públicos
- [x] Métodos complejos (>10 líneas o lógica no trivial)
- [x] Excepciones y casos especiales

**Formato de comentarios (Javadoc):**
```java
/**
 * Descripción breve de la clase/método.
 *
 * <p>Descripción detallada si es necesario, incluyendo comportamiento,
 * restricciones y consideraciones importantes.</p>
 *
 * @param parametro descripción del parámetro
 * @return descripción del valor de retorno
 * @throws ExcepcionTipo cuando ocurre X condición
 * @author Equipo BMM
 * @since 2025
 */
```

### 7.2 Architecture Decision Records (ADRs)

**Formato:** MADR (Markdown ADR)

**Ubicación:** `.SAC/artifacts/ADR/`

**Plantilla:**
```markdown
# ADR-{número}: {título}

## Estado
{Propuesto | Aceptado | Rechazado | Deprecado | Supersedido por ADR-X}

## Contexto
{Descripción del problema y contexto}

## Decisión
{La decisión tomada}

## Consecuencias
### Positivas
- {consecuencia positiva}

### Negativas
- {consecuencia negativa}

## Alternativas Consideradas
### Opción 1: {nombre}
- Pro: {ventaja}
- Con: {desventaja}
```

### 7.3 README por Módulo

- [x] Cada módulo principal debe tener README
- [x] Incluir: propósito, dependencias, ejemplos de uso
- [x] Mantener actualizado con cambios significativos

---

## 8. Seguridad y Calidad

### 8.1 Datos Sensibles

**Regla de logging:** NUNCA loguear datos sensibles

| Tipo de Dato | Loguear | Acción |
|--------------|---------|--------|
| Passwords | ❌ NUNCA | No incluir en ningún log |
| Tokens/API Keys | ❌ NUNCA | Enmascarar si necesario para debug |
| PII (emails, nombres, documentos) | ❌ NUNCA | Enmascarar: `***@domain.com`, `****1234` |
| Números de teléfono | ❌ NUNCA | Enmascarar últimos 4 dígitos visibles |
| IDs de transacción | ✅ Permitido | Para trazabilidad |
| Etapas/Estados | ✅ Permitido | Para debugging de flujo |

### 8.2 Validación de Entradas

**Política:** Obligatoria en todos los puntos de entrada

- [x] Validar en punto de entrada (Controllers/Handlers)
- [x] Validar en constructores de dominio (fail-fast con `Objects.requireNonNull`)
- [x] Usar Bean Validation (`@NotNull`, `@Valid`) en DTOs de entrada
- [x] Sanitizar entradas de usuario antes de procesar

### 8.3 Límites de Código

| Métrica | Límite | Acción si Excede |
|---------|--------|------------------|
| Líneas por método | 30 | Extraer métodos privados |
| Líneas por clase | 300 | Dividir responsabilidades, extraer clases |
| Parámetros por método | 5 | Usar objeto de parámetros (Parameter Object) |
| Complejidad ciclomática | 10 | Simplificar lógica, extraer métodos |
| Profundidad de herencia | 2 | Preferir composición |

### 8.4 Análisis Estático

**Herramientas obligatorias:**
- SonarQube (calidad de código)
- OWASP Dependency Check (vulnerabilidades en dependencias)
- ArchUnit (validación de arquitectura en tests)

**Configuración:** 
- Quality Gate de SonarQube debe pasar en CI/CD
- No merge si hay vulnerabilidades críticas/altas
- Tests de ArchUnit en cada build

---

## 9. Checklist de Validación

### Para Code Reviews

- [ ] ¿Sigue las convenciones de nomenclatura (PascalCase clases, camelCase métodos)?
- [ ] ¿Respeta las capas arquitectónicas (dominio sin dependencias externas)?
- [ ] ¿Usa los patrones obligatorios correctamente (Repository, Strategy, etc.)?
- [ ] ¿Tiene tests con cobertura >= 80%?
- [ ] ¿Documenta según las reglas (Javadoc en públicos)?
- [ ] ¿No usa dependencias prohibidas?
- [ ] ¿No loguea datos sensibles (PII, tokens)?
- [ ] ¿Métodos/clases dentro de límites de tamaño (30/300 líneas)?
- [ ] ¿Usa `final` e inmutabilidad donde corresponde?
- [ ] ¿Valida entradas con `Objects.requireNonNull` o Bean Validation?

### Para Pull Requests

- [ ] Tests pasan ✅
- [ ] Cobertura >= 80%
- [ ] Sin warnings críticos de SonarQube
- [ ] Sin vulnerabilidades críticas/altas (OWASP)
- [ ] Documentación actualizada si aplica
- [ ] ADR creado si hay decisión arquitectónica significativa
- [ ] Tests de ArchUnit pasan

---

## 📜 Historial de Cambios

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | 2026-02-15 | Usuario | Versión inicial |

---

---
✅ Aprobado por **Usuario** | 📅 2026-02-15
---
