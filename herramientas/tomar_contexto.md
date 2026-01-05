# 🛠️ Herramienta: Tomar Contexto

> **Versión:** 2.0  
> **Fecha de Actualización:** 10 de octubre de 2025  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `tomar_contexto`

---

## 🎯 Objetivo

Realizar un análisis profundo y automatizado de un proyecto de software para extraer información técnica, arquitectónica y contextual, generando un archivo `{{contexto_proyecto_location}}` que sirve como base de conocimiento reutilizable para otras herramientas del sistema y facilita la comprensión rápida del proyecto en futuras sesiones.

---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

*Esta herramienta funciona de manera independiente y no invoca otras herramientas del sistema.*

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **`diagnosticar_devops`** | Al inicio del diagnóstico DevOps | Obtener contexto del proyecto para análisis contextualizado |
| **`define_arquitectura`** | Al evaluar arquitecturas | Usar patrones detectados para documentación arquitectónica |
| **`analizar_code_smells`** | Antes de analizar código | Aplicar reglas específicas del stack tecnológico detectado |
| **`refinar_hu`** | Al refinar historias de usuario | Obtener contexto arquitectónico para estimaciones precisas |
| **`solucionar_smells`** | Durante refactoring | Obtener contexto del proyecto para decisiones de refactoring apropiadas |
| **`verifica_pruebas`** | Al validar pruebas | Adaptar estrategias de testing al stack detectado |
| **`crear_pruebas`** | Al generar tests | Generar tests apropiados para el framework identificado |
| **`generar_commit`** | Al crear mensajes de commit | Mejorar scope y contexto basado en componentes del proyecto |

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Acceso a la estructura de directorios del proyecto de software
- Permisos de lectura en la raíz del proyecto y subcarpetas principales

**Secundario (Opcional):**
- Archivo README.md existente (si está presente)
- Archivos de configuración específicos del stack (application.properties, .env, config files)
- Documentación técnica adicional (docs/, wiki/, CHANGELOG.md)
- Archivos de deployment y containerización (Dockerfile, docker-compose.yml, K8s manifests)
- Configuración de CI/CD (.github/workflows, .gitlab-ci.yml, Jenkinsfile)
- Licencias y metadatos del proyecto (LICENSE, CONTRIBUTING.md, package info)

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `profundidad_analisis` | string | basico\|completo\|exhaustivo | completo | Nivel de detalle del análisis del proyecto |
| `incluir_dependencias` | boolean | true\|false | true | Analizar dependencias y frameworks detectados |
| `generar_readme` | string | auto\|siempre\|nunca | auto | Crear o actualizar README.md si es necesario |
| `actualizar_existente` | boolean | true\|false | false | Sobrescribir archivo contexto_proyecto.md existente |
| `incluir_devops` | boolean | true\|false | true | Analizar archivos de CI/CD y containerización |
| `detectar_patrones` | boolean | true\|false | true | Identificar patrones arquitectónicos y de diseño |
| `ruta_contexto` | string | path | artefactos/contexto_proyecto.md | Ubicación del archivo de contexto a generar |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (uso principal - necesita contexto del proyecto para todas sus funciones)
- ✅ **Arquitecto Onad** (análisis estratégico y comprensión de proyectos nuevos)
- ✅ **Arquitecto DevOps** (contexto de infraestructura para diagnósticos y optimizaciones)
- ✅ **Refinador HU** (comprensión del dominio y componentes para refinamiento)
- ✅ **Artesano de Commits** (contexto del proyecto para commits más precisos)

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Configuración Inicial y Validación

- **Verificar permisos y acceso al proyecto:**
  - Confirmar acceso de lectura a la raíz del proyecto
  - Verificar si existe archivo `{{contexto_proyecto_location}}` previo
  - Si existe y `actualizar_existente=false`, preguntar al usuario si desea actualizar o preservar

- **Preparar estructura de artefactos:**
  - Crear carpeta de {{artifacts_location}} si no existe (según `{{output_folder}}`)
  - Inicializar estructura base del archivo de contexto
  - Configurar parámetros según la configuración del usuario

