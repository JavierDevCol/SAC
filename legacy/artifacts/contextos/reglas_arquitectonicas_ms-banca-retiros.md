# 📐 Reglas Arquitectónicas del Proyecto

> **Proyecto:** ms-banca-retiros  
> **Stack:** Java 21, Spring Boot 3.5.4, Gradle  
> **Generado:** 2026-02-15  
> **Versión:** 1.0  
> **Aprobado por:** JavierMaldonado

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
| Clases/Tipos | PascalCase | `RetiroService`, `OtpController` | `retiro_service` |
| Métodos/Funciones | camelCase | `validarOtp()`, `procesarRetiro()` | `Validar_Otp()` |
| Variables | camelCase | `montoRetiro`, `codigoOtp` | `monto_retiro` |
| Constantes | UPPER_SNAKE_CASE | `MAX_REINTENTOS`, `TIMEOUT_OTP` | `maxReintentos` |
| Interfaces (Puertos) | Sin prefijo, sufijo descriptivo | `PuertoOTPBanco`, `RepositorioRetiro` | `IPuertoOTP` |
| Implementaciones | Prefijo descriptivo (tecnología) | `RabbitOtpAdapter`, `RedisRetiroRepository` | `PuertoOTPImpl` |

### 1.2 Patrones de Nombres por Tipo

| Tipo | Patrón | Ejemplo |
|------|--------|---------|
| Entidad | `{Sustantivo}` | `Retiro`, `OtpSolicitud` |
| Value Object | `{Concepto}` | `MontoRetiro`, `CodigoOtp` |
| Puerto (Interfaz) | `Puerto{Dominio}` | `PuertoOTPBanco`, `PuertoOTPInfobip` |
| Adaptador | `{Tecnologia}{Dominio}Adapter` | `RabbitOtpAdapter` |
| Caso de Uso | `{Accion}{Entidad}UseCase` | `ValidarOtpUseCase` |
| DTO Request | `{Accion}{Entidad}Request` | `SolicitarOtpRequest` |
| DTO Response | `{Entidad}Response` | `OtpResponse` |
| Excepción | `{Dominio}Exception` | `OtpExpiradoException` |
| Evento | `{Entidad}{Accion}Event` | `OtpValidadoEvent` |

### 1.3 Prefijos y Sufijos

| Uso | Prefijo/Sufijo | Ejemplo | Cuándo Usar |
|-----|----------------|---------|-------------|
| Interfaces | Sin prefijo | `PuertoOTPBanco` | Siempre (estilo Hexagonal) |
| Implementaciones | Prefijo tecnología | `RabbitOtpAdapter` | Adaptadores de infraestructura |
| Test classes | `Test` sufijo | `RetiroServiceTest` | Siempre para tests |
| Mocks | `Mock` prefijo | `MockPuertoOTPBanco` | En tests manuales |

---

## 2. Arquitectura

### 2.1 Estilo Arquitectónico

**Patrón Principal:** Hexagonal (Ports & Adapters)

El dominio está en el centro, completamente aislado de frameworks y tecnologías externas. Los puertos definen las interfaces que el dominio necesita, y los adaptadores implementan esas interfaces con tecnologías específicas.

### 2.2 Estructura de Carpetas/Paquetes

```
co.com.bmm.retiros/
├── dominio/
│   ├── modelo/          # Entidades, Value Objects, Aggregates
│   ├── puertos/         # Interfaces (ports) - entrada y salida
│   ├── servicios/       # Servicios de dominio
│   └── excepciones/     # Excepciones de dominio
├── aplicacion/
│   ├── casos_uso/       # Use Cases / Application Services
│   ├── dto/             # DTOs de entrada/salida
│   └── mapeadores/      # Mappers (MapStruct)
└── infraestructura/
    ├── adaptadores/     # Implementaciones de puertos
    │   ├── entrada/     # Controllers, Listeners RabbitMQ
    │   └── salida/      # Repositories, Clients externos
    └── configuracion/   # Spring Config, Beans, Properties
```

### 2.3 Reglas de Dependencia

```
Infrastructure → Application → Domain
      ↓              ↓           ↓
   (adapters)    (use cases)  (pure logic)
```

**Regla:** ESTRICTA - Las dependencias solo fluyen hacia adentro

| Capa | Puede Importar | NO Puede Importar |
|------|----------------|-------------------|
| Domain | Nada externo (solo Java SE) | Application, Infrastructure, Spring |
| Application | Domain | Infrastructure, Controllers |
| Infrastructure | Domain, Application | - |

### 2.4 Domain-Driven Design

**Nivel de DDD:** Táctico Completo

