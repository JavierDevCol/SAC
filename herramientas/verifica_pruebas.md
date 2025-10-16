# 🛠️ Herramienta: Verificar Pruebas

> **Versión:** 2.0  
> **Fecha de Actualización:** 10 de octubre de 2025  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `verifica_pruebas`

---

## 🎯 Objetivo

Ejecutar, analizar y corregir automáticamente las pruebas unitarias de un proyecto, identificando fallos y aplicando las correcciones necesarias para garantizar la calidad del código. Optimiza el ciclo de desarrollo mediante la detección temprana de errores y la corrección inteligente de casos de prueba.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

| Herramienta | Cuándo se Invoca | Propósito |
|-------------|------------------|-----------|
| **`tomar_contexto`** | Al inicio de la verificación (opcional) | Obtener información del proyecto (gestor de build, framework de pruebas, comandos) |
| **`crear_pruebas`** | Cuando no existen pruebas o la cobertura es muy baja | Generar pruebas faltantes para mejorar la cobertura |

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **ArchDev Pro** | Después de cambios en código o refactoring | Validar que los cambios no rompieron las pruebas existentes |
| **`refactorizar`** | Al finalizar proceso de refactorización | Verificar que el código refactorizado pasa todas las pruebas |
| **Artesano de Commits** | Antes de realizar commits | Asegurar que las pruebas pasan antes de commitear cambios |
| **Arquitecto DevOps** | En pipelines CI/CD | Validación automática de pruebas en procesos de integración continua |

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- Ruta del proyecto o repositorio donde se ejecutarán las pruebas
- Acceso al sistema de build (Gradle, Maven) para ejecutar comandos de test

**Secundario (Opcional):**
- Paquete específico o clase de prueba a verificar (si no se quieren ejecutar todas)
- Configuración de entorno de pruebas (variables, perfiles, bases de datos de test)
- Umbral de cobertura mínima esperada
- Archivos de configuración de pruebas (application-test.properties, test containers)
- Contexto de cambios recientes para focalizar la verificación

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `alcance_pruebas` | string | todas\|paquete\|clase | todas | Ejecutar todas las pruebas o filtrar por paquete/clase específica |
| `modo_correccion` | string | interactivo\|autonomo\|solo_reporte | interactivo | Estrategia para manejar fallos detectados |
| `umbral_fallos` | number | 1-10 | 3 | Número máximo de fallos antes de cambiar a modo autónomo |
| `incluir_cobertura` | boolean | true\|false | true | Analizar cobertura de código además de ejecución |
| `detener_primer_fallo` | boolean | true\|false | false | Parar ejecución al primer fallo encontrado |
| `generar_reporte` | boolean | true\|false | true | Crear reporte detallado de resultados |
| `aplicar_correcciones` | boolean | true\|false | true | Permitir que la herramienta aplique correcciones automáticas |

---

## 👥 Roles Autorizados

- ✅ **ArchDev Pro** (uso principal - integración con flujos de desarrollo y refactoring)
- ✅ **Arquitecto DevOps** (verificación de pruebas en pipelines CI/CD)
- ✅ **Refinador HU** (validación de criterios de aceptación mediante pruebas)
- ✅ **Artesano de Commits** *(para verificar pruebas antes de commits)*

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Configuración Inicial y Validación

- **Análisis automático del contexto del proyecto:**
  - Verificar si existe `artefactos/contexto_proyecto.md` en la raíz del proyecto
  - Si existe, extraer información relevante:
    - **Gestor de Dependencias:** (Gradle/Maven) de la sección "Gestión y Comandos"
    - **Comandos de prueba:** Comandos específicos para ejecutar tests
    - **Stack Tecnológico:** Framework de pruebas utilizado (JUnit 4/5, TestNG, etc.)
    - **Estructura del proyecto:** Ubicación de las pruebas y convenciones
    - **Dependencias de test:** Librerías como Mockito, Spring Test, etc.

- **Si no existe contexto_proyecto.md, solicitar información al usuario:**
  - **Sistema de build:** "¿Tu proyecto usa Gradle o Maven?"
  - **Comando de pruebas:** "¿Cuál es el comando para ejecutar las pruebas? (ej: ./gradlew test, mvn test)"
  - **Framework de pruebas:** "¿Qué framework de pruebas usa el proyecto? (JUnit 5, JUnit 4, TestNG)"
  - **Ubicación de pruebas:** "¿Dónde están ubicadas las pruebas? (src/test/java, test/, etc.)"

- **Verificar entorno de trabajo:**
  - Confirmar que existe el archivo de build correspondiente (build.gradle, pom.xml)
  - Validar que las herramientas necesarias están disponibles (Java, Gradle/Maven)
  - Verificar acceso a la carpeta de pruebas identificada
  - Comprobar que los comandos de prueba son ejecutables

- **Establecer configuración de ejecución:**
  - Confirmar alcance de pruebas a ejecutar (todas, paquete específico, clase específica)
  - Configurar modo de corrección según los parámetros del usuario
  - Definir umbrales y opciones de reporte basado en el contexto disponible

