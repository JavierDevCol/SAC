# 📝 Ejemplo de Uso: Herramienta verifica_pruebas

> **Herramienta:** `verifica_pruebas`  
> **Fecha del ejemplo:** 10 de octubre de 2025  
> **Escenario:** Verificación de pruebas en un proyecto Spring Boot con fallos detectados

---

## 🔍 Contexto del Ejemplo

**Situación:** Un desarrollador ha refactorizado código de un servicio de e-commerce y necesita verificar que todas las pruebas unitarias sigan funcionando correctamente después de los cambios.

**Estado del proyecto:**
- **Framework:** Spring Boot 3.1.5 con Java 17
- **Testing:** JUnit 5 + Mockito + Spring Boot Test
- **Build:** Gradle 8.0
- **Módulos afectados:** UserService, OrderService, PaymentService

---

## 📥 Entrada Proporcionada

### Contexto del Proyecto Detectado:
```markdown
# Archivo: artefactos/contexto_proyecto.md (fragmento relevante)

## 2. Stack Tecnológico
- **Lenguaje Principal:** Java 17
- **Framework Principal:** Spring Boot 3.1.5
- **Framework de Pruebas:** JUnit 5, Mockito, Spring Boot Test

## 3. Gestión y Comandos
- **Gestor de Dependencias:** Gradle
- **Comandos Clave:**
  - `./gradlew test`: Ejecuta las pruebas unitarias y de integración
  - `./gradlew test --tests com.ecommerce.service.*`: Ejecuta pruebas de servicios específicos
```

### Parámetros Seleccionados:
- **alcance_pruebas:** todas
- **modo_correccion:** interactivo  
- **umbral_fallos:** 3
- **incluir_cobertura:** true
- **generar_reporte:** true
- **aplicar_correcciones:** true

---

## 🔄 Procesamiento Paso a Paso

### Paso 1: Configuración Inicial
✅ **Contexto detectado automáticamente:**
- Sistema de build: Gradle (detectado de contexto_proyecto.md)
- Comando de pruebas: `./gradlew test`
- Framework: JUnit 5 + Mockito
- Ubicación de pruebas: `src/test/java`

✅ **Verificación del entorno:**
- ✅ `build.gradle` encontrado
- ✅ Gradle disponible (versión 8.0)
- ✅ Java 17 configurado
- ✅ Carpeta `src/test/java` accesible

### Paso 2: Ejecución Inicial
```bash
$ ./gradlew test

> Task :test FAILED

BUILD FAILED in 45s

Tests completed: 42, failed: 5, skipped: 2
Test failures:
- UserServiceTest > testCreateUser() FAILED
- UserServiceTest > testValidateEmail() FAILED  
- OrderServiceTest > testCalculateTotal() FAILED
- PaymentServiceTest > testProcessPayment() FAILED
- PaymentServiceTest > testValidateCard() FAILED
```

### Paso 3: Análisis de Resultados
**Fallos detectados:** 5 fallos (> umbral de 3)
**Estrategia:** Cambiar a modo autónomo para corrección automática

**Clasificación de errores:**
- **3 fallos de importación:** Imports faltantes después del refactoring
- **1 fallo de aserción:** AssertEquals mal usado
- **1 fallo de configuración de mock:** Mock no configurado correctamente

### Paso 4: Modo Autónomo - Correcciones Aplicadas

#### Corrección 1: UserServiceTest.java
**Problema detectado:**
```java
// Error: import faltante
@MockBean
private EmailValidator emailValidator; // Cannot resolve symbol 'MockBean'
```

**Corrección aplicada:**
```java
+ import org.springframework.boot.test.mock.mockito.MockBean;

@MockBean
private EmailValidator emailValidator;
```

#### Corrección 2: UserServiceTest.java  
**Problema detectado:**
```java
// Error: Assert deprecated
assertEquals(user.getEmail(), "test@example.com");
// Warning: assertEquals(actual, expected) - argumentos invertidos
```

**Corrección aplicada:**
```java
- assertEquals(user.getEmail(), "test@example.com");
+ assertEquals("test@example.com", user.getEmail());
```

#### Corrección 3: OrderServiceTest.java
**Problema detectado:**
```java
// Error: Assert no recomendado para objetos complejos
assertEquals(expectedOrder, actualOrder);
// Objects should be compared using assertThat()
```

**Corrección aplicada:**
```java
+ import static org.assertj.core.api.Assertions.assertThat;

- assertEquals(expectedOrder, actualOrder);
+ assertThat(actualOrder)
+     .usingRecursiveComparison()
+     .isEqualTo(expectedOrder);
```

#### Corrección 4 & 5: PaymentServiceTest.java
**Problema detectado:**
```java
// Error: Mock sin comportamiento configurado
@Mock
private PaymentGateway paymentGateway;

// Test falla porque el mock retorna null por defecto
PaymentResult result = paymentService.processPayment(request);
```