| Táctica DDD | Uso | Descripción |
|-------------|-----|-------------|
| Aggregates | ✅ Obligatorio | `Retiro` como aggregate root, controla consistencia |
| Value Objects | ✅ Obligatorio | `MontoRetiro`, `CodigoOtp` - inmutables, sin identidad |
| Domain Events | ✅ Recomendado | `OtpSolicitadoEvent`, `OtpValidadoEvent` via RabbitMQ |
| Repositories | ✅ Obligatorio | Interfaces en dominio, implementación en infraestructura |
| Domain Services | ✅ Cuando necesario | Lógica que no pertenece a una sola entidad |

---

## 3. Patrones de Diseño

### 3.1 Patrones Obligatorios

| Patrón | Cuándo Usar | Ejemplo de Aplicación |
|--------|-------------|----------------------|
| Repository | Acceso a datos/cache | `RepositorioRetiro` (puerto) → `RedisRetiroRepository` (adapter) |
| Adapter | Integración con servicios externos | `InfobipOtpAdapter`, `BancoOtpAdapter` |
| Factory | Creación de aggregates complejos | `RetiroFactory.crearRetiro()` |
| Builder | Objetos con más de 3 parámetros | `OtpSolicitud.builder().codigo().expiracion().build()` |
| Strategy | Algoritmos intercambiables | Estrategias de validación OTP (banco vs Infobip) |
| Circuit Breaker | Llamadas a servicios externos | Resilience4j para Infobip y servicios del banco |

### 3.2 Patrones Prohibidos

| Patrón | Razón | Alternativa |
|--------|-------|-------------|
| Service Locator | Anti-pattern, dificulta testing y oculta dependencias | Inyección de dependencias con Spring |
| God Object | Viola SRP, difícil de mantener y testear | Dividir en clases con responsabilidad única |
| Anemic Domain Model | Dominio sin comportamiento, lógica dispersa | Rich Domain Model con comportamiento en entidades |
| Singleton manual | Estado global, dificulta testing | Spring Beans con scope apropiado |

### 3.3 Guía de Selección de Patrones

| Situación | Patrón Recomendado | Justificación |
|-----------|-------------------|---------------|
| Creación de objetos complejos (>3 params) | Builder | Código legible, inmutabilidad |
| Múltiples algoritmos intercambiables | Strategy | Open/Closed principle |
| Acceso a datos externos | Repository | Abstracción de persistencia |
| Llamadas a servicios externos | Adapter + Circuit Breaker | Aislamiento + Resiliencia |
| Notificación de cambios | Domain Events | Desacoplamiento entre módulos |

---

## 4. Principios y Paradigmas

### 4.1 Principios SOLID

**Nivel de aplicación:** Estricto (todos obligatorios)

| Principio | Obligatorio | Guía de Aplicación |
|-----------|-------------|-------------------|
| **S**ingle Responsibility | ✅ | Una clase = una razón para cambiar |
| **O**pen/Closed | ✅ | Abierto a extensión vía puertos/adaptadores |
| **L**iskov Substitution | ✅ | Adaptadores intercambiables sin romper contratos |
| **I**nterface Segregation | ✅ | Puertos pequeños y específicos |
| **D**ependency Inversion | ✅ | Dominio define interfaces, infraestructura implementa |

### 4.2 Principios Adicionales

| Principio | Aplicación |
|-----------|------------|
| DRY | Lógica común en servicios de dominio o utilidades compartidas |
| KISS | Soluciones simples primero, complejidad solo cuando se justifica |
| YAGNI | No implementar funcionalidad especulativa o "por si acaso" |

### 4.3 Inmutabilidad

**Política:** Inmutabilidad por defecto

- ✅ Usar `final` en campos de entidades y value objects
- ✅ Preferir Records para DTOs y Value Objects
- ✅ Value Objects siempre inmutables
- ✅ Colecciones inmutables donde sea posible (`List.of()`, `Set.of()`)
- ✅ Retornar copias defensivas de colecciones

### 4.4 Manejo de Null

**Política:** Prohibir null - usar `Optional<T>`

| Situación | Manejo Requerido |
|-----------|------------------|
| Retorno de métodos | `Optional<T>` para valores que pueden no existir |
| Parámetros opcionales | Sobrecarga de métodos o patrón Builder |
| Campos opcionales | `Optional<T>` con `@JsonInclude(NON_ABSENT)` |
| Validación | `Objects.requireNonNull()` en constructores |

### 4.5 Paradigma

**Paradigma predominante:** Híbrido (OOP estructura + Funcional lógica)

| Aspecto | Enfoque |
|---------|---------|
| Estructura | OOP - clases, interfaces, encapsulamiento |
| Lógica de negocio | OOP - comportamiento en entidades de dominio |
| Transformaciones de datos | Funcional - streams, lambdas, Optional |