### 2️⃣ Ejecución de Pruebas

- **Ejecutar comando de pruebas según el gestor de dependencias:**
  - Gradle: `./gradlew test` o `./gradlew test --tests [filtro]`
  - Maven: `mvn test` o `mvn test -Dtest=[filtro]`
  - Capturar tanto la salida estándar como los errores

- **Recopilar métricas de ejecución:**
  - Número total de pruebas ejecutadas
  - Pruebas exitosas vs fallidas
  - Tiempo total de ejecución
  - Cobertura de código (si `incluir_cobertura=true`)

### 3️⃣ Análisis de Resultados

- **Clasificar tipos de fallos detectados:**
  - **Fallos de aserción:** Expectativas no cumplidas en el código
  - **Errores de configuración:** Problemas de setup/teardown, mocks mal configurados
  - **Excepciones no controladas:** RuntimeException, NullPointerException, etc.
  - **Problemas de dependencias:** Beans no encontrados, autowiring fallido
  - **Timeouts:** Pruebas que exceden tiempo límite

- **Evaluar estrategia de corrección según número de fallos:**
  - **≤ umbral_fallos:** Activar modo interactivo (mostrar cada fallo individualmente)
  - **> umbral_fallos:** Activar modo autónomo (corregir automáticamente patrones conocidos)

### 4️⃣ Corrección de Fallos (Modo Interactivo)

- **Para cada fallo detectado:**
  - Mostrar descripción del error y stacktrace relevante
  - Analizar el código de la prueba y identificar causa probable
  - Proponer solución específica con justificación
  - Solicitar confirmación del usuario antes de aplicar cambios
  - Aplicar corrección y re-ejecutar esa prueba específica para validar

### 5️⃣ Corrección Automática (Modo Autónomo)

- **Aplicar patrones de corrección conocidos:**
  - **Imports faltantes:** Agregar imports necesarios automáticamente
  - **Anotaciones incorrectas:** Corregir @Test, @Mock, @InjectMocks mal aplicadas
  - **Setup de mocks:** Configurar comportamiento básico de mocks cuando falta
  - **Asserts comunes:** Corregir assertEquals vs assertThat mal usados
  - **Limpieza de recursos:** Agregar @AfterEach para cleanup si es necesario

- **Registrar todas las correcciones aplicadas para el reporte final**

### 6️⃣ Verificación Final y Reporte

- **Re-ejecutar suite completo de pruebas después de correcciones**
- **Generar reporte comprehensivo con:**
  - Resumen de ejecución (antes/después de correcciones)
  - Lista detallada de fallos encontrados y corregidos
  - Métricas de cobertura (si aplicable)
  - Recomendaciones para mejoras futuras
  - Tiempo total invertido en correcciones

- **Confirmar estado final:** Todas las pruebas pasan o quedan fallos manuales pendientes

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| Archivo `contexto_proyecto.md` corrupto o mal formateado | Advertir al usuario y solicitar información manualmente como fallback |
| Sistema de build no disponible (Gradle/Maven no instalado) | Informar requisitos faltantes y detener ejecución hasta que se resuelvan |
| Proyecto sin pruebas unitarias existentes | Sugerir usar herramienta `crear_pruebas` y ofrecer crear estructura básica de testing |
| Todas las pruebas fallan por problemas de configuración | Identificar problemas de setup (base de datos, properties) y sugerir correcciones de entorno |
| Pruebas cuelgan indefinidamente (timeout) | Terminar procesos colgados después de 5 minutos y reportar pruebas problemáticas |
| Dependencias de prueba faltantes en el build | Detectar imports sin resolver y sugerir dependencias necesarias (JUnit, Mockito, etc.) |
| Conflictos de versiones en frameworks de pruebas | Advertir sobre incompatibilidades detectadas y sugerir alineación de versiones |
| Código de producción con errores de compilación | Informar que las pruebas no pueden ejecutarse hasta resolver errores de compilación |
| Permisos insuficientes para modificar archivos de prueba | Solicitar permisos o ejecutar en modo solo-lectura (solo reporte) |
| Cobertura extremadamente baja (<10%) | Sugerir revisión de estrategia de testing y posible creación masiva de pruebas |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Reporte estructurado en formato Markdown con resultados de ejecución y correcciones aplicadas
- Estado final de las pruebas (exitoso/con fallos pendientes)