**Corrección aplicada:**
```java
@BeforeEach
void setUp() {
+     // Configurar comportamiento básico del mock
+     when(paymentGateway.process(any(PaymentRequest.class)))
+         .thenReturn(PaymentResult.success("TXN-123"));
+     
+     when(paymentGateway.validateCard(any(CreditCard.class)))
+         .thenReturn(true);
}
```

### Paso 5: Verificación Final
```bash
$ ./gradlew test

BUILD SUCCESSFUL in 38s

Tests completed: 47, failed: 0, skipped: 2
Coverage: 87.3% (1,245 of 1,426 lines covered)
```

---

## 📤 Salida Generada

### Reporte Completo:
```markdown
# 📊 Reporte de Verificación de Pruebas

## ✅ Resumen Ejecutivo
- **Total de pruebas:** 47 ejecutadas (2 skipped por @Disabled)
- **Estado final:** ✅ Todas las pruebas activas pasan
- **Tiempo de ejecución:** 38s (mejora de 7s después de correcciones)
- **Correcciones aplicadas:** 5 automáticas

## 🔧 Correcciones Realizadas

### Automáticas (Modo Autónomo)
1. **UserServiceTest.java** - Agregado import `@MockBean` de Spring Boot Test
2. **UserServiceTest.java** - Corregido orden de parámetros en `assertEquals`
3. **OrderServiceTest.java** - Migrado de `assertEquals` a `assertThat` para objetos complejos
4. **PaymentServiceTest.java** - Configurado mock `PaymentGateway.process()`
5. **PaymentServiceTest.java** - Configurado mock `PaymentGateway.validateCard()`

## 📈 Métricas de Cobertura
- **Cobertura total:** 87.3% ⬆️ (+2.1% vs anterior)
- **Líneas cubiertas:** 1,245 / 1,426
- **Métodos cubiertos:** 189 / 203
- **Clases cubiertas:** 23 / 25

### Distribución por Módulo:
- **UserService:** 94% ✅
- **OrderService:** 91% ✅  
- **PaymentService:** 89% ✅
- **ReportService:** 45% ⚠️ (necesita atención)

## 🎯 Recomendaciones
- ✅ **Completado:** Todas las pruebas críticas funcionan correctamente
- ⚠️ **Atención:** ReportService tiene baja cobertura (45%)
- 💡 **Sugerencia:** Considerar usar `crear_pruebas` para generar tests del módulo de reportes
- 🔧 **Mantenimiento:** 2 pruebas están marcadas como @Disabled - revisar si siguen siendo relevantes

## ⏱️ Métricas de Rendimiento
- **Tiempo total del proceso:** 2m 15s
- **Tiempo de análisis:** 12s
- **Tiempo de correcciones:** 8s
- **Re-ejecución final:** 38s
```

### Notificación Final:
```
🎉 Verificación completada exitosamente!

✅ Estado: Todas las pruebas pasan
🔧 Correcciones: 5 aplicadas automáticamente
📊 Cobertura: 87.3% (objetivo: >80%)
⏱️ Tiempo total: 2m 15s

¿Deseas revisar el reporte detallado o proceder con el commit de los cambios?
```

---

## 🔄 Variaciones del Ejemplo

### Si hubiera elegido **Modo Interactivo** (≤3 fallos):
```
🔍 Fallo detectado en UserServiceTest.java (1/3):

Error: Missing import for @MockBean
Line 15: @MockBean private EmailValidator emailValidator;

💡 Solución sugerida:
Agregar: import org.springframework.boot.test.mock.mockito.MockBean;

¿Aplicar esta corrección? (s/n): _
```

### Si hubiera seleccionado **Solo Reporte** (`aplicar_correcciones=false`):
```markdown
# 📊 Análisis de Pruebas (Solo Lectura)

## ❌ Fallos Detectados: 5
1. UserServiceTest.java:15 - Import faltante @MockBean
2. UserServiceTest.java:32 - Argumentos invertidos en assertEquals
[... lista completa sin correcciones aplicadas ...]

## 📋 Plan de Corrección Sugerido
- Ejecutar nuevamente con `aplicar_correcciones=true`
- O aplicar manualmente las correcciones listadas
```

---

## 📚 Notas Adicionales

- **Tiempo de ejecución típico:** 1-3 minutos para proyectos medianos (40-60 pruebas)
- **Tipos de corrección automática:** Imports, anotaciones, asserts básicos, configuración de mocks
- **Límites de corrección:** No modifica lógica de negocio, solo aspectos técnicos del testing
- **Integración:** Se complementa perfectamente con `crear_pruebas` para pruebas faltantes y `refactorizar` para cambios de código