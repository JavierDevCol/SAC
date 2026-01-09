# Reglas de Detección: Java / JVM

```yaml
descripcion: "Detección de stack en proyectos Java"
archivos: ["pom.xml", "build.gradle", "build.gradle.kts"]

# =============================================================================
# VERSIÓN
# =============================================================================
version:
  maven: "properties > java.version | maven.compiler.source"
  gradle: "sourceCompatibility | java.toolchain.languageVersion"

# =============================================================================
# FRAMEWORKS
# =============================================================================
frameworks:
  spring_boot:
    detectar: "spring-boot-starter-parent | org.springframework.boot plugin"
    comandos: { build: "mvn package | gradle build", run: "mvn spring-boot:run | gradle bootRun", test: "mvn test | gradle test" }
  quarkus:
    detectar: "quarkus-bom | io.quarkus plugin"
    comandos: { build: "mvn package", run: "mvn quarkus:dev", test: "mvn test" }
  micronaut:
    detectar: "micronaut-parent | io.micronaut.application plugin"

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias:
  web: ["spring-boot-starter-web", "spring-boot-starter-webflux"]
  persistencia: ["spring-boot-starter-data-jpa", "spring-boot-starter-data-mongodb"]
  seguridad: ["spring-boot-starter-security", "spring-boot-starter-oauth2-*"]
  mensajeria: ["spring-kafka", "spring-boot-starter-amqp"]
  utilidades: ["lombok", "mapstruct", "modelmapper"]

# =============================================================================
# TESTING
# =============================================================================
testing:
  frameworks: ["junit-jupiter", "mockito-core", "spring-boot-starter-test"]
  integracion: ["testcontainers", "wiremock"]
  arquitectura: ["archunit"]

# =============================================================================
# CONVENCIONES
# =============================================================================
convenciones:
  estructura: "src/main/java, src/test/java, src/main/resources"
  paquetes: "com.empresa.proyecto.{domain,application,infrastructure}"
  naming: "PascalCase clases, camelCase métodos, UPPER_SNAKE constantes"
      mapstruct:
        patron: "org.mapstruct:mapstruct"
        significa: "Mapeo automático entre DTOs y entidades"
      modelmapper:
        patron: "org.modelmapper:modelmapper"
        significa: "Mapeo de objetos"
      jackson:
        patron: "com.fasterxml.jackson"
        significa: "Serialización JSON"
      openapi:
        patron: "org.springdoc:springdoc-openapi | io.swagger"
        significa: "Documentación API (Swagger/OpenAPI)"
  
  testing:
    junit5:
      patron: "org.junit.jupiter:junit-jupiter"
      significa: "Framework de testing principal"
    mockito:
      patron: "org.mockito:mockito-core | org.mockito:mockito-junit-jupiter"
      significa: "Mocking de dependencias"
    spring_test:
      patron: "spring-boot-starter-test"
      significa: "Testing de integración Spring"
      incluye: ["JUnit 5", "Mockito", "AssertJ", "Hamcrest", "JSONPath"]
    testcontainers:
      patron: "org.testcontainers:testcontainers"
      significa: "Contenedores para tests de integración"
    archunit:
      patron: "com.tngtech.archunit:archunit"
      significa: "Testing de arquitectura"
    wiremock:
      patron: "com.github.tomakehurst:wiremock"
      significa: "Mock de servicios HTTP externos"
    rest_assured:
      patron: "io.rest-assured:rest-assured"
      significa: "Testing de APIs REST"
  
  build_tool:
    nombre: "Maven"
    comandos:
      build: "mvn clean package"
      build_skip_tests: "mvn clean package -DskipTests"
      test: "mvn test"
      test_integration: "mvn verify"
      run: "mvn spring-boot:run"
      dependency_tree: "mvn dependency:tree"

# =============================================================================
# GRADLE
# =============================================================================
gradle:
  archivos: ["build.gradle", "build.gradle.kts"]
  
  version_lenguaje:
    groovy:
      buscar_en: "sourceCompatibility"
      ejemplo: "sourceCompatibility = '17'"
    kotlin_dsl:
      buscar_en: "java { toolchain { languageVersion } }"
      ejemplo: |
        java {
            toolchain {
                languageVersion.set(JavaLanguageVersion.of(17))
            }
        }
  
  framework:
    spring_boot:
      detectar: "plugins contiene 'org.springframework.boot'"
      version: "extraer de id 'org.springframework.boot' version 'X.X.X'"
      ejemplo_groovy: |
        plugins {
            id 'org.springframework.boot' version '3.2.0'
            id 'io.spring.dependency-management' version '1.1.4'
        }
      ejemplo_kotlin: |
        plugins {
            id("org.springframework.boot") version "3.2.0"
            id("io.spring.dependency-management") version "1.1.4"
        }
    
    quarkus:
      detectar: "plugins contiene 'io.quarkus'"
    
    micronaut:
      detectar: "plugins contiene 'io.micronaut.application'"
  
  dependencias_clave:
    buscar_en: "dependencies { }"
    patron_groovy: "implementation 'grupo:artefacto:version'"
    patron_kotlin: "implementation(\"grupo:artefacto:version\")"
    nota: "Mismas dependencias que Maven, diferente sintaxis"
  
  testing:
    buscar_en: "dependencies { testImplementation }"
    patron_groovy: "testImplementation 'grupo:artefacto'"
    patron_kotlin: "testImplementation(\"grupo:artefacto\")"
  
  build_tool:
    nombre: "Gradle"
    detectar_wrapper: "./gradlew o gradlew.bat"
    comandos:
      build: "./gradlew build"
      build_skip_tests: "./gradlew build -x test"
      test: "./gradlew test"
      run: "./gradlew bootRun"
      dependencies: "./gradlew dependencies"

# =============================================================================
# PATRONES ARQUITECTÓNICOS COMUNES EN JAVA
# =============================================================================
patrones_sugeridos:
  spring_boot:
    por_defecto:
      - "Controller → Service → Repository"
      - "DTOs para entrada/salida de APIs"
      - "Entities para persistencia"
    avanzados:
      - "Hexagonal: ports/adapters"
      - "CQRS con CommandHandler/QueryHandler"
      - "Event Sourcing con Spring Events o Axon"
  
  quarkus:
    por_defecto:
      - "JAX-RS Resources"
      - "CDI para inyección"
      - "Panache para persistencia"

# =============================================================================
# CONVENCIONES DEL ECOSISTEMA
# =============================================================================
convenciones:
  estructura_carpetas:
    maven_standard:
      - "src/main/java → Código fuente"
      - "src/main/resources → Configuración y recursos"
      - "src/test/java → Tests"
      - "src/test/resources → Recursos de test"
  
  archivos_configuracion:
    spring_boot:
      - "application.yml | application.properties → Configuración principal"
      - "application-{profile}.yml → Configuración por ambiente"
      - "bootstrap.yml → Configuración temprana (Cloud Config)"
  
  naming:
    clases: "PascalCase (UserService, OrderController)"
    metodos: "camelCase (findById, createUser)"
    constantes: "UPPER_SNAKE_CASE (MAX_RETRY_COUNT)"
    paquetes: "lowercase (com.empresa.proyecto.dominio)"
```