### 2️⃣ Análisis Estático del Ecosistema (Bottom-Up)

- **Identificación del stack tecnológico:**
  - **Buscar gestores de dependencias en orden de prioridad:**
    - `pom.xml` → Java/Maven
    - `build.gradle` o `build.gradle.kts` → Java/Kotlin/Gradle
    - `package.json` → JavaScript/TypeScript/NPM/Yarn
    - `go.mod` → Go
    - `pyproject.toml`, `requirements.txt`, `setup.py` → Python
    - `Cargo.toml` → Rust
    - `*.csproj`, `*.sln` → .NET/C#

- **Análisis profundo de dependencias (si `incluir_dependencias=true`):**
  - **Parsear archivo de dependencias detectado:**
    - Extraer frameworks principales (Spring Boot, React, Express, Django, etc.)
    - Identificar bases de datos (PostgreSQL, MySQL, MongoDB, Redis, etc.)
    - Detectar herramientas de testing (JUnit, Jest, PyTest, etc.)
    - Listar librerías de seguridad, logging, monitoring
  
  - **Inferir comandos comunes basados en el ecosistema:**
    - Maven: `mvn clean install`, `mvn spring-boot:run`, `mvn test`
    - Gradle: `./gradlew build`, `./gradlew bootRun`, `./gradlew test`
    - NPM: `npm install`, `npm start`, `npm test`, `npm run build`
    - Python: `pip install -r requirements.txt`, `python app.py`, `pytest`

### 3️⃣ Análisis de Estructura Arquitectónica

- **Detectar patrones arquitectónicos (si `detectar_patrones=true`):**
  - **Escanear estructura de paquetes/directorios:**
    - `domain/`, `application/`, `infrastructure/` → Arquitectura Hexagonal/Clean
    - `controller/`, `service/`, `repository/`, `model/` → Arquitectura en Capas/MVC
    - `events/`, `consumer/`, `producer/`, `kafka/` → Event-Driven Architecture
    - `src/components/`, `src/pages/`, `src/hooks/` → React/Frontend patterns
    - `cmd/`, `internal/`, `pkg/` → Go standard layout
    - `views/`, `models/`, `controllers/` → MVC tradicional

- **Identificar componentes clave del sistema:**
  - **Clases/módulos principales del dominio**
  - **Puntos de entrada (controllers, handlers, main functions)**
  - **Integraciones externas (APIs, databases, message queues)**
  - **Configuración principal de la aplicación**

### 4️⃣ Análisis de DevOps e Infraestructura (si `incluir_devops=true`)

- **Detectar configuración de containerización:**
  - `Dockerfile` → Analizar imagen base, puertos expuestos, comandos
  - `docker-compose.yml` → Servicios, dependencias, networks, volumes
  - Kubernetes manifests → Deployments, services, ingress, configmaps

- **Identificar pipelines CI/CD:**
  - `.github/workflows/` → GitHub Actions
  - `.gitlab-ci.yml` → GitLab CI
  - `Jenkinsfile` → Jenkins
  - `.azure-pipelines.yml` → Azure DevOps
  - `bitbucket-pipelines.yml` → Bitbucket Pipelines

- **Analizar configuración de deployment:**
  - Scripts de deployment (`deploy.sh`, `deploy/`)
  - Configuración de environment (`env/`, `.env files`)
  - Infrastructure as Code (Terraform, CloudFormation, ARM templates)

### 5️⃣ Análisis Conceptual y Documentación (Top-Down)

- **Análisis del README.md:**
  - **Si existe, evaluar calidad y completitud:**
    - Presencia de descripción del proyecto
    - Instrucciones de instalación y ejecución
    - Documentación de APIs o funcionalidades principales
    - Información de contribución y licencias
  
  - **Clasificar README como:** Completo, Básico, Pobre, o Inexistente

- **Revisar documentación adicional:**
  - `docs/` folder → Documentación técnica
  - `CHANGELOG.md` → Historial de cambios
  - `CONTRIBUTING.md` → Guías de contribución
  - `LICENSE` → Información de licencia
  - `API.md` o `swagger.yaml` → Documentación de APIs

### 6️⃣ Síntesis y Generación del Contexto

