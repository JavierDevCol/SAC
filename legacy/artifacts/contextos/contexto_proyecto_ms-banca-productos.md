# Contexto del Proyecto: ms-banca-productos

> **Generado:** 2026-02-15  
> **Confianza:** Alto

---

## 📊 Scorecard Ejecutivo

| Aspecto | Puntuación | Estado |
|---------|------------|--------|
| Arquitectura | 9/10 | ✅ Hexagonal + DDD |
| Stack | 9/10 | ✅ Java 21, Spring Boot 3.5.4 |
| Testing | 7/10 | ⚠️ Tests presentes |
| DevOps | 9/10 | ✅ CI/CD completo + K8s |
| Documentación | 5/10 | ⚠️ README básico |

---

## 1. Identificación

- **Nombre:** ms-banca-productos (MSBancaProductos)
- **Descripción:** Microservicio para consulta de productos bancarios del cliente.
- **Tipo:** Microservicio
- **Estado:** Producción
- **Group ID:** co.com.bmm

---

## 2. Stack Tecnológico

### Resumen
| Categoría | Tecnología | Versión |
|-----------|------------|---------|
| Lenguaje | Java | 21 |
| Framework | Spring Boot | 3.5.4 |
| Spring | Spring Framework | 6.2.11 |
| Build | Gradle | 8.x |
| Mensajería | RabbitMQ | - |
| Cache | Redis | - |
| Mapping | MapStruct | 1.6.3 |
| API Docs | SpringDoc OpenAPI | 2.3.0 |
| Testing | JUnit 5, Mockito | 3.12.4 |

### Dependencias Core
| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| spring-boot-starter-web | 3.5.4 | REST API (Undertow) |
| spring-boot-starter-amqp | 3.5.4 | RabbitMQ |
| spring-boot-starter-data-redis | 3.5.4 | Cache Redis |
| mapstruct | 1.6.3 | Object mapping |
| libBancaTransversales | 1.0.8 | Cliente servicios BMM |
| archunit-junit5 | 1.3.0 | Tests arquitectura |

---

## 3. Comandos Clave

```bash
# Build
cd microservicio && ./gradlew clean build

# Tests
./gradlew test

# Docker local
docker-compose up -d

# Ejecutar
./gradlew bootRun
```

---

## 4. Arquitectura

- **Estilo:** Hexagonal (Ports and Adapters)
- **Patrón Principal:** DDD Táctico + Repository

### Estructura del Proyecto
```
ms-banca-productos/
├── microservicio/
│   ├── dominio/src/main/java/co/com/bmm/
│   │   ├── modelo/                 # Entidades de dominio
│   │   ├── puertos/                # Interfaces (ports)
│   │   ├── servicios/              # Servicios de dominio
│   │   └── util/                   # Utilidades
│   ├── aplicacion/                 # Use cases
│   ├── infraestructura/            # Adapters
│   └── src/                        # Main app
├── comun/                          # Módulos compartidos locales
├── Dockerfile
├── deployment.yaml
└── docker-compose.yml
```

### Componentes Principales
| Componente | Ubicación | Responsabilidad |
|------------|-----------|-----------------|
| Modelos | dominio/modelo/ | Entidades de productos |
| Puertos | dominio/puertos/ | Interfaces de dominio |
| Servicios | dominio/servicios/ | Lógica de negocio |
| Application | src/ | Punto de entrada Spring Boot |

---

## 5. Integraciones

| Tipo | Tecnología | Configuración |
|------|------------|---------------|
| BD Principal | N/A | Sin persistencia local |
| Cache | Redis | spring-boot-starter-data-redis |
| Mensajería | RabbitMQ | AMQP |
| Servicios BMM | HTTP | libBancaTransversales |
| Secretos | HashiCorp Vault | VAULT_* env vars |

---

## 6. DevOps

| Aspecto | Estado | Archivo |
|---------|--------|---------|
| Dockerfile | ✅ | Dockerfile |
| Docker Compose | ✅ | docker-compose.yml |
| CI/CD | ✅ | azure-pipelines.yml |
| IaC | ✅ | deployment.yaml (K8s) |

**Puertos:** 8080  
**Profiles:** develop, prepro, pro

---

## 7. Convenciones

### Código
| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Clases | PascalCase | ConsultaProductos |
| Métodos | camelCase | obtenerProductos() |
| Paquetes | lowercase | modelo, puertos |

### Proyecto
- **Commits:** Conventional Commits
- **Branching:** GitFlow
- **Estructura:** Por capa (dominio, aplicacion, infraestructura)

---

## 8. Puntos de Atención

### 🟢 Sugerencias
- Documentar contratos de productos con ADR
- Agregar cache layer para productos frecuentes

---

## 📜 Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| 2026-02-15 | Análisis inicial | Generado por >tomar_contexto |

---

> **Archivo generado automáticamente.**  
> **Proyecto:** ms-banca-productos  
> **Workspace:** bmm

