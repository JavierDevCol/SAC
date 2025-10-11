# 🛠️ Herramienta: Creación de Pruebas

> El propósito de esta herramienta es generar código de pruebas (unitarias, integración, carga) de forma automática e inteligente, identificando casos felices, casos de borde y escenarios de error.

---

## 📋 Identificación

**Herramienta:** `crear_pruebas`

---

## 🎯 Objetivo

Diseñar y generar código para diferentes tipos de pruebas (unitarias, de integración, de carga) con generación automática inteligente, identificando casos felices, casos de borde y escenarios de error, asegurando la calidad y robustez del software.

---

## 📥 Entradas Requeridas (Contexto)

**Principal:**
- El contenido del archivo activo o el código seleccionado en el editor (#selection o #file) que contiene la clase o componente a probar.

**Secundario (Opcional):**
- Framework de testing específico del proyecto (detectado automáticamente o especificado).
- Convenciones de nomenclatura del proyecto.
- Requisitos de cobertura de código establecidos.
- Dependencias externas a mockear (repositorios, servicios, APIs).

---

## ⚙️ Parámetros del Usuario

| Parámetro | Tipo | Valores | Por Defecto | Descripción |
|-----------|------|---------|-------------|-------------|
| `tipo_test` | string | UNITARIO\|INTEGRACION\|CARGA\|AMBOS | UNITARIO | Tipo de prueba a generar |
| `framework_test` | string | junit5\|testcontainers | junit5 | Framework de testing preferido |
| `nivel_cobertura` | string | BASICO\|COMPLETO\|EXHAUSTIVO | COMPLETO | Nivel de exhaustividad de los tests |
| `generar_automatico` | boolean | true\|false | true | Generar scaffolding automático |
| `cobertura_objetivo` | number | 0-100 | 80 | Porcentaje de cobertura objetivo |

---

## 👥 Roles Autorizados

- ✅ `archdev_pro`

---

## 🔄 Proceso Paso a Paso

### 1️⃣ Análisis Automático del Código

- Analizar el código fuente proporcionado:
  - Identificar métodos públicos que requieren pruebas
  - Analizar parámetros, tipos de retorno y excepciones
  - Detectar dependencias para mocking (servicios, repositorios, APIs externas)
  - Calcular complejidad del código (paths, branches)

- Identificar casos de prueba automáticamente:
  - **Casos Felices (Happy Paths):** Parámetros válidos típicos, flujos principales de negocio, retornos esperados exitosos
  - **Casos de Borde (Edge Cases):** `null` en parámetros opcionales, colecciones vacías, valores límite, strings vacíos
  - **Casos de Error (Error Cases):** Excepciones declaradas, validaciones que pueden fallar, condiciones de negocio no cumplidas

- Presentar al usuario el análisis con formato estructurado:
  ```markdown
  📊 **Análisis Completado:**
  
  **Métodos a testear:** [N]
  - [lista de métodos]
  
  **Casos identificados:**
  - ✅ Casos felices: [N]
  - ⚠️ Casos de borde: [N]
  - ❌ Casos de error: [N]
  
  **Dependencias detectadas:**
  - [lista de dependencias a mockear]
  
  **Cobertura estimada:** [X]% líneas, [Y]% branches
  ```

### 2️⃣ Generación Automática de Scaffolding

- Generar clase de test con estructura completa:
  - Nomenclatura descriptiva: `[ClaseOriginal]Test`
  - Annotations correctas (@ExtendWith, @SpringBootTest según tipo)
  - Setup común en @BeforeEach
  - Declaración de mocks y subject under test

- Generar métodos de test con nombres descriptivos usando patrón: `should[Comportamiento]When[Condicion]()`

- Aplicar patrón AAA (Arrange-Act-Assert) en cada método de prueba con comentarios claros.

### 3️⃣ Generación por Tipo de Prueba

**Si tipo_test = UNITARIO:**
- Generar tests con JUnit 5 + Mockito + AssertJ
- Aislamiento completo con mocks de todas las dependencias
- Estructura con @ExtendWith(MockitoExtension.class)
- Tests de ejecución rápida (< 100ms por test)
- Incluir dependencias necesarias en comentario

**Si tipo_test = INTEGRACION:**
- Generar tests con Spring Boot Test + Testcontainers
- Usar dependencias reales en entorno controlado
- Configurar contenedor de BD (PostgreSQL, MySQL)
- Contexto Spring completo con @SpringBootTest
- Setup de datos inicial en @BeforeEach
- Incluir dependencias necesarias en comentario

**Si tipo_test = CARGA:**
- NO generar código directamente
- Proporcionar plan de pruebas estructurado con:
  - Objetivos de rendimiento (throughput, latencia, tasa de error)
  - Escenarios de carga (normal, pico, estrés)
  - Endpoints a probar con porcentajes de distribución
  - Métricas a monitorear
  - Configuración para JMeter o Gatling
  - Comandos para ejecutar las pruebas

**Si tipo_test = AMBOS:**
- Ejecutar el proceso para UNITARIO
- Ejecutar el proceso para INTEGRACION
- Generar ambos archivos de test

### 4️⃣ Revisión y Ajuste de Casos

- Presentar código generado al usuario de forma organizada
- Preguntar por escenarios adicionales específicos del dominio:
  - "¿Hay reglas de negocio específicas que deba validar?"
  - "¿Existen escenarios de seguridad o permisos a testear?"
  - "¿Necesitas tests para casos de concurrencia?"
- Ajustar tests según feedback recibido

### 5️⃣ Entrega y Validación

- Utilizar la herramienta #createFile para crear el archivo de prueba en la ruta correcta (src/test/java/...)
- Si el archivo ya existe, preguntar si sobrescribir o fusionar
- Proporcionar lista de verificación:
  - ✅ Todos los métodos públicos tienen al menos un test
  - ✅ Casos felices, borde y error cubiertos
  - ✅ Mocks configurados correctamente
  - ✅ Assertions claras y específicas
  - ✅ Nomenclatura consistente
- Informar al usuario de la acción completada y la ubicación del archivo generado
- Sugerir comando para ejecutar los tests: `mvn test` o `./gradlew test`

---

## ⚠️ Manejo de Errores y Casos Borde

| Situación | Acción |
|-----------|--------|
| El contexto no contiene una clase de Java válida | Informar al usuario y solicitar el código correcto |
| Una dependencia no puede ser mockeada (ej: clase final) | Informar al usuario y sugerir wrapper o spy |
| No se pueden identificar métodos públicos | Informar que la clase no tiene métodos testeables |
| El proyecto no tiene las dependencias de testing | Proporcionar las dependencias necesarias para agregar al pom.xml/build.gradle |
| tipo_test no es válido | Usar valor por defecto (UNITARIO) e informar al usuario |

---

## 📤 Formato de Salida Esperado

**Tipo principal:**
- Uno o dos archivos Java (.java) creados directamente en el sistema de archivos del proyecto en la ruta src/test/java/...
- Nomenclatura: `[NombreClase]Test.java` para unitarios, `[NombreClase]IntegrationTest.java` para integración

**Notificación:**
- Mensaje de confirmación en el chat con:
  - Ruta del archivo generado
  - Número de tests creados
  - Cobertura estimada
  - Comando para ejecutar

**Estructura del output para tests unitarios:**
```java
@ExtendWith(MockitoExtension.class)
class [Clase]Test {
    
    @Mock
    private [Dependencia] [dependencia];
    
    @InjectMocks
    private [Clase] [instancia];
    
    @Test
    void should[Comportamiento]When[Condicion]() {
        // Arrange
        [preparación de datos y mocks]
        
        // Act
        [ejecución del método]
        
        // Assert
        [verificaciones con assertThat]
        [verificaciones de interacciones con verify]
    }
    
    // ...más tests
}
```

**Estructura del output para tests de integración:**
```java
@SpringBootTest
@Testcontainers
@AutoConfigureTestDatabase(replace = Replace.NONE)
class [Clase]IntegrationTest {
    
    @Container
    static [Contenedor] [contenedor] = new [Contenedor]("[imagen]")
        .withDatabaseName("testdb");
    
    @Autowired
    private [Servicio] [servicio];
    
    @BeforeEach
    void setUp() {
        [limpieza de datos]
    }
    
    @Test
    void should[Comportamiento]When[Condicion]() {
        // Arrange
        [preparación de datos reales]
        
        // Act
        [ejecución del flujo completo]
        
        // Assert
        [verificaciones con assertThat]
    }
}
```

---

## 💡 Ejemplo de Uso

Para ver un ejemplo detallado de uso de esta herramienta, consulta:
📁 **Archivo de ejemplo:** `ejemplos/herramientas/crear_pruebas_ejemplo.md`

---

## 📚 Referencias y Notas

**Dependencias Maven para Tests Unitarios:**
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>5.5.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.assertj</groupId>
    <artifactId>assertj-core</artifactId>
    <version>3.24.2</version>
    <scope>test</scope>
</dependency>
```

**Dependencias Maven para Tests de Integración:**
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.19.1</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>postgresql</artifactId>
    <version>1.19.1</version>
    <scope>test</scope>
</dependency>
```

**Convenciones de Nomenclatura:**
- Tests unitarios: `[Clase]Test.java`
- Tests de integración: `[Clase]IntegrationTest.java`
- Métodos de test: `should[Comportamiento]When[Condicion]()`

**Limitaciones conocidas:**
- Solo soporta Java con Spring Boot actualmente
- Testcontainers requiere Docker instalado y corriendo
- Las pruebas de carga requieren herramientas externas (JMeter/Gatling)

**Comandos útiles:**
```bash
# Ejecutar todos los tests
mvn test

# Ejecutar solo tests unitarios
mvn test -Dtest="*Test"

# Ejecutar solo tests de integración
mvn test -Dtest="*IntegrationTest"

# Ver reporte de cobertura
mvn jacoco:report
```