- **Consolidar información recolectada:**
  - **Organizar datos según plantilla de `contexto_proyecto.md`:**
    - Resumen del proyecto (basado en README y análisis)
    - Stack tecnológico detectado
    - Gestión y comandos inferidos
    - Arquitectura y patrones identificados
    - Componentes clave del sistema
    - Integraciones externas detectadas
    - Configuración DevOps encontrada

- **Generar archivo `{{contexto_proyecto_location}}`:**
  - Aplicar plantilla estándar desde `{{contexto_proyecto_plantilla}}` con información recolectada
  - Incluir metadata del análisis (fecha, herramienta, parámetros)
  - Marcar secciones que requieren validación manual
  - Agregar notas sobre archivos no encontrados o información incompleta

### 7️⃣ Mejora de Documentación (si `generar_readme` permite)

- **Evaluar necesidad de README.md:**
  - **Si `generar_readme=siempre`:** Crear o actualizar README completo
  - **Si `generar_readme=auto` y README es Pobre/Inexistente:** Preguntar al usuario
  - **Si `generar_readme=nunca`:** Solo reportar estado del README actual

- **Generar README mejorado (si autorizado):**
  - Usar información del contexto para crear estructura base
  - Incluir comandos detectados automáticamente
  - Agregar secciones estándar (instalación, uso, contribución)
  - Mantener contenido existente válido si lo hay

### 8️⃣ Validación y Entrega

- **Verificar calidad del análisis:**
  - Confirmar que se detectó al menos un gestor de dependencias
  - Validar que se identificaron componentes principales
  - Verificar completitud de las secciones generadas

- **Generar reporte de análisis:**
  - Resumen de archivos analizados
  - Confianza del análisis (alta/media/baja) basada en información disponible
  - Recomendaciones para mejorar la documentación del proyecto
  - Lista de archivos que podrían proporcionar más contexto si existieran

### 9️⃣ Generación de Reglas Arquitectónicas y Confirmación

Este paso genera automáticamente el archivo `{{reglas_arquitectonicas_location}}` basándose en el análisis realizado, y solicita confirmación del usuario antes de finalizar.

#### **9.1. Generar Archivo de Reglas Arquitectónicas**

- **Crear archivo `{{reglas_arquitectonicas_location}}`** con las reglas inferidas del análisis:

**Plantilla del archivo:**

