# Contexto del Proyecto: comun-svc-lib

> **Generado:** 2026-02-15  
> **Confianza:** Alto

---

## 📊 Scorecard Ejecutivo

| Aspecto | Puntuación | Estado |
|---------|------------|--------|
| Arquitectura | 8/10 | ✅ Librería bien estructurada |
| Stack | 9/10 | ✅ Java 21, módulos JPMS |
| Testing | 7/10 | ⚠️ Tests básicos |
| DevOps | 9/10 | ✅ CI/CD con versionado automático |
| Documentación | 6/10 | ⚠️ README presente |

---

## 1. Identificación

- **Nombre:** libBancaTransversales (comun-svc-lib)
- **Descripción:** Librería compartida con utilidades comunes para todos los microservicios de la banca.
- **Tipo:** Librería Java
- **Estado:** Producción
- **Artifact ID:** libBancaTransversales
- **Group ID:** com.bmm.banca

---

## 2. Stack Tecnológico

### Resumen
| Categoría | Tecnología | Versión |
|-----------|------------|---------|
| Lenguaje | Java | 21 |
| Build | Gradle | 8.x |
| Testing | JUnit Jupiter | 5.11.3 |
| JSON | Jackson | 2.17.0 |
| Crypto | Nimbus JOSE+JWT | - |
| SBOM | CycloneDX | 2.3.0 |
| Mutación | Pitest | 1.15.0 |

### Dependencias Core
| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| jackson-databind | 2.17.0 | Serialización JSON |
| jackson-datatype-jsr310 | 2.17.0 | Soporte Java Time |
| nimbus-jose-jwt | - | JWE/JWT handling |
| guava | 33.3.1-jre | Utilidades Google |
| commons-math3 | 3.6.1 | Matemáticas |

### Herramientas de Desarrollo
| Herramienta | Propósito | Config |
|-------------|-----------|--------|
| JaCoCo | Cobertura de código | build.gradle |
| Pitest | Testing de mutación | build.gradle |
| CycloneDX | Generación SBOM | build.gradle |

---

## 3. Comandos Clave

```bash
# Build
./gradlew clean build

# Tests
./gradlew test

# Publicar a Azure Artifacts
./gradlew publish -PciVersion=X.Y.Z

# Generar SBOM
./gradlew cyclonedxBom
```

---

## 4. Arquitectura

- **Estilo:** Librería modular con JPMS
- **Patrón Principal:** Cliente HTTP con Factory

### Estructura del Proyecto
```
comun-svc-lib/
├── src/main/java/com/bmm/banca/busservicios/
│   ├── ClienteBmmBusServicios.java      # Cliente principal
│   ├── ClienteBmmBusServiciosFabrica.java # Factory
│   ├── cliente/                          # Implementaciones cliente
│   ├── configuracion/                    # Configuración
│   ├── excepciones/                      # Excepciones custom
│   ├── internal/                         # Utilidades internas
│   ├── modelo/                           # DTOs y modelos
│   └── util/                             # Utilidades
├── module-info.java                      # Módulo JPMS
└── build.gradle
```

### Componentes Principales
| Componente | Ubicación | Responsabilidad |
|------------|-----------|-----------------|
| ClienteBmmBusServicios | busservicios/ | Cliente HTTP para servicios BMM |
| ClienteBmmBusServiciosFabrica | busservicios/ | Factory para crear clientes |
| Modelos | modelo/ | DTOs para comunicación |
| Excepciones | excepciones/ | Excepciones de dominio |

---

## 5. Integraciones

| Tipo | Tecnología | Configuración |
|------|------------|---------------|
| Registry | Azure Artifacts | Maven feed |
| CI/CD | Azure Pipelines | azure-pipelines.yml |

---

## 6. DevOps

| Aspecto | Estado | Archivo |
|---------|--------|---------|
| Dockerfile | ❌ | N/A (librería) |
| Docker Compose | ❌ | N/A |
| CI/CD | ✅ | azure-pipelines.yml |
| IaC | ❌ | N/A |

**Publicación:** Azure Artifacts Feed `libBancaTransversales`  
**Versionado:** Automático basado en Azure Artifacts (scripts/generate-version.ps1)

---

## 7. Convenciones

### Código
| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Clases/Tipos | PascalCase | ClienteBmmBusServicios |
| Métodos | camelCase | obtenerCliente() |
| Variables | camelCase | tokenAcceso |
| Constantes | UPPER_SNAKE | MAX_RETRY_COUNT |

### Proyecto
- **Commits:** Conventional Commits
- **Branching:** GitFlow (main, develop)
- **Módulos:** JPMS (module-info.java)

---

## 8. Puntos de Atención

### 🟠 Importantes
- Librería crítica: cambios afectan todos los microservicios
- Versionado semántico importante para compatibilidad

### 🟢 Sugerencias
- Documentar API pública con Javadoc
- Aumentar cobertura de tests de mutación

---

## 9. Artefactos Relacionados

| Artefacto | Ubicación | Estado | Fecha |
|-----------|-----------|--------|-------|
| Reglas Arquitectónicas | .SAC/artifacts/reglas_arquitectonicas.md | ⏳ Pendiente | - |
| Backlog | .SAC/artifacts/backlog_desarrollo.md | ⏳ Pendiente | - |
| ADRs | .SAC/artifacts/ADR/ | ⏳ Pendiente | - |

> 💡 Para configurar reglas arquitectónicas: `>init_reglas_arquitectonicas`

---

## 📜 Historial

| Fecha | Acción | Detalle |
|-------|--------|---------|
| 2026-02-15 | Análisis inicial | Generado por >tomar_contexto |

---

> **Archivo generado automáticamente.**  
> **Proyecto:** comun-svc-lib  
> **Workspace:** bmm

