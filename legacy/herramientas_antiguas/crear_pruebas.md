# 🛠️ Herramienta: Creación de Pruebas

> **Versión:** 2.1  
> **Fecha de Actualización:** 4 de enero de 2026  
> **Estado:** Activa - Reestructurada según plantilla estándar

---

## 📋 Identificación

**Herramienta:** `crear_pruebas`  
**Comando:** `crear-pruebas [archivo.java]`  
**Rol Propietario:** ArchDev Pro

---

## 🎯 Objetivo

Diseñar y generar código para diferentes tipos de pruebas (unitarias, de integración, de carga) con generación automática inteligente, identificando casos felices, casos de borde y escenarios de error, asegurando la calidad y robustez del software.
---

Debes de seguir todas las instrucciones de activación exactamente como se especifican. NUNCA rompas el personaje hasta que se te dé un comando de salida.

---

## 🔗 Integración con Otras Herramientas

### Herramientas que Invoca

*Esta herramienta funciona de manera independiente y no invoca otras herramientas del sistema.*

### Herramientas que la Invocan

| Herramienta/Rol | Cuándo | Propósito |
|-----------------|--------|-----------|
| **ArchDev Pro** | Después de crear/refactorizar código | Generar pruebas para validar el código nuevo o refactorizado |
| **`verifica_pruebas`** | Antes de validación | Puede sugerir ejecutar `crear_pruebas` si detecta cobertura insuficiente |
| **Usuario directo** | Cuando necesita tests | Creación manual de pruebas para código existente |

---

## 📥 Entradas Requeridas (Contexto)

**Parámetro requerido:**
- `archivo_java`: Código fuente Java a analizar para generar pruebas

**Ejemplo de uso:**
```
crear-pruebas UserService.java
crear-pruebas UserService.java --tipo=INTEGRACION
crear-pruebas --cobertura_objetivo=90 --nivel=EXHAUSTIVO
```

**Archivos requeridos:**
- `{{session_state_location}}` - Estado de sesión
- Código fuente Java a testear (archivo o contenido)

**Archivos que genera:**
- `src/test/java/[paquete]/[Clase]Test.java` - Tests unitarios
- `src/test/java/[paquete]/[Clase]IntegrationTest.java` - Tests de integración (si aplica)

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

**Paso 0 [CRÍTICO - OBLIGATORIO]:** 
Cargar y leer `{{session_state_location}}` y `{project-root}/.cochas/CONFIG_INIT.yaml` antes de continuar.

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

## 🔐 Restricciones

1. **Solo genera código Java** - No soporta otros lenguajes de programación
2. **Requiere código válido** - El código fuente debe compilar correctamente
3. **No ejecuta tests** - Solo genera el código, la ejecución es responsabilidad del usuario
4. **Dependencias deben existir** - Asume que las dependencias de testing están configuradas
5. **Docker requerido para integración** - Testcontainers necesita Docker corriendo
6. **No modifica código de producción** - Solo genera archivos en `src/test/`

---

## 📊 Métricas Sugeridas

Trackear en `{{session_state_location}}`:

| Métrica | Descripción |
|---------|-------------|
| tests_generados_total | Total de archivos de test generados |
| tests_unitarios_generados | Total de tests unitarios creados |
| tests_integracion_generados | Total de tests de integración creados |
| metodos_test_promedio | Promedio de métodos de test por archivo |
| cobertura_estimada_promedio | % de cobertura estimada promedio |
| tiempo_promedio_generacion | Tiempo promedio para generar tests |

---

## 🔄 Actualización de Session State

### Registro de Eventos

**Al generar tests:**

```json
{
  "timestamp": "[timestamp_actual]",
  "rol": "ArchDev Pro",
  "herramienta": "crear_pruebas",
  "tipo": "tests_generados",
  "detalle": "Clase: [NombreClase] - Tipo: [UNITARIO|INTEGRACION] - Tests: [N] - Cobertura estimada: [X]%"
}
```

**Actualizar registro de tests en session_state:**

```json
{
  "ultimo_test_generado": {
    "timestamp": "[timestamp]",
    "clase_testeada": "[NombreClase].java",
    "archivo_test": "src/test/java/[paquete]/[NombreClase]Test.java",
    "tipo": "[UNITARIO|INTEGRACION]",
    "metodos_generados": [N],
    "cobertura_estimada": [X]
  }
}
```

**Actualizar metadata:**
- Incrementar `metadata.total_artefactos_generados`
- Actualizar `metadata.ultima_actividad`

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

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | - | Versión inicial básica |
| 2.0 | - | ✅ Proceso estructurado de 5 pasos<br>✅ Soporte para unitarios, integración y carga<br>✅ Análisis automático de código<br>✅ Patrón AAA documentado |
| 2.1 | 2026-01-04 | ✅ Integración con placeholders y session_state<br>✅ Paso 0 crítico obligatorio<br>✅ Secciones de Restricciones y Métricas<br>✅ Registro de eventos en log<br>✅ Comando en Identificación |