```markdown
# 📐 Reglas Arquitectónicas del Proyecto

> **Proyecto:** [Nombre del Proyecto]  
> **Generado por:** tomar_contexto  
> **Fecha de generación:** [timestamp]  
> **Basado en:** contexto_proyecto.md v[fecha]

---

## 1. Arquitectura Base

- **Estilo Arquitectónico:** [Hexagonal/Capas/MVC/Event-Driven/etc.]
- **Nivel de Adherencia Esperado:** [Estricto/Flexible]

---

## 2. Reglas de Capas y Dependencias

### 2.1. Capa de Dominio
- [ ] **NO importar** clases de infraestructura (frameworks, BD, APIs externas)
- [ ] **NO importar** clases de aplicación/casos de uso
- [ ] Solo puede contener: Entidades, Value Objects, Excepciones de Dominio, Interfaces de Puertos
- [ ] Paquetes permitidos: `[paquete.dominio]`, `[paquete.modelo]`, `[paquete.puerto]`

### 2.2. Capa de Aplicación / Casos de Uso
- [ ] **NO importar** clases de infraestructura directamente
- [ ] Puede importar: Dominio (entidades, puertos)
- [ ] Debe usar **interfaces (puertos)** para comunicarse con infraestructura
- [ ] Paquetes permitidos: `[paquete.casodeuso]`, `[paquete.aplicacion]`

### 2.3. Capa de Infraestructura
- [ ] Puede importar: Dominio, Aplicación
- [ ] Contiene implementaciones de puertos (adaptadores)
- [ ] Paquetes permitidos: `[paquete.adaptador]`, `[paquete.infraestructura]`

---

## 3. Reglas de Persistencia

### 3.1. Migraciones de Base de Datos
- [ ] **Gestor de migraciones:** [Flyway/Liquibase/Alembic/Prisma/etc.]
- [ ] **Nomenclatura obligatoria:** `V[XXX]__[descripcion_snake_case].sql`
- [ ] **NO modificar** migraciones ya ejecutadas en producción
- [ ] **Versiones incrementales** - verificar última versión antes de crear nueva
- [ ] **Incluir comentarios** descriptivos en cada migración
- [ ] **Plan de rollback** requerido para cambios destructivos (DROP)

### 3.2. Repositorios
- [ ] Interfaces de repositorio en capa de dominio (puertos)
- [ ] Implementaciones en capa de infraestructura (adaptadores)
- [ ] Usar **convención de nombres:** `[Entidad]Repository` (interfaz), `[Entidad]RepositoryImpl` o `[Entidad]Postgres` (implementación)

---

## 4. Reglas de Testing

### 4.1. Cobertura Mínima
- [ ] **Dominio:** ≥ [80]% de cobertura
- [ ] **Casos de Uso:** ≥ [75]% de cobertura
- [ ] **Adaptadores:** ≥ [60]% de cobertura

### 4.2. Tipos de Tests Requeridos
- [ ] Tests unitarios para lógica de dominio
- [ ] Tests unitarios para casos de uso (con mocks de puertos)
- [ ] Tests de integración para adaptadores de BD (usar [Testcontainers/H2/etc.])
- [ ] Tests de integración para controladores/endpoints

### 4.3. Convenciones de Nombres de Tests
- [ ] Formato: `deberia[Resultado]_Cuando[Condicion]_Entonces[Comportamiento]`
- [ ] Archivos: `[ClaseBajoTest]Test.java` o `[ClaseBajoTest].test.ts`

---

## 5. Reglas de Código

### 5.1. Convenciones de Nombres
- [ ] **Clases:** PascalCase
- [ ] **Métodos/Funciones:** camelCase
- [ ] **Constantes:** SCREAMING_SNAKE_CASE
- [ ] **Paquetes/Módulos:** lowercase con puntos o guiones según lenguaje

### 5.2. Principios SOLID
- [ ] **S** - Single Responsibility: Una clase, una responsabilidad
- [ ] **O** - Open/Closed: Abierto a extensión, cerrado a modificación
- [ ] **L** - Liskov Substitution: Subtipos sustituibles por sus tipos base
- [ ] **I** - Interface Segregation: Interfaces específicas, no generales
- [ ] **D** - Dependency Inversion: Depender de abstracciones, no de concreciones

### 5.3. Restricciones Específicas del Stack
[Reglas específicas detectadas según el stack tecnológico]
- [ ] [Regla específica 1]
- [ ] [Regla específica 2]
- [ ] [Regla específica 3]

---

## 6. Reglas de Git y Commits

- [ ] **Convención de commits:** [Conventional Commits/GitFlow/etc.]
- [ ] **Formato:** `[tipo]: [descripción breve]`
- [ ] **Tipos permitidos:** feat, fix, refactor, test, docs, chore
- [ ] **Ramas:** `feature/[ID]-[descripcion]`, `bugfix/[ID]-[descripcion]`

---

## 7. Reglas de Seguridad

- [ ] No hardcodear credenciales en código
- [ ] Usar variables de entorno para configuración sensible
- [ ] Validar todas las entradas de usuario
- [ ] Sanitizar datos antes de persistir o mostrar
- [ ] [Reglas adicionales según el proyecto]

---

## 8. Excepciones Documentadas

| Regla | Excepción | Justificación | Aprobado por |
|-------|-----------|---------------|--------------|
| [Regla X] | [Descripción de la excepción] | [Por qué se permite] | [Usuario/Fecha] |

---

## 9. Historial de Cambios

| Fecha | Acción | Descripción | Usuario |
|-------|--------|-------------|---------|
| [timestamp] | Creación | Generación inicial por tomar_contexto | Sistema |

---

**⚠️ IMPORTANTE:** Este archivo fue generado automáticamente basándose en el análisis del proyecto. 
Debe ser revisado y ajustado según las necesidades específicas del equipo.
```