### 4.6 Composición vs Herencia

**Política:** Composición preferida (herencia permitida solo justificada)

- ✅ **Usar herencia cuando:** Framework lo requiere (ej: `extends RuntimeException`)
- ✅ **Usar herencia cuando:** Relación "es-un" verdadera y clara
- ❌ **Evitar herencia cuando:** Solo para reutilizar código
- ❌ **Evitar herencia cuando:** Más de 2 niveles de profundidad

---

## 5. Dependencias

### 5.1 Dependencias Aprobadas

#### Testing
| Librería | Versión Mínima | Uso |
|----------|----------------|-----|
| JUnit 5 | 5.10+ | Framework de testing |
| Mockito | 5.x | Mocks y stubs |
| AssertJ | 3.24+ | Aserciones fluidas |
| ArchUnit | 1.3+ | Tests de arquitectura hexagonal |
| Testcontainers | 1.19+ | Tests integración Redis/RabbitMQ |
| WireMock | 3.x | Mocks de APIs externas (Infobip) |

#### Logging
| Librería | Versión | Uso |
|----------|---------|-----|
| SLF4J | 2.x | Facade de logging |
| Logback | 1.4+ | Implementación (Spring Boot default) |

#### Mapping y Utilidades
| Librería | Versión | Uso |
|----------|---------|-----|
| MapStruct | 1.6+ | Mapeo entre DTOs y entidades |
| Resilience4j | 2.x | Circuit breaker, retry |

### 5.2 Dependencias Prohibidas

| Librería | Razón | Alternativa |
|----------|-------|-------------|
| Lombok @Data | Genera equals/hashCode inseguros en entidades | Records o implementación manual |
| Lombok @Setter | Rompe inmutabilidad | Constructores o Builders |
| Apache Commons Lang | APIs nativas de Java 21 son suficientes | `java.util`, `java.util.stream` |
| Gson | Inconsistente con Jackson de Spring Boot | Jackson (default de Spring) |
| Guava | Mayoría de utilidades en Java 21 | APIs nativas de Java |

### 5.3 Política de Actualizaciones

**Estrategia:** Versiones LTS preferidas

- Actualizar dependencias de seguridad: **inmediatamente**
- Dependencias menores (patch): mensualmente
- Dependencias mayores (breaking): evaluar en sprint dedicado
- Spring Boot: seguir versiones LTS (3.2.x, 3.5.x)

---

## 6. Testing

### 6.1 Metodología

**Enfoque principal:** TDD Flexible (test junto al código)

- Escribir tests antes o durante la implementación
- Ciclo Red-Green-Refactor recomendado
- No se permite código en dominio sin tests

### 6.2 Cobertura

| Capa | Cobertura Mínima | Tipo de Tests |
|------|------------------|---------------|
| Domain | 90%+ | Unitarios puros (sin mocks de infra) |
| Application | 80%+ | Unitarios + Integración con mocks |
| Infrastructure | 70%+ | Integración con Testcontainers |

### 6.3 Convención de Nombres

**Patrón:** `should_{resultado}_when_{condicion}`

```java
@Test
void should_validarOtp_when_codigoEsValido() {
    // Given - Arrange
    // When - Act
    // Then - Assert
}

@Test
void should_lanzarOtpExpiradoException_when_otpHaExpirado() { }

@Test
void should_enviarSmsExitosamente_when_infobipRespondeOk() { }
```

### 6.4 Tests de Integración

**Tecnología:** Testcontainers

```java
@Testcontainers
class RedisRetiroRepositoryIntegrationTest {
    
    @Container
    static GenericContainer<?> redis = new GenericContainer<>("redis:7-alpine")
        .withExposedPorts(6379);
}
```

| Servicio | Container |
|----------|-----------|
| Redis | `redis:7-alpine` |
| RabbitMQ | `rabbitmq:3-management-alpine` |
| APIs externas | WireMock (mock server) |

### 6.5 Tests de Arquitectura

**Obligatorio:** ArchUnit para validar reglas hexagonales

```java
@AnalyzeClasses(packages = "co.com.bmm.retiros")
class ArchitectureTest {

    @ArchTest
    static final ArchRule dominio_no_depende_de_infraestructura =
        noClasses()
            .that().resideInAPackage("..dominio..")
            .should().dependOnClassesThat()
            .resideInAPackage("..infraestructura..");

    @ArchTest
    static final ArchRule dominio_no_depende_de_spring =
        noClasses()
            .that().resideInAPackage("..dominio..")
            .should().dependOnClassesThat()
            .resideInAPackage("org.springframework..");
}
```

