# Herramienta: tomar_contexto

## Objetivo
(Ver descripción en Contenido Original.)

## Entradas Requeridas (Contexto)
(No estructuradas explícitamente en el original.)

## Parámetros del Usuario
(No definidos en el original.)

## Roles Autorizados
(No definidos en el original; herramienta fundamental.)

## Proceso Paso a Paso
(Descrito en Contenido Original en Fases.)

## Manejo de Errores y Casos Borde
(Implícito en el análisis; no especificado explícitamente.)

## Formato de Salida Esperado
Archivo `artefactos/contexto_proyecto.md` siguiendo plantilla incluida.

---

## Contenido Original

### Herramienta Fundamental: Toma de Contexto del Proyecto (Comando: `tomar-contexto`)

*Esta es una herramienta de análisis profundo que se ejecuta para obtener un entendimiento completo de un proyecto de software. Puede ser activada manualmente o como parte del comportamiento por defecto de una personalidad al iniciar una conversación en un nuevo entorno.*

#### **Fase 1: Análisis Estático (Bottom-Up) - Los Hechos**

El objetivo de esta fase es recolectar datos objetivos del código fuente y los archivos de configuración sin ejecutar nada.

1.  **Identificación del Ecosistema:**
    * Buscará archivos de gestión de dependencias para identificar el lenguaje y el gestor principal:
        * `pom.xml` -> **Java / Maven**.
        * `build.gradle` o `build.gradle.kts` -> **Java o Kotlin / Gradle**.
        * `package.json` -> **JavaScript o TypeScript / NPM o Yarn**.
        * `go.mod` -> **Go**.
        * `pyproject.toml` o `requirements.txt` -> **Python**.
    * Si no encuentra ninguno, lo notificará.

2.  **Análisis del Gestor de Dependencias:**
    * **Lectura Profunda:** Parseará el archivo (`pom.xml` o `build.gradle`).
    * **Extracción de Dependencias Clave:** Identificará frameworks (`spring-boot-starter-web`), librerías de base de datos (`spring-data-jpa`, `postgresql`), herramientas de prueba (`junit`, `mockito`), etc.
    * **Identificación de Comandos:** Analizará los plugins (Maven) y tareas (Gradle) configurados para inferir comandos comunes como `mvn clean install`, `mvn spring-boot:run`, `gradlew build`, `gradlew test`, etc.

3.  **Análisis de la Estructura de Directorios:**
    * Buscará patrones de nomenclatura en los paquetes/directorios para inferir la arquitectura:
        * Paquetes `domain`, `application`, `infrastructure` -> Fuerte indicio de **Arquitectura Hexagonal / Limpia**.
        * Paquetes `controller`, `service`, `repository`, `model` -> Fuerte indicio de **Arquitectura en Capas / MVC**.
        * Presencia de `events`, `consumer`, `producer`, `kafka` -> Fuerte indicio de **Arquitectura Orientada a Eventos (EDA)**.
    * Identificará la ubicación de los tests (`src/test/...`) y el código fuente (`src/main/...`).

#### **Fase 2: Análisis Conceptual (Top-Down) - El Propósito**

1.  **Revisión del `README.md`:**
    * **Lectura Completa:** Leerá el archivo `README.md` si existe, buscando secciones clave como "Propósito del Proyecto", "Stack Tecnológico", "Cómo Empezar", "Variables de Entorno", etc.
    * **Evaluación de Calidad:** Determinará si el `README.md` está completo o es "pobre" (si carece de las secciones mencionadas).

#### **Fase 3: Síntesis y Generación de Artefactos**

1.  **Creación del `contexto_proyecto.md`:**
    * Creará un nuevo archivo llamado `contexto_proyecto.md` en la raíz del proyecto.
    * Volcará toda la información recolectada en las Fases 1 y 2 en este archivo, usando una estructura clara y seccionada (ver plantilla de artefacto).

2.  **Interacción con el Usuario sobre el `README.md`:**
    * **Si `README.md` no existe:** Preguntará al usuario: "He notado que este proyecto no tiene un archivo `README.md`. Con el contexto que he recolectado, ¿te gustaría que genere una primera versión para documentar el proyecto?"
    * **Si `README.md` es pobre:** Preguntará al usuario: "He analizado el `README.md` existente y creo que podría enriquecerse con más detalles sobre el stack tecnológico y los comandos de ejecución. ¿Te gustaría que lo actualice con la información que he descubierto?"

---

### `artefactos/contexto_proyecto.md`

Esta es la plantilla del archivo que se generará como resultado del análisis.

```md
# Contexto del Proyecto: [Nombre del Proyecto Ingerido]

> **Último Análisis:** [Fecha y Hora del Análisis]
> **Analizado por:** [Nombre del Rol/Personalidad, ej: Onad]

## 1. Resumen del Proyecto

*[Esta sección se rellena a partir del `README.md` o se deja como "Pendiente de definir" si no hay información. Describe el propósito de negocio del software en 1-2 párrafos.]*

---

## 2. Stack Tecnológico

- **Lenguaje Principal:** [Ej: Java 17]
- **Framework Principal:** [Ej: Spring Boot 3.1.5]
- **Base de Datos:** [Ej: PostgreSQL, Redis (caché)]
- **Framework de Pruebas:** [Ej: JUnit 5, Mockito]
- **Contenerización:** [Ej: Docker detectado a través de Dockerfile]

---

## 3. Gestión y Comandos

- **Gestor de Dependencias:** [Ej: Gradle]
- **Comandos Clave:**
  - `gradlew build`: Compila el proyecto y ejecuta los tests.
  - `gradlew clean`: Elimina los artefactos de compilación.
  - `gradlew test`: Ejecuta las pruebas unitarias y de integración.
  - `java -jar build/libs/{nombre-artefacto}.jar`: Ejecuta la aplicación compilada.

---

## 4. Arquitectura y Patrones

- **Estilo Arquitectónico Detectado:** [Ej: Arquitectura Hexagonal (Puertos y Adaptadores). Se han detectado paquetes claros de `domain`, `application` e `infrastructure`.]
- **Patrones de Diseño Recurrentes:**
  - Patrón Repositorio para la persistencia de datos.
  - Inyección de Dependencias (gestionado por Spring).
  - [Otro patrón detectado, ej: Patrón Strategy en el módulo de cálculo de precios.]

---

## 5. Componentes Clave

- **Clases Core del Dominio:**
  - `[Ej: com.empresa.proyecto.domain.model.Pedido]`
  - `[Ej: com.empresa.proyecto.domain.model.Cliente]`
- **Puntos de Entrada (Entrypoints):**
  - `[Ej: com.empresa.proyecto.infrastructure.rest.PedidoController]` (API REST)
- **Clase Principal de la Aplicación:**
  - `[Ej: com.empresa.proyecto.Application]`

---

## 6. Integraciones Externas

- **APIs Consumidas:**
  - Servicio de Pagos: `POST https://api.pagos.com/v1/pagar`
- **Mensajería / Eventos:**
  - Publica el evento `PedidoCreado` en el topic de Kafka `pedidos.nuevos`.

---

## 7. Historial de Cambios Relevantes

*[Esta sección es actualizada por el rol/personalidad cuando realiza cambios significativos que alteran el contexto del proyecto.]*

- **[Fecha] - [Nombre del Rol]:** Se refactorizó el `CalculadorDeImpuestos` para usar el Patrón Strategy, desacoplando las reglas de impuestos por país.