#### **9.2. Adaptar Reglas al Contexto Detectado**

Basándose en la información recolectada en pasos anteriores:

1. **Detectar arquitectura** → Configurar reglas de capas apropiadas
2. **Detectar stack** → Agregar reglas específicas del lenguaje/framework
3. **Detectar gestor de migraciones** → Configurar nomenclatura correcta
4. **Detectar framework de testing** → Ajustar convenciones de tests
5. **Detectar CI/CD** → Agregar reglas de commits/branching si hay convenciones

**Ejemplos de adaptación:**

| Si se detecta... | Entonces configurar... |
|------------------|------------------------|
| Arquitectura Hexagonal | Reglas estrictas de separación dominio/infraestructura |
| Spring Boot | Reglas de @Component, @Service, @Repository |
| Flyway | Nomenclatura V[X]__descripcion.sql |
| JUnit 5 | Convención de nombres de tests Java |
| Jest | Convención de nombres .test.ts/.spec.ts |
| React | Reglas de componentes, hooks, estado |
| Conventional Commits | Tipos de commits permitidos |

#### **9.3. Solicitar Confirmación del Usuario**

**Mostrar resumen de reglas generadas:**

```markdown
---

## 📐 Reglas Arquitectónicas Generadas

He generado el archivo `{{reglas_arquitectonicas_location}}` con las siguientes reglas inferidas del análisis:

### Resumen de Reglas Detectadas:

| Categoría | Reglas Generadas | Confianza |
|-----------|------------------|-----------|
| Arquitectura | [X] reglas de capas | [Alta/Media/Baja] |
| Persistencia | [Y] reglas de migraciones | [Alta/Media/Baja] |
| Testing | [Z] reglas de cobertura | [Alta/Media/Baja] |
| Código | [W] convenciones | [Alta/Media/Baja] |
| Git | [V] reglas de commits | [Alta/Media/Baja] |

### Reglas Clave Detectadas:
1. **Arquitectura:** [Tipo detectado] con separación de capas [estricta/flexible]
2. **Migraciones:** Usar [Flyway/Liquibase/etc.] con formato [nomenclatura]
3. **Testing:** Cobertura mínima [X]% con [framework detectado]
4. **Commits:** [Convención detectada o sugerida]

---

### ⚠️ Confirmación Requerida

¿Aceptas estas reglas arquitectónicas para el proyecto?

**A) ✅ Sí, aceptar todas las reglas**
   - Se guardará el archivo tal como está
   - Las herramientas `validar-hu` y `planificar-hu` usarán estas reglas

**B) 📝 Revisar y ajustar antes de aceptar**
   - Mostraré el archivo completo para que puedas editarlo
   - Puedes agregar, modificar o eliminar reglas
   - Una vez editado, se guardará la versión final

**C) ❌ No generar reglas arquitectónicas**
   - No se creará el archivo
   - Las herramientas funcionarán sin reglas explícitas (modo flexible)

**D) 🔄 Regenerar con más contexto**
   - Puedes proporcionar información adicional sobre las reglas del proyecto
   - Se regenerará el archivo con tus indicaciones

---
```

#### **9.4. Procesar Respuesta del Usuario**

**Si elige A (Aceptar):**
1. Confirmar guardado del archivo
2. Mostrar ruta: `{{reglas_arquitectonicas_location}}`
3. Continuar con cierre normal de la herramienta

**Si elige B (Revisar):**
1. Mostrar contenido completo del archivo generado
2. Esperar ediciones del usuario
3. Guardar versión editada
4. Agregar al historial: "Editado manualmente por usuario"

**Si elige C (No generar):**
1. No crear el archivo
2. Mostrar advertencia: "⚠️ Las herramientas `validar-hu` y `planificar-hu` funcionarán sin reglas explícitas"
3. Continuar con cierre normal

**Si elige D (Regenerar):**
1. Solicitar información adicional al usuario
2. Volver al paso 9.1 con el nuevo contexto
3. Regenerar archivo con las indicaciones

#### **9.5. Finalización**