**Estructura del output:**
```
# 📊 Reporte de Verificación de Pruebas

## ✅ Resumen Ejecutivo
- **Total de pruebas:** 45 ejecutadas
- **Estado final:** ✅ Todas las pruebas pasan
- **Tiempo de ejecución:** 2m 34s
- **Correcciones aplicadas:** 3 automáticas, 1 manual

## 🔧 Correcciones Realizadas

### Automáticas
1. **UserServiceTest.java** - Agregado import faltante para `@MockBean`
2. **OrderServiceTest.java** - Corregido assert: `assertEquals` → `assertThat`
3. **PaymentServiceTest.java** - Configurado mock de `paymentGateway.process()`

### Manuales (Modo Interactivo)
1. **ProductServiceTest.java** - Actualizada lógica de validación de stock

## 📈 Métricas de Cobertura (si aplicable)
- **Cobertura total:** 87%
- **Líneas cubiertas:** 1,245 / 1,431
- **Métodos cubiertos:** 156 / 178

## 🎯 Recomendaciones
- Considerar agregar pruebas para el módulo de reportes (cobertura: 45%)
- Revisar timeouts en pruebas de integración con servicios externos
```

**Notificación de confirmación:**
- Resumen del estado final de las pruebas
- Número de correcciones aplicadas vs pendientes
- Tiempo total invertido en el proceso

**Tipos de salida según configuración:**
- **Solo reporte:** Análisis sin modificaciones de código
- **Reporte + correcciones:** Incluye cambios aplicados automáticamente
- **Reporte interactivo:** Incluye decisiones tomadas por el usuario

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/verifica_pruebas_ejemplo.md`

---

## 📚 Referencias y Notas

### Frameworks y Herramientas Soportados

**Gestores de Build:**
- **Gradle:** Soporte completo con `./gradlew test` y filtros específicos
- **Maven:** Soporte completo con `mvn test` y `-Dtest` parameters

**Frameworks de Testing:**
- **JUnit 5:** Detección y corrección de anotaciones (@Test, @BeforeEach, @Mock)
- **JUnit 4:** Compatibilidad con anotaciones legacy (@Before, @RunWith)
- **Mockito:** Configuración automática de mocks y verificaciones
- **Spring Boot Test:** Manejo de @MockBean, @TestConfiguration, @SpringBootTest

### Herramientas Complementarias

**Integración con otras herramientas del sistema:**
- `crear_pruebas` - Para generar pruebas cuando no existen o cobertura es muy baja
- `refactorizar` - Puede invocar `verifica_pruebas` después de cambios estructurales
- `analizar_code_smells` - Para identificar problemas en código de pruebas
- `tomar_contexto` - Proporciona el archivo `contexto_proyecto.md` necesario

**Herramientas externas compatibles:**
- **JaCoCo:** Para análisis detallado de cobertura de código
- **SonarQube:** Integración con métricas de calidad de pruebas
- **Testcontainers:** Soporte para pruebas de integración con contenedores

### Limitaciones Conocidas

- **Scope de corrección:** Solo corrige aspectos técnicos del testing, no lógica de negocio
- **Frameworks no soportados:** TestNG, Spock (Groovy), frameworks de JavaScript
- **Pruebas de integración:** Limitaciones con bases de datos externas y servicios remotos
- **Paralelización:** No optimiza ejecución paralela de pruebas automáticamente
- **Cobertura avanzada:** No genera reportes de mutación testing o cobertura de branches complejos

### Consideraciones de Rendimiento

- **Proyectos pequeños (<20 pruebas):** Ejecución típica < 30 segundos
- **Proyectos medianos (20-100 pruebas):** 1-3 minutos incluyendo correcciones
- **Proyectos grandes (>100 pruebas):** 3-10 minutos, considerar filtros por paquete
- **Memoria:** Requiere suficiente heap para compilación y ejecución de pruebas

### Patrones de Corrección Automática

**Imports y dependencias:**
- Auto-import de anotaciones JUnit/Mockito faltantes
- Detección de dependencias Maven/Gradle necesarias

**Configuración de mocks:**
- Setup básico de `when().thenReturn()` para mocks sin comportamiento
- Corrección de `@Mock` vs `@MockBean` según contexto Spring

**Assertions modernas:**
- Migración de `assertEquals` a `assertThat` para objetos complejos
- Corrección de orden de parámetros (expected, actual)
- Uso de AssertJ para assertions más expresivas

### Futuras Mejoras

- **Análisis de mutación:** Integración con PIT para mutation testing
- **Pruebas de performance:** Detección de pruebas lentas y sugerencias de optimización
- **Generación inteligente:** Auto-generación de pruebas faltantes basada en código de producción
- **Integración CI/CD:** Plugin para pipelines que ejecute verificación automática
- **Soporte multi-lenguaje:** Extensión a Kotlin, Groovy y otros lenguajes JVM

### Casos de Uso Recomendados

**Flujo de desarrollo típico:**
1. **Post-refactoring:** Verificar que cambios no rompieron pruebas existentes
2. **Pre-commit:** Validar estado de pruebas antes de commit
3. **Code review:** Asegurar calidad de pruebas en nuevas funcionalidades
4. **Mantenimiento:** Limpieza periódica de pruebas obsoletas o mal configuradas

**Integración con metodologías:**
- **TDD:** Verificación rápida de ciclo red-green-refactor
- **BDD:** Validación de criterios de aceptación implementados como pruebas
- **Continuous Integration:** Ejecución automática en pipelines de CI/CD