---

## 7. Documentación

### 7.1 Documentación de Código

**Obligatoria en:**
- ✅ Clases/Interfaces públicas (JavaDoc con propósito)
- ✅ Métodos públicos de puertos y servicios
- ✅ Métodos complejos (>10 líneas o algoritmos no triviales)
- ✅ Excepciones y casos especiales

**Formato JavaDoc:**
```java
/**
 * Valida un código OTP contra el almacenado en Redis.
 *
 * @param solicitud datos de la solicitud de validación
 * @return resultado de la validación con estado y mensaje
 * @throws OtpExpiradoException si el OTP ha superado el TTL
 * @throws OtpInvalidoException si el código no coincide
 */
public ResultadoValidacion validarOtp(SolicitudValidacion solicitud) { }
```

### 7.2 Decisiones Arquitectónicas

**Formato:** ADR (Architecture Decision Records) - MADR

**Ubicación:** `.SAC/artifacts/ADR/`

**Cuándo crear ADR:**
- Cambios en patrones arquitectónicos
- Nuevas integraciones externas
- Decisiones de tecnología significativas
- Trade-offs importantes

---

## 8. Seguridad y Calidad

### 8.1 Datos Sensibles en Logs

**Política:** NUNCA loguear datos sensibles

| ⛔ PROHIBIDO | ✅ PERMITIDO |
|-------------|--------------|
| Códigos OTP | `"OTP enviado correctamente"` |
| Passwords | `"Autenticación exitosa para usuario [ID]"` |
| Tokens/API Keys | `"Llamada a Infobip completada"` |
| PII (nombre, cédula, teléfono) | `"Procesando solicitud [requestId]"` |
| Números de cuenta | `"Retiro procesado [transactionId]"` |

```java
// ❌ MAL
log.info("OTP generado: {} para usuario: {}", codigoOtp, telefono);

// ✅ BIEN
log.info("OTP generado exitosamente [requestId={}]", requestId);
```

### 8.2 Validación de Entradas

**Política:** Obligatoria en todos los puntos de entrada

| Capa | Mecanismo |
|------|-----------|
| Controllers | `@Valid`, `@NotNull`, `@Size`, `@Pattern` |
| Listeners RabbitMQ | Validación en deserialización + dominio |
| Casos de uso | Validaciones de negocio en dominio |
| Dominio | Validación en constructores de entidades/VOs |

### 8.3 Límites de Código

| Métrica | Límite | Herramienta |
|---------|--------|-------------|
| Líneas por método | ≤ 25 | SonarQube |
| Líneas por clase | ≤ 300 | SonarQube |
| Parámetros por método | ≤ 4 | SonarQube (usar objetos si más) |
| Complejidad ciclomática | ≤ 10 | SonarQube |
| Profundidad de herencia | ≤ 2 | ArchUnit |

### 8.4 Análisis Estático

**Herramienta:** SonarQube (obligatorio)

- Quality Gate debe pasar antes de merge a main
- Zero bugs y vulnerabilidades bloqueantes
- Deuda técnica máxima: 1 día por sprint
- Code smells: resolver en siguiente sprint

---

## 9. Checklist de Validación

### Pre-Commit Checklist

```markdown
## Verificación antes de commit

### Nomenclatura
- [ ] Clases en PascalCase
- [ ] Métodos y variables en camelCase
- [ ] Constantes en UPPER_SNAKE_CASE
- [ ] Puertos sin prefijo "I"
- [ ] Adaptadores con prefijo de tecnología

### Arquitectura
- [ ] Dominio NO importa infraestructura ni Spring
- [ ] Application NO importa infraestructura
- [ ] Nuevos puertos definidos en dominio
- [ ] Implementaciones en infraestructura/adaptadores

### Código
- [ ] Campos con `final` donde corresponde
- [ ] Sin uso de `null` (usar Optional)
- [ ] Sin datos sensibles en logs
- [ ] Validaciones en puntos de entrada

### Testing
- [ ] Tests unitarios para lógica nueva
- [ ] Cobertura ≥ umbral de la capa
- [ ] Tests de arquitectura pasan
- [ ] Nombres siguen patrón should_when

### Documentación
- [ ] JavaDoc en clases/métodos públicos
- [ ] ADR si hay decisión arquitectónica
```

### Pre-Merge Checklist

```markdown
## Verificación antes de merge a main

- [ ] Pipeline CI verde
- [ ] Quality Gate de SonarQube aprobado
- [ ] Code review aprobado
- [ ] Tests de integración pasan
- [ ] Sin TODOs sin ticket asociado
```

---

✅ Aprobado por **JavierMaldonado** | 📅 2026-02-15

---