```markdown
---

✅ **Análisis de Contexto Completado**

📄 **Artefactos Generados:**
1. `artefactos/contexto_proyecto.md` - Contexto técnico del proyecto
2. `{{reglas_arquitectonicas_location}}` - Reglas arquitectónicas [si fue aceptado]

📊 **Resumen:**
- Stack: [resumen del stack]
- Arquitectura: [tipo detectado]
- Reglas: [X] reglas arquitectónicas definidas

💡 **Siguiente paso recomendado:**
- Ejecutar `refinar-hu` para crear historias de usuario alineadas con la arquitectura
- O ejecutar `analizar_code_smells` para detectar violaciones a las reglas

---
```
---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Sin permisos de lectura en el directorio del proyecto | Informar al usuario sobre permisos insuficientes y solicitar acceso o cambio de directorio |
| Proyecto vacío o sin archivos de código detectables | Generar contexto básico con estructura mínima y sugerir inicialización del proyecto |
| Múltiples gestores de dependencias detectados (ej: Maven + NPM) | Analizar ambos y marcar como proyecto polyglot, priorizando el gestor principal por tamaño |
| Archivo contexto_proyecto.md existente más reciente | Comparar timestamps y preguntar al usuario si desea actualizar o mantener la versión existente |
| Dependencias corruptas o archivos de build mal formateados | Reportar errores de parsing y generar contexto parcial con información disponible |
| Estructura de directorios no estándar o muy personalizada | Usar análisis heurístico y marcar baja confianza en detección de patrones arquitectónicos |
| Proyecto legacy sin documentación README | Generar contexto básico y ofrecer crear README desde información inferida |
| Carpeta artefactos/ no escribible o con restricciones | Solicitar ubicación alternativa o permisos de escritura |
| Proyecto muy grande (>10GB o >100K archivos) | Aplicar muestreo selectivo y análisis solo en directorios principales |
| Archivos de configuración encriptados o binarios | Reportar archivos detectados pero no analizables, sugerir proporcionar información manual |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Archivo `{{contexto_proyecto_location}}` estructurado según plantilla estándar
- Archivo `{{reglas_arquitectonicas_location}}` con reglas inferidas del análisis
- Reporte de análisis con nivel de confianza y recomendaciones

**Artefactos generados:**

| Artefacto | Ubicación | Descripción | Requiere Confirmación |
|-----------|-----------|-------------|----------------------|
| Contexto del Proyecto | `{{contexto_proyecto_location}}` | Información técnica y arquitectónica | No |
| Reglas Arquitectónicas | `{{reglas_arquitectonicas_location}}` | Restricciones y patrones obligatorios | **Sí** |
| README.md | `README.md` (raíz) | Documentación actualizada (opcional) | Sí (si aplica) |

**Estructura del archivo contexto_proyecto.md:**
```
# Contexto del Proyecto: [Nombre del Proyecto Detectado]

> **Último Análisis:** [Fecha y Hora del Análisis]
> **Analizado por:** [Herramienta y Rol ejecutor]
> **Nivel de Confianza:** [Alto/Medio/Bajo] basado en información disponible

## 1. Resumen del Proyecto
[Descripción extraída del README o inferida del análisis]

## 2. Stack Tecnológico
- **Lenguaje Principal:** [Java 17, JavaScript ES2022, Python 3.11, etc.]
- **Framework Principal:** [Spring Boot 3.1.5, React 18, Django 4.2, etc.]
- **Base de Datos:** [PostgreSQL, MongoDB, Redis, etc.]
- **Framework de Pruebas:** [JUnit 5, Jest, PyTest, etc.]
- **Contenerización:** [Docker, Podman, sin containerización]

## 3. Gestión y Comandos
- **Gestor de Dependencias:** [Maven, Gradle, NPM, pip, etc.]
- **Comandos Clave:**
  - [Comando de build]: [Descripción]
  - [Comando de ejecución]: [Descripción]
  - [Comando de testing]: [Descripción]

## 4. Arquitectura y Patrones
- **Estilo Arquitectónico:** [Hexagonal, Capas, Event-Driven, etc.]
- **Patrones Detectados:** [Repository, Strategy, Factory, etc.]
- **Nivel de Confianza:** [Alto/Medio/Bajo]

## 5. Componentes Clave
- **Clases/Módulos Principales:** [Lista de componentes core]
- **Puntos de Entrada:** [Controllers, handlers, main functions]
- **Servicios Principales:** [Business logic components]

## 6. Integraciones Externas
- **APIs Consumidas:** [External services detected]
- **Bases de Datos:** [Database connections identified]
- **Mensajería/Eventos:** [Message queues, event systems]

## 7. Configuración DevOps
- **Containerización:** [Docker setup, compose files]
- **CI/CD:** [Pipeline configurations detected]
- **Infrastructure:** [IaC files, deployment scripts]

## 8. Historial de Análisis
- **[Fecha] - tomar_contexto:** Análisis inicial del proyecto
```

**Reporte complementario de análisis:**
```
📊 Reporte de Análisis de Contexto

✅ Información Detectada:
- Gestor de dependencias: Maven (pom.xml encontrado)
- Framework principal: Spring Boot 3.1.5
- Arquitectura: Hexagonal (alta confianza)
- DevOps: Dockerfile + GitHub Actions detectados

⚠️ Información Parcial o Faltante:
- README.md: Básico (faltan secciones de instalación)
- Tests: Detectados pero sin configuración de cobertura
- Documentación API: No encontrada

💡 Recomendaciones:
- Considerar generar README.md más completo
- Revisar documentación de APIs con Swagger/OpenAPI
- Evaluar agregar configuración de code coverage

📈 Nivel de Confianza General: Alto (8/10)
- Stack tecnológico: Muy alta confianza
- Arquitectura: Alta confianza  
- DevOps: Media confianza
- Documentación: Baja confianza
```

**Artefactos adicionales generados (opcionales):**
- README.md actualizado (si autorizado por usuario)
- Lista de archivos faltantes recomendados
- Plantilla de configuración para herramientas complementarias

---

## 📚 Referencias y Notas

### Gestores de Dependencias y Ecosistemas Soportados

**Java Ecosystem:**
- **Maven:** `pom.xml` - Análisis de dependencies, plugins, profiles
- **Gradle:** `build.gradle`, `build.gradle.kts` - Tasks, configurations, Kotlin DSL
- **SBT:** `build.sbt` - Scala projects

**JavaScript/TypeScript:**
- **NPM/Yarn:** `package.json` - Scripts, dependencies, devDependencies
- **Bun:** `bun.lockb` - Modern JavaScript runtime
- **Deno:** `deno.json` - Secure TypeScript runtime

**Python:**
- **Pip:** `requirements.txt`, `pyproject.toml` - Standard Python packages
- **Poetry:** `pyproject.toml` - Modern dependency management
- **Pipenv:** `Pipfile` - Virtual environments

**Otros Ecosistemas:**
- **Go:** `go.mod` - Go modules system
- **Rust:** `Cargo.toml` - Cargo package manager
- **.NET:** `*.csproj`, `*.sln` - NuGet packages
- **Ruby:** `Gemfile` - RubyGems

### Patrones Arquitectónicos Detectables

**Arquitecturas Modernas:**
- **Hexagonal Architecture:** `domain/`, `application/`, `infrastructure/`
- **Clean Architecture:** Variaciones de hexagonal con dependency rule
- **Onion Architecture:** Capas concéntricas de dependencia

**Arquitecturas Tradicionales:**
- **MVC (Model-View-Controller):** `models/`, `views/`, `controllers/`
- **Layered Architecture:** `presentation/`, `business/`, `data/`
- **Component-Based:** React, Angular, Vue.js patterns

**Arquitecturas de Microservicios:**
- **Event-Driven:** `events/`, `consumers/`, `producers/`
- **API Gateway:** Gateway patterns y routing
- **Service Mesh:** Istio, Linkerd configurations

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `diagnosticar_devops` - Consume el contexto para análisis DevOps contextualizados
- `define_arquitectura` - Usa patrones detectados para documentación arquitectónica
- `verifica_pruebas` - Adapta estrategias de testing al stack detectado
- `crear_pruebas` - Genera tests apropiados para el framework identificado
- `generar_commit` - Mejora scope y contexto de commits basado en componentes
- `analizar_code_smells` - Aplica reglas específicas del stack tecnológico

**Herramientas de análisis externas:**
- **SonarQube:** Análisis estático de código complementario
- **CLOC:** Conteo de líneas de código para métricas
- **Dependency-Check:** Análisis de vulnerabilidades en dependencias
- **Architecture Decision Records (ADR):** Documentación de decisiones

### Limitaciones Conocidas

- **Acceso filesystem:** Requiere permisos de lectura, no funciona con APIs remotas
- **Proyectos encriptados:** No puede analizar código ofuscado o encriptado
- **Monorepos complejos:** Puede requerir configuración manual del scope de análisis
- **Dependencias privadas:** No resuelve dependencias no públicas o corporativas
- **Configuración runtime:** No analiza configuración que se determina en tiempo de ejecución
- **Análisis dinámico:** Solo análisis estático, no ejecuta código ni pruebas

### Consideraciones de Rendimiento

**Proyectos por tamaño:**
- **Pequeños (<1K archivos):** Análisis completo en 1-2 minutos
- **Medianos (1K-10K archivos):** 3-5 minutos con sampling inteligente
- **Grandes (>10K archivos):** 5-15 minutos con análisis selectivo
- **Enterprise (>100K archivos):** Requiere configuración de directorios principales

**Optimizaciones aplicadas:**
- **Muestreo selectivo:** En proyectos grandes, analiza solo directorios principales
- **Cache de patterns:** Reutiliza detección de patrones entre ejecuciones
- **Parsing lazy:** Solo parsea archivos de dependencias cuando es necesario
- **Skip binaries:** Ignora automáticamente archivos binarios y compilados

### Casos de Uso Recomendados

**Onboarding de desarrolladores:**
- Nuevo miembro del equipo necesita entender proyecto rápidamente
- Consultor externo requiere assessment inicial de codebase
- Documentación técnica desactualizada o inexistente

**Auditorías y assessments:**
- Due diligence técnica para acquisiciones
- Evaluación de legacy systems para modernización
- Compliance checks para estándares arquitectónicos

**Integración en workflows:**
- Pre-requisito automático para otras herramientas del sistema
- Parte de onboarding automation en nuevos repositorios
- Análisis periódico para detectar drift arquitectónico

### Futuras Mejoras

**Análisis más profundo:**
- **ML-powered pattern detection:** Machine learning para patrones arquitectónicos complejos
- **Semantic analysis:** Análisis semántico de nombres y estructura de código
- **Performance insights:** Detección de anti-patterns de performance
- **Security patterns:** Identificación de patrones de seguridad implementados

**Integraciones extendidas:**
- **IDE plugins:** Integración directa con VS Code, IntelliJ, Eclipse
- **CI/CD hooks:** Ejecución automática en pipelines de integración
- **Dashboard web:** Interface visual para visualizar contexto de múltiples proyectos
- **API REST:** Exposición de análisis como servicio para herramientas externas

### Formato del Archivo de Contexto

**Estándar markdown estructurado:**
- Secciones numeradas para consistencia
- Metadata al inicio para trazabilidad
- Nivel de confianza por sección para transparency
- Formato consumible por otras herramientas del sistema

**Versionado y evolución:**
- El archivo se actualiza preservando historial en sección 8
- Compatible con futuras versiones de la herramienta
- Extensible para nuevos tipos de análisis

### Mejores Prácticas de Uso

**Frecuencia de ejecución:**
- **Inicial:** Al comenzar trabajo en nuevo proyecto
- **Cambios arquitectónicos:** Después de refactorings significativos
- **Periódico:** Mensual o trimestral para proyectos en desarrollo activo
- **Pre-deliveries:** Antes de entregas importantes para documentación

**Combinación con otras herramientas:**
1. Ejecutar `tomar_contexto` como primer paso
2. Seguir con `diagnosticar_devops` para análisis de infraestructura
3. Usar `define_arquitectura` para documentar decisiones
4. Aplicar `analizar_code_smells` para mejorar calidad
5. Implementar `crear_pruebas` para completar coverage